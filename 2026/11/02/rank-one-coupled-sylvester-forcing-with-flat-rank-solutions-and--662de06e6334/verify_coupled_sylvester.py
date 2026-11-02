#!/usr/bin/env python3
"""Exact checks of the coupled Sylvester construction; uses only Python's standard library."""
from fractions import Fraction
from math import sqrt


def matrix(n):
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def mm(A,B):
    n=len(A)
    return [[sum((A[i][j]*B[j][k] for j in range(n)),Fraction(0)) for k in range(n)] for i in range(n)]


def add(A,B):
    return [[a+b for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]


def neg(A):
    return [[-x for x in row] for row in A]


def subtract(A,B):
    return add(A,neg(B))


def norm2(A):
    return sum((x*x for row in A for x in row),Fraction(0))


def ident(n):
    D=matrix(n)
    for i in range(n): D[i][i]=Fraction(1)
    return D


def make(n,tau):
    P=matrix(n);Q=matrix(n);E=ident(n)
    for j in range(n-1): P[j+1][j]=Q[j+1][j]=Fraction(1)
    P[0][n-1]=Fraction(1);Q[0][n-1]=Fraction(-1)
    E[0][0]+=tau
    F1=neg(subtract(P,Q));F2=subtract(E,ident(n))
    return P,Q,E,F1,F2


def power(A,n):
    X=ident(len(A))
    for _ in range(n): X=mm(X,A)
    return X


def check():
    count=0
    for n in range(2,12):
      for tau in [Fraction(1,8),Fraction(1,2),Fraction(1)]:
        P,Q,E,F1,F2=make(n,tau)
        I=ident(n)
        assert power(P,n)==I;count+=1
        assert power(Q,n)==neg(I);count+=1
        assert norm2(F1)==4;assert norm2(F2)==tau*tau;count+=2
        # Exact solution (X,Y)=(I,-I) of A1 X + Y A2=-F1,
        # E1 X + Y E2=-F2.
        assert add(add(mm(P,I),mm(neg(I),Q)),F1)==matrix(n);count+=1
        assert add(add(I,mm(neg(I),E)),F2)==matrix(n);count+=1
        # Characteristic equation: (E^-1 Q)^n=-(1+tau)^-1 I.
        Einv=ident(n);Einv[0][0]=1/(1+tau)
        W=mm(Einv,Q)
        target=[[(-1/(1+tau))*x for x in row] for row in I]
        assert power(W,n)==target;count+=1
        for k in range(1,n):
            K=matrix(n)
            for j in range(k): K[j][j]=Fraction(1)
            R1=add(add(mm(P,K),mm(neg(K),Q)),F1)
            R2=add(add(K,mm(neg(K),E)),F2)
            assert norm2(R1)==2;count+=1
            assert norm2(R2)==0;count+=1
            assert norm2(mm(P,K))==k and norm2(mm(K,Q))==k;count+=1
            assert norm2(subtract(I,K))==n-k;count+=1
            assert abs((sqrt(float(norm2(R1))) / (2*sqrt(k)+2)) -
                      (sqrt(2)/(2*sqrt(k)+2))) < 1e-13;count+=1
    print('EXACT_CHECKS_OK',count)

if __name__=='__main__': check()
