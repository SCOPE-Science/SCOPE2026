#!/usr/bin/env python3
"""Finite incidence calculations for the three-particle equal-arm star space.

This verifies the combinatorial arithmetic of a proved good-cover reduction,
not the topological nerve lemma itself.
"""
from collections import defaultdict, deque
from fractions import Fraction
from itertools import combinations
from math import comb

def compositions(total, slots):
    if slots == 1:
        yield (total,)
        return
    for k in range(total+1):
        for tail in compositions(total-k, slots-1):
            yield (k,) + tail

def eligible_chamber(a, r):
    nmax=max(a)
    if nmax == 3: return 2*r <= 1
    if nmax == 2: return r <= 1
    return r <= 2

def eligible_center(b, r):
    if max(b)==2: return 2*r <= 1
    return r <= 1

def graph_result(m,r):
    alpha = [a for a in compositions(3,m) if eligible_chamber(a,r)]
    b = [t for t in compositions(2,m) if eligible_center(t,r)]
    vertices=[('A',a) for a in alpha]+[('B',t) for t in b]
    adjacency={v:set() for v in vertices}
    for t in b:
        for i in range(m):
            a=list(t);a[i]+=1;a=tuple(a)
            assert a in alpha, (m,r,t,a)
            x,y=('B',t),('A',a)
            adjacency[x].add(y);adjacency[y].add(x)
    components=0
    unseen=set(vertices)
    while unseen:
        components+=1
        seed=unseen.pop(); todo=[seed]
        while todo:
            q=todo.pop()
            for nb in adjacency[q]&unseen:
                unseen.remove(nb)
                todo.append(nb)
    edges=sum(map(len,adjacency.values()))//2
    first_betti=edges-len(vertices)+components
    return len(alpha),len(b),len(vertices),edges,components,first_betti

def formulas(m,r):
    if r<=Fraction(1,2):
        return (1, (m-1)*comb(m+1,2)-comb(m+2,3)+1)
    if r<=1:
        return (1, 2*comb(m,3)-comb(m,2)+1)
    if r<=2:
        return (comb(m,3), 0)
    return (0,0)

R=[Fraction(1,100),Fraction(1,2),Fraction(501,1000),Fraction(1,1),Fraction(1001,1000),Fraction(2,1),Fraction(201,100)]
for m in range(3,12):
    for r in R:
        a,b,v,e,c,h=graph_result(m,r)
        expected=formulas(m,r)
        assert (c,h)==expected,(m,r,c,h,expected)
        if c == 1 and h>0: assert e-v+1==h
        if r>2: assert v==0 and e==0
        if m in (3,4,5) and r in (Fraction(1,2),Fraction(501,1000),Fraction(1001,1000)):
            print(f'm={m}, r={r}, chambers={a}, center-faces={b}, vertices={v}, edges={e}, pi0={c}, b1={h}')
print('INCIDENCE_VERIFY_OK: m=3..11, seven representative/critical separation values')
