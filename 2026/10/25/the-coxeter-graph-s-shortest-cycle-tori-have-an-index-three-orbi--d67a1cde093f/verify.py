"""Exact integral chain and lattice verifier for the Coxeter graph's shortest-cycle tori.

Dependencies: Python >= 3.11, networkx==3.6.1, sympy==1.14.0.
Run: python coxeter_heptagon_verify.py
"""
from collections import Counter
from itertools import combinations
from math import comb, gcd
import random
import networkx as nx
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

# The Fano lines are {a,b,a xor b} on the seven nonzero binary triples.
lines = {frozenset((a,b,a^b)) for a in range(1,8) for b in range(a+1,8)}
assert len(lines) == 7
triples = [t for t in combinations(range(1,8),3) if frozenset(t) not in lines]
assert len(triples) == 28
edges = [(i,j) for i in range(28) for j in range(i+1,28)
         if set(triples[i]).isdisjoint(triples[j])]
assert len(edges) == 42
neighbors = [set() for _ in range(28)]
for a,b in edges:
    neighbors[a].add(b); neighbors[b].add(a)
assert all(len(x)==3 for x in neighbors)

# Canonical simple cycles: smallest vertex first, smaller neighbor second.
def cycles_upto(limit):
    found = set()
    for root in range(28):
        def search(path):
            for v in sorted(neighbors[path[-1]]):
                if v == root and len(path) >= 3:
                    if path[1] < path[-1]:
                        found.add(tuple(path))
                elif v > root and v not in path and len(path) < limit:
                    search(path + [v])
        search([root])
    return sorted(found,key=lambda x:(len(x),x))
cycles = cycles_upto(7)
assert len(cycles) == 24 and {len(c) for c in cycles} == {7}
heptagon_pairs = [(x,y) for j,x in enumerate(cycles) for y in cycles[j+1:]
                  if set(x).isdisjoint(y)]
assert len(heptagon_pairs) == 108

# Unordered cubical deleted-product cells, with each graph edge increasing.
vertex_pairs = list(combinations(range(28),2))
vertex_index = {x:i for i,x in enumerate(vertex_pairs)}
edgestates = [(i,v) for i,(a,b) in enumerate(edges) for v in range(28)
              if v not in (a,b)]
state_index = {x:i for i,x in enumerate(edgestates)}
squares = [(i,j) for i,e in enumerate(edges) for j in range(i+1,42)
           if set(e).isdisjoint(edges[j])]
square_index = {x:i for i,x in enumerate(squares)}
assert (len(vertex_pairs),len(edgestates),len(squares)) == (378,1092,777)

# d1([e,v])=[b,v]-[a,v]; d2([e_i,e_j]) is the product boundary.
def d1_of_state(i,v):
    a,b = edges[i]
    return {vertex_index[tuple(sorted((b,v)))]:1,
            vertex_index[tuple(sorted((a,v)))]:-1}
def square_boundary(i,j):
    a,b = edges[i];c,d=edges[j]
    return {state_index[(j,b)]:1,state_index[(j,a)]:-1,
            state_index[(i,d)]:-1,state_index[(i,c)]:1}
boundary2 = [square_boundary(i,j) for i,j in squares]
for col in boundary2:
    v={}
    for st,coeff in col.items():
        a,b=d1_of_state(*edgestates[st])
        for q,c in ((a,1),(b,-1)):
            v[q]=v.get(q,0)+coeff*c
    assert all(x==0 for x in v.values())

edge_index={e:i for i,e in enumerate(edges)}
def torus(x,y):
    values={}
    for a,b in zip(x,x[1:]+x[:1]):
        i=edge_index[tuple(sorted((a,b)))]
        s=1 if a<b else -1
        for c,d in zip(y,y[1:]+y[:1]):
            j=edge_index[tuple(sorted((c,d)))]
            q=s*(1 if c<d else -1)*(1 if i<j else -1)
            k=square_index[tuple(sorted((i,j)))]
            values[k]=values.get(k,0)+q
    return {k:v for k,v in values.items() if v}
tori=[torus(x,y) for x,y in heptagon_pairs]
for tor in tori:
    b={}
    assert len(tor)==49 and set(map(abs,tor.values()))=={1}
    for q,c in tor.items():
        for r,d in boundary2[q].items():
            b[r]=b.get(r,0)+c*d
    assert all(x==0 for x in b.values())

# Exact sparse finite-field Gaussian elimination, by column.
def column_elim(cols,p):
    pivots={};chosen={}
    for k,c in enumerate(cols):
        v={i:a%p for i,a in c.items() if a%p}
        while v:
            r=min(v)
            if r not in pivots:
                inv=pow(v[r],-1,p)
                pivots[r]={i:(a*inv)%p for i,a in v.items()}
                chosen[r]=k
                break
            factor=v[r]
            for i,a in pivots[r].items():
                t=(v.get(i,0)-factor*a)%p
                if t:v[i]=t
                else:v.pop(i,None)
    return len(pivots),list(pivots),list(chosen.values())

assert column_elim(boundary2,101)[0] == 700
assert column_elim(boundary2,2)[0] == 699
r,selected_rows,selected_columns=column_elim(tori,2)
assert r==77
basis = Matrix([[tori[j].get(i,0) for j in selected_columns] for i in selected_rows])
assert basis.det(method='domain-ge') == -1
# Unit minor makes the candidate torus lattice primitive in the 777-cell lattice.
all_rows = Matrix([[tori[j].get(i,0) for j in range(108)] for i in selected_rows])
coordinates = basis.inv()*all_rows
assert all(x.q==1 for x in coordinates)
for j in range(108):
    reconstructed={}
    for k in range(77):
        coeff=int(coordinates[k,j])
        if coeff:
            for i,value in tori[selected_columns[k]].items():
                reconstructed[i]=reconstructed.get(i,0)+coeff*value
    assert {i:v for i,v in reconstructed.items() if v}==tori[j]

# Exhaustive 336-automorphism action, with each heptagon normalized.
graph=nx.Graph()
graph.add_nodes_from(range(28));graph.add_edges_from(edges)
automorphisms=[tuple(phi[i] for i in range(28))
               for phi in nx.algorithms.isomorphism.GraphMatcher(graph,graph).isomorphisms_iter()]
assert len(automorphisms)==336
pair_to_index={p:j for j,p in enumerate(heptagon_pairs)}
def canonical_cycle(c):
    r=c.index(min(c));x=c[r:]+c[:r]
    return x if x[1]<x[-1] else x[:1]+x[:0:-1]
def pair_image(pair,aut):
    return tuple(sorted((canonical_cycle(tuple(aut[v] for v in c)) for c in pair)))
remaining=set(range(108)); orbits=[]
while remaining:
    j=min(remaining)
    orbit={pair_to_index[pair_image(heptagon_pairs[j],aut)] for aut in automorphisms}
    assert orbit<=remaining
    orbits.append(sorted(orbit));remaining-=orbit
assert sorted(map(len,orbits))==[24,84]
bridge2=[];bridge0=[]
for orb in orbits:
    profiles={sum(b in neighbors[a] for a in x for b in y)
              for k in orb for x,y in [heptagon_pairs[k]]}
    assert len(profiles)==1
    if profiles=={2}:bridge2=orb
    elif profiles=={0}:bridge0=orb
assert len(bridge2)==84 and len(bridge0)==24

# For L2 from the 84 bridge-connected pairs, prove index=3 without
# relying on a black-box Smith form: mod 3 rank=76 and two exact
# maximal minors in an integral basis have gcd 3.
assert column_elim([tori[j] for j in bridge2],3)[0]==76
assert column_elim([tori[j] for j in bridge2],101)[0]==77
assert column_elim([tori[j] for j in bridge0],101)[0]==23
_,_,local_columns=column_elim([tori[j] for j in bridge2],2)
minor_columns1=[bridge2[j] for j in local_columns]
d1=int(coordinates[:,minor_columns1].det(method='domain-ge'))
assert d1==-273
shuffled=bridge2.copy();random.Random(18).shuffle(shuffled)
_,_,local_columns=column_elim([tori[j] for j in shuffled],2)
minor_columns2=[shuffled[j] for j in local_columns]
d2=int(coordinates[:,minor_columns2].det(method='domain-ge'))
assert d2==5427 and gcd(abs(d1),abs(d2))==3
# Independent exact Smith calculation on integral coordinate matrices.
for orb,expected_rank,expected_torsion in [(bridge2,77,[3]),(bridge0,23,[])]:
    A=coordinates[:,orb]
    S=smith_normal_form(A,domain=ZZ)
    factors=[abs(int(S[j,j])) for j in range(min(S.rows,S.cols)) if S[j,j]]
    assert len(factors)==expected_rank
    assert [x for x in factors if x!=1]==expected_torsion

print('VERIFY_OK_COXETER_HEPTAGON_TORI_INDEX_THREE')
print('GRAPH_FANO_COXETER',28,42,'GIRTH',7,'AUTOMORPHISMS',len(automorphisms))
print('DELETED_PRODUCT_CELLS',378,1092,777,'BOUNDARY_COMPOSES_ZERO')
print('H2_INTEGRAL_RANK',77,'BOUNDARY2_MOD101_RANK',700)
print('HEPTAGONS',len(cycles),'VERTEX_DISJOINT_PAIRS',len(tori))
print('BRIDGE_ORBITS',[(2,len(bridge2)),(0,len(bridge0))])
print('BRIDGE_TWO_INDEX',3,'MOD3_RANK',76,'MINORS',d1,d2)
print('BRIDGE_ZERO_RANK',23,'EACH_TORUS_COMPLETES_INDEX_THREE')
print('SELECTED_FULL_BASIS_COLUMNS',tuple(selected_columns))
print('SELECTED_FULL_BASIS_ROWS',tuple(selected_rows))
print('SELECTED_FULL_BASIS_DETERMINANT',-1)
