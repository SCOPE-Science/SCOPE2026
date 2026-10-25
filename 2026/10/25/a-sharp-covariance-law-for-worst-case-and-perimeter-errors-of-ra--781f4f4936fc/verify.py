"""Deterministic finite checks for the random cyclic-polygon error theorem.

No simulation establishes an asymptotic limit; the theorem requires the proof
in RESULT.md. This script checks exact finite-moment identities and the
finite-n conditional-max integral that drives the covariance constant.
"""
import math


def exponential_poly_moment(coeff):
    return sum(v * math.factorial(k) for k, v in coeff.items())


def polynomial_multiply(a, b):
    c = {}
    for i, x in a.items():
        for j, y in b.items():
            c[i + j] = c.get(i + j, 0) + x * y
    return c


def simpson(f, lo, hi, count=16000):
    assert count % 2 == 0
    h = (hi - lo) / count
    total = f(lo) + f(hi)
    for i in range(1, count):
        total += (4 if i % 2 else 2) * f(lo + i * h)
    return total * h / 3


def max_density(n, m):
    if m <= 0:
        return 0.0
    q = math.exp(-m)
    return n * q * math.exp((n - 1) * math.log1p(-q))


def conditional_psi_sum(n, m):
    if m <= 0:
        return 0.0
    q = math.exp(-m)
    return (m ** 3 - 18 * m + 12
            - (n - 1) * q * (m ** 3 + 3 * m ** 2 - 12 * m) / (1 - q))


def covariance_max_squared_psi_sum(n):
    hi = math.log(n) + 27
    em2 = simpson(lambda m: m * m * max_density(n, m), 0, hi)
    return simpson(lambda m: (m * m - em2)
                   * conditional_psi_sum(n, m) * max_density(n, m), 0, hi)


if __name__ == '__main__':
    psi = {3: 1, 1: -18, 0: 12}
    assert exponential_poly_moment(psi) == 0
    assert exponential_poly_moment(polynomial_multiply(psi, psi)) == 360
    print('exact exponential influence mean=0 and variance=360: PASS')
    print('Cov(M_n^2, sum psi(E_i)) / (2(log n)^4), finite-n quadrature:')
    for n in [100, 1000, 10000]:
        cov = covariance_max_squared_psi_sum(n)
        ratio = cov / (2 * math.log(n) ** 4)
        print(f'n={n:5d}: covariance={cov:.8f}, ratio={ratio:.8f}')
        assert cov > 0 and 0.5 < ratio < 5
    print('finite-n conditional integration: PASS')
