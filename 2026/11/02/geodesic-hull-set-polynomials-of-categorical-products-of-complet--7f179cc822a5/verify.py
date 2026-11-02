"""Independent finite checks of geodesic hull-set enumerators for clique direct products.

Run with Python 3, standard library only. Finite checks corroborate the structural
proof; they do not replace its arguments for arbitrary graph dimensions.
"""
from collections import Counter
from itertools import permutations
from math import comb, factorial


def graph(m, n):
    v = [(i, j) for i in range(m) for j in range(n)]
    adj = [[b for b, (k, l) in enumerate(v) if k != i and l != j]
           for (i, j) in v]
    return v, adj


def intervals(m, n):
    v, adj = graph(m, n)
    size = len(v)
    distances = []
    for src in range(size):
        d = [-1] * size
        d[src] = 0
        layer = [src]
        while layer:
            future = []
            for a in layer:
                for b in adj[a]:
                    if d[b] == -1:
                        d[b] = d[a] + 1
                        future.append(b)
            layer = future
        assert all(x >= 0 for x in d)
        distances.append(d)
    assert max(map(max, distances)) == 2
    middle = [[0] * size for _ in range(size)]
    for a in range(size):
        for b in range(a + 1, size):
            distance = distances[a][b]
            mid = 0
            if distance > 1:
                for c in range(size):
                    if distances[a][c] + distances[c][b] == distance:
                        mid |= 1 << c
            middle[a][b] = mid
    return v, middle


def close(seed, middle, size):
    selected = seed
    while True:
        indexes = [i for i in range(size) if selected & (1 << i)]
        expanded = selected
        for k, a in enumerate(indexes):
            for b in indexes[k + 1:]:
                expanded |= middle[a][b]
        if expanded == selected:
            return expanded
        selected = expanded


def predicted(m, n):
    if (m, n) == (3, 3):
        return {3: 6, 4: 45, 5: 90, 6: 78, 7: 36, 8: 9, 9: 1}
    size = m * n
    return {k: comb(size, k) -
            (comb(m, k) * comb(n, k) * factorial(k)
             if k <= min(m, n) else 0)
            for k in range(size + 1)
            if comb(size, k) - (comb(m, k) * comb(n, k) * factorial(k)
                                if k <= min(m, n) else 0)}


def main():
    cases = [(3, 3), (3, 4), (4, 3), (3, 5), (4, 4)]
    total = 0
    for m, n in cases:
        vertex, mid = intervals(m, n)
        nvert = len(vertex)
        full = (1 << nvert) - 1
        actual = Counter()
        convex = []
        for seed in range(1 << nvert):
            hull = close(seed, mid, nvert)
            if hull == full:
                actual[seed.bit_count()] += 1
            elif m == n == 3 and hull == seed:
                convex.append(seed)
            total += 1
        assert dict(actual) == predicted(m, n), (m, n, actual, predicted(m, n))
        if (m, n) == (3, 3):
            six = set()
            for perm in permutations(range(3)):
                matching = sum(1 << (i * 3 + perm[i]) for i in range(3))
                six.add(full ^ matching)
            assert len(six) == 6
            assert set(s for s in convex if s.bit_count() == 6) == six
            assert all(any((s & ~q) == 0 for q in six) for s in convex)
            for s in range(1 << 9):
                assert (close(s, mid, 9) != full) == any(
                    (s & ~q) == 0 for q in six)
        print(f'CHECK_OK: {(m, n)}, {1 << nvert} subsets; hull counts {dict(sorted(actual.items()))}')
    # Independent finite inclusion-exclusion on the six maximal convex sets.
    v, middle = intervals(3, 3)
    full = (1 << 9) - 1
    maximal = [full ^ sum(1 << (i * 3 + p[i]) for i in range(3))
               for p in permutations(range(3))]
    nonhull_by_ie = Counter()
    for k in range(1, 1 << 6):
        intersect = full
        for a in range(6):
            if k & (1 << a):
                intersect &= maximal[a]
        sign = 1 if k.bit_count() % 2 == 1 else -1
        for j in range(intersect.bit_count() + 1):
            nonhull_by_ie[j] += sign * comb(intersect.bit_count(), j)
    for j in range(10):
        assert comb(9, j) - nonhull_by_ie[j] == predicted(3, 3).get(j, 0)
    print(f'VERIFY_OK: {len(cases)} exact graph families, {total} subsets, 63-term exceptional inclusion-exclusion')


if __name__ == '__main__':
    main()
