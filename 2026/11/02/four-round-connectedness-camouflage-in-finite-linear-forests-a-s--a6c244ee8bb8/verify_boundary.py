#!/usr/bin/env python3
"""Standalone bottom-up Hintikka type refinement for finite undirected linear forests.

No external dependencies. Computes equality/adjacency q-types for arbitrary parameter lists.
The construction is independent of the top-down C++ census implementation.
"""
from itertools import product

CODES = [dict() for _ in range(4)]

def type_id(level, key):
    table = CODES[level]
    if key not in table:
        table[key] = len(table) + 1
    return table[key]

def adj_of(lengths):
    n = sum(lengths)
    adj = [0] * n
    start = 0
    for length in lengths:
        for i in range(start, start + length - 1):
            adj[i] |= 1 << (i + 1)
            adj[i + 1] |= 1 << i
        start += length
    return adj

def atom(t, adj):
    vals = []
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            a, b = t[i], t[j]
            vals.append(0 if a == b else (1 if (adj[a] >> b) & 1 else 2))
    return tuple(vals)

def graph_type(lengths):
    adj = adj_of(lengths)
    n = len(adj)
    # bottom-up: for k chosen vertices, look up their one-step extensions
    # using the rank-(3-k) types at k+1 tuples.
    level = {}
    for t in product(range(n), repeat=3):
        child = {atom(t + (v,), adj) for v in range(n)}
        level[t] = type_id(3, (atom(t, adj), frozenset(child)))
    for k in (2,1):
        prev = level
        level = {}
        for t in product(range(n), repeat=k):
            children = frozenset(prev[t + (v,)] for v in range(n))
            level[t] = type_id(k, (atom(t, adj), children))
    return type_id(0, ((), frozenset(level[(v,)] for v in range(n))))

def main():
    cases = [(16,), (17,), (15,), (13,16), (14,14),
             (14,15), (14,16), (15,15), (15,16), (16,16), (12,18)]
    got = {}
    for case in cases:
        got[case] = graph_type(case)
        print(f'CASE {case} n={sum(case)} rank4_type={got[case]}', flush=True)
    yes = [(17,), (14,15), (14,16), (15,15), (15,16), (16,16)]
    no = [(15,), (13,16), (14,14), (12,18)]
    assert all(got[c] == got[(16,)] for c in yes)
    assert all(got[c] != got[(16,)] for c in no)
    print('INDEPENDENT_BOTTOM_UP_BOUNDARY_OK', flush=True)

if __name__ == '__main__':
    main()
