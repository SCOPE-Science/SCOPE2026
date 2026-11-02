#!/usr/bin/env python3
"""Reproducible exact-arithmetic checks for the displayed dual-degree formula.
This program checks local valuation algebra and sample arithmetic; the proof
of Gauss birationality and geometric exhaustiveness is in RESULT.md.
"""
from math import gcd

def primes_up_to(m):
    out=[]
    for a in range(3,m+1,2):
        if all(a % b for b in range(2,int(a**0.5)+1)):
            out.append(a)
    return out

def proper_divisors(a):
    return [n for n in range(2,a) if a%n==0]

def case(p,e,n):
    q=p**e; N=q+1; r=N//n
    assert N == n*r and r >= 2 and n >= 2
    assert gcd(N,p) == gcd(n,p) == 1
    # At u=0 and u=-1 the poles of the rational function a^N have
    # orders r-1 and N-1=p^e, respectively.
    assert r-1 > 0 and N-1 == q
    # The derivative of h=x*c(u), u=x^n, has nonzero numerator:
    # 2(2n-1)u^2+(5n-3)u+(n-1), modulo p.
    dh=[(n-1)%p,(5*n-3)%p,(4*n-2)%p]
    assert any(dh), (p,e,n)
    B0=N*(n-1)
    if r==2:
        Binf=0; degree=N*(N-1)-B0
        assert degree==2*n*n
        return (q,n,r,degree,False)
    g=gcd(r,2)
    t_y=(N-1)*(r-2)//g
    t_x=n*(r-2)*r//g
    t_z0=(N-2*n-1)*r//g
    t_z1=(N-n-1)*r//g
    t_z = t_z1 if (r-2)%p==0 else min(t_z0,t_z1)
    # x and y have the claimed pole/zero orders at infinity.
    base=min(t_y,t_x,t_z)
    assert base == t_z0 + (2//g if (r-2)%p==0 else 0)
    assert base >= 0 and n*g>=1
    Binf=n*g*base
    assert Binf==N*(N-2*n-1) + (2*n if (r-2)%p==0 else 0)
    degree=N*(N-1)-B0-Binf
    assert degree == N*(n+1)-(2*n if (r-2)%p==0 else 0)
    assert degree>0
    return (q,n,r,degree,(r-2)%p==0)

if __name__=='__main__':
    examined=[]
    for p in primes_up_to(37):
        for e in range(1,6):
            q=p**e
            for n in proper_divisors(q+1):
                examined.append(case(p,e,n))
    assert case(3,2,2)==(9,2,5,26,True)
    assert case(3,1,2)==(3,2,2,8,False)
    assert case(5,1,2)==(5,2,3,18,False)
    assert case(5,3,18)==(125,18,7,2358,True)  # N=126, N*19-36
    assert any(ex for *_,ex in examined)
    assert any(not ex for *_,ex in examined)
    print('VERIFY_OK:',len(examined),'admissible parameter pairs; 4 explicit checks;')
    print(' examples:',[case(3,2,2),case(5,1,2),case(5,3,18)])
