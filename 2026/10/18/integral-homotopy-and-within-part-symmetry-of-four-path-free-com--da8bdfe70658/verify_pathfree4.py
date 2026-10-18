#!/usr/bin/env python3
"""Finite verification for four-vertex-path-free complexes of complete multipartite graphs.

Requires only Python 3; computes faces from forbidden four-vertex paths,
checks a separate part-count classification, and reduces augmented boundary
matrices over GF(2). Infinite-parameter conclusions require the written proof.
"""
from itertools import combinations, combinations_with_replacement, permutations
from collections import defaultdict
from math import comb


def experiment(parts):
    sizes = list(parts)
    n = sum(sizes)
    colors = sum(([i] * s for i, s in enumerate(sizes)), [])
    edges = lambda u, v: colors[u] != colors[v]
    forbidden = set()
    for four in combinations(range(n), 4):
        for p in permutations(four):
            if edges(p[0], p[1]) and edges(p[1], p[2]) and edges(p[2], p[3]):
                forbidden.add(sum(1 << x for x in four))
                break
    F = defaultdict(list)
    for mask in range(1, 1 << n):
        direct = not any((mask & x) == x for x in forbidden)
        counter = [sum((mask >> k) & 1 for k, c in enumerate(colors) if c == i)
                   for i in range(len(sizes))]
        nonzero = [v for v in counter if v]
        classified = (len(nonzero) == 1 or
                      (len(nonzero) == 2 and min(nonzero) == 1) or
                      (len(nonzero) == 3 and max(nonzero) == 1))
        assert direct == classified, (parts, mask, counter)
        if direct:
            F[mask.bit_count() - 1].append(mask)
    rank = {}
    for dim in sorted(F):
        if dim == 0:
            continue
        previous = {m: k for k, m in enumerate(F[dim - 1])}
        pivot = {}
        for simplex in F[dim]:
            boundary = 0
            bits = simplex
            while bits:
                v = bits & -bits
                bits -= v
                boundary ^= 1 << previous[simplex ^ v]
            while boundary:
                p = boundary.bit_length() - 1
                if p not in pivot:
                    pivot[p] = boundary
                    break
                boundary ^= pivot[p]
        rank[dim] = len(pivot)
    betti = {d: len(s) - rank.get(d, 0) - rank.get(d + 1, 0)
             for d, s in F.items()}
    betti[0] -= 1
    m = len(sizes)
    E2 = sum(sizes[i] * sizes[j] for i in range(m) for j in range(i + 1, m))
    E3 = sum(sizes[i] * sizes[j] * sizes[k]
             for i in range(m) for j in range(i + 1, m)
             for k in range(j + 1, m))
    expected = (m - 1) * (1 - n) + E2 + E3
    assert all(b == (expected if d == 2 else 0) for d, b in betti.items()), (parts, betti, expected)
    assert len(F[0]) == n
    return len(forbidden), sum(len(z) for z in F.values()), expected


def main():
    total = 0
    max_faces = 0
    for m in (2, 3, 4, 5):
        for sizes in combinations_with_replacement((1, 2, 3, 4), m):
            if sum(sizes) > 10:
                continue
            obs = experiment(sizes)
            total += 1
            max_faces = max(max_faces, obs[1])
    print('cases_checked:', total)
    print('maximum_simplex_count:', max_faces)
    for sizes in ((2, 2), (3, 3), (2, 2, 2), (3, 3, 3), (2, 2, 2, 2), (1, 1, 1, 1, 1)):
        print('example:', sizes, experiment(sizes))
    print('path_enumeration_vs_part_criterion: PASS')
    print('mod_two_reduced_homology_vs_formula: PASS')


if __name__ == '__main__':
    main()
