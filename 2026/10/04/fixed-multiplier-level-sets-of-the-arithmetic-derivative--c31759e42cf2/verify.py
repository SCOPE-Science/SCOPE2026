#!/usr/bin/env python3
from math import isqrt

LIMIT = 200000
KMAX = 5

def factor(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            a=0
            while n%d==0:
                n//=d; a+=1
            out.append((d,a))
        d=3 if d==2 else d+2
    if n>1: out.append((n,1))
    return out

def deriv(n, fac=None):
    if n<=1: return 0
    fac=fac or factor(n)
    return sum(a*(n//p) for p,a in fac)

def structural_k(fac):
    if not fac: return None
    s=0
    for p,a in fac:
        if a%p: return None
        s += a//p
    return s

counts=[0]*(KMAX+1)
for n in range(2, LIMIT+1):
    fac=factor(n)
    d=deriv(n,fac)
    sk=structural_k(fac)
    for k in range(1,KMAX+1):
        lhs=(d==k*n)
        rhs=(sk==k)
        if lhs != rhs:
            raise SystemExit(f"mismatch n={n} k={k} fac={fac} D={d} structural={sk}")
        if lhs: counts[k]+=1
print("VERIFY_OK", LIMIT, counts[1:])
