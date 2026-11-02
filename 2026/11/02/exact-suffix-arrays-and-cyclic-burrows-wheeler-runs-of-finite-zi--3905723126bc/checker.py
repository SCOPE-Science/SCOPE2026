#!/usr/bin/env python3
"""Reproduce finite checks for Zimin suffix arrays and cyclic Burrows-Wheeler transforms.

All positions are zero-based; the original rotation has start position zero.
The checks enumerate and sort all suffixes independently of the recurrence.
"""
from itertools import groupby


def word(rank):
    w = ()
    for a in range(1, rank + 1):
        w = w + (a,) + w
    return w


def suffix_array_brute(w):
    return sorted(range(len(w)), key=lambda i: w[i:])


def suffix_array_formula(rank):
    sa = [0]
    for n in range(2, rank + 1):
        old_length = 2 ** (n - 1) - 1
        sa = [2 * old_length] + [2 * i for i in sa] + [2 * i + 1 for i in sa]
    return sa


def bwt_brute(w):
    starts = sorted(range(len(w)), key=lambda i: w[i:] + w[:i])
    return tuple(w[(i - 1) % len(w)] for i in starts), starts


def bwt_formula(rank):
    if rank == 1:
        return (1,)
    initial = tuple(range(2, rank + 1)) + (1,)
    middle = tuple(letter for j in range(rank - 1, 1, -1)
                   for letter in [j] * (2 ** (rank - j) - 1))
    return initial + middle + (1,) * (2 ** (rank - 1) - 1)


def run_encoding(w):
    return [(a, sum(1 for _ in g)) for a, g in groupby(w)]


def run():
    # Exact cyclic sorting remains independent through rank nine.
    for n in range(1, 10):
        w = word(n)
        cyclic_bwt, starts = bwt_brute(w)
        sa = suffix_array_brute(w)
        asserted_sa = suffix_array_formula(n)
        asserted_bwt = bwt_formula(n)
        assert starts == sa, ('cyclic versus suffix order', n)
        assert sa == asserted_sa, ('suffix array recurrence', n)
        assert cyclic_bwt == asserted_bwt, ('BWT blocks', n)
        assert starts.index(0) + 1 == n, ('primary row', n)
        assert len(run_encoding(cyclic_bwt)) == (2 if n == 2 else 2 * n - 1), ('run count', n)
        print(f'rank={n} length={len(w)} bwt_runs={len(run_encoding(cyclic_bwt))} original_row={n}')

    # A separate set of suffix-order checks at larger rank.
    for n in (10, 11):
        w = word(n)
        sa = suffix_array_brute(w)
        assert sa == suffix_array_formula(n), ('large suffix array', n)
        bwt_from_sa = tuple(w[(i - 1) % len(w)] for i in sa)
        assert bwt_from_sa == bwt_formula(n), ('large BWT', n)
        print(f'rank={n} length={len(w)} suffixes=verified bwt=verified')
    print('All finite checks passed; unrestricted claims rely on the supplied proof.')


if __name__ == '__main__':
    run()
