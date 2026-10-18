#!/usr/bin/env python3
"""Exact integer spectral verification of the two Johnson distance graphs."""
import itertools
import sympy as sp

checked=0
for v in range(4,9):
    vertices=list(itertools.combinations(range(v),2));N=len(vertices)
    adjacency=sp.zeros(N)
    for i,S in enumerate(vertices):
        for j in range(i+1,N):
            if set(S).intersection(vertices[j]): adjacency[i,j]=adjacency[j,i]=1
    L1=2*(v-2)*sp.eye(N)-adjacency
    J=sp.ones(N)
    L2=N*sp.eye(N)-J-L1
    p=v-1; q=v*(v-3)//2
    e1={sp.Integer(0):1,sp.Integer(v):p,sp.Integer(2*(v-1)):q}
    got1=L1.eigenvals()
    if got1!=e1:raise AssertionError((v,got1,e1))
    e2={sp.Integer(0):1,sp.Integer(N-v):p,sp.Integer(N-2*(v-1)):q}
    if v==4:
        e2={sp.Integer(0):q+1,sp.Integer(N-v):p}
    got2=L2.eigenvals()
    if got2!=e2:raise AssertionError((v,got2,e2))
    assert L1+L2==N*sp.eye(N)-J
    checked+=1
print('PASS integer characteristic spectral comparisons',checked)
