"""Reproducible direct graph-vertex verifier for minimal connected domination of rook graphs."""
from collections import Counter
from functools import lru_cache
from math import comb, factorial

@lru_cache(None)
def stirling(n, k):
    if n == 0:
        return int(k == 0)
    if k == 0:
        return 0
    return k * stirling(n - 1, k) + stirling(n - 1, k - 1)


def predicted(m, n):
    counts = Counter()
    for b in range(1, min(m - 1, n - 1) + 1):
        counts[m + b - 1] += comb(n, b) * m ** (b - 1) * factorial(b) * stirling(m - 1, b)
    for a in range(1, min(m - 1, n - 1) + 1):
        counts[n + a - 1] += comb(m, a) * n ** (a - 1) * factorial(a) * stirling(n - 1, a)
    return dict(sorted(counts.items()))


def direct(m, n):
    vertices = [(i, j) for i in range(m) for j in range(n)]
    order = len(vertices)
    adj = []
    for i, j in vertices:
        adj.append(sum(1 << q for q, (r, c) in enumerate(vertices)
                       if (r == i or c == j) and (r, c) != (i, j)))

    def dominates(mask):
        return all((mask & (1 << u)) or (adj[u] & mask) for u in range(order))

    def connected(mask):
        if not mask:
            return False
        discovered = mask & -mask
        while True:
            extended = discovered
            for u in range(order):
                if discovered & (1 << u):
                    extended |= adj[u] & mask
            if extended == discovered:
                return discovered == mask
            discovered = extended

    observed = Counter()
    for mask in range(1, 1 << order):
        if not dominates(mask) or not connected(mask):
            continue
        if any(dominates(mask ^ (1 << u)) and connected(mask ^ (1 << u))
               for u in range(order) if mask & (1 << u)):
            continue
        observed[mask.bit_count()] += 1
    return dict(sorted(observed.items()))


if __name__ == '__main__':
    boards = [(2, 2), (2, 3), (2, 4), (3, 3), (3, 4),
              (3, 5), (3, 6), (4, 4), (4, 5)]
    total = 0
    for m, n in boards:
        p, b = predicted(m, n), direct(m, n)
        assert p == b, (m, n, p, b)
        print(f'{m}x{n}: {p} = direct enumeration')
        total += (1 << (m * n)) - 1
    print(f'VERIFICATION_OK boards={len(boards)} candidate_subsets={total}')
