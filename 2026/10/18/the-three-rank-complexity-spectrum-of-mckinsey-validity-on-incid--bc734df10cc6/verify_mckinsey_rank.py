#!/usr/bin/env python3
"""Finite exhaustive checks for McKinsey validity on incidence frames.

Run: python3 verify_mckinsey_rank.py. Uses only the Python standard library.
"""
from itertools import combinations

def incidence_frame(n, hyperedges):
    m = len(hyperedges)
    N = 1 + m + n
    successors = [set() for _ in range(N)]
    for i, edge in enumerate(hyperedges):
        successors[0].add(1 + i)
        successors[1 + i] = {1 + m + v for v in edge}
    for v in range(n):
        successors[1 + m + v].add(1 + m + v)
    return successors

def mckinsey_valid(successors):
    N = len(successors)
    for value_mask in range(1 << N):
        for w, neighbors in enumerate(successors):
            box_diamond = all(any((value_mask >> v) & 1 for v in successors[u])
                              for u in neighbors)
            diamond_box = any(all((value_mask >> v) & 1 for v in successors[u])
                              for u in neighbors)
            if box_diamond and not diamond_box:
                return False
    return True

def root_valid_by_leaf_enumeration(n, hyperedges):
    frame = incidence_frame(n, hyperedges)
    offset = 1 + len(hyperedges)
    for leaf_mask in range(1 << n):
        world_mask = leaf_mask << offset
        root_successors = frame[0]
        box_diamond = all(any((world_mask >> v) & 1 for v in frame[u]) for u in root_successors)
        diamond_box = any(all((world_mask >> v) & 1 for v in frame[u]) for u in root_successors)
        if box_diamond and not diamond_box:
            return False
    return True

def bicolorable(n, hyperedges):
    return any(all(any((value_mask >> v) & 1 for v in edge) and
                       any(not ((value_mask >> v) & 1) for v in edge)
                       for edge in hyperedges)
               for value_mask in range(1 << n))

def connected(n, edges, s, t):
    seen = {s}
    while True:
        grown = seen | {v for u, v in edges if u in seen} | {u for u, v in edges if v in seen}
        if grown == seen:
            return t in seen
        seen = grown

def subdivide_and_add_edge(n, edges, s, t):
    expanded_edges = [(u, n + i) for i, (u, v) in enumerate(edges)] + [
        (v, n + i) for i, (u, v) in enumerate(edges)] + [(s, t)]
    return n + len(edges), expanded_edges

def check():
    graphs = rank3 = rank1 = st_instances = 0
    for n in range(1, 6):
        singletons = [(i,) for i in range(n)]
        for mask in range(1 << n):
            hedges = [e for i, e in enumerate(singletons) if mask & (1 << i)]
            assert mckinsey_valid(incidence_frame(n, hedges)) == bool(hedges)
            rank1 += 1
        pairs = list(combinations(range(n), 2))
        for bitmask in range(1 << len(pairs)):
            edges = [pair for i, pair in enumerate(pairs) if bitmask & (1 << i)]
            expected = not bicolorable(n, edges)
            got = (mckinsey_valid(incidence_frame(n, edges)) if n <= 4
                   else root_valid_by_leaf_enumeration(n, edges))
            assert got == expected, (n, edges, got, expected)
            graphs += 1
            if n <= 4:
                for s in range(n):
                    for t in range(s + 1, n):
                        N, new_edges = subdivide_and_add_edge(n, edges, s, t)
                        assert (not bicolorable(N, new_edges)) == connected(n, edges, s, t)
                        st_instances += 1
    for n in range(3, 6):
        triples = list(combinations(range(n), 3))
        for bitmask in range(1 << len(triples)):
            hedges = [triple for i, triple in enumerate(triples) if bitmask & (1 << i)]
            got = (mckinsey_valid(incidence_frame(n, hedges)) if n <= 4
                   else root_valid_by_leaf_enumeration(n, hedges))
            assert got == (not bicolorable(n, hedges))
            rank3 += 1
    print(f'PASS: {rank1} rank-one, {graphs} graph, {rank3} rank-three hypergraph instances; '
          f'{st_instances} marked connectivity reductions')

if __name__ == '__main__':
    check()
