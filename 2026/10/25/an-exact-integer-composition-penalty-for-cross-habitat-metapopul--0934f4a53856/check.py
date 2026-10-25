#!/usr/bin/env python3
"""Independent finite block-matrix and integer-threshold checks.
Python >=3.9; standard library only. This code tests instances, not the theorem's universal quantifiers.
"""
from fractions import Fraction
from math import sqrt, floor, ceil, isclose
from random import Random

def direct_threshold(N, delta, a, b, k):
    return ((delta-a*(k-1))*(delta-b*(N-k-1)))/(k*(N-k))

def predicted(N, delta, a, b):
    U,V = delta+a,delta+b
    B,C = delta-a*(N-1),delta-b*(N-1)
    assert N>=2 and a>0 and b>0 and B>0 and C>0
    s0=sqrt(U*C/(B*V))
    k0=N*s0/(1+s0)
    R0=(sqrt(U*V)+sqrt(B*C))**2/N**2
    options=sorted({k for k in (floor(k0),ceil(k0)) if 1<=k<N})
    kval=min(options,key=lambda k:direct_threshold(N,delta,a,b,k))
    return k0,R0,kval,direct_threshold(N,delta,a,b,kval),options

def jacobi_largest(mat):
    n=len(mat)
    a=[list(map(float,row)) for row in mat]
    for _ in range(100*n*n):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda t:abs(a[t[0]][t[1]]))
        if abs(a[p][q])<1e-12:break
        tau=(a[q][q]-a[p][p])/(2*a[p][q])
        t=(1 if tau>=0 else -1)/(abs(tau)+sqrt(1+tau*tau))
        c=1/sqrt(1+t*t); s=t*c
        app,aqq,apq=a[p][p],a[q][q],a[p][q]
        a[p][p]=app-t*apq; a[q][q]=aqq+t*apq
        a[p][q]=a[q][p]=0.0
        for k in range(n):
            if k==p or k==q:continue
            akp,akq=a[k][p],a[k][q]
            a[k][p]=a[p][k]=c*akp-s*akq
            a[k][q]=a[q][k]=s*akp+c*akq
    return max(a[i][i] for i in range(n))

def full_rho(N,k,a,b,c):
    m=[[0.0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i==j:continue
            m[i][j]=a if i<k and j<k else b if i>=k and j>=k else c
    return jacobi_largest(m)

def reduced_rho(N,k,a,b,c):
    x=a*(k-1); y=b*(N-k-1)
    return (x+y+sqrt((x-y)**2+4*c*c*k*(N-k)))/2

def run():
    rng=Random(450624)
    count=0
    for _ in range(1200):
        N=rng.randrange(2,13)
        delta=rng.uniform(.7,9)
        a=rng.uniform(.015,delta/(N-1)*.98)
        b=rng.uniform(.015,delta/(N-1)*.98)
        k0,R0,kbest,Rbest,options=predicted(N,delta,a,b)
        allR=[direct_threshold(N,delta,a,b,k) for k in range(1,N)]
        assert isclose(Rbest,min(allR),rel_tol=5e-12,abs_tol=1e-12)
        U,V=delta+a,delta+b
        B,C=delta-a*(N-1),delta-b*(N-1)
        H=sqrt(U*V*B*C)
        for k in range(1,N):
            R=allR[k-1]
            penalty=H*(k-k0)**2/(k*k0*(N-k)*(N-k0))
            assert isclose(R-R0,penalty,rel_tol=1e-7,abs_tol=3e-10),(N,k,R,R0,penalty)
            for factor in (.93,1.,1.07):
                c=sqrt(R)*factor
                full=full_rho(N,k,a,b,c)
                reduced=reduced_rho(N,k,a,b,c)
                assert isclose(full,reduced,rel_tol=1e-9,abs_tol=1e-9)
                assert (full>delta)==(factor>1) if factor!=1 else abs(full-delta)<1e-8
                count+=1
    N=5; delta=Fraction(5); a=b=Fraction(1)
    assert direct_threshold(N,delta,a,b,2)==Fraction(2)
    assert direct_threshold(N,delta,a,b,3)==Fraction(2)
    assert direct_threshold(N,delta,a,b,1)==Fraction(5,2)
    assert direct_threshold(N,delta,a,b,4)==Fraction(5,2)
    assert Fraction(49,25)<Fraction(141*141,10000)<Fraction(2)
    assert full_rho(5,2,1,1,1.41)<5
    assert full_rho(5,2,1,1,1.42)>5
    print(f'PASS {count} independently diagonalized configurations, 1200 global discrete optimizations, penalty identities, exact N=5 example')
if __name__=='__main__':run()
