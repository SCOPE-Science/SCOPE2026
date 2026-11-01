"""Reproducible numerical checks for the joint area/silhouette law of a regular tetrahedron.

Requires numpy and scipy. Finite checks corroborate, but do not replace, the
spherical-geometry proof in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.spatial import ConvexHull

sqrt = math.sqrt
pi = math.pi
b0 = 2 * sqrt(2)
bs = 4 * sqrt(2 / 3)
bt = 2 * sqrt(3)
alpha = math.asin(1 / 3)
Omega = pi / 2 - 3 * alpha
P3 = 2 * Omega / pi
vertices = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float)


def densities(t):
    if t <= b0 or t >= 4:
        return 0., 0.
    if t < bs:
        z3 = max(-1., min(1., t / (2 * sqrt(2) * sqrt(12 - t * t))))
        z4 = max(-1., min(1., t / (sqrt(2) * sqrt(16 - t * t))))
        f3 = 2 / sqrt(3) * (1 - 3 / pi * math.acos(z3))
        f4 = .75 - 3 / pi * math.acos(z4)
        return f3, f4
    if t < bt:
        return 2 / sqrt(3), .75
    return 0., .75


def moments(j, k):
    def integrand(t):
        return t ** k * densities(t)[j]
    return sum(quad(integrand, lo, hi, epsabs=2e-12, epsrel=2e-12)[0]
               for lo, hi in [(b0, bs), (bs, bt), (bt, 4.)])


for j, p in enumerate((P3, 1 - P3)):
    assert abs(moments(j, 0) - p) < 2e-11
assert abs(moments(0, 1) - 2 / sqrt(3)) < 2e-11
assert abs(moments(1, 1) - 4 / sqrt(3)) < 2e-11
assert abs(moments(0, 2) - P3 * (4 + 8 * sqrt(2) / (3 * Omega))) < 2e-11
assert abs(moments(1, 2) - (1 - P3) * (16 / 3 + 16 * sqrt(2) / (9 * alpha))) < 2e-11
for t in np.linspace(bs + .01, bt - .01, 21):
    f3, f4 = densities(float(t))
    assert abs(f3 / (f3 + f4) - 8 / (8 + 3 * sqrt(3))) < 1e-14
assert abs(8 * sum(densities((bs + bt) / 2)) - (6 + 16 / sqrt(3))) < 1e-13
assert abs(8 * sum(densities((bt + 4) / 2)) - 6) < 1e-13

# Independently reconstruct the projected convex hull, not just facet normals.
def polygon_from_projection(u):
    t = np.array([0., 0., 1.]) if abs(u[2]) < .8 else np.array([1., 0., 0.])
    e1 = np.cross(u, t)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(u, e1)
    coords = np.stack([vertices @ e1, vertices @ e2], axis=1)
    hull = ConvexHull(coords)
    return len(hull.vertices), hull.volume

rng = np.random.default_rng(20261031)
u = rng.standard_normal((2500, 3))
u /= np.linalg.norm(u, axis=1, keepdims=True)
for v in u:
    aa = np.abs(v)
    predicted_area = max(2 * float(aa.sum()), 4 * float(aa.max()))
    predicted_nv = 3 if 2 * aa.max() < aa.sum() else 4
    nv, area = polygon_from_projection(v)
    assert nv == predicted_nv
    assert abs(area - predicted_area) < 2e-12

# Haar-spherical simulation of a separate large sample.
u = rng.standard_normal((450000, 3))
u /= np.linalg.norm(u, axis=1, keepdims=True)
a = np.abs(u)
area = np.maximum(2 * a.sum(axis=1), 4 * a.max(axis=1))
tri = (2 * a.max(axis=1) < a.sum(axis=1))
assert abs(tri.mean() - P3) < .003
assert abs(area[tri].mean() - (2 / sqrt(3)) / P3) < .015
assert abs(area[~tri].mean() - (4 / sqrt(3)) / (1 - P3)) < .015
band = (area >= bs + .015) & (area <= bt - .015)
assert band.sum() > 50000
assert abs(tri[band].mean() - 8 / (8 + 3 * sqrt(3))) < .012
print('ALL_TETRAHEDRAL_JOINT_AREA_SILHOUETTE_CHECKS_PASSED')
