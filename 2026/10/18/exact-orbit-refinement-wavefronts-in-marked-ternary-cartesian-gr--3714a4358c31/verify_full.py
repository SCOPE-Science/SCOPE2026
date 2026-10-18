"""Direct vertex-level synchronous counting-colour refinement on Cartesian powers of P3.

Usage: python verify_full.py
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb


def partition(colors):
    return {frozenset(ids) for ids in _groups(colors).values()}


def _groups(colors):
    out = defaultdict(set)
    for vertex, color in colors.items():
        out[color].add(vertex)
    return out


def refine(colors, neighbors):
    signatures = {}
    for vertex, old in colors.items():
        counts = Counter(colors[u] for u in neighbors[vertex])
        signatures[vertex] = (old, tuple(sorted(counts.items())))
    lookup = {s: i for i, s in enumerate(sorted(set(signatures.values())))}
    return {vertex: lookup[s] for vertex, s in signatures.items()}


def predicted(vertices, d, round_number):
    by_key = defaultdict(set)
    for v in vertices:
        b = v.count(1)
        c = v.count(2)
        distance = b + 2*c
        if round_number == 0:
            key = ("root",) if distance == 0 else ("other",)
        elif distance <= round_number:
            key = ("near", b, c)
        else:
            key = ("far", b)
        by_key[key].add(v)
    return {frozenset(s) for s in by_key.values()}


def run(d):
    vertices = list(product(range(3), repeat=d))
    neighbors = {}
    for v in vertices:
        nn = []
        for i, x in enumerate(v):
            for y in (x-1, x+1):
                if 0 <= y < 3:
                    changed = list(v)
                    changed[i] = y
                    nn.append(tuple(changed))
        neighbors[v] = nn
    root = (0,)*d
    colors = {v: int(v == root) for v in vertices}
    assert partition(colors) == predicted(vertices, d, 0)
    last = None
    for t in range(1, 2*d+3):
        updated = refine(colors, neighbors)
        actual = partition(updated)
        expected = predicted(vertices, d, t)
        assert actual == expected, (d,t,len(actual),len(expected))
        if partition(colors) == actual and last is None:
            last = t-1
        colors = updated
    assert last == 2*d-2, (d,last)
    assert len(partition(colors)) == comb(d+2,2)
    assert sum(len(p) for p in partition(colors)) == 3**d
    return last, len(partition(colors))


if __name__ == '__main__':
    for d in range(2,9):
        r, classes = run(d)
        print(f'd={d} vertices={3**d} stable_round={r} orbit_classes={classes} PASS')
    print('DIRECT CHECK PASSED')
