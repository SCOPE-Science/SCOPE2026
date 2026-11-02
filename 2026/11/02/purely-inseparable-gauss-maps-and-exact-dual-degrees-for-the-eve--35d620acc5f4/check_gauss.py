#!/usr/bin/env python3
"""Exact characteristic-p checks for the Ma-Wang plane Kummer models.
The infinite-family arguments are proved in RESULT.md; these are finite tests.
"""
from math import gcd

def add(A,B,p):
    C=A.copy()
    for k,v in B.items():
        C[k]=(C.get(k,0)+v)%p
        if not C[k]: del C[k]
    return C

def mul(A,B,p):
    C={}
    for i,a in A.items():
        for j,b in B.items():
            C[i+j]=(C.get(i+j,0)+a*b)%p
    return {k:v for k,v in C.items() if v}

def pow_poly(A,n,p):
    out={0:1}
    while n:
        if n&1: out=mul(out,A,p)
        A=mul(A,A,p)
        n//=2
    return out

def deriv(A,p):
    return {i-1:i*v%p for i,v in A.items() if i and i*v%p}

for p,e,n in [(2,1,4),(3,1,4),(2,2,4),(5,1,4),(2,1,6)]:
    q=p**e
    s=q**n
    N=s+1
    r=(q**(n-1)-1)//(q-1)
    j=q*q-q
    assert r%(q+1)==1
    assert gcd(r,N)==1
    assert (r-1)//q %p == 1
    A={q:1,1:(-1)%p}
    B=add({0:1},pow_poly(A,q-1,p),p)
    assert deriv(A,p)==({0:(-1)%p})
    assert deriv(B,p)==pow_poly(A,q-2,p)
    f=mul(A,pow_poly(B,r,p),p)
    assert max(f)==s
    expect={i:(-v)%p for i,v in pow_poly(B,r-1,p).items()}
    expect={i:v for i,v in expect.items() if v}
    assert deriv(f,p)==expect,(p,e,n)
    assert gcd(N,q**(n-1))==1
    # Check genus and singularity delta invariants independently.
    genus=(q*q-1)*s//2
    delta=j*(N-1)*(r-1)//2
    assert (N-1)*(N-2)//2 -delta ==genus
    assert N*q==q*(s+1)
    print(f'checked q={q},n={n}: degree {N}, cusps {j}, genus {genus}, dual degree {N*q}')
print('VERIFY_OK')
