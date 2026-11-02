#!/usr/bin/env python3
"""Exact finite search for maximal scan bi-threshold periods on trees.
Standard library only.  Python >= 3.10.  Run: python3 verify.py
All graphs are represented as simple undirected edges with vertices 0,...,n-1.
"""
import json
from collections import deque

EXPECTED_COUNTS = [1, 1, 1, 2, 3, 6, 11, 23, 47, 106, 235, 551]
EXPECTED_MAX = [1, 1, 1, 1, 2, 3, 6, 10, 14, 22, 42, 58]


def canonical_tree(n, edges):
    """Unrooted Aho-Hopcroft-Ullman parenthesis form, rooted at center(s)."""
    adj = [[] for _ in range(n)]
    for v, w in edges:
        adj[v].append(w); adj[w].append(v)
    remaining = n
    deg = list(map(len, adj))
    leaves = [i for i in range(n) if deg[i] <= 1]
    while remaining > 2:
        remaining -= len(leaves)
        new_leaves = []
        for v in leaves:
            for w in adj[v]:
                deg[w] -= 1
                if deg[w] == 1:
                    new_leaves.append(w)
        leaves = new_leaves
    centers = leaves
    def rooted(v, parent):
        codes = [rooted(w, v) for w in adj[v] if w != parent]
        codes.sort()
        return '(' + ''.join(codes) + ')'
    return min(rooted(c, -1) for c in centers)


def unlabeled_trees(n_max):
    """Leaf augmentation enumerates every tree isomorphism class once."""
    level = {canonical_tree(1, ()): ()}
    for n in range(1, n_max+1):
        assert len(level) == EXPECTED_COUNTS[n-1], (n, len(level))
        yield n, level
        if n == n_max: return
        nxt = {}
        for edges in level.values():
            for v in range(n):
                new_edges = edges + ((v, n),)
                code = canonical_tree(n+1, new_edges)
                if code not in nxt: nxt[code] = new_edges
        level = nxt


def advance(s, neighbors):
    """One sweep for closed-neighborhood k_up=1, k_down=3."""
    for v, mask in enumerate(neighbors):
        adjacent_ones = (s & mask).bit_count()
        if s & (1 << v):
            if adjacent_ones < 2: s &= ~(1 << v)
        elif adjacent_ones >= 1:
            s |= 1 << v
    return s


def analyze_tree(n, edges):
    masks = [0] * n
    for v, w in edges:
        masks[v] |= 1 << w
        masks[w] |= 1 << v
    size = 1 << n
    successor = [0] * size
    indegree = [0] * size
    for s in range(size):
        nxt = advance(s, masks)
        successor[s] = nxt
        indegree[nxt] += 1
    todo = deque(s for s, d in enumerate(indegree) if d == 0)
    while todo:
        x = todo.popleft()
        y = successor[x]
        indegree[y] -= 1
        if indegree[y] == 0: todo.append(y)
    max_period = 0
    best = None
    multiplicity = 0
    for s in range(size):
        if indegree[s]:
            t = s
            p = 0
            while indegree[t]:
                indegree[t] = 0
                p += 1
                t = successor[t]
            if p > max_period:
                max_period = p
                best = s
                multiplicity = 1
            elif p == max_period:
                multiplicity += 1
    assert best is not None
    # Independently traverse a cycle from its first state, without indegree logic.
    orbit = [best]
    t = advance(best, masks)
    while t != best:
        assert t not in orbit
        orbit.append(t)
        t = advance(t, masks)
    assert len(orbit) == max_period
    return max_period, best, multiplicity


def main():
    table = []
    for n, types in unlabeled_trees(12):
        top = 0
        witness = None
        graph_count = orbit_count = 0
        for edges in types.values():
            p, state, num = analyze_tree(n, edges)
            if p > top:
                top = p; witness = (edges, state)
                graph_count = 1; orbit_count = num
            elif p == top:
                graph_count += 1; orbit_count += num
        assert top == EXPECTED_MAX[n-1], (n, top)
        table.append({'n':n,'tree_isomorphism_classes':len(types),
                      'max_primitive_period':top,'extremal_tree_classes':graph_count,
                      'maximum_length_orbits_over_representatives':orbit_count,
                      'witness_edges':list(witness[0]),'witness_state':witness[1]})
        print('n=%d classes=%d max_period=%d maximizers=%d' % (
              n,len(types),top,graph_count), flush=True)
    with open('certificate.json', 'w', encoding='utf-8') as f:
        json.dump({'thresholds':{'up':1,'down':3,'closed_neighborhood':True},
                   'update_scan':'0,1,...,n-1', 'table':table},
                  f, ensure_ascii=False, indent=2)
        f.write('\n')
    print('VERIFY_OK: complete unlabeled-tree enumeration n=1..12')

if __name__ == '__main__': main()
