#!/usr/bin/env python3
"""Exact finite graph and polynomial checks for six Bernoulli summands.
The universal inequality is proved analytically in RESULT.md; this checker
exhausts the finite six-vertex graph lemma and verifies its algebraic bounds.
"""
from fractions import Fraction as F
from itertools import combinations

EDGES = list(combinations(range(6), 2))
EDGE_INDEX = {edge: i for i, edge in enumerate(EDGES)}
TRIANGLE_MASKS = [sum(1 << EDGE_INDEX[e] for e in combinations(t, 2))
                  for t in combinations(range(6), 3)]
assert len(EDGES) == 15 and len(TRIANGLE_MASKS) == 20
maximum = [-1] * 16
count = [0] * 16
for mask in range(1 << 15):
    k = mask.bit_count()
    tri = sum((mask & tm) == tm for tm in TRIANGLE_MASKS)
    maximum[k] = max(maximum[k], tri)
    count[k] += 1
    if k >= 5:
        assert tri <= 2 * k - 8, (mask, k, tri)
assert sum(count) == 32768
assert maximum == [0, 0, 0, 1, 1, 2, 4, 4, 5, 7, 10, 10, 11, 13, 16, 20]

# Coefficient check by exact arithmetic, independent of symbolic software.
def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out

def pscale(a, c):
    return [c * x for x in a]

def padd(*polys):
    out = [F(0)] * max(map(len, polys))
    for p in polys:
        for i, c in enumerate(p): out[i] += c
    return out

def powp(a, n):
    out = [F(1)]
    for _ in range(n): out = pmul(out, a)
    return out

P = [F(0), F(1)]
Q = [F(1), F(-1)]
def bino_tail_atleast2():
    return padd([F(1)], pscale(powp(Q,6), -1), pscale(pmul(P, powp(Q,5)), -6))
def tail_atleast4():
    return padd(pscale(pmul(powp(P,4),powp(Q,2)),15),
                pscale(pmul(powp(P,5),Q),6),powp(P,6))

def prob_atleast_counts(k2, k3):
    return padd(pscale(pmul(powp(P,2),powp(Q,4)),k2),
                pscale(pmul(powp(P,3),powp(Q,3)),k3),tail_atleast4())
def evaluate(poly,p):
    return sum(c*p**i for i,c in enumerate(poly))

def exact_on_interval(poly, lo, hi):
    # Exact positive Bernstein coefficients imply polynomial strictly positive.
    import math
    n = len(poly)-1
    L = [F(lo), F(hi-lo)]
    subst = [F(0)]*(n+1)
    for j,c in enumerate(poly):
        pj = powp(L,j)
        for k,z in enumerate(pj): subst[k] += c*z
    bs = [sum(subst[j] * F(math.comb(i,j),math.comb(n,j))
              for j in range(i+1)) for i in range(n+1)]
    assert all(b > 0 for b in bs), bs
    return bs

# Region 1: 1/6 <= p <= 1/5
bound1 = padd(bino_tail_atleast2(), pscale(P,-1))
assert evaluate(bound1,F(1,6)) == F(4505,46656)
bs1=exact_on_interval(bound1,F(1,6),F(1,5))
# Region 2: 1/5 <= p <= 1/4
bound2 = padd(prob_atleast_counts(10,20),pscale(P,-1))
assert evaluate(bound2,F(1,5)) == F(196,3125)
bs2=exact_on_interval(bound2,F(1,5),F(1,4))
# Region 3: 1/4 <= p <= 1/3
bound3 = padd(prob_atleast_counts(5,18),pscale(P,-1))
assert evaluate(bound3,F(1,4)) == F(21,4096)
bs3=exact_on_interval(bound3,F(1,4),F(1,3))
assert bs3[0] == F(21,4096) and bs3[-1] == F(2,27)
print('EXACT_CHECK_OK; graphs=32768; edges=15; triangles=20;')
print('max_triangles_by_edges:',maximum)
print('verified_positive_Bernstein_coefficients:',len(bs1)+len(bs2)+len(bs3))
print('range_minima_lower_borders:',[bs1[0],bs2[0],bs3[0]])
