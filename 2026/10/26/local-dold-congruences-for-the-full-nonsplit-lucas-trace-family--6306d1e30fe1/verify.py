#!/usr/bin/env python3
"""Exact small-prime checks of companion Lucas local arithmetic; not an infinite proof."""
from math import gcd

def primes(n):
    return [p for p in range(2,n+1) if all(p%d for d in range(2,int(p**.5)+1))]

def mob(n):
    if n==1:return 1
    fac=0; q=n; p=2
    while p*p<=q:
        if q%p==0:
            q//=p; fac+=1
            if q%p==0:return 0
            while q%p==0:q//=p
        p+=1
    if q>1:fac+=1
    return -1 if fac%2 else 1

def valuation(n,p):
    v=0
    while n%p==0:
        n//=p;v+=1
    return v

def legendre(a,p):
    v=pow(a%p,(p-1)//2,p)
    return 0 if v==0 else (1 if v==1 else -1)

def expected(P,p,N):
    vals=[0]*(N+1)
    if p==2:
        if P%2==0:
            s=valuation(P,2); vals[1]=2**s
            if N>=2:vals[2]=2-2**s
        else:
            vals[1]=1
            if N>=3:vals[3]=3
            if N>=6:vals[6]=-2
        return vals
    # Search rank mod p: recurrence has invertible transition; the first p^2+1 terms suffice.
    a,b=2%p,P%p; lam=None
    for n in range(1,p*p+3):
        if b==0:lam=n;break
        a,b=b,(P*b+a)%p
    vals[1]=1
    if lam is None:return vals
    # Compute V_lam exactly to find first valuation.
    a,b=2,P
    for n in range(1,lam):a,b=b,P*b+a
    e=valuation(b,p); z=lam
    if z==1:vals[1]=p**e
    elif z<=N:vals[z]=p**e-1
    if 2*z<=N:vals[2*z]=1-p**e
    j=1
    while z*p**j<=N:
        x=z*p**j; f=p**(e+j-1)*(p-1);vals[x]=f
        if 2*x<=N:vals[2*x]=-f
        j+=1
    return vals

count=0; bad=0; ram=0
for P in range(3,21):
    N=260
    V=[2,P]
    for n in range(2,N+1):V.append(P*V[-1]+V[-2])
    for p in primes(101):
        a=[0]+[p**valuation(V[n],p) for n in range(1,N+1)]
        T=[0]*(N+1)
        for n in range(1,N+1):
            T[n]=sum(mob(n//d)*a[d] for d in range(1,n+1) if n%d==0)
        E=expected(P,p,N)
        for n in range(1,N+1):
            assert T[n]==E[n],('transform',P,p,n,T[n],E[n])
        if p>2:
            D=P*P+4
            chi=legendre(D,p)
            if chi==0:ram+=1
            # using divisibility n | T directly; zero terms always divisible.
            obs=any(T[n]%n for n in range(1,N+1))
            if chi==-1 and p%4==3:
                assert obs,('predicted bad',P,p)
                bad+=1
            else:assert not obs,('predicted good',P,p)
        count+=N
print('VERIFY_OK parameter_count=18 prime_count=26 exact_transform_cells=%s bad_cases=%s ramified_cases=%s finite_only=YES'%(count,bad,ram))
