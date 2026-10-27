"""Exact finite checks for two-candidate threshold-report welfare distortion.

This program corroborates the algebraic proof; finite checks do not prove the
all-threshold, all-electorate theorem.
"""
from fractions import Fraction as Q
from itertools import combinations, product


def cells(thresholds):
    cuts = sorted({Q(0), Q(1), *thresholds, *(1 - x for x in thresholds)})
    return tuple(zip(cuts, cuts[1:]))


def maximum_width(intervals):
    return max(hi - lo for lo, hi in intervals)


def pointwise_distortion(intervals):
    n = len(intervals)
    L = sum((x for x, _ in intervals), Q(0)) / n
    U = sum((y for _, y in intervals), Q(0)) / n
    loss_A = max(Q(1), (1 - L) / L) if L else None
    loss_B = max(Q(1), U / (1 - U)) if U < 1 else None
    if loss_A is None:
        return loss_B
    if loss_B is None:
        return loss_A
    return min(loss_A, loss_B)


def midpoint_rule_distortion(intervals):
    n = len(intervals)
    L = sum((x for x, _ in intervals), Q(0)) / n
    U = sum((y for _, y in intervals), Q(0)) / n
    if L + U >= 1:
        return max(Q(1), (1 - L) / L)
    return max(Q(1), U / (1 - U))


def check_thresholds(thresholds):
    I = cells(thresholds)
    w = maximum_width(I)
    R = (1 + w) / (1 - w)
    checks = 0
    for n in (1, 2, 3):
        for indices in product(range(len(I)), repeat=n):
            profile = tuple(I[j] for j in indices)
            assert pointwise_distortion(profile) <= R
            assert midpoint_rule_distortion(profile) <= R
            checks += 2
    longest = next((lo, hi) for lo, hi in I if hi - lo == w)
    mirror = (1 - longest[1], 1 - longest[0])
    assert mirror in I
    assert pointwise_distortion((longest, mirror)) == R
    assert midpoint_rule_distortion((longest, mirror)) == R
    return checks + 2


def main():
    checked = 0
    vectors = 0
    for t in (1, 2, 3):
        for vec in combinations([Q(j, 10) for j in range(1, 10)], t):
            checked += check_thresholds(vec)
            vectors += 1
    for t in range(1, 9):
        perfect_cuts = [Q(j, 2*t+1) for j in range(1, 2*t+1)]
        for orientations in product((False, True), repeat=t):
            thresholds = tuple(perfect_cuts[j if flag else 2*t-j-1] for j,flag in enumerate(orientations))
            I = cells(thresholds)
            assert len(I) == 2*t+1
            assert maximum_width(I) == Q(1, 2*t+1)
            assert (1 + maximum_width(I))/(1-maximum_width(I)) == 1 + Q(1,t)
            checked += 3
            vectors += 1
    print(f"PASS: {vectors} threshold vectors; {checked} exact-rational assertions.")


if __name__ == '__main__':
    main()
