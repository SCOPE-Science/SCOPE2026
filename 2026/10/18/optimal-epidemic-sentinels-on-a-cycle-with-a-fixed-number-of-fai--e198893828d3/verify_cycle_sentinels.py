#!/usr/bin/env python3
"""Exact checks for finite-cycle fixed-count edge-failure surveillance.
Run with: python cycle_sentinel_verify.py
"""
from math import comb
from fractions import Fraction
from itertools import combinations

def B(n,m,l):
    return Fraction(comb(n-l,m),comb(n,m)) if 0 <= l <= n and 0 <= m <= n-l else Fraction(0)

def f(n,m,l):
    return sum((Fraction(1)-B(n,m,r)-B(n,m,l-r)+B(n,m,l) for r in range(1,l)), Fraction(0))

def gap_lengths(n,S):
    a=sorted(S)
    return tuple([(a[(i+1)%len(a)]-a[i])%n or n for i in range(len(a))])

def formula(n,m,S):
    return sum((f(n,m,l) for l in gap_lengths(n,S)),Fraction(0))/n

def direct(n,m,S):
    total=0
    for dead in combinations(range(n),m):
        dead=set(dead)
        seen=set()
        for v in range(n):
            if v in seen: continue
            cc={v}; queue=[v]; seen.add(v)
            for x in queue:
                for eid,y in ((x,(x+1)%n),((x-1)%n,(x-1)%n)):
                    if eid not in dead and y not in cc:
                        cc.add(y); queue.append(y); seen.add(y)
            if not cc.intersection(S): total+=len(cc)
    return Fraction(total,n*comb(n,m))

def expected_optimal(n,m,k,S):
    if m<=1:return True
    gaps=gap_lengths(n,S)
    L=n-m+1
    if n>k*L:
        return min(gaps)>=L
    q,r=divmod(n,k)
    return sorted(gaps)==[q]*(k-r)+[q+1]*r

def theorem():
    checks=0; opt_checks=0
    for n in range(3,10):
        for m in range(n+1):
            for k in range(1,n+1):
                vals=[]
                for s in combinations(range(n),k):
                    got=direct(n,m,set(s))
                    exp=formula(n,m,s)
                    assert got==exp,(n,m,s,got,exp)
                    vals.append((got,s))
                    checks+=1
                minval=min(x[0] for x in vals)
                for val,s in vals:
                    assert (val==minval)==expected_optimal(n,m,k,s),(n,m,k,s,val,minval)
                    opt_checks+=1
    print('full brute-force checks:',checks,'optimizer classifications:',opt_checks)
    n,m,k=10,8,2
    for gaps in ((1,9),(2,8),(3,7),(4,6),(5,5)):
        S=(0,gaps[0])
        print('n=10,m=8,k=2 gaps',gaps,'miss',formula(n,m,S),'detected',1-formula(n,m,S))
    for n,m in ((10,8),(12,9),(12,10),(11,10)):
        for l in range(1,n-1):
            curvature=f(n,m,l+2)-2*f(n,m,l+1)+f(n,m,l)
            cert=Fraction((l+1)*comb(n-l-2,m-2),comb(n,m)) if n-l-2>=m-2 else Fraction(0)
            assert curvature==cert,(n,m,l,curvature,cert)
    print('curvature certificates verified')
if __name__=='__main__': theorem()
