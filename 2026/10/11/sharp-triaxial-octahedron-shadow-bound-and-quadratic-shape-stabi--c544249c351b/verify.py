"""Independent finite diagnostics for anisotropic octahedral shadow combinatorics.

Requires Python 3, NumPy, and SciPy. No simulation is used as an infinite proof.
"""
from math import atan, exp, hypot, pi, sqrt, log
import numpy as np
from scipy.spatial import ConvexHull


def hexagon_probability(a):
    a, b, c = map(float, a)
    u, v, w = hypot(a, b), hypot(a, c), hypot(b, c)
    den = u*v*w + a*a*w + b*b*v + c*c*u
    return 4.0/pi*atan(2*a*b*c/den)


def count_projection_vertices(a, u):
    u = np.asarray(u, dtype=float)
    u = u / np.linalg.norm(u)
    axis = np.eye(3)[np.argmin(np.abs(u))]
    s = np.cross(u, axis)
    s /= np.linalg.norm(s)
    t = np.cross(u, s)
    v = np.diag(np.asarray(a, dtype=float))
    points = np.vstack((v, -v))
    proj = np.column_stack((points@s, points@t))
    return len(ConvexHull(proj).vertices)


def run_checks():
    rng = np.random.default_rng(20261010)
    cases = ((1, 1, 1), (2, 1, 1), (1, 2, 3), (1, .2, 1.8), (5, 3, .25))
    checks = 0
    for a in cases:
        a = np.asarray(a, dtype=float)
        target = hexagon_probability(a)
        g = rng.normal(size=(300000, 3))
        x = np.abs(g) / a
        triangular = (2*np.max(x, axis=1) < np.sum(x, axis=1))
        measured = np.mean(triangular)
        assert abs(measured - target) < 0.007, (a, target, measured)
        checks += len(g)
        for u in g[:400]:
            pred = 6 if 2*np.max(np.abs(u)/a) < np.sum(np.abs(u)/a) else 4
            actual = count_projection_vertices(a, u)
            assert pred == actual, (a, u, pred, actual)
            checks += 1
        print('case',tuple(a),'exact',format(target,'.12f'),'simulated',format(measured,'.12f'))
    exact_regular = 4/pi*atan(sqrt(2)/5)
    assert abs(hexagon_probability((1, 1, 1))-exact_regular) < 1.e-14
    assert abs(exact_regular - 0.35095931218) < 1.e-9
    checks += 2
    # The symmetric point is the strict maximum on these tested nonsymmetric parameters.
    for a in np.exp(rng.uniform(-5, 5, size=(25000, 3))):
        assert hexagon_probability(a) <= exact_regular + 1.e-13
        checks += 1
    # Quadratic local asymptotics along two independent normalized log-axis directions.
    for t, vec in ((0.002, np.array([1., -1., 0.])), (.002, np.array([2., -1., -1.]))):
        delta = exact_regular - hexagon_probability(np.exp(t*vec))
        predicted = t*t*sum(vec*vec)/(sqrt(2)*pi)
        assert abs(delta/predicted-1.) < .006, (vec,delta,predicted)
        checks += 1
    print('VERIFY_OK', checks)


if __name__ == '__main__':
    run_checks()
