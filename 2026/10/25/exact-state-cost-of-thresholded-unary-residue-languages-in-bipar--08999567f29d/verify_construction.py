#!/usr/bin/env python3
"""Finite checks of the explicit witness construction; the proof is in RESULT.md."""
from math import lcm


def build(p, m):
    ell = lcm(p, 2)
    t = max(0, m - p + 1)
    e = m - t
    nstates = t + ell
    start = 0 if t else 0
    nxt = {}
    for i in range(t - 1):
        nxt[i] = i + 1
    if t:
        nxt[t - 1] = t
    for j in range(ell):
        nxt[t + j] = t + ((j + 1) % ell)
    accepting = {t + j for j in range(e, ell, p)}
    edges = set()
    for u, v in nxt.items():
        if u != v:
            edges.add(tuple(sorted((u, v))))
    colors = {i: i % 2 for i in range(t + ell)}
    assert all(colors[u] != colors[v] for u, v in edges)
    # The underlying simple graph is a path attached to one cycle; for ell=2,
    # the two directed arcs collapse to one undirected edge, leaving a tree.
    adj = {i: set() for i in range(nstates)}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    seen = set()
    stack = [start]
    while stack:
        u = stack.pop()
        if u in seen:
            continue
        seen.add(u)
        stack.extend(adj[u] - seen)
    assert len(seen) == nstates
    if ell == 2:
        assert len(edges) == nstates - 1
    else:
        assert len(edges) == nstates
    assert nstates == max(ell, m + ell - p + 1)
    return start, nxt, accepting, nstates


def check():
    cases = 0
    for p in range(1, 11):
        for m in range(0, 26):
            start, nxt, accepting, nstates = build(p, m)
            state = start
            bound = m + 5 * p + 5
            for length in range(bound + 1):
                actual = state in accepting
                expected = length >= m and (length - m) % p == 0
                assert actual == expected, (p, m, length, actual, expected)
                state = nxt[state]
            cases += 1
    print(f'PASS: {cases} parameter pairs checked; acceptance, state count, bipartition, and cactus structure verified.')
    print('Finite checks corroborate the construction only; the general lower bound is proved in RESULT.md.')

if __name__ == '__main__':
    check()
