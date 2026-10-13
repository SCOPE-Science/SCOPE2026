#!/usr/bin/env python3
"""Reproduce the finite checks for the square-torus Crank--Nicolson threshold.
No nonstandard modules required. Universal assertions are proved in RESULT.md.
"""
from fractions import Fraction as F
from math import cos, pi, sqrt, isclose


def inverse(M):
    n = len(M)
    A = [list(M[i]) + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        piv = next(i for i in range(k,n) if A[i][k])
        A[k],A[piv] = A[piv],A[k]
        c = A[k][k]
        A[k] = [q/c for q in A[k]]
        for i in range(n):
            if i != k and A[i][k]:
                c = A[i][k]
                A[i] = [A[i][j]-c*A[k][j] for j in range(2*n)]
    return [row[n:] for row in A]


def direct(n,s):
    N=n*n
    B = [[F(int(i==j)) for j in range(N)] for i in range(N)]
    for a in range(N):
        x,y=divmod(a,n)
        B[a][a]+=4*s
        for xx,yy in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            B[a][(xx%n)*n+yy%n]-=s
    R = inverse(B)
    T = [[2*R[i][j]-int(i==j) for j in range(N)] for i in range(N)]
    assert all(sum(row)==1 for row in T)
    assert all(T[i][j]>0 for i in range(N) for j in range(N) if i!=j)
    assert all(T[i][i]==T[0][0] for i in range(N))
    return T[0][0], R[0][0]


def g(n,s):
    z=[2-2*cos(2*pi*j/n) for j in range(n)]
    return sum(1/(1+s*(z[j]+z[k]-0)) for j in range(n) for k in range(n))/(n*n)


def bisect_root(f,lo,hi,it=85):
    assert f(lo)>0 and f(hi)<0
    for _ in range(it):
        m=(lo+hi)/2
        if f(m)>0:lo=m
        else: hi=m
    return (lo+hi)/2


def ellipk(k):
    a,b=1.0,sqrt(1-k*k)
    while abs(a-b)>1e-15:
        a,b=(a+b)/2,sqrt(a*b)
    return pi/(2*a)


def ginf(s):
    z=1+4*s
    return 2/(pi*z)*ellipk(4*s/z)


if __name__ == '__main__':
    checks=0
    for n in (3,4):
        for s in (F(1,4),F(1,3)):
            diag,ginv=direct(n,s)
            assert (diag>0) == (s==F(1,4))
            assert diag==2*ginv-1
            assert abs(float(ginv)-g(n,float(s)))<3e-13
            checks+=n**4+2
    s3=(1+sqrt(57))/28
    assert abs(14*s3*s3-s3-1)<1e-13
    assert abs(g(3,s3)-0.5)<1e-13
    checks+=2
    sinf=bisect_root(lambda s:ginf(s)-0.5,0.1,1.)
    roots=[]
    for n in (3,4,5,6,7,8,10,12,16,20):
        sn=bisect_root(lambda s:g(n,s)-0.5,0.1,1.)
        roots.append(sn)
        assert sn>sinf-1e-12
        assert abs(g(n,sn)-0.5)<1e-12
        checks+=2
    assert all(roots[i]>roots[i+1]+1e-13 for i in range(len(roots)-1))
    assert abs(roots[0]-s3)<1e-12
    assert abs(sinf-0.29409864184281406)<2e-14
    r=4*sinf/(1+4*sinf)
    for n,sn in zip((3,4,5,6,7,8,10,12,16,20),roots):
        ub=(1+8*s3)**2*r**n/(1-r**n)**2
        assert 0<sn-sinf<ub
        checks+=1
    print('VERIFY_OK',checks,'rational matrix entries and Fourier/elliptic thresholds')
    print('s_infinity=%.16f h_infinity=%.16f'%(sinf,2*sinf))
    print('s_3=%.16f h_3=%.16f'%(s3,2*s3))
