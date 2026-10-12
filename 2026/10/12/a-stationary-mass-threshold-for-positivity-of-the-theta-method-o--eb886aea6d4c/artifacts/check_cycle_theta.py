#!/usr/bin/env python3
"""Exact arithmetic checks for the positive theta-step law on directed rate cycles."""
from fractions import Fraction as F
from itertools import product


def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def inverse(A):
    n=len(A); M=[row[:]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        pivot=next(k for k in range(j,n) if M[k][j]); M[j],M[pivot]=M[pivot],M[j]
        d=M[j][j]; M[j]=[x/d for x in M[j]]
        for k in range(n):
            if k != j:
                d=M[k][j]; M[k]=[M[k][l]-d*M[j][l] for l in range(2*n)]
    return [row[n:] for row in M]


def matstep(rates,theta,h):
    n=len(rates);Q=[[F(0) for j in range(n)] for i in range(n)]
    for j,v in enumerate(rates):
        Q[j][j]-=v;Q[(j+1)%n][j]+=v
    M=[[F(int(i==j))-theta*h*Q[i][j] for j in range(n)] for i in range(n)]
    B=[[F(int(i==j))+(1-theta)*h*Q[i][j] for j in range(n)] for i in range(n)]
    return mm(B,inverse(M))


def diag_res(rates,a):
    q=[a*r/(1+a*r) for r in rates];P=F(1)
    for v in q:P*=v
    return [(1-x)/(1-P) for x in q]


def invariant(rates):
    s=[1/x for x in rates];S=sum(s);return [v/S for v in s]


def run():
    cases=0;checks=0
    for n in range(2,7):
        for k,rates in enumerate(product((F(1),F(2),F(3)),repeat=n)):
            if k>=90:break
            pi=invariant(rates)
            for theta in (F(0),F(1,4),F(1,2),F(3,4),F(9,10),F(1)):
                for h in (F(1,10),F(1),F(7)):
                    T=matstep(rates,theta,h)
                    assert all(sum(T[i][j] for i in range(n))==1 for j in range(n))
                    for i in range(n):
                        for j in range(n):
                            if i!=j:assert T[i][j]>0 if theta else T[i][j]>=0
                    if theta:
                        f=diag_res(rates,theta*h)
                        assert all(T[i][i]==(f[i]-(1-theta))/theta for i in range(n))
                    else:
                        assert all(T[i][i]==1-h*rates[i] for i in range(n))
                    assert (min(T[i][i] for i in range(n))>=0)==(h<=1/max(rates) if not theta else diag_res(rates,theta*h)[rates.index(max(rates))]>=1-theta)
                    cases+=1
            a,b=F(1,100),F(100)
            fa,fb=diag_res(rates,a),diag_res(rates,b)
            assert all(fa[i]>fb[i]>pi[i] for i in range(n))
            assert all(fa[i]>=fa[j] for i in range(n) for j in range(n) if rates[i]<=rates[j])
            checks+=1
    assert invariant((F(1),F(2),F(6)))==[F(3,5),F(3,10),F(1,10)]
    assert (1-min(invariant((F(1),F(2),F(6)))))==F(9,10)
    # theta=1/2 and h=2a: polynomial sign vanishes at a=(-3+sqrt(73))/32.
    from math import sqrt
    a=(sqrt(73)-3)/32
    assert abs((1-3*a-16*a*a))<1e-12
    print(f'VERIFY_OK {cases} exact rational transition matrices, {checks} strict diagonal-resolvent comparisons, heterogeneous critical example')

if __name__=='__main__': run()
