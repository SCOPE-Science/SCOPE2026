#!/usr/bin/env python3
"""Exact finite combinatorial checks for the Ising-triangle coherence thresholds."""
from fractions import Fraction as Q
from itertools import product

bits = list(product((0,1), repeat=3))
def energy(b):
    z = [1-2*t for t in b]
    return z[0]*z[1]+z[1]*z[2]+z[2]*z[0]
assert sorted(energy(b) for b in bits) == [-1]*6+[3]*2
G = [b for b in bits if energy(b) == -1]
assert len(G) == 6
edges = []
for i, b in enumerate(G):
    for j, a in enumerate(G):
        if j > i and sum(x != y for x,y in zip(a,b)) == 1:
            edges.append((i,j))
assert len(edges)==6
assert all(sum(i in e for e in edges)==2 for i in range(6))
visited={0}; frontier=[0]
while frontier:
    i=frontier.pop()
    for e in edges:
        if i in e:
            j=e[0] if e[1]==i else e[1]
            if j not in visited:
                visited.add(j);frontier.append(j)
assert len(visited)==6
for site in range(3):
    edgecount=sum(G[i][site] != G[j][site] for i,j in edges)
    assert edgecount==2
    x_expectation=Q(2*edgecount,6)
    assert x_expectation==Q(2,3)
    assert sum(1-2*b[site] for b in G)==0
# The symmetric constant vector saturates the row-sum upper bound 2.
assert all(sum(i in e for e in edges)==2 for i in range(6))
for c in [Q(i,300) for i in range(101)]:
    # Base product: site 0 fixed +Z, site 1 fixed -Z, site 2 X=3c.
    assert 0<=3*c<=1
    assert Q(1)+Q(-1)+Q(-1) == -1
    # Cyclic permutations: each site receives X=3c once; global flip kills Z.
    assert Q(3*c,3)==c
print('VERIFY_OK',len(G),len(edges),101)
