#!/usr/bin/env python3
"""Exact finite checks of origin/core laws for uniformly random self-maps."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial, isclose, pi, sqrt, exp

ASSERTIONS = 0
def ck(a,b):
    global ASSERTIONS
    ASSERTIONS += 1
    assert a == b, (a,b)

def falling(n,k):
    v=1
    for j in range(k): v*=n-j
    return v

def cyclic_count(f):
    n=len(f); seen=set(); cyc=set()
    for start in range(n):
        if start in seen: continue
        chain=[]; where={}; v=start
        while v not in seen and v not in where:
            where[v]=len(chain); chain.append(v); v=f[v]
        if v in where: cyc.update(chain[where[v]:])
        seen.update(chain)
    return len(cyc)

def joint(n):
    d=Counter()
    for f in product(range(n),repeat=n):
        c=cyclic_count(f)
        indeg=[0]*n
        for t in f: indeg[t]+=1
        l=sum(x==0 for x in indeg)
        d[c,l]+=1
    return d

def tail(n,k):
    return Fraction(falling(n,k),n**k) if k<=n else Fraction(0)

def ecyc(n):
    return sum((tail(n,k) for k in range(1,n+1)),Fraction(0))

for n in range(2,8):
    d=joint(n); total=n**n
    ck(sum(d.values()),total)
    # Exact cyclic-count tails and conditional occupancy factorial moments.
    for k in range(1,n+1):
        ck(Fraction(sum(z for (c,l),z in d.items() if c>=k),total),tail(n,k))
    for c in range(1,n+1):
        count=sum(z for (cc,ll),z in d.items() if cc==c)
        if c==n:
            ck(sum(z for (cc,ll),z in d.items() if cc==c and ll!=0),0)
            continue
        m=n-c
        for r in range(m+1):
            observed=Fraction(sum(falling(l,r)*z for (cc,l),z in d.items() if cc==c),count)
            expected=Fraction(falling(m,r)*(n-r)**(m-1),n**(m-1))
            ck(observed,expected)
    # Entire mixed falling-factorial identity against each possible cyclic count.
    for r in range(n):
        moment=Fraction(falling(n,r)*(n-r)**n,n**n)
        for k in range(1,n+1):
            empirical=Fraction(sum(falling(l,r)*z for (c,l),z in d.items() if c>=k),total)
            predicted=moment*tail(n-r,k)
            ck(empirical,predicted)
    # Whole t-tilted cyclic law, including exact strict comparison at all thresholds.
    for t1,t2 in ((1,2),(2,3),(3,5)):
        den1=sum(z*t1**l for (c,l),z in d.items())
        den2=sum(z*t2**l for (c,l),z in d.items())
        for k in range(2,n+1):
            p1=Fraction(sum(z*t1**l for (c,l),z in d.items() if c>=k),den1)
            p2=Fraction(sum(z*t2**l for (c,l),z in d.items() if c>=k),den2)
            ck(p1>p2,True)
        for t in (t1,t2):
            poly=[comb(n,r)*Fraction((n-r)**n,n**n)*(t-1)**r for r in range(n)]
            norm=sum(poly)
            for k in range(1,n+1):
                theory=sum(poly[r]*tail(n-r,k) for r in range(n))/norm
                empirical=Fraction(sum(z*t**l for (c,l),z in d.items() if c>=k),sum(z*t**l for zc,z in d.items() for l in [zc[1]]))
                ck(empirical,theory)
    p=Fraction((n-1)**n,n**n)
    E_CL=Fraction(sum(c*l*z for (c,l),z in d.items()),total)
    E_C=ecyc(n)
    E_L=n*p
    ck(E_CL-E_C*E_L,n*p*(ecyc(n-1)-ecyc(n)))
    print('n=',n,'maps=',total,'pairs=',len(d),'PASS')

# Verify asymptotic constants numerically (not a proof of the limit).
for n in (2000,10000,50000):
    def S(m):
        p=1.; acc=0.
        for k in range(1,m+1):
            p*=1-(k-1)/m
            acc+=p
            if p<1e-15: break
        return acc
    a=sqrt(n)*(S(n)-S(n-1))
    if n==50000: assert abs(a-sqrt(pi/8))<0.01
    print('n=',n,'scaled adjacent mean difference=',a)

print('PASS exact assertions:',ASSERTIONS)
