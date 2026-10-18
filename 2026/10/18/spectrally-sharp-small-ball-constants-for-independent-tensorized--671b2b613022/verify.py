"""Reproduce selected special cases of the Gaussian tensor-probe small-ball theorem.

The proof of the general limiting laws is analytic and does not rely on these checks.
Execute: python verify.py (requires scipy >= 1.10).
"""
from math import pi, sqrt, gamma, log, exp
from scipy.integrate import quad
from scipy.special import k0, iti0k0


def volume_ball(d):
    return pi ** (d / 2) / gamma(1 + d / 2)


def origin_density(singular_values):
    return quad(
        lambda t: 1 / pi / __import__('math').prod(
            (1 + (s * t) ** 2) ** 0.5 for s in singular_values
        ), 0, float('inf'), epsabs=3e-12, epsrel=3e-12
    )[0]


def flat_rank_density(r):
    return gamma((r - 1) / 2) / (2 * sqrt(pi) * gamma(r / 2))


def small_ball_constant(singular_values, probes):
    norm = sqrt(sum(s * s for s in singular_values))
    return volume_ball(probes) * (sqrt(probes) * norm * origin_density(singular_values)) ** probes


def laplace_disk_probability(radius):
    # Two independent unit-scale Laplace variables; polar-coordinate quadrature.
    def radial_integral(theta):
        import math
        a = math.cos(theta) + math.sin(theta)
        return -math.expm1(-a * radius) / (a * a) - radius * math.exp(-a * radius) / a
    return quad(radial_integral, 0, pi / 2, epsabs=1e-14)[0]


def product_normal_abs_probability(radius):
    # Product density K_0(|x|)/pi, integrated symmetrically.
    return (2 / pi) * quad(lambda t: k0(t), 0, radius, epsabs=1e-12)[0]


def two_product_norm_probability(radius):
    # Two independent product-normal variables; exact 1D nested integral.
    def integrand(x):
        import math
        boundary = math.sqrt(max(0, radius * radius - x * x))
        return k0(x) * iti0k0(boundary)[1]
    return (4 / pi**2) * quad(integrand, 0, radius, epsabs=2e-12, limit=250)[0]


def verify():
    checks = 0
    for r in range(2, 9):
        exact = flat_rank_density(r)
        numerical = origin_density([1] * r)
        assert abs(numerical - exact) < 3e-9, (r, numerical, exact)
        checks += 1
    for probes in range(1, 7):
        rank2_constant = small_ball_constant([1, 1], probes)
        exact = volume_ball(probes) * (probes / 2) ** (probes / 2)
        assert abs(rank2_constant - exact) < 1e-10
        rank1_coeff = probes ** (probes / 2) / (pi ** (probes / 2) * gamma(1 + probes / 2))
        assert rank1_coeff > 0
        checks += 2
    # Flat spectra uniquely minimize the origin density at each fixed rank.
    for r in range(2, 7):
        flat = [1.0] * r
        skewed = [1.35] + [sqrt((r - 1.35**2) / (r - 1))] * (r - 1)
        assert sum(t*t for t in skewed) > 0
        assert origin_density(skewed) > origin_density(flat), (r, skewed)
        assert sqrt(r) * origin_density(flat) > 1 / sqrt(2*pi)
        checks += 2
    # For two independent unit Laplace probes and M=I_2, radius is 2/tau.
    for tau in (100, 500, 2000):
        p = laplace_disk_probability(2 / tau)
        ratio = p * tau * tau / pi
        assert abs(ratio - 1) < 3 / tau, (tau, ratio)
        checks += 1
    for tau in (1000, 10000, 100000):
        p = product_normal_abs_probability(1 / tau)
        predicted = (2 / pi) * log(tau) / tau
        assert 1.0 < p / predicted < 1.2, (tau, p / predicted)
        checks += 1
    # Log-squared behavior: the ratio converges slowly at rate 1/log(tau).
    for tau in (1000, 10000, 100000):
        p = two_product_norm_probability(sqrt(2) / tau)
        predicted = (2 / pi) * (log(tau) ** 2) / (tau ** 2)
        assert 1.0 < p / predicted < 1.55, (tau, p / predicted)
        checks += 1
    print(f"PASS: {checks} scalar density, constant, and small-ball checks")
    for tau in (1000, 10000, 100000):
        print(f"rank-one, two-probe ratio at tau={tau}: {two_product_norm_probability(sqrt(2)/tau) / ((2/pi)*log(tau)**2/tau**2):.8f}")

if __name__ == '__main__':
    verify()
