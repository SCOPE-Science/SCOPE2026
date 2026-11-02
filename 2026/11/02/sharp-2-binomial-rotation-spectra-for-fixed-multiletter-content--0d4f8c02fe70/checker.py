"""Independent finite tests for the multiletter two-binomial rotation theorem.

Run: python3 ternary_rotation_checker.py
Requires only Python's standard library. Finite tests support, but do not replace,
the arbitrary-length mathematical proof.
"""

from collections import Counter
from itertools import combinations
from math import gcd


def words_of_content(c):
    n = sum(c)
    def rec(left, prefix):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for a, count in enumerate(left):
            if count:
                left[a] -= 1
                prefix.append(a)
                yield from rec(left, prefix)
                prefix.pop()
                left[a] += 1
    yield from rec(list(c), [])


def direct_profile(t, k):
    """All scattered-subsequence counts of length 1 and 2, directly."""
    ones = [0] * k
    pairs = [[0] * k for _ in range(k)]
    for b in t:
        for a in range(k):
            pairs[a][b] += ones[a]
        ones[b] += 1
    return tuple(ones) + tuple(x for row in pairs for x in row)


def rotation_count_direct(t, k):
    n = len(t)
    return len({direct_profile(t[i:] + t[:i], k) for i in range(n)})


def rotation_count_walk(t, c):
    """Independent profile computation from circular prefix balance vectors."""
    k = len(c)
    n = len(t)
    prefix = [0] * k
    seen = set()
    for b in t:
        # Projective coordinates compare prefix counts scaled by total content.
        seen.add(tuple(n * prefix[a] - sum(prefix) * c[a] for a in range(k)))
        prefix[b] += 1
    return len(seen)


def periodic_at_primitive_content(t, c):
    d = gcd(*c)
    period = len(t) // d
    return all(t[i] == t[i % period] for i in range(len(t)))


def balanced_segment_collision(t, c):
    """Find any nontrivial circular segment with proportional Parikh vector."""
    n = len(t)
    d = gcd(*c)
    length_step = n // d
    for i in range(n):
        for j in range(1, d):
            length = j * length_step
            segment = tuple(t[(i + h) % n] for h in range(length))
            if all(segment.count(a) * d == j * c[a] for a in range(len(c))):
                return True
    return False


def bubble_path(c):
    """A constructive adjacent-transposition chain, periodic to grouped."""
    d = gcd(*c)
    w = [a for a in range(len(c)) for _ in range(c[a] // d)] * d
    target = [a for a in range(len(c)) for _ in range(c[a])]
    yield tuple(w)
    for i in range(len(w)):
        j = next(j for j in range(i, len(w)) if w[j] == target[i])
        while j > i:
            w[j], w[j - 1] = w[j - 1], w[j]
            j -= 1
            yield tuple(w)
    assert w == target


def test_content(c):
    k = len(c)
    n = sum(c)
    d = gcd(*c)
    L = n // d
    histogram = Counter()
    count = 0
    for t in words_of_content(c):
        count += 1
        a = rotation_count_direct(t, k)
        b = rotation_count_walk(t, c)
        assert a == b, (c, t, a, b)
        assert L <= a <= n, (c, t, a)
        assert (a == L) == periodic_at_primitive_content(t, c), (c, t, a)
        if d > 1:
            assert (a == n) == (not balanced_segment_collision(t, c)), (c, t, a)
        histogram[a] += 1
    assert sorted(histogram) == list(range(L, n + 1)), (c, histogram)
    path = list(bubble_path(c))
    numbers = [rotation_count_walk(t, c) for t in path]
    assert numbers[0] == L and numbers[-1] == n
    assert all(abs(x - y) <= 1 for x, y in zip(numbers, numbers[1:]))
    assert set(numbers) == set(range(L, n + 1))
    return count, histogram, len(path) - 1


def main():
    cases = [(2, 2, 2), (3, 3, 3), (2, 2, 4), (2, 4, 6),
             (2, 2, 2, 2), (2, 2, 1), (1, 1, 1), (1, 2, 3)]
    total = 0
    for c in cases:
        count, hist, swaps = test_content(c)
        total += count
        print('counts', c, 'words', count, 'spectrum',
              sorted(hist), 'histogram', dict(sorted(hist.items())),
              'witness-path-swaps', swaps)
    print('PASS: independent direct/walk agreement, exact spectra, extrema,')
    print('      balanced-arc criterion and adjacent-swap interpolation;')
    print('      total fixed-content words inspected:', total)


if __name__ == '__main__':
    main()
