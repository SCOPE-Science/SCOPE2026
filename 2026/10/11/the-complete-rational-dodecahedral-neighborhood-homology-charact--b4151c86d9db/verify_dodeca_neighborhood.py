#!/usr/bin/env python3
"""Exact finite chain-character calculation for the dodecahedral open-neighborhood complex.

Usage: python3 verify_dodeca_neighborhood.py
Uses Python's standard library only.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations

V = tuple(range(20))
E = set()
for i in range(10):
    E.add(tuple(sorted((i, (i + 1) % 10))))
    E.add(tuple(sorted((i, 10 + i))))
    E.add(tuple(sorted((10 + i, 10 + (i + 2) % 10))))
assert len(E) == 30
N = {i: set() for i in V}
for a,b in E:
    N[a].add(b); N[b].add(a)
assert all(len(N[i]) == 3 for i in V)

# All-pairs shortest paths, determined without external graph libraries.
D = []
for v in V:
    distances = {v:0};front = [v]
    for x in front:
        for y in sorted(N[x]):
            if y not in distances:
                distances[y] = distances[x] + 1;front.append(y)
    assert len(distances) == 20
    D.append([distances[i] for i in V])
assert max(map(max,D)) == 5
assert all(sum(D[x][y] == 5 for y in V) == 1 for x in V)
Z = tuple(next(y for y in V if D[x][y] == 5) for x in V)

# Every graph automorphism is uniquely identified by the images of root 0
# and its ordered three neighbors. Distances supply unique extensions.
R = (0, 1, 9, 10)
def signature(x, refs):
    return tuple(D[x][r] for r in refs)
assert len({signature(x, R) for x in V}) == 20
AUT = set()
for image0 in V:
    for nb_images in permutations(sorted(N[image0])):
        refs = (image0,) + nb_images
        candidate_inv = {signature(y, refs):y for y in V}
        if len(candidate_inv) != 20:
            continue
        p = tuple(candidate_inv[signature(x, R)] for x in V)
        assert len(set(p)) == 20
        if {tuple(sorted((p[u], p[v]))) for u,v in E} == E:
            AUT.add(p)
assert len(AUT) == 120

I = V
P = (1, 2, 12, 14, 16, 6, 7, 17, 19, 11, 0, 3, 10, 4, 18, 5, 8, 15, 9, 13)
Q = (0, 9, 19, 17, 15, 5, 4, 14, 12, 10, 1, 8, 11, 7, 13, 6, 3, 16, 2, 18)
assert P in AUT and Q in AUT and Z in AUT

def mult(p, q):
    return tuple(p[q[x]] for x in V)

def perm_order(p):
    x = I
    for j in range(1,121):
        x = mult(p,x)
        if x == I:return j
    raise AssertionError("order bound")

def generated(gens):
    seen = {I}; queue = [I]
    for x in queue:
        for g in gens:
            y = mult(x,g)
            if y not in seen:
                seen.add(y);queue.append(y)
    return seen

ROT = generated([P,Q]); GROUP = generated([P,Q,Z])
assert perm_order(P) == 5 and perm_order(Q) == 3 and perm_order(Z) == 2
assert len(ROT) == 60 and GROUP == AUT
assert Z not in ROT and all(mult(Z,r) == mult(r,Z) for r in ROT)
assert Counter(map(perm_order, ROT)) == {1:1,2:15,3:20,5:24}
assert all(mult(Z,r) not in ROT for r in ROT)

# Build the ordinary open-neighborhood complex exactly.
triangles = {tuple(sorted(N[x])) for x in V}
edges = {tuple(sorted(ee)) for t in triangles for ee in combinations(t, 2)}
assert len(triangles) == 20 and len(edges) == 60
multiplicity = Counter(edge for tri in triangles for edge in combinations(tri,2))
assert set(multiplicity.values()) == {1}  # Each triangle has only free edges.

# The distance-two graph is connected: the input graph has a five-cycle.
reached = {0};queue = [0]
for u in queue:
    for a,b in edges:
        v = b if u == a else (a if u == b else None)
        if v is not None and v not in reached:
            reached.add(v);queue.append(v)
assert reached == set(V)
assert len(edges) - 20 + 1 == 41  # Rank of the full 1-skeleton.
assert len(edges) - len(triangles) - len(V) + 1 == 21

# Signed simplicial trace on chains; because H0=Q, H2=0,
# chi_H1(g) = 1 - trace_C0(g) + trace_C1(g) - trace_C2(g).
def signed_fixed(face, p):
    img = [p[x] for x in face]
    if tuple(sorted(img)) != face:return 0
    inversions = sum(img[i] > img[j] for i in range(len(img)) for j in range(i+1,len(img)))
    return -1 if inversions % 2 else +1

def homology_trace(p):
    return (1 - sum(signed_fixed((x,),p) for x in V)
              + sum(signed_fixed(e,p) for e in edges)
              - sum(signed_fixed(t,p) for t in triangles))

traces = {r:homology_trace(r) for r in GROUP}
rot_rows=defaultdict(set);twisted_rows=defaultdict(set)
for r in ROT:
    k=perm_order(r)
    rot_rows[k].add(traces[r]);twisted_rows[k].add(traces[mult(Z,r)])
assert dict(rot_rows)=={1:{21},2:{1},3:{-3},5:{1}}
assert dict(twisted_rows)=={1:{1},2:{-3},3:{1},5:{1}}

# Rational A5 characters, class order 1,2,3,5a,5b; both order-5
# classes occur 12 times. The last two are grouped because all relevant
# character values are rational and equal on the order-five classes.
weights=(1,15,20,24)
chars = {
    '1': (1,1,1,1),
    'V4':(4,0,1,-1),
    'V5':(5,1,-1,0),
    'W6':(6,-2,0,1),
}
chi_plus = tuple((list(rot_rows[k])[0]+list(twisted_rows[k])[0])//2 for k in (1,2,3,5))
chi_minus = tuple((list(rot_rows[k])[0]-list(twisted_rows[k])[0])//2 for k in (1,2,3,5))
assert chi_plus == (11,-1,-1,1) and chi_minus == (10,2,-2,0)
def inner(a,b):
    numerator = sum(w*x*y for w,x,y in zip(weights,a,b))
    assert numerator%60==0
    return numerator//60
assert {label:inner(chi_plus, char) for label,char in chars.items()}=={'1':0,'V4':0,'V5':1,'W6':2}
assert {label:inner(chi_minus,char) for label,char in chars.items()}=={'1':0,'V4':0,'V5':2,'W6':0}
assert inner(chars['W6'],chars['W6'])==2  # Galois-paired rational six-dimensional module.
print('AUT=120; ROT=60; simplices=(20,60,20); reduced H1 rank=21')
print('Rotations order 1,2,3,5: traces (21,1,-3,1)')
print('Inversion times rotations: traces (1,-3,1,1)')
print('Antipodal + character:',chi_plus,'= W6 + V5')
print('Antipodal - character:',chi_minus,'= 2 V5')
print('VERIFY_OK')
