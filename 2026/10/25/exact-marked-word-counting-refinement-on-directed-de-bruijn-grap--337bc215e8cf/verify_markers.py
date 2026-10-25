#!/usr/bin/env python3
"""Exact directed counting-refinement checks with arbitrary colored markers.

Each marked word receives a different color. Only graph adjacency is used.
"""
from collections import Counter, defaultdict
from itertools import product, combinations
from random import Random


def check(q, k, marked):
    vertices = tuple(product(range(q), repeat=k))
    positions = {v: j for j, v in enumerate(vertices)}
    outs = [tuple(positions[v[1:] + (a,)] for a in range(q)) for v in vertices]
    ins = [[] for _ in vertices]
    for i, successors in enumerate(outs):
        for j in successors:
            ins[j].append(i)
    labels = {v: j + 1 for j, v in enumerate(sorted(marked))}
    color = [labels.get(v, 0) for v in vertices]
    for _ in range(len(vertices) + 1):
        key = [
            (color[i], tuple(sorted(Counter(color[j] for j in outs[i]).items())),
             tuple(sorted(Counter(color[j] for j in ins[i]).items())))
            for i in range(len(vertices))
        ]
        p = {x: j for j, x in enumerate(sorted(set(key)))}
        new = [p[x] for x in key]
        if len(set(new)) == len(set(color)):
            color = new
            break
        color = new
    else:
        raise AssertionError('refinement did not stabilize')
    used = set(a for v in marked for a in v)
    coarse = [tuple(a if a in used else q for a in v) for v in vertices]
    groups = defaultdict(set)
    for c, w in zip(color, coarse):
        groups[c].add(w)
    assert all(len(g) == 1 for g in groups.values())
    t, u = len(used), q - len(used)
    assert len(groups) == (t + bool(u)) ** k
    return len(vertices)


def main():
    rng = Random(8675309)
    checked = seen = 0
    for q, k in [(1, 1), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2),
                 (3, 3), (4, 2), (4, 3), (4, 4), (5, 2), (5, 3)]:
        universe = tuple(product(range(q), repeat=k))
        if len(universe) <= 9:
            subsets = [tuple(v for i,v in enumerate(universe) if mask & (1<<i))
                       for mask in range(1<<len(universe))]
        else:
            subsets = [(), universe] + [(v,) for v in universe]
            for length in [2, 3, 4, 5, 7, 11]:
                for _ in range(16):
                    subsets.append(tuple(rng.sample(universe, min(len(universe), length))))
        for marked in subsets:
            seen += check(q, k, marked)
            checked += 1
        print(f'q={q}, length={k}: tested_marker_sets={len(subsets)} PASS')
    print(f'TOTAL marker_sets={checked}, examined_vertices={seen}')
    print('VERIFY_MARKERS_OK')


if __name__ == '__main__':
    main()
