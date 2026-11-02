"""Direct finite verification of a minimal-domination theorem for cycle powers.

Run: python verify_minimal_cycle_powers.py
The graph-level test does not call the cyclic-gap classification.
"""
from collections import Counter
from functools import lru_cache
from math import ceil


def graph_count(n, r):
    closed = []
    for v in range(n):
        mask = 0
        for w in range(n):
            d = min((w - v) % n, (v - w) % n)
            if d <= r:
                mask |= 1 << w
        closed.append(mask)
    target = (1 << n) - 1
    counts = Counter()
    for selection in range(1, target + 1):
        covered = 0
        for v in range(n):
            if selection & (1 << v):
                covered |= closed[v]
        if covered != target:
            continue
        minimal = True
        for v in range(n):
            if not (selection & (1 << v)):
                continue
            remainder_covered = 0
            for w in range(n):
                if w != v and selection & (1 << w):
                    remainder_covered |= closed[w]
            if remainder_covered == target:
                minimal = False
                break
        if minimal:
            counts[selection.bit_count()] += 1
    return dict(counts)


def word_counts(n, r):
    """Independently count finite cyclic integer words by dynamic programming."""
    largest = 2 * r + 1
    limit = 2 * r + 2
    result = {}
    for k in range(1, n + 1):
        if k > n or k * largest < n or k * (r + 1) > n:
            continue
        words = 0
        for first in range(1, largest + 1):
            @lru_cache(None)
            def extend(remaining, last, slots):
                if slots == 0:
                    return int(remaining == 0 and last + first >= limit)
                ans = 0
                for gap in range(1, largest + 1):
                    if last + gap >= limit and gap <= remaining:
                        ans += extend(remaining-gap, gap, slots - 1)
                return ans
            words += extend(n - first, first, k - 1)
        if words:
            assert n * words % k == 0, (n, r, k, words)
            result[k] = n * words // k
    return result


def check():
    graph_cases = 0
    subsets = 0
    for r in range(1, 5):
        for n in range(2*r+1, min(15, 2*r+10)):
            observed = graph_count(n, r)
            predicted = word_counts(n, r)
            assert observed == predicted, (r, n, observed, predicted)
            assert sorted(predicted) == list(range(ceil(n/(2*r+1)), n//(r+1)+1)), (r, n, predicted)
            graph_cases += 1
            subsets += 2**n-1
    parity_cases = 0
    for r in range(1, 8):
        for k in range(2, 7):
            n = k * (r + 1)
            got = word_counts(n, r).get(k, 0)
            expected = r + 1 if k % 2 else (r+1)*(2*r+1)
            assert got == expected, (r,k,got,expected)
            parity_cases += 1
    print(f'VERIFY_OK graph_cases={graph_cases} direct_subsets={subsets} parity_cases={parity_cases}')


if __name__ == '__main__':
    check()
