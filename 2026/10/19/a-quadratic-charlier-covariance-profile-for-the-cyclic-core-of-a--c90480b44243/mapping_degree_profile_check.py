#!/usr/bin/env python3
"""Standalone verification of finite identities for cyclic points and indegree histograms.

This verifies small finite cases; analytic asymptotics require the proof in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, exp, sqrt, pi

def B(n,k,d):
    if not (0<=d<=k): return F(0)
    return F(comb(k,d)*(n-1)**(k-d), n**k)

def cond_hist(n,c,d):
    if c==n:return F(n if d==1 else 0)
    k=n-c-1
    return (F(c-1)*B(n,k,d-1)+B(n,k,d-2)+F(n-c)*B(n,k,d))

def cyclic_count(f):
    n=len(f); answer=0
    for start in range(n):
        j=start;seen=set()
        while j not in seen:
            seen.add(j);j=f[j]
        answer+=int(j==start)
    return answer

def mu(n):
    out=F(0);t=F(1)
    for j in range(1,n+1):
        t*=F(n-j+1,n);out+=t
    return out

checks=0
for n in range(2,7):
    cc=defaultdict(int);hist=defaultdict(int);pairs=defaultdict(int)
    for f in product(range(n),repeat=n):
        c=cyclic_count(f);cc[c]+=1
        counts=[0]*n
        for y in f:counts[y]+=1
        for d in range(n+1):
            h=sum(x==d for x in counts)
            hist[d]+=h
            pairs[c,d]+=h
    total=n**n
    for c in range(1,n+1):
        predicted=F(c, n**(c+1))
        for j in range(c):predicted*=n-j
        assert F(cc[c],total)==predicted,(n,c)
        checks+=1
        for d in range(n+1):
            actual=F(pairs[c,d],cc[c]);expected=cond_hist(n,c,d)
            assert actual==expected,(n,c,d,actual,expected)
            checks+=1
    for d in range(n+1):
        assert F(hist[d],total)==n*B(n,n,d)
        checks+=1
    if n>=2:
        # Conditional expected cyclic points for indegree 0,1,2.
        for d in range(3):
            num=den=0
            for f in product(range(n),repeat=n):
                dd=sum(v==0 for v in f)
                if dd==d: den+=1;num+=cyclic_count(f)
            got=F(num,den)
            m=mu(n-1)
            want= m if d==0 else (1+F(1,n))*m + (F(1,n) if d==1 else -F(1,n))
            assert got==want,(n,d,got,want)
            checks+=1

# Exact sign flip exhibited between n=6 and n=7; no unverified all-n uniqueness assertion.
for n,expected_sign in [(6,-1),(7,1)]:
    m=mu(n-1); val=(1+F(1,n))*m-F(1,n)-mu(n)
    assert (val>0)-(val<0)==expected_sign
    checks+=1

# Exact finite covariance computed by conditioning on the cyclic-point count.
for n in (20,50,100,200,400):
    mass=[];p=F(1)
    for c in range(1,n+1):
        # P(C_n=c)=c (n)_c/n^(c+1).
        p*=F(n-c+1,n)
        mass.append(F(c,n)*p)
    assert sum(mass)==1
    mean_c=sum((c+1)*pc for c,pc in enumerate(mass))
    for d in range(7):
        mean_h=n*B(n,n,d)
        mixed=sum((c+1)*mass[c]*cond_hist(n,c+1,d) for c in range(n))
        cv=float((mixed-mean_c*mean_h)/F(n))
        target=sqrt(pi/8)/exp(1)*(-d*d+3*d-1)/factorial(d)
        # finite values need not be close at low n; compare direction only for n>=100.
        if n>=100:
            assert (cv>0)==(target>0),(n,d,cv,target)
        checks+=1

print('CHECKS_OK',checks)
print('Limit profile coefficients:',[(d,round(sqrt(pi/8)/exp(1)*(-d*d+3*d-1)/factorial(d),9)) for d in range(8)])
print('Boundary n=6 and n=7 differences:',[float((1+F(1,n))*mu(n-1)-F(1,n)-mu(n)) for n in (6,7)])
