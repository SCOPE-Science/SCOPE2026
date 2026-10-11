#!/usr/bin/env python3
"""Independent finite checks for projected-width spectra of tangential polygons.

Uses direct vertex dot products and shoelace geometry, not the piecewise
normal-cone formula that yields the analytic survival function.
"""
import math
import numpy as np

PI = math.pi


def polygon_from_half_gaps(gaps, radius=1.0):
    """Vertices from the intersections of successive tangent lines."""
    angles = [0.0]
    for delta in list(gaps) * 2:
        angles.append(angles[-1] + delta)
    assert abs(angles[-1] - 2 * PI) < 2e-12
    vertices = []
    for i in range(len(angles) - 1):
        left, right = angles[i], angles[i + 1]
        mid = (left + right) / 2
        R = radius / math.cos((right - left) / 2)
        vertices.append((R * math.cos(mid), R * math.sin(mid)))
    return np.asarray(vertices)


def exact_survival(t, gaps):
    if t < 1:
        return 1.0
    return 2.0 / PI * sum(math.acos(min(1.0, t * math.cos(delta / 2)))
                          for delta in gaps if t < 1 / math.cos(delta / 2))


def polygon_area_and_perimeter(vertices):
    v = np.asarray(vertices)
    shifted = np.roll(v, -1, axis=0)
    cross = v[:, 0] * shifted[:, 1] - v[:, 1] * shifted[:, 0]
    return abs(np.sum(cross)) / 2.0, np.linalg.norm(shifted - v, axis=1).sum()


def direct_widths(vertices, number=262144):
    directions = 2.0 * PI * np.arange(number) / number
    # The opposite-direction support is computed separately for independence.
    x = np.cos(directions)
    y = np.sin(directions)
    pos = np.max(vertices[:, 0, None] * x + vertices[:, 1, None] * y, axis=0)
    neg = np.max(-vertices[:, 0, None] * x - vertices[:, 1, None] * y, axis=0)
    return pos + neg


def run():
    profiles = [
        ([PI / 10, PI / 5, 3 * PI / 10, 2 * PI / 5], 1),
        ([PI / 10, PI / 5, 2 * PI / 5, 3 * PI / 10], 1),
        ([PI / 3, PI / 3, PI / 3], 2),
        ([PI / 6, PI / 6, PI / 3, PI / 3], 0.8),
        ([PI / 11] * 10 + [PI / 11], 1.3),
    ]
    rng = np.random.default_rng(551208)
    for m in (2, 3, 4, 5, 7):
        gaps = rng.dirichlet(np.ones(m) * 1.5) * PI
        profiles.append((gaps.tolist(), 0.5 + m / 8))
    counts = 0
    reference = []
    for gaps, radius in profiles:
        v = polygon_from_half_gaps(gaps, radius)
        assert np.max(np.linalg.norm(v[:len(gaps)] + v[len(gaps):], axis=1)) < 1e-12
        A, P = polygon_area_and_perimeter(v)
        predicted_A = 2 * radius ** 2 * sum(math.tan(d / 2) for d in gaps)
        predicted_P = 4 * radius * sum(math.tan(d / 2) for d in gaps)
        assert abs(A - predicted_A) < 2e-10
        assert abs(P - predicted_P) < 2e-10
        counts += 3
        widths = direct_widths(v)
        assert widths.min() >= 2 * radius - 2e-10
        max_expected = 2 * radius * max(1 / math.cos(d / 2) for d in gaps)
        assert abs(widths.max() - max_expected) < 3e-7
        counts += 2
        endpoints = sorted(set(1 / math.cos(d / 2) for d in gaps))
        thresholds = np.linspace(1.0001, max(endpoints) - 0.0001, 20)
        for t in thresholds:
            empirical = np.mean(widths > 2 * radius * t)
            predicted = exact_survival(float(t), gaps)
            # Deterministic regular angular grid: at most 4m crossings.
            assert abs(empirical - predicted) < 0.0006, (gaps, t, empirical, predicted)
            counts += 1
        if len(reference) < 2:
            reference.append((sorted(gaps), radius, widths))
    one, two = reference
    assert one[0] == two[0] and one[1] == two[1]
    for level in np.linspace(2.0001, min(one[2].max(), two[2].max()) - 0.0001, 50):
        assert abs(np.mean(one[2] > level) - np.mean(two[2] > level)) < 0.001
        counts += 1
    print(f"VERIFY_OK: {counts} independent area/perimeter/support/CDF checks")


if __name__ == "__main__":
    run()
