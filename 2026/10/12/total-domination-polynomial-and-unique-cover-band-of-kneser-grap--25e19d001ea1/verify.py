"""Exact, stdlib-only checks for the total-domination enumerator of KG(n,2)."""
from collections import Counter
from itertools import combinations
from math import comb


def bc(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def polynomial(n):
    """Return all cardinality coefficients, with negative values disallowed."""
    assert n >= 3
    m = bc(n, 2)
    total = Counter({k: bc(m, k) for k in range(m + 1)})
    low = Counter({
        0: 1,
        1: bc(n, 2),
        2: 3 * bc(n, 3) + 3 * bc(n, 4),
        3: bc(n, 3) + 12 * bc(n, 4) + 30 * bc(n, 5),
        4: 3 * bc(n, 4) + 60 * bc(n, 5) + 90 * bc(n, 6),
    })
    one_hub = Counter()
    for k in range(3, n):
        one_hub[k] += n * bc(n - 1, k)
        one_hub[k + 1] += n * bc(n - 1, 2) * bc(n - 1, k)
    for k in range(3, n - 1):
        one_hub[k + 2] += n * (n - 1) * bc(n - 2, 2) * bc(n - 2, k)
    two_hubs = Counter()
    for uv in (0, 1):
        for a in range(n - 1):
            for b in range(n - 1 - a):
                for c in range(n - 1 - a - b):
                    d = n - 2 - a - b - c
                    if d < 0 or uv + a + c < 3 or uv + b + c < 3:
                        continue
                    ways = bc(n, 2) * bc(n - 2, a) * bc(n - 2 - a, b) * bc(n - 2 - a - b, c)
                    two_hubs[uv + a + b + 2 * c] += ways
    excluded = low + one_hub + two_hubs
    answer = Counter({k: total[k] - excluded[k] for k in range(m + 1)})
    assert all(v >= 0 for v in answer.values())
    return answer


def brute(n):
    """Independent exhaustive test of every edge subset and all possible 2-covers."""
    edges = list(combinations(range(n), 2))
    m = len(edges)
    masks = []
    for u, v in edges:
        masks.append(sum(1 << i for i, (x, y) in enumerate(edges) if u in (x, y) or v in (x, y)))
    counts = Counter()
    for family in range(1 << m):
        if all(family & ~cover for cover in masks):
            counts[family.bit_count()] += 1
    return counts


def verify():
    subsets = 0
    for n in range(3, 7):
        observed = brute(n)
        predicted = polynomial(n)
        assert all(observed[k] == predicted[k] for k in range(bc(n, 2) + 1)), n
        subsets += 1 << bc(n, 2)
    for n in range(5, 31):
        p = polynomial(n)
        m = bc(n, 2)
        for k in range(n + 1, m + 1):
            failure = bc(n, 2) * bc(2 * n - 3, k) if k <= 2 * n - 3 else 0
            assert p[k] == bc(m, k) - failure, (n, k)
        if n == 5:
            assert p[4] == 10
        else:
            assert p[3] == 15 * bc(n, 6)
    print('VERIFY_OK exhaustive_n=3..6 subsets=%d top_band_n=5..30 endpoints_and_coefficients=passed' % subsets)
    print('PETERSEN', [(i, polynomial(5)[i]) for i in range(4, 11)])


if __name__ == '__main__':
    verify()
