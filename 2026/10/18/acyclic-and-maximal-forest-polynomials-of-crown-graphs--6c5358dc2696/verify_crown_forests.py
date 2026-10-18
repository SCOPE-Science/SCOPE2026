"""Direct exhaustive validation of crown-graph induced forests and maximality.

Python >=3.9; no third-party modules. Check all vertex subsets for orders 3..9.
This tests cycle-freeness by union-find on actual graph edges, then tests every
missing vertex for one-step extension. It does not use occupancy theorems.
"""
from collections import Counter
from math import comb


def predicted(n):
    forests = Counter()
    for a in range(n + 1):
        for b in range(n + 1):
            if min(a, b) <= 1:
                forests[(a, b)] = comb(n, a) * comb(n, b)
    forests[(2, 2)] = comb(n, 2) * (2 * n - 3)
    forests[(2, 3)] = comb(n, 2) * (n - 2)
    forests[(3, 2)] = comb(n, 2) * (n - 2)
    facets = Counter({(2, 3): comb(n, 2) * (n - 2),
                      (3, 2): comb(n, 2) * (n - 2)})
    if n >= 4:
        facets[(1, n)] = n
        facets[(n, 1)] = n
    return forests, facets


def actual(n):
    length = 2 * n
    adjacency = [0] * length
    for i in range(n):
        for j in range(n):
            if i != j:
                adjacency[i] |= 1 << (n + j)
                adjacency[n + j] |= 1 << i
    present = bytearray(1 << length)
    result = Counter()
    low_half = (1 << n) - 1

    def acyclic(mask):
        parent = list(range(length))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        for i in range(length):
            if not (mask & (1 << i)):
                continue
            neigh = adjacency[i] & mask & ~((1 << (i + 1)) - 1)
            while neigh:
                bit = neigh & -neigh
                neigh ^= bit
                j = bit.bit_length() - 1
                u, v = find(i), find(j)
                if u == v:
                    return False
                parent[u] = v
        return True

    for mask in range(1 << length):
        if acyclic(mask):
            present[mask] = 1
            a = (mask & low_half).bit_count()
            b = (mask >> n).bit_count()
            result[(a, b)] += 1
    facets = Counter()
    for mask, valid in enumerate(present):
        if valid and all(not present[mask | (1 << i)]
                         for i in range(length) if not mask & (1 << i)):
            a = (mask & low_half).bit_count()
            b = (mask >> n).bit_count()
            facets[(a, b)] += 1
    return result, facets


def main():
    candidates = 0
    for n in range(3, 10):
        predicted_faces, predicted_facets = predicted(n)
        actual_faces, actual_facets = actual(n)
        assert actual_faces == predicted_faces, ('faces', n, actual_faces, predicted_faces)
        assert actual_facets == predicted_facets, ('facets', n, actual_facets, predicted_facets)
        candidates += 1 << (2 * n)
        size_counts = Counter()
        for (a, b), total in actual_facets.items():
            size_counts[a + b] += total
        print('n=%d faces=%d facets=%d sizes=%s' % (
            n, sum(actual_faces.values()), sum(actual_facets.values()),
            dict(sorted(size_counts.items()))))
    assert candidates == sum(1 << (2*n) for n in range(3, 10))
    print('VERIFICATION_OK n=3..9 vertex_subsets=%d bivariate=True' % candidates)


if __name__ == '__main__':
    main()
