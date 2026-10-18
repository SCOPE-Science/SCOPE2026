"""Exact finite checks of cubical norming faces for book-graph free spaces.

Python standard library only. Run: python3 verify_book_faces.py
An analytic classification is required for the all-parameter theorem.
"""
from collections import Counter
from itertools import product
from math import comb


def vertices(m):
    """Normalized extreme unit-Lipschitz functions on the book graph."""
    return sorted(set(
        [(0,) + x for x in product((-1, 1), repeat=m)]
        + [(1,) + x for x in product((0, 1), repeat=m)]
        + [(-1,) + x for x in product((-1, 0), repeat=m)]
    ))


def connected_tight(m, v):
    """Independent spanning-tight graph criterion for a dual vertex."""
    h = (0, v[0]) + v[1:]
    edges = [(0, 1)] + [(i, j) for i in (0, 1) for j in range(2, m+2)]
    adj = [set() for _ in h]
    for i, j in edges:
        if abs(h[i]-h[j]) == 1:
            adj[i].add(j)
            adj[j].add(i)
    reach = {0}
    while True:
        nxt = reach | set().union(*(adj[i] for i in reach))
        if nxt == reach:
            break
        reach = nxt
    return len(reach) == m + 2


def affine_rank(points):
    """Exact rational-free rank by fraction-free integer Gaussian elimination."""
    if len(points) <= 1:
        return 0
    a = [[z-y for z, y in zip(x, points[0])] for x in points[1:]]
    nrows, ncols = len(a), len(a[0])
    rank = 0
    for col in range(ncols):
        pivot = next((i for i in range(rank, nrows) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        q = a[rank][col]
        for i in range(rank+1, nrows):
            p = a[i][col]
            if not p:
                continue
            a[i] = [q*a[i][c] - p*a[rank][c] for c in range(ncols)]
        rank += 1
        if rank == min(nrows, ncols):
            break
    return rank


def face_distribution(m):
    """Independently intersect all defining Lipschitz halfspace facets."""
    v = vertices(m)
    constraints = [lambda x: x[0] == 1, lambda x: x[0] == -1]
    for j in range(1, m+1):
        constraints += [
            lambda x, j=j: x[j] == 1,
            lambda x, j=j: x[j] == -1,
            lambda x, j=j: x[j]-x[0] == 1,
            lambda x, j=j: x[j]-x[0] == -1,
        ]
    facets = [sum((1 << i) for i, x in enumerate(v) if con(x)) for con in constraints]
    full = (1 << len(v))-1
    faces = {full}
    for facet in facets:
        faces.update({old & facet for old in tuple(faces)})
    counts = Counter()
    for mask in faces:
        if mask == 0:
            counts[-1] += 1
            continue
        points = [v[i] for i in range(len(v)) if (mask >> i) & 1]
        counts[affine_rank(points)] += 1
    return counts


def predicted(m):
    return [3 * comb(m, j) * (2 ** (m-j))
            + (2 * comb(m, j-1) * (2 ** (m-j+1)) if j else 0)
            - (1 if j == m else 0)
            for j in range(m+1)] + [1]


if __name__ == '__main__':
    for m in range(2, 7):
        observed = face_distribution(m)
        expected = predicted(m)
        assert [observed[k] for k in range(m+2)] == expected, (m, observed, expected)
        assert observed[-1] == 1
        assert len(vertices(m)) == 3 * 2**m
        # All plausible {-1,0,1}-valued potentials: independently identify vertices.
        candidates = []
        for h in product((-1,0,1), repeat=m+1):
            b=h[0]
            if all(abs(x-b) <= 1 for x in h[1:]) and connected_tight(m, h):
                candidates.append(h)
        assert sorted(candidates) == vertices(m), m
        print('m=%d: dual f-vector=%s; integer-potential criterion passed' % (m, expected))
    print('ALL EXACT BOOK-GRAPH FACE CHECKS PASSED')
