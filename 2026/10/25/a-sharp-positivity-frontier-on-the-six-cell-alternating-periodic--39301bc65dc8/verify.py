#!/usr/bin/env python3
"""Exact rational test suite for the six-element alternating mesh identities.
No dependencies outside the Python standard library. Finite tests supplement analytic proof.
"""
from fractions import Fraction as F

def invert(A):
    n=len(A)
    T=[A[i][:]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if T[i][k])
        T[k],T[pivot]=T[pivot],T[k]
        div=T[k][k]
        T[k]=[z/div for z in T[k]]
        for i in range(n):
            if i!=k:
                z=T[i][k]
                T[i]=[v-z*w for v,w in zip(T[i],T[k])]
    return [line[n:] for line in T]

def matrix(a,b,t):
    n=6
    M=[[F(0) for _ in range(n)] for _ in range(n)]
    K=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        j=(i+1)%n
        h=a if i%2==0 else b
        for x in (i,j):
            M[x][x]+=h/3
            K[x][x]+=1/h
        M[i][j]+=h/6
        M[j][i]+=h/6
        K[i][j]-=1/h
        K[j][i]-=1/h
    D=[[M[i][j]+t*K[i][j] for j in range(n)] for i in range(n)]
    I=invert(D)
    P=[[sum(I[i][k]*M[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    return M,K,P

def run():
    checks=0
    lengths=[F(1,4),F(1,2),F(1),F(2),F(3),F(7)]
    steps=[F(0),F(1,100),F(1,12),F(1,6),F(1,2),F(1),F(2),F(8),F(17)]
    for a in lengths:
        for b in lengths:
            for t in steps:
                M,K,P=matrix(a,b,t)
                den=(a*b+6*t)*(a*b+12*t)*(a*a+3*a*b+b*b+6*t)
                f02=2*t*(6*t-a*a)*(a*b+b*b+6*t)/den
                f04=2*t*(6*t-b*b)*(a*a+a*b+6*t)/den
                assert P[0][2]==f02 and P[0][4]==f04
                assert all(sum(P[i])==1 for i in range(6))
                assert all(M[i][j]==M[j][i] and K[i][j]==K[j][i]
                           for i in range(6) for j in range(6))
                positive=(t==0 or 6*t>=max(a*a,b*b))
                assert all(P[i][j]>=0 for i in range(6) for j in range(6))==positive
                checks+=1
    print('PASS',checks,'exact rational matrix configurations')
if __name__=='__main__': run()
