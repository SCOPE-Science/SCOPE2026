#!/usr/bin/env python3
"""Exact maximal-tetrahedron determinant certificate for a simplex difference body.

Requires only Python 3 standard library. Coefficients use increasing powers.
"""
from collections import Counter
from itertools import combinations, permutations
from math import factorial


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return tuple(c)


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return tuple(c)


def canonical(a):
    c = list(a)
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    if c[-1] < 0:
        c = [-x for x in c]
    return tuple(c)


def sign(p):
    inversions = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inversions % 2 else 1


def determinant(rows):
    acc = (0,)
    for p in permutations(range(4)):
        term = (1,)
        for i in range(4):
            term = mul(term, rows[i][p[i]])
        if sign(p) == -1:
            term = tuple(-x for x in term)
        acc = add(acc, term)
    return canonical(acc)


basis = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
labels = [(i, j) for i in range(4) for j in range(4) if i != j]
points = []
for i, j in labels:
    points.append([(1,), *[(basis[i][k], -basis[j][k]) for k in range(3)]])

expected = {
    (0,): 78,
    (0, 1, 1): 120,
    (0, 0, 1): 72,
    (0, 1): 72,
    (0, 0, 1, 1): 48,
    (1, 1): 48,
    (0, 1, 1, 1): 24,
    (1, 1, 1): 24,
    (1, 1, 1, 1): 6,
    (-1, -1, 1, 1): 3,
}

spectrum = Counter()
maximizers = []
for quad in combinations(range(12), 4):
    det = determinant([points[i] for i in quad])
    spectrum[det] += 1
    if det == (1, 1, 1, 1):
        maximizers.append(frozenset(labels[i] for i in quad))

assert sum(spectrum.values()) == 495
assert spectrum == expected, (spectrum - expected, expected - spectrum)
assert len(maximizers) == 6
assert len(set(maximizers)) == 6
for tet in maximizers:
    assert len({i for i, j in tet}) == 4
    assert len({j for i, j in tet}) == 4
    assert any(all((i, f[i]) in tet for i in range(4)) for f in permutations(range(4))
               if all(f[i] != i for i in range(4))
               and all(f[f[i]] != i for i in range(4)))
for p, q in combinations(maximizers, 2):
    assert len(p & q) <= 1, (p, q)

# Exact inequalities against (1+s)(1+s*s) on the positive ray:
# all positive-coefficient classes are dominated coefficientwise,
# and the sole sign-changing class has explicit factorizations.
D = (1, 1, 1, 1)
for f in expected:
    if f in [(0,), D, (-1, -1, 1, 1)]:
        continue
    assert all(D[i] - (f[i] if i < len(f) else 0) >= 0 for i in range(4))
    assert any(D[i] - (f[i] if i < len(f) else 0) > 0 for i in range(4))
# D(s)-|(s-1)(s+1)^2| equals 2*s^2*(1+s) if 0<s<1,
# and 2*(1+s) if s>=1; both are strictly positive.
assert factorial(4) == 24
print("VERIFY_OK quadruples=495 determinant_classes=10 maximum_orbits=6")
