#!/usr/bin/env python3
"""Independent exhaustive checks of triple intersections of exact-two Hamming spheres.
Only Python's standard library is required.
"""
from collections import Counter
from itertools import combinations
from math import comb


def expected_histogram(n):
    assert n >= 3
    p = Counter()
    p[n - 2] += (1 << n) * comb(n, 3)
    for d, rate, size in [(4, 3, 4), (5, 10, 3), (6, 15, 1)]:
        if n >= d:
            p[size] += (1 << n) * rate * comb(n, d)
    p[0] = comb(1 << n, 3) - sum(p.values())
    return +p


def actual_histogram(n):
    words = list(range(1 << n))
    # These masks are generated independently of the coordinate-pattern proof.
    shells = [sum(1 << y for y in words if (y ^ x).bit_count() == 2) for x in words]
    hist = Counter()
    for a in range(len(words)):
        for b in range(a + 1, len(words)):
            partial = shells[a] & shells[b]
            for c in range(b + 1, len(words)):
                hist[(partial & shells[c]).bit_count()] += 1
    return +hist


def algebraic_profile_checks():
    # The eight possible positive-intersection orbit patterns arise by
    # enumerating three nonnegative binary-center disagreement counts.
    found = {}
    for a in range(5):
        for b in range(5):
            for c in range(5):
                if not (0 < a + b <= 4 and 0 < a + c <= 4 and 0 < b + c <= 4):
                    continue
                if (a + b) % 2 or (a + c) % 2 or (b + c) % 2:
                    continue
                k = max(6, a + b + c)
                A = k - a - b - c
                val = 0
                for r in range(c + 1):
                    j = (a + c) // 2 - r
                    l = (b + c) // 2 - r
                    i = 2 - r - j - l
                    if 0 <= j <= a and 0 <= l <= b and 0 <= i <= A:
                        val += comb(c, r) * comb(a, j) * comb(b, l) * comb(A, i)
                found[(a, b, c)] = val
    expect = {(0, 2, 2): 4, (2, 0, 2): 4, (2, 2, 0): 4,
              (1, 1, 1): 4, (1, 1, 3): 3, (1, 3, 1): 3,
              (3, 1, 1): 3, (2, 2, 2): 1}
    assert found == expect, (found, expect)


def main():
    algebraic_profile_checks()
    for n in range(3, 9):
        have = actual_histogram(n)
        want = expected_histogram(n)
        assert have == want, (n, have, want)
        positive = sum(count for size, count in have.items() if size > 0)
        mx = max(have)
        assert mx == (1 if n == 3 else max(4, n-2))
        print(f'n={n}: triples={comb(1 << n, 3)}, positive={positive}, maximum={mx}, profiles={dict(sorted(have.items()))}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
