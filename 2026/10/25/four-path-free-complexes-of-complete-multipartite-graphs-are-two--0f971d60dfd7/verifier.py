"""Finite independent checks for four-vertex path-free multipartite complexes.

This program uses only the Python standard library. It tests the definition by
enumerating actual four-vertex graph paths, independently tests the face
classification, and computes all reduced homology ranks over F_2.
"""
from itertools import combinations, permutations
from math import comb


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(1, total - length + 2):
        for tail in compositions(total - first, length - 1):
            yield (first,) + tail


def check(sizes):
    n = sum(sizes)
    colors = tuple(i for i, count in enumerate(sizes) for _ in range(count))
    edges = {(i, j) for i in range(n) for j in range(n)
             if colors[i] != colors[j]}
    forbidden = set()
    for four in combinations(range(n), 4):
        if any((path[0], path[1]) in edges and
               (path[1], path[2]) in edges and
               (path[2], path[3]) in edges
               for path in permutations(four)):
            forbidden.add(sum(1 << j for j in four))
    by_dim = [[] for _ in range(n)]
    for mask in range(1, 1 << n):
        actual = all(mask & pattern != pattern for pattern in forbidden)
        counts = tuple(sum(bool(mask & (1 << j)) and colors[j] == i
                           for j in range(n)) for i in range(len(sizes)))
        occupied = tuple(x for x in counts if x)
        expected = (len(occupied) <= 1 or
                    (len(occupied) == 2 and min(occupied) == 1) or
                    (len(occupied) == 3 and max(occupied) == 1))
        assert actual == expected, (sizes, mask, actual, expected)
        if actual:
            by_dim[mask.bit_count()-1].append(mask)
    while by_dim and not by_dim[-1]:
        by_dim.pop()
    ranks = []
    for d in range(1, len(by_dim)):
        index = {mask: j for j, mask in enumerate(by_dim[d-1])}
        pivots = {}
        for face in by_dim[d]:
            col = 0
            for j in range(n):
                if face & (1 << j):
                    col ^= 1 << index[face ^ (1 << j)]
            while col:
                high = col.bit_length() - 1
                if high not in pivots:
                    pivots[high] = col
                    break
                col ^= pivots[high]
        ranks.append(len(pivots))
    reduced = []
    for d, faces in enumerate(by_dim):
        rank_in = ranks[d] if d < len(ranks) else 0
        rank_out = ranks[d-1] if d else 0
        reduced.append(len(faces) - rank_in - rank_out - (d == 0))
    e2 = sum(sizes[i] * sizes[j] for i, j in combinations(range(len(sizes)), 2))
    e3 = sum(sizes[i] * sizes[j] * sizes[k]
             for i, j, k in combinations(range(len(sizes)), 3))
    predicted = e2 + e3 - (len(sizes)-1)*(n-1)
    assert all(b == (predicted if d == 2 else 0)
               for d, b in enumerate(reduced)), (sizes, reduced, predicted)
    return predicted, tuple(len(x) for x in by_dim)


def main():
    total = 0
    for n in range(3, 10):
        cases = 0
        for r in range(3, min(n, 5) + 1):
            for sizes in compositions(n, r):
                check(sizes)
                cases += 1
        total += cases
        print(f'N={n}: verified {cases} ordered compositions')
    print(f'TOTAL: {total} finite cases checked')
    for sizes in [(1,1,1),(2,1,1),(2,2,2),(3,3,1),
                  (3,3,3),(2,2,2,2),(3,2,2,2)]:
        beta, faces = check(sizes)
        print(f'{sizes}: f={faces}; reduced F2 Betti_2={beta}; other reduced Betti=0')
    print('PASS: direct path enumeration, face classification and all F2 boundary ranks')


if __name__ == '__main__':
    main()
