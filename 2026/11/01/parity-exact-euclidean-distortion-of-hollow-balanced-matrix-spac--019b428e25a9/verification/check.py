#!/usr/bin/env python3
"""Independent finite-dimensional checks for hollow symmetric row-balanced cube sections.
No numerical test is used as a substitute for the universal proof.
"""
from fractions import Fraction as F
from itertools import combinations
import random
import numpy as np
from scipy.optimize import linprog
import networkx as nx


def edge_data(n):
    edges=list(combinations(range(n),2))
    B=np.zeros((n,len(edges)),dtype=int)
    for j,(a,b) in enumerate(edges):B[a,j]=B[b,j]=1
    return edges,B

def witness(n):
    G=nx.complete_graph(n)
    if n%2==0:
        G.remove_edges_from((i,i+1) for i in range(0,n,2))
    elif n%4==3:
        G.remove_edges_from([(0,1),(0,2),(1,2)])
    assert nx.is_eulerian(G) and G.number_of_edges()%2==0
    path=list(nx.eulerian_circuit(G,source=0))
    assert len(path)==G.number_of_edges()
    signs={tuple(sorted(e)):(1 if i%2==0 else -1) for i,e in enumerate(path)}
    edges,B=edge_data(n)
    x=np.array([signs.get(e,0) for e in edges],dtype=int)
    assert np.max(np.abs(x))==1
    assert np.all(B@x==0)
    expected=(n*(n-2)//2 if n%2==0 else n*(n-1)//2-(3 if n%4==3 else 0))
    assert int(x@x)==expected
    return x,expected

def rational_projection(n):
    edges,B=edge_data(n)
    E=len(edges)
    # A=B B^T=(n-2)I+J and A^-1=(I-J/[2(n-1)])/(n-2)
    def d(i,j):return F(int(B[:,i]@B[:,j]))
    def P(i,j):
        return (F(int(i==j))
                -(d(i,j)-F(2,n-1))/F(n-2))
    diag=P(0,0)
    assert diag==F(n-3,n-1)
    x=[P(j,0)/diag for j in range(E)]
    for v in range(n):
        assert sum(x[i] for i,e in enumerate(edges) if v in e)==0
    assert max(abs(t) for t in x)==1
    assert sum(t*t for t in x)==1/diag
    # Frobenius-equivariant projector P²=P, tested exactly by all indices.
    if n<=9:
        for i in range(E):
            for j in range(E):
                assert sum(P(i,k)*P(k,j) for k in range(E))==P(i,j)
    return diag


def lp_vertices(n,repeats=40):
    rng=np.random.default_rng(1234+n)
    edges,B=edge_data(n)
    num=0
    for _ in range(repeats):
        c=rng.normal(size=len(edges))
        ans=linprog(c,A_eq=B,b_eq=np.zeros(n),bounds=[(-1,1)]*len(edges),method='highs')
        assert ans.success
        assert np.linalg.norm(B@ans.x,np.inf)<1e-8
        if n%2==1:
            assert all(min(abs(v),abs(v-1),abs(v+1))<1e-7 for v in ans.x), (n,ans.x)
        n2=float(ans.x@ans.x)
        assert n2 <= witness(n)[1]+1e-7
        num+=1
    return num

if __name__=='__main__':
    cases=0
    for n in range(4,20):
        x,M=witness(n)
        d=rational_projection(n)
        d2=d*M
        dim=n*(n-3)//2
        assert d2<=dim
        if n%4==1:assert d2==dim
        print(f'n={n}: dimension={dim}, maxedge2={M}, minedge2={1/d}, distance_squared={d2}')
        cases+=1
    lp=0
    for n in range(4,12):lp+=lp_vertices(n,20)
    print(f'CHECK_OK explicit_witnesses={cases} exact_projectors={cases} random_linprog_vertices={lp}')
