"""Exact finite checks for the sharp weighted-star maximal-function variation theorem.

This is auxiliary reproducibility code. The general theorem is proved analytically.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random


def maximal(x):
    m = len(x) - 1
    avg = sum(x, Q(0)) / (m + 1)
    return [max(x[0], avg)] + [max(x[i], (x[0] + x[i]) / 2, avg) for i in range(1, m + 1)]


def var(x, w):
    return sum((w[i - 1] * abs(x[i] - x[0]) for i in range(1, len(x))), Q(0))


def difference(a, b):
    return [u - v for u, v in zip(a, b)]


def bound(w):
    m = len(w)
    if m == 1:
        return Q(1, 2)
    W = sum(w, Q(0))
    wmin = min(w)
    return 1 + (W - wmin) / ((m + 1) * wmin)


def all_formal_jacobians(m, w):
    """Enumerate even infeasible selector combinations to check column bounds."""
    N = m + 1
    bound_value = bound(w)
    count = 0
    for center_choice, leaves in product((0, 1), product((0, 1, 2), repeat=m)):
        # Center choice 0 selects central sample, 1 selects whole-star mean.
        # Leaf choices 0, 1, 2 select sample, pair average, whole-star mean.
        for j in range(m):
            row_abs_sum = Q(0)
            for i, choice in enumerate(leaves):
                own = Q(1 if i == j else 0) if choice == 0 else (Q(1, 2) if i == j else Q(0)) if choice == 1 else Q(1, N)
                cent = Q(center_choice, N)
                row_abs_sum += w[i] * abs(own - cent)
            assert row_abs_sum <= bound_value * w[j], (m, w, center_choice, leaves, j, row_abs_sum)
            count += 1
    return count


def attaining_pair(w):
    m = len(w)
    idx = w.index(min(w))
    N = m + 1
    if m == 1:
        x = [Q(2), Q(3)]
        y = [Q(2), Q(3) + Q(1, 8)]
    else:
        # g for the high leaf is m-3/2; every other leaf g=-1.
        # Whole-star offset mu=-1/(2N), strictly between -1/2 and 0.
        x = [Q(2)] + [Q(1)] * m
        x[idx + 1] = Q(2) + Q(m) - Q(3, 2)
        y = x.copy()
        y[idx + 1] += Q(1, 8)
    dx = difference(y, x)
    dm = difference(maximal(y), maximal(x))
    assert var(dx, w) > 0
    assert var(dm, w) == bound(w) * var(dx, w), (w, x, y, dm, var(dm, w), bound(w))


def signed_boundary():
    for m in range(2, 9):
        x = [Q(1)] + [Q(0)] * m
        y = [z - 2 for z in x]
        w = [Q(1)] * m
        assert var(difference(x, y), w) == 0
        assert var(difference(maximal([abs(t) for t in x]), maximal([abs(t) for t in y])), w) > 0


def main():
    count = 0
    cases = 0
    random_tests = 0
    rng = Random(130321)
    for m in range(1, 8):
        weights = [[Q(1)] * m, [Q(i + 1) for i in range(m)], [Q(2 ** i) for i in range(m)]]
        if m == 1:
            weights = [[Q(1)], [Q(7, 3)]]
        for w in weights:
            attaining_pair(w)
            cases += 1
            if m >= 2:
                count += all_formal_jacobians(m, w)
            for trial in range(250):
                # Positive inputs with independent arbitrary edge gradients.
                gx = [Q(rng.randrange(-12, 13), 4) for _ in range(m)]
                gy = [Q(rng.randrange(-12, 13), 4) for _ in range(m)]
                a = [Q(10)] + [Q(10) + t for t in gx]
                b = [Q(10)] + [Q(10) + t for t in gy]
                assert min(a + b) >= 0
                denom = var(difference(a, b), w)
                if denom:
                    lhs = var(difference(maximal(a), maximal(b)), w)
                    assert lhs <= bound(w) * denom, (m, w, a, b, lhs, denom, bound(w))
                random_tests += 1
    signed_boundary()
    print('PASS: exact selector-column checks:', count)
    print('PASS: exact attaining pairs:', cases)
    print('PASS: exact-rational random secants:', random_tests)
    print('PASS: signed-input obstruction examples: 7')

if __name__ == '__main__':
    main()
