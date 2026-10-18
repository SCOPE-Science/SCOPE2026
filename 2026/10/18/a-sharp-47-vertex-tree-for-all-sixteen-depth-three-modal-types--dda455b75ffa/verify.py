"""Reproduce the sharp 47-vertex modal-type-complete tree certificate.

Usage: python3 verify.py (beside witness.json). Standard library only.
"""
import json
from collections import Counter
from pathlib import Path


def main():
    data = json.loads(Path(__file__).with_name("witness.json").read_text(encoding="utf-8"))
    given = data["types"]
    edges = data["edges"]
    n = len(given)
    assert n == 47
    assert len(edges) == n - 1
    assert set(map(type, given)) == {int}
    children = [[] for _ in range(n)]
    incoming = [0] * n
    for edge in edges:
        assert isinstance(edge, list) and len(edge) == 2
        p, u = edge
        assert type(p) is type(u) is int
        assert 0 <= p < n and 0 <= u < n and p != u
        children[p].append(u)
        incoming[u] += 1
    assert incoming[0] == 0
    assert incoming[1:] == [1] * (n - 1)
    assert all(len(set(v)) == len(v) for v in children)
    visited = set()
    stack = [0]
    while stack:
        v = stack.pop()
        assert v not in visited, "The edge set must be acyclic."
        visited.add(v)
        stack.extend(children[v])
    assert len(visited) == n

    # Topological order obtained from the graph, not assumed from its indexing.
    order = []
    stack = [(0, False)]
    while stack:
        v, processed = stack.pop()
        if processed:
            order.append(v)
        else:
            stack.append((v, True))
            stack.extend((u, False) for u in children[v])
    type_at_depth = [[0] * n for _ in range(4)]
    for v in order:
        for depth in range(1, 4):
            predecessors = {type_at_depth[depth - 1][u] for u in children[v]}
            type_at_depth[depth][v] = sum(1 << b for b in predecessors)
    assert type_at_depth[3] == given
    assert set(given) == set(range(16))
    assert type_at_depth[3][0] == 4

    # Independent 16-case algebraic check of the lower-bound potential.
    lam = [1, 2, 3, 4]
    beta = []
    for s in range(16):
        # Direct set-bit reduction: bit zero corresponds to depth-one code 0.
        # Every other bit corresponds to depth-one code 1.
        beta.append(int(bool(s & 1)) + 2 * int(bool(s & 14)))
    assert beta == [0, 1] + [2 if t % 2 == 0 else 3 for t in range(2, 16)]
    h = [1 + sum(lam[b] for b in range(4) if s & (1 << b)) - lam[beta[s]]
         for s in range(16)]
    assert h == [0, 0, 0, 0, 1, 1, 3, 3, 2, 2, 4, 4, 5, 5, 7, 7]
    assert sum(h) == 44
    assert all(x >= 0 for x in h)
    assert sum(h[s] for s in given) == 44
    assert beta[given[0]] == 2 and lam[beta[given[0]]] == 3
    for v in range(n):
        demand = sum(lam[b] for b in range(4) if given[v] & (1 << b))
        supply = sum(lam[type_at_depth[2][u]] for u in children[v])
        assert demand <= supply, (v, demand, supply)
    assert n >= sum(h[s] for s in given) + lam[beta[given[0]]]
    assert 44 + 3 == n == 47
    assert Counter(given) == Counter({0: 19, 1: 11, 2: 3, 3: 2, **{t: 1 for t in range(4, 16)}})
    print("PASS: 47 vertices, 46 child edges, 16 types, weighted lower bound 47")


if __name__ == "__main__":
    main()
