"""Exact finite checks for the Catalan excursion-length fragmentation law.

Standard-library-only: Python 3.9+.  These are finite checks, not a proof
of the stated all-n coupling; the mathematical proof is in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, prod


def cat(j):
    return comb(2 * j, j) // (j + 1)


def w(j):
    return cat(j - 1)


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for head in range(1, n - k + 2):
            for tail in compositions(n - head, k - 1):
                yield (head,) + tail


def partition(n, k):
    return {c: prod(w(v) for v in c) for c in compositions(n, k)}


def normalizer(n, k):
    return k * comb(2 * n - k, n - k) // (2 * n - k) if (k * comb(2 * n - k, n - k)) % (2 * n - k) == 0 else Fraction(k * comb(2 * n - k, n - k), 2 * n - k)


def verify_transition(n, k):
    parents = partition(n, k)
    children = partition(n, k + 1)
    z0 = sum(parents.values())
    z1 = sum(children.values())
    assert z0 == normalizer(n, k)
    assert z1 == normalizer(n, k + 1)
    output = defaultdict(Fraction)
    for p, mass in parents.items():
        for i, size in enumerate(p):
            if size <= 1:
                continue
            for a in range(1, size):
                b = size - a
                new = p[:i] + (a, b) + p[i+1:]
                prob = (Fraction(mass, z0) * Fraction(size-1, n-k)
                        * Fraction(w(a)*w(b), w(size)) * Fraction(1, k+1))
                for shift in range(k+1):
                    rotated = new[shift:] + new[:shift]
                    output[rotated] += prob
    assert set(output) == set(children)
    for c, count in children.items():
        assert output[c] == Fraction(count, z1), (n, k, c)
    assert sum(output.values()) == 1
    # A split decreases the sum of squares by 2ab > 0.
    expected_before = sum(Fraction(mass, z0) * sum(q*q for q in c)
                          for c, mass in parents.items())
    expected_after = sum(Fraction(mass, z1) * sum(q*q for q in c)
                         for c, mass in children.items())
    assert expected_before > expected_after


def verify_walk_counts(n):
    counts = defaultdict(int)
    for increments in product((-1, +1), repeat=2*n):
        h, last, lengths = 0, 0, []
        for t, step in enumerate(increments, 1):
            h += step
            if h == 0:
                lengths.append((t-last)//2)
                last = t
        if h == 0:
            counts[tuple(lengths)] += 1
    assert sum(counts.values()) == comb(2*n, n)
    for k in range(1, n+1):
        expected = partition(n, k)
        for lengths, mass in expected.items():
            assert counts[lengths] == 2**k * mass, (n, k, lengths)


def main():
    for n in range(2, 11):
        for k in range(1, n):
            verify_transition(n, k)
        print(f'Catalan transition: n={n}, every k, PASS')
    for n in range(1, 7):
        verify_walk_counts(n)
        print(f'Independent bridge enumeration: n={n}, PASS')
    print('All exact finite checks passed; all-n proof is separate.')


if __name__ == '__main__':
    main()
