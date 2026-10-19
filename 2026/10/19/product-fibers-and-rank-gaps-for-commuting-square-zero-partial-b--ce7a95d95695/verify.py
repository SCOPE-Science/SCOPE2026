"""Independent finite enumeration of commuting square-zero partial injections.

Run with Python 3.9 or newer. This checks every pair for n <= 7, every
prescribed product fiber, and the exponential-generating-function counts.
It supplies finite corroboration, not a replacement for the general proof.
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb, factorial


def partial_square_zero_maps(n):
    """Construct from disjoint source/target sets, not from graph classes."""
    U = tuple(range(n))
    for k in range(n // 2 + 1):
        for sources in combinations(U, k):
            remaining = [u for u in U if u not in sources]
            for targets in permutations(remaining, k):
                f = [-1] * n
                for u, v in zip(sources, targets):
                    f[u] = v
                yield tuple(f)


def compose(f, g):
    """(f o g)(x); undefined values are represented by -1."""
    return tuple(-1 if v == -1 else f[v] for v in g)


def zero_product_counts(nmax):
    """Integer species recurrence based on alternating paths and cycles."""
    z = [0] * (nmax + 1)
    z[0] = 1
    for n in range(1, nmax + 1):
        connected = lambda k: (1 if k == 1 else
                               2 * factorial(k) +
                               (2 * factorial(k - 1) if k % 2 == 0 else 0))
        z[n] = sum(comb(n - 1, k - 1) * connected(k) * z[n - k]
                   for k in range(1, n + 1))
    return z


def product_fiber(n, rank, z):
    if 4 * rank > n:
        return 0
    return factorial(n - 2 * rank) // factorial(n - 4 * rank) * z[n - 4 * rank]


def main():
    Z = zero_product_counts(12)
    for n in range(8):
        mappings = list(partial_square_zero_maps(n))
        mapping_set = set(mappings)
        fibers = Counter()
        for a in mappings:
            for b in mappings:
                ab = compose(a, b)
                if ab == compose(b, a):
                    assert ab in mapping_set
                    fibers[ab] += 1
        observed_by_rank = Counter()
        for c in mappings:
            r = sum(v >= 0 for v in c)
            observed = fibers[c]
            expected = product_fiber(n, r, Z)
            assert observed == expected, (n, r, c, observed, expected)
            observed_by_rank[r] += observed
        assert fibers.keys() <= mapping_set
        for r in range(n // 4 + 1):
            num_outputs = factorial(n) // (factorial(r) * factorial(n - 2 * r))
            assert observed_by_rank[r] == num_outputs * product_fiber(n, r, Z)
        print('n=%d maps=%d total=%d ranks=%s VERIFIED' %
              (n, len(mappings), sum(fibers.values()),
               dict(sorted(observed_by_rank.items()))))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
