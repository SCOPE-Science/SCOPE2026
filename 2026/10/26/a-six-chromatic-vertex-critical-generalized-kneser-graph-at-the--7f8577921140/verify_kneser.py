#!/usr/bin/env python3
"""Reproduce the 5-colour exclusion and six orbit-witness certificate.

Usage: python3 verify_kneser.py; needs deletion_orbit_witnesses.txt beside it.
Standard-library only. No precomputed graph data is trusted.
"""
from itertools import combinations
from pathlib import Path

TRIPLES = tuple(t for t in combinations(range(10), 3)
                if all(not (i in t and ((i + 1) % 9) in t) for i in range(9)))
N = len(TRIPLES)
assert N == 57
TRIPLE_INDEX = {t:i for i,t in enumerate(TRIPLES)}
ADJ = [[] for _ in range(N)]
for i in range(N):
    for j in range(i):
        if not set(TRIPLES[i]).intersection(TRIPLES[j]):
            ADJ[i].append(j)
            ADJ[j].append(i)
assert sum(map(len, ADJ)) == 996
cycle_only = [u for u,t in enumerate(TRIPLES) if 9 not in t]
with_isolate = [u for u,t in enumerate(TRIPLES) if 9 in t]
assert len(cycle_only) == 30 and len(with_isolate) == 27
assert sum(u in ADJ[v] for i,u in enumerate(cycle_only) for v in cycle_only[i+1:]) == 138
assert sum(u in ADJ[v] for u in cycle_only for v in with_isolate) == 360
assert not any(u in ADJ[v] for i,u in enumerate(with_isolate) for v in with_isolate[i+1:])

# Six-colouring without search: a stable triple receives the first of labels
# 0..4 that it contains; if none, color 5. The latter triples live inside a
# five-element set and cannot be mutually disjoint.
six_coloring = [min((x for x in t if x <= 4), default=5) for t in TRIPLES]
assert all(six_coloring[u] != six_coloring[v]
           for u in range(N) for v in ADJ[u])

# Compute all dihedral automorphisms of the nine-cycle (the isolate is fixed).
PERMS = []
for direction in (-1, 1):
    for shift in range(9):
        perm = tuple(TRIPLE_INDEX[tuple(sorted(
            ((direction*x + shift)%9 if x<9 else 9) for x in t))]
            for t in TRIPLES)
        assert len(set(perm)) == N
        assert all((v in ADJ[u]) == (perm[v] in ADJ[perm[u]])
                   for u in range(N) for v in range(N) if u != v)
        PERMS.append(perm)
remaining = set(range(N))
reps = []
sizes = []
while remaining:
    rep = min(remaining)
    orb = {perm[rep] for perm in PERMS}
    assert orb.issubset(remaining)
    reps.append(rep)
    sizes.append(len(orb))
    remaining -= orb
assert reps == [0,1,4,6,8,11]
assert sizes == [9,18,9,3,9,9]

# One 5-colouring of H - vertex for each vertex orbit. Every other deletion
# is carried to one of these six by an automorphism of C9 plus the isolate.
witness_lines = Path(__file__).with_name('deletion_orbit_witnesses.txt').read_text().splitlines()
assert len(witness_lines) == len(reps)
covered = set()
for rep, line in zip(reps, witness_lines):
    idx_text, word = line.split(' ')
    assert int(idx_text) == rep and len(word) == N
    assert word[rep] == '-' and set(word) == set('01234-')
    assert all(word[u] != word[v] for u in range(N) for v in ADJ[u]
               if u!=rep and v!=rep)
    for perm in PERMS:
        transported = ['!'] * N
        for u in range(N):
            transported[perm[u]] = word[u]
        absent = perm[rep]
        assert transported[absent] == '-'
        assert all(transported[u] != transported[v]
                   for u in range(N) for v in ADJ[u]
                   if u!=absent and v!=absent)
        covered.add(absent)
assert covered == set(range(N))

# Direct exact search for 5-colourings, independently regenerating the graph.
# Reordering the color names of any proper partial colouring makes used names
# exactly 0..used-1. Consequently only ONE fresh name must be tried.
COLORS = [-1]*N
NB_COLOR_MASK = [0]*N
UNCOLORED_DEG = [len(a) for a in ADJ]
nodes = 0

def has_five_coloring(depth, used):
    global nodes
    nodes += 1
    if depth == N:
        return True
    pivot = -1
    best_key = (-1,-1)
    for u in range(N):
        if COLORS[u] != -1:
            continue
        key = (NB_COLOR_MASK[u].bit_count(), UNCOLORED_DEG[u])
        if key > best_key:
            pivot, best_key = u, key
    forbidden = NB_COLOR_MASK[pivot]
    for c in range(min(5, used+1)):
        if forbidden & (1<<c):
            continue
        COLORS[pivot] = c
        changed = []
        for v in ADJ[pivot]:
            if COLORS[v] == -1:
                changed.append((v, NB_COLOR_MASK[v]))
                NB_COLOR_MASK[v] |= 1<<c
                UNCOLORED_DEG[v] -= 1
        ok = has_five_coloring(depth+1, max(used,c+1))
        for v, old in changed:
            NB_COLOR_MASK[v] = old
            UNCOLORED_DEG[v] += 1
        COLORS[pivot] = -1
        if ok:
            return True
    return False

assert not has_five_coloring(0, 0)
assert nodes == 122153, nodes
assert COLORS == [-1]*N
assert NB_COLOR_MASK == [0]*N
assert UNCOLORED_DEG == [len(a) for a in ADJ]
print('VERIFY_OK vertices=57 edges=498 χ=6 6-critical orbit_representatives=6 search_nodes=122153')
