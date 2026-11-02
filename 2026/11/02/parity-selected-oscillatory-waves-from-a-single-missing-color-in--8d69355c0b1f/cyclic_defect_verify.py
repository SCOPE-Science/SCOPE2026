#!/usr/bin/env python3
"""Standalone numerical cross-checks for color-defect waves of cyclic cellular automata.

Usage: python3 cyclic_defect_verify.py
Only standard-library imports. No external files or network access.
"""
from collections import Counter
from itertools import product
from math import comb
import random


def onto(k, n):
    return sum((-1)**j * comb(k, j) * (k-j)**n for j in range(k+1))


def update(q, a, b):
    # Independent vertex-level implementation: detect colors among opposite vertices.
    sa = set(a)
    sb = set(b)
    an = tuple((v+1) % q if (v+1) % q in sb else v for v in a)
    bn = tuple((v+1) % q if (v+1) % q in sa else v for v in b)
    return an, bn


def first_period(q, a, b):
    config = (tuple(a), tuple(b))
    positions = {}
    while config not in positions:
        positions[config] = len(positions)
        config = update(q, *config)
        if len(positions) > 6*q+40:
            raise RuntimeError('unexpectedly long orbit')
    return positions[config], len(positions)-positions[config]


def support_masks(q):
    a = set(range(1, q))
    b = set(range(q))
    while True:
        yield a, b
        a, b = (
            {(c+1)%q if (c+1)%q in b else c for c in a},
            {(c+1)%q if (c+1)%q in a else c for c in b},
        )


def closed_support(q, t):
    k = t // 2
    if t % 2 == 0:
        a = set(range(1, 2*k+2, 2)) | set(range(2*k+2, q))
        b = set(range(0, 2*k, 2)) | set(range(2*k, q))
    else:
        a = set(range(0, 2*k+1, 2)) | set(range(2*k+2, q))
        b = set(range(1, 2*k+2, 2)) | set(range(2*k+2, q))
    return a, b


def target_supports(q):
    if q % 2 == 0:
        e = frozenset(range(0, q, 2))
        o = frozenset(range(1, q, 2))
        return {(e, o), (o, e)}
    odd = set(range(1, q, 2)) | {q-1}
    even = set(range(0, q, 2))
    return {
        (frozenset((x+r) % q for x in aa),
         frozenset((x+r) % q for x in bb))
        for r in range(q)
        for aa, bb in ((even, odd), (odd, even))
    }


def test_induction():
    total = 0
    for q in range(3, 65):
        stop = q - 1 if q % 2 == 0 else q - 2
        flow = support_masks(q)
        for t in range(stop+1):
            assert next(flow) == closed_support(q, t), (q, t)
            total += 1
        a, b = next(flow)
        c, d = next(flow)
        # The two period-2 supports persist and reverse.
        assert (frozenset(a),frozenset(b)) in target_supports(q)
        assert (frozenset(c),frozenset(d)) == (frozenset(b),frozenset(a))
    return total


def test_microscopic():
    rng = random.Random(20261025)
    total = 0
    for q in range(3, 49):
        t_want = q-1 if q%2==0 else q-2
        p_want = q if q%2==0 else q+1
        for missing in range(q):
            for flip in (False, True):
                aa = [x for x in range(q) if x != missing]
                bb = list(range(q))
                for _ in range(2):
                    rng.shuffle(aa)
                    rng.shuffle(bb)
                    a = aa + [rng.randrange(q) for _ in range(rng.randrange(4))]
                    a = a[:len(aa)] + [rng.choice(aa) for _ in range(len(a)-len(aa))]
                    b = bb + [rng.randrange(q) for _ in range(rng.randrange(4))]
                    if flip: a,b = b,a
                    got = first_period(q,a,b)
                    assert got == (t_want,p_want), (q, missing, flip, got)
                    total += 1
    return total


def test_orbit_counts():
    total = 0
    samples = []
    for q, a, b in ((3,3,3),(4,3,3),(5,3,3),(6,3,3),(5,4,3)):
        palettes = target_supports(q)
        m = (q+1)//2
        period = q if q%2==0 else q+1
        support_count = 2 if q%2==0 else 2*q
        target = support_count*onto(m,a)*onto(m,b)
        count = 0
        for aa in product(range(q), repeat=a):
            for bb in product(range(q), repeat=b):
                if (frozenset(aa), frozenset(bb)) in palettes:
                    assert first_period(q, aa, bb) == (0,period)
                    count += 1
                total += 1
        assert count == target,(q,a,b,count,target)
        assert count%period==0
        samples.append((q,a,b,count,count//period))
    return total, samples


def main():
    nind = test_induction()
    nmic = test_microscopic()
    nenum,smps = test_orbit_counts()
    print('SUPPORT_INDUCTION_CASES',nind)
    print('MICRO_DEFECT_EXPERIMENTS',nmic)
    print('COMPLETE_LABELLED_ENUMERATION',nenum)
    for row in smps: print('ALT_STATES_ORBITS',*row)
    print('CYCLIC_DEFECT_PARITY_VERIFY_OK')

if __name__ == '__main__':main()
