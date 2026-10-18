"""Independent numerical cross-checks for the cuboctahedron silhouette theorem.

Run with Python, NumPy, and SciPy. Quadrature and simulation check the
analytic proof; neither constitutes a proof of the infinite assertion.
"""
import itertools
import math
import numpy as np
from scipy.spatial import ConvexHull
from numpy.polynomial.legendre import leggauss


def model(unit_vector):
    a, b, c = sorted(np.abs(unit_vector), reverse=True)
    if abs(a - b - c) < 1e-10:
        raise ValueError('Boundary direction; choose a generic one')
    return (8 if a > b + c else 6), (4*a + 2*b + 2*c if a > b + c else 3*(a+b+c))


def orthographic_hull(unit_vector, vertices):
    vector = np.asarray(unit_vector, dtype=float)
    anchor = np.eye(3)[np.argmin(np.abs(vector))]
    v1 = np.cross(vector, anchor)
    v1 /= np.linalg.norm(v1)
    v2 = np.cross(vector, v1)
    coords = np.column_stack((vertices @ v1, vertices @ v2))
    hull = ConvexHull(coords)
    return len(hull.vertices), hull.volume


def check():
    # Explicitly reconstruct by placement of the zero coordinate.
    vertices = np.array([
        tuple(0 if k == zero else (signs[0] if k == (zero+1)%3 else signs[1])
              for k in range(3))
        for zero in range(3)
        for signs in itertools.product((-1, 1), repeat=2)], dtype=float)
    assert len(vertices) == 12
    delta = 3 - 2 * math.sqrt(2)
    omega = 2 * math.atan(delta)
    p = 6 * omega / math.pi
    nodes, weights = leggauss(72)
    vals = (nodes + 1) / 2
    weights = weights / 2
    solid = moment = 0.0
    for s, ws in zip(vals, weights):
        for w, ww in zip(vals, weights):
            t = (1-s)*w
            R = 1+s*s+t*t
            weight = ws*ww*(1-s)
            solid += weight * R**(-1.5)
            moment += weight * (4+2*s+2*t) / (R*R)
    assert abs(solid - omega) < 3e-13, (solid, omega)
    assert abs(moment - math.pi/2) < 3e-13, (moment, math.pi/2)
    assert abs((2/math.pi)*3*moment - 3) < 3e-13
    rng = np.random.default_rng(20261016)
    samples = rng.standard_normal((240000, 3))
    samples /= np.linalg.norm(samples, axis=1)[:, None]
    triples = np.sort(np.abs(samples), axis=1)[:, ::-1]
    eight = triples[:, 0] > triples[:, 1] + triples[:, 2]
    brightness = np.where(eight, 4*triples[:, 0]+2*triples[:, 1]+2*triples[:, 2],
                          3*triples.sum(axis=1))
    assert abs(eight.mean()-p) < 0.004
    assert abs(np.mean(brightness*eight)-3) < 0.02
    assert abs(np.mean(brightness*(~eight))-math.sqrt(3)) < 0.02
    checked = 0
    for unit in samples[:500]:
        anticipated = model(unit)
        observed = orthographic_hull(unit, vertices)
        assert anticipated[0] == observed[0], (unit, anticipated, observed)
        assert abs(anticipated[1]-observed[1]) < 1e-10, (unit, anticipated, observed)
        checked += 1
    cond8 = 3/p
    cond6 = math.sqrt(3)/(1-p)
    cov = 2*(3-p*(3+math.sqrt(3)))
    assert cov < -0.14 and cond8 < cond6
    print('CUBOCTAHEDRON_SILHOUETTE_OK ' +
          f'quadrature_nodes={72**2} direct_hulls={checked} monte_carlo={len(samples)} ' +
          f'p_octagon={p:.12f} mean_oct_area={cond8:.12f} ' +
          f'mean_hex_area={cond6:.12f} covariance={cov:.12f}')


if __name__ == '__main__':
    check()
