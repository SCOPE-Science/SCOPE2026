"""Independent finite-parameter checks for an asymmetric telegraph stopping-time law.

Requires scipy and numpy. Numerical checks do not replace the analytic proof.
"""
from math import exp, sqrt, isclose
from scipy.integrate import quad
from scipy.special import iv


def check(a, b, cp, cm, x, s):
    h, k, d = cp + cm, cp * cm, cp - cm
    eta = 2 * b * sqrt(k) / h
    sign = 1 if x > 0 else -1
    speed = cp if sign == 1 else cm
    r, q = abs(x), a + s
    delta = sqrt((q + b)**2 - eta**2)
    zeta = (h * delta - sign * d * (q + b)) / (2 * k)
    amp = (1 / (2 * speed)
           + h / (4 * k) * ((q + b) / delta - 1)
           + b / (h * delta))
    resolvent = a * amp * exp(-r * zeta)

    # Independent formula: the asymmetric fixed-time telegraph Bessel kernel,
    # with its no-switch ballistic atom, integrated against exponential killing.
    def fixed_time_density(t):
        xi0 = (x + cm * t) / h
        xi1 = (cp * t - x) / h
        if xi0 < 0 or xi1 < 0:
            return 0.
        product = max(0., xi0 * xi1)
        zz = 2 * b * sqrt(product)
        correction = (t / (2 * sqrt(product)) * iv(1, zz)
                      if product > 1e-14 else b * t / 2)
        return b * exp(-b * t) / h * (iv(0, zz) + correction)

    ballistic_time = r / speed
    ballistic = a / (2 * speed) * exp(-(a + b + s) * ballistic_time)
    integrated = ballistic + quad(
        lambda t: a * exp(-(a + s) * t) * fixed_time_density(t),
        ballistic_time, 75, epsabs=2e-12, epsrel=2e-11
    )[0]
    assert isclose(resolvent, integrated, rel_tol=2e-8, abs_tol=2e-10), (
        a, b, cp, cm, x, s, resolvent, integrated)

    # A(q) is a positive Laplace transform with an explicitly positive density.
    continuous = quad(
        lambda t: exp(-(q + b) * t) * (
            h * eta / (4 * k) * iv(1, eta * t) + b / h * iv(0, eta * t)),
        0, 60, epsabs=5e-11
    )[0]
    assert isclose(amp, 1 / (2 * speed) + continuous,
                   rel_tol=2e-8, abs_tol=2e-10)

    # Compound-Poisson jump intensity follows from integration of the Levy density.
    def nu(t):
        return h * eta / (2 * k) * exp(-(a + b) * t) * iv(1, eta * t) / t
    total = quad(nu, 0, 60, epsabs=5e-11)[0]
    intensity = h / (2 * k) * ((a + b) - sqrt((a + b)**2 - eta**2))
    assert isclose(total, intensity, rel_tol=2e-8, abs_tol=2e-10)

    # The exact derivative of the spatial exponent is consistent with the
    # drift-plus-jumps Laplace exponent.
    base_delta = sqrt((a + b)**2 - eta**2)
    base_zeta = (h * base_delta - sign * d * (a + b)) / (2 * k)
    spatial_exponent = zeta - base_zeta
    compound_exponent = s / speed + quad(
        lambda t: -__import__('math').expm1(-s * t) * nu(t),
        0, 60, epsabs=5e-11
    )[0]
    assert isclose(spatial_exponent, compound_exponent,
                   rel_tol=2e-8, abs_tol=2e-10)
    return 4


def main():
    assertions = 0
    cases = [(0.8, 1.2, 1.5, 0.5),
             (1.7, 0.25, 0.5, 2.0),
             (0.3, 1.1, 2.1, 0.9),
             (1.0, 1.0, 2.0, 2.0)]
    for a, b, cp, cm in cases:
        for x in (-1.0, -0.2, 0.2, 1.0):
            for s in (0., 0.2, 0.6, 2.0):
                assertions += check(a, b, cp, cm, x, s)
    print(f'{assertions} independent numerical assertions passed')


if __name__ == '__main__':
    main()
