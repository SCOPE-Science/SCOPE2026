"""Exact rational checks for the two-opposite-corner cut difference-body theorem.

Run: python verify.py
No third-party dependencies. Finite checks support but never replace the proof.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial


def actual_feasible(w, a, b):
    d = len(w)
    p = sum((max(v, 0) for v in w), F(0))
    q = sum((max(-v, 0) for v in w), F(0))
    S = sum(w, F(0))
    low = max(q, a, a - S)
    high = min(d - p, d - b, d - b - S)
    return low <= high


def predicted_feasible(w, a, b):
    return all(-1 <= v <= 1 for v in w) and abs(sum(w, F(0))) <= len(w) - a - b


def volumes(d, a, b):
    s = a + b
    return 1 - (a**d + b**d) / factorial(d), 2**d - 2*s**d / factorial(d)


def test():
    count = 0
    half = (F(-1), F(-1, 2), F(0), F(1, 2), F(1))
    ab = (F(0), F(1, 2), F(1))
    for d in (3, 4, 5):
        for a, b in product(ab, repeat=2):
            for w in product(half, repeat=d):
                assert actual_feasible(w, a, b) == predicted_feasible(w, a, b), (d, a, b, w)
                count += 1
    ratio_checks = 0
    for d in range(3, 14):
        for s in (F(1, 3), F(1), F(5, 3)):
            lo, hi = max(F(0), s - 1), min(F(1), s)
            mid = s / 2
            prev = F(0)
            for i in range(9):
                a = mid + (hi - mid) * F(i, 8)
                b = s - a
                v, vb = volumes(d, a, b)
                R = vb / v
                assert R >= 2**d
                if i:
                    assert R > prev, (d, s, i)
                else:
                    assert R == 2**d
                prev = R
                # The two opposite cut allocations have the same exact difference-body volume.
                _, vb2 = volumes(d, b, a)
                assert vb == vb2
                ratio_checks += 1
    print(f"EXACT_FEASIBILITY_OK samples={count} dimensions=3..5")
    print(f"EXACT_VOLUME_RATIO_OK samples={ratio_checks} dimensions=3..13")


if __name__ == "__main__":
    test()
