#!/usr/bin/env python3
"""Exact certificate checker for the four-prime Pythagorean-pair invariant.

Usage: python3 verify.py [CERTIFICATE.json]
Only the Python standard library is needed.
"""
import json
import math
import sys
from collections import Counter
from pathlib import Path


def validate(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    assert data["schema_version"] == 1
    assert data["primes"] == [2, 3, 5, 7]
    assert data["exponent_bound_exclusive"] == 4
    primes = data["primes"]
    V = []
    for i in range(256):
        a, r = divmod(i, 64)
        b, r = divmod(r, 16)
        c, d = divmod(r, 4)
        assert 0 <= min(a, b, c, d) <= max(a, b, c, d) <= 3
        V.append(2**a * 3**b * 5**c * 7**d)
    assert len(set(V)) == 256
    # This is the complete, exact test of the source's right-triangle condition.
    edges = set()
    adjacency = [set() for _ in range(256)]
    for i in range(256):
        for j in range(i + 1, 256):
            z = V[i] * V[i] + V[j] * V[j]
            if math.isqrt(z)**2 == z:
                edges.add((i, j))
                adjacency[i].add(j)
                adjacency[j].add(i)
    assert len(edges) == data["edge_count"] == 408
    # Lower bound certificate: 144 indices with no forbidden edge.
    independent = data["independent_indices"]
    assert len(independent) == 144 and len(set(independent)) == 144
    assert all(type(i) is int and 0 <= i < 256 for i in independent)
    I = set(independent)
    assert all(not (i in I and j in I) for i, j in edges)
    # Upper bound certificate: 112 disjoint forbidden pairs. One must be
    # omitted from each, bounding every independent set by 256 - 112.
    pair_rows = data["disjoint_edges"]
    assert len(pair_rows) == 112
    used = set()
    for p in pair_rows:
        assert type(p) is list and len(p) == 2
        i, j = p
        assert type(i) is int and type(j) is int and 0 <= i < j < 256
        assert (i, j) in edges
        assert i not in used and j not in used
        used.update((i, j))
    assert len(used) == 224
    # Additional independent structural check, not needed for extremality.
    visited = set()
    components = Counter()
    for start in range(256):
        if start in visited:
            continue
        seen = {start}
        todo = [start]
        while todo:
            v = todo.pop()
            for u in adjacency[v]:
                if u not in seen:
                    seen.add(u)
                    todo.append(u)
        assert not (seen & visited)
        visited.update(seen)
        components[len(seen)] += 1
    assert len(visited) == 256
    expected = {int(k): v for k, v in data["component_size_multiplicities"].items()}
    assert components == expected == {1: 10, 2: 2, 242: 1}
    assert 256 - len(pair_rows) == len(I) == 144
    print("CERTIFICATE_OK vertices=256 edges=408 matching_edges=112 independent_vertices=144 components=13")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) == 2 else str(Path(__file__).with_name("CERTIFICATE.json"))
    validate(path)
