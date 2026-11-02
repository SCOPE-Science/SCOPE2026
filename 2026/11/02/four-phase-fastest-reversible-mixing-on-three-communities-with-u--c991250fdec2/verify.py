#!/usr/bin/env python3
"""Exact rational checks for the three-community fastest-mixing classification.
No external packages are required. Finite checks supplement the written proof.
"""
from fractions import Fraction as Q
from itertools import product


def solution(a):
    """a is the stationary mass of EACH of the two equal communities."""
    if not (Q(0) < a < Q(1, 2)):
        raise ValueError('Requires 0 < a < 1/2')
    g = 1-2*a
    if a <= Q(1,6):
        x, y, m = Q(0), a, (1-4*a)/g
    elif a <= Q(1,3):
        x = 2*a*(6*a-1)/(3*(1+2*a))
        y = 2*a*g/(1+2*a)
        m = g/(1+2*a)
    elif a <= Q(2,5):
        x = 2*a*a/(2-a)
        y = 2*a*g/(2-a)
        m = a/(2-a)
    else:
        x = (4*a-1)/3
        y = g/2
        m = (4*a-1)/(6*a)
    return x, y, m


def eigenvalues(a, x, y):
    g=1-2*a
    return (1-(x+y)/a, 1-2*y/g, 1-(2*x+y)/a, 1-y/(a*g))


def x_interval(a, y, m):
    return (max(Q(0), a*(1-m)-y),
            min(a-y, (a*(1+m)-y)/2))


def matrix(a, m, r, x, y):
    g=1-2*a
    n=2*m+r
    P=[[Q(0) for _ in range(n)] for _ in range(n)]
    pi=[a/m]*(2*m)+[g/r]*r
    for i in range(n):
        for j in range(n):
            if i==j:
                P[i][j]=1-(x+y)/a if i<2*m else 1-2*y/g
            elif i<m and m<=j<2*m or j<m and m<=i<2*m:
                P[i][j]=x/(a*m)
            elif i<2*m<=j:
                P[i][j]=y/(a*r)
            elif j<2*m<=i:
                P[i][j]=y/(g*m)
    return P,pi


def matvec(P,v):
    return [sum(p*z for p,z in zip(row,v)) for row in P]


def checks():
    count=0
    vals=sorted(set(Q(i,d) for d in range(7,63) for i in range(1,(d+1)//2)))
    vals+= [Q(1,6),Q(1,4),Q(1,3),Q(2,5)]
    for a in vals:
        g=1-2*a
        x,y,mu=solution(a)
        assert x>=0 and y>0 and x+y<=a and 2*y<=g
        ev=eigenvalues(a,x,y)
        assert mu==max(map(abs,ev)), (a,x,y,mu,ev)
        lo,hi=x_interval(a,y,mu)
        assert lo<=x<=hi
        for xx in set([lo,hi,(lo+hi)/2,x]):
            eigs=eigenvalues(a,xx,y)
            assert max(map(abs,eigs))==mu
            assert xx>=0 and xx+y<=a
            count+=4
        # Phase-dependent exact lower-bound certificates in scalar y.
        if a<=Q(1,6):
            assert mu==1-2*a/g
        elif a<=Q(1,3):
            assert mu==1-2*y/g==-(1-y/(a*g))
        elif a<=Q(2,5):
            assert mu==(a-y)/(3*a)==-(1-y/(a*g))
        else:
            assert y==g/2 and mu==(a-y)/(3*a)
        count+=5
    # Full finite matrices, exact stationary balance and all spectral subspaces.
    for a,m,r in product([Q(1,12),Q(1,6),Q(1,5),Q(1,4),Q(3,10),Q(1,3),Q(7,20),Q(2,5),Q(9,20)], [2,3,4], [2,3]):
        g=1-2*a
        x,y,mu=solution(a)
        P,pi=matrix(a,m,r,x,y)
        n=len(P)
        for i in range(n):
            assert sum(P[i])==1
            for j in range(n):
                assert P[i][j]>=0 and pi[i]*P[i][j]==pi[j]*P[j][i]
                count+=2
        e=eigenvalues(a,x,y)
        vectors=[([1 if i==0 else -1 if i==1 else 0 for i in range(n)],e[0]),
                 ([1 if i==m else -1 if i==m+1 else 0 for i in range(n)],e[0]),
                 ([1 if i==2*m else -1 if i==2*m+1 else 0 for i in range(n)],e[1]),
                 ([1 if i<m else -1 if i<2*m else 0 for i in range(n)],e[2]),
                 ([1 if i<2*m else -2*a/g for i in range(n)],e[3]),
                 ([Q(1)]*n,Q(1))]
        for v,l in vectors:
            if matvec(P,v)!=[l*z for z in v]:
                print("FAIL",a,m,r,"lambda",l,"vector",v,"actual",matvec(P,v),"expected",[l*z for z in v]);raise AssertionError
            count+=n
    return count,len(vals)

if __name__=='__main__':
    n,params=checks()
    print(f'PASS: {n} counted exact rational validation components; {params} rational stationary masses and 54 full matrices.')
