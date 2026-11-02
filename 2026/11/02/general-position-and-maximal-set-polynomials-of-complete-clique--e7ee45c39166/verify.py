#!/usr/bin/env python3
"""Independent exact checks for general-position polynomials of clique paths.

Uses the graph's adjacency list, breadth-first distances, and the geodesic
predicate directly. Does not use the structural classification to test sets.
All arithmetic is exact. Python 3 standard library only.
"""
from collections import deque
from math import comb


def build_graph(n, length):
    vertices = [(c, h) for c in range(n) for h in range(length)]
    edges = [[] for _ in vertices]
    for i, (c, h) in enumerate(vertices):
        for j, (d, k) in enumerate(vertices):
            if i != j and ((h == k and c != d) or (c == d and abs(h-k) == 1)):
                edges[i].append(j)
    return vertices, edges


def all_distances(edges):
    result = []
    for source in range(len(edges)):
        dist = [-1] * len(edges)
        dist[source] = 0
        todo = deque([source])
        while todo:
            u = todo.popleft()
            for v in edges[u]:
                if dist[v] < 0:
                    dist[v] = dist[u] + 1
                    todo.append(v)
        if any(x < 0 for x in dist):
            raise AssertionError('Disconnected product')
        result.append(dist)
    return result


def expected_polynomials(n, length):
    coefficients = [0] * (n + 2)
    for k in range(n + 1):
        coefficients[k] += comb(n, k) * length ** k
    for a in range(length):
        for b in range(a + 1, length):
            for k in range(n):
                coefficients[k+2] += n * comb(n-1, k) * (b-a-1) ** k
    first = n*(length-1)
    full = n * sum((length - 1 - h) * h**(n-1) for h in range(1, length-1))
    extendible_min = n * sum(h**(n-1) for h in range(1, length-1))
    overlap = n*(n-1) * sum((b-a-1)**(n-2)
        for a in range(1, length-1) for b in range(a+1, length-1))
    middle = length**n - 2*extendible_min + overlap
    maxima = [0] * (n+2)
    maxima[2] = first
    maxima[n] = middle
    maxima[n+1] = full
    return coefficients, maxima


def independently_count(n, length):
    _, edges = build_graph(n, length)
    d = all_distances(edges)
    nv = len(edges)
    pair_by_smallest = [[] for _ in range(nv)]
    for a in range(nv):
        for b in range(a+1, nv):
            for c in range(b+1, nv):
                if (d[a][c] == d[a][b] + d[b][c] or
                    d[a][b] == d[a][c] + d[c][b] or
                    d[b][c] == d[b][a] + d[a][c]):
                    pair_by_smallest[a].append((1<<b)|(1<<c))
    limit = 1 << nv
    good = bytearray(limit)
    good[0] = 1
    counts = [0] * (nv+1)
    max_counts = [0] * (nv+1)
    for mask in range(1, limit):
        low = mask & -mask
        u = low.bit_length() - 1
        rest = mask ^ low
        if good[rest] and not any((rest & bad) == bad for bad in pair_by_smallest[u]):
            good[mask] = 1
    for mask in range(limit):
        if not good[mask]:
            continue
        size = mask.bit_count()
        counts[size] += 1
        if all(not good[mask|(1<<j)] for j in range(nv) if not(mask & (1<<j))):
            max_counts[size] += 1
    return counts, max_counts, limit, sum(good)


def main():
    cases = [(3,3), (3,4), (4,3), (4,4), (3,5), (5,3), (3,6), (4,5)]
    checks = 0
    for n, length in cases:
        have, maximal, subsets, good_count = independently_count(n, length)
        want, expected_max = expected_polynomials(n, length)
        assert have[:n+2] == want, (n, length, have[:n+2], want)
        assert not any(have[n+2:]), (n, length)
        assert maximal[:n+2] == expected_max, (n, length, maximal[:n+2], expected_max)
        assert not any(maximal[n+2:]), (n, length)
        print('PASS', n, length, 'subsets', subsets, 'general_position_sets', good_count,
              'maximal_total', sum(maximal))
        checks += subsets
    print('VERIFIED_TOTAL_SUBSETS', checks)
    print('VERIFICATION_OK')

if __name__ == '__main__':
    main()
