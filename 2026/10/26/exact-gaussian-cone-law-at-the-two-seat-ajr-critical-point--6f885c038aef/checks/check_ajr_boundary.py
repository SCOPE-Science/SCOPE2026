"""Reproducibility checks for the three-candidate AJR critical boundary."""
from fractions import Fraction
from itertools import product
from math import ceil, comb, asin, pi

BALLOTS = list(range(8))

def approve(ballot, c):
    return (ballot >> c) & 1

def exact_ajr(ballots, omitted):
    n = len(ballots)
    elected = [c for c in range(3) if c != omitted]
    for ell in (1, 2):
        for mask in range(1, 1 << n):
            ids = [i for i in range(n) if (mask >> i) & 1]
            if len(ids) * 2 < ell * n:
                continue
            common = sum(all(approve(ballots[i], c) for i in ids) for c in range(3))
            if common < ell:
                continue
            total = sum(approve(ballots[i], c) for i in ids for c in elected)
            if total < ell * len(ids):
                return False
    return True

def approximate_failure(ballots, omitted):
    n = len(ballots)
    q = ceil(n / 2)
    supports = [b for b in ballots if approve(b, omitted)]
    other = [c for c in range(3) if c != omitted]
    low_count = sum(sum(approve(b, c) for c in other) <= 1 for b in supports)
    L = sum(2 - sum(approve(b, c) for c in other) for b in supports)
    return len(supports) >= q and L > q, low_count >= q

def moments():
    z = []
    for b in BALLOTS:
        bvec = [approve(b, c) for c in range(3)]
        vals = [bvec[c] - Fraction(1, 2) for c in range(3)]
        vals.extend(bvec[c] * (2 - sum(bvec[d] for d in range(3) if d != c)) - Fraction(1, 2) for c in range(3))
        z.append(vals)
    covariance = [[sum(x[i] * x[j] for x in z) / 8 for j in range(6)] for i in range(6)]
    expected = [[Fraction((2 if i == j else 0), 8) if i < 3 and j < 3 else
                 Fraction((3 if (i % 3) == (j % 3) else 0) - 1, 8) if (i < 3) != (j < 3) else
                 Fraction((5 if i == j else 0) - 1, 8)
                 for j in range(6)] for i in range(6)]
    assert covariance == expected
    assert covariance[0][3] == Fraction(1, 4)
    assert covariance[3][3] == Fraction(1, 2)
    print('Six-dimensional covariance verified exactly over eight equally likely ballots.')
    print('Single-committee limiting success: 5/8 =', Fraction(5, 8))

def finite_profiles():
    for n in (2, 3, 4):
        exceptional = 0
        mismatches_outside = 0
        for ballots in product(BALLOTS, repeat=n):
            flags = [approximate_failure(ballots, c) for c in range(3)]
            exceptional_here = any(flag[1] for flag in flags) or all(approve(b, a) and approve(b, d) for b in ballots for a, d in [(0, 1)])
            # Separately test whether some cohesive two-candidate intersection exists.
            pair_event = any(all(approve(b, a) and approve(b, d) for b in ballots) for a, d in ((0, 1), (0, 2), (1, 2)))
            if exceptional_here or pair_event:
                exceptional += 1
            if not (any(flag[1] for flag in flags) or pair_event):
                approx_pass = any(not flag[0] for flag in flags)
                actual_pass = any(exact_ajr(ballots, c) for c in range(3))
                assert approx_pass == actual_pass
                mismatches_outside += 1
        print('n=', n, 'checked', 8 ** n, 'profiles, good-event matches=', mismatches_outside, 'exceptional=', exceptional)

if __name__ == '__main__':
    moments()
    finite_profiles()
