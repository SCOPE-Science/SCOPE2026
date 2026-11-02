#!/usr/bin/env python3
"""Exact arithmetic checks for Hopf-torus harmonic sampling.
Uses only the Python standard library. Numerical experiments are not the proof.
"""
from fractions import Fraction
from math import gcd, isqrt


def weights(k):
    return [(u,v) for u in range(-k,k+1) for v in range(-k,k+1)
            if abs(u)+abs(v) <= k and (k-abs(u)-abs(v))%2 == 0]


def coeffs(k,u,v):
    m=(k-abs(u)-abs(v))//2
    c=[Fraction(1)]
    for j in range(m):
        c.append(-c[-1]*Fraction((m-j)*(m-j+abs(v)),(j+1)*(j+1+abs(u))))
    return c


def radial_value(k,u,v,s):
    m=(k-abs(u)-abs(v))//2
    return sum((c*s**a*(1-s)**(m-a) for a,c in enumerate(coeffs(k,u,v))),Fraction(0))


def independent(k,n,m):
    S=weights(k)
    return len({(u%n,v%m) for u,v in S})==len(S)


def predicted(k,n,m):
    return (n>=k+1 if n%2 else n>2*k) and (m>=k+1 if m%2 else m>2*k)


def prime(t):
    if t<2:return False
    for j in range(2,isqrt(t)+1):
        if t%j==0:return False
    return True


def prime_for(n):
    p=((1000000//n)+1)*n+1
    while not prime(p):p+=n
    return p


def primitive_root(p):
    j=p-1; factors=[]; q=2
    while q*q<=j:
        if j%q==0:
            factors.append(q)
            while j%q==0:j//=q
        q+=1
    if j>1:factors.append(j)
    for g in range(2,p):
        if all(pow(g,(p-1)//q,p)!=1 for q in factors):return g
    raise RuntimeError('No root')


def rank_mod(A,p):
    if not A:return 0
    rows=[row[:] for row in A]; R=len(rows); C=len(rows[0]); rank=0
    for col in range(C):
        pivot=next((j for j in range(rank,R) if rows[j][col]%p),None)
        if pivot is None:continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        inv=pow(rows[rank][col],-1,p)
        rows[rank][col:]=[a*inv%p for a in rows[rank][col:]]
        for j in range(rank+1,R):
            f=rows[j][col]
            if f:
                rows[j][col:]=[(a-f*b)%p for a,b in zip(rows[j][col:],rows[rank][col:])]
        rank+=1
        if rank==R:break
    return rank


def full_mod_rank(k,n,m):
    # Use s=2/9 in F_p. This is an independent finite-field evaluation
    # of the explicit *polynomial* harmonic basis (not an infinitude proof).
    S=weights(k)
    L=n*m//gcd(n,m)
    p=prime_for(L)
    if p<=7:
        p+=L
        while not prime(p):p+=L
    g=primitive_root(p); zn=pow(g,(p-1)//n,p); zm=pow(g,(p-1)//m,p)
    s=2*pow(9,-1,p)%p; y=(1-s)%p
    # Recover monomial z_1^+ zbar_1^- z_2^+ zbar_2^- at algebraic
    # radius using a formal sqrt in F_p, selecting p where s,y square.
    # Instead build Fourier angular model and check polynomial coefficients;
    # the diagonal nonzero factors of sqrt(s),sqrt(y) do not affect rank.
    def Q(k,u,v):
        M=(k-abs(u)-abs(v))//2; out=0
        for a,c in enumerate(coeffs(k,u,v)):
            out=(out+c.numerator*pow(c.denominator,-1,p)*pow(s,a,p)*pow(y,M-a,p))%p
        return out
    Qs=[Q(k,u,v) for u,v in S]
    assert all(Qs),'Unlucky modular radius/prime; use a different test.'
    mat=[]
    for i in range(n):
        for j in range(m):
            mat.append([Qs[t]*pow(zn,i*(u%n),p)*pow(zm,j*(v%m),p)%p
                        for t,(u,v) in enumerate(S)])
    return rank_mod(mat,p)


def check():
    nassert=0
    for k in range(0,13):
        S=weights(k)
        assert len(S)==(k+1)**2
        nassert+=1
        for u,v in S:
            cs=coeffs(k,u,v); M=(k-abs(u)-abs(v))//2
            assert cs[0]==1 and len(cs)==M+1
            for j in range(M):
                assert cs[j+1]*(j+1)*(j+1+abs(u))+cs[j]*(M-j)*(M-j+abs(v))==0
                nassert+=1
            if k<=8:
                assert radial_value(k,u,v,Fraction(2,9)) != 0
                nassert+=1
        for n in range(1,2*k+5):
            for m in range(1,2*k+5):
                assert independent(k,n,m)==predicted(k,n,m),(k,n,m)
                nassert+=1
        minimum=k+1 if k%2==0 else k+2
        assert minimum==min(n for n in range(1,3*k+5) if independent(k,n,n))
        nassert+=1
    tests=[(0,1,1),(1,2,2),(1,3,3),(2,2,3),(2,3,3),(2,3,4),
           (2,5,3),(3,4,4),(3,5,5),(3,5,4),(3,7,6),
           (4,5,5),(4,6,5),(4,7,7),(5,6,6),(5,7,7),(5,7,8)]
    for k,n,m in tests:
        assert full_mod_rank(k,n,m)==len({(u%n,v%m) for u,v in weights(k)}),(k,n,m)
        nassert+=1
    print('HOPF_GRID_CHECK_OK',nassert,'exact assertion groups',len(tests),'independent finite-field matrix ranks')

if __name__=='__main__':check()
