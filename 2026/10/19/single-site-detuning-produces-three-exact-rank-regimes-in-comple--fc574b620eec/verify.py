#!/usr/bin/env python3
"""Exact-rational quantum Cesaro-mixing rank verification for marked bicliques.
Uses the symmetric commutant, independently of spectral diagonalisation.
"""
from fractions import Fraction
from time import monotonic
from sympy import Matrix, Rational, zeros

def make_H(a, b, t):
    n = a+b
    H = zeros(n)
    H[0,0] = Rational(t.numerator,t.denominator)
    for i in range(a):
        for j in range(a,n): H[i,j] = H[j,i] = 1
    return H

def rank_via_commutant(a,b,t):
    H=make_H(a,b,t); n=H.rows
    pairs=[(i,j) for i in range(n) for j in range(i,n)]
    # Matrix columns are H K - K H, with K an elementary skew matrix;
    # the diagonal columns are attached afterward.
    C=[]
    for i in range(n):
        for j in range(i+1,n):
            K=zeros(n); K[i,j]=1; K[j,i]=-1
            A=H*K-K*H
            C.append([A[u,v] for u,v in pairs])
    D=[[int(u==v==i) for u,v in pairs] for i in range(n)]
    rankC=Matrix.hstack(*[Matrix(c) for c in C]).rank()
    rankAll=Matrix.hstack(*[Matrix(c) for c in C+D]).rank()
    return rankAll-rankC

def expected(a,b,t):
    if t==0: return a+b-(a==2)-(b==2)
    return a+b-(a==3)-(b==2)

if __name__=='__main__':
    st=monotonic(); count=0
    for a in range(2,7):
        for b in range(2,7):
            for t in (Fraction(0),Fraction(1,2),Fraction(-2),Fraction(3)):
                got=rank_via_commutant(a,b,t)
                want=expected(a,b,t)
                if got!=want:raise AssertionError((a,b,t,got,want))
                count+=1
                if count%25==0: print('progress',count,round(monotonic()-st,1),flush=True)
    print('VERIFY_OK exact_commutant_cases=',count,'elapsed=',round(monotonic()-st,2))
