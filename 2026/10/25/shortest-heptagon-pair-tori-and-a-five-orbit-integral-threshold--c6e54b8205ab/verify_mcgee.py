#!/usr/bin/env python3
"""Exact certificates for shortest-cycle torus lattices on the 24-vertex McGee graph.

Requires Python 3.10+, numpy, networkx, sympy. All graph data and certificates
are generated deterministically from the LCF presentation of the graph.
"""
from itertools import combinations
from collections import Counter
import networkx as nx
import numpy as np
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

N = 24
SHIFTS = (12, 7, -7) * 8
EDGES = tuple(sorted({tuple(sorted((i,(i+1) % N))) for i in range(N)} |
                     {tuple(sorted((i,(i+SHIFTS[i]) % N))) for i in range(N)}))
assert len(EDGES) == 36
EDGE_INDEX = {e:i for i,e in enumerate(EDGES)}
GRAPH = nx.Graph()
GRAPH.add_nodes_from(range(N))
GRAPH.add_edges_from(EDGES)
assert all(d == 3 for _,d in GRAPH.degree())
assert nx.is_biconnected(GRAPH)

# Canonical length-seven cycles: minimum vertex first, orientation chosen
# by second vertex < last vertex. Explicitly exclude shorter cycles.
ADJ = [set(GRAPH.neighbors(i)) for i in range(N)]
def enumerate_cycles(k):
    result = set()
    for start in range(N):
        def visit(path):
            if len(path) == k:
                if start in ADJ[path[-1]] and path[1] < path[-1]:
                    result.add(tuple(path))
                return
            for v in sorted(ADJ[path[-1]]):
                if v > start and v not in path:
                    visit(path + [v])
        for second in sorted(ADJ[start]):
            if second > start:
                visit([start,second])
    return tuple(sorted(result))
assert all(len(enumerate_cycles(k))==0 for k in range(3,7))
CYCLES = enumerate_cycles(7)
assert len(CYCLES) == 32

# Unordered discrete configuration, with each graph edge oriented upwards.
CELLS0 = tuple(combinations(range(N),2))
CELLS1 = tuple((v,i) for v in range(N) for i,(a,b) in enumerate(EDGES) if v not in (a,b))
CELLS2 = tuple((i,j) for i,(a,b) in enumerate(EDGES)
                     for j,(c,d) in enumerate(EDGES) if i<j and len({a,b,c,d})==4)
assert (len(CELLS0),len(CELLS1),len(CELLS2)) == (276,792,558)
i0={z:i for i,z in enumerate(CELLS0)}
i1={z:i for i,z in enumerate(CELLS1)}
i2={z:i for i,z in enumerate(CELLS2)}
D1=np.zeros((len(CELLS0),len(CELLS1)),dtype=np.int16)
for j,(v,i) in enumerate(CELLS1):
    a,b=EDGES[i]
    D1[i0[tuple(sorted((v,b)))],j] += 1
    D1[i0[tuple(sorted((v,a)))],j] -= 1
D2=np.zeros((len(CELLS1),len(CELLS2)),dtype=np.int16)
for j,(i,k) in enumerate(CELLS2):
    a,b=EDGES[i]; c,d=EDGES[k]
    D2[i1[(b,k)],j]+=1
    D2[i1[(a,k)],j]-=1
    D2[i1[(d,i)],j]-=1
    D2[i1[(c,i)],j]+=1
assert not (D1 @ D2).any()

def rank_mod(a,p,with_columns=False):
    x=np.asarray(a,dtype=np.int64).copy() % p
    m,n=x.shape
    r=0;pivots=[]
    for col in range(n):
        nz=np.flatnonzero(x[r:,col])
        if len(nz)==0:continue
        k=r+int(nz[0])
        if k!=r:x[[r,k],:]=x[[k,r],:]
        x[r,col:] = x[r,col:]*pow(int(x[r,col]),-1,p) % p
        rows=np.flatnonzero(x[r+1:,col])+r+1
        if len(rows):x[rows,col:] = (x[rows,col:]-x[rows,col,None]*x[r,col:])%p
        pivots.append(col);r+=1
        if r==m:break
    return (r,pivots) if with_columns else r

r_d2 = rank_mod(D2,101)
assert r_d2 == 504
oriented=[];vertex_sets=[]
for cycle in CYCLES:
    vertex_sets.append(set(cycle))
    oriented.append(tuple((EDGE_INDEX[tuple(sorted((u,v)))],1 if u<v else -1)
                 for u,v in zip(cycle,cycle[1:]+cycle[:1])))
PAIRS=[];torus=[]
for i,j in combinations(range(len(CYCLES)),2):
    if vertex_sets[i] & vertex_sets[j]:continue
    z=np.zeros(len(CELLS2),dtype=np.int16)
    for a,sa in oriented[i]:
        for b,sb in oriented[j]:
            z[i2[tuple(sorted((a,b)))]] += sa*sb*(1 if a<b else -1)
    PAIRS.append((i,j));torus.append(z)
assert len(PAIRS)==152
T=np.column_stack(torus)
assert not (D2 @ T).any()
rank_torus,pivcols=rank_mod(T,101,True)
assert rank_torus==54
rank_rows,selected_rows=rank_mod(T[:,pivcols].T,101,True)
assert rank_rows==54
# Unit-minor is an exact integral certificate, not a finite-field inference.
unit_minor=Matrix(T[np.ix_(selected_rows,pivcols)].tolist()).det(method='domain-ge')
assert unit_minor==1
assert rank_mod(T,2)==54

# The 32 automorphisms act on unoriented cycle-pair supports.
CYCLE_IDX={frozenset(c):i for i,c in enumerate(CYCLES)}
PAIR_IDX={pair:i for i,pair in enumerate(PAIRS)}
automorphisms=list(nx.algorithms.isomorphism.GraphMatcher(GRAPH,GRAPH).isomorphisms_iter())
assert len(automorphisms)==32
actions=[]
for f in automorphisms:
    image=[CYCLE_IDX[frozenset(f[v] for v in c)] for c in CYCLES]
    actions.append(tuple(PAIR_IDX[tuple(sorted((image[i],image[j])))] for i,j in PAIRS))
remaining=set(range(152));orbits=[]
while remaining:
    anchor=min(remaining)
    orbit=sorted({action[anchor] for action in actions})
    assert set(orbit) <= remaining
    orbits.append(orbit)
    remaining-=set(orbit)
assert list(map(len,orbits))==[16,32,16,8,32,32,16]

# Projection onto selected squares is an integral isomorphism on H_2:
# 54 torus columns form a unimodular minor, while D_2 has rank 504.
coordinates=T[selected_rows,:]
for size in (1,2,3,4):
    mod2_max=max(rank_mod(coordinates[:,[j for i in subset for j in orbits[i]]],2)
                 for subset in combinations(range(7),size))
    assert mod2_max == {1:31,2:46,3:51,4:53}[size]

# Three orbits are enough rationally but not integrally; their exact
# quotient has elementary divisors 2,2,4 (index 16).
def invariants(subset):
    cols=[j for i in subset for j in orbits[i]]
    S=smith_normal_form(Matrix(coordinates[:,cols].tolist()),domain=ZZ)
    diag=[abs(int(S[i,i])) for i in range(min(S.shape))]
    return Counter(diag)
assert rank_mod(coordinates[:,[j for i in (1,3,4) for j in orbits[i]]],101)==54
assert invariants((1,3,4))==Counter({1:51,2:2,4:1})
# Five orbits suffice integrally, and four orbits never suffice, by mod 2.
assert invariants((0,1,2,3,5))==Counter({1:54})

print('VERIFY_OK_MCGEE_SHORTEST_CYCLE_TORI_FIVE_ORBIT_THRESHOLD')
print('GRAPH',GRAPH.number_of_nodes(),GRAPH.number_of_edges(),'GIRTH',7,'AUTOMORPHISMS',len(automorphisms))
print('UNORDERED_CELLS',len(CELLS0),len(CELLS1),len(CELLS2),'D1D2_ZERO')
print('D2_RANK_MOD_101',r_d2,'H2_INTEGRAL_RANK',len(CELLS2)-r_d2)
print('HEPTAGONS',len(CYCLES),'DISJOINT_PAIRS',len(PAIRS),'TORUS_RANK_MOD_101',rank_torus)
print('UNIT_MINOR',int(unit_minor),'PIVOT_COLUMNS',tuple(pivcols))
print('PIVOT_SQUARE_ROWS',tuple(selected_rows))
print('SEVEN_ORBIT_SIZES',tuple(map(len,orbits)))
print('FOUR_ORBIT_MOD2_MAX',53)
print('THREE_ORBIT_QUOTIENT',dict(invariants((1,3,4))))
print('FIVE_ORBIT_QUOTIENT',dict(invariants((0,1,2,3,5))))
