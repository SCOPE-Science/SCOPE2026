#!/usr/bin/env python3
"""Exact finite certificates for the fourth-power cycle three-cut complex.

Run: python3 verify.py  (with cert_p4_n17.json ... cert_p4_n20.json beside it).
Uses Python standard library and exact integer arithmetic only.
"""
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def graph_neighbors(n, p):
    return [set((v + j) % n for j in range(1, p + 1)) |
            set((v - j) % n for j in range(1, p + 1)) for v in range(n)]


def is_disconnected(vertices, adjacency):
    available = set(vertices)
    root = next(iter(available))
    seen = {root}
    stack = [root]
    while stack:
        vertex = stack.pop()
        for neighbor in adjacency[vertex] & available:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    return seen != available


def disconnected_triples(n, p=4):
    adjacency = graph_neighbors(n, p)
    return [tuple(s) for s in combinations(range(n), 3)
            if is_disconnected(s, adjacency)]


def mod2_betti(n, triples):
    all_vertices = (1 << n) - 1
    face = bytearray(1 << n)
    face[0] = 1
    for triple in triples:
        t = sum(1 << v for v in triple)
        F = all_vertices ^ t
        s = F
        while s:
            face[s] = 1
            s = (s - 1) & F
    faces = defaultdict(list)
    for bitmask, ok in enumerate(face):
        if ok:
            faces[bitmask.bit_count() - 1].append(bitmask)
    boundary_rank = {}
    for degree in sorted(faces, reverse=True):
        if degree <= 0:
            continue
        rows = {s: i for i, s in enumerate(faces[degree - 1])}
        pivots = {}
        for simplex in faces[degree]:
            vector = 0
            z = simplex
            while z:
                bit = z & -z
                z ^= bit
                vector ^= 1 << rows[simplex ^ bit]
            while vector:
                pivot = vector.bit_length() - 1
                if pivot in pivots:
                    vector ^= pivots[pivot]
                else:
                    pivots[pivot] = vector
                    break
        boundary_rank[degree] = len(pivots)
    betti = {degree: len(faces[degree]) - boundary_rank.get(degree, 0)
             - boundary_rank.get(degree + 1, 0)
             for degree in faces if degree >= 0}
    betti[0] -= 1  # reduced homology, nonvoid complexes only
    return {k: v for k, v in betti.items() if v}, sum(len(faces[d]) for d in faces if d >= 0)


def verify_shelling(n, triples):
    file = ROOT / f'cert_p4_n{n}.json'
    record = json.loads(file.read_text(encoding='utf-8'))
    assert record['n'] == n and record['p'] == 4
    order = [tuple(row) for row in record['triples']]
    assert len(order) == len(triples) and set(order) == set(triples)
    assert len(order) == len(set(order))
    previous = []
    spanning = 0
    for i, t in enumerate(order):
        T = set(t)
        if i:
            # For complements of triples, ridge witnesses are precisely those
            # earlier triples W with |W\\T|=1; the unique element of W\\T
            # belongs to the ridge witness set R.
            R = set()
            for old in previous:
                delta = set(old) - T
                if len(delta) == 1:
                    R.update(delta)
            assert R, (n, i, 'no ridge witness')
            # Pure shelling criterion: for each earlier U there is a previous
            # ridge W such that F_i intersect U is contained in F_i intersect W.
            for old in previous:
                assert (set(old) - T) & R, (n, i, old)
            if len(R) == n - 3:
                spanning += 1
        previous.append(t)
    return len(order), spanning


def run():
    expected_betti = {
        11: {3: 1}, 12: {6: 6}, 13: {7: 40},
        14: {8: 15}, 15: {9: 1}, 16: {11: 3},
    }
    expected_facets = {17: 408, 18: 528, 19: 665, 20: 820}
    for n in range(3, 21):
        triples = disconnected_triples(n)
        if n <= 10:
            assert not triples, (n, len(triples))
        elif n <= 16:
            betti, face_count = mod2_betti(n, triples)
            assert betti == expected_betti[n], (n, betti)
            assert all(d < n - 4 for d in betti)
            print(f'NONSHELLABLE_OK n={n} facets={len(triples)} faces={face_count} '
                  f'reduced_mod2_betti={betti}')
        else:
            nfacets, spanning = verify_shelling(n, triples)
            assert nfacets == expected_facets[n]
            expected_spanning = (n*n-17*n+2)//2
            assert spanning == expected_spanning, (n, spanning)
            print(f'SHELLING_OK n={n} facets={nfacets} '
                  f'spanning={spanning} dimension={n-4}')
    print('VERIFY_OK all n=3..20 finite cases; n>=21 from cited theorem')


if __name__ == '__main__':
    run()
