#!/bin/sh
set -eu
cd "$(dirname "$0")"
g++ -std=c++17 -O2 verify_strict.cpp -o /tmp/strict_exact_verify_$$
trap 'rm -f /tmp/strict_exact_verify_$$ /tmp/strict_exact_cpp_$$ /tmp/strict_exact_py_$$' EXIT
/tmp/strict_exact_verify_$$ > /tmp/strict_exact_cpp_$$
python3 verify_strict.py > /tmp/strict_exact_py_$$
cmp /tmp/strict_exact_cpp_$$ /tmp/strict_exact_py_$$
cat /tmp/strict_exact_cpp_$$
