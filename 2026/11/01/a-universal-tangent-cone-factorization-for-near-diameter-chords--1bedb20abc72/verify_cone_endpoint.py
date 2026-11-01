"""Independent numerical and symbolic tests of the polytope diameter-tail constant.

Dependencies: Python 3, numpy, sympy. Run: python verify_cone_endpoint.py
The finite-sample tests corroborate, but do not prove, the general theorem.
"""
import math
import numpy as np
import sympy as sp


def kappa(q):
    return math.pi ** (q / 2) / math.gamma(q / 2 + 1)


def regular_simplex_coefficient(d):
    q = d - 1
    side_section_volume = math.sqrt(2 ** (q - 1) * (q + 2)) / math.factorial(q)
    surface_area = (d + 1) * math.sqrt(d) / (math.factorial(q) * 2 ** (q / 2))
    num_pairs = d * (d + 1) // 2
    return (2 * math.factorial(q) ** 2 / (math.factorial(2 * q) * kappa(q) * surface_area)
            * num_pairs * side_section_volume ** 2)


def orthotope_coefficient_via_cones(lengths):
    d = len(lengths)
    q = d - 1
    A = math.sqrt(sum(a * a for a in lengths))
    D = 2 * A
    B = A ** d / (math.factorial(q) * math.prod(lengths))
    S = 2 ** d * math.prod(lengths) * sum(1 / a for a in lengths)
    pairs = 2 ** (d - 1)
    cone = 2 * math.factorial(q) ** 2 * pairs * B ** 2 / (kappa(q) * S * D ** q * math.factorial(2 * q))
    direct = (2 ** (1 - d) * A ** (d + 1) * math.gamma((d + 1) / 2)
              / (math.pi ** ((d - 1) / 2) * math.factorial(2 * d - 2)
                 * (math.prod(lengths) ** 3) * sum(1 / a for a in lengths)))
    return cone, direct


# Exact Gram determinant for a regular simplex section: diag 3, off-diag 1.
for d in range(2, 9):
    q = d - 1
    G = 2 * sp.eye(q) + sp.ones(q, q)
    assert G.det() == 2 ** (q - 1) * (q + 2)
    C = regular_simplex_coefficient(d)
    assert C > 0
    print(f"simplex dimension {d}: C={C:.12g}")

for ls in [(1., 1., 1., 1.), (1., 2., 3., 4.), (0.5, 1., 1.7, 3.5, 5.), (0.7, 1., 1.6, 2.3, 3.8, 4.9)]:
    a, b = orthotope_coefficient_via_cones(ls)
    assert math.isclose(a, b, rel_tol=1e-12)
    print(f"orthotope dimension {len(ls)}: independently simplified constants agree, C={a:.12g}")

# Direct clipping of affine lines by the facets of a regular 4-simplex.
# Samples are uniform in the tangent-cone section at each of one diameter's endpoints.
rng = np.random.default_rng(20261026)
d = 4
q = d - 1
m = d + 1
vertices = (np.eye(m) - np.ones((m, m)) / m) / np.sqrt(2)
a, b = vertices[0], vertices[1]
e = b - a
D = np.linalg.norm(e)
e /= D
others = [i for i in range(m) if i not in (0, 1)]
BA = np.stack([2 * (vertices[i] - a) - e for i in others])
BB = np.stack([2 * (vertices[i] - b) + e for i in others])
assert np.max(abs(BA @ e)) < 1e-12
assert np.max(abs(BB @ e)) < 1e-12
vol_a = math.sqrt(np.linalg.det(BA @ BA.T)) / math.factorial(q)
vol_b = math.sqrt(np.linalg.det(BB @ BB.T)) / math.factorial(q)
expected_volume = math.sqrt(2 ** (q - 1) * (q + 2)) / math.factorial(q)
assert math.isclose(vol_a, expected_volume, rel_tol=1e-12)
assert math.isclose(vol_b, expected_volume, rel_tol=1e-12)

N = 400000
ya0 = rng.dirichlet(np.ones(q + 1), N)[:, :q] @ BA
yb0 = rng.dirichlet(np.ones(q + 1), N)[:, :q] @ BB
S = (d + 1) * math.sqrt(d) / (math.factorial(q) * 2 ** (q / 2))
C = regular_simplex_coefficient(d)
for eps, tolerance in [(0.15, 0.4), (0.06, 0.2), (0.02, 0.09), (0.006, 0.045)]:
    ya = eps * ya0
    yb = eps * yb0
    slope = e + (yb - ya) / D
    x0 = a[None, :] + ya
    bound = -1 / (m * math.sqrt(2))
    ratios = (bound - x0) / slope
    zlo = np.max(np.where(slope > 0, ratios, -np.inf), axis=1)
    zhi = np.min(np.where(slope < 0, ratios, np.inf), axis=1)
    lengths = np.maximum(0, zhi - zlo) * np.linalg.norm(slope, axis=1)
    good = lengths > D - eps
    jacobian = (1 + np.sum(((yb - ya) / D) ** 2, axis=1)) ** (-(d + 1) / 2)
    fraction = np.mean(good * jacobian)
    estimate = (2 * (m * (m - 1) // 2) * vol_a * vol_b / (kappa(q) * S * D ** q) * fraction)
    relative_error = abs(estimate / C - 1)
    assert relative_error < tolerance, (eps, estimate, C, relative_error)
    print(f"4-simplex eps={eps:.3g}: tail coefficient estimate={estimate:.9f}, limiting C={C:.9f}, relative error={relative_error:.4f}")
print('PASS: exact identities and independent direct-line numerical tests')
