#!/usr/bin/env python3
"""Exact rational verification of four-vertex voter-consensus edge insertions.

No external packages are needed. Each event is one attempt to update a vertex
or oriented edge, including attempts that leave every opinion unchanged.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from functools import lru_cache

RULES = ("VM", "LD", "IP")


def normal_edges(edges):
    return tuple(sorted(tuple(sorted(e)) for e in edges))


def connected(n, edges):
    if n < 1:
        return False
    nbr = [set() for _ in range(n)]
    for u, v in edges:
        nbr[u].add(v)
        nbr[v].add(u)
    seen = {0}
    todo = [0]
    while todo:
        for j in nbr[todo.pop()]:
            if j not in seen:
                seen.add(j)
                todo.append(j)
    return len(seen) == n


def solve_fraction(a, b):
    """Exact Gauss-Jordan elimination, not approximate linear algebra."""
    n = len(a)
    aug = [list(row) + [b[i]] for i, row in enumerate(a)]
    for k in range(n):
        p = next((i for i in range(k, n) if aug[i][k]), None)
        assert p is not None, "A connected finite voting graph must absorb"
        aug[k], aug[p] = aug[p], aug[k]
        pivot = aug[k][k]
        aug[k][k:] = [z / pivot for z in aug[k][k:]]
        for i in range(n):
            if i == k or aug[i][k] == 0:
                continue
            multiple = aug[i][k]
            aug[i][k:] = [u - multiple * v for u, v in zip(aug[i][k:], aug[k][k:])]
    return [row[-1] for row in aug]


@lru_cache(None)
def mean_updates(n, edges, rule):
    """Uniform iid fair initial spin configuration, including 2 absorbing ones."""
    assert connected(n, edges) and rule in RULES
    nbr = [[] for _ in range(n)]
    for u, v in edges:
        nbr[u].append(v)
        nbr[v].append(u)
    m = len(edges)
    transient = (1 << n) - 2
    matrix = [[F(int(i == j)) for j in range(transient)] for i in range(transient)]
    for state in range(1, (1 << n) - 1):
        row = state - 1
        for i in range(n):
            for j in nbr[i]:
                if rule == "VM":
                    receiver, donor, p = i, j, F(1, n * len(nbr[i]))
                elif rule == "IP":
                    receiver, donor, p = j, i, F(1, n * len(nbr[i]))
                else:
                    receiver, donor, p = i, j, F(1, 2 * m)
                bit = (state >> donor) & 1
                next_state = (state & ~(1 << receiver)) | (bit << receiver)
                if 0 < next_state < (1 << n) - 1:
                    matrix[row][next_state - 1] -= p
    elapsed = solve_fraction(matrix, [F(1)] * transient)
    return sum(elapsed, F()) / (1 << n)


def pair_orbit_key(n, edges, added_edge):
    # Canonicalize the pair (old graph, distinguished new edge) jointly.
    outcomes = []
    for p in permutations(range(n)):
        ee = normal_edges((p[u], p[v]) for u, v in edges)
        new = tuple(sorted((p[added_edge[0]], p[added_edge[1]])))
        outcomes.append((ee, new))
    return min(outcomes)


def enumerate_pair_orbits(n):
    universe = list(combinations(range(n), 2))
    orbits = {}
    for mask in range(1 << len(universe)):
        edges = normal_edges(e for k, e in enumerate(universe) if mask & (1 << k))
        if not connected(n, edges):
            continue
        for uv in universe:
            if uv in edges:
                continue
            key = pair_orbit_key(n, edges, uv)
            orbits[key] = (key[0], key[1])
    return list(orbits.values())


def verify():
    graphs = {
        "S4": (4, normal_edges(((0, 1), (0, 2), (0, 3)))),
        "P4": (4, normal_edges(((0, 1), (1, 2), (2, 3)))),
        "paw": (4, normal_edges(((0, 1), (0, 2), (0, 3), (1, 2)))),
        "C4": (4, normal_edges(((0, 1), (1, 2), (2, 3), (0, 3)))),
        "diamond": (4, normal_edges(((0, 1), (0, 2), (0, 3), (1, 2), (1, 3)))),
        "K4": (4, normal_edges(combinations(range(4), 2))),
    }
    # Expected values are independent hand-transcribed exact fractions.
    expected = {
        "S4": ((37, 8), (55, 8), (109, 8)),
        "P4": ((361, 56), (437, 56), (95, 8)),
        "paw": ((1117, 208), (927, 136), (695, 76)),
        "C4": ((47, 8), (47, 8), (47, 8)),
        "diamond": ((97, 18), (323, 56), (69, 11)),
        "K4": ((43, 8), (43, 8), (43, 8)),
    }
    for name, (n, ee) in graphs.items():
        actual = tuple(mean_updates(n, ee, rule) for rule in RULES)
        target = tuple(F(*ab) for ab in expected[name])
        assert actual == target, (name, actual, target)
        print(name, *map(str, actual))
    # Every orbit of connected-four-vertex edge insertions is represented.
    cases = (
        ("S4", "paw", (1, 2)),
        ("P4", "paw", (0, 2)),
        ("P4", "C4", (0, 3)),
        ("paw", "diamond", (1, 3)),
        ("C4", "diamond", (0, 2)),
        ("diamond", "K4", (2, 3)),
    )
    represented = set()
    counts = {rule: {"+": 0, "-": 0, "0": 0} for rule in RULES}
    for src, dst, added in cases:
        n, ee = graphs[src]
        h = normal_edges(ee + (added,))
        # Labels need not match the canonical naming of the destination.
        assert pair_orbit_key(n, ee, added) not in represented
        represented.add(pair_orbit_key(n, ee, added))
        outcome = []
        for rule in RULES:
            diff = mean_updates(n, h, rule) - mean_updates(n, ee, rule)
            s = "+" if diff > 0 else "-" if diff < 0 else "0"
            counts[rule][s] += 1
            outcome.append(str(diff))
        print(src + "->" + dst, *outcome)
    all_orbits = {pair_orbit_key(4, e, new) for e, new in enumerate_pair_orbits(4)}
    assert represented == all_orbits and len(all_orbits) == 6
    assert counts["VM"] == {"+": 2, "-": 4, "0": 0}
    assert counts["LD"] == {"+": 0, "-": 6, "0": 0}
    assert counts["IP"] == {"+": 1, "-": 5, "0": 0}
    p3 = normal_edges(((0, 1), (0, 2)))
    k3 = normal_edges(combinations(range(3), 2))
    assert len(enumerate_pair_orbits(3)) == 1
    assert (mean_updates(3, k3, "VM") - mean_updates(3, p3, "VM")) == 0
    assert (mean_updates(3, k3, "LD") - mean_updates(3, p3, "LD")) == F(-1, 2)
    assert (mean_updates(3, k3, "IP") - mean_updates(3, p3, "IP")) == F(-3, 2)
    assert len(enumerate_pair_orbits(2)) == 0
    print("n=2 orbits 0; n=3 orbits 1; n=4 orbits 6")
    s5 = normal_edges((0, i) for i in range(1, 5))
    w5 = normal_edges(s5 + ((1, 2),))
    b, a = mean_updates(5, s5, "LD"), mean_updates(5, w5, "LD")
    assert (b, a, a-b) == (F(613, 48), F(693195, 52592), F(32327, 78888))
    print("n=5 LD S5->S5+edge", str(b), str(a), str(a-b))
    print("PASS: exact rational equations, edge-orbit exhaustion, onset bounds")


if __name__ == "__main__":
    verify()
