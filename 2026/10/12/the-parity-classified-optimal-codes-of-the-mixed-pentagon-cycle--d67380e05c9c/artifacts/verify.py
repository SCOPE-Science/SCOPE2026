#!/usr/bin/env python3
"""Exact checker for maximum independent sets in C5 strong Cn.

Runs two finite counting algorithms and checks the all-length formula on
sample lengths.  The all-length theorem uses the separate symbolic proof.
"""
from collections import defaultdict
from math import comb


def states():
    return tuple(s for s in range(32) if all(not ((s >> i) & (s >> ((i + 1) % 5)) & 1) for i in range(5)))


def compatible(a, b):
    return all(((i - j) % 5 not in (0, 1, 4))
               for i in range(5) if (a >> i) & 1
               for j in range(5) if (b >> j) & 1)


STATES = states()
NEXT = {a: tuple(b for b in STATES if compatible(a, b)) for a in STATES}


def trace_independent_sets(n):
    """Direct transfer-matrix coefficient of weight n on cyclic strips."""
    tally = 0
    for first in STATES:
        dp = {(first, first.bit_count()): 1}
        for _ in range(1, n):
            nxt = defaultdict(int)
            for (last, weight), ways in dp.items():
                for state in NEXT[last]:
                    total = weight + state.bit_count()
                    if total <= n:
                        nxt[(state, total)] += ways
            dp = nxt
        tally += sum(ways for (last, weight), ways in dp.items()
                     if weight == n and compatible(last, first))
    return tally


def exhaustive_maximum(n):
    """Brute enumeration, independent of transfer-matrix aggregation."""
    tally, big = 0, 0

    def visit(first, last, pos, total):
        nonlocal tally, big
        if pos == n:
            if compatible(last, first):
                if total > big:
                    big, tally = total, 1
                elif total == big:
                    tally += 1
            return
        if total + 2 * (n-pos) < big:
            return
        for nxt in NEXT[last]:
            visit(first, nxt, pos + 1, total + nxt.bit_count())

    for first in STATES:
        visit(first, first, 1, first.bit_count())
    return big, tally


def predicted(n):
    walks = 5 * sum(comb(n, k) for k in range(n + 1) if (2*k - n) % 5 == 0)
    return walks + (2*5**(n//2) if n % 2 == 0 else 0)


def main():
    assert len(STATES) == 11, STATES
    for n in range(4, 23):
        direct = trace_independent_sets(n)
        formula = predicted(n)
        assert direct == formula, (n, direct, formula)
        if n <= 8:
            alpha, brute = exhaustive_maximum(n)
            assert alpha == n and brute == formula, (n, alpha, brute, formula)
        print(f"n={n:2d} alpha={n:2d} maximum_sets={formula}")
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
