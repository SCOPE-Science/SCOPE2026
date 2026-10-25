#!/usr/bin/env python3
"""Reproducible finite certificate for an icosahedral two-independence shelling.

Usage: python3 verify.py shelling.json
Standard-library only; exact integer and set arithmetic.
"""
import itertools
import json
import sys
from collections import Counter

N = 12

def make_graph():
    e = set()
    def put(x, y):
        assert x != y
        e.add(tuple(sorted((x, y))))
    for i in range(5):
        a = 1 + i
        b = 6 + i
        put(0, a)
        put(11, b)
        put(a, 1 + (i + 1) % 5)
        put(b, 6 + (i + 1) % 5)
        put(a, b)
        put(a, 6 + (i - 1) % 5)
    return e

def subfaces(m):
    s = m
    while True:
        yield s
        if s == 0:
            break
        s = (s - 1) & m

def connected_components_bounded(m, nbr):
    unseen = m
    while unseen:
        v = unseen & -unseen
        unseen ^= v
        frontier = v
        count = 1
        while frontier:
            reach = 0
            for i in range(N):
                if frontier & (1 << i):
                    reach |= nbr[i]
            frontier = reach & unseen
            unseen &= ~frontier
            count += frontier.bit_count()
            if count > 2:
                return False
    return True

def check(order):
    edges = make_graph()
    assert len(edges) == 30
    nbr = [0] * N
    for i, j in edges:
        nbr[i] |= 1 << j
        nbr[j] |= 1 << i
    assert [x.bit_count() for x in nbr] == [5] * N
    forbidden = set()
    for t in itertools.combinations(range(N), 3):
        pairs = sum(tuple(sorted(p)) in edges for p in itertools.combinations(t, 2))
        if pairs >= 2:
            forbidden.add(sum(1 << i for i in t))
    assert len(forbidden) == 80
    faces = set()
    for m in range(1 << N):
        valid_triples = all(m & t != t for t in forbidden)
        valid_components = connected_components_bounded(m, nbr)
        assert valid_triples == valid_components, (m, valid_triples, valid_components)
        if valid_triples:
            faces.add(m)
    assert len(faces) == 324
    counts = Counter(m.bit_count() for m in faces)
    assert [counts[i] for i in range(5)] == [1, 12, 66, 140, 105]
    facets = {m for m in faces if not any((m | (1 << i)) in faces for i in range(N) if not m & (1 << i))}
    assert len(facets) == 105
    assert all(m.bit_count() == 4 for m in facets)
    assert len(order) == 105 and set(order) == facets and len(set(order)) == 105
    seen = set()
    homology_facets = 0
    restrictions = []
    for k, f in enumerate(order):
        all_subsets = set(subfaces(f))
        assert all_subsets <= faces
        new = all_subsets - seen
        if k == 0:
            assert new == all_subsets
            restrictions.append(0)
        else:
            common = all_subsets & seen
            assert common and f not in common
            maximal_common = {x for x in common if not any(x != y and x & y == x for y in common)}
            assert all(x.bit_count() == 3 for x in maximal_common), (k, f, maximal_common)
            smallest_new = {x for x in new if not any(x != y and y & x == y for y in new)}
            assert len(smallest_new) == 1, (k, f, smallest_new)
            r = next(iter(smallest_new))
            assert r != 0
            assert new == {x for x in all_subsets if x & r == r}
            restrictions.append(r)
            if r == f:
                homology_facets += 1
        seen.update(all_subsets)
    assert seen == faces
    assert homology_facets == 20
    # h-polynomial of a pure 3-complex: sum f_{j-1} t^j(1-t)^(4-j).
    from math import comb
    h = [0] * 5
    for j in range(5):
        for u in range(5 - j):
            h[j + u] += counts[j] * comb(4 - j, u) * (-1)**u
    assert h == [1, 8, 36, 40, 20]
    assert sum((-1)**(k - 1) * counts[k] for k in range(5)) == -20
    return homology_facets

if __name__ == '__main__':
    f = sys.argv[1] if len(sys.argv) > 1 else 'shelling.json'
    with open(f, encoding='utf-8') as file:
        data = json.load(file)
    assert data['vertex_model'] == 'two poles, two staggered pentagons'
    result = check(data['facet_order_bitmasks'])
    print('ICO_2_SHELLING_VERIFY_OK', 'facets=105', 'spheres=' + str(result))
