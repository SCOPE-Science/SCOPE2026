"""Exact-rational checks of the idealized log-determinant allocation theorem."""
from fractions import Fraction as Q
from random import Random


def profile(weights, B, m):
    """Return exact MSEs and increasing block masses for descending weights."""
    n = len(weights)
    assert n >= B >= 2 * m >= 2
    assert all(weights[i] >= weights[i + 1] >= 0 for i in range(n - 1))
    K = B // m
    values = [2 * sum(weights[B - m * j :], Q(0)) / j
              for j in range(1, K + 1)]
    blocks = [sum(weights[B - m * j : B - m * (j - 1)], Q(0))
              for j in range(1, K + 1)]
    return values, blocks


def check_case(weights, B, m):
    f, c = profile(weights, B, m)
    K = len(f)
    assert all(c[i] <= c[i + 1] for i in range(K - 1))
    t = [sum(weights[B - m * j :], Q(0)) for j in range(1, K + 1)]
    H = [j * c[j] - t[j - 1] for j in range(1, K)]
    for j in range(1, K):
        assert f[j] - f[j - 1] == 2 * H[j - 1] / (j * (j + 1))
    for j in range(K - 2):
        assert H[j + 1] - H[j] == (j + 2) * (c[j + 2] - c[j + 1])
    index = next((j for j in range(1, K) if H[j - 1] >= 0), K)
    assert f[index - 1] == min(f)
    assert (f[0] == min(f)) == (K == 1 or H[0] >= 0)
    assert (f[0] < min(f[1:])) == (K == 1 or H[0] > 0)
    assert all(not (f[j] < f[j + 1] > f[j + 2]) for j in range(K - 2))
    return K


def test():
    rng = Random(260105778)
    count = 0
    tests = 0
    for n in range(4, 24):
        for m in range(1, n // 2 + 1):
            for B in range(2 * m, n + 1):
                for _ in range(3):
                    seq = sorted((Q(rng.randrange(0, 25), 1) for _ in range(n)), reverse=True)
                    count += check_case(seq, B, m)
                    tests += 1
    # Explicit all-equal and all-zero degenerate plateaus.
    for a in [0, 1, 3]:
        for n in [8, 16]:
            for m in [1, 2, 3]:
                for B in [2 * m, n]:
                    if B <= n:
                        count += check_case([Q(a)] * n, B, m)
                        tests += 1
    # Geometric exact finite-N threshold and limiting-geometry formula.
    geom = 0
    for q in [Q(1, 10), Q(1, 3), Q(1, 2), Q(2, 3), Q(3, 4), Q(9, 10)]:
        for m in [1, 2, 3]:
            for B in [2 * m, 4 * m]:
                for n in [B, B + 1, B + 12]:
                    w = [q ** i for i in range(n)]
                    f, c = profile(w, B, m)
                    # The sharp one-probe boundary for q^{i-1}.
                    assert (f[0] <= min(f)) == (q ** (-m) + q ** (n - B + m) >= 2)
                    for j in range(1, B // m):
                        sign = q ** (-m * j) * (j * (q ** (-m) - 1) - 1) + q ** (n - B)
                        assert (f[j] >= f[j - 1]) == (sign >= 0)
                    geom += 1
    print(f'VERIFY_OK exact_rational_allocation_cases={tests} checked_probe_values={count} geometric_cases={geom}')

if __name__ == '__main__':
    test()
