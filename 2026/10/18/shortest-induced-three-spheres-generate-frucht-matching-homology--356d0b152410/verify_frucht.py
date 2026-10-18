#!/usr/bin/env python3
"""Exact reproducible tests for induced matching spheres of the Frucht graph.

Uses only standard-library integer arithmetic; explicitly rebuilds each simplex
and every signed boundary matrix. Failing an assertion invalidates the certificate.
"""
from collections import Counter
from itertools import combinations, product
from functools import reduce
from math import gcd

EDGES = (
    (0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
    (4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11)
)
assert len(EDGES)==18 and len({p for e in EDGES for p in e})==12
assert all(sum(v in e for e in EDGES)==3 for v in range(12))
assert EDGES == tuple(sorted(EDGES))

# A simplex is a sorted tuple of edge indices of a graph matching.
faces = [None]
for k in range(1,7):
    faces.append(tuple(F for F in combinations(range(18),k)
             if len({v for j in F for v in EDGES[j]})==2*k))
assert tuple(len(faces[k]) for k in range(1,7)) == (18,117,333,397,152,8)

# Integer-column boundary. Dict row-index -> coefficient, never modular.
def boundary(k):
    if k==1: return []
    lower={f:i for i,f in enumerate(faces[k-1])}
    return [dict((lower[f[:j]+f[j+1:]], (-1)**j) for j in range(k))
            for f in faces[k]]

B={k:boundary(k) for k in range(2,7)}

def elim(column, pivots):
    x=dict(column)
    while x:
        pivot = next((i for i in sorted(x) if i in pivots), None)
        if pivot is None: return x
        scale=x[pivot]
        for j,a in pivots[pivot].items():
            z=x.get(j,0)-scale*a
            if z:x[j]=z
            else:x.pop(j,None)
    return x

def exact_unit_basis(columns):
    pivots={}; used=[]
    for index,col in enumerate(columns):
        x=elim(col,pivots)
        if not x: continue
        p=min(x)
        assert abs(x[p])==1, ('nonunit pivot',index,p,x[p])
        s=x[p]
        pivots[p]={j:s*v for j,v in x.items()}
        used.append(index)
    return pivots,used

ranks={1:0};pivot={}
for k in range(2,7):
    pivot[k],used=exact_unit_basis(B[k])
    ranks[k]=len(pivot[k])
assert [ranks[k] for k in range(2,7)] == [17,100,233,144,8]
# Check all chain identities via signed integer arithmetic.
for k in range(3,7):
    for col in B[k]:
        acc={}
        for row,val in col.items():
            for j,a in B[k-1][row].items():
                acc[j]=acc.get(j,0)+val*a
        assert not any(acc.values())

# Enumerate induced copies of M(4P3) = (S0) * (S0) * (S0) * (S0).
wedges=[]
for i,j in combinations(range(18),2):
    vertices=frozenset(EDGES[i]+EDGES[j])
    if len(vertices)==3:wedges.append(((i,j),vertices))

carriers=[]
def find_carriers(t, chosen, used):
    if len(chosen)==4:
        carriers.append(tuple(chosen));return
    for i in range(t,len(wedges)):
        pair,vs=wedges[i]
        if used.isdisjoint(vs):find_carriers(i+1,chosen+[pair],used|vs)
find_carriers(0,[],frozenset())
carriers=sorted(set(carriers))
assert len(carriers)==87
assert len({frozenset(e for pair in c for e in pair) for c in carriers})==87
assert all(len({v for pair in c for e in pair for v in EDGES[e]})==12 for c in carriers)

# The join of oriented zero-spheres gives the oriented three-cycle.
tetra={f:i for i,f in enumerate(faces[4])}
cycles=[]
for carrier in carriers:
    z={}
    for choice in product((0,1),repeat=4):
        unsorted=[carrier[j][choice[j]] for j in range(4)]
        f=tuple(sorted(unsorted))
        inversions=sum(unsorted[j]>unsorted[k]
                       for j in range(4) for k in range(j+1,4))
        sign=(-1)**(sum(choice)+inversions)
        z[tetra[f]]=sign
    assert len(z)==16
    # Explicitly verify the chain is a cycle.
    dz={}
    for row,coef in z.items():
        for j,a in B[4][row].items():dz[j]=dz.get(j,0)+coef*a
    assert not any(dz.values())
    cycles.append(z)

# Work in the integral chain quotient C3 / im(d4), which is free by the
# exact all-unit pivot reduction of d4. Each reduced cycle represents
# precisely its homology class: z is itself a cycle.
classes=[elim(z,pivot[5]) for z in cycles]
assert all(c and reduce(gcd,map(abs,c.values()),0)==1 for c in classes)

# An additional 20 independent unit pivots on these classes prove that
# their generated subgroup is primitive in C3/im(d4). Since H3 has rank20,
# and the rank is certified above, this subgroup equals integral H3.
p,chosen=exact_unit_basis(classes)
assert len(p)==20
assert len(chosen)==20
assert sum(len(faces[k]) for k in range(1,7))==1025

betti={k:len(faces[k+1])-ranks[k+1]-ranks.get(k+2,0) for k in range(6)}
assert [betti[k] for k in range(6)] == [1,0,0,20,0,0]
print('VERIFY_OK_FRUCHT_MATCHING_COMPLEX')
print('EDGES_18_NODES_12_FACES',tuple(len(faces[k]) for k in range(1,7)))
print('BOUNDARY_RANKS',tuple(ranks[k] for k in range(2,7)))
print('H3_INTEGRAL_FREE_RANK_20 OTHER_REDUCED_HOMOLOGY_ZERO')
print('87_SHORTEST_INDUCED_OCTAHEDRAL_S3_CLASSES_ALL_PRIMITIVE')
print('EXACT_INTEGRAL_GENERATION_20_UNIT_PIVOTS')
print('BASIS_CARRIER_INDICES_0_BASED',chosen)
for ix in chosen:
    print('BASIS_CARRIER',ix,tuple(EDGES[a] for pair in carriers[ix] for a in pair))
