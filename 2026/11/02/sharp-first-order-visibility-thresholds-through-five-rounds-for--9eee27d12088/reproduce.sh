#!/bin/sh
set -eu
cd "$(dirname "$0")"
CXX="${CXX:-g++}"
"$CXX" -std=c++17 -O2 -Wall -Wextra -pedantic verify_incidence_types.cpp -o verify_incidence_types.bin
./verify_incidence_types.bin > .actual_cpp.out
python3 verify_incidence_types.py > .actual_py.out
python3 verify_direct_small.py > .actual_raw.out
diff -u verify_cpp.out .actual_cpp.out
diff -u verify_py.out .actual_py.out
diff -u verify_raw.out .actual_raw.out
rm -f .actual_cpp.out .actual_py.out .actual_raw.out verify_incidence_types.bin
printf 'REPRODUCTION_PASS\n'
