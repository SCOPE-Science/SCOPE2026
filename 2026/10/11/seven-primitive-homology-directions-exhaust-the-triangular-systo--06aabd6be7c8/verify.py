#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
from math import gcd
import re

RAW = r'''
a1a2b1b2c1, a1b1b2c1c2, a1a2b1c1c2, a1a2a4b1c2, a2b1b2b4c1, a1b2c1c2c4,
a1a2a4b2c2, a2b1b2b4c2, a2b2c1c2c4, a1a4b1b2c2, a2b1b4c1c2, a1a2b2c1c4,
a1a2b2c2c4, a2a4b1b2c2, a2b2b4c1c2, a1a2a3a4b2, b1b2b3b4c2, a2c1c2c3c4,
a1a2a3b1b2, b1b2b3c1c2, a1a2c1c2c3, a1a2c1c3c4, a1a3a4b1b2, b1b3b4c1c2,
a1a2c2c3c4, a2a3a4b1b2, b2b3b4c1c2, a1a2a3a5b1, b1b2b3b5c1, a1c1c2c3c5,
a1a2a4a5b1, b1b2b4b5c1, a1c1c2c4c5, a1a3a4a5b1, b1b3b4b5c1, a1c1c3c4c5,
a2a3a4a5c5, a5b2b3b4b5, b5c2c3c4c5, a2a3a4b1c5, a5b2b3b4c1, a1b5c2c3c4,
a2a3a5b1c5, a5b2b3b5c1, a1b5c2c3c5, a2a4a5b1c5, a5b2b4b5c1, a1b5c2c4c5,
a3a4a5b1c4, a4b3b4b5c1, a1b4c3c4c5, a3a4b1c4c5, a4a5b3b4c1, a1b4b5c3c4,
a3a5b1c4c5, a4a5b3b5c1, a1b4b5c3c5, a4a5b1c4c5, a4a5b4b5c1, a1b4b5c4c5,
a3a4a5c3c4, a3a4b3b4b5, b3b4c3c4c5, a3a4a5c3c5, a3a5b3b4b5, b3b5c3c4c5,
a3a4c3c4c5, a3a4a5b3b4, b3b4b5c3c4, a4a5c3c4c5, a3a4a5b4b5, b3b4b5c4c5,
a3a5c2c3c4, a2a3a4b3b5, b2b3b4c3c5, a3a5c2c3c5, a2a3a5b3b5, b2b3b5c3c5,
a3a5c2c4c5, a2a4a5b3b5, b2b4b5c3c5, a2a3a4a5b5, b2b3b4b5c5, a5c2c3c4c5,
a1a2a3a4b3, b1b2b3b4c3, a3c1c2c3c4, a1a2a3a5b3, b1b2b3b5c3, a3c1c2c3c5,
a1a2a4a5b3, b1b2b4b5c3, a3c1c2c4c5, a1a3a4a5b3, b1b3b4b5c3, a3c1c3c4c5
'''

V = [f'{x}{i}' for x in 'abc' for i in range(1,6)]
VID = {v:i for i,v in enumerate(V)}
facets = []
for token in re.findall(r'(?:[abc][1-5]){5}', RAW):
    labels = re.findall(r'[abc][1-5]', token)
    facets.append(tuple(sorted(VID[x] for x in labels)))
F = set(facets)
assert len(facets) == len(F) == 96

def faces(k):
    return sorted({c for f in F for c in combinations(f,k)})

E, T, Q = faces(2), faces(3), faces(4)
assert (len(V),len(E),len(T),len(Q),len(F)) == (15,105,230,240,96)
assert len(E) == 15*14//2

# Contract the star at a1. Since the graph is complete, this is a spanning tree.
TREE = {(0,j) for j in range(1,15)}
NTE = [e for e in E if e not in TREE]
EI = {e:i for i,e in enumerate(NTE)}
assert len(NTE) == 91

def relation(t):
    a,b,c = t
    row = [0]*len(NTE)
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        if e in EI:
            row[EI[e]] += s
    return row

A = [relation(t) for t in T]
m,n = len(A),len(A[0])
Qchange = [[int(i==j) for j in range(n)] for i in range(n)]
k = 0
while k < min(m,n):
    pos = None
    for i in range(k,m):
        for j in range(k,n):
            if abs(A[i][j]) == 1:
                pos = (i,j)
                break
        if pos is not None:
            break
    if pos is None:
        break
    i,j = pos
    A[k],A[i] = A[i],A[k]
    if j != k:
        for row in A:
            row[k],row[j] = row[j],row[k]
        for row in Qchange:
            row[k],row[j] = row[j],row[k]
    if A[k][k] == -1:
        A[k] = [-x for x in A[k]]
    for i2 in range(m):
        if i2 != k and A[i2][k]:
            q = A[i2][k]
            A[i2] = [x-q*y for x,y in zip(A[i2],A[k])]
    for j2 in range(n):
        if j2 != k and A[k][j2]:
            q = A[k][j2]
            for i2 in range(m):
                A[i2][j2] -= q*A[i2][k]
            for i2 in range(n):
                Qchange[i2][j2] -= q*Qchange[i2][k]
    k += 1

assert k == 88
assert all(A[i][j] == (1 if i == j and i < 88 else 0)
           for i in range(m) for j in range(n))
# Thus H_1 is Z^3 and the last three transformed coordinates are an integral basis.

def chain_coords_order(order):
    x = [0]*n
    cyc = [(order[0],order[1]),(order[1],order[2]),(order[2],order[0])]
    for u,v in cyc:
        if u < v:
            e,s = (u,v),1
        else:
            e,s = (v,u),-1
        if e in EI:
            x[EI[e]] += s
    y = [sum(x[i]*Qchange[i][j] for i in range(n)) for j in range(n)]
    return tuple(y[88:])

def sorted_triangle_coords(t):
    return chain_coords_order(tuple(sorted(t)))

def adapted(c):
    # Cyclic symmetry basis g1=e1, g2=-e3, g3=e2.
    return (c[0],-c[2],c[1])

def canonical_sign(c):
    for z in c:
        if z < 0:
            return tuple(-x for x in c)
        if z > 0:
            return tuple(c)
    return tuple(c)

TSET = set(T)
empty = [s for s in combinations(range(15),3) if s not in TSET]
assert len(empty) == 455-230 == 225
coords = [adapted(sorted_triangle_coords(t)) for t in empty]
assert all(c != (0,0,0) for c in coords)
assert all(gcd(gcd(abs(c[0]),abs(c[1])),abs(c[2])) == 1 for c in coords)

counts = Counter(canonical_sign(c) for c in coords)
expected = Counter({
    (1,0,0):46,
    (0,1,0):46,
    (0,0,1):46,
    (1,1,0):18,
    (1,0,1):18,
    (0,1,1):18,
    (1,1,1):33,
})
assert counts == expected

# Verify the published order-three automorphism and a symmetry-adapted integral basis.
p = {}
for i in range(1,6):
    p[VID[f'a{i}']] = VID[f'b{i}']
    p[VID[f'b{i}']] = VID[f'c{i}']
    p[VID[f'c{i}']] = VID[f'a{i}']
assert {tuple(sorted(p[x] for x in f)) for f in F} == F

g1 = (VID['a1'],VID['a2'],VID['b4'])
g2 = tuple(p[x] for x in g1)
g3 = tuple(p[x] for x in g2)
assert tuple(p[x] for x in g3) == g1
assert all(tuple(sorted(g)) in empty for g in (g1,g2,g3))
assert [adapted(chain_coords_order(g)) for g in (g1,g2,g3)] == [
    (1,0,0),(0,1,0),(0,0,1)
]

print(
    'VERIFY_OK f=15,105,230,240,96 H1_Z=Z^3 '
    'graph_triangles=455 facial3=230 empty3=225 '
    'all_empty3_nonzero_primitive=yes simple_integral_1_systole=3 '
    'unoriented_classes=7 binary_subset_shell=yes '
    'singleton_counts=46x3 pair_counts=18x3 triple_count=33 '
    'order3_basis_cycle=yes smith=1^88,0^3'
)
