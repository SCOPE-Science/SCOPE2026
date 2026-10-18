#!/usr/bin/env python3
"""Exact rational checks for the finite-volume local-resetting TASEP theorem.
Usage: python check.py (Python 3 standard library only)."""
from fractions import Fraction as F
from itertools import product

def generator(n, alpha, beta, r):
    size = 1 << n
    q = [[F(0) for _ in range(size)] for _ in range(size)]
    for s in range(size):
        moves = []
        if not (s & 1):
            moves.append((s | 1, alpha))
        if s & (1 << (n-1)):
            moves.append((s ^ (1 << (n-1)), beta))
        for i in range(n-1):
            if s & (1 << i) and not (s & (1 << (i+1))):
                moves.append((s ^ (1 << i) ^ (1 << (i+1)), F(1)))
        if not (s & 1):
            for i in range(1,n):
                if s & (1 << i):
                    moves.append((s ^ (1 << i) ^ 1, r))
        for t, rate in moves:
            q[t][s] += rate
            q[s][s] -= rate
    return q

def solve(A, b):
    A = [row[:] + [rhs] for row, rhs in zip(A, b)]
    n=len(b)
    for col in range(n):
        pivot=next(i for i in range(col,n) if A[i][col]!=0)
        A[col],A[pivot]=A[pivot],A[col]
        w=A[col][col]
        A[col]=[a/w for a in A[col]]
        for i in range(n):
            if i==col: continue
            z=A[i][col]
            if z:
                A[i]=[x-z*y for x,y in zip(A[i],A[col])]
    return [A[i][-1] for i in range(n)]

def stationary(n,alpha,beta,r):
    m=1<<n;Q=generator(n,alpha,beta,r)
    Q[-1]=[F(1)]*m
    rhs=[F(0)]*m;rhs[-1]=F(1)
    return solve(Q,rhs)

def coeff(n,a,b,s):
    A=1
    B=2 # 0,1,0,...
    if s==A:return None
    if s==B:return F(1)
    if n==2 and s==0:return b/a
    if s&1 and s.bit_count()==2:
        k=next(i+1 for i in range(1,n) if s&(1<<i))
        if k==n:return a/b
        if n>=3:return a*(b+F(1,2))/b*F(3,2)**(n-1-k)
    return F(0)

num=0
for n in range(2,6):
    for a,b in [(F(3,10),F(1,5)),(F(3,4),F(7,5)),(F(5,2),F(2,3))]:
        for r in [F(10000),F(100000)]:
            pi=stationary(n,a,b,r)
            assert sum(pi)==1 and all(x>=0 for x in pi)
            num+=2
            Q=generator(n,a,b,r)
            for i in range(1<<n):
                assert sum(Q[i][j]*pi[j] for j in range(1<<n))==0
                num+=1
            for state,p in enumerate(pi):
                c=coeff(n,a,b,state)
                if c is None:continue
                error=abs(r*p-c)
                # First-order fixed-volume asymptotic; generous constant accounts for large occupancies.
                assert error <= F(5000000,r), (n,a,b,r,state,float(error),float(c))
                num+=1
            p_e=sum(p for s,p in enumerate(pi) if not(s&1))
            p_2=sum(p for s,p in enumerate(pi) if s&2)
            p_e2=sum(p for s,p in enumerate(pi) if not(s&1) and s&2)
            cov=(p_2-p_e2)-(1-p_e)*p_2
            assert abs(r*cov+1)<= F(5000000,r)
            num+=1
            if n>=3:
                assert abs(r*p_e-1)<=F(5000000,r)
                num+=1
            current=b*sum(p for s,p in enumerate(pi) if s&(1<<(n-1)))
            target=a+b if n==2 else a
            assert abs(r*current-target) <= F(5000000,r)
            num+=1
# Algebraic flux balances for reduced chain, arbitrary positive rate pairs and N.
for n in range(3,31):
    for a,b in [(F(1,3),F(1,2)),(F(7,4),F(2,7))]:
        c={j:coeff(n,a,b,1|(1<<(j-1))) for j in range(2,n+1)}
        assert c[n]*b==a
        num+=1
        assert c[2]==a+sum(c[j]/2 for j in range(3,n+1))
        num+=1
        for j in range(3,n):
            assert c[j-1]==F(3,2)*c[j]
            num+=1
        assert c[n-1]==(b+F(1,2))*c[n]
        num+=1
print('PASS', num, 'exact rational assertions')
