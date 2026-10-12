#!/usr/bin/env python3
"""Finite direct-enumeration checks of the eight-state super-domination forest enumerator.

Runs with standard Python 3 and no third-party dependencies.
All assertions compare exact integers. Finite tests do not prove the general theorem.
"""
from collections import defaultdict
from itertools import product
import random


def multiply(p, q):
    out = defaultdict(int)
    for i, a in p.items():
        for j, b in q.items():
            out[i + j] += a * b
    return dict(out)


def super_domination_polynomial(n, edges):
    """Return {degree: coefficient} of sum x^|D| for super-dominating D."""
    adjacency = [[] for _ in range(n)]
    for u, v in edges:
        assert 0 <= u < n and 0 <= v < n and u != v
        adjacency[u].append(v)
        adjacency[v].append(u)
    seen = set()

    def walk(v, parent):
        seen.add(v)
        children = []
        for u in adjacency[v]:
            if u == parent:
                continue
            assert u not in seen, 'input must be a forest'
            children.append(walk(u, v))
        # messages[t][(c,h,q)], where t is the parent's selected-color bit.
        messages = {0: {}, 1: {}}
        for t in (0, 1):
            for c in (0, 1):
                # w = capped number of white children, r = any pending white
                # child, s = any black child witnessing this white parent.
                accum = {(0, 0, 0): {0: 1}}
                for child in children:
                    nxt = {}
                    for (w, r, s), old_poly in accum.items():
                        for (cu, hu, qu), child_poly in child[c].items():
                            if c == 0 and hu:
                                continue
                            key = (min(2, w + (cu == 0)),
                                   int(r or hu),
                                   int(s or (cu == 1 and qu == 1)))
                            dest = nxt.setdefault(key, {})
                            for degree, count in multiply(old_poly, child_poly).items():
                                dest[degree] = dest.get(degree, 0) + count
                    accum = nxt
                for (w, r, s), poly in accum.items():
                    if c == 0:
                        if r:
                            continue
                        key = (0, int(s == 0), 0)
                    else:
                        if r and w + (1 - t) != 1:
                            continue
                        key = (1, 0, int(w == 0))
                    dest = messages[t].setdefault(key, {})
                    for degree, count in poly.items():
                        dest[degree + c] = dest.get(degree + c, 0) + count
        return messages

    total = {0: 1}
    for root in range(n):
        if root in seen:
            continue
        message = walk(root, -1)
        component = {}
        for (color, pending, only_white_parent), poly in message[1].items():
            if pending:
                continue  # The artificial black parent cannot witness the root.
            for degree, count in poly.items():
                component[degree] = component.get(degree, 0) + count
        total = multiply(total, component)
    return total


def independently_enumerate(n, edges):
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    polynomial = {}
    for selected in range(1 << n):
        white = ((1 << n) - 1) ^ selected
        if all(any((selected >> u) & 1 and (adj[u] & white) == (1 << v)
                   for u in range(n)) for v in range(n) if (white >> v) & 1):
            degree = selected.bit_count()
            polynomial[degree] = polynomial.get(degree, 0) + 1
    return polynomial


def prufer_edges(sequence):
    n = len(sequence) + 2
    degree = [1] * n
    for vertex in sequence:
        degree[vertex] += 1
    output = []
    for vertex in sequence:
        leaf = next(v for v in range(n) if degree[v] == 1)
        output.append((leaf, vertex))
        degree[leaf] -= 1
        degree[vertex] -= 1
    u, v = [vertex for vertex in range(n) if degree[vertex] == 1]
    output.append((u, v))
    return output


def maximum_matching_forest(n, edges):
    # Every forest has an optimal matching containing an edge at any leaf.
    adjacency = [set() for _ in range(n)]
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    result = 0
    while True:
        leaf = next((v for v in range(n) if len(adjacency[v]) == 1), None)
        if leaf is None:
            return result
        parent = next(iter(adjacency[leaf]))
        result += 1
        for v in (leaf, parent):
            for u in tuple(adjacency[v]):
                adjacency[u].discard(v)
            adjacency[v].clear()


def run_checks():
    graphs = 0
    candidates = 0
    for n in range(1, 7):
        sequences = [()] if n == 1 else product(range(n), repeat=n-2)
        for seq in sequences:
            edges = [] if n == 1 else prufer_edges(seq)
            found = super_domination_polynomial(n, edges)
            expected = independently_enumerate(n, edges)
            assert found == expected, (n, edges, found, expected)
            assert min(found) == n - maximum_matching_forest(n, edges)
            graphs += 1
            candidates += 1 << n
    print('ALL_LABELLED_TREES_N_LE_6', graphs)
    print('EXHAUSTIVE_CANDIDATES_ON_LABELLED_TREES', candidates)

    rng = random.Random(213843)
    forests = 0
    for n in range(1, 17):
        for _ in range(25):
            edges = [(v, rng.randrange(v)) for v in range(1, n)]
            edges = [e for e in edges if rng.randrange(5) > 0]
            found = super_domination_polynomial(n, edges)
            expected = independently_enumerate(n, edges)
            assert found == expected, (n, edges, found, expected)
            assert min(found) == n - maximum_matching_forest(n, edges)
            forests += 1
            candidates += 1 << n
    print('SEEDED_RANDOM_FORESTS_N_LE_16', forests)
    print('TOTAL_DIRECT_SUBSET_CANDIDATES', candidates)

    # Uniformly permuting vertex labels changes the intermediate root order.
    for n in range(2, 18):
        edges = [(v, v+1) for v in range(n-1)]
        expected = super_domination_polynomial(n, edges)
        for _ in range(10):
            permutation = list(range(n))
            rng.shuffle(permutation)
            permuted = [(permutation[u], permutation[v]) for u, v in edges]
            assert super_domination_polynomial(n, permuted) == expected
    print('PATH_ROOT_AND_RELABEL_INVARIANCE_CASES', 160)

    for n in range(1, 45):
        edges = [(v, v+1) for v in range(n-1)]
        found = super_domination_polynomial(n, edges)
        assert min(found) == (n + 1) // 2
        assert sum(found.values()) <= 2 ** n
    print('PATH_ORDER_BOUNDARY_CHECKS', 44)
    print('ALL_CHECKS_PASS')


if __name__ == '__main__':
    run_checks()
