#!/usr/bin/env python3
"""Exhaustive classification of three-bit odd factor pairs below 2**23.

Requires only Python 3.8+ and the published global bound for the infinite claim.
"""
from math import isqrt
from itertools import combinations_with_replacement

BOUND = 1 << 23
EXPECTED = {
    (7, 7, 49),
    (7, 19, 133),
    (7, 37, 259),
    (11, 35, 385),
    (13, 21, 273),
    (21, 49, 1029),
}

# First route: enumerate all eligible factors by their exact three one-bit positions.
factors = sorted(1 + (1 << i) + (1 << j)
                 for j in range(2, 23) for i in range(1, j))
assert len(factors) == sum(range(1, 21+1)) == 231
assert len(set(factors)) == len(factors)
assert all(1 <= a < BOUND and a & 1 and a.bit_count() == 3 for a in factors)
first = set()
qualifying_factor_pairs = 0
for a, b in combinations_with_replacement(factors, 2):
    n = a * b
    if n >= BOUND:
        continue
    qualifying_factor_pairs += 1
    if n.bit_count() == 3:
        first.add((a, b, n))

# Second route: enumerate candidate *products*, then test all odd divisors.
# No reliance on the first route's factor table for deciding membership.
second = set()
products = sorted(1 + (1 << i) + (1 << j)
                  for j in range(2, 23) for i in range(1, j))
assert len(products) == 231
for n in products:
    for a in range(7, isqrt(n) + 1, 2):
        if a.bit_count() != 3 or n % a:
            continue
        b = n // a
        if b & 1 and b.bit_count() == 3:
            second.add((a, b, n))

assert first == second == EXPECTED, (sorted(first), sorted(second))
assert all(a <= b and a*b == n and
           a.bit_count() == b.bit_count() == n.bit_count() == 3 and
           (a&1) and (b&1) for a,b,n in EXPECTED)

print('PASS first-route factors:', len(factors))
print('PASS pairs with product below bound:', qualifying_factor_pairs)
print('PASS second-route products:', len(products))
print('PASS both independent routes agree on', len(EXPECTED), 'unordered pairs')
for a,b,n in sorted(EXPECTED):
    print(f'{a:4d} {b:4d} -> {n:5d} : {n:b}')
