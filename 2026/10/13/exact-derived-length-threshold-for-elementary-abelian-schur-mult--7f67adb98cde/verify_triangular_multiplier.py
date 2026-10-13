#!/usr/bin/env python3
"""Finite sanity checks for the triangular-rank criterion for abelian Schur multipliers.

For a p-primary abelian group with cyclic-factor exponents a_i>=1, the standard
formula gives multiplier cyclic factors p^{min(a_i,a_j)} over unordered pairs.
This script exhausts small exponent tuples and checks that an elementary-abelian
multiplier has rank binom(r,2), hence triangular. The theorem itself is symbolic.
"""
from itertools import product
from math import comb, isqrt

def multiplier_exponents(a):
    return [min(a[i], a[j]) for i in range(len(a)) for j in range(i+1, len(a))]

def triangular(k):
    d = 8*k + 1
    s = isqrt(d)
    return s*s == d and s % 2 == 1

checked = 0
for r in range(1, 8):
    for a in product(range(1, 5), repeat=r):
        exps = multiplier_exponents(a)
        elementary = all(e == 1 for e in exps)
        if elementary:
            k = len(exps)
            assert k == comb(r, 2)
            assert triangular(k)
            assert sum(x > 1 for x in a) <= 1
        checked += 1

for k in range(1, 101):
    by_square = triangular(k)
    by_rank = any(comb(r,2) == k for r in range(2, 30))
    assert by_square == by_rank

print(f"checked_exponent_tuples={checked}")
print("checked_k_range=1..100")
print("CHECK_OK")
