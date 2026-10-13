#!/usr/bin/env python3
"""Exact-rational checks for finite-patch extinction-time CV theorem."""
from fractions import Fraction as F
from itertools import combinations


def graphs(n):
    pairs=list(combinations(range(n),2))
    for mask in range(1<<len(pairs)):
        edges=[p for j,p in enumerate(pairs) if (mask>>j)&1]
        adj=[0]*n
        for u,v in edges: adj[u]|=1<<v; adj[v]|=1<<u
        seen=1
        while True:
            reach=seen
            for u in range(n):
                if (seen>>u)&1: reach|=adj[u]
            if reach==seen: break
            seen=reach
        if seen==(1<<n)-1:
            yield adj


def zero_derivs(adj):
    n=len(adj); kmax=1<<n
    m0=[F(0)]*kmax; m1=[F(0)]*kmax
    s0=[F(0)]*kmax; s1=[F(0)]*kmax
    sets=sorted(range(1,kmax),key=lambda S:S.bit_count())
    for S in sets:
        k=S.bit_count()
        base_m=sum((m0[S &~(1<<i)] for i in range(n) if (S>>i)&1),F(0))
        m0[S]=(1+base_m)/k
        s0[S]=(2*m0[S]+sum((s0[S &~(1<<i)] for i in range(n) if (S>>i)&1),F(0)))/k
    for S in sets:
        k=S.bit_count()
        birth_m=birth_s=F(0)
        for v in range(n):
            if (S>>v)&1: continue
            b=(adj[v]&S).bit_count()
            if b:
                birth_m+=b*(m0[S|(1<<v)]-m0[S])
                birth_s+=b*(s0[S|(1<<v)]-s0[S])
        m1[S]=(birth_m+sum((m1[S &~(1<<i)] for i in range(n) if (S>>i)&1),F(0)))/k
        s1[S]=(2*m1[S]+birth_s+sum((s1[S &~(1<<i)] for i in range(n) if (S>>i)&1),F(0)))/k
    for v in range(n):
        idx=1<<v; d=adj[v].bit_count()
        assert m0[idx]==1 and s0[idx]==2
        assert m1[idx]==F(d,2) and s1[idx]==F(5*d,2)
        # d/dlambda (E[T^2]/E[T]^2-1)|0 = s1 - 2*s0*m1.
        assert s1[idx]-4*m1[idx]==F(d,2)
    return n


def solve(A,b):
    n=len(b); X=[list(map(F,row))+[F(b[i])] for i,row in enumerate(A)]
    for i in range(n):
        j=next(k for k in range(i,n) if X[k][i])
        X[i],X[j]=X[j],X[i]
        z=X[i][i]; X[i]=[v/z for v in X[i]]
        for k in range(n):
            if k!=i and X[k][i]:
                c=X[k][i]; X[k]=[X[k][t]-c*X[i][t] for t in range(n+1)]
    return [row[-1] for row in X]


def finite_moments(adj,lam):
    n=len(adj); states=list(range(1,1<<n)); ix={S:i for i,S in enumerate(states)}
    A=[]
    for S in states:
        row=[F(0)]*len(states)
        for v in range(n):
            if (S>>v)&1:
                row[ix[S]]+=1
                if S!=(1<<v): row[ix[S&~(1<<v)]]-=1
            else:
                b=(adj[v]&S).bit_count()
                if b:
                    row[ix[S]]+=lam*b
                    row[ix[S|(1<<v)]]-=lam*b
        A.append(row)
    m=solve(A,[F(1)]*len(states))
    sec=solve(A,[2*v for v in m])
    return {S:(m[ix[S]],sec[ix[S]]) for S in states}


def main():
    counts=[]
    for n in range(2,6):
        count=0
        for adj in graphs(n): zero_derivs(adj); count+=1
        counts.append((n,count))
    assert counts==[(2,1),(3,4),(4,38),(5,728)],counts
    for lam in map(F,[0,1,2,3,5,20,100]):
        m,s=finite_moments([2,1],lam)[1]
        assert m==1+lam/2
        assert s==2+F(5,2)*lam+lam*lam/2
        assert s/(m*m)-1==1+2*lam/(lam+2)**2
    for n,ed in ((3,[(0,1),(1,2)]),(4,[(0,1),(0,2),(0,3)])):
        adj=[0]*n
        for u,v in ed: adj[u]|=1<<v; adj[v]|=1<<u
        for lam in (F(1),F(100)):
            data=finite_moments(adj,lam)
            assert all(m>0 and s>m*m for m,s in data.values())
    print('VERIFY_OK connected_labeled_counts=',counts,'two_patch_exact_points=7 additional_examples=4')


if __name__=='__main__': main()
