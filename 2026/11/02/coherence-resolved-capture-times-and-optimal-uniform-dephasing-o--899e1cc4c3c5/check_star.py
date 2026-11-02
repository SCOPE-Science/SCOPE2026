"""Independent numerical checks for a dephased quantum-star first-absorption theorem.

Usage: python check_star.py
Dependencies: numpy, scipy. Uses a full density-matrix Liouvillian rather than
symmetry reduction. All rates are in the population-decay convention.
"""
import numpy as np
from scipy.linalg import solve


def liouvillian(n, hop, sink, leaf_noise, hub_noise):
    dim = n + 1
    H = np.zeros((dim, dim), complex)
    H[0, 1:] = hop
    H[1:, 0] = hop
    ident = np.eye(dim, dtype=complex)
    q = np.zeros((dim, dim), complex)
    q[0, 0] = 1
    L = -1j * (np.kron(ident, H) - np.kron(H.T, ident))
    L -= sink / 2 * (np.kron(ident, q) + np.kron(q.T, ident))
    for j, rate in enumerate([hub_noise] + [leaf_noise] * n):
        p = np.zeros_like(q)
        p[j, j] = 1
        L += rate * (np.kron(p.conj(), p) - 0.5 * np.kron(ident, p) - 0.5 * np.kron(p.T, ident))
    return L


def analytic_observable(n, hop, sink, leaf_noise, hub_noise):
    dim = n + 1
    h = (n + 1) / sink
    eta = (sink + leaf_noise + hub_noise) / (4 * hop**2)
    x = np.zeros((dim, dim), complex)
    x[0, 0] = h
    x[1:, 1:] = (h + eta + n / leaf_noise) * np.eye(n) - np.ones((n, n)) / leaf_noise
    x[0, 1:] = 1j / (2 * hop)
    x[1:, 0] = -1j / (2 * hop)
    return x


def analytic_mean(n, hop, sink, leaf_noise, hub_noise, rho):
    bright = np.ones(n) / np.sqrt(n)
    b = np.vdot(bright, rho[1:, 1:] @ bright).real
    return ((n + 1) / sink + (sink + leaf_noise + hub_noise) / (4 * hop**2)
            + n * (1 - b) / leaf_noise)


def run():
    rng = np.random.default_rng(20261027)
    cases = 0
    maximum_relative_error = 0.0
    maximum_observable_residual = 0.0
    for n in range(2, 8):
        dim = n + 1
        for _ in range(6):
            hop, sink, leaf, hub = np.exp(rng.uniform(-1.4, 1.4, 4))
            if _ % 2 == 0:
                hub = 0.0
            L = liouvillian(n, hop, sink, leaf, hub)
            x = analytic_observable(n, hop, sink, leaf, hub)
            residual = L.conj().T @ x.reshape(-1, order="F") + np.eye(dim).reshape(-1, order="F")
            err = np.max(np.abs(residual))
            maximum_observable_residual = max(maximum_observable_residual, float(err))
            assert err < 2e-10, ('observable', n, err)
            assert np.min(np.linalg.eigvalsh(x)) > 0, 'observable positivity'
            bright = np.zeros(dim, complex)
            bright[1:] = 1 / np.sqrt(n)
            dark = np.zeros(dim, complex)
            dark[1:3] = [1 / np.sqrt(2), -1 / np.sqrt(2)]
            for which in range(5):
                if which == 0:
                    psi = np.eye(dim, dtype=complex)[1]
                    rho = np.outer(psi, psi.conj())
                elif which == 1:
                    rho = np.outer(bright, bright.conj())
                elif which == 2:
                    rho = np.outer(dark, dark.conj())
                elif which == 3:
                    z = rng.normal(size=n) + 1j * rng.normal(size=n)
                    z /= np.linalg.norm(z)
                    psi = np.concatenate(([0j], z))
                    rho = np.outer(psi, psi.conj())
                else:
                    a = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
                    a = a @ a.conj().T
                    a /= np.trace(a)
                    rho = np.zeros((dim, dim), complex)
                    rho[1:, 1:] = a
                integrated = solve(-L, rho.reshape(-1, order="F")).reshape(dim, dim, order="F")
                direct = np.trace(integrated).real
                predicted = analytic_mean(n, hop, sink, leaf, hub, rho)
                rel = abs(direct - predicted) / max(1, abs(predicted))
                maximum_relative_error = max(maximum_relative_error, float(rel))
                assert rel < 2e-9, (n, which, predicted, direct)
                cases += 1
    # Check exact optimizer by an analytic reciprocal/linear profile for nonbright starts.
    for n in (2, 5, 9):
        hop, sink, hub = 0.7, 1.2, 0.3
        rho = np.zeros((n + 1, n + 1), complex)
        rho[1, 1] = 1
        w = (n - 1) / n
        gopt = 2 * hop * np.sqrt(n * w)
        minimum = analytic_mean(n, hop, sink, gopt, hub, rho)
        expected = (n + 1) / sink + (sink + hub) / (4 * hop**2) + np.sqrt(n * w) / hop
        assert abs(minimum - expected) < 1e-12
        for factor in (0.1, 0.5, 1.5, 2.0, 10.0):
            assert analytic_mean(n, hop, sink, factor * gopt, hub, rho) > minimum
    print(f'PASS {cases} full-Liouvillian first-moment comparisons; '
          f'maximum relative error {maximum_relative_error:.3e}; '
          f'maximum adjoint residual {maximum_observable_residual:.3e}; '
          'positive observables; analytic minimizers checked.')


if __name__ == '__main__':
    run()
