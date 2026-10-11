#!/usr/bin/env python3
"""Numerical finite checks for the orthogonal three-disk hull formulas.

Requires NumPy and SciPy. Finite polygonal approximations are not proofs.
"""

import math
import numpy as np
from scipy.integrate import quad
from scipy.spatial import ConvexHull


def expected(radius):
    volume = (8 - 10 * math.sqrt(2) / 3) * radius**3
    area = (12 - 4 * math.sqrt(3) + 2 * math.pi) * radius**2
    return volume, area


def disk_boundary_samples(n, radius):
    theta = 2 * math.pi * np.arange(n) / n
    a = radius * np.cos(theta)
    b = radius * np.sin(theta)
    zeros = np.zeros(n)
    return np.concatenate([
        np.column_stack([a, b, zeros]),
        np.column_stack([a, zeros, b]),
        np.column_stack([zeros, a, b]),
    ])


def support_formula(u, radius):
    return radius * math.sqrt(float(np.dot(u, u) - np.min(u * u)))


def main():
    expected_patch_area = 0.5 - math.sqrt(3) / 4 + math.pi / 12
    numeric_patch_area = quad(
        lambda x: math.sin(x) * math.sqrt(1 + math.sin(x) ** 2),
        0, math.pi / 4, epsabs=2e-14, epsrel=2e-14
    )[0]
    assert abs(numeric_patch_area - expected_patch_area) < 5e-14
    numeric_patch_flux = quad(lambda x: math.sin(x), 0, math.pi / 4)[0]
    assert abs(numeric_patch_flux - (1 - 1 / math.sqrt(2))) < 5e-14

    for radius in [0.625, 1.0, 2.3]:
        vol, area = expected(radius)
        assert abs(area - (24 * expected_patch_area + 2 * math.sqrt(3)) * radius ** 2) < 1e-11
        assert abs(3 * vol - (24 * numeric_patch_flux + 2 * math.sqrt(2)) * radius ** 3) < 1e-11

        previous_errors = None
        for n in [64, 256, 1024]:
            points = disk_boundary_samples(n, radius)
            hull = ConvexHull(points)
            errors = (abs(hull.volume - vol) / vol, abs(hull.area - area) / area)
            if previous_errors is not None:
                assert errors[0] < previous_errors[0]
                assert errors[1] < previous_errors[1]
            previous_errors = errors
        assert previous_errors[0] < 1e-5
        assert previous_errors[1] < 1e-5

    rng = np.random.default_rng(3157)
    points = disk_boundary_samples(16384, 1.0)
    for _ in range(300):
        u = rng.standard_normal(3)
        a = support_formula(u, 1.0)
        b = float(np.max(points @ u))
        assert 0 <= a - b < 4e-8 * float(np.linalg.norm(u))

    # Verify that the eight planar facets have the stated area and distance.
    v1 = np.array([1 / math.sqrt(2), 1 / math.sqrt(2), 0.0])
    v2 = np.array([1 / math.sqrt(2), 0.0, 1 / math.sqrt(2)])
    v3 = np.array([0.0, 1 / math.sqrt(2), 1 / math.sqrt(2)])
    assert np.isclose(np.linalg.norm(v1 - v2), 1.0)
    assert np.isclose(np.linalg.norm(v1 - v3), 1.0)
    assert np.isclose(np.linalg.norm(v2 - v3), 1.0)
    facet_area = 0.5 * np.linalg.norm(np.cross(v2 - v1, v3 - v1))
    assert abs(facet_area - math.sqrt(3) / 4) < 1e-14
    assert abs(np.dot(v1, np.ones(3) / math.sqrt(3)) - math.sqrt(2 / 3)) < 1e-14

    # The maximum and minimum support values on the sphere give the radii.
    assert abs(support_formula(np.ones(3) / math.sqrt(3), 1.0) - math.sqrt(2 / 3)) < 1e-14
    assert abs(support_formula(np.array([1.0, 0, 0]), 1.0) - 1.0) < 1e-14

    print("VERIFY_OK: patch integrals, divergence flux, 9 polyhedral hulls,"
          " 300 support directions, facet geometry, radii and scaling")
    print("unit_volume=%.15f unit_area=%.15f" % expected(1.0))


if __name__ == "__main__":
    main()
