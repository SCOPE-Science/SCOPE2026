#!/usr/bin/env python3
"""Exact finite checks for priced-wheel resistance formulas.

These tests corroborate, but do not establish, general dimension or asymptotic assertions.
Only Python standard-library Fraction arithmetic is used.
"""
from fractions import Fraction as Q


def mat_inv(A):
    n=len(A)
    R=[[Q(a) for a in row]+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        z=next(i for i in range(j,n) if R[i][j])
        R[j],R[z]=R[z],R[j]
        d=R[j][j]
        R[j]=[x/d for x in R[j]]
        for i in range(n):
            if i!=j:
                c=R[i][j]
                if c:
                    R[i]=[x-c*y for x,y in zip(R[i],R[j])]
    return [row[n:] for row in R]


def tr(A):
    return sum((A[i][i] for i in range(len(A))),Q(0))


def prod(A,B):
    return [[sum((a*b for a,b in zip(row,col)), Q(0)) for col in zip(*B)] for row in A]


def lap(n,a,b):
    # The first n vertices form the rim; vertex n is the hub.
    N=n+1
    L=[[Q(0) for j in range(N)] for i in range(N)]
    for i in range(n):
        j=(i+1)%n
        for x,y,w in ((i,j,b),(i,n,a)):
            L[x][x]+=w; L[y][y]+=w
            L[x][y]-=w; L[y][x]-=w
    return L


def cycle_lap(n):
    L=[[Q(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        j=(i+1)%n
        L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
    return L


def check():
    total=0
    for n in range(3,10):
        N=n+1
        C=cycle_lap(n)
        assert tr(C)==2*n
        assert tr(prod(C,C))==6*n
        for t in (Q(1,4),Q(1),Q(3,2),Q(2),Q(9,4),Q(3),Q(5)):
            for u in (Q(0), Q(1,17*t), Q(2,7*t)):
                a=(1-t*u)/n
                b=u/n
                W=lap(n,a,b)
                G=[[W[i][j]+Q(1,N) for j in range(N)] for i in range(N)]
                KI=N*(tr(mat_inv(G))-1)
                V=[[a*int(i==j)+b*C[i][j] for j in range(n)] for i in range(n)]
                formula=N*(Q(1,N*a)+tr(mat_inv(V))-Q(1,a))
                assert KI==formula,(n,t,u,KI,formula)
                if u==0: assert KI==n**3
                total+=1
            # Independent derivative from d/d u of tr [(L+J/N)^-1].
            a=Q(1,n); b=Q(0)
            X=[[x+Q(1,N) for x in row] for row in lap(n,a,b)]
            Xi=mat_inv(X)
            Y=lap(n,-t/n,Q(1,n))
            deriv=-N*tr(prod(prod(Xi,Y),Xi))
            assert deriv==n**3*t-2*n*n*(n+1),(n,t,deriv)
            assert (deriv>=0)==(t>=Q(2*(n+1),n))
            total+=1
    print(f'VERIFY_OK {total} exact finite wheel/index/derivative instances; cycle traces and thresholds; general proof is analytic')


if __name__=='__main__':
    check()
