#!/bin/sh
set -eu
cd "$(dirname "$0")"
g++ -std=c++17 -O3 type_recursion.cpp -o type_recursion_exec
./type_recursion_exec 26 > type_recursion_replayed.txt
python3 independent_types.py 12 > independent_types_replayed.txt
diff -u type_recursion_output.txt type_recursion_replayed.txt
diff -u independent_types_output.txt independent_types_replayed.txt
printf 'VERIFIED: C++ finite-range result through 26 and independent Python result through 12 agree with recorded transcripts.\n'
rm -f type_recursion_exec type_recursion_replayed.txt independent_types_replayed.txt
