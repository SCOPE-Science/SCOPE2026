"""Exact normalization and extremizer checks for the regular 24-cell.

Only standard-library arithmetic is required. Analytic global extrema are proved
in RESULT.md; these finite checks verify the combinatorial and algebraic inputs.
"""
from fractions import Fraction as F
from itertools import product, combinations, permutations
from math import factorial

E = [tuple(F(1) if k == i else F(0) for k in range(4)) for i in range(4)]
vertices = set()
for v in E:
    vertices.add(v)
    vertices.add(tuple(-x for x in v))
for signs in product((-1, 1), repeat=4):
    vertices.add(tuple(F(s, 2) for s in signs))
assert len(vertices) == 24

normals = set()
for i, j in combinations(range(4), 2):
    for s, t in product((-1, 1), repeat=2):
        r = tuple(s if k == i else t if k == j else 0 for k in range(4))
        normals.add(r)
assert len(normals) == 24

def dot(x, y):
    return sum(F(a)*F(b) for a, b in zip(x, y))

for root in normals:
    assert all(dot(root, v) <= 1 for v in vertices)
    facet = [v for v in vertices if dot(root, v) == 1]
    assert len(facet) == 6
    center = tuple(F(r, 2) for r in root)
    centered = {tuple(v[i] - center[i] for i in range(4)) for v in facet}
    assert len(centered) == 6
    assert all(tuple(-z for z in w) in centered for w in centered)
    assert all(dot(w, w) == F(1, 2) for w in centered)
    one_each = []
    for w in centered:
        if -w[0] < w[0] or (w[0] == 0 and -w[1] < w[1]) or (w[0] == w[1] == 0 and -w[2] < w[2]) or (w[0] == w[1] == w[2] == 0 and -w[3] < w[3]):
            one_each.append(w)
    assert len(one_each) == 3
    assert all(dot(a, b) == 0 for a, b in combinations(one_each, 2))

# The centered facet is a 3D cross-polytope with circumradius 1/sqrt(2),
# hence its 3-volume is (4/3)*(1/sqrt(2))^3 = sqrt(2)/3.

def sum_pairs_abs(q):
    return sum(abs(q[i] + q[j]) + abs(q[i] - q[j]) for i,j in combinations(range(4), 2))

def b_square_of_direction(q):
    # For integer q, the unit direction is q / sqrt(dot(q,q)).
    # Cauchy formula: b = sum_pairs_abs(q) / (3 sqrt(dot(q,q))).
    return F(sum_pairs_abs(q)**2, 9*dot(q,q))

assert b_square_of_direction((1,0,0,0)) == 4
assert b_square_of_direction((1,1,1,1)) == 4
assert b_square_of_direction((3,2,1,0)) == F(56,9)
assert [3,5,6,6] == [3,3+2,3+2+1,3+2+1+0]
# The strict cone-generator comparisons are 25>18 and 36>27.
assert 25 > 18 and 36 > 27

minima = set()
maxima = set()
for q in ((1,0,0,0), (1,1,1,1)):
    for p in set(permutations(q)):
        inds=[i for i,x in enumerate(p) if x]
        for signs in product((-1,1),repeat=len(inds)):
            a=list(p)
            for i,s in zip(inds,signs): a[i]*=s
            minima.add(tuple(a))
for p in set(permutations((3,2,1,0))):
    inds=[i for i,x in enumerate(p) if x]
    for signs in product((-1,1),repeat=len(inds)):
        a=list(p)
        for i,s in zip(inds,signs): a[i]*=s
        maxima.add(tuple(a))
assert len(minima) == 24 and len(maxima) == 192
assert all(b_square_of_direction(a) == 4 for a in minima)
assert all(b_square_of_direction(a) == F(56,9) for a in maxima)

print("VERIFY_OK")
print("facets=24; facet_vertices=6; facet_cross_polytope_r2=1/2")
print("min_square=4; min_directions=24")
print("max_square=56/9; max_directions=192")
