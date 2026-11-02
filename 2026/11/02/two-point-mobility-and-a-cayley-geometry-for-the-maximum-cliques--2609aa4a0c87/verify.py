#!/usr/bin/env python3
"""Exhaustive and affine-group certificate for maximum-clique exchanges in Paley(41)."""
from collections import Counter, deque
from itertools import combinations

P = 41
Q = {x*x % P for x in range(1, P)}
assert len(Q) == 20 and all((-r) % P in Q for r in Q)
adj = [{(x+r)%P for r in Q} for x in range(P)]
cliques = []

def extend(c, candidates):
    if len(c) == 5:
        cliques.append(tuple(c))
        return
    if not candidates:
        return
    for i, v in enumerate(candidates):
        extend(c + [v], [w for w in candidates[i+1:] if w in adj[v]])

extend([], list(range(P)))
C = set(cliques)
assert len(C) == len(cliques) == 205
assert all(not set.intersection(*(adj[x] for x in c)) - set(c) for c in C)
B = (0, 1, 2, 10, 33)
assert B in C
H = (1, 10, 16, 18, 37)
assert {pow(10, k, P) for k in range(5)} == set(H)
assert all(a in Q for a in H)

act = lambda b, a: tuple(sorted((a*x + b) % P for x in B))
orb = {(b,a):act(b,a) for a in H for b in range(P)}
assert len(orb) == len(set(orb.values())) == 205
assert set(orb.values()) == C
R = Counter(len(set(B).intersection(c)) for c in C)
assert R == {5: 1, 3: 8, 2: 16, 1: 64, 0: 116}
S = {g for g,c in orb.items() if len(set(B).intersection(c)) == 3}
assert S == {(0,10),(0,37),(1,37),(9,37),(10,37),(23,10),(31,10),(33,10)}
assert all(len(set(B).intersection(c)) != 4 for c in C)

def multiply(g,h):
    b,a = g
    d,c = h
    return ((b + a*d)%P, (a*c)%P)

def inverse(g):
    b,a = g
    i = pow(a,-1,P)
    return ((-i*b)%P, i)

assert set(map(inverse,S)) == S
dist = {(0,1):0}
queue = deque([(0,1)])
while queue:
    g = queue.popleft()
    for s in S:
        h = multiply(g,s)
        if h not in dist:
            dist[h] = dist[g] + 1
            queue.append(h)
assert Counter(dist.values()) == {0:1,1:8,2:36,3:98,4:62}
assert len(dist) == 205
# Because left translation permutes edges, all vertices have this distance profile.
for g,c in orb.items():
    for s in S:
        neighbor=orb[multiply(g,s)]
        assert len(set(c).intersection(neighbor)) == 3

# Full affine orbit is the same state space; four transformations fix B.
full = {tuple(sorted((a*x+b)%P for x in B)) for a in Q for b in range(P)}
assert full == C
stabilizer = [(a,b) for a in Q for b in range(P)
              if set((a*x+b)%P for x in B) == set(B)]
assert stabilizer == [(1,0),(9,33),(32,10),(40,2)]
print('CLIQUE_CERTIFICATE_OK order=41 omega=5 cliques=205')
print('AFFINE_CERTIFICATE_OK regular_group=205 full_affine_orbit=205 stabilizer=4')
print('EXCHANGE_CERTIFICATE_OK single_swap_edges=0 double_swap_edges=820')
print('DISTANCE_CERTIFICATE_OK shells=1,8,36,98,62 radius=4 diameter=4')
print('FULL_CERTIFICATE_OK')
