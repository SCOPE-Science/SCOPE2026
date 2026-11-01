"""Independent finite and numerical checks of a truncated-octahedron section law.

Run with Python 3; only the standard library is required. The exact rational
section and edge tests test samples, not the infinite spherical theorem.
"""
import itertools
import math
import random

vertices = sorted({tuple(p[i] * s[i] for i in range(3))
                   for p in set(itertools.permutations((0, 1, 2)))
                   for s in itertools.product((-1, 1), repeat=3)})
faces = []
for i in range(3):
    for sign in (-1, 1):
        faces.append(tuple(v for v in vertices if v[i] == 2 * sign))
for signs in itertools.product((-1, 1), repeat=3):
    faces.append(tuple(v for v in vertices
                       if sum(signs[i] * v[i] for i in range(3)) == 3))
assert len(vertices) == 24 and len(faces) == 14
assert sorted(map(len, faces)) == [4]*6 + [6]*8

incidence = {v: frozenset(i for i, f in enumerate(faces) if v in f)
             for v in vertices}
edges = [(a, b) for a, b in itertools.combinations(vertices, 2)
         if len(incidence[a] & incidence[b]) == 2]
assert len(edges) == 36

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def by_faces(u):
    return sum(min(dot(u, v) for v in f) < 0 < max(dot(u, v) for v in f)
               for f in faces)

def by_edges(u):
    return sum(dot(u, a)*dot(u, b) < 0 for a, b in edges)

def by_chambers(u):
    x, y, z = sorted(map(abs, u), reverse=True)
    return 4 + 2*(int(x > 2*y) + int(x > 2*z) + int(y < 2*z))

checks = 0
for x in range(1, 41):
    for y in range(1, x+1):
        for z in range(1, y+1):
            if x == 2*y or x == 2*z or y == 2*z:
                continue
            u = (x, y, z)
            a, b, c = by_faces(u), by_edges(u), by_chambers(u)
            assert a == b == c, (u, a, b, c)
            checks += 1

A, B, C = (1, 1, 1), (1, 1, 0), (1, 0, 0)
U, V, T, W = (2, 2, 1), (2, 1, 1), (4, 2, 1), (2, 1, 0)
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def norm(a):
    return math.sqrt(dot(a,a))
def omega(a,b,c):
    denominator=(norm(a)*norm(b)*norm(c)+dot(a,b)*norm(c)
                 +dot(a,c)*norm(b)+dot(b,c)*norm(a))
    return 2*math.atan2(abs(dot(a,cross(b,c))),denominator)

area8 = omega(U,V,T)+omega(T,W,C)
area10 = omega(V,T,C)
area6 = omega(A,U,V)+omega(U,B,W)+omega(U,W,T)
assert abs(area6+area8+area10-math.pi/12)<1e-12
p = {6:12*area6/math.pi, 8:12*area8/math.pi, 10:12*area10/math.pi}
assert abs(sum(p.values())-1)<1e-12
# Direct orientation sampling does not use the normalized-chamber formula.
rng = random.Random(20261025)
counts = {6:0, 8:0, 10:0}
for _ in range(80000):
    u = tuple(rng.gauss(0,1) for _ in range(3))
    n = by_faces(u)
    assert n in counts
    counts[n] += 1
freq = {k: counts[k]/80000 for k in counts}
for k in counts:
    assert abs(freq[k]-p[k])<0.02, (k,freq[k],p[k])
print('24 vertices, 14 facets, 36 edges')
print('Exact integer-normal checks:', checks)
print('Normal-chamber probabilities:', p)
print('Independent Gaussian-normal frequencies:', freq)
print('All checks passed')
