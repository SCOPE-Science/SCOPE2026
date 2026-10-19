#!/usr/bin/env python3
"""Independent finite verification of a sharp five-symbol multiset deletion bound.

Requires Python >= 3.9; standard library only. Run: python3 verify.py
"""
from collections import Counter
from itertools import combinations, permutations, product
from fractions import Fraction


def all_profiles(length, coordinates):
    if coordinates == 1:
        yield (length,)
    else:
        for a in range(length + 1):
            for tail in all_profiles(length - a, coordinates - 1):
                yield (a,) + tail


def meet(x, y):
    return sum(min(a, b) for a, b in zip(x, y))


X = set(all_profiles(5, 5))
assert len(X) == 126

# A and B are indexed cliques, even where their member sets coincide.
A = {i: frozenset(x for x in X if x[i] >= 3) for i in range(5)}
B = {(i, j): frozenset(x for x in X if x[i] >= 2 and x[j] >= 1)
     for i in range(5) for j in range(5) if i != j}

# C is the union of exactly six patterns, with remaining three coordinates
# considered without order. Each pattern specifies (x_i, x_j, sorted rest).
allowed = {
    (0, 1, (2, 1, 1)),
    (0, 2, (1, 1, 1)),
    (0, 2, (2, 1, 0)),
    (0, 3, (1, 1, 0)),
    (1, 1, (1, 1, 1)),
    (1, 2, (1, 1, 0)),
}
C = {(i, j): frozenset(x for x in X if
     (x[i], x[j], tuple(sorted((x[h] for h in range(5) if h not in (i,j)), reverse=True)))
     in allowed) for i in range(5) for j in range(5) if i != j}
assert len(A) == 5 and len(B) == 20 and len(C) == 20
assert Counter(map(len, A.values())) == {15: 5}, Counter(map(len, A.values()))
assert Counter(map(len, B.values())) == {15: 20}, Counter(map(len, B.values()))
assert Counter(map(len, C.values())) == {17: 20}, Counter(map(len, C.values()))

for family in (A, B, C):
    for key, clique in family.items():
        for x, y in combinations(clique, 2):
            assert meet(x, y) >= 3, (key, x, y)

expected_incidence = {
    (5, 0, 0, 0, 0): (1, 0, 0),
    (4, 1, 0, 0, 0): (1, 1, 0),
    (3, 2, 0, 0, 0): (1, 2, 0),
    (3, 1, 1, 0, 0): (1, 2, 2),
    (2, 2, 1, 0, 0): (0, 4, 4),
    (2, 1, 1, 1, 0): (0, 3, 7),
    (1, 1, 1, 1, 1): (0, 0, 20),
}
counts = Counter()
for x in X:
    key = tuple(sorted(x, reverse=True))
    inc = tuple(sum(x in clique for clique in family.values())
                for family in (A, B, C))
    assert inc == expected_incidence[key], (x, inc, key)
    assert Fraction(inc[0], 1) + Fraction(3*inc[1]+inc[2], 16) >= 1
    counts[key] += 1
assert counts == {
    (5, 0, 0, 0, 0): 5,
    (4, 1, 0, 0, 0): 20,
    (3, 2, 0, 0, 0): 20,
    (3, 1, 1, 0, 0): 30,
    (2, 2, 1, 0, 0): 30,
    (2, 1, 1, 1, 0): 20,
    (1, 1, 1, 1, 1): 1,
}
# Sum of weights of cliques is exactly ten.
assert len(A) + Fraction(3*len(B)+len(C), 16) == 10

# An attaining code consists of all pure compositions and five rotations.
base = (2, 2, 0, 1, 0)
cyclic = [tuple(base[(h-s) % 5] for h in range(5)) for s in range(5)]
pure = [tuple(5 if i == j else 0 for i in range(5)) for j in range(5)]
code = pure + cyclic
assert len(set(code)) == 10
assert all(x in X for x in code)
for x, y in combinations(code, 2):
    assert meet(x, y) <= 2, (x, y)

print('VERIFY_OK profiles=126 cliques=45 patterns=7 bound=10 witness=10')
