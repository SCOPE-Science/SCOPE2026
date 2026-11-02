#!/usr/bin/env python3
"""Numerical consistency checks for the joint section-shadow geometry of ellipsoids.

Tests are finite and do not replace the analytical proof.
Requires NumPy; no network or unpublished inputs.
"""
import math
import numpy as np

rng = np.random.default_rng(20261031)


def volumes(axes, u):
    axes = np.asarray(axes, dtype=float)
    u = np.asarray(u, dtype=float)
    c = math.pi * np.prod(axes) if len(axes) == 3 else math.pi ** ((len(axes) - 1) / 2) / math.gamma((len(axes) + 1) / 2) * np.prod(axes)
    t = np.dot(axes * axes, u * u)
    v = np.dot(1 / (axes * axes), u * u)
    return c / math.sqrt(t), c * math.sqrt(v)


def independently_computed_3d_areas(axes, u):
    u = np.asarray(u, dtype=float)
    trial = np.eye(3)[int(np.argmin(abs(u)))]
    e1 = trial - u * np.dot(trial, u)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(u, e1)
    P = np.stack([e1, e2], axis=1)
    mat = np.diag(np.square(axes))
    # Shadow ellipse: image under projection of the ellipsoid.
    shadow = math.pi * math.sqrt(np.linalg.det(P.T @ mat @ P))
    # Central section ellipse: inverse quadratic form restricted to the plane.
    section = math.pi / math.sqrt(np.linalg.det(P.T @ np.linalg.inv(mat) @ P))
    return section, shadow


def check_3d():
    for axes in ([1, 2, 3], [1, 1.7, 5.2], [.5, 2.2, 3.1]):
        l = np.square(axes)
        c = math.pi * np.prod(axes)
        delta = (l[1] - l[0]) * (l[2] - l[0]) * (l[2] - l[1]) / np.prod(l)
        matrix = np.array([[1., 1., 1.], l, 1. / l])
        assert abs(np.linalg.det(matrix) - delta) <= 1e-12 * delta
        for sample_index in range(400):
            u = rng.normal(size=3)
            u /= np.linalg.norm(u)
            sec, shadow = volumes(axes, u)
            indep_sec, indep_shadow = independently_computed_3d_areas(axes, u)
            assert abs(sec - indep_sec) < 1e-11 * sec
            assert abs(shadow - indep_shadow) < 1e-11 * shadow
            t, v = (c / sec) ** 2, (shadow / c) ** 2
            recovered = np.empty(3)
            for i in range(3):
                j, k = [h for h in range(3) if h != i]
                recovered[i] = l[i] * (l[j] * l[k] * v - l[j] - l[k] + t) / ((l[i] - l[j]) * (l[i] - l[k]))
            assert np.max(abs(recovered - u * u)) < 2e-12
            # Verify the density's reciprocal Jacobian after pulling back
            # the conventional Dirichlet density in (x1,x2).
            x = u * u
            dirichlet = 1. / (2 * math.pi * math.sqrt(np.prod(x)))
            density_t_v = dirichlet / delta
            density_s_b = 2 * shadow / (math.pi * delta * sec ** 3 * math.sqrt(np.prod(x)))
            jac_t_v_from_s_b = 4 * shadow / sec ** 3
            assert abs(density_s_b - density_t_v * jac_t_v_from_s_b) < 1e-9 * density_s_b


def check_association():
    count = 240000
    for axes in ([1, 1, 1], [1, 1, 3], [1, 2, 3], [.3, 1, 5], [1, 2, 5, 8], [1, 1, 1, 5, 20]):
        l = np.square(axes)
        z = rng.normal(size=(count, len(l)))
        x = z * z
        x /= x.sum(axis=1)[:, None]
        s = 1 / np.sqrt(x @ l)
        b = np.sqrt(x @ (1 / l))
        cov = float(np.mean((s - s.mean()) * (b - b.mean())))
        if len(set(axes)) == 1:
            assert abs(cov) < 1e-25
        else:
            assert cov > 5e-6, (axes, cov)
        for p, q in [(0.2, 0.2), (0.4, 0.6), (0.7, 0.4)]:
            event1 = s > np.quantile(s, p)
            event2 = b > np.quantile(b, q)
            gap = float(np.mean(event1 & event2) - np.mean(event1) * np.mean(event2))
            assert gap > -.005, (axes, p, q, gap)


def check_stick_breaking():
    d = 7
    samples = 30000
    z = np.empty((samples, d - 1))
    for k in range(1, d):
        z[:, k - 1] = rng.beta(k / 2, 0.5, samples)
    p = np.ones((samples, d))
    for k in reversed(range(d - 1)):
        p[:, k] = z[:, k] * p[:, k + 1]
    x = np.empty_like(p)
    x[:, 0] = p[:, 0]
    x[:, 1:] = p[:, 1:] - p[:, :-1]
    assert np.min(x) > 0
    assert abs(x.mean(axis=0) - 1 / d).max() < .009
    assert abs(z.mean(axis=0) - np.arange(1, d) / np.arange(2, d + 1)).max() < .01
    # Independent beta inputs reconstruct Dirichlet(1/2,...,1/2).
    assert np.max(abs(x.sum(axis=1) - 1)) < 1e-12


if __name__ == '__main__':
    check_3d()
    check_association()
    check_stick_breaking()
    print('ELLIPSOID_JOINT_SECTION_SHADOW_CHECKS_PASSED')
