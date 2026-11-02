#!/usr/bin/env python3
"""Exact checks for rankwise search-depth stochastic ordering in random BSTs.

All arithmetic is rational. These finite checks supplement, but do not replace,
the all-size hypergeometric and record-count proof in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import comb, factorial

checks = 0

def check(statement):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(f"exact assertion {checks} failed")

def add_scaled(dst, src, scale):
    if len(dst)<len(src):
        dst.extend([Fraction(0)]*(len(src)-len(dst)))
    for j,x in enumerate(src):
        dst[j] += scale*x

def recurrence(limit):
    f = {(1,1):[Fraction(1)]}
    for n in range(2,limit+1):
        for i in range(1,n+1):
            p=[Fraction(1)]
            for root in range(1,n+1):
                if root<i:
                    add_scaled(p, [Fraction(0)]+f[(n-root,i-root)], Fraction(1))
                elif root>i:
                    add_scaled(p, [Fraction(0)]+f[(root-1,i)], Fraction(1))
            f[(n,i)]=[x/n for x in p]
            check(sum(f[(n,i)])==1)
            check(f[(n,i)][0]==Fraction(1,n))
    return f

def record_polynomials(limit):
    h=[[Fraction(1)]]
    for r in range(1,limit+1):
        prev=h[-1]; p=[Fraction(0)]*(len(prev)+1)
        for j,v in enumerate(prev):
            p[j]+=v*Fraction(r-1,r)
            p[j+1]+=v*Fraction(1,r)
        h.append(p)
    return h

def conv(p,q):
    out=[Fraction(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):out[i+j]+=x*y
    return out

def beta_formula(n,i,h):
    a=i-1; b=n-i; N=n-1;out=[Fraction(0)]
    for r in range(a+1):
        for s in range(b+1):
            weight=Fraction(comb(a,r)*comb(b,s)*factorial(r+s)*factorial(N-r-s),factorial(n))
            add_scaled(out,conv(h[r],h[s]),weight)
    return out

def direct_depths(order):
    n=len(order)
    L=[0]*(n+1); R=[0]*(n+1); root=order[0]
    depth=[0]*(n+1)
    for key in order[1:]:
        node=root;d=0
        while True:
            d+=1
            if key<node:
                if L[node]==0:L[node]=key;break
                node=L[node]
            else:
                if R[node]==0:R[node]=key;break
                node=R[node]
        depth[key]=d
    return depth

f=recurrence(24)
h=record_polynomials(12)
for n in range(1,13):
    for i in range(1,n+1):
        p=beta_formula(n,i,h)
        check(p==f[n,i])
for n in range(1,25):
    for i in range(1,n+1):
        p=f[n,i]
        check(p==f[n,n+1-i])
        E=sum(j*v for j,v in enumerate(p))
        H=lambda m:sum((Fraction(1,r) for r in range(1,m+1)),Fraction(0))
        check(E==H(i)+H(n+1-i)-2)
    for i in range(1,n//2+1):
        x=f[n,i];y=f[n,i+1]
        for t in range(n+1):
            tx=sum(x[t:]);ty=sum(y[t:])
            check(ty>=tx)
            if i<n/2 and 2<=t<=n-1:check(ty>tx)
            if (2*i==n) or t in (0,1,n):check(ty==tx)
        w=sum((sum(y[t:])-sum(x[t:]) for t in range(1,n)),Fraction(0))
        check(w==Fraction(1,i+1)-Fraction(1,n+1-i))
for n in range(1,9):
    counts=[Counter() for _ in range(n+1)]
    for order in permutations(range(1,n+1)):
        depth=direct_depths(order)
        for i in range(1,n+1):counts[i][depth[i]]+=1
    for i in range(1,n+1):
        p=[Fraction(counts[i][j],factorial(n)) for j in range(n)]
        check(p==f[n,i])
print(f'PASS: {checks:,} exact assertions; exhaustive insertion trees through n=8; recurrence and all adjacent tails through n=24; beta-binomial/record mixture through n=12')
