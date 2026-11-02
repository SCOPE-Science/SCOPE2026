#!/bin/sh
set -eu
python3 check_types.py
c++ -std=c++17 -O2 -Wall -Wextra -pedantic check_types.cpp -o check_types_local
./check_types_local
