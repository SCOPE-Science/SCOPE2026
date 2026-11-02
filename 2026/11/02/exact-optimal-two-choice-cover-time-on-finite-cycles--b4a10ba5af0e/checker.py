#!/usr/bin/env python3
"""Exact finite checks of a two-neighbor-choice cycle cover-time identity.

This diagnostic is not a substitute for the analytic all-size proof.
Python 3 standard library only.
"""
from fractions import Fraction as F
from itertools import product


def prediction(k, i):
    if k % 2 == 0:
        m = k // 2
        j = min(i, k - 1 - i)
        return F(2 * (j + 1)) + F(1, 3**m) - F(3**(j + 1), 3**m)
    m = (k - 1) // 2
    j = min(i, k - 1 - i)
    return F(2 * (j + 1)) + F(1, 2 * 3**m) - F(3**(j + 1), 2 * 3**m)


def cover_prediction(n):
    if n % 2:
        m = (n - 1) // 2
        return F(2 * n) - F(9, 2) + F(5, 2 * 3**m)
    m = n // 2
    return F(2 * n) - F(9, 2) + F(9, 2 * 3**m)


def value_fixed_policy(policy):
    """Exact solution for absorbing nearest-neighbor chain on an interval.

    When both offered neighbors differ, policy[i] chooses left (0) or right (1).
    Under replacement this gives a 3/4-1/4 biased step at each vertex.
    The tridiagonal system is solved by exact forward elimination.
    """
    k = len(policy)
    upper = []
    rhs = []
    for i, choice in enumerate(policy):
        p_left = F(3, 4) if choice == 0 else F(1, 4)
        p_right = 1 - p_left
        diag = F(1)
        effective_rhs = F(1)
        if i:
            diag -= p_left * upper[-1]
            effective_rhs += p_left * rhs[-1]
        upper.append(p_right / diag if i < k - 1 else F(0))
        rhs.append(effective_rhs / diag)
    out = [F(0)] * k
    for i in range(k - 1, -1, -1):
        out[i] = rhs[i] + (upper[i] * out[i + 1] if i + 1 < k else 0)
    return out


def run():
    checks = 0
    for k in range(1, 105):
        predicted = [prediction(k, i) for i in range(k)]
        for i, value in enumerate(predicted):
            left = predicted[i - 1] if i else F(0)
            right = predicted[i + 1] if i < k - 1 else F(0)
            assert value == 1 + F(3, 4) * min(left, right) + F(1, 4) * max(left, right), (k, i)
            checks += 1
        assert predicted == predicted[::-1]
        checks += 1
        for i in range((k - 1) // 2):
            assert predicted[i] < predicted[i + 1]
            checks += 1
        chosen = tuple(int((predicted[i-1] if i else F(0)) > (predicted[i+1] if i < k-1 else F(0))) for i in range(k))
        assert value_fixed_policy(chosen) == predicted
        checks += k
    # Exhaustively compare every deterministic memoryless policy, for the full
    # absorbing interval, with the claimed value at every starting point.
    for k in range(1, 10):
        p = [prediction(k, i) for i in range(k)]
        for policy in product((0, 1), repeat=k):
            v = value_fixed_policy(policy)
            for i, val in enumerate(v):
                assert val >= p[i], (k, policy, i, val, p[i])
                checks += 1
    # The full cover time decomposes into one interval-exit stage of each size.
    for n in range(3, 105):
        exact = sum((prediction(k, 0) for k in range(1, n)), F(0))
        assert exact == cover_prediction(n), n
        checks += 1
    print(f'PASS: {checks:,} exact rational assertions; 104 interval lengths, exhaustive memoryless policy checks for k<=9, 102 full cycle sizes.')


if __name__ == '__main__':
    run()
