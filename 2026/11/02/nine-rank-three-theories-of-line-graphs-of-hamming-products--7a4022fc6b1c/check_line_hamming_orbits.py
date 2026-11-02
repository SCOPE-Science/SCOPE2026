#!/usr/bin/env python3
"""Finite verification of rank-three pair profiles of line graphs of Hamming products.
Each edge-coordinate direction is one orbit under symbol permutations.
Computational samples corroborate, but do not establish, the infinite classification.
"""
from itertools import product
from math import prod

PATTERNS = ((0, 0), (0, 1), (1, 0), (1, 1))


def classify(q):
    d = len(q)
    if d == 1:
        return 'one_2' if q[0] == 2 else ('one_3' if q[0] == 3 else ('one_4' if q[0] == 4 else ('one_5' if q[0] == 5 else 'one_6plus')))
    if d == 2:
        if max(q) == 2:
            return 'square'
        if min(q) == 2:
            return 'thin3' if max(q) == 3 else 'thin4plus'
    return 'stable'


def edges_incidence(q):
    vertices = list(product(*[range(z) for z in q]))
    ix = {v: i for i, v in enumerate(vertices)}
    edges, incident, axis = [], [set() for _ in vertices], []
    for a, u in enumerate(vertices):
        for j in range(len(q)):
            for val in range(u[j] + 1, q[j]):
                w = u[:j] + (val,) + u[j+1:]
                b = ix[w]
                e = len(edges)
                edges.append((a, b))
                incident[a].add(e)
                incident[b].add(e)
                axis.append(j)
    return edges, incident, axis


def rank3_profile(q):
    edges, inc, axes = edges_incidence(q)
    count = len(edges)
    anchor = {}
    # The factorwise symmetric group is transitive on edges within each axis.
    for x, j in enumerate(axes):
        if j in anchor:
            continue
        a, b = edges[x]
        nx = (inc[a] | inc[b]) - {x}
        signatures = set()
        for y, (c, d) in enumerate(edges):
            if x == y:
                continue
            ny = (inc[c] | inc[d]) - {y}
            flags = (
                count - 2 - len((nx | ny) - {x, y}) > 0,
                bool(ny - nx - {x}),
                bool(nx - ny - {y}),
                bool((nx & ny) - {x, y}),
            )
            signatures.add((int(y in nx), tuple(t for t, p in zip(PATTERNS, flags) if p)))
        anchor[j] = frozenset(signatures)
    return frozenset(anchor.values())


def main():
    representatives = {
        'one_2': (2,), 'one_3': (3,), 'one_4': (4,), 'one_5': (5,),
        'one_6plus': (6,), 'square': (2,2), 'thin3': (2,3),
        'thin4plus': (2,4), 'stable': (2,2,2),
    }
    expected = {key: rank3_profile(q) for key, q in representatives.items()}
    assert len(set(expected.values())) == 9, expected
    checks = 0
    for d, alphabet_max in ((1,9),(2,8),(3,5),(4,4),(5,3)):
        for q in product(range(2, alphabet_max+1), repeat=d):
            cls = classify(q)
            actual = rank3_profile(q)
            assert actual == expected[cls], (q, cls, actual, expected[cls])
            checks += 1
    print('VERIFY_OK finite axis-orbit pair profiles:', checks, 'tuples; exactly 9 spectra')
    for k in sorted(representatives):
        print(k, 'representative', representatives[k], 'line vertices', len(edges_incidence(representatives[k])[0]),
              'pointed types', len(expected[k]))

if __name__ == '__main__':
    main()
