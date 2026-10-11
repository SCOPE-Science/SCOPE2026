"""Exact-rational sanity checks for explicit sharpness models, not a general proof."""
from fractions import Fraction as Q


def moment_from_order(r, a):
    """Absolute first Fourier moment of A_f for h(z)=z, omega(z)=a*z."""
    return r * (1 + a * a * (1 - r * r) / (2 * (1 - a * a * r * r)))


def moment_from_energy(r, a):
    """Radius plus the exactly integrated energy correction for same model."""
    energy_over_pi = a * a * r * r / (1 - a * a * r * r)
    return r + (1 - r * r) * energy_over_pi / (2 * r)


for r, a, expected in [(Q(1, 2), Q(1, 3), Q(73, 140)),
                       (Q(3, 4), Q(2, 3), Q(61, 72)),
                       (Q(2, 3), Q(0), Q(2, 3))]:
    assert moment_from_order(r, a) == expected
    assert moment_from_energy(r, a) == expected
print('PASS: three exact rational model checks; no infinite-scope certification')
