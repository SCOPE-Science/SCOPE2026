#!/usr/bin/env python3
"""Exact rational checks for dense-complement transfer-current expansions.

This optional finite checker builds several regular deleted graphs and compares
all cut and cycle projection columns against the local-codegree error bounds.
It verifies finite instances only; the general estimates have an analytic proof.
"""
from fractions import Fraction
from itertools import combinations
from math import comb
import networkx as nx
import sympy as sp


def check(H):
    vertices=list(H.nodes()); N=len(vertices); order={v:i for i,v in enumerate(vertices)}
    edges_h={tuple(sorted((order[u],order[v]))) for u,v in H.edges()}
    degrees={H.degree(v) for v in vertices}; assert len(degrees)==1
    r=degrees.pop(); assert N>=4*r and r>=1
    edges_g=[(u,v) for u in range(N) for v in range(u+1,N) if (u,v) not in edges_h]
    # Grounded inverse: exact rational potentials with last vertex held at zero.
    L=sp.zeros(N,N)
    for u,v in edges_g:
        L[u,u]+=1;L[v,v]+=1;L[u,v]-=1;L[v,u]-=1
    inv=L[:-1,:-1].inv()
    neigh=[set() for i in range(N)]
    for u,v in edges_h:neigh[u].add(v);neigh[v].add(u)
    checked=0; extrema=[]
    for u,v in edges_g:
        s=sp.zeros(N-1,1)
        if u<N-1:s[u]=1
        if v<N-1:s[v]=-1
        x=list(inv*s)+[sp.Integer(0)]
        actual_q=sum(abs(x[a]-x[b]) for a,b in edges_g)
        actual_p=actual_q+1-2*(x[u]-x[v])
        c=len(neigh[u]&neigh[v]); A=r-c
        expect_q=sp.Rational(2)+sp.Rational(2*A-2,N)
        expect_p=sp.Rational(3)+sp.Rational(2*A-6,N)
        assert abs(actual_q-expect_q)<=sp.Rational(32*r*r,N*N)
        assert abs(actual_p-expect_p)<=sp.Rational(44*r*r,N*N)
        # Exact first two Neumann terms and exact first-order correction.
        delta=[int(w in neigh[v])-int(w in neigh[u]) for w in range(N)]
        assert delta[u]==0 and delta[v]==0
        x0=[sp.Rational(delta[w],N*N) for w in range(N)]
        x0[u]=sp.Rational(1,N)+sp.Rational(r,N*N)
        x0[v]=-sp.Rational(1,N)-sp.Rational(r,N*N)
        tv0=sum(abs(x0[a]-x0[b]) for a,b in edges_g)
        T=sum(abs(delta[a]-delta[b]) for a,b in edges_h if a not in (u,v) and b not in (u,v))
        formula0=expect_q-sp.Rational(2*r*r+2*r+2*A*(A+3)+T,N*N)
        assert tv0==formula0,('identity',N,r,u,v,tv0,formula0)
        assert T<=4*r*r
        checked+=1
        extrema.append((c,actual_q,actual_p))
    return checked,len(edges_g),r,N,extrema


def main():
    cases=[]
    for n in [8,10,12,14]:cases.append(nx.cycle_graph(n))
    for n in [12,14]:cases.append(nx.random_regular_graph(3,n,seed=173+n))
    cases.append(nx.hypercube_graph(4))
    cases.append(nx.disjoint_union_all([nx.complete_graph(4) for _ in range(3)]))
    cases.append(nx.random_regular_graph(4,16,seed=761))
    cases.append(nx.random_regular_graph(1,8,seed=344))
    for n in [12]:cases.append(nx.random_regular_graph(2,n,seed=902+n))
    total=0; examples=[]
    for H in cases:
        checked,m,r,N,e=check(H);total+=checked
        examples.append((N,r,checked))
        # Under the appropriate size condition, no maximizing edge can have
        # greater deleted-graph codegree than the minimum.
        if N>44*r*r:
            mc=min(a[0] for a in e)
            assert min(a[0] for a in e if a[1]==max(b[1] for b in e))==mc
            assert all(a[0]==mc for a in e if a[2]==max(b[2] for b in e))
    print('DENSE_COMPLEMENT_EXACT_OK graphs=%d columns=%d examples=%s' % (len(cases),total,examples))

if __name__=='__main__':main()
