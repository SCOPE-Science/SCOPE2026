"""Exact arithmetic checks for a six-line/conic incidence obstruction.

Run with Python >=3.9: python verify.py
All calculations use the standard library and integer polynomial arithmetic.
"""
from itertools import combinations, permutations


def add(a, b):
    out = dict(a)
    for e, v in b.items():
        out[e] = out.get(e, 0) + v
    return {e: v for e, v in out.items() if v}


def multiply(a, b):
    out = {}
    for e, v in a.items():
        for f, w in b.items():
            out[e + f] = out.get(e + f, 0) + v * w
    return {e: v for e, v in out.items() if v}


def determinant(matrix):
    n = len(matrix)
    assert all(len(row) == n for row in matrix)
    out = {}
    for p in permutations(range(n)):
        sign = (-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        term = {0: sign}
        for i in range(n):
            term = multiply(term, matrix[i][p[i]])
        out = add(out, term)
    return out


# Six-line triple-incidence patterns: pairwise intersection of any two
# triple blocks contains <=1 line.  All patterns on six labels have
# three pairwise intersections, one line in each (the triangle sides).
triples = list(combinations(range(6), 3))
patterns = []
for T in combinations(triples, 3):
    if all(len(set(a) & set(b)) <= 1 for a,b in combinations(T, 2)):
        assert len(set().union(*(set(t) for t in T))) == 6
        assert sorted(len(set(a) & set(b)) for a,b in combinations(T,2)) == [1,1,1]
        patterns.append(T)
assert len(patterns) == 120

# For nonzero u different from 1, the normalized six lines are
# x=0, y=0, z=0, y=z, z=x, x=u*y.
# Their six ordinary double intersections (homogeneous coordinates) are:
u = {1: 1}
one = {0: 1}
zero = {}
points = [
    (zero, one, one), (one, zero, one), (u, one, zero),
    (one, one, one), (u, one, one), (u, one, u),
]
rows = []
for x,y,z in points:
    rows.append([multiply(x,x), multiply(y,y), multiply(z,z),
                 multiply(x,y), multiply(x,z), multiply(y,z)])
actual = determinant(rows)
expected = {4: 1, 3: -2, 2: 1}  # u^2*(u-1)^2
assert actual == expected, (actual, expected)

# At u=2, the distinct line-pair crossing multiplicities are 3^3 2^6.
lines = [(1,0,0),(0,1,0),(0,0,1),(0,1,-1),(-1,0,1),(1,-2,0)]
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def normalize(p):
    from fractions import Fraction
    i = next(i for i,z in enumerate(p) if z)
    return tuple(Fraction(z,p[i]) for z in p)
counts = {}
for a,b in combinations(lines,2):
    p = normalize(cross(a,b))
    counts[p] = counts.get(p,0)+1
assert sorted(counts.values()) == [1]*6 + [3]*3  # 3 pairs per triple point

# In a putative arrangement with only nine ordinary triple points:
# 12 line-conic intersections are 2 at each of six mixed triples;
# the remaining 15 line pairs give three pure line triples.
mixed = 12 // 2
pure = (15-mixed)//3
assert (mixed,pure) == (6,3)
assert 2*mixed == 12  # all line-conic pair intersections
assert mixed + 3*pure == 15  # all line-line pair intersections
assert 3*(mixed + pure) == 27  # all component-pair intersections
assert 4*(mixed + pure) == 36  # sum of local Tjurina numbers
assert 4*4 - 4*7 + 7*7 == 36 + 1  # near-free numerical identity
print('INCIDENCE: six mixed triples and three pure triples')
print('HYPERGRAPH: 120 labelled triangle-with-cevians descriptions')
print('CONIC DETERMINANT:', actual, '= u^2*(u-1)^2')
print('CONCLUSION: no conic through the six doubles for u not in {0,1}')
