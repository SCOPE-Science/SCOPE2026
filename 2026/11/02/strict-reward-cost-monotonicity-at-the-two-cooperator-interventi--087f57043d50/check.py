"""Reproduce the exact two-cooperator institutional reward Green kernel.
Only standard-library modules are required; every matrix comparison is rational.
"""
from fractions import Fraction as Q
from math import log, exp
from random import Random


def solve(a, b):
    n=len(b)
    a=[list(row)+[b[i]] for i,row in enumerate(a)]
    for j in range(n):
        k=next(k for k in range(j,n) if a[k][j])
        a[j],a[k]=a[k],a[j]
        p=a[j][j]
        a[j]=[v/p for v in a[j]]
        for i in range(n):
            if i!=j:
                v=a[i][j]
                a[i]=[a[i][h]-v*a[j][h] for h in range(n+1)]
    return [row[-1] for row in a]


def b_formula(n, r, R):
    T=sum((R**i for i in range(n-2)),Q(0))
    return (1+r)*((1+r*T)/Q(n-1)+T/Q(n-2))/(1+r+r*r*T)


def b_markov(n,r,R):
    m=n-1
    p=[None]+[Q(1)/(1+(r if j<=2 else R)) for j in range(1,n)]
    mat=[[Q(int(i==j)) for j in range(m)] for i in range(m)]
    cost=[Q(0)]*m
    for j in range(1,n):
        i=j-1
        h=Q(j*(n-j),n*n)
        mat[i][i]=h # I-U has diagonal h
        if j>1: mat[i][i-1]-=h*(1-p[j])
        if j<n-1:mat[i][i+1]-=h*p[j]
        cost[i]=Q(j) if j<=2 else Q(0)
    value=solve(mat,cost)
    return value[0]/Q(n*n)


def b_derivative(n,r,R):
    T=sum(R**i for i in range(n-2))
    A=1/(n-1);C=1/(n-2)
    K=A+C*T;L=A*T
    D=1+r+T*r*r
    B=(1+r)*(K+L*r)/D
    Bd=(L-2*C*T*T*r-(A+C)*T*T*r*r)/D**2
    return B,Bd


def main():
    total=0
    for n in range(4,11):
        for R in [Q(11,10),Q(2),Q(3),Q(5),Q(10)]:
            for r in [Q(1,10),Q(1,3),Q(1,2),Q(1),Q(2),Q(4)]:
                if r>R:continue
                assert b_formula(n,r,R)==b_markov(n,r,R),(n,R,r)
                total+=1
    rng=Random(812)
    nd=0
    for _ in range(10000):
        n=rng.randint(4,40)
        R=1+10**rng.uniform(-3,1.2)
        r=R*exp(-rng.uniform(0,23))
        B,Bd=b_derivative(n,r,R)
        deriv=B-log(R/r)*r*Bd
        assert deriv>0,(n,R,r,deriv)
        nd+=1
    # Algebraic boundary checks independent of logs, across rational samples
    for n in range(4,18):
        for R in [1.01,2,5,25]:
            T=sum(R**i for i in range(n-2))
            A=1/(n-1);C=1/(n-2)
            for r in [1e-10,1/(8*T),1/(3*T),1, R]:
                B,Bd=b_derivative(n,r,R)
                if Bd>0:
                    assert r<1/(2*T)
                    assert Bd/B<1/(1+r)
                    assert r*log(R/r)<1
    print('PASS: %d exact-rational Green-kernel cases; %d positive-derivative numerical cases; analytic intermediate bounds.'%(total,nd))

if __name__=='__main__':main()
