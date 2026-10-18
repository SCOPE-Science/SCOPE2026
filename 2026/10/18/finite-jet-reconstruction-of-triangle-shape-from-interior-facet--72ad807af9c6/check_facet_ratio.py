"""Reproducible numerical and exact-algebra checks of simplex supporting-facet margins."""
from fractions import Fraction
from math import factorial
import itertools
import numpy as np


def face_areas_and_distances(vertices, barycentric):
    verts = np.asarray(vertices, dtype=float)
    m, dim = verts.shape
    points = barycentric @ verts
    area = np.zeros(m)
    dist = np.zeros((len(points), m))
    for i in range(m):
        face = np.delete(verts, i, axis=0)
        edges = face[1:] - face[0]
        if dim == 2:
            e = edges[0]
            area[i] = np.linalg.norm(e)
            normal = np.array([-e[1], e[0]]) / area[i]
        elif dim == 3:
            e = np.cross(edges[0], edges[1])
            area[i] = np.linalg.norm(e) / 2
            normal = e / (2 * area[i])
        else:
            raise ValueError('This independent geometric checker handles dim 2 and 3')
        dist[:, i] = np.abs((points - face[0]) @ normal)
    return area, dist


def run_geometry(vertices, seed, n=230000):
    m = len(vertices)
    rng = np.random.default_rng(seed)
    bary = rng.dirichlet([1.0] * m, n)
    area, dist = face_areas_and_distances(vertices, bary)
    p = area / area.sum()
    sorted_dist = np.sort(dist, axis=1)
    r = sorted_dist[:, 1] / sorted_dist[:, 0]
    for y in (0.18, 0.75, 2.0, 5.0):
        theo = sum(float(v) / (1.0 + (1.0 - float(v)) * y) for v in p)
        obs = np.count_nonzero(r > 1.0 + y) / n
        err = (theo * (1 - theo) / n)**0.5
        assert abs(theo - obs) < max(0.004, 6 * err), (y, obs, theo, err)
    closest = np.argmin(dist, axis=1)
    for i, pred in enumerate(p):
        obs = np.count_nonzero(closest == i) / n
        err = (pred * (1 - pred) / n)**0.5
        assert abs(pred - obs) < max(0.004, 6 * err), (i, obs, pred)
    # The affine formula distance = altitude times barycentric coordinate,
    # checked using independently constructed face normals.
    mat = np.asarray(vertices, dtype=float)
    vol = abs(np.linalg.det((mat[1:] - mat[0]).T)) / factorial(m - 1)
    altitude = (m - 1) * vol / area
    assert np.max(np.abs(dist - bary * altitude)) < 1e-10
    return m, tuple(float(round(x, 8)) for x in p)


def run_exact_jet():
    from math import comb
    for amounts in ((3, 4, 5), (3, 5, 7), (1, 1, 1), (2, 3, 4, 5)):
        m = len(amounts)
        p = [Fraction(q, sum(amounts)) for q in amounts]
        moments = [sum(x ** k for x in p) for k in range(1, m + 1)]
        deriv = [sum(x * (1 - x) ** k for x in p) for k in range(m)]
        recovered = [Fraction(0), Fraction(1)]
        for k in range(1, m):
            preceding = sum((-1) ** j * comb(k, j) * recovered[j + 1] for j in range(k))
            recovered.append((-1) ** k * (deriv[k] - preceding))
        assert recovered[1:] == moments
        elem = [Fraction(1)]
        for k in range(1, m + 1):
            elem.append(sum((-1) ** (j - 1) * elem[k - j] * recovered[j] for j in range(1, k + 1)) / k)
        # Characteristic polynomial vanishes on all original area ratios.
        for x in p:
            poly = sum((-1) ** k * elem[k] * x ** (m - k) for k in range(m + 1))
            assert poly == 0, (amounts, x, poly)
        if m == 3:
            assert elem[2] == deriv[1] / 2
            assert elem[3] == (deriv[2] - deriv[1] / 2) / 3
    return 4


def run_extremum():
    rng = np.random.default_rng(20261016)
    for _ in range(1500):
        # Positive triangle side lengths via apex/polygon points; here
        # uniform feasible normalized side profiles obtained from two random
        # angles in the open simplex with maximum below one half.
        while True:
            q = rng.dirichlet(np.ones(3))
            if max(q) < 0.5:
                break
        for y in (0.1, 1.0, 10.0):
            s = sum(v / (1 + (1-v)*y) for v in q)
            assert 3/(3+2*y)-1e-12 <= s <= 2/(2+y)+1e-12
    return 1500


if __name__ == '__main__':
    cases = [
        [[0, 0], [3, 0], [0, 4]],
        [[0, 0], [4, 0], [0.8, 2.4]],
        [[0, 0], [1, 0], [0.5, 3**0.5/2]],
        [[0, 0, 0], [2.0, 0, 0], [0.3, 1.7, 0], [0.2, 0.4, 2.1]],
    ]
    results = [run_geometry(v, seed=20261016+i) for i, v in enumerate(cases)]
    exact = run_exact_jet()
    profiles = run_extremum()
    print('SIMPLEX_FACET_RATIO_OK geometry_cases=%d samples=%d exact_jets=%d extremal_profiles=%d' % (
        len(cases), 230000*len(cases), exact, profiles))
    for result in results:
        print('facet_profile', result)
