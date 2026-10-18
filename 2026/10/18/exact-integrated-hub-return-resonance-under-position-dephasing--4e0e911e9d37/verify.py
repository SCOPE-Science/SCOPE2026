"""Independent finite checks for universal-vertex position-dephasing theorem.

Requires numpy and scipy; finite tests corroborate, but do not prove, universal statements.
"""
import itertools
import math

import numpy as np
from scipy.linalg import expm


def graph_laplacian(k, leaf_edges):
    n = k + 1
    a = np.zeros((n, n), dtype=float)
    a[0, 1:] = 1.0
    a[1:, 0] = 1.0
    for i, j in leaf_edges:
        assert 1 <= i < j <= k
        a[i, j] = a[j, i] = 1.0
    return np.diag(a.sum(axis=1)) - a


def full_liouvillian(lap, gamma):
    # Column-major vectorization: vec(H rho)=(I kron H)vec(rho).
    n = len(lap)
    eye = np.eye(n)
    liouv = -1j * (np.kron(eye, lap) - np.kron(lap, eye))
    for j in range(n):
        p = np.zeros((n, n))
        p[j, j] = 1.0
        liouv += gamma * (np.kron(p, p) - .5 * (np.kron(eye, p) + np.kron(p, eye)))
    return liouv


def reduced(k, gamma):
    return np.array([[0., 0., 2. * (k + 1)],
                     [0., -gamma, float(k + 1)],
                     [-1., -(k - 1.), -gamma]])


def formula(k, gamma):
    return (gamma * gamma + k * k - 1) / (2 * (k + 1) * gamma)


def run():
    checks = 0
    time_grid = [0.03, .2, .7, 1.6, 2.9]
    for k in [2, 3, 4, 5, 6]:
        possibilities = list(itertools.combinations(range(1, k + 1), 2))
        edge_sets = [[], possibilities, possibilities[:1],
                     possibilities[::2], possibilities[1::2]]
        for gamma in [0.23, 1.0, math.sqrt(k * k - 1), 2.4]:
            m = reduced(k, gamma)
            p = (k + 1)
            assert np.allclose(np.linalg.eigvals(m).real < 0, True)
            assert abs(np.linalg.solve(-m, np.array([1., 0., 0.]))[0] - formula(k, gamma)) < 2e-12
            checks += 1
            baseline = {}
            for edges in edge_sets:
                lap = graph_laplacian(k, edges)
                liouv = full_liouvillian(lap, gamma)
                rho0 = np.zeros(((k + 1), (k + 1)), dtype=complex)
                rho0[0, 0] = 1.0
                v0 = rho0.flatten(order='F')
                for t in time_grid:
                    state = (expm(t * liouv) @ v0).reshape((p, p), order='F')
                    x = (p * state[0, 0].real - 1.) / k
                    xr = (expm(t * m) @ np.array([1., 0., 0.]))[0]
                    assert abs(x - xr) < 1e-10, (k, gamma, t, edges, x, xr)
                    if t in baseline:
                        assert np.linalg.norm(state - baseline[t]) < 2e-10
                        checks += 1
                    else:
                        baseline[t] = state.copy()
                    assert abs(np.trace(state) - 1) < 2e-10
                    assert np.linalg.eigvalsh(state).min() > -2e-10
                    # Entire state, not only center probability, is uniform on leaves.
                    diagonal = np.diag(state)[1:]
                    assert max(abs(diagonal - diagonal[0])) < 1e-10
                    checks += 1
    for k in [2, 3, 6, 10, 100]:
        opt = math.sqrt(k * k - 1)
        assert formula(k, opt) <= formula(k, opt * 1.01)
        assert formula(k, opt) <= formula(k, opt / 1.01)
        assert abs(formula(k, opt) - math.sqrt((k - 1) / (k + 1))) < 1e-12
        checks += 1
    for theta in [.6, 1., 1.8]:
        rate = 2 * theta / (1 + theta * theta)
        for k in [100, 500, 2000]:
            m = reduced(k, theta * k)
            for t in [.02, .2, 1., 3., 7.]:
                x = (expm(t * m) @ np.array([1., 0., 0.]))[0]
                assert abs(x - math.exp(-rate * t)) < 0.03, (k, theta, t, x)
                checks += 1
    print(f'VERIFY_OK {checks} direct full-Lindblad / resolvent / optimizer / scaling checks')


if __name__ == '__main__':
    run()
