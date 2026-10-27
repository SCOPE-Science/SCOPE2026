"""Exact finite checks for regular block-design public-goods imitation.

Standard library only.  Assertions test finite examples; proofs are in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def degs(v, edges):
    return [sum(i in e for e in edges) for i in range(v)]


def payoff(v, edges, coal, r):
    deg = degs(v, edges)
    assert min(deg) > 0
    return [r * sum(len(coal.intersection(e)) for e in edges if i in e) / deg[i] - (i in coal)
            for i in range(v)]


def birth_coeff(v, edges, coal):
    deg = degs(v, edges)
    return sum(Q(1, v * deg[i]) *
               sum(1 for e in edges if i in e and coal.intersection(e))
               for i in range(v) if i not in coal)


def check_design(v, edges):
    ds = degs(v, edges)
    pairs = [sum(i in e and j in e for e in edges) for i in range(v) for j in range(i + 1, v)]
    assert len(set(ds)) == len(set(pairs)) == 1
    d, lam, g = ds[0], pairs[0], len(edges[0]); assert lam * (v-1) == d * (g-1)
    for r in (Q(1,2), Q(4,3), Q(3,2), Q(2,1), Q(5,2)):
        gap = r * (v-g) / (v-1) - 1
        for k in range(v + 1):
            for tup in combinations(range(v), k):
                c = set(tup)
                p = payoff(v, edges, c, r)
                assert all(p[i] == p[j] for i in c for j in c)
                assert all(p[i] == p[j] for i in range(v) if i not in c for j in range(v) if j not in c)
                if 0 < k < v:
                    assert p[next(iter(c))] - p[next(i for i in range(v) if i not in c)] == gap
                    assert birth_coeff(v, edges, c) > 0
    return d, lam

fano = [(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)]
assert check_design(7, fano) == (3,1)
assert birth_coeff(7, fano, {0,1,2}) == Q(4,7)
assert birth_coeff(7, fano, {0,1,3}) == Q(3,7)

for v,g in ((4,2),(4,3),(5,2),(6,3),(7,3),(7,4)):
    edges = list(combinations(range(v),g))
    check_design(v, edges)
    d = comb(v-1,g-1)
    for k in range(1,v):
        expected = Q(v-k,v) * (1-Q(comb(v-k-1,g-1) if v-k-1>=g-1 else 0,d))
        for tup in combinations(range(v),k):
            assert birth_coeff(v,edges,set(tup))==expected

# Complete pair game: harmonic identity for exact holding-time sum.
for v in range(3,31):
    total=sum(Q(v*(v-1), k*(v-k)) for k in range(1,v))
    harmonic=sum((Q(1,k) for k in range(1,v)), Q(0))
    assert total == 2*(v-1)*harmonic

# The asymptotic constant is checkable numerically, not proved by these tests.
from math import log
for g in (2,3,4):
    for v in (500,2000):
        coef=sum(v / ((v-k)*(1 - (comb(v-k-1,g-1)/comb(v-1,g-1) if v-k-1>=g-1 else 0))) for k in range(1,v))
        target=g/(g-1)
        assert abs(coef/(v*log(v))-target)<0.35
print('PASS: exhaustive exact rational design payoffs, 6 complete designs, all Fano configurations, Fano non-lumpability, 28 harmonic identities, asymptotic sanity.')
