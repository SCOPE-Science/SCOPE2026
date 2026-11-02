"""Finite diagnostics for the photonic-path Mpemba crossover.

Run with Python 3.10 or later: python verify.py
Uses only the Python standard library. Infinite-size statements require the
analytic proof and are not certified by these finite tests.
"""
from math import cos, exp, log, log1p, pi, sin


def spectrum(n, rate=1.0):
    theta = pi / (2 * n)
    decay = [4 * rate * sin(k * theta) ** 2 for k in range(n)]
    c = [cos(k * theta) for k in range(n)]
    return theta, decay, c


def quadratic_distances(n, rate, t):
    _, decay, c = spectrum(n, rate)
    h_center = sum(exp(-2 * decay[k] * t) for k in range(2, n, 2))
    h_missing = sum(c[k] ** 2 * exp(-2 * decay[k] * t)
                    for k in range(1, n)) / (n - 1) ** 2
    return h_center, h_missing


def state_and_relative_entropy(n, rate, t):
    theta, decay, c = spectrum(n, rate)
    mean_i = mean_ii = 0.0
    pi_dist, q_dist = [], []
    for j in range(n):
        x = pi * (j + 0.5) / n
        zi = 2 * sum((-1) ** (k // 2) * cos(k * x) * exp(-decay[k] * t)
                     for k in range(2, n, 2))
        zii = -2 / (n - 1) * sum((-1) ** k * c[k] * cos(k * x) * exp(-decay[k] * t)
                                for k in range(1, n))
        pi_dist.append((1 + zi) / n)
        q_dist.append((1 + zii) / n)
        for z, first in ((zi, True), (zii, False)):
            if z <= -1:  # the usual continuous extension at a zero probability
                entropy_piece = -z
            else:
                entropy_piece = (1 + z) * log1p(z) - z
            if first:
                mean_i += entropy_piece / n
            else:
                mean_ii += entropy_piece / n
    return mean_i, mean_ii, pi_dist, q_dist


def reference_time(n, rate):
    theta, decay, c = spectrum(n, rate)
    return log((n - 1) / c[1]) / (decay[2] - decay[1])


def crossing(n, rate=1.0, measure='quadratic'):
    T = reference_time(n, rate)
    def f(t):
        if measure == 'quadratic':
            x, y = quadratic_distances(n, rate, t)
        else:
            x, y, _, _ = state_and_relative_entropy(n, rate, t)
        return x - y
    left = max(0.0, T - 2.0 / rate)
    right = T + 2.0 / rate
    if left == 0 and f(left) <= 0:
        raise AssertionError('expected initial positive sign')
    assert f(left) > 0 and f(right) < 0, (n, measure, f(left), f(right))
    for _ in range(60):
        middle = (left + right) / 2
        if f(middle) > 0:
            left = middle
        else:
            right = middle
    return (left + right) / 2


def test_eigenmodes():
    tests = 0
    for n in (5, 7, 9, 17, 31):
        _, decay, _ = spectrum(n)
        for k in range(n):
            vec = [1.0 / n ** 0.5 if k == 0 else
                   (2.0 / n) ** 0.5 * cos(k * pi * (j + .5) / n)
                   for j in range(n)]
            for j in range(n):
                left = vec[j - 1] if j else vec[0]
                right = vec[j + 1] if j < n - 1 else vec[-1]
                residual = left + right - 2 * vec[j] + decay[k] * vec[j]
                assert abs(residual) < 1e-12
                tests += 1
    return tests


def test_pairing_inequality():
    tests = 0
    for n in range(5, 202, 2):
        _, decay, c = spectrum(n)
        eps = (n - 1) ** -2
        for k in range(2, n - 1, 2):
            de, do = decay[k] - decay[1], decay[k + 1] - decay[1]
            A, B = 1 - eps * c[k] ** 2, eps * c[k + 1] ** 2
            assert A > B and A * de > B * do
            assert do / de <= 8 / 3 + 1e-12
            tests += 3
    return tests


def test_markov_evolution():
    tests = 0
    for n in (5, 9, 15):
        for t in (0.02, 0.3, 1.4):
            h1, h2 = quadratic_distances(n, 0.7, t)
            d1, d2, p, q = state_and_relative_entropy(n, 0.7, t)
            assert min(p) >= -1e-12 and min(q) >= -1e-12
            assert abs(sum(p) - 1) < 1e-12 and abs(sum(q) - 1) < 1e-12
            assert abs(h1 - n / 2 * sum((x - 1 / n) ** 2 for x in p)) < 1e-12
            assert abs(h2 - n / 2 * sum((x - 1 / n) ** 2 for x in q)) < 1e-12
            assert d1 >= -1e-12 and d2 >= -1e-12
            tests += 6
    return tests


def main():
    count = test_eigenmodes() + test_pairing_inequality() + test_markov_evolution()
    target = -1 / (6 * pi * pi)
    print('n  quadratic_minus_reference  KL_minus_quadratic_scaled  leading_coefficient')
    for n in (5, 9, 15, 31, 51, 81, 121, 201):
        T = reference_time(n, 1)
        s = crossing(n, 1, 'quadratic')
        k = crossing(n, 1, 'entropy')
        assert s > 0 and k > 0 and k < s
        print(f'{n:3d} {s-T:+.9f} {(k-s)*n**(1/3):+.9f} {s/(n*n*log(n)):.9f}')
        count += 3
    print(f'limit (dimensionless additive and entropy-shift coefficients): {target:.12f}')
    print(f'limit leading quadratic/logarithmic coefficient: {1/(3*pi*pi):.12f}')
    print(f'finite diagnostic assertions passed: {count}')


if __name__ == '__main__':
    main()
