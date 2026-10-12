"""Reproduce finite consistency checks for the sharp two-link SCP envelope.

The infinite-law theorem rests on the analytic projection proof, not these tests.
Run using: python3 verify.py
"""
import math
import random
from fractions import Fraction as Q


def lower_envelope(v):
    if not 0 <= v <= 0.25:
        raise ValueError('variance outside the admissible interval')
    return (0.5 - math.sqrt(v / 3.0) if v <= 1.0 / 12.0
            else 7.0 / 16.0 - 1.5 * v + 3.0 * v * v)


def expectation_min(atoms):
    return sum(w * z * min(x, y) for x, w in atoms for y, z in atoms)


checks = 0
# All rational large-variance candidate moments and mean-minimum laws.
for v in (Q(1, 12), Q(1, 10), Q(1, 8), Q(1, 6), Q(1, 5), Q(1, 4)):
    a = 3 * v - Q(1, 4)
    b = 1 - 2 * a
    # This is the actual mixed distribution: endpoint atoms a each and uniform density b.
    # Moment calculations are performed as exact rational integrals.
    mu = a + b / 2
    second = a + b / 3
    q_integral = a * a + a * b + b * b / 3
    claimed = Q(7, 16) - Q(3, 2) * v + 3 * v * v
    assert mu == Q(1, 2)
    assert second - mu * mu == v
    assert q_integral == claimed
    checks += 4

# All rational widths in the interior-uniform regime.
for width in (Q(1, 16), Q(1, 10), Q(1, 5), Q(1, 2), Q(3, 4), Q(1)):
    lo = (1 - width) / 2
    hi = (1 + width) / 2
    mu = (lo + hi) / 2
    var = width * width / 12
    # Integral of F**2 equals width/3 plus 1-hi from the saturated tail.
    q_integral = width / 3 + (1 - hi)
    assert mu == Q(1, 2)
    assert var <= Q(1, 12)
    assert q_integral == Q(1, 2) - width / 6
    assert abs(float(q_integral) - lower_envelope(float(var))) < 1e-14
    checks += 4

# Boundary uniqueness and matching of branches.
assert lower_envelope(0.0) == 0.5
assert abs(lower_envelope(1 / 12) - 1 / 3) < 1e-14
assert lower_envelope(0.25) == 0.25
checks += 3

# Finite independent tests of the universal inequality on random discrete SCP laws.
rng = random.Random(20261009)
for _ in range(16000):
    x = rng.random() / 2
    y = rng.random() / 2
    wt = rng.random()
    # A symmetric five-point distribution has exact mean one half.
    atoms = [(0.5 - x, wt / 2), (0.5 + x, wt / 2),
             (0.5 - y, (1 - wt) / 2), (0.5 + y, (1 - wt) / 2)]
    v = wt * x * x + (1 - wt) * y * y
    assert expectation_min(atoms) + 2e-13 >= lower_envelope(v)
    checks += 1

# Unsymmetrical laws with enforced mean one half provide additional tests.
for _ in range(10000):
    x = rng.random() * 0.49
    y = 0.51 + 0.49 * rng.random()
    # Take x and y with the unique weights that force mean exactly one half;
    # mix an independent atom at one half at random intensity.
    mass = rng.random()
    wx = mass * (y - 0.5) / (y - x)
    wy = mass * (0.5 - x) / (y - x)
    atoms = [(x, wx), (y, wy), (0.5, 1 - mass)]
    mu = sum(z * w for z, w in atoms)
    var = sum(w * (z - 0.5)**2 for z, w in atoms)
    assert abs(mu - 0.5) < 1e-12
    assert expectation_min(atoms) + 2e-13 >= lower_envelope(var)
    checks += 2

# The triangular bond threshold crosses the first branch strictly before 1/12.
tau = 2 * math.sin(math.pi / 18)
vcritical = 3 * (0.5 - tau)**2
assert 0 < vcritical < 1 / 12
assert abs(lower_envelope(vcritical) - tau) < 1e-14
assert lower_envelope(0.8 * vcritical) > tau
assert lower_envelope(1.2 * vcritical) < tau
checks += 4
print('VERIFY_OK', checks, 'checks', 'threshold', f'{vcritical:.15f}')
