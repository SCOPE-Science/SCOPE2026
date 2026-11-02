#!/usr/bin/env python3
"""Exact-enumeration and geometric checks for a triangular Fourier shell."""
from collections import Counter
from math import ceil, sqrt, pi, acos, isclose

def div_character(n):
    return sum((1 if d%3==1 else -1 if d%3==2 else 0) for d in range(1,n+1) if n%d==0)

def rhex(m):
    return 1 if m==0 else 6*div_character(m)

def expected_cdf(s):
    if s<=1/3: return 0.
    if s>=1: return 1.
    r2=s-1/3
    h=1/sqrt(6)
    cap=0. if r2<=h*h else r2*acos(h/sqrt(r2))-h*sqrt(r2-h*h)
    return (pi*r2-3*cap)/(sqrt(3)/2)

def spectrum(M):
    n=3*M
    counts=Counter()
    for a in range(n+1):
      for b in range(n+1-a):
        c=n-a-b
        v=a*a+b*b+c*c
        assert (v-3*M*M)%2==0
        m=(v-3*M*M)//2
        counts[m]+=1
    assert sum(counts.values())==(n+1)*(n+2)//2
    return counts

nchecks=0
for M in range(1,36):
    counts=spectrum(M)
    m0=ceil(3*(M+1)**2/4)
    for m in range(m0):
        assert counts[m]==rhex(m),(M,m,counts[m],rhex(m))
        nchecks+=1
    assert counts[m0]<rhex(m0),(M,m0,counts[m0],rhex(m0))
    nchecks+=1
    assert sum(counts.values())==(3*M+1)*(3*M+2)//2
    nchecks+=1

for N in (300,600,1200):
    q=(.34,.39,.48,.52,.65,.80,.95)
    vals=[(a*a+b*b+(N-a-b)**2)/(N*N) for a in range(N+1) for b in range(N-a+1)]
    scale=1/len(vals)
    for t in q:
        actual=sum(v<=t for v in vals)*scale
        assert abs(actual-expected_cdf(t))< 5/N,(N,t,actual,expected_cdf(t))
        nchecks+=1

# Check nonanalytic cusp constant from exact density function at s = 1/2.
for delta in (1.e-4,1.e-6,1.e-8):
    f0=2*pi/sqrt(3)
    f1=2/sqrt(3)*(pi-3*acos((1/sqrt(6))/sqrt(1/6+delta)))
    assert abs((f0-f1)/sqrt(delta)-6*sqrt(2))<1.e-2
    nchecks+=1
print(f'PASS {nchecks} exact or precision-tested assertions; all critical thresholds and density comparisons passed.')
