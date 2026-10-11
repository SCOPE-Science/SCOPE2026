#!/usr/bin/env python3
"""Exact finite certificate for Fourier spectra of radius-one Lee balls.

Run with Python 3.10+: python3 checker.py
Uses only the Python standard library; all arithmetic is integral modulo p.
"""
from collections import Counter
from itertools import permutations, product
from math import factorial


def vector_set(p):
    d = (p - 1) // 2
    return {
        tuple(s * a % p for a, s in zip(perm, signs))
        for perm in permutations(range(1, d + 1))
        for signs in product((-1, 1), repeat=d)
    }


def difference(a, b, p):
    return tuple((x - y) % p for x, y in zip(a, b))


def maximal_clique_sizes(graph):
    """Independent exhaustive Bron--Kerbosch pivot recursion."""
    sizes = Counter()

    def bron_kerbosch(R, P, X):
        if not P and not X:
            sizes[len(R)] += 1
            return
        # Selecting a pivot affects speed but not completeness.
        pivot = max(P | X, key=lambda u: len(P & graph[u])) if P or X else None
        candidates = (P - graph[pivot]) if pivot is not None else P.copy()
        for v in tuple(sorted(candidates)):
            bron_kerbosch(R | {v}, P & graph[v], X & graph[v])
            P.remove(v)
            X.add(v)

    bron_kerbosch(set(), set(graph), set())
    return dict(sorted(sizes.items()))


def certify(p, predicted_neighbours, expected_profile):
    d = (p - 1) // 2
    u = tuple(range(1, d + 1))
    D = vector_set(p)
    assert len(D) == (2 ** d) * factorial(d)
    assert (0,) * d not in D
    assert all(tuple(k * x % p for x in v) in D for v in D for k in (2, p - 1))
    V = sorted(v for v in D if difference(v, u, p) in D)
    assert len(V) == predicted_neighbours
    radial = {tuple(k * x % p for x in u) for k in range(2, p)}
    assert radial.issubset(V) and len(radial) == p - 2
    graph = {i: set() for i in range(len(V))}
    edge_count = 0
    for i, a in enumerate(V):
        for j in range(i + 1, len(V)):
            if difference(a, V[j], p) in D:
                graph[i].add(j)
                graph[j].add(i)
                edge_count += 1
    profiles = maximal_clique_sizes(graph)
    assert profiles == expected_profile, (p, profiles)
    assert profiles.get(p - 2) == 1, (p, profiles)
    # A full affine line always supplies a clique.  Unique maximum
    # clique then proves that no other normalized spectrum is possible.
    indices = {i for i, v in enumerate(V) if v in radial}
    assert len(indices) == p - 2
    assert all((j in graph[i]) for i in indices for j in indices if i != j)
    dirs = len(D) // (p - 1)
    assert len(D) % (p - 1) == 0
    total_spectra = dirs * (p ** (d - 1))
    return len(D), len(V), edge_count, profiles, dirs, total_spectra


def main():
    cases = {
        5: (3, {3: 1}),
        7: (5, {5: 1}),
        11: (69, {2: 120, 9: 1}),
        13: (319, {1: 24, 2: 324, 3: 225, 5: 42, 11: 1}),
    }
    for p, (vnum, profile) in cases.items():
        D, V, edges, got, directions, spectra = certify(p, vnum, profile)
        print(f'p={p} |D|={D} |V|={V} edges={edges} maximal_cliques={got} '
              f'directions={directions} affine_spectra={spectra}')
    # The smaller local-difference rigidity fails in dimension six:
    # these vectors span a noncollinear triangle in the Fourier zero set.
    p = 13
    D = vector_set(p)
    a = (1, 2, 3, 4, 5, 6)
    b = (2, 4, 7, 10, 8, 1)
    c = (5, 10, 6, 2, 4, 12)
    assert all(x in D for x in (a, b, c))
    assert all(difference(x, y, p) in D for x, y in ((a, b), (b, c), (c, a)))
    assert not any(b == tuple(k * t % p for t in a) for k in range(p))
    print('CHECK_PASS')


if __name__ == '__main__':
    main()
