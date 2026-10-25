#!/usr/bin/env python3
"""Independent verification of maximal stable-set enumerator for two-token complete bipartite graphs."""
from collections import Counter
from itertools import combinations
from math import comb
import networkx as nx

def form(m,n):
    uvals=[u for u in range(1,m+1) if u != m-1]
    vvals=[v for v in range(1,n+1) if v != n-1]
    c=Counter({comb(m,2)+comb(n,2):1})
    for u in uvals:
        for v in vvals:
            c[comb(m-u,2)+comb(n-v,2)+u*v] += comb(m,u)*comb(n,v)
    return c

def brute(m,n):
    vertices=list(combinations(range(m+n),2))
    edges=set()
    for i,a in enumerate(vertices):
        for j in range(i+1,len(vertices)):
            b=vertices[j]
            if len(set(a)^set(b))!=2:continue
            x,y=set(a)^set(b)
            if (x<m)!=(y<m): edges.add((i,j))
    g=nx.Graph();g.add_nodes_from(range(len(vertices)));g.add_edges_from(edges)
    counts=Counter(map(len,nx.find_cliques(nx.complement(g))))
    return counts

def ind_num(m,n):
    a,b=sorted((m,n))
    if a==2 and b==2:return 2
    if a==2:return 2*b-3
    return comb(a,2)+b-a

def min_mult(m,n):
    a,b=sorted((m,n))
    if a==2 and b==2:return 1
    if a==2:return comb(b,2)+(comb(b,3) if b>=4 else 0)
    if a<b:return a*comb(b,2)
    return sum(comb(a,u)*((comb(a,u) if u>=2 else 0)+comb(a,u+1)) for u in range(1,a-1))

if __name__=='__main__':
    trials=0;configs=0
    for m in range(2,7):
        for n in range(m,7):
            actual=brute(m,n)
            expected=form(m,n)
            assert actual==expected,(m,n,actual,expected)
            assert sum(actual.values())==1+(2**m-m-1)*(2**n-n-1)
            assert min(actual)==ind_num(m,n),(m,n,min(actual),ind_num(m,n))
            assert actual[min(actual)]==min_mult(m,n),(m,n,actual[min(actual)],min_mult(m,n))
            trials+=1;configs+=sum(actual.values())
    print('VERIFY_OK pairs=',trials,'distinct_maximal_independent_sets=',configs)
