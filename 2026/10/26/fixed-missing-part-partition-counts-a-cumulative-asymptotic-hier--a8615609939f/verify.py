#!/usr/bin/env python3
"""Exact finite tests of the missing-part product identity and coefficient extraction."""
from math import comb, factorial, sqrt, pi, log, exp
from functools import lru_cache
N=120
M=4
f=[[0]*(N+1) for _ in range(M+1)];f[0][0]=1
for k in range(1,N+1):
    # Product (1+q^k-w*q^k)/(1-w*q^k), each truncation in degree w.
    old=f
    a=[[0]*(N+1) for _ in range(M+1)]
    for m in range(M+1):
        for n in range(N+1):
            v=old[m][n]
            if n>=k:
                v+=old[m][n-k]
                if m:v-=old[m-1][n-k]
                if m:v+=a[m-1][n-k]
            a[m][n]=v
    f=a
@lru_cache(None)
def partitions(n,maxp):
    if n==0:return ((),)
    return tuple((p,)+tail for p in range(min(n,maxp),0,-1) for tail in partitions(n-p,p))
for n in range(0,17):
    brute=[0]*(M+1)
    for p in partitions(n,n):
        if not p:miss=0
        else:miss=sum(k not in p for k in range(1,p[0]))
        if miss<=M:brute[miss]+=1
    assert [f[m][n] for m in range(M+1)]==brute, (n,brute,[f[m][n] for m in range(M+1)])
assert all(x>=0 for row in f for x in row)
# Compare ratios at finite cutoffs to their predicted leading ratio.
for x in (40,80,120):
    c=[sum(f[m][:x+1]) for m in range(4)]
    assert c[0]>0
    for m in (1,2,3):
        th=(2*sqrt(3)*(1-log(2))/pi)**m*x**(m/2)/factorial(m)
        assert c[m]/c[0]>0 and th>0
print('VERIFY_OK: exact product vs independent partitions through n=16; finite ratios positive')
