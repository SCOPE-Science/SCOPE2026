#!/usr/bin/env python3
"""Exact interval certificate for the exponent-three alternating divisor function.
Uses integer/rational arithmetic only, including rigorous reciprocal-zeta bounds.
"""
from fractions import Fraction as F
from itertools import product
from math import prod

P=(2,3,5,7)
R=3
Q=10**18
N=100000

def local(p,a):
    t=F(1,p**3)
    return sum(((-t)**j for j in range(a+1)), F(0))

def zeta_bounds():
    # For S_N=sum_{n<=N}1/n^3, each floor contributes < 1/Q error.
    fsum=sum(Q//(n*n*n) for n in range(1,N+1))
    low=F(fsum,Q)
    high=F(fsum+N,Q)+F(1,2*N*N)
    return low,high

zl,zu=zeta_bounds()
assert F(1202,1000) < zl < zu < F(1203,1000)
K=prod((F(1,1)/(1-F(1,p**3)) for p in P),start=F(1))
TL=K/zu; TU=K/zl
assert F(998190,10**6) < TL < TU < F(998192,10**6)
# The next-three-primes argument using Nagura's interval theorem.
c=[F(5,6)**(3*j) for j in (1,2,3)]
s1=sum(c,F(0));s2=sum((c[i]*c[j] for i in range(3) for j in range(i+1,3)),F(0))
assert s1>1 and s1-1>F(1,29**3)*s2
# Finite exceptional primes before the uniform Nagura regime.
small={11:(13,17,19),13:(17,19,23,29),17:(19,23),19:(23,29,31),23:(29,31,37)}
for p,qs in small.items():
    assert prod((1-F(1,q**3) for q in qs),start=F(1)) <= 1-F(1,p**3)
# Local choice dominance/overlap; for p=2 positive alpha>=3
# lies in the hull of alpha=3,4, and alpha=1,2 remain separate.
assert TU*local(2,4) <= local(2,3)
for p in (3,5,7):
    assert TU*local(p,2) <= local(p,1)

CH=((0,1,2,3,4),(0,1,2),(0,1,2),(0,1,2))
products={}
for e in product(*CH):
    a=prod((local(p,k) for p,k in zip(P,e)),start=F(1))
    products.setdefault(a,e)
assert len(products)==135
nums=sorted(products)
intervals=[]
worst_overlap=None
smallest_gap=None
for a in nums:
    if not intervals:
        intervals.append([a,a]);continue
    lo,hi=intervals[-1]
    if TU*a <= hi:
        excess=hi-TU*a
        worst_overlap=excess if worst_overlap is None else min(worst_overlap,excess)
        intervals[-1][1]=max(hi,a)
    else:
        gap=TL*a-hi
        assert gap>0, ('ambiguous T interval',a,hi)
        smallest_gap=gap if smallest_gap is None else min(smallest_gap,gap)
        intervals.append([a,a])
assert len(intervals)==19
assert worst_overlap is not None and smallest_gap is not None
assert all(TL*intervals[i][0]>intervals[i-1][1] for i in range(1,len(intervals)))
# First and last exact structure.
assert intervals[0][0]==prod((local(p,1) for p in P),start=F(1))
assert intervals[-1]==[F(1),F(1)]
print('VERIFY_OK')
print('ZETA_LOWER',zl,'ZETA_UPPER',zu)
print('T_LOWER',TL,'T_UPPER',TU)
print('distinct_finite_local_products',len(nums))
print('components',len(intervals),'min_certified_gap',float(smallest_gap),'min_certified_overlap',float(worst_overlap))
for i,(a,b) in enumerate(intervals,1):
    print('%2d  lower=T*(%s)    upper=%s   left_exp=%s right_exp=%s  approx=[%.12f,%.12f]' % (
         i,a,b,products[a],products[b],float(TL*a),float(b)))
