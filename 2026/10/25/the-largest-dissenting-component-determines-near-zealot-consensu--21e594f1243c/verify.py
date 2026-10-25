#!/usr/bin/env python3
"""Exact-rational checks of near-zealot partisan voter hitting asymptotics.
The finite checks are corroboration, not a proof for arbitrary graphs.
"""
from fractions import Fraction as F
from itertools import combinations
from functools import lru_cache
import sympy as sp


def components(b_vertices, edges):
    b_vertices=set(b_vertices); output=[]
    while b_vertices:
        start=next(iter(b_vertices)); stack=[start]; b_vertices.remove(start); c={start}
        while stack:
            x=stack.pop()
            for y in (edges[x]&b_vertices):
                b_vertices.remove(y);stack.append(y);c.add(y)
        output.append(frozenset(c))
    return output


def coefficient(vertices, edges, zealots):
    """Return (size, k) for each induced-B connected component."""
    b=set(vertices)-set(zealots)
    results=[]
    for C in components(b,edges):
        C=frozenset(C)
        @lru_cache(None)
        def H(S):
            if S==C:return F(1)
            rem=C-S
            q=sum(F(len(edges[v]&rem),len(edges[v])) for v in S)
            assert q>0
            out=F(0)
            for v in rem:
                bv=F(len(edges[v] & (set(zealots)|set(S))),len(edges[v]))
                out+=bv*H(S|{v})
            return out/(2*q)
        k=F(0)
        for v in C:
            k+=F(len(edges[v]&set(zealots)),2*len(edges[v]))*H(frozenset({v}))
        assert k>0
        results.append((len(C),k))
    return results


def graph(N,undirected_edges):
    G=[set() for _ in range(N)]
    for i,j in undirected_edges:
        assert i!=j
        G[i].add(j);G[j].add(i)
    return G


def exact_mean(Ed, zealots={0}):
    """Symbolically solve transient CTMC hitting time for given graph."""
    E=sp.symbols('e',positive=True)
    N=len(Ed); b=sorted(set(range(N))-set(zealots));m=len(b)
    full=(1<<m)-1
    Q=sp.zeros(full,full)
    for S in range(full):
        plus={v for j,v in enumerate(b) if (S>>j)&1}|set(zealots)
        for j,v in enumerate(b):
            rate=sp.Rational(len(Ed[v]&plus),len(Ed[v]))*E/2 if not (S>>j)&1 else sp.Rational(len(Ed[v]-plus),len(Ed[v]))*(1-E/2)
            if rate:
                dest=S^(1<<j)
                Q[S,S]+=rate
                if dest!=full:Q[S,dest]-=rate
    T=Q.inv()*sp.ones(full,1)
    return E, sp.factor(T[0])


def verify():
    samples={
        'star_m3':graph(4,[(0,1),(0,2),(0,3)]),
        'clique_m3':graph(4,list(combinations(range(4),2))),
        'path_m3':graph(4,[(0,1),(1,2),(2,3)]),
        'split_2plus1':graph(4,[(0,1),(1,2),(0,3)]),
        'clique_m2_z2':graph(4,list(combinations(range(4),2))),
    }
    for name,Ed in samples.items():
        Z={0,1} if name=='clique_m2_z2' else {0}
        info=coefficient(range(len(Ed)),Ed,Z)
        exponent=max(m for m,k in info)
        e,T=exact_mean(Ed,Z)
        predicted=sum((1/k for m,k in info if m==exponent),F(0)) if len([1 for m,k in info if m==exponent])==1 else None
        obs=sp.limit(e**exponent*T,e,0,dir='+')
        print(name,'components/k',info,'E[T] rational',T,'scaled limit',obs,'single slow prediction',predicted)
        if predicted is not None:assert obs==predicted
        if name=='star_m3':assert T==sp.Rational(11,3)/e
        if name=='clique_m3':assert obs==sp.Rational(8,3)
        if name=='split_2plus1':assert obs==1/info[0][1] if info[0][0]==2 else obs==1/info[1][1]

if __name__=='__main__':
    verify()
    print('All exact symbolic assertions passed.')
