"""Independent reproducibility checks for planar anisotropic Brownian resetting moments.

Run: python3 verify_moments.py
No external packages are required. Exact rational checks are finite diagnostics;
the proof of the all-order identity is analytical.
"""
from fractions import Fraction
import cmath
import math
import random

checks = 0

def check(condition, description):
    global checks
    assert condition, description
    checks += 1


def generator_moment(n, k, reset, rotation, contrast):
    """Stationary angular-Fourier generator recurrence for the rotated frame."""
    if n == 0:
        return reset / (reset + 4 * rotation * k * k)
    return (4 * n * (2 * n - 1) * contrast
            * generator_moment(n - 1, k + 1, reset, rotation, contrast)
            / (reset + 4 * rotation * k * k))


def ordered_time_moment(n, reset, rotation, contrast):
    """Wick formula and the ordered-exponential angular occupation integral."""
    numerator = Fraction(math.factorial(2 * n)) * (2 * contrast) ** n
    denominator = Fraction(1)
    for j in range(1, n + 1):
        denominator *= reset + 4 * rotation * j * j
    return numerator / denominator


cases = (
    (Fraction(3, 2), Fraction(1, 5), Fraction(3, 4)),
    (Fraction(11, 7), Fraction(0), Fraction(1, 7)),
    (Fraction(7, 9), Fraction(17, 13), Fraction(-9, 10)),
    (Fraction(13, 5), Fraction(31, 17), Fraction(1, 2)),
)
for reset, rotation, contrast in cases:
    for n in range(1, 17):
        check(generator_moment(n, 0, reset, rotation, contrast)
              == ordered_time_moment(n, reset, rotation, contrast),
              'independent exact moment constructions disagree')
    second = ordered_time_moment(1, reset, rotation, contrast)
    fourth = ordered_time_moment(2, reset, rotation, contrast)
    quotient = fourth / second ** 2
    check(quotient == 6 * (reset + 4 * rotation) / (reset + 16 * rotation),
          'fourth/second quotient mismatch')
    recovered = (6 - quotient) / (16 * quotient - 24)
    check(recovered == rotation / reset, 'rotational rate inversion mismatch')

# Full parameter inversion at a nontrivial nonaligned initial angle.
for reset, rotation, parallel, transverse, angle in (
    (1.3, 0.19, 2.7, 0.4, 0.37),
    (2.1, 0.0, 1.2, 0.1, -1.29),
    (1.0, 7.4, 1.11, 0.98, 0.66),
):
    avg = (parallel + transverse) / 2
    contrast = (parallel - transverse) / 2
    second = cmath.exp(2j * angle) * 4 * contrast / (reset + 4 * rotation)
    fourth = (cmath.exp(4j * angle) * 96 * contrast ** 2
              / ((reset + 4 * rotation) * (reset + 16 * rotation)))
    radial_second = 4 * avg / reset
    quotient = fourth / second ** 2
    check(abs(quotient.imag) < 1e-12 and 1.5 < quotient.real <= 6 + 1e-12,
          'physical ratio must be real and in the correct interval')
    q = quotient.real
    g = (6 - q) / (16 * q - 24)
    avg_est = radial_second / 4
    contrast_est = abs(second) * (1 + 4 * g) / 4
    check(abs(g - rotation / reset) < 1e-11, 'rotation inverse failure')
    check(abs(avg_est - avg / reset) < 1e-12, 'isotropic inverse failure')
    check(abs(contrast_est - contrast / reset) < 1e-11,
          'anisotropic inverse failure')
    check(abs(cmath.exp(2j * angle) - second / abs(second)) < 1e-12,
          'orientation phase inverse failure')
    check(abs((avg_est + contrast_est) - parallel / reset) < 1e-11,
          'parallel inverse failure')
    check(abs((avg_est - contrast_est) - transverse / reset) < 1e-11,
          'perpendicular inverse failure')
    check(0 < abs(second) / radial_second < (4 * q - 6) / (3 * q),
          'strict positive-diffusivity feasibility failed')

# Independent randomized Brownian-angle path integration: checks the first
# two ordered-time integrals without employing the moment recurrence.
reset = 1.5
rotation = 0.23
trials = 16000
steps = 96
rng = random.Random(20261030)
sum_i = 0j
sum_i2 = 0j
for _ in range(trials):
    age = rng.expovariate(reset)
    dt = age / steps
    phase = 0.0
    integral = 0j
    angular_step_sd = math.sqrt(2 * rotation * dt)
    for j in range(steps):
        phase += angular_step_sd * rng.gauss(0, 1)
        integral += cmath.exp(2j * phase) * dt
    sum_i += integral
    sum_i2 += integral ** 2
empirical_1 = sum_i / trials
empirical_2 = sum_i2 / trials
truth_1 = 1 / (reset + 4 * rotation)
truth_2 = 2 / ((reset + 4 * rotation) * (reset + 16 * rotation))
check(abs(empirical_1 - truth_1) < 0.035,
      'Brownian path first occupation integral mismatch')
check(abs(empirical_2 - truth_2) < 0.055,
      'Brownian path second occupation integral mismatch')

print(f'PASS: {checks} exact and simulation assertions')
print(f'Independent occupation integrals: empirical={empirical_1}, {empirical_2}')
print(f'Independent occupation integrals: expected={truth_1}, {truth_2}')
