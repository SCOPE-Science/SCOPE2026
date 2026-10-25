#!/usr/bin/env python3
"""Finite certificate for the five-vertex bidirected-cycle multipath complex.

Run with Python 3 standard library: python verify_bp4.py
"""
from collections import Counter, deque
from itertools import combinations
from pathlib import Path
import json

N = 5
ARCS = [(j, (j+1) % N) for j in range(N)] + [((j+1) % N, j) for j in range(N)]
CERT = json.loads(Path(__file__).with_name('matching_certificate.json').read_text('utf-8'))


def admissible_a(mask):
    """Indegree, outdegree and forbidden directed-cycle test."""
    ins, outs = set(), set()
    for j, (u, v) in enumerate(ARCS):
        if mask & (1 << j):
            if u in outs or v in ins:
                return False
            outs.add(u)
            ins.add(v)
    for j in range(N):
        if mask & (1 << j) and mask & (1 << (N+j)):
            return False
    return mask.bit_count() != N


def admissible_b(mask):
    """Independent alternate test: every nonisolated weak component is a directed simple path."""
    edges = [ARCS[j] for j in range(2*N) if mask & (1 << j)]
    adjacency = {v: set() for v in range(N)}
    indeg, outdeg = [0]*N, [0]*N
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
        outdeg[u] += 1
        indeg[v] += 1
    seen = set()
    for start in range(N):
        if start in seen:
            continue
        todo = [start]
        component = set()
        while todo:
            v = todo.pop()
            if v in component:
                continue
            component.add(v)
            todo.extend(adjacency[v] - component)
        seen.update(component)
        m = sum(u in component and v in component for u, v in edges)
        if m and (m != len(component)-1 or any(indeg[v]>1 or outdeg[v]>1 for v in component)):
            return False
    return True

FACE_SET_A = {x for x in range(1, 1 << (2*N)) if admissible_a(x)}
FACE_SET_B = {x for x in range(1, 1 << (2*N)) if admissible_b(x)}
assert FACE_SET_A == FACE_SET_B, 'Independent multipath predicates disagree'
faces = sorted(FACE_SET_A, key=lambda m: (m.bit_count(), m))
assert Counter(m.bit_count()-1 for m in faces) == {0:10, 1:30, 2:30, 3:10}

# Explicit Morse matching, independently generated and cross-checked against a fixed certificate.
order = CERT['pivot_order']
assert sorted(order) == list(range(2*N))
remaining = set(faces)
pairs = []
for pivot in order:
    toggle = 1 << pivot
    for x in faces:
        upper = x | toggle
        if not x & toggle and x in remaining and upper in remaining:
            remaining.remove(x)
            remaining.remove(upper)
            pairs.append([x, upper])
assert pairs == CERT['matched_pairs'], 'Matching does not reproduce recorded 38 pairs'
assert sorted(remaining) == CERT['critical_masks'], 'Unexpected critical cells'
assert len(pairs) == 38 and len(remaining) == 4
assert Counter(m.bit_count()-1 for m in remaining) == {0:1, 2:1, 3:2}

# Hasse edges are directed downward, except matched edges are reversed.
matched = {(a, b) for a, b in pairs}
adjacency = {m: [] for m in faces}
for higher in faces:
    for bit in range(2*N):
        if not (higher & (1 << bit)):
            continue
        lower = higher ^ (1 << bit)
        if lower not in FACE_SET_A:
            continue
        if (lower, higher) in matched:
            adjacency[lower].append(higher)
        else:
            adjacency[higher].append(lower)
assert sum(map(len, adjacency.values())) == 190
indegree = {m:0 for m in faces}
for m in faces:
    for next_m in adjacency[m]:
        indegree[next_m] += 1
queue = deque(m for m in faces if indegree[m] == 0)
visited = []
while queue:
    current = queue.popleft()
    visited.append(current)
    for nxt in adjacency[current]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)
assert len(visited) == len(faces), 'Gradient directed graph contains a closed gradient path'

# Entire degree-three chain group consists of two disjoint oriented simplex boundaries.
forward = set(range(N))
backward = set(range(N, 2*N))
tetra = {m for m in faces if m.bit_count() == 4}
assert tetra == {sum(1 << bit for bit in forward if bit != omitted) for omitted in forward} | {sum(1 << bit for bit in backward if bit != omitted) for omitted in backward}

def boundary(simplex):
    vertices = [j for j in range(2*N) if simplex & (1 << j)]
    return [(simplex ^ (1 << bit), (-1)**i) for i, bit in enumerate(vertices)]

# Exact integral fundamental cycles of the two oriented tetrahedral boundaries.
for side in [sorted(forward), sorted(backward)]:
    chain = [(sum(1 << bit for bit in side if bit != omit), (-1)**i) for i, omit in enumerate(side)]
    bd = Counter()
    for simplex, coefficient in chain:
        for face, sign in boundary(simplex):
            bd[face] += coefficient*sign
    assert all(x == 0 for x in bd.values()), 'Top boundary is not a cycle'

print('VERIFY_OK')
print('nonempty_face_vector_by_dimension=10,30,30,10')
print('independent_complete_face_checks=1023')
print('matching_pairs=38')
print('critical_cells_dimension_0_2_3=1,1,2')
print('critical_masks=' + ','.join(map(str, sorted(remaining))))
print('hasse_arrows=190')
print('gradient_dag_nodes=80')
print('independent_integral_top_cycles=2')
