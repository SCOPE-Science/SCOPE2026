#!/usr/bin/env python3
"""Exhaustive finite certificate for the house-graph strong matching complex.

Uses the definition of a strong graph matching induced by each total vertex order.
Run with Python 3, without external packages.
"""
from itertools import permutations, combinations
from collections import defaultdict, Counter

EDGES = {(0, 1), (1, 2), (2, 3), (0, 3), (1, 4), (2, 4)}
EDGES = {frozenset(e) for e in EDGES}
PAIR = sorted((v, w) for v in range(5) for w in range(5) if frozenset((v, w)) in EDGES)
INDEX = {p: k for k, p in enumerate(PAIR)}

# Each row is a free edge (two incidence vertices), followed by its
# unique triangular coface (three incidence vertices). Incidence (v,w)
# denotes pairing vertex v with edge {v,w}.
COLLAPSES = [
 ([(3, 0), (4, 2)], [(2, 3), (3, 0), (4, 2)]),
 ([(1, 0), (3, 0)], [(1, 0), (3, 0), (4, 1)]),
 ([(3, 2), (4, 2)], [(0, 3), (3, 2), (4, 2)]),
 ([(2, 4), (3, 2)], [(0, 3), (2, 4), (3, 2)]),
 ([(2, 3), (4, 2)], [(0, 3), (2, 3), (4, 2)]),
 ([(1, 0), (4, 1)], [(0, 3), (1, 0), (4, 1)]),
 ([(3, 0), (4, 1)], [(0, 1), (3, 0), (4, 1)]),
 ([(1, 4), (3, 0)], [(0, 1), (1, 4), (3, 0)]),
]

def subs(f):
    seq = sorted(f)
    for k in range(len(seq) + 1):
        for comb in combinations(seq, k):
            yield frozenset(comb)

def full_complex():
    faces = {frozenset()}
    matchings = set()
    for order in permutations(range(5)):
        seen = set()
        face = set()
        for v in order:
            prior = [w for w in seen if frozenset((v, w)) in EDGES]
            if len(prior) == 1:
                face.add(INDEX[(v, prior[0])])
            seen.add(v)
        f = frozenset(face)
        matchings.add(f)
        faces.update(subs(f))
    return faces, matchings

def signature(seq):
    return (-1) ** sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq)))

def main():
    faces, matchings = full_complex()
    assert len(matchings) == 37, len(matchings)
    assert sum(not any(f < g for g in matchings) for f in matchings) == 18
    assert len(faces) == 49
    assert Counter(len(f) for f in faces if f) == {1: 12, 2: 28, 3: 8}
    assert all(frozenset(INDEX[x] for x in tri) in matchings for _, tri in COLLAPSES)
    remaining = set(faces)
    remaining.remove(frozenset())
    for free_pairs, tri_pairs in COLLAPSES:
        lo = frozenset(INDEX[p] for p in free_pairs)
        hi = frozenset(INDEX[p] for p in tri_pairs)
        assert lo in remaining and hi in remaining and lo < hi
        assert {f for f in remaining if lo < f} == {hi}, (free_pairs, tri_pairs)
        remaining.remove(lo)
        remaining.remove(hi)
    assert Counter(len(f) for f in remaining) == {1: 12, 2: 20}
    adjacency = defaultdict(set)
    for f in remaining:
        if len(f) == 2:
            a, b = tuple(f)
            adjacency[a].add(b)
            adjacency[b].add(a)
    vertices = {next(iter(f)) for f in remaining if len(f) == 1}
    visited, stack = set(), [next(iter(vertices))]
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        stack.extend(adjacency[v] - visited)
    assert visited == vertices
    assert 20 - 12 + 1 == 9

    # Reflection across the roof axis: (0 3)(1 2), fixing roof 4.
    refl = {0: 3, 3: 0, 1: 2, 2: 1, 4: 4}
    assert {frozenset((refl[a], refl[b])) for a, b in EDGES} == EDGES
    induced = {i: INDEX[(refl[v], refl[w])] for i, (v, w) in enumerate(PAIR)}
    assert {frozenset(induced[v] for v in f) for f in faces} == faces
    chain_traces = {}
    for k in (1, 2, 3):
        tr = 0
        for f in faces:
            if len(f) != k:
                continue
            f_seq = sorted(f)
            image = [induced[i] for i in f_seq]
            if set(image) == set(f_seq):
                tr += signature(image)
        chain_traces[k - 1] = tr
    assert chain_traces == {0: 0, 1: 0, 2: 0}
    lefschetz = sum((-1)**q * chain_traces[q] for q in chain_traces)
    assert lefschetz == 0
    trace_h1 = 1 - lefschetz
    assert trace_h1 == 1
    # Involution eigendimensions from rank and trace.
    assert ((9 + trace_h1)//2, (9 - trace_h1)//2) == (5, 4)
    print('VERIFY_OK orders=120 faces=48 vertices=12 edges=28 triangles=8 '
          'free_collapses=8 graph_edges=20 connected=1 beta1=9 '
          'reflection_chain_traces=(0,0,0) reflection_H1_trace=1 '
          'reflection_eigenspaces=(5,4)')

if __name__ == '__main__':
    main()
