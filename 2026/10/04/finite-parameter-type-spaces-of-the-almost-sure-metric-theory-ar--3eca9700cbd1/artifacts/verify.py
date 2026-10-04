#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction
from math import comb, factorial
import itertools


def stirling2(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    row = [0] * (k + 1)
    row[0] = 1
    for a in range(1, n + 1):
        nxt = [0] * (k + 1)
        for b in range(1, min(a, k) + 1):
            nxt[b] = row[b - 1] + b * row[b]
        row = nxt
    return row[k]


def falling(m, j):
    ans = 1
    for t in range(j):
        ans *= m - t
    return ans


def bell(q):
    return sum(stirling2(q, k) for k in range(q + 1))


def N_inclusion(m, n, k):
    # Temporarily label the k new equality classes, require all of them,
    # then divide by k! to forget their labels.
    total = sum(((-1) ** i) * comb(k, i) * (m + k - i) ** n
                for i in range(k + 1))
    return total // factorial(k)


def N_stirling(m, n, k):
    # j nonempty classes are identified with distinct parameters;
    # k additional classes are genuinely new.
    return sum(stirling2(n, j + k) * comb(j + k, j) * falling(m, j)
               for j in range(0, min(m, n - k) + 1))


def enumerate_patterns(m, n):
    # A canonical pattern is an n-tuple whose entries are either one of m
    # named parameters ('p',i), or anonymous new blocks ('n',j) introduced
    # in restricted-growth order.  This independently enumerates equality /
    # parameter-identification patterns.
    counts = Counter()
    examples = []

    def rec(seq, new_count):
        if len(seq) == n:
            counts[new_count] += 1
            examples.append(tuple(seq))
            return
        for p in range(m):
            rec(seq + [('p', p)], new_count)
        for j in range(new_count):
            rec(seq + [('n', j)], new_count)
        rec(seq + [('n', new_count)], new_count + 1)

    rec([], 0)
    return counts, examples


def component_total(m, n):
    # Choose q variable positions not identified with parameters, partition
    # those q positions arbitrarily, and send the rest to named parameters.
    return sum(comb(n, q) * (m ** (n - q)) * bell(q) for q in range(n + 1))


def cube_dim(m, k):
    return m * k + comb(k, 2)


def check_triangle_gap():
    vals = [Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(1, 1)]
    for a, b, c in itertools.product(vals, repeat=3):
        assert a <= b + c and b <= a + c and c <= a + b


def main():
    check_triangle_gap()
    rows = []
    for m in range(0, 4):
        for n in range(1, 7):
            counts, patterns = enumerate_patterns(m, n)
            for k in range(n + 1):
                a = counts[k]
                b = N_inclusion(m, n, k)
                c = N_stirling(m, n, k)
                assert a == b == c, (m, n, k, a, b, c)
            total = sum(counts.values())
            assert total == component_total(m, n), (m, n, total, component_total(m, n))
            # The largest nonempty cell has k=n and the claimed dimension.
            assert counts[n] == 1
            assert max(cube_dim(m, k) for k in counts if counts[k]) == m*n + comb(n, 2)
            rows.append((m, n, total, tuple(counts[k] for k in range(n + 1))))

    # Explicit low-arity fingerprints.
    expected_m0 = [1, 2, 5, 15, 52, 203]  # Bell numbers B_n, n=1..6.
    assert [component_total(0, n) for n in range(1, 7)] == expected_m0
    expected_m1 = [2, 5, 15, 52, 203, 877]  # Bell B_{n+1}.
    assert [component_total(1, n) for n in range(1, 7)] == expected_m1

    print('checked parameter sizes m=0..3 and arities n=1..6')
    print('component totals for m=0:', [component_total(0, n) for n in range(1, 7)])
    print('component totals for m=1:', [component_total(1, n) for n in range(1, 7)])
    print('sample layer counts m=2,n=5:', [N_inclusion(2,5,k) for k in range(6)])
    print('top dimension m=3,n=6:', 3*6 + comb(6,2))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
