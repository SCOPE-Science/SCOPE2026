#!/usr/bin/env python3
"""Reproduce exact two-hub spectral allocation identities (stdlib only).

The analytic minimization and symmetry reduction are written in RESULT.md;
finite enumerations below are checks, not substitutes for that proof.
"""
from fractions import Fraction as F
from math import sqrt, exp, log


def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def characteristic_coefficients(A):
    n=len(A)
    T=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    coeff=[F(1)]
    for k in range(1,n+1):
        T=mm(A,T)
        c=-sum(T[i][i] for i in range(n))/k
        coeff.append(c)
        for i in range(n):
            T[i][i]+=c
    return list(reversed(coeff))  # ascending powers


def polymul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out


def laplacian(m,u,v):
    n=m+2
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(2,n):
        for j,w in ((0,u),(1,v)):
            L[i][i]+=w; L[j][j]+=w
            L[i][j]-=w; L[j][i]-=w
    return L


def spectrum_poly(m,u,v):
    s=u+v
    f=[F(1)]
    for _ in range(m-1):
        f=polymul(f,[-s,F(1)])
    return polymul(polymul([F(0),F(1)],f),
                   [m*(m+2)*u*v,-(m+1)*s,F(1)])


def price_cost(m,p,q):
    p,q=sorted((float(p),float(q)))
    d=sqrt((m-2)/(m+2))
    k=sqrt(q/p)
    if k+1/k <= m*m-2:
        u,v=(1+d)/2,(1-d)/2
        C=m*(p*u+q*v)
        phase='leaf-hub coincidence'
    else:
        u=(m+1+k)/(m*(m+2))
        v=(m+1+1/k)/(m*(m+2))
        C=((m+1)*(p+q)+2*sqrt(p*q))/(m+2)
        phase='simple hub mode'
    return C,u,v,phase


def check():
    checks=0
    # Exact spectral polynomial, full matrices, and sharp high-price designs.
    for m in range(3,13):
        for k in (1,2,3,4,6,8,16,32,128):
            p=F(1); q=F(k*k)
            if F(k*k+1,k)>m*m-2:
                u=F(m+1+k,m*(m+2))
                v=F((m+1)*k+1,k*m*(m+2))
                C=F((m+1)*(1+k*k)+2*k,m+2)
                assert m*(p*u+q*v)==C
                assert (u+v)>=1
                assert F(1)-(m+1)*(u+v)+m*(m+2)*u*v==0
                checks+=3
                assert characteristic_coefficients(laplacian(m,u,v)) == spectrum_poly(m,u,v)
                checks+=1
            else:
                d2=F(m-2,m+2)
                assert (F(1)-d2)/4==F(1,m+2)
                # The boundary spectrum is exactly zero, 1 (m times), and m.
                assert polymul([F(0),F(1)],polymul(
                    [F(-1),F(1)], [F(-m),F(1)])) == [F(0),F(m),-F(m+1),F(1)]
                checks+=2
    # A dense independent ratio sweep never exceeds the analytical optimum.
    for m in (3,4,5,8,12):
        for p,q in ((1,1),(1,2),(1,8),(1,32),(1,64),(1,256),
                    (1,4096),(3,120),(17,2)):
            C,u,v,phase=price_cost(m,p,q)
            assert u>0 and v>0 and abs(m*(min(p,q)*u+max(p,q)*v)-C)<1e-7*max(C,1)
            best=0
            for j in range(1601):
                z=exp(-13+26*j/1600)
                s=z+1
                trace=(m+1)*s
                product=m*(m+2)*z
                lm=2*product/(trace+sqrt(max(0,trace*trace-4*product)))
                gap=min(s,lm)
                value=gap/(m*(min(p,q)*z+max(p,q)))
                best=max(best,value)
                assert value <= (1+2e-10)/C
                checks+=1
            assert best >= 0.98/C
            checks+=3
    return checks

if __name__=='__main__':
    print('PASS: %d exact identity, characteristic-polynomial and ratio-sweep checks' % check())
