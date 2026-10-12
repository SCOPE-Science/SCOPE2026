#!/usr/bin/env python3
"""Exact regression checks for matched-edge graph associahedra.

Uses only the Python standard library. Does not replace the all-n fan proof.
"""
from functools import lru_cache
from itertools import combinations, product
from math import comb


def graph_edges(n, matching_size):
    return frozenset((a, b) for a in range(n) for b in range(a + 1, n)
                     if not (a % 2 == 0 and b == a + 1 and a // 2 < matching_size))


def connected_components(vertices, edges):
    remaining = set(vertices)
    out = []
    while remaining:
        start = min(remaining)
        remaining.remove(start)
        part = {start}
        frontier = [start]
        while frontier:
            v = frontier.pop()
            neighbors = {w for w in remaining if tuple(sorted((v, w))) in edges}
            part.update(neighbors)
            remaining.difference_update(neighbors)
            frontier.extend(sorted(neighbors))
        out.append(frozenset(part))
    return tuple(out)


def is_connected(vertices, edges):
    return len(connected_components(vertices, edges)) == 1


def disconnected_proper_sets(n, edges):
    all_vertices = tuple(range(n))
    out = set()
    for size in range(2, n):
        for sub in combinations(all_vertices, size):
            if not is_connected(sub, edges):
                out.add(frozenset(sub))
    return out


def complement_is_matching(n, edges):
    missing = [(a, b) for a in range(n) for b in range(a + 1, n) if (a, b) not in edges]
    endpoints = [v for edge in missing for v in edge]
    return len(endpoints) == len(set(endpoints))


def maximal_tubings(n, edges):
    @lru_cache(None)
    def rec(vertices):
        if len(vertices) == 1:
            return (frozenset(),)
        possibilities = []
        for removed in sorted(vertices):
            components = connected_components(vertices.difference({removed}), edges)
            for pieces in product(*(rec(c) for c in components)):
                joined = frozenset(set(components).union(*(set(piece) for piece in pieces)))
                assert len(joined) == len(vertices) - 1
                possibilities.append(joined)
        return tuple(possibilities)
    return rec(frozenset(range(n)))


def h_coefficients(n, edges):
    dimension = n - 1
    face_sets = [set() for _ in range(dimension + 1)]
    for maximal in maximal_tubings(n, edges):
        ordered = sorted(maximal, key=lambda s: (len(s), tuple(sorted(s))))
        for j in range(dimension + 1):
            face_sets[j].update(frozenset(sub) for sub in combinations(ordered, j))
    out = [0] * (dimension + 1)
    for j, face_set in enumerate(face_sets):
        for k in range(j, dimension + 1):
            out[k] += len(face_set) * (-1)**(k - j) * comb(dimension - j, k - j)
    return tuple(out), len(face_sets[-1])


def eulerian_numbers(n):
    v = (1,)
    for m in range(2, n + 1):
        v = tuple((k + 1) * (v[k] if k < len(v) else 0)
                  + (m - k) * (v[k - 1] if k else 0)
                  for k in range(m))
    return v


def verify():
    graphs = 0
    for n in range(3, 6):
        complete = [(a, b) for a in range(n) for b in range(a + 1, n)]
        for mask in range(1 << len(complete)):
            edges = frozenset(edge for bit, edge in enumerate(complete) if mask & (1 << bit))
            if not is_connected(range(n), edges):
                continue
            absent = disconnected_proper_sets(n, edges)
            antichain = all(not (a < b or b < a) for a, b in combinations(absent, 2))
            assert antichain == complement_is_matching(n, edges), (n, edges)
            graphs += 1
    print('CONNECTED_GRAPH_ANTICHAIN_CASES', graphs)

    cases = 0
    for n in range(3, 8):
        for r in range(n // 2 + 1):
            edges = graph_edges(n, r)
            missing = disconnected_proper_sets(n, edges)
            should_be = {frozenset((2 * i, 2 * i + 1)) for i in range(r)}
            assert missing == should_be, (n, r, missing)
            actual, maximal_count = h_coefficients(n, edges)
            expected = list(eulerian_numbers(n))
            for k, coeff in enumerate(eulerian_numbers(n - 2)):
                expected[k + 1] -= r * coeff
            assert actual == tuple(expected), (n, r, actual, expected)
            assert sum(actual) == __import__('math').factorial(n) - r * __import__('math').factorial(n - 2)
            assert maximal_count == sum(actual)
            print('BETTI_PROFILE', n, r, tuple(actual), 'fixed_points', maximal_count)
            cases += 1
    print('MATCHING_GRAPH_PROFILES', cases)
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    verify()
