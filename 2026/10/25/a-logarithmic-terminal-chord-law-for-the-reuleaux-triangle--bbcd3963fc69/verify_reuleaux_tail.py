"""Independent numerical checks for a Reuleaux triangle's long-chord tail.

The unit-width Reuleaux triangle is represented as an intersection of three
unit disks; no source document or precomputed values are read.
Run: python verify_reuleaux_tail.py
Requires numpy and scipy.
"""
import math
import numpy as np
from scipy.integrate import quad

CENTERS = np.array([[0.0, 0.0], [1.0, 0.0], [0.5, math.sqrt(3.0) / 2.0]])
SECTOR = math.pi / 3.0


def chord_length(phi, t):
    """Exactly intersect the three closed disk intervals on an affine line."""
    u = np.array([math.cos(phi), math.sin(phi)])
    v = np.array([-math.sin(phi), math.cos(phi)])
    a = CENTERS @ u
    b = CENTERS @ v
    d = 1.0 - (t - b) ** 2
    if min(d) < 0.0:
        return 0.0
    r = np.sqrt(np.maximum(0.0, d))
    return max(0.0, float(min(a + r) - max(a - r)))


def root_offset(phi, eps, direction):
    lo, hi = 0.0, math.sqrt(2.0 * eps) * 1.001
    assert chord_length(phi, 0.0) > 1.0 - eps
    for _ in range(49):
        mid = (lo + hi) / 2.0
        if chord_length(phi, direction * mid) > 1.0 - eps:
            lo = mid
        else:
            hi = mid
    return lo


def near_diameter_probability(eps):
    def sector_width(phi):
        return root_offset(phi, eps, 1) + root_offset(phi, eps, -1)

    result, _ = quad(
        sector_width, 0.0, SECTOR,
        points=[math.sqrt(eps), SECTOR - math.sqrt(eps)],
        epsabs=2e-11, limit=250,
    )
    return 3.0 * result / math.pi


def check_geometry():
    rng = np.random.default_rng(431)
    for _ in range(800):
        phi = rng.uniform(0.0, SECTOR)
        t = rng.uniform(-0.3, 0.3)
        z = chord_length(phi, t)
        assert -1e-12 <= z <= 1.0 + 1e-12
        if t > 0.0 and t + math.sin(phi) < 1.0:
            lower_one = math.cos(phi) - math.sqrt(1.0 - (t + math.sin(phi)) ** 2)
            assert lower_one >= -1e-12
        if t < 0.0 and -t + math.sin(SECTOR - phi) < 1.0:
            beta = SECTOR - phi
            lower_two = math.cos(beta) - math.sqrt(1.0 - (t - math.sin(beta)) ** 2)
            assert lower_two >= -1e-12
    for phi in np.linspace(0.001, SECTOR - 0.001, 250):
        assert abs(chord_length(float(phi), 0.0) - 1.0) < 1e-13
    print('THREE_DISK_CHORD_INTERVAL_GEOMETRY_OK')


def check_coefficient():
    vals = {}
    for e in [1e-3, 1e-4, 1e-5, 1e-6]:
        vals[e] = near_diameter_probability(e)
        assert vals[e] > 0.0
        rem = (vals[e] - (3.0 / math.pi) * e * math.log(1.0 / e)) / e
        assert 0.5 < rem < 0.9
        print('TAIL_SCALED_REMAINDER', format(e, '.0e'), format(rem, '.7f'))
    for e in [1e-3, 1e-4]:
        coeff = (10.0 * vals[e / 10.0] - vals[e]) / (e * math.log(10.0))
        assert abs(coeff - 3.0 / math.pi) < 0.004
        print('LOG_COEFFICIENT_DIFFERENCE_OK', format(e, '.0e'), format(coeff, '.8f'))
    print('SHARP_EPSILON_LOG_EPSILON_CHORD_TAIL_CHECKS_OK')


if __name__ == '__main__':
    check_geometry()
    check_coefficient()
    print('ALL_REULEAUX_CHORD_TAIL_CHECKS_OK')
