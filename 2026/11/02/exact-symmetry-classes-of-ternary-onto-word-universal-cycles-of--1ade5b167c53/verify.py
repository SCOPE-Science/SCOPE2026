#!/usr/bin/env python3
"""Standalone exact checks for universal cycles of 4-letter ternary onto words.
Python standard library only; run: python3 verify.py
"""
from itertools import product, permutations, combinations
from collections import Counter
from math import factorial

ALPHABET = (0, 1, 2)
EDGES = sorted(w for w in product(ALPHABET, repeat=4) if len(set(w)) == 3)
VERTICES = sorted(set(w[:3] for w in EDGES) | set(w[1:] for w in EDGES))
EID = {w: i for i, w in enumerate(EDGES)}
VID = {v: i for i, v in enumerate(VERTICES)}
TAIL = [VID[w[:3]] for w in EDGES]
HEAD = [VID[w[1:]] for w in EDGES]
OUT = [[] for _ in VERTICES]
for e in range(len(EDGES)):
    OUT[TAIL[e]].append(e)
assert len(EDGES) == 36 and len(VERTICES) == 24
assert Counter(len(a) for a in OUT) == {1: 18, 3: 6}

# Integer Bareiss determinant, unrelated to the DFS tour count.
def det(a):
    a = [list(row) for row in a]
    n = len(a)
    if not n:
        return 1
    sign, prev = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next(j for j in range(k + 1, n) if a[j][k])
            a[k], a[j] = a[j], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                assert num % prev == 0
                a[i][j] = num // prev
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]

def cofactor(lap, root=0):
    return det([[lap[i][j] for j in range(len(lap)) if j != root]
                for i in range(len(lap)) if i != root])

PERMS = sorted(w for w in permutations(ALPHABET))
reduced = {}
for x, y, z in PERMS:
    # Forced-path lengths 1, 2, 3; list of original 4-word edges.
    reduced[(x, y, z)] = [
        ((x,y,z,x),),
        ((x,y,z,y), (y,z,y,x)),
        ((x,y,z,z), (y,z,z,x), (z,z,x,y)),
    ]
    targets = [(y,z,x), (z,y,x), (z,x,y)]
    for path, target in zip(reduced[(x,y,z)], targets):
        assert path[0][:3] == (x,y,z) and path[-1][1:] == target
        assert all(e in EID for e in path)
        assert all(path[i][1:] == path[i+1][:3] for i in range(len(path)-1))
assert len({e for paths in reduced.values() for p in paths for e in p}) == 36

# Reduced graph has the triangular-prism underlying simple graph.
V6 = list(PERMS)
idx = {v: i for i, v in enumerate(V6)}
A = [[0]*6 for _ in range(6)]
for v in V6:
    for p in reduced[v]:
        A[idx[v]][idx[p[-1][1:]]] += 1
assert all(sum(row) == 3 for row in A)
assert all(A[i][j] == A[j][i] for i in range(6) for j in range(6))
prism_edges = [(i,j) for i in range(6) for j in range(i+1,6) if A[i][j]]
assert len(prism_edges) == 9
lap = [[(3 if i == j else 0)-A[i][j] for j in range(6)] for i in range(6)]
assert cofactor(lap) == 75
# Independent matrix-tree check by enumerating 5-edge spanning trees.
trees = 0
for subset in combinations(prism_edges, 5):
    parent = list(range(6))
    def find(u):
        while parent[u] != u:
            u = parent[u]
        return u
    for u,v in subset:
        parent[find(u)] = find(v)
    trees += len({find(i) for i in range(6)}) == 1
assert trees == 75
assert 75 * factorial(2)**6 == 4800

# Quotient by a symbol transposition (0 1).
tau = lambda v: tuple({0:1,1:0,2:2}[c] for c in v)
reps = [(0,1,2),(0,2,1),(2,0,1)]
orbit = {v:i for i,r in enumerate(reps) for v in (r, tau(r))}
Q = [[0]*3 for _ in range(3)]
voltage = 0
for i, r in enumerate(reps):
    for p in reduced[r]:
        v = p[-1][1:]
        j = orbit[v]
        Q[i][j] += 1
        voltage += int(v != reps[j])
assert Q == [[0,1,2],[1,1,1],[2,1,0]]
QL = [[(3 if i == j else 0) - Q[i][j] for j in range(3)] for i in range(3)]
assert cofactor(QL) == 5 and voltage == 7
assert 5 * factorial(2)**3 == 40

# Quotient by cyclic relabeling: sum of voltage increments is 0 mod 3.
sigma = lambda v: tuple((c + 1) % 3 for c in v)
r3 = [(0,1,2),(0,2,1)]
rotorbits = {tuple((c+k)%3 for c in r):i for i,r in enumerate(r3) for k in range(3)}
voltage3 = 0
length3 = 0
for r in r3:
    for p in reduced[r]:
        v = p[-1][1:]
        i = rotorbits[v]
        k = next(k for k in range(3) if tuple((c+k)%3 for c in r3[i]) == v)
        voltage3 += k
        length3 += len(p)
assert voltage3 % 3 == 0 and length3 == 12

# Independent exhaustive DFS in the uncontracted 24-vertex graph.
ROOT_EDGE = EID[(0,1,2,0)]
ROOT = TAIL[ROOT_EDGE]
tours = []
path = [ROOT_EDGE]
def dfs(v, used):
    if len(path) == len(EDGES):
        if v == ROOT:
            w = tuple(EDGES[e][0] for e in path)
            assert {tuple(w[(i+j)%36] for j in range(4)) for i in range(36)} == set(EDGES)
            tours.append(w)
        return
    for e in OUT[v]:
        if not (used >> e) & 1:
            path.append(e)
            dfs(HEAD[e], used | (1 << e))
            path.pop()
dfs(HEAD[ROOT_EDGE], 1 << ROOT_EDGE)
assert len(tours) == 4800 and len(set(tours)) == 4800

# Every tour contains the factor 0120 exactly once, so normalize there.
def normalize(w):
    marks = [i for i in range(36) if tuple(w[(i+j)%36] for j in range(4)) == (0,1,2,0)]
    assert len(marks) == 1
    i = marks[0]
    return tuple(w[i:] + w[:i])
def apply(w, p, reverse=False):
    v = tuple(p[c] for c in w)
    return normalize(v[::-1] if reverse else v)

fix = {}
for p in PERMS:
    for r in (False, True):
        fix[(p,r)] = sum(apply(w,p,r) == w for w in tours)
assert fix[((0,1,2),False)] == 4800
assert sorted(v for (p,r),v in fix.items() if not r and p != (0,1,2)) == [0,0,40,40,40]
assert all(fix[(p,True)] == 0 for p in PERMS)
assert sum(fix[(p,False)] for p in PERMS) // 6 == 820
assert sum(fix.values()) // 12 == 410

print('VERIFY_OK directed=36 vertices=24 prism_trees=75 cycles=4800')
print('VERIFY_OK transposition_fixed=40 three_cycle_fixed=0 reversal_fixed=0')
print('VERIFY_OK alphabet_orbits=820 alphabet_reversal_orbits=410')
print('WITNESS', ''.join(map(str, tours[0])))
