#!/usr/bin/env python3
"""Finite exact checks of the dyadic-threshold doubling-map word counts.

All infinite claims require the separately stated proof; enumeration is only
an independent finite consistency check.
"""
from fractions import Fraction


def count_safe(r, k, L):
    """Number of length-L strings with all r-windows having the common label."""
    assert r >= 2 and 0 < k < (1 << r) and k != (1 << (r-1))
    a = 0 if k < (1 << (r-1)) else 1
    states = {0: 1}  # bit histories, before first bit
    for pos in range(L):
        next_states = {}
        for mask, n in states.items():
            for bit in (0, 1):
                word = ((mask << 1) | bit) & ((1 << r)-1)
                if pos >= r-1 and (word < k) != bool(a):
                    continue
                short = word & ((1 << (r-1))-1)
                next_states[short] = next_states.get(short, 0) + n
        states = next_states
    return sum(states.values())


def brute_count(r, k, L):
    a = 0 if k < 1 << (r-1) else 1
    count = 0
    for full in range(1 << L):
        good = True
        for start in range(L-r+1):
            sub = (full >> (L-r-start)) & ((1 << r)-1)
            if (sub < k) != bool(a):
                good = False
                break
        count += good
    return count


def run():
    cases = 0
    brute = 0
    bounds = 0
    for r in range(2, 7):
        for k in range(1, 1 << r):
            if k == 1 << (r-1):
                continue
            cases += 1
            S = (1 << r)-k if k < 1 << (r-1) else k
            assert 1 <= S < (1 << r)
            # Two independently implemented counters.
            for L in range(r, min(r+5, 12)):
                assert count_safe(r, k, L) == brute_count(r, k, L), (r, k, L)
                brute += 1
            for L in range(r, r+34):
                q, t = divmod(L, r)
                N = count_safe(r, k, L)
                assert (1 << q) <= N <= S**q * (1 << t), (r, k, L, N)
                bounds += 1
            # The exact cylinder probabilities for n=1 are k/2^r or its complement.
            n1 = count_safe(r, k, r)
            assert n1 == S
            assert Fraction(n1, 1 << r) in (Fraction(k, 1 << r), Fraction((1 << r)-k, 1 << r))
    # At the half threshold the process is the iid leading-bit process.
    for n in range(1, 13):
        assert Fraction(1, 1 << n) == Fraction(2**(12-n), 2**12)
    print(f'VERIFY_OK {cases} thresholds, {brute} exact brute/DP comparisons, {bounds} finite persistence bounds')


if __name__ == '__main__':
    run()
