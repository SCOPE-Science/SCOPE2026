#!/usr/bin/env python3
"""Exact residue-cover certificate and independent gcd-period checks."""
from itertools import product
from math import gcd, prod

SMALL = (3, 5, 7)
# (small prime support, j, minimal uncovered at length eleven)
ROWS = (
    ((), 6, 11),
    ((3,), 8, 7),
    ((5,), 7, 8),
    ((7,), 6, 9),
    ((3, 5), 9, 5),
    ((3, 7), 8, 5),
    ((5, 7), 7, 6),
    ((3, 5, 7), 11, 3),
)

def min_uncovered(length, primes):
    minimum = length
    for residues in product(*(range(p) for p in primes)):
        covered = 0
        for prime, residue in zip(primes, residues):
            for index in range(residue, length, prime):
                covered |= 1 << index
        minimum = min(minimum, length - covered.bit_count())
    return minimum

for small, j, at11 in ROWS:
    budget = 5 - len(small)
    assert min_uncovered(j-1, small) == budget, (small, 'lower')
    assert min_uncovered(j, small) == budget+1, (small, 'upper')
    assert min_uncovered(11, small) == at11 > budget, (small, 'cutoff')
    assert set(small).issubset(SMALL)

REPRESENTATIVES = (
    ((2, 3, 5, 7, 11), 14),
    ((2, 3, 7, 11, 13), 12),
    ((2, 5, 7, 11, 13), 10),
    ((3, 5, 7, 11, 13), 11),
    ((3, 5, 11, 13, 17), 9),
    ((3, 7, 11, 13, 17), 8),
    ((5, 7, 11, 13, 17), 7),
    ((7, 11, 13, 17, 19), 6),
)
for primes, expected in REPRESENTATIVES:
    n = prod(primes)
    coprime = [k for k in range(n) if gcd(k, n) == 1]
    observed = max(b-a for a, b in zip(coprime, coprime[1:] + [coprime[0]+n]))
    assert observed == expected, (primes, observed, expected)
print('JACOBSTHAL_FIVE_SUPPORT_EXACT_OK small_supports=8 residue_tuples=192 full_periods=8')
