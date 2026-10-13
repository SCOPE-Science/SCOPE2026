#!/usr/bin/env python3
"""Finite exact checks for a dyadic valuation theorem; no external dependencies."""
from math import factorial

def v2(x):
    assert x != 0
    return (abs(x) & -abs(x)).bit_length() - 1

def normalized_tail_mod(u, extra=8):
    assert 3 <= u <= 14
    j = 1 << u
    r = j + u
    M = 1 << r
    base = M - r
    precision = 3*u + extra
    modulus = 1 << precision
    acc = 0
    # All excluded terms lie strictly above the stated precision.
    for k in range(M-j, M+precision+8):
        t = v2(k)
        d = k-t-base
        if d < precision:
            assert d >= 0
            acc = (acc + (1 << d)*pow(k >> t, -1, modulus)) % modulus
    assert acc != 0
    return v2(acc)

for u in range(3, 13):
    actual = normalized_tail_mod(u)
    predicted = 3*u-2
    assert actual == predicted, (u, actual, predicted)
    print(f"u={u} r={2**u+u} valuation_excess={actual}")

# Independent exact-integer recurrence at the smallest nontrivial index.
u = 3
r = 2**u+u
n = 2**r-2**u-1
a, fact = 0, 1
for k in range(1, n+1):
    x = k*a
    assert x % 2 == 0
    a = x//2 + fact
    fact *= k
assert v2(a) == 2**r-2*r+3*u-1
print(f"exact_recurrence_n={n} two_adic_valuation={v2(a)}")
print("VERIFY_OK; finite checks supplement the all-u proof")
