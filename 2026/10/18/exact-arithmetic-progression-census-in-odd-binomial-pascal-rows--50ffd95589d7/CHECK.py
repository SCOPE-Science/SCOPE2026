#!/usr/bin/env python3
"""Exact-arithmetic finite corroboration of the Pascal-row progression formula."""
from math import prod


def run_lengths(n):
    return [len(s) for s in bin(n)[2:].split('0') if s]


def predicted(n, k):
    assert n >= 1 and k >= 2
    lengths = [1 << t for t in run_lengths(n)]
    block_counts = []
    for length in lengths:
        max_step = (length - 1) // (k - 1)
        block_counts.append(length * (2 * max_step + 1) -
                            (k - 1) * max_step * (max_step + 1))
    return (prod(block_counts) - prod(lengths)) // 2


def direct(n, k):
    # Lucas' parity support, then literal positive-step enumeration.
    positions = [j for j in range(n + 1) if (j & n) == j]
    allowed = set(positions)
    return sum(all(a + t * d in allowed for t in range(k))
               for a in positions
               for d in range(1, (n - a) // (k - 1) + 1))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    comparisons = 0
    for n in range(1, 1025):
        lengths = run_lengths(n)
        kmax = 1 << max(lengths)
        ones = sum(lengths)
        c = sum(t == max(lengths) for t in lengths)
        expected_max = (1 << (ones - c * max(lengths))) * (
            ((1 << max(lengths)) + 2) ** c - (1 << (c * max(lengths)))
        ) // 2
        assert predicted(n, kmax) == expected_max, (n, 'extremal count')
        assert predicted(n, kmax + 1) == 0, (n, 'maximality')
        assert (predicted(n, 3) == 0) == ('11' not in bin(n)), (n, '3AP')
        for k in range(2, 10):
            formula = predicted(n, k)
            observed = direct(n, k)
            comparisons += 1
            assert formula == observed, (n, k, formula, observed)
    for digits in range(13):
        observed = sum(i == 0 or '11' not in bin(i)[2:] for i in range(1 << digits))
        assert observed == fib(digits + 2), (digits, observed)
    assert [predicted(27, k) for k in (2, 3, 4)] == [120, 24, 10]
    print('PASS: {} exact direct counts, 1024 extrema, 1024 3AP criteria, '
          '13 Fibonacci checks'.format(comparisons))


if __name__ == '__main__':
    main()
