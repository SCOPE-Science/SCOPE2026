#!/usr/bin/env python3
"""Self-contained finite corroboration of the stated perfect-square reflection formula.

Usage: python3 verify.py. No third-party modules or downloaded data.
Finite exhaustive checks do not replace the infinite combinatorial argument.
"""
from math import isqrt


def formula(n):
    if n < 0:
        raise ValueError("length must be nonnegative")
    if n == 0:
        return 1
    if n == 1:
        return 2
    m, e = divmod(n, 2)
    return 2 + ((m + 1) ** 2 // 3) + e


def finite_prefix(n):
    # For length n, a factor with >=2 ones has its first consecutive-square
    # pair indexed by k with 2*k+1 <= n-1. For all other factors, a late
    # isolated 1 has at least n zeros on both sides. Hence this prefix
    # contains every distinct length-n factor of the infinite word.
    big = (n + 5) // 2 + 4
    length = big * big + 2 * n + 20
    word = bytearray(length)
    for k in range(isqrt(length - 1) + 1):
        word[k * k] = 1
    return word


def direct_counts(n):
    if n == 0:
        return 1, 1
    word = finite_prefix(n)
    factors = {bytes(word[i:i+n]) for i in range(len(word) - n + 1)}
    classes = {min(w, w[::-1]) for w in factors}
    return len(classes), len(factors)


def count_by_gaps(n):
    if n == 0:
        return 1, 1
    if n == 1:
        return 2, 2
    classes = 1 + (n + 1) // 2  # zero factor + one-one reversal classes
    factors = 1 + n
    for k in range((n - 2) // 2 + 1):
        before = 0 if k == 0 else 2 * k - 2
        rem = n - 2 * k - 2
        count = min(before, rem) + 1
        factors += count
        classes += count
        # A reversal match requires both outside runs to lie before the
        # preceding square. Its a-values form a symmetric integer interval;
        # each unequal pair is counted twice and should be merged.
        low = max(0, rem - before)
        high = min(rem, before)
        choices = max(0, high - low + 1)
        classes -= choices // 2
    return classes, factors


def main():
    for n in range(0, 101):
        reflected, distinct = direct_counts(n)
        by_gaps = count_by_gaps(n)
        assert reflected == formula(n) == by_gaps[0], (n, reflected, formula(n), by_gaps)
        assert distinct == by_gaps[1], (n, distinct, by_gaps)
    for n in range(101, 2001):
        assert count_by_gaps(n)[0] == formula(n), n
    for m in range(1, 1001):
        assert count_by_gaps(2*m)[1] == 1 + 3*m + 2*((m-2)**2//4)
    print("VERIFY_OK direct_reversal_census_lengths=0..100 gap_count_lengths=101..2000 ordinary_even_lengths=2..2000")


if __name__ == "__main__":
    main()
