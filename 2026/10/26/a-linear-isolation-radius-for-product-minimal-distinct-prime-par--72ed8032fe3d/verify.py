#!/usr/bin/env python3
"""Reproduce a finite exact-rational sanity check of the auxiliary inequality."""
from fractions import Fraction
from itertools import combinations
from math import prod

primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
maximum = (Fraction(0), ())
for k in range(2, 8):
    for subset in combinations(primes, k - 1):
        ratio = Fraction(k * sum(subset), prod(subset))
        assert ratio <= Fraction(5, 2), (k, subset, ratio)
        if ratio > maximum[0]:
            maximum = ratio, subset
assert maximum == (Fraction(5, 2), (2, 3))
print("VERIFY_OK", maximum)
