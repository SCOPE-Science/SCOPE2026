#!/usr/bin/env python3
"""Exact group-combinatorial checks for type-nine six-secant conics.

Requires only Python 3 and its standard library. Arithmetic is over
(Z/9Z)^2; no numerical geometry, coordinates, or random sampling occur.
"""
from collections import Counter
from math import comb

MOD = 9
T = [(a, b) for a in range(MOD) for b in range(MOD)
     if a % 3 != 0 or b % 3 != 0]
assert len(T) == 72
index = {p: i for i, p in enumerate(T)}

# Independently count six-element subsets with zero group sum.
ways = [[0] * 81 for _ in range(7)]
ways[0][0] = 1
for a, b in T:
    for n in range(6, 0, -1):
        for j, count in enumerate(ways[n - 1]):
            if count:
                x, y = divmod(j, 9)
                target = ((x + a) % 9) * 9 + (y + b) % 9
                ways[n][target] += count
N = ways[6][0]
assert N == 1_928_772

# Compute the same coefficient by character-order products.
# For characters of orders 1,3,9, multiplicities are 1,8,72.
coeff_trivial = comb(72, 6)
coeff_order3 = comb(14, 6) - 27 * comb(11, 3) + comb(27, 2)
coeff_order9 = comb(4, 2)
assert (coeff_trivial, coeff_order3, coeff_order9) == (
    156_238_908, -1_101, 6)
assert N * 81 == coeff_trivial + 8 * coeff_order3 + 72 * coeff_order9

# Every trisecant is an unordered zero-sum triple of distinct T elements.
triples = []
for i, (a, b) in enumerate(T):
    for j in range(i + 1, len(T)):
        c, d = T[j]
        k = index.get(((-a - c) % 9, (-b - d) % 9), -1)
        if k > j:
            triples.append((i, j, k))
assert len(triples) == 720
incidence = Counter(v for triple in triples for v in triple)
assert len(incidence) == 72 and set(incidence.values()) == {30}

# Disjoint unordered pairs of trisecants give exactly the reducible
# conics. Their six-element vertex supports must be unique.
mask = [sum(1 << v for v in tri) for tri in triples]
reducible = Counter()
for i, A in enumerate(mask):
    for B in mask[i + 1:]:
        if not A & B:
            reducible[A | B] += 1
assert len(reducible) == 227_520
assert sum(reducible.values()) == 227_520
assert set(reducible.values()) == {1}
red_per_point = Counter(v for support in reducible
                        for v in range(72) if support & (1 << v))
assert len(red_per_point) == 72
assert set(red_per_point.values()) == {18_960}

smooth = N - len(reducible)
assert smooth == 1_701_252
assert N * 6 == 72 * 160_731
assert smooth * 6 == 72 * 141_771
assert len(reducible) * 6 == 72 * 18_960
print('TYPE9_SIXSECANTS_GROUP_CHARACTER_AND_REDUCIBLE_COUNTS_OK')
print('points=72, trisecants=720, through_each=30')
print('conics_total=1928772, reducible=227520, smooth=1701252')
print('per_point_total=160731, reducible=18960, smooth=141771')
