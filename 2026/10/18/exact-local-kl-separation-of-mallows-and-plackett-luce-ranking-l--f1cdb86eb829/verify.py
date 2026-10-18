#!/usr/bin/env python3
"""Exact finite checks of a local ranking-law separation identity."""
from fractions import Fraction as F
from itertools import permutations

def harm(n):
    return sum((F(1,j) for j in range(1,n+1)),F(0))

def inversion(pi):
    return sum(pi[i] > pi[j] for i in range(len(pi)) for j in range(i+1,len(pi)))

def coefficient(n):
    H=harm(n)
    return F(n*(n-1)*(2*n+5),144)-F(n*(n*n-1)*(n-1),96)/(n-H)

def check(n):
    P=list(permutations(range(1,n+1)))
    M=len(P)
    E=lambda vals: sum(vals,F(0))/M
    z=[F(inversion(p))-F(n*(n-1),4) for p in P]
    S=[[F(1)-sum((F(1,n-t+1) for t in range(1,p.index(i)+2)),F(0)) for i in range(1,n+1)] for p in P]
    assert E(z)==0
    for i in range(n): assert E(row[i] for row in S)==0
    g=F(n,1)-harm(n)
    eig=g/F(n-1)
    for i in range(n):
        for j in range(n):
            moment=E(row[i]*row[j] for row in S)
            assert moment==(g/F(n) if i==j else -g/F(n*(n-1)))
        assert E(z[k]*S[k][i] for k in range(M))==F(2*(i+1)-n-1,4)
    vv=E(x*x for x in z)
    assert vv==F(n*(n-1)*(2*n+5),72)
    bsq=sum((F(2*i-n-1,4)**2 for i in range(1,n+1)),F(0))
    assert vv/2-bsq/(2*eig)==coefficient(n)
    if n==2: assert coefficient(n)==0
    else: assert coefficient(n)>0

if __name__=='__main__':
    for n in range(2,7):check(n)
    assert coefficient(3)==F(5,168)
    print('PASS: five exact permutation dimensions and harmonic-number projection identities')
