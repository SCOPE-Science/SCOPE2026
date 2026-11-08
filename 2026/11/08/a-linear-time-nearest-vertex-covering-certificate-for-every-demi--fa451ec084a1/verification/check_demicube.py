"""Exact rational finite checks for the demihypercube vertex-generation theorem.

Analytic proof in RESULT.md establishes the all-dimensional statement; this
script checks its normalization, facet inequality method, and sharp witnesses.
"""
from fractions import Fraction as F
from itertools import product, combinations
import random

rng = random.Random(20261101)
checks = 0

def ck(predicate, label):
    global checks
    checks += 1
    if not predicate:
        raise AssertionError(label)

def dot(x, y):
    return sum((a*b for a,b in zip(x,y)), F(0))

def sv(n, parity):
    return [tuple(x) for x in product((-1,1), repeat=n) if __import__('math').prod(x)==parity]

def inside(x, odd):
    n = len(x)
    return all(-1 <= t <= 1 for t in x) and all(dot(s,x)<=n-2 for s in odd)

for n in range(4, 9):
    even, odd = sv(n, 1), sv(n,-1)
    ck(len(even)==2**(n-1), ('number of even vertices',n))
    ck(len(odd)==2**(n-1), ('number of odd directions',n))
    for v in even:
        ck(inside(v, odd), ('vertex valid',n,v))
    for s in odd[:min(8,len(odd))]:
        support = [v for v in even if dot(s,v)==n-2]
        ck(len(support)==n, ('number simplex vertices',n,s))
        centroid = tuple(sum((F(v[i]) for v in support),F(0))/n for i in range(n))
        ck(centroid == tuple(F(n-2,n)*s[i] for i in range(n)), ('facet center',n,s))
        # At lambda = n-2, every attempted v leaves facet and violates one of
        # the n simplex barycentric coefficients.  Check directly via facets.
        for v in even:
            y = tuple(((n-1)*centroid[i]-v[i])/F(n-2) for i in range(n))
            ck(not inside(y,odd), ('sharp lower witness',n,s,v))

    candidates = list(even)
    candidates += [tuple((F(a)+F(b))/2 for a,b in zip(u,v))
                   for u,v in list(combinations(even,2))[:120]]
    for _ in range(90):
        sampled = [even[rng.randrange(len(even))] for j in range(4)]
        weights = [rng.randrange(1,9) for j in range(4)]
        total = sum(weights)
        candidates.append(tuple(sum((F(weights[j]*sampled[j][i],total) for j in range(4)),F(0)) for i in range(n)))
    for x in candidates:
        ck(inside(x,odd), ('sampled point',n,x))
        best = max(dot(x,v) for v in even)
        # Every tied nearest vertex must work.
        for v in even:
            if dot(x,v)==best:
                y = tuple((n*x[i]-v[i])/F(n-1) for i in range(n))
                ck(inside(y,odd), ('nearest vertex decomposition',n,x,v))

# The exceptional n=3 tetrahedron has 4 vertices and barycenter coefficients 1/4.
even3, odd3=sv(3,1), sv(3,-1)
ck(len(even3)==4,'tetrahedron vertices')
bar=tuple(F(0) for _ in range(3))
for v in even3:
    ck(not inside(tuple((3*bar[i]-v[i])/2 for i in range(3)),odd3),'n3 lower bound at lambda2')
print('EXACT_OK',checks)
