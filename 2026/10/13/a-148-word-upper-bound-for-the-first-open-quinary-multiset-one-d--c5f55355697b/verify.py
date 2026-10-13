#!/usr/bin/env python3
"""Standard-library exact rational certificate for a quinary multiset deletion bound."""
from collections import Counter
from fractions import Fraction

WEIGHTS = {
    (8, 0, 0, 0, 0): 420,
    (7, 1, 0, 0, 0): 200,
    (6, 2, 0, 0, 0): 220,
    (6, 1, 1, 0, 0): 108,
    (5, 3, 0, 0, 0): 200,
    (5, 2, 1, 0, 0): 120,
    (5, 1, 1, 1, 0): 96,
    (4, 4, 0, 0, 0): 220,
    (4, 3, 1, 0, 0): 100,
    (4, 2, 2, 0, 0): 180,
    (4, 2, 1, 1, 0): 84,
    (4, 1, 1, 1, 1): 57,
    (3, 3, 2, 0, 0): 140,
    (3, 3, 1, 1, 0): 136,
    (3, 2, 2, 1, 0): 72,
    (3, 2, 1, 1, 1): 111,
    (2, 2, 2, 2, 0): 204,
    (2, 2, 2, 1, 1): 54,
 }

def compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for v in range(total + 1):
            for tail in compositions(total - v, parts - 1):
                yield (v,) + tail

def canonical(v):
    return tuple(sorted(v, reverse=True))

X = list(compositions(9, 5))
Y = list(compositions(8, 5))
assert len(X) == 715 and len(Y) == 495
assert {canonical(y) for y in Y} == set(WEIGHTS)
assert sum(WEIGHTS[canonical(y)] for y in Y) == 62165
shadows = {}
for x in X:
    shadow = {tuple(x[j] - (j == i) for j in range(5))
              for i in range(5) if x[i] > 0}
    shadows[x] = shadow
    assert sum(WEIGHTS[canonical(y)] for y in shadow) >= 420
by_orbit = {canonical(x) for x in X}
assert len(by_orbit) == 23
weights_by_class = Counter(sum(i * x[i] for i in range(5)) % 5 for x in X)
assert all(weights_by_class[r] == 143 for r in range(5))
chosen = [x for x in X if sum(i * x[i] for i in range(5)) % 5 == 0]
seen = set()
for x in chosen:
    assert not (seen & shadows[x])
    seen.update(shadows[x])
assert len(chosen) == 143
assert Fraction(62165, 420) == Fraction(12433, 84)
assert 148 < Fraction(12433, 84) < 149
print('VERIFY_OK; 715 inputs; 495 shadows; 23 input orbits; 18 shadow orbits; lower=143; upper=148')
