#!/usr/bin/env python3
"""Exact finite first-order type recursion for standard carousel tournaments.

Use: python3 research03_carousel_verify.py
No external dependencies.
"""
from functools import lru_cache


def complete_type(order, rank, normalize=True):
    assert order >= 3 and order % 2 == 1 and rank >= 0
    radius = (order - 1) // 2

    def orientation(a, b):
        if a == b:
            return 0
        return 1 if 1 <= (b - a) % order <= radius else 2

    @lru_cache(None)
    def rec(xs, remaining):
        if normalize and xs:
            offset = xs[0]
            xs = tuple((u - offset) % order for u in xs)
        atomic = tuple(
            orientation(xs[i], xs[j])
            for i in range(len(xs)) for j in range(i + 1, len(xs))
        )
        if remaining == 0:
            return atomic
        extensions = frozenset(rec(xs + (y,), remaining - 1)
                               for y in range(order))
        return (atomic, extensions)

    return rec((), rank)


def verify():
    orders = tuple(range(3, 16, 2))
    rank_four = [complete_type(n, 4) for n in orders]
    assert all(a != b for i, a in enumerate(rank_four)
               for b in rank_four[i+1:])
    print('RANK4_EXACT_CLASSES', ' '.join(str(n) for n in orders), 'tail>=15')
    print('FINITE_SEPARATION_ALL_21_PAIRS_OK')

    rank_three = [complete_type(n, 3) for n in orders]
    assert rank_three[0] != rank_three[1]
    assert rank_three[0] != rank_three[2]
    assert rank_three[1] != rank_three[2]
    assert all(x == rank_three[2] for x in rank_three[2:])
    print('RANK3_EXACT_CLASSES 3 5 tail>=7')

    for n in (3, 5, 7, 9):
        norm = complete_type(n, 4, True)
        raw = complete_type(n, 4, False)
        assert norm == raw
        print('ROTATION_FREE_DIRECT_CHECK_OK', n)

    for n in (17, 19, 21, 23, 25, 31):
        assert complete_type(n, 4) == rank_four[-1]
        print('ADDITIONAL_TAIL_CHECK_OK', n)

    print('NOTE: Infinite tail follows from antipodal-gap EF proof, not these tests.')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
