"""Exact finite incidence checks for the characteristic-three magic-square surface.

This verifies the finite combinatorial premises of the accompanying proof.
The algebraic-geometric fiber and node arguments are written in RESULT.md.
"""
from itertools import combinations, product
from collections import Counter, defaultdict
from math import gcd
from fractions import Fraction

GRID = list(product((-1, 0, 1), repeat=2))
V = [(a, b, 1) for a, b in GRID]


def determinant(v, w, z):
    return (v[0]*(w[1]*z[2]-w[2]*z[1])
            -v[1]*(w[0]*z[2]-w[2]*z[0])
            +v[2]*(w[0]*z[1]-w[1]*z[0]))


def cross(v, w):
    return (v[1]*w[2]-v[2]*w[1],
            v[2]*w[0]-v[0]*w[2],
            v[0]*w[1]-v[1]*w[0])


def projective(v, p):
    v = tuple(int(a) % p for a in v)
    i = next(i for i, a in enumerate(v) if a)
    inverse = pow(v[i], -1, p)
    return tuple(a*inverse % p for a in v)


def projective_integer(v):
    g = gcd(*v)
    v = tuple(a//g for a in v)
    if next(a for a in v if a) < 0:
        v = tuple(-a for a in v)
    return v


# The seven equal-magic-sum differences have a six-by-six unit minor,
# so they define a rank-six linear subspace in every characteristic.
row_sums = [[int(i//3 == r) for i in range(9)] for r in range(3)]
col_sums = [[int(i%3 == c) for i in range(9)] for c in range(3)]
d1 = [int(i in (0, 4, 8)) for i in range(9)]
d2 = [int(i in (2, 4, 6)) for i in range(9)]
base = row_sums[0]
magic_relations = [[x-y for x,y in zip(row,base)]
                   for row in row_sums[1:] + col_sums + [d1,d2]]
minor = [[magic_relations[i][j] for j in (0,1,2,3,4,7)]
         for i in (0,1,2,3,5,6)]

def det_exact(a):
    a = [[Fraction(v) for v in row] for row in a]
    n = len(a)
    det = Fraction(1)
    for j in range(n):
        k = next((i for i in range(j,n) if a[i][j]),None)
        if k is None:return 0
        if k != j:
            a[j],a[k] = a[k],a[j]
            det = -det
        c = a[j][j]
        det *= c
        for i in range(j+1,n):
            f=a[i][j]/c
            for t in range(j,n):
                a[i][t] -= f*a[j][t]
    return det
assert det_exact(minor) == 1

triples = list(combinations(range(9), 3))
values = Counter(determinant(V[i], V[j], V[k]) for i, j, k in triples)
assert len(triples) == 84
assert max(map(abs, values)) == 4
assert values[0] == 8
assert sum(values[d] for d in values if d and d % 3 == 0) == 4

for p, expected in [(3, (0, 12)), (5, (12, 8)), (7, (12, 8))]:
    inter = defaultdict(set)
    for i, j in combinations(range(9), 2):
        pt = projective(cross(V[i], V[j]), p)
        inter[pt].update((i,j))
    profile = Counter(map(len, inter.values()))
    assert (profile.get(2, 0), profile.get(3, 0)) == expected, (p, profile)
    assert all(len(lines) <= 3 for lines in inter.values())
    assert sum(len(lines)*(len(lines)-1)//2 for lines in inter.values()) == 36
    assert expected[1]*32 == (384 if p==3 else 256)

interQ = defaultdict(set)
for i,j in combinations(range(9),2):
    interQ[projective_integer(cross(V[i],V[j]))].update((i,j))
assert Counter(map(len,interQ.values())) == Counter({2:12,3:8})

# The complete mod-three affine group acts transitively on the twelve
# projective branch triples (equivalently, affine grid lines).
points = list(product(range(3),repeat=2))
pointset = set(points)
matrices = [(a,b,c,d) for a,b,c,d in product(range(3),repeat=4)
            if (a*d-b*c)%3]
assert len(matrices) == 48
permutations = set()
triple_lines = {frozenset(GRID[i]) for i in ()}  # no empty lines admitted
triple_lines = set()
for i,j,k in triples:
    if determinant(V[i],V[j],V[k]) % 3 == 0:
        triple_lines.add(frozenset(tuple(t%3 for t in GRID[u])
                                   for u in (i,j,k)))
assert len(triple_lines) == 12
seed = next(iter(triple_lines))
orbit = set()
for a,b,c,d in matrices:
    for u,v in points:
        transform = lambda t: ((a*t[0]+b*t[1]+u)%3,
                               (c*t[0]+d*t[1]+v)%3)
        perm = tuple(transform(t) for t in points)
        assert set(perm) == pointset
        # Every coordinate pullback preserves the three-dimensional
        # linear subspace spanned by 1, the first coordinate, and the second.
        for coordinate in range(2):
            f = {pt: transform(pt)[coordinate] for pt in points}
            c0=f[(0,0)]
            c1=(f[(1,0)]-c0)%3
            c2=(f[(0,1)]-c0)%3
            assert all(f[x,y]==(c0+c1*x+c2*y)%3 for x,y in points)
        permutations.add(perm)
        image = frozenset(transform(t) for t in seed)
        assert image in triple_lines
        orbit.add(image)
assert len(permutations) == 432
assert orbit == triple_lines
assert 256*432 == 110592
assert 12*32 == 384
print('VERIFY_OK: 84 integer triples; 8/12 branch triples; 256/384 nodes; affine group 432; monomial subgroup 110592')
