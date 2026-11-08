"""Exact finite permutation check for record/inversion cross-covariances.

This checker is independent of the conditioning proof. It enumerates every
permutation of order 2 through 8 and compares exact rational statistics.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def cov_local_formula(k, i, j):
    """1-based indices satisfying 1 <= i < j <= n, 1 <= k <= n."""
    if k == i:
        return Fraction(k - 1, 2 * k * (k + 1))
    if k == j:
        return -Fraction(1, 2 * k)
    if i < k < j:
        return -Fraction(1, 2 * k * (k + 1))
    return Fraction(0)


def verify_order(n):
    pairs = [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]
    r_sum = [0] * (n + 1)
    x_sum = {pair: 0 for pair in pairs}
    rx_sum = {(k, i, j): 0 for k in range(1, n + 1) for i, j in pairs}
    total_record_sum = 0
    weighted_inversion_sum = 0
    weighted_cross_sum = 0
    w = {(i, j): i * i + 3 * j for i, j in pairs}
    count = 0
    for pi in permutations(range(n)):
        count += 1
        current_max = -1
        r = [0] * (n + 1)
        for k, value in enumerate(pi, start=1):
            if value > current_max:
                r[k] = 1
                current_max = value
        for k in range(1, n + 1):
            r_sum[k] += r[k]
        tr = sum(r)
        total_record_sum += tr
        weighted = 0
        for i, j in pairs:
            if pi[i - 1] > pi[j - 1]:
                x_sum[(i, j)] += 1
                weighted += w[(i, j)]
                for k in range(1, n + 1):
                    rx_sum[(k, i, j)] += r[k]
        weighted_inversion_sum += weighted
        weighted_cross_sum += weighted * tr

    assert count == factorial(n)
    assertions = 1
    for k in range(1, n + 1):
        for i, j in pairs:
            observed = Fraction(rx_sum[(k, i, j)], count) - Fraction(r_sum[k] * x_sum[(i, j)], count * count)
            assert observed == cov_local_formula(k, i, j), (n, k, i, j, observed)
            assertions += 1
    for i, j in pairs:
        observed = sum((Fraction(rx_sum[(k, i, j)], count) - Fraction(r_sum[k] * x_sum[(i, j)], count * count) for k in range(1, n + 1)), Fraction(0))
        assert observed == -Fraction(1, 2 * i * (i + 1)), (n, i, j, observed)
        assertions += 1
    w_cov = Fraction(weighted_cross_sum, count) - Fraction(total_record_sum * weighted_inversion_sum, count * count)
    predicted = -sum((Fraction(w[(i, j)], 2 * i * (i + 1)) for i, j in pairs), Fraction(0))
    assert w_cov == predicted, (n, w_cov, predicted)
    assertions += 1
    return assertions


def main():
    total_assertions = 0
    for n in range(2, 9):
        a = verify_order(n)
        total_assertions += a
        print(f"n={n}: {a} exact assertions passed")
    print(f"TOTAL: {total_assertions} exact assertions passed")


if __name__ == "__main__":
    main()
