"""Reproducible finite checks for the cyclic Bergman-kernel Gram spectrum.

Uses only Python's standard library. These finite checks are not a proof of
all-degree identities or their limiting consequences.
"""
import cmath
import math


def gram_eigen_closed(n, q):
    Q = q ** n
    scale = n * (1 - q) ** 2 / (1 - Q)
    A = n * Q / (1 - Q)
    return [scale * q ** j * (j + 1 + A) for j in range(n)]


def gram_eigen_direct_dft(n, q):
    omega = cmath.exp(2j * math.pi / n)
    first_row = [(1 - q) ** 2 / (1 - q * omega ** (-b)) ** 2
                 for b in range(n)]
    return [sum(first_row[b] * omega ** (j * b) for b in range(n)).real
            for j in range(n)]


def transition_position(n, q):
    return q / (1 - q) - 1 - n * q ** n / (1 - q ** n)


def limiting_profile(c, x):
    z = math.exp(-c)
    return c * c * math.exp(-c * x) * (x / (1 - z) + z / (1 - z) ** 2)


def run():
    cases = 0
    for n in range(2, 21):
        for q in (0.05, 0.3, 0.6, 0.9, 0.98):
            lambdas = gram_eigen_closed(n, q)
            check = gram_eigen_direct_dft(n, q)
            assert max(abs(a - b) for a, b in zip(lambdas, check)) < 2e-9
            assert lambdas.index(min(lambdas)) == n - 1
            T = transition_position(n, q)
            assert -1 < T < (n - 3) / 2
            if abs(T - round(T)) > 1e-8:
                assert lambdas.index(max(lambdas)) == max(0, math.ceil(T))
            cases += 1
    # Every predicted finite-radius transition is an exact adjacent top tie.
    for n in range(4, 19):
        for k in range(n):
            if not k < (n - 3) / 2:
                break
            low, high = 1e-8, 1 - 1e-7
            for _ in range(70):
                mid = (low + high) / 2
                if transition_position(n, mid) < k:
                    low = mid
                else:
                    high = mid
            q = (low + high) / 2
            eigen = gram_eigen_closed(n, q)
            assert abs(eigen[k] - eigen[k + 1]) < 1e-9
            assert min(eigen[k], eigen[k + 1]) > max(
                [eigen[j] for j in range(n) if j not in (k, k + 1)])
            cases += 1
    for c in (0.1, 0.5, 1.0, 2.0, 4.0, 8.0):
        x_star = 1 / c - 1 / math.expm1(c)
        assert 0 < x_star < 0.5
        kappa = math.expm1(c) / c * math.exp(-1 + c / math.expm1(c))
        for n in (200, 800, 2400):
            q = 1 - c / n
            lambdas = gram_eigen_closed(n, q)
            error = max(abs(y - limiting_profile(c, j / n))
                        for j, y in enumerate(lambdas))
            assert error < 2 * math.exp(c) / n
            assert abs(max(lambdas) / min(lambdas) - kappa) < 2 * math.exp(c) / n
            cases += 1
    print('PASS: {} finite DFT, extrema, and limiting-profile cases'.format(cases))


if __name__ == '__main__':
    run()
