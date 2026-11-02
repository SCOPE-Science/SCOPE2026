#!/usr/bin/env python3
"""Exact finite checks for fixed-point/succession covariance in uniform permutations.

Standard-library only; enumerates finite sample spaces. The general theorem is
proved separately; finite enumeration is not used as an infinite proof.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial

def matrix_rank(A):
    A = [[Fraction(v) for v in row] for row in A]
    m, n = len(A), len(A[0]); r=0
    for c in range(n):
        k=next((k for k in range(r,m) if A[k][c]), None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]
        pivot=A[r][c]
        A[r]=[v/pivot for v in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[u-z*v for u,v in zip(A[i],A[r])]
        r+=1
        if r==m: break
    return r

def expected_cov(n,j,i):
    positive = (j in (1,n,i,i+1))
    return Fraction(n-2 if positive else -2, n*n*(n-1)*(n-2))

def test():
    assertions=0
    for n in range(3,9):
        nf=factorial(n)
        sAB=[[0]*(n-1) for _ in range(n)]
        fU=0; f2=0; u2=0; f1=0; u1=0
        for p in permutations(range(1,n+1)):
            a=[int(p[j-1]==j) for j in range(1,n+1)]
            b=[int(p[i]==p[i-1]+1) for i in range(1,n)]
            for j,aj in enumerate(a):
                if aj:
                    for i,bi in enumerate(b):
                        sAB[j][i]+=bi
            f=sum(a);u=sum(b)
            fU+=f*u;f2+=f*f;u2+=u*u;f1+=f;u1+=u
        for j in range(1,n+1):
            for i in range(1,n):
                actual=Fraction(sAB[j-1][i-1],nf)-Fraction(1,n*n)
                expect=expected_cov(n,j,i)
                assert actual==expect,(n,i,j,actual,expect)
                assertions+=1
        assert Fraction(f1,nf)==1; assertions+=1
        assert Fraction(u1,nf)==Fraction(n-1,n); assertions+=1
        assert Fraction(f2,nf)-1==1; assertions+=1
        assert Fraction(u2,nf)-Fraction((n-1)**2,n*n)==Fraction(n*n-n-1,n*n); assertions+=1
        assert Fraction(fU,nf)-Fraction(n-1,n)==Fraction(2,n*(n-1)); assertions+=1
    for n in range(3,31):
        A=[[expected_cov(n,j,i) for i in range(1,n)] for j in range(1,n+1)]
        expected_rank=n-1 if n%2==0 else n-2
        assert matrix_rank(A)==expected_rank,(n,matrix_rank(A),expected_rank); assertions+=1
        if n%2:
            alt=[(-1)**i for i in range(n-1)]
            assert all(sum(v*z for v,z in zip(row,alt))==0 for row in A); assertions+=1
        assert sum(sum(row) for row in A)==Fraction(2,n*(n-1)); assertions+=1
    print(f'PASS {assertions} assertion groups; exhaustive permutations through n=8; exact matrix rank n=3..30')

if __name__=='__main__': test()
