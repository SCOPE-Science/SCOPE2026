#!/usr/bin/env python3
"""Finite checks of local Dold and repair formulas for Pell pairs."""
from math import gcd


def primes_upto(limit):
    sieve=[True]*(limit+1)
    sieve[:2]=[False,False]
    for d in range(2,int(limit**0.5)+1):
        if sieve[d]:
            for j in range(d*d,limit+1,d):sieve[j]=False
    return [i for i,v in enumerate(sieve) if v]


def vp(a,p):
    assert a!=0
    n=0
    while a%p==0:
        a//=p;n+=1
    return n


def pell(N):
    U=[0,1];V=[2,2]
    for n in range(2,N+1):
        U.append(2*U[-1]+U[-2]);V.append(2*V[-1]+V[-2])
    return U,V


def mobius(n):
    if n==1:return 1
    k=n;par=0
    for p in range(2,int(n**0.5)+1):
        if k%p==0:
            k//=p;par+=1
            if k%p==0:return 0
            while k%p==0:k//=p
    if k>1:par+=1
    return (-1)**par


def fold(arr,n):
    return sum(mobius(n//d)*arr[d] for d in range(1,n+1) if n%d==0)


def do():
    ps=primes_upto(103)
    N=320
    U,V=pell(N)
    cases=0
    for p in ps:
        r=next((n for n in range(1,p+2) if U[n]%p==0),None)
        if p>2:
            assert r is not None
            assert r>=3 and (p-(1 if p%8 in(1,7) else -1))%r==0
            ru=r//gcd(r,p-1)
            rv=(r//gcd(r,p-1)) if r%2==0 else 1
            assert (ru==1)==(p%8 in(1,7))
            assert (rv==1)==(p%8 !=3)
            if p%8==5:assert r%2==1
            if p%8 in(3,7):assert r%2==0
            if p%8==3:assert vp(r,2)>=2
        else:ru=2;rv=1
        e=vp(U[r],p) if p>2 else 0
        t=r//2 if (p>2 and r%2==0) else None
        ev=vp(V[t],p) if t else 0
        AU=[None];AV=[None]
        for n in range(1,N+1):
            a=p**vp(U[n],p);b=p**vp(V[n],p)
            if p>2:
                eu=(e+vp(n//r,p)) if n%r==0 else 0
                bv=ev+vp(n//t,p) if (t and n%t==0 and (n//t)%2==1) else 0
                assert a==p**eu,(p,n,a,eu)
                assert b==p**bv,(p,n,b,bv)
            else:assert a==2**vp(n,2) and b==2
            AU.append(a);AV.append(b)
        for n in range(1,N+1):
            if n==1:
                expected_u=1
                expected_v=2 if p==2 else 1
            elif p==2:
                expected_u=(2**(vp(n,2)-1)) if n&(n-1)==0 else 0
                expected_v=0
            else:
                expected_u=0
                expected_v=0
                if n==r:expected_u=p**e-1
                if n%r==0:
                    m=n//r
                    if m>1:
                        z=m;j=0
                        while z%p==0:z//=p;j+=1
                        if z==1:expected_u=p**(e+j-1)*(p-1)
                if t is not None and n%t==0:
                    m=n//t
                    sign=1 if m%2==1 else (-1 if m%4==2 else 0)
                    z=m//2 if m%2==0 else m
                    j=0
                    while z%p==0:z//=p;j+=1
                    if z==1:
                        expected_v=sign*(p**ev-1 if j==0 else p**(ev+j-1)*(p-1))
            assert fold(AU,n)==expected_u,(p,n,'U',fold(AU,n),expected_u)
            assert fold(AV,n)==expected_v,(p,n,'V',fold(AV,n),expected_v)
        for q in ps:
            for s in range(1,6):
                qs=q**s
                if qs>N:break
                for m in range(1,min(N//qs,15)+1):
                    if m%q==0:continue
                    n=m*qs;other=n//q
                    assert ru*(AU[n]-AU[other])%qs==0,(p,'U',ru,n,qs)
                    assert rv*(AV[n]-AV[other])%qs==0,(p,'V',rv,n,qs)
                    cases+=2
        if p>2 and r%2==0:
            assert fold(AV,2*t)<0
        if p==2:assert fold(AU,2)==1
    # Verify least repair obstruction at the rank, including one p-adic excursion.
    for p in ps:
        if p==2:continue
        r=next(n for n in range(1,p+2) if U[n]%p==0)
        e=vp(U[r],p)
        c=r//gcd(r,p-1)
        for q in ps:
            if r%q:continue
            qpart=1
            while r% (qpart*q)==0:qpart*=q
            d=r//qpart
            # across indices d*p^j*q^a, q^a=qpart; requiring all j=0,1 yields p-1
            A=[p**e-1,p**(e+1)-1]
            assert all(c*x%qpart==0 for x in A)
            if c%q==0:assert any((c//q)*x%qpart for x in A)
    print('VERIFY_OK',len(ps),'primes;',cases,'Dold modular comparisons; n<=',N)

if __name__=='__main__':do()
