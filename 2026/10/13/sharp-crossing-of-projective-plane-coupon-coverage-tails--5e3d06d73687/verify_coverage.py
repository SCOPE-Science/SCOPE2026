#!/usr/bin/env python3
"""Exact certificates for two projective-plane coupon collection comparisons.

Only the Python standard library is required. All equality tests use integer or
rational arithmetic. The arbitrary-time sign assertions use exact inequalities
at their analytic thresholds, not numerical sampling.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from math import comb


def points(q):
    """Canonical nonzero projective-coordinate representatives over F_q, q=2,3."""
    raw = (v for v in product(range(q), repeat=3) if any(v))
    def canon(v):
        return min(tuple((a*x) % q for x in v) for a in range(1, q))
    return sorted(set(map(canon, raw)))


def projective_lines(q):
    P = points(q)
    loc = {v:i for i,v in enumerate(P)}
    def canon(v):
        return min(tuple((a*x) % q for x in v) for a in range(1, q))
    L = set()
    for x,y in combinations(P,2):
        span = set()
        for a,b in product(range(q), repeat=2):
            z = tuple((a*u+b*v)%q for u,v in zip(x,y))
            if any(z):
                span.add(loc[canon(z)])
        if len(span)==q+1:
            L.add(tuple(sorted(span)))
    assert len(P)==len(L)==q*q+q+1
    assert all(len(line)==q+1 for line in L)
    assert all(sum(i in line for line in L)==q+1 for i in range(len(P)))
    assert all(sum({i,j}.issubset(line) for line in map(set,L))==1
               for i,j in combinations(range(len(P)),2))
    return tuple(sorted(L))


def signed_avoidance_counts(n,blocks):
    B = [sum(1 << i for i in block) for block in blocks]
    ans = Counter()
    for miss in range(1,1<<n):
        clean = sum((b & miss)==0 for b in B)
        ans[clean] += 1 if miss.bit_count()%2 else -1
    return {j:c for j,c in sorted(ans.items()) if c}


def full_counts(n,r):
    total = comb(n,r)
    ans = Counter()
    for missing in range(1,n+1):
        k = comb(n-missing,r) if n-missing>=r else 0
        ans[F(k,total)] += (-1)**(missing+1)*comb(n,missing)
    return {v:c for v,c in ans.items() if c}


def survive(coef,t):
    assert t>=1
    return sum(F(base)**t*coefficient for base,coefficient in coef.items() if base)

C2 = {0:-6,1:21,2:-21,4:7}
C3 = {0:-38,1:130,2:-78,3:-182,4:234,6:-78,9:13}
Q2 = {F(0):15,F(1,35):-35,F(4,35):35,F(2,7):-21,F(4,7):7}
Q3 = {F(0):-220,F(1,715):715,F(1,143):-1287,F(3,143):1716,
      F(7,143):-1716,F(14,143):1287,F(126,715):-715,
      F(42,143):286,F(6,13):-78,F(9,13):13}
assert signed_avoidance_counts(7,projective_lines(2))==C2
assert signed_avoidance_counts(13,projective_lines(3))==C3
assert full_counts(7,3)==Q2
assert full_counts(13,4)==Q3

A2={F(k,7):c for k,c in C2.items()}
A3={F(k,13):c for k,c in C3.items()}
assert sum(C2.values())==sum(C3.values())==sum(Q2.values())==sum(Q3.values())==1
for t in range(1,21):
    d2=survive(A2,t)-survive(Q2,t)
    assert d2==F(21,7**t)-35*F(4,35)**t+35*F(1,35)**t
    if t<=2: assert d2==0
    else: assert d2>0
    d3=survive(A3,t)-survive(Q3,t)
    p=(234*220**t-286*210**t-182*165**t+715*126**t
       -78*110**t-1287*70**t+130*55**t+1716*35**t
       -1716*15**t+1287*5**t-715)
    assert d3==F(p,715**t)
    assert (d3==0 if t<=3 else d3<0 if t==4 else d3>0)
assert survive(A3,4)-survive(Q3,4)==-F(15480,2924207)
assert survive(A3,5)-survive(Q3,5)==F(2178216,418161601)
assert survive(A3,6)-survive(Q3,6)==F(10152590256,1494927723575)
assert 234-286*F(21,22)**7-182*F(3,4)**7>0
assert 715-78*F(55,63)**5-1287*F(5,9)**5>0
assert F(4,5)**2-F(1,5)**2==F(3,5)
for t in range(1,21):
    assert 1287*5**t-715>0
print('Exact incidence, avoidance-spectrum, rational-tail and analytic-threshold checks PASS')
