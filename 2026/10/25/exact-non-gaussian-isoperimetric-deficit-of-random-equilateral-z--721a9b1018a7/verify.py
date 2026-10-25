"""Standard-library numerical corroboration of the planar zonogon deficit formulas.

Run: python3 verify.py
This is a finite consistency test, not a substitute for the analytic proof.
"""
import cmath
import math
import random

PI = math.pi
rng = random.Random(20261020)


def area(angles):
    return sum(abs(math.sin(a - b)) for i, a in enumerate(angles)
               for b in angles[i + 1:])


def partial_deficit(angles, cutoff):
    n = len(angles)
    answer = 0.0
    for k in range(1, cutoff + 1):
        real = math.fsum(math.cos(2 * k * a) for a in angles)
        imag = math.fsum(math.sin(2 * k * a) for a in angles)
        answer += (real * real + imag * imag) / (4 * k * k - 1)
    return answer * 2 / (PI * n)


def laplace_closed(s):
    if s < PI / 2:
        x = math.sqrt(1 - 2 * s / PI)
        return x / math.sin(PI * x / 2)
    if s > PI / 2:
        y = math.sqrt(2 * s / PI - 1)
        return y / math.sinh(PI * y / 2)
    return 2 / PI


def laplace_product(s, cutoff):
    return math.exp(-math.fsum(math.log1p(2 * s / (PI * (4 * k * k - 1)))
                               for k in range(1, cutoff + 1)))


cases = [
    (0.0, PI / 2),
    (0.0, PI / 3, 2 * PI / 3),
    (0.0, 0.0, PI / 2, PI / 4),
]
for n in (5, 9, 23):
    cases.append(tuple(rng.random() * PI for _ in range(n)))
for angles in cases:
    n = len(angles)
    deficit = (n * n / PI - area(angles)) / n
    for cutoff in (20, 120, 1600):
        partial = partial_deficit(angles, cutoff)
        # Deterministic bound: |S_{n,k}|^2 <= n^2 and the sum telescopes.
        bound = n / (PI * (2 * cutoff + 1))
        assert -1e-11 < deficit - partial < bound + 1e-11
    assert deficit >= -1e-12

for s in (0.1, 0.7, PI / 2, 1.9, 4.0, 12.0):
    product = laplace_product(s, 50000)
    assert abs(product - laplace_closed(s)) < 0.00008

second_weight_sum = math.fsum(1 / (4 * k * k - 1) ** 2 for k in range(1, 70000))
assert abs(second_weight_sum - (PI * PI - 8) / 16) < 1e-9

tail_factor = math.exp(-math.fsum(math.log1p(-3 / (4 * k * k - 1))
                                   for k in range(2, 70000)))
assert abs(tail_factor - 16 / (3 * PI)) < 0.00005

for n in (5, 12, 24):
    samples = 3200
    measurements = [area([rng.random() * PI for _ in range(n)])
                    for _ in range(samples)]
    mu = n * (n - 1) / PI
    variance = n * (n - 1) / 2 * (0.5 - 4 / PI ** 2)
    avg = math.fsum(measurements) / samples
    empirical_var = math.fsum((v - avg) ** 2 for v in measurements) / samples
    assert abs(avg - mu) < 6 * math.sqrt(variance / samples)
    assert abs(empirical_var / variance - 1) < 0.27

print('VERIFY_OK angular_cases=6 Fourier_cutoffs=3 Laplace_points=6 moments_n=3')
