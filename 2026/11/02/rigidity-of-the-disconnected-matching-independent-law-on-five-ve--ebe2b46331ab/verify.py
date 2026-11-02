#!/usr/bin/env python3
"""Exact standalone checks for five-vertex matching-independent connectivity rigidity."""
from fractions import Fraction as F
from itertools import combinations

V = tuple(range(5))
EDGES = tuple(combinations(V, 2))
EIDX = {e: i for i, e in enumerate(EDGES)}

def mask_for(parts):
    return sum(1 << EIDX[e] for part in parts for e in combinations(sorted(part), 2))

def components(mask):
    adj = [set() for _ in V]
    for i, (u, v) in enumerate(EDGES):
        if mask >> i & 1:
            adj[u].add(v); adj[v].add(u)
    seen = set(); comp = []
    for v in V:
        if v not in seen:
            todo = [v]; seen.add(v); part = []
            while todo:
                z = todo.pop(); part.append(z)
                for w in adj[z]:
                    if w not in seen:
                        seen.add(w); todo.append(w)
            comp.append(part)
    return comp

DISJOINT = tuple((i, j) for i, e in enumerate(EDGES)
                 for j, f in enumerate(EDGES) if i < j and not (set(e) & set(f)))
assert len(DISJOINT) == 15

def q(mask):
    return sum(bool(mask >> i & 1 and mask >> j & 1) for i, j in DISJOINT)

# Exact arithmetic in Q(sqrt(5)).
ZERO = (F(0), F(0))
ONE = (F(1), F(0))
A = (F(-2, 5), F(1, 5))
B = (F(3, 10), F(-1, 10))
P = (F(0), F(1, 5))

def add(x, y):
    return (x[0]+y[0], x[1]+y[1])

def mul(x, y):
    return (x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0])

def total(vals):
    z = ZERO
    for t in vals:
        z = add(z, t)
    return z

support = {}
for z in V:
    m = mask_for([set(V)-{z}, {z}]); assert m not in support
    support[m] = A
for uv in EDGES:
    m = mask_for([set(uv), set(V)-set(uv)]); assert m not in support
    support[m] = B
assert len(support) == 15
assert total(support.values()) == ONE
assert all(len(components(m)) > 1 and q(m) == 3 for m in support)
count = 0
maximal = set()
for m in range(1 << len(EDGES)):
    if len(components(m)) > 1:
        assert q(m) <= 3
        if q(m) == 3: maximal.add(m)
    count += 1
assert maximal == set(support)

def measure(predicate):
    return total(w for m, w in support.items() if predicate(m))

for i in range(len(EDGES)):
    assert measure(lambda m, i=i: bool(m >> i & 1)) == P
for i, j in DISJOINT:
    assert measure(lambda m, i=i, j=j: bool(m >> i & 1 and m >> j & 1)) == mul(P, P)

# Full independence for arbitrary induced subgraphs on disjoint vertex sets.
for nu in (2, 3):
    for U in combinations(V, nu):
        for nv in range(2, 6-nu):
            for W in combinations(sorted(set(V)-set(U)), nv):
                uidx = [EIDX[e] for e in combinations(U, 2)]
                widx = [EIDX[e] for e in combinations(W, 2)]
                def profile(m, ids):
                    return sum((1 << k) for k, i in enumerate(ids) if m >> i & 1)
                for c in range(1 << len(uidx)):
                    for d in range(1 << len(widx)):
                        pu = measure(lambda m, c=c: profile(m, uidx) == c)
                        pw = measure(lambda m, d=d: profile(m, widx) == d)
                        joint = measure(lambda m, c=c, d=d: profile(m, uidx) == c and profile(m, widx) == d)
                        assert joint == mul(pu, pw)
                        count += 1

# The equality equations have full column rank, so no asymmetric law survives.
cols = list(support)
rows = []
for i, j in DISJOINT:
    rows.append([F(bool(m >> i & 1 and m >> j & 1)) for m in cols])
for i in range(len(EDGES)):
    rows.append([F(bool(m >> i & 1)) for m in cols])
rows.append([F(1)] * len(cols))
rank = 0
for col in range(len(cols)):
    piv = next((r for r in range(rank, len(rows)) if rows[r][col]), None)
    if piv is None: continue
    rows[rank], rows[piv] = rows[piv], rows[rank]
    c = rows[rank][col]
    rows[rank] = [x/c for x in rows[rank]]
    for r in range(rank+1, len(rows)):
        if rows[r][col]:
            c = rows[r][col]
            rows[r] = [a-c*b for a,b in zip(rows[r], rows[rank])]
    rank += 1
assert rank == 15
print('VERIFY_OK 1024 graph states, 15 extremal support states, exact field independence, rank 15')
