#!/usr/bin/env python3
"""Exact, standalone checks for sharp adjacent likelihood changes in parking outcomes."""
from itertools import permutations, product
from fractions import Fraction
from math import comb

assertions=0

def verify(condition, label):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(label)

def ell(p, j):
    k=j-1
    while k>=0 and p[k]<p[j]:
        k-=1
    return j-k

def weight(p):
    z=1
    for j in range(len(p)):
        z*=ell(p,j)
    return z

def predicted_ratio(p, i):
    n=len(p)
    a,b=p[i],p[i+1]
    assert a<b
    A,B=ell(p,i),ell(p,i+1)
    q=Fraction(B-1,A*B)
    for j in range(i+2,n):
        if a<p[j]<b and all(p[k]<p[j] for k in range(i+2,j)):
            q*=Fraction(j-i,j-i-1)
    return q

# Exhaust over all permutations through n=8; per-position extremizers,
# exact local formula and complete mass normalization.
for n in range(2,9):
    lows=[None]*(n-1)
    highs=[None]*(n-1)
    total=0
    for p in permutations(range(1,n+1)):
        w=weight(p); total += w
        for i in range(n-1):
            if p[i]>=p[i+1]:
                continue
            q=list(p);q[i],q[i+1]=q[i+1],q[i]
            r=Fraction(weight(q),w)
            verify(r==predicted_ratio(p,i),f'formula n={n} p={p} i={i+1}')
            verify(r>=Fraction(1,i+2),f'lower n={n} p={p} i={i+1}')
            verify(r<=Fraction((i+1)*(n-i-1),i+2),f'upper n={n} p={p} i={i+1}')
            lows[i] = r if lows[i] is None else min(lows[i],r)
            highs[i] = r if highs[i] is None else max(highs[i],r)
    verify(total==(n+1)**(n-1),f'normalization n={n}')
    for i in range(n-1):
        verify(lows[i]==Fraction(1,i+2),f'sharp lower n={n} i={i+1}')
        verify(highs[i]==Fraction((i+1)*(n-i-1),i+2),f'sharp upper n={n} i={i+1}')
        # Explicit all-n extremizers, not depending on enumerative check.
        p=tuple(range(1,n+1))
        q=list(p);q[i],q[i+1]=q[i+1],q[i]
        verify(Fraction(weight(q),weight(p))==Fraction(1,i+2),f'witness lower n={n} i={i+1}')
        m=i+1
        p=tuple(list(range(2,m+1))+[1,n]+list(range(m+1,n)))
        verify(len(p)==n and len(set(p))==n and p[m-1]<p[m],f'witness indices n={n} i={m}')
        q=list(p);q[m-1],q[m]=q[m],q[m-1]
        verify(Fraction(weight(q),weight(p))==Fraction(m*(n-m),m+1),f'witness upper n={n} i={m}')
    print(f'n={n}: total={total}, max={max(highs)}, min={min(lows)}, ratio-tests complete')

# Independent direct parking simulator, checking preimage fibers through n=5.
def park(pref):
    n=len(pref)
    spots=[None]*n
    for car,a in enumerate(pref,1):
        while a<=n and spots[a-1] is not None:
            a+=1
        if a>n: return None
        spots[a-1]=car
    return tuple(spots)
for n in range(2,6):
    counts={}
    for pref in product(range(1,n+1), repeat=n):
        p=park(pref)
        if p is not None:
            counts[p]=counts.get(p,0)+1
    verify(len(counts)==__import__('math').factorial(n),f'full support n={n}')
    for p in permutations(range(1,n+1)):
        verify(counts.get(p,0)==weight(p),f'preimage n={n} p={p}')
print(f'PASS: {assertions} exact assertions; independent preference enumeration through n=5')
