#!/usr/bin/env python3
"""Exact finite checks for four-direction electrical metrics on F_3^2.

Requires Python 3 standard library only. Universal claims use the proof,
not finite sampling. Every matrix computation below uses exact fractions.
"""
from fractions import Fraction as F
from itertools import product
from math import isclose

P = list(product(range(3), repeat=2))
S = [(1,0), (0,1), (1,1), (1,2)]
N = len(P)

def inverse(a):
    a = [[F(v) for v in row] for row in a]
    n = len(a)
    z = [row + [F(i == j) for j in range(n)] for i,row in enumerate(a)]
    for k in range(n):
        pivot = next(i for i in range(k,n) if z[i][k] != 0)
        z[k],z[pivot] = z[pivot],z[k]
        t = z[k][k]
        z[k] = [u/t for u in z[k]]
        for i in range(n):
            if i == k: continue
            t = z[i][k]
            if t:
                z[i] = [x-t*y for x,y in zip(z[i],z[k])]
    return [row[n:] for row in z]

def test(w):
    w = list(map(F,w))
    assert sum(c>0 for c in w)>=2 and all(c>=0 for c in w)
    W=sum(w)
    L = [[F(0) for j in P] for i in P]
    for i,x in enumerate(P):
        for s,c in zip(S,w):
            for sign in (-1,1):
                y=((x[0]+sign*s[0])%3,(x[1]+sign*s[1])%3)
                j=P.index(y)
                L[i][i] += c
                L[i][j] -= c
    assert all(L[i][j]==L[j][i] for i in range(N) for j in range(N))
    A=[[L[i][j]+F(1,N) for j in range(N)] for i in range(N)]
    G = inverse(A)
    R = [[G[i][i]+G[j][j]-2*G[i][j] for j in range(N)] for i in range(N)]
    q=[1/(W-c) for c in w]
    rv=[F(2,9)*(sum(q)-z) for z in q]
    for i,x in enumerate(P):
        for j,y in enumerate(P):
            if i==j:
                assert R[i][j]==0
            else:
                z=((y[0]-x[0])%3,(y[1]-x[1])%3)
                h=next(h for h,s in enumerate(S) if z in (s,((-s[0])%3,(-s[1])%3)))
                assert R[i][j]==rv[h],(w,x,y,R[i][j],rv[h])
    for p in (1,2,3):
        D=[[R[i][j]**p for j in range(N)] for i in range(N)]
        for h,s in enumerate(S):
            normal=(s[1],-s[0])
            v=[2 if (normal[0]*x[0]+normal[1]*x[1])%3==0 else -1 for x in P]
            mu=3*rv[h]**p-sum(r**p for r in rv)
            assert sum(v)==0
            for i in range(N):
                assert sum(D[i][j]*v[j] for j in range(N)) == mu*v[i]
    qmin=min(q)
    eig=[F(1,2)*(sum(r*r for r in rv)-3*r*r) for r in rv]
    assert min(eig)>=F(14,81)*qmin**2
    assert all(a>0 for a in eig)
    equality=(min(eig)==F(14,81)*qmin**2)
    assert equality == (sum(c>0 for c in w)==2), (w,equality)
    return min(eig)

cases=[(1,1,0,0),(2,3,0,0),(1,0,1,0),(0,1,0,3),
       (1,2,3,0),(1,1,2,0),(1,1,1,1),(1,2,3,4),
       (1,1,1,5),(2,2,2,7),(1,1,2,2),(1,3,4,4),
       (5,3,2,1),(1,7,2,3),(2,2,2,2),
       (F(1,2),F(2,3),F(3,4),F(5,6))]
for w in cases:
    mm=test(w)
    print('EXACT_OK directions=',w,' min_Gram=',str(mm))
print('ALL_TERNARY_RESISTANCE_CHECKS_OK profiles=',len(cases))

# The Cartesian torus has exactly two largest line resistances.
w = [F(1),F(1),F(0),F(0)]
W=sum(w); q=[1/(W-a) for a in w]
r=[F(2,9)*(sum(q)-a) for a in q]
assert sorted(r)==[F(4,9),F(4,9),F(5,9),F(5,9)]
assert sum(v==max(r) for v in r)==2
print('CARTESIAN_TORUS_OK exponents log(2)/log(5/4), endpoint_Gram_rank=4')
