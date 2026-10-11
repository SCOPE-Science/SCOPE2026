#!/usr/bin/env python3
"""Integer sanity checks of explicit companion-family identities; no external dependencies."""
from math import gcd
from itertools import permutations

def multiply(A,B):
    n=len(A)
    return [[sum(A[i][z]*B[z][j] for z in range(n)) for j in range(n)] for i in range(n)]

def determinant(A):
    n=len(A)
    B=[list(x) for x in A]
    sign=1; den=1
    for i in range(n-1):
        if B[i][i]==0:
            j=next((j for j in range(i+1,n) if B[j][i]),None)
            if j is None:return 0
            B[i],B[j]=B[j],B[i];sign=-sign
        pivot=B[i][i]
        for j in range(i+1,n):
            for q in range(i+1,n):
                num=B[j][q]*pivot-B[j][i]*B[i][q]
                assert num%den==0
                B[j][q]=num//den
            B[j][i]=0
        den=pivot
    return sign*B[-1][-1]

def test(d,k):
    m=2*d
    A=[[0]*m for _ in range(m)]
    for j in range(m-1):A[j+1][j]=1
    A[0][m-1]=-k
    I=[[int(i==j) for j in range(m)] for i in range(m)]
    assert abs(determinant(A))==k
    power=I
    for n in range(1,15):
        power=multiply(power,A)
        if n==m:
            assert power==[[-k*int(i==j) for j in range(m)] for i in range(m)]
        g=gcd(m,n)
        M=[[I[i][j]-power[i][j] for j in range(m)] for i in range(m)]
        assert abs(determinant(M))==abs(1-(-k)**(n//g))**g,(d,k,n)

if __name__=='__main__':
    for dimension in range(1,5):
        for degree in (2,3,5,7):test(dimension,degree)
    print('PASS: exact determinant identities for dimensions 1..4, degrees 2,3,5,7 and iterates 1..14')
