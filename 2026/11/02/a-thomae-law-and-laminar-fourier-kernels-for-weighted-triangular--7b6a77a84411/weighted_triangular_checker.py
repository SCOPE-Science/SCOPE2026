#!/usr/bin/env python3
"""Standalone finite congruence checks for symmetric weighted triangular Fourier masks.
The infinite classification is established by the accompanying analytic proof.
"""
import math, cmath

def mask(p,k,a,j,m,n):
    t=1/(2*(1-math.cos(2*math.pi*a/p**k)))
    N=p**j
    return 1-2*t+t*cmath.exp(-2j*math.pi*m/N)+t*cmath.exp(-2j*math.pi*n/N)

def predicted(p,k,a,j,m,n):
    if j<k:return False
    N=p**j
    h=a*p**(j-k)
    return ((m-h)%N==0 and (n+h)%N==0) or ((m+h)%N==0 and (n-h)%N==0)

def test(p,k,a,J):
    for j in range(1,J+1):
        N=p**j
        count=0
        for m in range(N):
            for n in range(N):
                z=mask(p,k,a,j,m,n)
                iszero=abs(z)<1e-9
                pred=predicted(p,k,a,j,m,n)
                assert iszero==pred, (p,k,a,j,m,n,z,pred)
                count+=iszero
        assert count==(2 if j>=k else 0), (p,k,a,j,count)
        print(f'p={p} k={k} a={a} j={j} exact-zero-residues={count}')

test(3,1,1,4)
test(5,1,2,3)
test(5,2,7,3)
test(5,2,8,3)
test(7,1,2,2)

# Test finite-level first-zero census and laminar inclusion (including equal-level disjointness).
def all_first_hits(p,k,a,L):
    N=p**L
    hits=set()
    for j in range(k,L+1):
        h=a*p**(j-k)
        nj=p**j
        for m in range(N):
            if m%nj not in (h%nj,(-h)%nj):continue
            for n in range(N):
                if predicted(p,k,a,j,m,n):hits.add((m,n))
    expect=2*sum(p**(2*(L-j)) for j in range(k,L+1))
    assert len(hits)==expect, (p,k,a,L,len(hits),expect)
    return hits

for L in range(1,4):
    s=all_first_hits(5,1,2,L)
    if L>=2:
        s7=all_first_hits(5,2,7,L)
        s8=all_first_hits(5,2,8,L)
        assert s7.isdisjoint(s8) and s7.issubset(s) and s8.issubset(s)
    print(f'first-hit-census p=5 k=1 L={L}: {len(s)}')
print('WEIGHTED_TRIANGULAR_FINITE_MASK_CHECKS_OK')

try:
    from sympy import sqrt, pi, cos, simplify
    golden=(5-sqrt(5))/10
    assert simplify(1-2*golden+2*golden*cos(4*pi/5))==0
    print('GOLDEN_RATIO_MASK_EXACT_IDENTITY_OK')
except ImportError:
    print('SYMPY_UNAVAILABLE_EXACT_IDENTITY_NOT_CHECKED')
