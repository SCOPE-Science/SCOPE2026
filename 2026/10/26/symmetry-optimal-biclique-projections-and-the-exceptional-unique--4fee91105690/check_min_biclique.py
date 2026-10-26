#!/usr/bin/env python3
"""Exact rational checks for complete-bipartite cut/cycle projections."""
from fractions import Fraction as F
from itertools import product

def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def check(m,n):
    d=m*n
    C=[[(F(int(i==k))-F(1,m))*(F(int(j==l))-F(1,n))
        for k,l in product(range(m),range(n))]
       for i,j in product(range(m),range(n))]
    I=[[F(int(i==j)) for j in range(d)] for i in range(d)]
    Q=[[I[i][j]-C[i][j] for j in range(d)] for i in range(d)]
    assert matmul(C,C)==C and matmul(Q,Q)==Q
    assert matmul(C,Q)==[[F(0)]*d for _ in range(d)]
    assert all(sum(C[i*n+j][col] for i in range(m))==0 for j in range(n) for col in range(d))
    assert all(sum(C[i*n+j][col] for j in range(n))==0 for i in range(m) for col in range(d))
    c1=max(sum(abs(C[i][j]) for i in range(d)) for j in range(d))
    q1=max(sum(abs(Q[i][j]) for i in range(d)) for j in range(d))
    cinf=max(sum(abs(v) for v in row) for row in C)
    qinf=max(sum(abs(v) for v in row) for row in Q)
    assert c1==cinf==F(4*(m-1)*(n-1),m*n),(m,n,'cycle')
    assert q1==qinf==F(3*m*n-2*m-2*n+2,m*n),(m,n,'cut')
    assert c1-q1==F((m-2)*(n-2)-2,m*n)
    if m*n>4:
        z=[F(0)]*d
        for i,j,a in [(0,0,1),(0,1,-1),(1,0,-1),(1,1,1)]:
            z[i*n+j]=F(a)
        b=[F(int(j==2)) if n>=3 else F(int(i==2))
           for i,j in product(range(m),range(n))]
        eps=F(1,2*m*n)
        T=[[eps*z[i]*b[j] for j in range(d)] for i in range(d)]
        P=[[C[i][j]+T[i][j] for j in range(d)] for i in range(d)]
        assert any(any(t for t in row) for row in T)
        assert matmul(P,P)==P
        assert max(sum(abs(P[i][j]) for i in range(d)) for j in range(d))==c1
        assert all(sum(P[i*n+j][col] for i in range(m))==0 for j in range(n) for col in range(d))
        assert all(sum(P[i*n+j][col] for j in range(n))==0 for i in range(m) for col in range(d))
    return d

if __name__=='__main__':
    cases=0
    columns=0
    for m in range(2,10):
      for n in range(2,10):
        columns+=check(m,n); cases+=1
    print('PASS',cases,'biclique parameter pairs;',columns,'exact edge columns; projections, norms, thresholds and alternative optimizers.')
