#!/usr/bin/env python3
"""Independent finite checks for common index periods of second-kind Dickson functions.
Standard-library only. All checks are finite: the theorem requires the separate proof.
"""
from math import isqrt

def primes_upto(n):
    out = []
    for z in range(2, n+1):
        if all(z % d for d in range(2, isqrt(z)+1)):
            out.append(z)
    return out

def prime_factors(n):
    out = []
    d = 2
    while d*d <= n:
        if n%d == 0:
            out.append(d)
            while n%d == 0:
                n//=d
        d+=1
    if n>1:
        out.append(n)
    return out

I=(1,0,0,1)
def mm(A,B,m):
    return ((A[0]*B[0]+A[1]*B[2])%m, (A[0]*B[1]+A[1]*B[3])%m,
            (A[2]*B[0]+A[3]*B[2])%m, (A[2]*B[1]+A[3]*B[3])%m)
def mpow(A,n,m):
    out=I
    while n:
        if n&1: out=mm(out,A,m)
        A=mm(A,A,m)
        n>>=1
    return out

def dickson(n,x,a,m):
    e0,e1=1,x%m
    if n==0: return 1
    for j in range(1,n):
        e0,e1=e1,(x*e1-a*e0)%m
    return e1

def slope(n,x,a,p):
    # Differentiate the defining recurrence over F_p.
    e0,e1=1,x%p
    d0,d1=0,1
    if n==0: return 0
    for j in range(1,n):
        e0,e1,d0,d1=e1,(x*e1-a*e0)%p,d1,(e1+x*d1-a*d0)%p
    return d1

systems=matrices=quotient_checks=0
scalar_checks=derivative_checks=0
for p in [3,5,7,11,13]:
    sq={z*z%p for z in range(1,p)}
    L0=p*p-1
    for a in range(1,p):
        if a not in sq:
            for x in range(p):
                delta=(x*x-4*a)%p
                assert delta != 0
                expected=(2*L0*pow(delta,-1,p))%p
                assert slope(L0-1,x,a,p)==expected
                derivative_checks+=1
    for k in [1,2,3]:
        m=p**k
        if m>1000: continue
        for a in range(1,m):
            if a%p==0: continue
            L=(p**(k-1)*(p*p-1) if a%p not in sq else p**k*(p*p-1)//2)
            for x in range(m):
                A=(x,-a,1,0)
                assert mpow(A,L,m)==I,(p,k,a,x,'not a period')
                matrices+=1
                if m<=125 and x in (0,1,m//2,m-1):
                    for n in [0,1,2,3,7,11,20]:
                        assert dickson(n+L,x,a,m)==dickson(n,x,a,m)
                        scalar_checks+=1
            for r in prime_factors(L):
                assert any(mpow((x,-a,1,0),L//r,m)!=I for x in range(m)),(p,k,a,r,'not least')
                quotient_checks+=1
            systems+=1
print('VERIFY_OK systems=',systems,'matrices=',matrices,
      'proper_prime_quotient_exclusions=',quotient_checks,
      'scalar_recurrence_checks=',scalar_checks,'nonzero_derivative_checks=',derivative_checks)
