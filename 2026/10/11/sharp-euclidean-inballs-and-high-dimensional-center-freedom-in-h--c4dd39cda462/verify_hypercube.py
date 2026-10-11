"""Exact checks for the Euclidean inballs of hypercube symmetric edge polytopes.

The finite computations are corroboration, not an all-dimensions proof.
Uses Python 3 standard library only.
"""
from collections import Counter
from fractions import Fraction


def polar_vertices(d):
    n = 1 << d
    earlier = [[u ^ (1 << j) for j in range(d) if (u ^ (1 << j)) < u]
               for u in range(n)]
    values = [0] * n

    def search(i):
        if i == n:
            yield tuple(values)
            return
        choices = None
        for v in earlier[i]:
            options = {values[v] - 1, values[v] + 1}
            choices = options if choices is None else choices & options
        for val in sorted(choices or []):
            values[i] = val
            yield from search(i + 1)
    return list(search(1))


def rank_of_rows(rows):
    a = [[Fraction(z) for z in r] for r in rows]
    if not a:
        return 0
    h, w, rank = len(a), len(a[0]), 0
    for col in range(w):
        pivot = next((i for i in range(rank, h) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        z = a[rank][col]
        a[rank] = [t / z for t in a[rank]]
        for i in range(rank + 1, h):
            z = a[i][col]
            if z:
                a[i] = [t - z * q for t, q in zip(a[i], a[rank])]
        rank += 1
        if rank == h:
            break
    return rank


def check():
    for d, expected in [(2, 6), (3, 38), (4, 990)]:
        n = 1 << d
        vertices = polar_vertices(d)
        assert len(vertices) == expected
        M = Fraction(n*d, 4)
        centered = []
        norms = Counter()
        maximizing = []
        for p in vertices:
            mean = Fraction(sum(p), n)
            f = tuple(Fraction(x) - mean for x in p)
            sq = sum(x*x for x in f)
            assert all(abs(p[u] - p[u ^ (1 << j)]) == 1
                       for u in range(n) for j in range(d))
            assert sq <= M
            norms[sq] += 1
            centered.append((f, sq))
            if sq == M:
                maximizing.append(f)
        assert len(maximizing) == n
        assert rank_of_rows(maximizing) == d
        # Every maximal polar vertex is a Walsh-linear (rank-one) character sum.
        expected_contacts = set()
        from itertools import product
        for signs in product([-1, 1], repeat=d):
            vector = tuple(Fraction(sum(signs[j] * (1 if ((u >> j) & 1) == 0 else -1)
                                         for j in range(d)), 2)
                           for u in range(n))
            expected_contacts.add(vector)
        assert set(maximizing) == expected_contacts
        # A nonzero higher-degree Walsh displacement remains a maximal-ball center.
        # The check is exact rational after squaring the nonnegative inequality.
        degree_two = tuple(1 if ((u & 1) == 0) == (((u >> 1) & 1) == 0) else -1
                           for u in range(n))
        center = tuple(Fraction(z, 1000) for z in degree_two)
        assert sum(center) == 0
        assert all(sum(center[u] * (1 if ((u >> j) & 1) == 0 else -1)
                       for u in range(n)) == 0 for j in range(d))
        for f, sq in centered:
            dot = abs(sum(center[u]*f[u] for u in range(n)))
            assert dot <= 1 and (1-dot)**2 >= sq / M, (d, dot, sq)
        print(f'PASS d={d}: {len(vertices)} polar vertices, {len(maximizing)} '
              f'maximum-norm facets, Walsh rank {d}, '
              f'center affine dimension {n-d-1}; exact displaced-ball test passed')
    print('PASS: all finite exact checks')


if __name__ == '__main__':
    check()
