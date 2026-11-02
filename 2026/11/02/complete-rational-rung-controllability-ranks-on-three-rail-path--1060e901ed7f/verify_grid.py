#!/usr/bin/env python3
"""Exact finite-field tests of controllability ranks on anisotropic three-rail grids."""
from fractions import Fraction
from math import gcd

def theoretical(n,s,p,r):
    r=Fraction(r)
    q=2*s-1
    g=gcd(n,q)
    active=n-(g-1)//2
    D=lambda x:int(n%x==0)
    A=lambda x: int(n%x==0 and q%x!=0)
    if p==2: # vertical coordinate 2, only modes 0 and 3
        return 2*active-int(r==1 and n%3==0)
    if r==1:
        loss=2*A(3) + D(6)*(q%3!=0)+2*A(5)+D(2)+D(3)
    elif r==2:
        loss=D(2)+A(3)
    elif r==Fraction(3,2) or r==3:
        loss=D(3)
    else:
        loss=0
    return 3*active-loss

def modular_rank(n,s,p,r,mod):
    r=Fraction(r)
    a,b=r.numerator,r.denominator
    a%=mod; b%=mod
    N=3*n
    bvec=[0]*N
    bvec[(p-1)*n+(s-1)]=1
    edges=[]
    for j in range(3):
        for k in range(n-1):
            edges.append((j*n+k,j*n+k+1,b))
    for j in range(2):
        for k in range(n):
            edges.append((j*n+k,(j+1)*n+k,a))
    pivots={}
    rank=0
    v=bvec
    for k in range(N):
        u=v[:]
        for loc in sorted(pivots):
            alpha=u[loc]
            if alpha:
                w=pivots[loc]
                for i in range(loc,N):u[i]=(u[i]-alpha*w[i])%mod
        loc=next((i for i,z in enumerate(u) if z),None)
        if loc is not None:
            inv=pow(u[loc],-1,mod)
            pivots[loc]=[0]*loc+[(x*inv)%mod for x in u[loc:]]
            rank+=1
        if rank==N:
            return rank
        vv=[0]*N
        for i,j,w in edges:
            d=(v[i]-v[j])*w%mod
            vv[i]=(vv[i]+d)%mod
            vv[j]=(vv[j]-d)%mod
        v=vv
    return rank

if __name__=='__main__':
    from time import perf_counter
    t0=perf_counter()
    rs=[Fraction(1),Fraction(3,2),Fraction(2),Fraction(3),Fraction(4,3),Fraction(5,4),Fraction(7,3),Fraction(4)]
    total=0
    for n in range(2,17):
        for s in range(1,n+1):
            for p in (1,2,3):
                for r in rs:
                    expected=theoretical(n,s,p,r)
                    observed=modular_rank(n,s,p,r,1000003)
                    assert observed==expected,(n,s,p,r,observed,expected)
                    total+=1
    print(f'PASS: {total} exact modular Krylov rank matches (n=2..16, all sites, 8 rational weights, modulus 1000003), elapsed {perf_counter()-t0:.2f}s')
    for n,s,p,r in [(3,1,1,1),(6,1,1,1),(10,1,1,1),(15,1,1,1),(30,1,1,1),(6,2,2,Fraction(4,3)),(16,1,1,Fraction(4,3))]:
        print(f'n={n},s={s},row={p},r={r},analytic rank={theoretical(n,s,p,r)} of {3*n}')
