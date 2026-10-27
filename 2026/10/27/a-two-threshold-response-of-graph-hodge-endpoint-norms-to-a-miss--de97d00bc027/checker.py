#!/usr/bin/env python3
"""Exact finite rational comparisons for edge-deleted cliques.
This verifies finite cases only, not the parameter-uniform analytic proof.
"""
from fractions import Fraction as F

def solve(A,b):
    n=len(b);T=[[F(x) for x in A[i]]+[F(b[i])] for i in range(n)]
    for i in range(n):
        k=next(k for k in range(i,n) if T[k][i])
        T[i],T[k]=T[k],T[i]
        z=T[i][i];T[i]=[u/z for u in T[i]]
        for j in range(n):
            if j==i:continue
            h=T[j][i]
            if h:T[j]=[u-h*v for u,v in zip(T[j],T[i])]
    return [x[-1] for x in T]

def check(N):
    E=[(u,v) for u in range(N) for v in range(u+1,N) if (u,v)!=(0,1)]
    L=[[0]*N for _ in range(N)]
    for u,v in E:
        L[u][u]+=1;L[v][v]+=1;L[u][v]-=1;L[v][u]-=1
    Qa=F(2)-F(1,N-2); Pa=F(3*N*N-11*N+6,N*(N-2))
    Qb=F(2*(N-1),N);Pb=F(3)-F(6,N)
    Qvals=[];Pvals=[]
    for u,v in E:
        rhs=[0]*(N-1)
        if u<N-1:rhs[u]+=1
        if v<N-1:rhs[v]-=1
        z=solve([row[:-1] for row in L[:-1]],rhs)+[F(0)]
        Q=sum((abs(z[x]-z[y]) for x,y in E),F(0))
        R=abs(z[u]-z[v]);P=F(1)+Q-2*R
        category='A' if 0 in (u,v) or 1 in (u,v) else 'B'
        assert (Q,P)==((Qa,Pa) if category=='A' else (Qb,Pb)),(N,u,v,Q,P)
        Qvals.append(Q);Pvals.append(P)
    assert max(Qvals)==max(Qa,Qb) if N>=4 else max(Qvals)==Qa
    assert max(Pvals)==max(Pa,Pb) if N>=4 else max(Pvals)==Pa
    return len(E)

def run():
    cols=sum(check(n) for n in range(3,12))
    print('DELETED_CLIQUE_EXACT_RATIONAL_OK graph_sizes=9 columns=',cols)
if __name__=='__main__':run()
