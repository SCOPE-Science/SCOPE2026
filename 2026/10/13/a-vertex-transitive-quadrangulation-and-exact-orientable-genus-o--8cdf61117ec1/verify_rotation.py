#!/usr/bin/env python3
"""Exact face-tracing certificate for the bipartite Kneser graph H(8,3).
Uses polynomial representatives of GF(8)=GF(2)[z]/(z^3+z+1).
No third-party modules or network access are needed.
"""
from itertools import combinations
from collections import deque, Counter

# Multiplication in GF(8) by binary polynomial arithmetic and reduction.
def product(a, b):
    polynomial = 0
    for j in range(3):
        if (b >> j) & 1:
            polynomial ^= a << j
    for j in (4, 3):
        if (polynomial >> j) & 1:
            polynomial ^= 0b1011 << (j-3)
    return polynomial

field = range(8)
G = [(a,b) for a in range(1,8) for b in field]  # maps t -> a*t+b
identity = (1,0)
def compose(g,h):  # first apply h, then g
    a,b = g
    c,d = h
    return (product(a,c), product(a,d)^b)
def inverse(g):
    return next(h for h in G if compose(g,h)==identity and compose(h,g)==identity)

P = frozenset((0,1,2))
def translate(g,S):
    a,b=g
    return frozenset(product(a,x)^b for x in S)

targets = {g:translate(g,P) for g in G}
assert len(G)==len(set(targets.values()))==56, 'affine action not regular on triples'
S = [g for g in G if P.isdisjoint(targets[g])]
assert len(S)==10
assert {inverse(s) for s in S} == set(S)
assert identity not in S

# Explicit 10-cycle in S; sequence specifies rho_A cyclic rotation.
cycle = [(1,4),(1,5),(1,6),(5,6),(3,5),(1,7),(2,7),(4,7),(7,3),(6,3)]
assert len(cycle)==len(set(cycle))==10 and set(cycle)==set(S)
rho = {cycle[i]:cycle[(i+1)%10] for i in range(10)}
rho_inv = {b:a for a,b in rho.items()}
rhoB = {s:inverse(rho_inv[inverse(s)]) for s in S}
assert len(set(rhoB.values()))==10
assert len(set(rho.values()))==10

# Work directly on 3-subset vertices, not only the abstract group multiplication table.
A = sorted(frozenset(c) for c in combinations(field,3))
assert len(A)==56
triple_id = {t:i for i,t in enumerate(A)}

def ID(g,side):return 56*side+triple_id[targets[g]]

neighbors = {v:set() for v in range(112)}
rotation = {}
for g in G:
    a = ID(g,0)
    around_a = tuple(ID(compose(g,s),1) for s in cycle)
    assert len(set(around_a))==10
    rotation[a]=around_a
    for b in around_a:
        assert A[a].isdisjoint(A[b-56])
        neighbors[a].add(b)
        neighbors[b].add(a)
    b = ID(g,1)
    cycB=[]
    s=cycle[0]
    for _ in range(10):
        cycB.append(ID(compose(g,inverse(s)),0))
        s=rhoB[s]
    assert s==cycle[0] and len(set(cycB))==10
    rotation[b]=tuple(cycB)

assert all(len(neighbors[v])==10 for v in neighbors)
assert all(set(rotation[v])==neighbors[v] for v in range(112))
assert all(neighbors[v]=={w for w in range(112) if (w//56)!=(v//56) and A[v%56].isdisjoint(A[w%56])} for v in range(112))

# Connectivity and undirected edge count.
seen={0}; queue=deque((0,))
while queue:
    v=queue.popleft()
    for w in neighbors[v]:
        if w not in seen:seen.add(w);queue.append(w)
assert len(seen)==112
E=sum(map(len,neighbors.values()))//2
assert E==560

# Every directed edge is a dart (v,w). Rotation map R follows successor of w at v.
darts={(v,w) for v in neighbors for w in neighbors[v]}
assert len(darts)==2*E==1120
successor = {v: {seq[i]:seq[(i+1)%len(seq)] for i in range(10)} for v,seq in rotation.items()}
def face_step(d):
    v,w=d
    return (w,successor[w][v])  # R(tau(v->w))
assert {face_step(d) for d in darts}==darts
faces=[]
remaining=set(darts)
while remaining:
    first=min(remaining); face=[]; d=first
    while d in remaining:
        remaining.remove(d);face.append(d);d=face_step(d)
    assert d==first
    faces.append(face)

sizes=Counter(map(len,faces))
assert sizes=={4:280},sizes
assert all(len({v for v,w in f})==4 for f in faces)
V=len(neighbors);F=len(faces)
chi=V-E+F
assert chi==-168 and (2-chi)%2==0
orientable_genus=(2-chi)//2
assert orientable_genus==85
# Edge incidence automatically twice because both oriented darts are assigned one face.
print('CERTIFICATE_OK')
print('field_order=8 polynomial=0b1011')
print('affine_group_size=56; orbit_of_triples=56; connection_set_size=10')
print('vertex_count=112; edge_count=560; darts=1120; faces=280; face_sizes={4:280}')
print('connected=True; facial_walks_simple=True; orientable_genus=85')
print('rotation_cycle='+repr(cycle))
