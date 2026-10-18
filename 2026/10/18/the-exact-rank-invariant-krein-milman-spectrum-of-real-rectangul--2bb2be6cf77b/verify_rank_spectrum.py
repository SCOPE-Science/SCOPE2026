#!/usr/bin/env python3
"""Exact finite tests for the rank-invariant convexification theorem (real case)."""
from itertools import product
from fractions import Fraction as Q


def rank(a):
    x = [[Q(v) for v in row] for row in a]
    m=len(x); n=len(x[0]); pivot=0
    for j in range(n):
        k=next((i for i in range(pivot,m) if x[i][j]), None)
        if k is None: continue
        x[pivot],x[k]=x[k],x[pivot]
        z=x[pivot][j]
        x[pivot]=[v/z for v in x[pivot]]
        for i in range(m):
            if i!=pivot and x[i][j]:
                z=x[i][j]
                x[i]=[x[i][t]-z*x[pivot][t] for t in range(n)]
        pivot+=1
        if pivot==m: break
    return pivot


def witnesses(m,n,r,t):
    assert 2<=r<=min(m,n) and 0<t<1
    S=[[Q(1) for j in range(n)] for i in range(m)]
    for j in range(1,r-1):
        S[j-1][j]=Q(-1)
    P=[row[:] for row in S]
    P[r-2][r-1]=Q(-1)
    T=[[ (1-t)*S[i][j]+t*P[i][j] for j in range(n)] for i in range(m)]
    assert rank(S)==r-1,(m,n,r,S)
    assert rank(P)==r,(m,n,r,P)
    assert rank(T)==r,(m,n,r,t,T)
    assert max(abs(z) for row in T for z in row)==1
    # All but one coordinates stay saturated. Only S and P sign vertices can occur.
    assert sum(abs(T[i][j])!=1 for i in range(m) for j in range(n))==1
    assert T[r-2][r-1]==1-2*t
    return True


def rank_one_decomposition(u,v):
    assert max(abs(x) for x in u)==max(abs(y) for y in v)==1
    m,n=len(u),len(v)
    target=[[u[i]*v[j] for j in range(n)] for i in range(m)]
    result=[[Q(0) for j in range(n)] for i in range(m)]; total=Q(0)
    for ss in product((-1,1),repeat=m):
        ps=Q(1)
        for i in range(m): ps*=(1+ss[i]*u[i])/2
        for tt in product((-1,1),repeat=n):
            p=ps
            for j in range(n): p*=(1+tt[j]*v[j])/2
            if not p: continue
            V=[[Q(ss[i]*tt[j]) for j in range(n)] for i in range(m)]
            assert rank(V)==1 and all(abs(z)==1 for row in V for z in row)
            total+=p
            for i in range(m):
                for j in range(n): result[i][j]+=p*V[i][j]
    assert total==1 and result==target
    return True


def main():
    nw=0
    for m in range(2,8):
        for n in range(2,8):
            for r in range(2,min(m,n)+1):
                for t in (Q(1,4),Q(1,2),Q(3,4)):
                    witnesses(m,n,r,t);nw+=1
    nr=0
    for m in range(1,5):
        for n in range(1,5):
            us=([Q(1)]+[Q((i%4)-2,5) for i in range(1,m)],
                [Q(-1)]+[Q((3*i)%5-2,5) for i in range(1,m)])
            vs=([Q(1)]+[Q((2*j)%5-2,5) for j in range(1,n)],
                [Q(-1)]+[Q((3*j)%5-2,5) for j in range(1,n)])
            for u in us:
                for v in vs:
                    rank_one_decomposition(u,v);nr+=1
    print('PASS exact rational edge witnesses:',nw)
    print('PASS exact rational rank-one sign decompositions:',nr)

if __name__=='__main__':main()
