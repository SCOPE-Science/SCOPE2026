"""Supplementary exact finite tests for the weighted-shift power criterion.

The infinite-dimensional statements are proved analytically in RESULT.md;
finite tests below are diagnostic, not substitutes for those arguments.
"""
from fractions import Fraction as F
from math import prod
import random


def weight_a(k):
    return F(3, 2) if k == 0 else F(k, k + 1)


def weight_b(k):
    if k < 3:
        return F(9, 10)
    if k % 2:
        return F(1, 10)
    return F(1) - F(1, k // 2 + 3)


def block(weight, i, n):
    return prod((weight(j) for j in range(i, i+n)), start=F(1))

checks = 0
for n in range(2, 18):
    for i in range(1, 150):
        assert block(weight_a, i, n) == F(i, i + n)
        checks += 1
    assert block(weight_a, 0, n) == F(3, 2*n)
    checks += 1
for r in (0, 1):
    assert block(weight_b, r, 2) == F(81, 100)
    checks += 1
    for k in range(1, 150):
        assert block(weight_b, r+2*k, 2) <= F(1, 10)
        checks += 1
for k in range(2, 200):
    assert weight_b(2*k) == F(1)-F(1, k+3)
    checks += 1
# The arbitrary-weight block decomposition is verified coefficient-wise.
random.seed(20261009)
for trial in range(40):
    ws=[F(random.randint(1, 20), random.randint(1, 20)) for _ in range(42)]
    for n in range(1, 7):
        for r in range(n):
            for k in range((len(ws)-r)//n-1):
                i=r+n*k
                if i+n < len(ws):
                    original=prod(ws[i:i+n], start=F(1))
                    residue=prod((ws[r+n*k+j] for j in range(n)), start=F(1))
                    assert original == residue
                    checks += 1
print(f'PASS: {checks} exact rational checks (finite examples and residue blocks).')
