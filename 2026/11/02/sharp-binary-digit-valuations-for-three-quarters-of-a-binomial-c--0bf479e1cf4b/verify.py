#!/usr/bin/env python3
"""Exact finite test of the two-adic digit-weight theorem."""
from math import comb

def v2(value):
    if value == 0:
        raise ValueError('zero has no finite 2-adic valuation')
    return (value & -value).bit_length()-1

s = 0
checked = 0
for n in range(1,1025):
    k = n-1
    s = 16*s+(3*k+1)*comb(2*k,k)**3
    if n % 4 == 0:
        continue
    predicted = 3*(n-1).bit_count() + (1 if n % 4 == 2 else 0)
    actual = v2(s)
    assert actual == predicted, (n, predicted, actual)
    checked += 1
assert checked == 768
print(f'VERIFY_OK cases={checked} max_n=1024')
