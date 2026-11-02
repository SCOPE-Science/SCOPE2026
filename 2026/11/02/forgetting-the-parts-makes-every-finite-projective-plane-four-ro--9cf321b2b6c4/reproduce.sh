#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 verify_local.py > local_replayed.txt
diff -u local_output.txt local_replayed.txt
c++ -O3 -std=c++17 verify_ef.cpp -o verify_ef_replayed
./verify_ef_replayed > ef_replayed.txt
diff -u ef_output.txt ef_replayed.txt
printf 'PASS both verification programs reproduced their recorded outputs\n'
