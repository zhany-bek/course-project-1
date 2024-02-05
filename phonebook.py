import os

# Check and create files:
def check_directory(filename: str):
    if filename not in os.listdir():
        with open(filename, 'w', encoding='utf-8') as data:
            data.write("")

# Option 1:
def read_all(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as data:
        result = data.read()
    return result

# Option 2:
def add_new_user(name: str, phone: str, filename: str):
    with open(filename, 'a+', encoding='utf-8') as data:
        data.seek(0)
        lines_count = len(data.readlines())
        data.write(f"{lines_count + 1};{name};{phone}\n")

# Option 3:
def search_user(data: str, filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    res_list = [line for line in lines if data in line.lower()]
    if res_list:
        return ''.join(res_list)
    else:
        return "Нет подходящих записей"

# Option 4:
def copy_line(line_num: str, filename: str, copy_filename: str):
    with open(filename, 'r', encoding='utf-8') as og_file:
        og_lines = og_file.readlines()
        if len(og_lines) < int(line_num) or int(line_num) <= 0:
            print("Нет такой строки")
            return
    for line in og_lines:
        if line.startswith(line_num + ';'):
            line_to_copy = line
            break
    with open(copy_filename, 'a+', encoding='utf-8') as copy_file:
        copy_file.seek(0)
        lines_count = len(copy_file.readlines())
        copy_file.write(f"{lines_count + 1};{line_to_copy.split(';', 1)[1]}")


INFO_STRING = """
    Выберите режим работы:
    1 - Вывести все данные
    2 - Добавление нового пользователя
    3 - Поиск
    4 - Копирование строки
"""

DATASOURCE = "phone.txt"
DATACOPY = "phone-copy.txt"
check_directory(DATASOURCE)
check_directory(DATACOPY)

while True:
    mode = int(input(INFO_STRING))

    if mode == 1:
        print(read_all(DATASOURCE))

    elif mode == 2:
        user = input("Имя: ")
        phone = input("Номер телефона: ")
        add_new_user(user, phone, DATASOURCE)

    elif mode == 3:
        search = input("Введите строку для поиска: ")
        print(search_user(search, DATASOURCE))

    elif mode == 4:
        line_num = input("Введите номер копируемой строки: ")
        copy_line(line_num, DATASOURCE, DATACOPY)
