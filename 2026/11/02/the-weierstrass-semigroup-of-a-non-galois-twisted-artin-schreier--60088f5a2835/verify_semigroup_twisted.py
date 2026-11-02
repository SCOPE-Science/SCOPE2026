#!/usr/bin/env python3
"""Exact arithmetic checks for tame quotients of polynomial Artin--Schreier curves.
No computer algebra or external dependencies are required.
"""
from math import gcd

def numerical_semigroup(p, m, bound):
    gens = [p] + [p + j*m for j in range(1,p)]
    arr = [False]*(bound+1)
    arr[0] = True
    for x in range(1, bound+1):
        arr[x] = any(x>=g and arr[x-g] for g in gens)
    return gens, arr

def verify(p,d):
    m=d-1
    assert p >= 3 and all(p%a for a in range(2,int(p**.5)+1))
    assert d>=2 and gcd(p,m)==1
    g=(p-1)*d//2
    F=(p-1)*m
    gens, arr=numerical_semigroup(p,m,max(4*g+2*p, F+3*p))
    gaps=[n for n in range(F+1) if not arr[n]]
    assert len(gaps)==g, (p,d,g,len(gaps))
    assert gaps[-1] == F
    assert all(arr[n] for n in range(F+1,len(arr)))
    for j in range(1,p):
        r=(j*m)%p
        assert min(i for i in range(len(arr)) if arr[i] and i%p==r)==p+j*m
        assert not any(arr[a] and arr[p+j*m-a] for a in range(1,p+j*m))
    pseudo=[]
    for n in gaps:
        if all(n+gen<len(arr) and arr[n+gen] for gen in gens):
            pseudo.append(n)
    assert pseudo==[j*m for j in range(1,p)]
    assert len(gens)==p
    # Riemann--Hurwitz for the tame scalar quotient of the Artin--Schreier cover.
    M=1+(p-1)*d
    gw=(p-1)*(M-1)//2
    assert 2*gw-2==(p-1)*(2*g-2)+2*(p-2)
    # The x/y pole valuations on the cover descend by ramification p-1.
    assert M-p==(p-1)*m

count=0
for p in [3,5,7,11,13,17,19]:
    for d in range(2,55):
        if gcd(p,d-1)==1:
            verify(p,d)
            count+=1
print(f'VERIFY_OK: {count} pairs; Apéry, gaps, pseudo-Frobenius, genus, tame Riemann-Hurwitz and pole-order identities')
