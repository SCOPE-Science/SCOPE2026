#!/usr/bin/env python3
"""Exact finite checks for percolation outbreak-size variance on trees.

Requires Python 3, networkx and sympy. Run: python verify.py
The unrestricted theorem is proved analytically in RESULT.md.
"""
import networkx as nx
import sympy as sp

p=sp.symbols('p')

def paths_of_tree(g, root):
    return {
        v: {
            tuple(sorted((a,b)))
            for a,b in zip(path[:-1],path[1:])
        }
        for v in g
        for path in [nx.shortest_path(g,root,v)]
    }

def variance_polynomial(g,root):
    paths=paths_of_tree(g,root)
    e1=sum((p**len(paths[v]) for v in g),sp.Integer(0))
    e2=sum((p**len(paths[u]|paths[v]) for u in g for v in g),sp.Integer(0))
    return sp.Poly(sp.expand(e2-e1*e1),p)

def test():
    count=0
    for n in range(3,10):
        for g in nx.nonisomorphic_trees(n):
            wiener=sum(nx.shortest_path_length(g,u,v) for u in g for v in g if u<v)
            for root in g:
                poly=variance_polynomial(g,root)
                assert poly.nth(1)==g.degree[root]
                farness=sum(nx.shortest_path_length(g,root,v) for v in g)
                assert -poly.diff().eval(1)==n*farness-wiener
                count+=1
    g=nx.path_graph(3)
    center=variance_polynomial(g,1).as_expr()
    leaf=variance_polynomial(g,0).as_expr()
    assert sp.expand(center-leaf-p*(p-1)*(p*p+3*p-1))==0
    print(f'PASS: {count} rooted exact covariance-polynomial and branch-identity checks; exact three-vertex threshold.')

if __name__=='__main__':
    test()
