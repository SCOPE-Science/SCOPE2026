#!/usr/bin/env python3
"""Exact independent enumeration for a two-center fair-allocation criterion.

Four agents, allocated in order A,B | C,D. A,B,C value each good 1;
D values each good epsilon. Centers use realized own welfare and
optimal item reassignment to their own agents when evaluating rivals.
"""
from fractions import Fraction
from itertools import product


def predicted(m):
    assert m >= 4
    q, r = divmod(m, 4)
    if r == 0:
        return Fraction(q - 1, q)
    if r == 1:
        return max(Fraction(0), Fraction(q - 2, q))
    if r == 2:
        return Fraction(q - 1, q)
    return Fraction(q - 1, q + 1)


def exhaustive(m, eps):
    # Exclude no allocations; the count vector represents each labeling
    # because all goods are identical in every agent's valuation.
    weights = (Fraction(1), Fraction(1), Fraction(1), eps)
    good = []
    for a in range(m + 1):
        for b in range(m - a + 1):
            for c in range(m - a - b + 1):
                d = m - a - b - c
                x = (a, b, c, d)
                # For positive constant per-good valuations, any EF1
                # allocation must have all bundle counts within one.
                if max(x) - min(x) > 1:
                    continue
                # Direct individual-level inter-EF1 inequalities.
                if not all(weights[i] * x[i] >= weights[i] * max(x[j] - 1, 0)
                           for i in range(4) for j in range(4)):
                    continue
                # A,B form center 1; C,D form center 2.
                # The rival's goods can all go to a unit-value agent
                # in the observing center after removal of one good.
                own_1 = a + b
                own_2 = Fraction(c) + eps * d
                rival_2_after_removal = max(c + d - 1, 0)
                rival_1_after_removal = max(a + b - 1, 0)
                if own_1 >= rival_2_after_removal and own_2 >= rival_1_after_removal:
                    good.append(x)
    return good


def verify():
    samples = [Fraction(1, 100), Fraction(1, 10), Fraction(1, 4),
               Fraction(1, 3), Fraction(2, 5), Fraction(1, 2),
               Fraction(3, 5), Fraction(2, 3), Fraction(3, 4),
               Fraction(4, 5), Fraction(9, 10), Fraction(99, 100)]
    checked = 0
    for m in range(4, 81):
        threshold = predicted(m)
        samples_for_m = set(samples + [threshold])
        # Include rational points immediately either side of a positive
        # predicted threshold, and exact boundary when <1.
        for h in [threshold-Fraction(1, 1000), threshold+Fraction(1, 1000)]:
            if Fraction(0) < h < Fraction(1):
                samples_for_m.add(h)
        for e in samples_for_m:
            if not (0 < e < 1):
                continue
            witnesses = exhaustive(m, e)
            want = e >= threshold
            assert bool(witnesses) == want, (m, e, threshold, witnesses[:2])
            checked += 1
    # Explicit nonmonotonic existence at fixed epsilon.
    assert not exhaustive(8, Fraction(1, 4))
    assert exhaustive(9, Fraction(1, 4))
    assert not exhaustive(10, Fraction(1, 4))
    assert not exhaustive(11, Fraction(1, 4))
    assert exhaustive(11, Fraction(1, 3))
    assert not exhaustive(12, Fraction(1, 2))
    assert exhaustive(12, Fraction(2, 3))
    # For m < 8, this family always has a solution at positive eps.
    for m in range(4, 8):
        assert exhaustive(m, Fraction(1, 10**8))
    # Among eight goods with one discounted agent, epsilon=1/2
    # is the precise feasibility boundary.
    assert not exhaustive(8, Fraction(499, 1000))
    assert exhaustive(8, Fraction(1, 2))
    print(f'PASS: {checked} independent exact-rational m/epsilon instances, m=4..80; 12 boundary checks')
    for m in range(4, 17):
        print(f'm={m}: epsilon_min={predicted(m)}; example={exhaustive(m, max(Fraction(1,1000),predicted(m)))[:1]}')

if __name__ == '__main__':
    verify()
