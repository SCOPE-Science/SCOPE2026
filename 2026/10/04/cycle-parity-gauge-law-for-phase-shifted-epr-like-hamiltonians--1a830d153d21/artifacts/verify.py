#!/usr/bin/env python3
from fractions import Fraction
import cmath, math


def matmul(A,B):
    n=len(A); m=len(B[0]); q=len(B)
    return [[sum(A[i][k]*B[k][j] for k in range(q)) for j in range(m)] for i in range(n)]

def eye(n,one=1,zero=0):
    return [[one if i==j else zero for j in range(n)] for i in range(n)]

def trace(A):
    return sum(A[i][i] for i in range(len(A)))

def mpow(A,p):
    R=eye(len(A),1,0); B=A
    while p:
        if p&1: R=matmul(R,B)
        B=matmul(B,B); p//=2
    return R

def bit(x,i,n):
    return (x>>(n-1-i))&1

def cycle_matrix(n,s,phases,exact=False):
    z0=Fraction(0) if exact else 0j
    A=[[z0 for _ in range(1<<n)] for __ in range(1<<n)]
    for e in range(n):
        p,q=e,(e+1)%n
        if exact:
            z=s*phases[e]; zc=z
        else:
            z=s*cmath.exp(1j*phases[e]); zc=z.conjugate()
        for x in range(1<<n):
            bp,bq=bit(x,p,n),bit(x,q,n)
            if bp==0 and bq==0:
                A[x][x]+=1
                y=x | (1<<(n-1-p)) | (1<<(n-1-q))
                A[y][x]+=z
            elif bp==1 and bq==1:
                A[x][x]+=z*zc
                y=x & ~(1<<(n-1-p)) & ~(1<<(n-1-q))
                A[y][x]+=zc
    return A

def charpoly_faddeev(A):
    n=len(A); I=eye(n,1+0j,0j); B=I
    coeff=[1+0j]
    for k in range(1,n+1):
        AB=matmul(A,B)
        ck=-trace(AB)/k
        coeff.append(ck)
        B=[[AB[i][j]+(ck if i==j else 0) for j in range(n)] for i in range(n)]
    return coeff

def poly_from_roots(roots):
    c=[1+0j]
    for r in roots:
        d=[0j]*(len(c)+1)
        for i,a in enumerate(c):
            d[i]+=a; d[i+1]-=a*r
        c=d
    return c

def check_c3():
    tests=[(0.2,[0.3,1.1,-0.7]),(0.57,[2.2,-1.3,0.41]),(0.91,[0.8,2.6,-2.1])]
    for s,ph in tests:
        A=cycle_matrix(3,s,ph)
        H=[[-x for x in row] for row in A]
        got=charpoly_faddeev(H)
        roots=[-(3+s*s),-(1+3*s*s),-1,-1,-s*s,-s*s,0,0]
        want=poly_from_roots(roots)
        err=max(abs(a-b) for a,b in zip(got,want))
        assert err<2e-8,(s,err)

def check_c4_exact():
    for s in [Fraction(1,2),Fraction(2,3),Fraction(3,5)]:
        A0=cycle_matrix(4,s,[Fraction(1),Fraction(1),Fraction(1),Fraction(1)],exact=True)
        Api=cycle_matrix(4,s,[Fraction(1),Fraction(1),Fraction(1),Fraction(-1)],exact=True)
        tr0=trace(mpow(A0,4)); trpi=trace(mpow(Api,4))
        assert tr0-trpi==96*s**4,(s,tr0-trpi,96*s**4)
        const=4*(81+124*s**2+122*s**4+124*s**6+81*s**8)
        assert tr0==const+48*s**4
        assert trpi==const-48*s**4

if __name__=='__main__':
    check_c3(); check_c4_exact()
    print('VERIFY_OK')
