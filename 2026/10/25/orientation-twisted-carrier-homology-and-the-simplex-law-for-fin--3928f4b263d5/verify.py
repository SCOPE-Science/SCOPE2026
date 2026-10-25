#!/usr/bin/env python3
"""Reproducible finite example for orientation-twisted top homology.
No third-party dependencies except SymPy for exact integer/rational ranks.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
import sympy as sp

FACETS = ['012','013','024','035','045','125','134','145','234','235']
F = [tuple(map(int, t)) for t in FACETS]
EDGES = sorted(set(e for t in F for e in combinations(t, 2)))
assert len(F)==10 and len(EDGES)==15
incidences = defaultdict(list)
for j,t in enumerate(F):
    for i in range(3):
        e = tuple(v for k,v in enumerate(t) if k!=i)
        incidences[e].append((j,(-1)**i))
assert all(len(s)==2 for s in incidences.values())
assert len(incidences)==len(EDGES)
# Each vertex link is connected 5-cycle: together with chi=1 verifies RP2.
for v in range(6):
    link = [tuple(u for u in t if u!=v) for t in F if v in t]
    degrees=Counter(u for e in link for u in e)
    assert len(link)==5 and len(degrees)==5 and set(degrees.values())=={2}
    seen={link[0][0]}; pending=[link[0][0]]
    while pending:
        x=pending.pop()
        for e in link:
            if x in e:
                for y in e:
                    if y not in seen: seen.add(y);pending.append(y)
    assert len(seen)==5
assert 6-15+10==1
B = sp.zeros(len(EDGES),len(F))
T = sp.zeros(len(EDGES),len(F))
for k,e in enumerate(EDGES):
    (j,s),(l,t)=sorted(incidences[e])
    B[k,j],B[k,l]=s,t
    T[k,j],T[k,l]=1,-1
assert B.rank()==10
assert T.rank()==9
# Traverse facet-dual graph.  Ordinary global orientability means the coefficients
# of each ordinary boundary row cancel; the local sign change around a loop is -1.
graph=defaultdict(list)
for e,((a,s),(b,t)) in incidences.items():
    ratio=-s*t # relation c_b=ratio*c_a for ordinary cycle
    graph[a].append((b,ratio))
    graph[b].append((a,ratio))
coeff={0:1};todo=deque([0]);inconsistencies=0
while todo:
    a=todo.popleft()
    for b,r in graph[a]:
        y=coeff[a]*r
        if b not in coeff: coeff[b]=y;todo.append(b)
        elif coeff[b]!=y: inconsistencies+=1
assert len(coeff)==10 and inconsistencies>0
# r disjoint copies of the same RP2, mapped by identity on each component.
# The distribution simplex consists of weights on copies; its dimension is r-1.
for r in range(1,6):
    ob=sp.diag(*([B]*r)); tb=sp.diag(*([T]*r))
    assert ob.cols == 10*r and tb.cols == 10*r
    assert ob.rank()==10*r and tb.rank()==9*r
    assert ob.cols-ob.rank()==0
    assert tb.cols-tb.rank()==r
    assert (tb.cols-tb.rank())-1==r-1
    print(f'copies={r} carrier_dimension={r-1} ordinary_top_rank=0 twisted_top_rank={r}')
print('RP2_f=(6,15,10) orientation_holonomy_nontrivial=True')
print('VERIFY_OK')
