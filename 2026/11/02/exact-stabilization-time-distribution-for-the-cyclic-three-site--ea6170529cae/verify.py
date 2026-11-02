"""Reproduce the exact finite-ring majority-stabilization formulas.

Uses only the Python standard library. Exhaustive tests are finite checks;
the all-length conclusions follow from the separate mathematical proof.
"""
from itertools import product


def majority_step(x):
    n = len(x)
    return tuple(int(x[(i - 1) % n] + x[i] + x[(i + 1) % n] >= 2)
                 for i in range(n))


def predicted_hitting_time(x):
    """Return -1 for the alternating 2-cycle, otherwise first fixed time."""
    n = len(x)
    walls = [x[i] ^ x[(i + 1) % n] for i in range(n)]
    if all(walls):
        return -1
    if not any(walls):
        return 0
    first_zero = walls.index(0)
    longest = run = 0
    for j in range(1, n + 1):
        if walls[(first_zero + j) % n]:
            run += 1
            longest = max(longest, run)
        else:
            run = 0
    return longest // 2


def log_derivative_coefficients(length_bound, weight, order):
    """Coefficients of -z d/dz log(1-sum_{k=1}^{L+1}u^(k-1) z^k)."""
    c = [0] * (order + 1)
    for n in range(1, order + 1):
        c[n] = sum(weight ** (k - 1) * c[n - k]
                   for k in range(1, min(n - 1, length_bound + 1) + 1))
        if n <= length_bound + 1:
            c[n] += n * weight ** (n - 1)
    return c


def matrix_trace(length_bound, weight, n):
    """Independent small-order finite transfer-matrix trace."""
    d = length_bound + 1
    matrix = [[0] * d for _ in range(d)]
    for j in range(d):
        matrix[j][0] += 1   # a zero closes any current run
        if j < length_bound:
            matrix[j][j + 1] += weight
    power = [[int(i == j) for j in range(d)] for i in range(d)]
    for _ in range(n):
        power = [[sum(power[i][k] * matrix[k][j] for k in range(d))
                  for j in range(d)] for i in range(d)]
    return sum(power[i][i] for i in range(d))


def main():
    for L in range(1, 9):
        for u in (-1, 1):
            series = log_derivative_coefficients(L, u, 14)
            for n in range(1, 15):
                assert matrix_trace(L, u, n) == series[n], (L, u, n)

    for n in range(1, 17):
        buckets = {}
        for x in product((0, 1), repeat=n):
            hit = predicted_hitting_time(x)
            y = x
            if hit == -1:
                assert n % 2 == 0 and majority_step(y) != y
                assert majority_step(majority_step(y)) == y
            else:
                for _ in range(hit):
                    assert majority_step(y) != y, (n, x, hit)
                    y = majority_step(y)
                assert majority_step(y) == y, (n, x, hit)
            buckets[hit] = buckets.get(hit, 0) + 1

        assert buckets.get(-1, 0) == (2 if n % 2 == 0 else 0)
        assert max(k for k in buckets if k >= 0) == (n - 1) // 2
        for t in range((n - 1) // 2 + 1):
            L = 2 * t + 1
            exact = (log_derivative_coefficients(L, 1, n)[n]
                     + log_derivative_coefficients(L, -1, n)[n])
            observed = sum(count for depth, count in buckets.items()
                           if 0 <= depth <= t)
            assert exact == observed, (n, t, exact, observed)
        assert sum(buckets.values()) == 1 << n
    print("VERIFY_OK")


if __name__ == '__main__':
    main()
