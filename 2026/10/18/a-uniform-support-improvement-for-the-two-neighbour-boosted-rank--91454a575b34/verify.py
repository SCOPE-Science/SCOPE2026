#!/usr/bin/env python3
"""Reproducible finite checks for a two-neighbour rank statistic lower bound."""
from fractions import Fraction as F
from itertools import permutations

SUPPORTS = [
    (F(3, 2), F(1, 2), {(0,0):F(0),(0,1):F(-1),(1,0):F(-1,2),(1,1):F(-1)}),
    (F(5, 2), F(1), {(0,0):F(0),(0,1):F(-3,2),(1,0):F(-1),(1,1):F(-2)}),
    (F(4), F(2), {(0,0):F(0),(0,1):F(-2),(1,0):F(-1),(1,1):F(-3)}),
]

def lower(n, k):
    return max(0, (3*k-n+1)//2, (5*k-2*n+1)//2, 4*k-2*n)

def score(r):
    n = len(r)
    return sum(min(r[i], r[i+j]) for j in (1,2) for i in range(n-j)) + r[-2] + 2*r[-1]

# The complete finite-state certificate for each linear supporting inequality.
checks = 0
for slope, shift, h in SUPPORTS:
    for a in (0,1):
        for b in (0,1):
            for c in (0,1):
                q = (a,b); nq=(b,c)
                slack = c*(a+b)-slope*c+shift+h[q]-h[nq]
                assert slack >= 0, (slope,shift,a,b,c,slack)
                checks += 1
            assert a+2*b+h[(a,b)] >= 0
            checks += 1

# Threshold bound and the rank formulation are exact at every finite test.
permutation_checks=0
for n in range(2,10):
    target=sum(lower(n,k) for k in range(1,n+1))
    for r in permutations(range(1,n+1)):
        p=score(r)
        assert p >= target, (n,r,p,target)
        threshold_sum=0
        for z in range(1,n+1):
            bits=sum((1<<i) for i,x in enumerate(r) if x>=z)
            threshold_sum += (bits&(bits>>1)).bit_count()+(bits&(bits>>2)).bit_count() + ((bits>>(n-2))&1) + 2*((bits>>(n-1))&1)
        assert p == threshold_sum
        permutation_checks+=1

# Dynamic subset optimum is diagnostic only, not an infinite theorem.
subset_checks=0
for n in range(2,17):
    N=1<<n
    costs=[0]*N
    for mask in range(1,N):
        k=mask.bit_count()
        part=(mask&(mask>>1)).bit_count()+(mask&(mask>>2)).bit_count()+((mask>>(n-2))&1)+2*((mask>>(n-1))&1)
        assert part>=lower(n,k)
        c=mask
        best=10**9
        while c:
            bit=c&-c
            prior=costs[mask^bit]
            if prior<best:best=prior
            c-=bit
        costs[mask]=best+part
        subset_checks+=1
    assert costs[-1] >=sum(lower(n,k) for k in range(1,n+1))

# Verify that the integrated supporting profile is 13/24.
from fractions import Fraction
# 0 until 1/3; (3d-1)/2 until 1/2; (5d-2)/2 until 2/3; 4d-2 thereafter.
def antiderivative(s,t,x): return s*x*x/2-t*x
integral=sum(antiderivative(s,t,hi)-antiderivative(s,t,lo)
             for s,t,lo,hi in [
                 (F(3,2), F(1,2),F(1,3),F(1,2)),
                 (F(5,2), F(1),F(1,2),F(2,3)),
                 (F(4), F(2),F(2,3),F(1))])
assert integral == F(13,24)
print('PASS: transition and boundary certificates:',checks)
print('PASS: exhaustive distinct-rank configurations:',permutation_checks)
print('PASS: subset dynamic-programming configurations:',subset_checks)
print('PASS: exact integral:',integral)
for n in (8,16,24):
    hsum=sum(lower(n,k) for k in range(1,n+1))
    den=F(n+1)*F(4*n+3,2)
    print('n=',n,'sum support=',hsum,'certified xi bound=',float(F(-2)+F(6*hsum)/den))
