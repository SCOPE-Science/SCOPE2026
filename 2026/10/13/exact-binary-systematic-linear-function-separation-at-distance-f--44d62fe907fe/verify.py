#!/usr/bin/env python3
"""Reproducibility checks for binary linear function-separation at distance four.
Only standard Python is required. Finite checks complement the all-dimension proof.
"""
from itertools import product
from math import comb


def threshold(r):
    return (1 << (r-1)) - r if r >= 1 else 0


def ntypes(fcols):
    return len(set(fcols) - {0})


def best_predicted(n):
    if n == 0:
        return 0
    return next(r for r in range(3, 64) if n <= threshold(r))


def delta_at_least_four(fcols, pcols):
    n = len(fcols)
    for mask in range(1, 1 << n):
        fv = 0
        pv = 0
        for i in range(n):
            if mask >> i & 1:
                fv ^= fcols[i]
                pv ^= pcols[i]
        if fv and mask.bit_count() + pv.bit_count() < 4:
            return False
    return True


def construct(fcols):
    n = ntypes(fcols)
    r = best_predicted(n)
    if n == 0:
        return 0, [0] * len(fcols)
    options = [p for p in range(1 << r) if p.bit_count() >= 3 and p.bit_count() % 2 == 1]
    assert len(options) == threshold(r)
    lookup = dict(zip(sorted(set(fcols) - {0}), options))
    return r, [lookup.get(z, 0) for z in fcols]


def all_small_functions():
    num = 0
    for k in range(1, 4):
        for fcols in product(range(4), repeat=k):
            predicted = best_predicted(ntypes(fcols))
            # Exhaustively search *all* systematic parity matrices of redundancy below or equal to 4.
            for r in range(0, min(4, predicted) + 1):
                exists = any(delta_at_least_four(fcols, pcols)
                             for pcols in product(range(1 << r), repeat=k))
                assert exists == (r >= predicted), (k, fcols, r, exists, predicted)
            rc, pc = construct(fcols)
            assert rc == predicted and delta_at_least_four(fcols, pc)
            num += 1
    return num


def check_full_projective():
    counts = []
    for s in range(1, 5):
        f = list(range(1, 1 << s))
        r, p = construct(f)
        assert r == (s + 2), (s, r)
        assert delta_at_least_four(f, p)
        counts.append((s, len(f), r, sum(bool(z) for z in p)))
    return counts


def check_matching_bound():
    for r in range(3, 9):
        odds = [x for x in range(1 << r) if x.bit_count() >= 3 and x.bit_count() % 2]
        assert len(odds) == threshold(r)
        assert all((a ^ b).bit_count() >= 2 for i, a in enumerate(odds) for b in odds[i+1:])
        # The fixed-coordinate matching has r fully disallowed pairs (prefix weights 0 and 1).
        forbidden = sum(not ((t.bit_count() >= 3) or ((t | (1 << (r-1))).bit_count() >= 3))
                        for t in range(1 << (r-1)))
        assert forbidden == r


if __name__ == '__main__':
    print('EXHAUSTIVE_SMALL_FUNCTIONS', all_small_functions())
    print('FULL_PROJECTIVE_CASES', check_full_projective())
    check_matching_bound()
    print('MATCHING_BOUND_CHECKED_R_3_TO_8')
    print('VERIFY_OK')
