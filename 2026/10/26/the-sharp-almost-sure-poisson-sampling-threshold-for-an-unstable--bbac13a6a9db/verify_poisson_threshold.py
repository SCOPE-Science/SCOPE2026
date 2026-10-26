"""Reproducible checks for a scalar Poisson-sampled feedback threshold.

This script tests finite identities and numerically evaluates an integral. It does
not replace the analytic proof of the sharp all-parameter classification.
"""
import math
import random
from fractions import Fraction

from scipy.integrate import quad
from scipy.special import digamma

EULER_GAMMA = 0.5772156649015328606065120900824


def log_multiplier(alpha, theta):
    """E log |M| for Exp(alpha*a) intersample times and a>0."""
    assert alpha > 0 and 0 < theta < 1
    head = theta**alpha * (1 / alpha - EULER_GAMMA - digamma(alpha + 1))
    integral, _ = quad(
        lambda z: z ** (-alpha - 1) * math.log1p(-z),
        theta,
        1,
        epsabs=2e-11,
        epsrel=2e-11,
        limit=250,
    )
    return -math.log1p(-theta) + head + alpha * theta**alpha * integral


def direct_log_multiplier(alpha, theta):
    left, _ = quad(
        lambda y: alpha * y ** (alpha - 1) * math.log(theta / y - 1),
        0,
        theta,
        epsabs=1e-10,
        limit=250,
    )
    right, _ = quad(
        lambda y: alpha * y ** (alpha - 1) * math.log1p(-theta / y),
        theta,
        1,
        epsabs=1e-10,
        limit=250,
    )
    return -math.log1p(-theta) + left + right


def second_moment(alpha, theta):
    if alpha <= 2:
        return math.inf
    s = theta / (1 - theta)
    ev = 1 / (alpha - 1)
    ev2 = 2 / ((alpha - 1) * (alpha - 2))
    return 1 - 2 * s * ev + s * s * ev2


# Rational exact check of the sampling multiplier at integer holding multipliers.
for a, k, eh in [(Fraction(1, 1), Fraction(3, 2), Fraction(2, 1)),
                 (Fraction(2, 1), Fraction(5, 1), Fraction(4, 1)),
                 (Fraction(3, 1), Fraction(7, 2), Fraction(9, 1))]:
    theta = (k - a) / k
    m_original = k / a + (1 - k / a) * eh
    m_beta = (1 / eh - theta) / ((1 - theta) / eh)
    assert m_original == m_beta

# Two independently implemented integrals agree at interior parameter points.
checks = 0
for alpha in [0.25, 0.5, 0.75, 1.0, 1.25, 2.0, 3.0]:
    for theta in [0.001, 0.017, 0.12]:
        f = log_multiplier(alpha, theta)
        g = direct_log_multiplier(alpha, theta)
        assert abs(f - g) < 1e-7, (alpha, theta, f, g)
        checks += 1

# Critical-half law has an independent elementary closed form.
for theta in [0.001, 0.01, 0.1, 0.3, 0.6]:
    s = math.sqrt(theta)
    exact = s * math.log((1 + s) / (1 - s))
    assert abs(log_multiplier(0.5, theta) - exact) < 2e-9
    assert exact > 0

# At alpha=1 the singular integral simplifies to an exact elementary law.
for theta in [0.001, 0.1, 0.3, 0.6]:
    exact = theta * math.log(theta / (1 - theta))
    assert abs(log_multiplier(1.0, theta) - exact) < 1e-9

# Positive exponents below the threshold and negative above it.
for alpha in [0.25, 0.4, 0.5]:
    assert all(log_multiplier(alpha, theta) > 0 for theta in [0.001, 0.01, 0.1])
for alpha in [0.55, 0.75, 1.0, 1.25, 2.0, 3.0]:
    assert log_multiplier(alpha, 1e-4) < 0

# Singular small-theta coefficients at two noncritical alphas.
for alpha in [0.25, 0.75]:
    coeff = math.pi / math.tan(math.pi * alpha)
    observed = log_multiplier(alpha, 1e-7) / (1e-7 ** alpha)
    assert abs(observed - coeff) < 0.08, (alpha, observed, coeff)

# Above alpha 2, the exact second-moment minimizing gain is k=lambda/2.
for alpha in [2.5, 3.0, 5.0, 10.0]:
    theta = 1 - 2 / alpha
    optimal_q = alpha / (2 * (alpha - 1))
    assert abs(second_moment(alpha, theta) - optimal_q) < 1e-12
    for offset in [-0.01, 0.01]:
        trial = theta + offset
        if 0 < trial < 1:
            assert second_moment(alpha, trial) > optimal_q

# Sampled-trajectory SLLN check is only illustrative (not a proof).
rng = random.Random(1772)
a, alpha, theta = 1.0, 0.75, 0.1
n = 80000
h = [rng.expovariate(alpha * a) for _ in range(n)]
log_gains = [math.log(abs((math.exp(-a * q) - theta) /
                          ((1 - theta) * math.exp(-a * q)))) for q in h]
empirical = sum(log_gains) / sum(h)
predicted = alpha * a * log_multiplier(alpha, theta)
assert abs(empirical - predicted) < 0.03, (empirical, predicted)
print(f"VERIFY_OK: 3 exact rational identities; {checks} split-integral checks; "
      "critical and transition tests; moment-optimality checks; "
      "one illustrative sample-path convergence check")
