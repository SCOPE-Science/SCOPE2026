"""Independent finite checks for the near-diameter law of regular Reuleaux polygons.

Requires Python 3, numpy and scipy. Numerical tests corroborate but do not
establish the infinite-limit theorem, whose proof is geometric.
"""
import math
import numpy as np
from scipy.integrate import quad


def area(n):
    assert n >= 3 and n % 2 == 1
    return (math.pi - n * math.tan(math.pi / (2 * n))) / 2


def disk_intersection_covariogram(n, s, phi):
    # An exact geometric construction: intersect n unit disks and their translates.
    radius = 1 / (2 * math.cos(math.pi / (2 * n)))
    centers = np.array([[radius * math.cos(2 * math.pi * k / n),
                         radius * math.sin(2 * math.pi * k / n)]
                        for k in range(n)])
    z = (1 - s) * np.array([math.cos(phi), math.sin(phi)])
    both = np.concatenate((centers, centers - z), axis=0)
    lo = np.max(both[:, 0] - 1)
    hi = np.min(both[:, 0] + 1)
    if lo >= hi:
        return 0.0

    def vertical_slice_length(x):
        square_radii = 1 - (x - both[:, 0]) ** 2
        if np.any(square_radii < 0):
            return 0.0
        radii = np.sqrt(square_radii)
        return max(0.0, np.min(both[:, 1] + radii) -
                   np.max(both[:, 1] - radii))

    value = quad(vertical_slice_length, lo, hi,
                 epsabs=4e-11, limit=120)[0]
    return value


def run():
    count = 0
    assert abs(area(3) - (math.pi - math.sqrt(3)) / 2) < 1e-14
    assert all(0.70 < area(n) < math.pi / 4 for n in (3, 5, 7, 9, 11))
    count += 6
    for n in (3, 5, 7, 9, 11):
        alpha = math.pi / n
        for k in range(1, 51):
            phi = alpha * k / 51
            c = math.sin(alpha) / (2 * math.sin(phi) * math.sin(alpha - phi))
            other = (1 / math.tan(phi) + 1 / math.tan(alpha - phi)) / 2
            assert abs(c / other - 1) < 1e-12
            count += 1
        for delta in (1e-2, 1e-3):
            if 2 * delta >= alpha:
                continue
            exact = math.log(math.sin(alpha - delta) / math.sin(delta))
            quadrature = quad(lambda x: math.sin(alpha) /
                              (2 * math.sin(x) * math.sin(alpha - x)),
                              delta, alpha - delta, epsabs=1e-10)[0]
            assert abs(quadrature - exact) < 1e-9
            count += 1
    for n in (3, 5, 7):
        c_mid = 1 / math.tan(math.pi / (2 * n))
        for s in (0.01, 0.003):
            got = disk_intersection_covariogram(n, s, math.pi)
            assert 0.78 < got / (c_mid * s * s) < 1.02, (n, s, got)
            count += 1
            seam = disk_intersection_covariogram(n, s, math.pi + math.pi / (2 * n))
            # The edge-direction crossover is of order s^{3/2}, not s^2.
            assert 0.64 < seam / s**1.5 < 0.73, (n, s, seam)
            count += 1
    print(f'REULEAUX_FINITE_CHECKS_OK: {count} checks; 3, 5, 7, 9, 11 vertices')
    print('These tests do not prove the limiting logarithmic coefficient.')


if __name__ == '__main__':
    run()
