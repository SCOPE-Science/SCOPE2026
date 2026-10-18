#!/usr/bin/env python3
"""Integral acyclic-matching certificate for the bidirected five-vertex wheel."""
from collections import Counter, defaultdict, deque
from functools import lru_cache

# Vertex 0 is the hub; rim vertices 1,2,3,4 form a cycle.
EDGES = {tuple(sorted((0, v))) for v in range(1, 5)}
EDGES |= {tuple(sorted((v, 1 + v % 4))) for v in range(1, 5)}
ARCS = sorted((u, v) for a, b in EDGES for u, v in ((a, b), (b, a)))
assert len(ARCS) == 16

# Independently enumerate every subset of arcs, not just maximal faces.
def valid(mask):
    nxt = {}
    targets = set()
    for j, (u, v) in enumerate(ARCS):
        if mask & (1 << j):
            if u in nxt or v in targets:
                return False
            nxt[u] = v
            targets.add(v)
    for start in nxt:
        seen = set()
        u = start
        while u in nxt:
            if u in seen:
                return False
            seen.add(u)
            u = nxt[u]
    return True

FACES = {mask for mask in range(1 << 16) if valid(mask)}
assert len(FACES) == 261
assert dict(Counter(f.bit_count() - 1 for f in FACES)) == {-1: 1, 0: 16, 1: 76, 2: 120, 3: 48}

# Deterministic successive matching on one arc at a time; fix one vertex.
# Match only active faces, so one vertex is critical throughout.
FIXED = 5  # the directed arc (1,2)
active = FACES - {0, 1 << FIXED}
pairs = []
stages = []
while True:
    score = [sum(not (f & (1 << j)) and f | (1 << j) in active
                 for f in active) for j in range(16)]
    pivot = max(range(16), key=lambda j: score[j])
    if score[pivot] == 0:
        break
    low = sorted(f for f in active if not (f & (1 << pivot))
                 and f | (1 << pivot) in active)
    for f in low:
        active.remove(f)
        active.remove(f | (1 << pivot))
        pairs.append((f, f | (1 << pivot)))
    stages.append((pivot, len(low)))
CRITICAL = active | {1 << FIXED}
assert stages == [(5, 49), (8, 37), (12, 13), (15, 10),
                  (0, 2), (2, 2), (1, 1), (3, 1)]
assert len(pairs) == 115 and 2 * len(pairs) + len(CRITICAL) == len(FACES) - 1
assert Counter(f.bit_count() - 1 for f in CRITICAL) == {0: 1, 1: 1, 2: 20, 3: 8}

# Entire directed Hasse diagram: matched covering relations point up,
# every other covering relation points down. Check acyclicity by Kahn sort.
up = {low: high for low, high in pairs}
adj = defaultdict(list)
indeg = {f: 0 for f in FACES if f}
covers = 0
for high in indeg:
    for j in range(16):
        if not high & (1 << j):
            continue
        low = high ^ (1 << j)
        if not low:
            continue
        covers += 1
        source, target = (low, high) if up.get(low) == high else (high, low)
        adj[source].append(target)
        indeg[target] += 1
q = deque(f for f, degree in indeg.items() if degree == 0)
topo = 0
while q:
    f = q.popleft()
    topo += 1
    for other in adj[f]:
        indeg[other] -= 1
        if indeg[other] == 0:
            q.append(other)
assert covers == 704 and topo == len(indeg) == 260

# Standard signed integral algebraic Morse differential: a matched
# lower face is eliminated using the boundary of its matched upper face.
def boundary(f):
    bit_indices = [j for j in range(16) if f & (1 << j)]
    return [(f ^ (1 << j), (-1) ** k) for k, j in enumerate(bit_indices)]
upper = {high for _, high in pairs}
@lru_cache(None)
def projection(f):
    if f in upper:
        return {}
    if f not in up:
        return {f: 1}
    high = up[f]
    pivot_coeff = dict(boundary(high))[f]
    assert abs(pivot_coeff) == 1
    out = Counter()
    for face, sign in boundary(high):
        if face != f:
            for cell, coefficient in projection(face).items():
                out[cell] -= pivot_coeff * sign * coefficient
    return {cell: coefficient for cell, coefficient in out.items() if coefficient}

def morse_boundary(f):
    out = Counter()
    for face, sign in boundary(f):
        for cell, coefficient in projection(face).items():
            out[cell] += sign * coefficient
    return {cell: coefficient for cell, coefficient in out.items() if coefficient}

boundaries = {f: morse_boundary(f) for f in CRITICAL if f.bit_count() >= 2}
crit1 = [f for f in CRITICAL if f.bit_count() == 2]
assert len(crit1) == 1
b2 = {f: boundaries[f].get(crit1[0], 0)
      for f in CRITICAL if f.bit_count() == 3}
assert Counter(b2.values()) == {0: 14, 1: 3, -1: 3}
assert all(not boundaries[f] for f in CRITICAL if f.bit_count() == 4)
assert not boundaries[crit1[0]]
print('MORSE_OK: 261 faces; 704 covering relations; 115 matched pairs;')
print('critical cells 0:1, 1:1, 2:20, 3:8; signed d2 has 3 +1 and 3 -1; d3=0.')
