#!/usr/bin/env python3
"""Exact integer checks for a prime-to-42 cobalancing square-window theorem."""
from math import gcd

LIMIT = 500
b = [0, 0]
B = [0, 1]
C = [1, 3]
for _ in range(2, LIMIT + 7):
    b.append(6*b[-1] - b[-2] + 2)
    B.append(6*B[-1] - B[-2])
    C.append(6*C[-1] - C[-2])
assert b[:7] == [0, 0, 2, 14, 84, 492, 2870]
assert B[6] == 6930 and C[6] == 19601

def co42(x):
    assert x > 0
    for p in (2, 3, 7):
        while x % p == 0:
            x //= p
    return x

def valuation(x, p):
    assert x > 0
    e = 0
    while x % p == 0:
        x //= p
        e += 1
    return e

examples = {}
for k in range(1, LIMIT+1):
    # All windows have the same fifth-order integer recurrence, so their
    # infinite GCD equals the GCD of these first five exact windows.
    d = 0
    for n in range(5):
        s = sum(b[i] * b[i] for i in range(n+1, n+k+1))
        d = gcd(d, s)
    target = gcd(5*k, gcd(B[k], C[k]-1))
    assert co42(d) == co42(target), ('prime-to-42',k,d,target)
    expected_v5 = (1 + valuation(k,5)) if k%6 == 0 else 0
    assert valuation(d,5) == expected_v5, ('prime-five',k,d,expected_v5)
    if k in (1,2,3,6,12,30,150):
        examples[k] = d
assert examples == {1:4,2:4,3:4,6:20,12:120,30:100,150:500}
print('VERIFY_OK lengths=500; exact five-window GCD; prime-to-42 identity; prime-five law')
print('Examples:', examples)
