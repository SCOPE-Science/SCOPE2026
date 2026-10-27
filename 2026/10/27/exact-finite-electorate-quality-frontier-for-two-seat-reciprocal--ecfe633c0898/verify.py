#!/usr/bin/env python3
"""Exact small-instance checks for two-seat reciprocal representation.

This file is an independent finite checker, not an infinite proof.
Usage: python verify.py
"""
from fractions import Fraction
from itertools import product, combinations
from random import Random


def jr(n, h, support, W):
    """Direct reciprocal-JR condition by enumerating voter groups."""
    size = len(h)
    chosen = set(W)
    for mask in range(1, 1 << n):
        voters = [v for v in range(n) if mask >> v & 1]
        common = [c for c in range(size) if all(support[c] >> v & 1 for v in voters)]
        if not common:
            continue
        if all(not any(support[c] >> v & 1 for c in W) for v in voters):
            if any(2 * len(voters) * h[c] >= n for c in common):
                return False
    return True


def ejr(n, h, support, W):
    if not jr(n, h, support, W):
        return False
    for mask in range(1, 1 << n):
        voters = [v for v in range(n) if mask >> v & 1]
        common = [c for c in range(len(h)) if all(support[c] >> v & 1 for v in voters)]
        for c, d in combinations(common, 2):
            if Fraction(1, h[c]) + Fraction(1, h[d]) <= Fraction(2 * len(voters), n):
                if all(sum(bool(support[t] >> v & 1) for t in W) < 2 for v in voters):
                    return False
    return True


def optimal_ratio(n, h, support, axiom):
    allW = list(combinations(range(len(h)), 2))
    best_possible = max(sum(h[c] for c in W) for W in allW)
    eligible = [sum(h[c] for c in W) for W in allW if axiom(n, h, support, W)]
    assert eligible
    return max(eligible) / best_possible


def instance(n, h, support):
    bound = Fraction(3 * n - 2, 4 * (n - 1))
    jr_ratio = optimal_ratio(n, h, support, jr)
    ejr_ratio = optimal_ratio(n, h, support, ejr)
    assert jr_ratio >= bound, (n, h, support, jr_ratio, bound)
    assert ejr_ratio >= bound, (n, h, support, ejr_ratio, bound)
    # EJR and JR have equal optimum for two seats.
    assert jr_ratio == ejr_ratio, (n, h, support, jr_ratio, ejr_ratio)
    return 1


def witness(n):
    tau = Fraction(n, 2*(n-1))
    h = [Fraction(1), Fraction(1), tau]
    sup = [1 << (n-1), 1 << (n-1), (1 << (n-1)) - 1]
    ratio = Fraction(3*n-2, 4*(n-1))
    assert optimal_ratio(n, h, sup, jr) == ratio
    assert optimal_ratio(n, h, sup, ejr) == ratio
    return 1


def main():
    count = 0
    qualities = (Fraction(1,2), Fraction(2,3), Fraction(3,4), Fraction(1))
    for n in (2, 3):
        for masks in product(range(1, 1 << n), repeat=3):
            for hs in product(qualities, repeat=3):
                count += instance(n, hs, masks)
    rng = Random(20260908)
    for n in range(2, 8):
        for _ in range(120):
            m = rng.randint(3, 6)
            sup = tuple(rng.randint(1, (1 << n)-1) for _ in range(m))
            hs = tuple(qualities[rng.randrange(len(qualities))] for _ in range(m))
            count += instance(n, hs, sup)
    for n in range(2, 9):
        count += witness(n)
    print('CHECKS_OK', count, 'including exhaustive 3-candidate profiles for 2-3 voters, sampled 2-7 voters, and sharp witnesses 2-8 voters')

if __name__ == '__main__':
    main()
