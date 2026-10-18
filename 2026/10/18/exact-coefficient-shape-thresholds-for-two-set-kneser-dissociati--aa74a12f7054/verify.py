"""Definition-based finite checker for dissociation polynomials of two-set Kneser graphs.
Uses exact integers and the adjacency definition, not a classification oracle.
Python 3.10+; no third-party packages.
"""
from itertools import combinations
from math import comb


def formula(n):
    a = [0] * (max(n - 1, 6) + 1)
    a[0] = 1
    a[1] = comb(n, 2)
    for k in range(2, n):
        a[k] += n * comb(n - 1, k)
    a[3] += comb(n, 3)
    for k in range(7):
        a[k] += comb(n, 4) * (comb(6, k) - (comb(3, k) * 2**k if k <= 3 else 0))
    return a


def direct(n):
    edges = list(combinations(range(n), 2))
    m = len(edges)
    adj = [0] * m
    for i, e in enumerate(edges):
        for j, f in enumerate(edges):
            if i != j and set(e).isdisjoint(f):
                adj[i] |= 1 << j
    good = bytearray(1 << m)
    good[0] = 1
    counts = [0] * (m + 1)
    counts[0] = 1
    maximal = [0] * (m + 1)
    for mask in range(1, 1 << m):
        # Dissociation is hereditary. Check only the newly added vertex,
        # plus its previously selected neighbors (which may gain a second neighbor).
        bit = mask & -mask
        i = bit.bit_length() - 1
        rest = mask ^ bit
        if not good[rest]:
            continue
        neigh = rest & adj[i]
        if neigh & (neigh - 1):
            continue
        if neigh and (rest & adj[neigh.bit_length() - 1]):
            # Any selected old neighbor already had an old selected neighbor.
            continue
        good[mask] = 1
        counts[mask.bit_count()] += 1
    # Explicit one-vertex extension test, independent of maximal classification.
    for mask, val in enumerate(good):
        if not val: continue
        if not any(good[mask | (1 << j)] for j in range(m) if not (mask & (1 << j))):
            maximal[mask.bit_count()] += 1
    return counts, maximal, (1 << m)


def is_unimodal(a):
    return any(all(a[i] <= a[i + 1] for i in range(k)) and
               all(a[i] >= a[i + 1] for i in range(k, len(a) - 1))
               for k in range(len(a)))


def is_logconcave(a):
    return all(a[k] ** 2 >= a[k - 1] * a[k + 1]
               for k in range(1, len(a) - 1))


def main():
    total = 0
    for n in range(4, 8):
        actual, maximal, examined = direct(n)
        expect = formula(n)
        assert actual[:len(expect)] == expect and not any(actual[len(expect):]), (n, actual, expect)
        expected_maximal = [0] * len(maximal)
        if n >= 5: expected_maximal[n - 1] += n
        expected_maximal[6] += comb(n, 4)
        assert maximal == expected_maximal, (n, maximal, expected_maximal)
        total += examined
    for n in range(4, 501):
        a = formula(n)
        assert is_unimodal(a) == (n != 14), (n, 'unimodality')
        assert is_logconcave(a) == (n <= 12), (n, 'log-concavity')
    print(f'VERIFICATION_OK direct_orders=4..7 subsets={total} maximal_sets_checked=True shape_orders=4..500')

if __name__ == '__main__':
    main()
