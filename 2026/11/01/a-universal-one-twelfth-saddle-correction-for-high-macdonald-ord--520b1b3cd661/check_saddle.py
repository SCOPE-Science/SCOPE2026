"""Numerical diagnostic for the exact-saddle Macdonald order-moment law.

Requires Python 3, SciPy and NumPy. The mathematical theorem has an
analytic proof; quadrature is only a reproducible finite-sample check.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import lambertw


def sample(x, n):
    assert x > 0 and n > 0 and n % 2 == 0
    w = float(lambertw(2.0 * n / x).real)
    t = brentq(lambda v: x * v * math.sinh(v) - n, w, w + 2.0,
               xtol=5e-14)
    B = n / t**2 + x * math.cosh(t)
    f3 = 2 * n / t**3 - x * math.sinh(t)
    f4 = -6 * n / t**4 - x * math.cosh(t)
    correction = f4 / (8 * B**2) + 5 * f3**2 / (24 * B**3)

    def centered(u):
        y = t + u / math.sqrt(B)
        if y <= 0:
            return 0.0
        exponent = n * math.log(y / t) - x * (math.cosh(y) - math.cosh(t))
        return math.exp(exponent)

    ratio = quad(centered, -12.0, 12.0, epsabs=2e-12,
                 epsrel=2e-12, limit=250)[0] / math.sqrt(2 * math.pi)
    scaled_remainder = (ratio - 1 - correction) * (n / t)**2
    return t, ratio, correction, scaled_remainder


def main():
    for x in (0.25, 1.0, 3.0, 10.0):
        for n in (60, 200, 600):
            t, ratio, correction, err = sample(x, n)
            assert math.isfinite(ratio) and math.isfinite(err)
            assert abs(err) < 0.08, (x, n, err)
            print(f'x={x:g} n={n:3d} saddle={t:.9f} '
                  f'ratio={ratio:.10f} correction={correction:+.10f} '
                  f'rescaled_remainder={err:+.7f}')
    print('Finite-sample diagnostics: PASS; not a proof of the asymptotic theorem.')


if __name__ == '__main__':
    main()
