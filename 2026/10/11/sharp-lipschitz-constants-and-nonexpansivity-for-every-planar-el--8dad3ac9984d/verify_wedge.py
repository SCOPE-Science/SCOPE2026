"""Numerical cross-checks for sharp metric-projection Lipschitz constants on planar wedges.

Requires Python 3.10+, NumPy and SciPy. Execute `python verify_wedge.py`.
Floating-point tests supplement, not replace, the analytic proof.
"""
import math
import numpy as np
from scipy.optimize import minimize


def pn(x, p):
    return float(np.sum(np.abs(x)**p)**(1.0/p))


def phi(v, p):
    q = p/(p-1)
    v = np.asarray(v, dtype=float)
    return np.sign(v)*np.abs(v)**(q-1)/np.sum(np.abs(v)**q)


def line(x, v, p):
    return np.asarray(v)*float(np.dot(phi(v, p), x))


def ray_norm(v, p):
    q = p/(p-1)
    a = np.abs(np.asarray(v, dtype=float))
    return float((np.sum(a**p)**(1/p)) *
                 np.sum(a**(q*(q-1)))**(1/q) / np.sum(a**q))


def cone_point(x, u, v, p):
    # Exact active-face selection, up to floating-point rounding.
    a = np.linalg.solve(np.column_stack((u, v)), x)
    candidates = [np.zeros(2)]
    if a.min() >= -1e-12:
        candidates.append(x)
    for w in (u, v):
        y = line(x, w, p)
        if np.dot(y, w) > 0:
            candidates.append(y)
    return min(candidates, key=lambda y: pn(x-y, p))


def independent_solver(x, u, v, p):
    A = np.column_stack((u, v))
    def fun(a):
        return pn(x-A@a, p)
    def jac(a):
        r = x-A@a
        nr = pn(r, p)
        return np.zeros(2) if nr < 1e-12 else -A.T@(np.sign(r)*np.abs(r)**(p-1))/nr**(p-1)
    res = minimize(fun, [0.4, 0.4], jac=jac, bounds=[(0, None)]*2,
                   method='SLSQP', options={'ftol': 1e-13, 'maxiter': 300})
    return A@res.x


def main():
    rng = np.random.default_rng(314159)
    independent_checks = pair_checks = local_checks = 0
    worst_independent = 0.
    for p in (1.3, 1.5, 2., 2.7, 3., 4., 6.):
        for _ in range(15):
            angles = np.sort(rng.uniform(0, 2*np.pi, 2))
            if angles[1]-angles[0] > np.pi:
                angles[0], angles[1] = angles[1], angles[0]+2*np.pi
            u = np.array([np.cos(angles[0]), np.sin(angles[0])])
            v = np.array([np.cos(angles[1]), np.sin(angles[1])])
            M = max(1., ray_norm(u, p), ray_norm(v, p))
            for _ in range(35):
                x = rng.normal(size=2)
                actual = cone_point(x, u, v, p)
                numeric = independent_solver(x, u, v, p)
                worst_independent = max(worst_independent, pn(actual-numeric, p))
                assert pn(actual-numeric, p) <= 3.e-5, (p, x, actual, numeric)
                independent_checks += 1
            for _ in range(30):
                x, y = rng.normal(size=2), rng.normal(size=2)
                ratio = pn(cone_point(x, u, v, p)-cone_point(y, u, v, p), p)/pn(x-y, p)
                assert ratio <= M+5e-9, (p, ratio, M)
                pair_checks += 1
            # Each boundary ray really realizes its full line-projection derivative.
            for w, other in ((u, v), (v, u)):
                h = np.array([-w[1], w[0]])
                if np.dot(h, other) >= 0:
                    h = -h
                q = p/(p-1)
                residual = np.sign(h)*np.abs(h)**(q-1)
                x = w + residual
                assert pn(cone_point(x, u, v, p)-w, p) < 1e-8
                f = phi(w, p)
                direction = np.sign(f)*np.abs(f)**(q-1)
                direction /= pn(direction, p)
                eps = 1.e-5
                ratio = pn(cone_point(x+eps*direction, u, v, p)-cone_point(x, u, v, p), p)/eps
                assert abs(ratio-ray_norm(w, p)) < 2e-7, (p, ratio, ray_norm(w, p))
                local_checks += 1
    for p in (1.1, 1.5, 2., 3., 4., 6., 20.):
        assert abs(ray_norm([1., 0.], p)-1) < 2.e-14
        assert abs(ray_norm([1., 1.], p)-1) < 2.e-14
    for p in (1.5, 3., 4., 6.):
        assert ray_norm([1., 2.], p) > 1.001
    print(f'VERIFY_OK independent_optimizations={independent_checks} '
          f'global_pair_checks={pair_checks} boundary_sharpness_checks={local_checks} '
          f'max_solver_difference={worst_independent:.3g}')


if __name__ == '__main__':
    main()
