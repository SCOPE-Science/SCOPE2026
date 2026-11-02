"""Deterministic checks for the stationary four-level detuned-dot battery theorem.

Requires NumPy and SciPy. Finite calculations illustrate, but do not prove,
the parameter-uniform and infinite-detuning assertions.
"""
import math
import numpy as np
from scipy.linalg import eigh


def predicted(mu, omega, temp):
    h = omega / temp
    z = math.exp(mu / temp)
    a, b = z * math.exp(h), z * math.exp(-h)
    Z = 1.0 + 1.5 * (a + b)
    p = np.array([1.0, a, b, 0.5 * (a + b)]) / Z
    ecoef = float(p[3])
    wcoef = ecoef - min(p[0], p[2])
    etacoef = math.tanh(h) if mu <= omega else 1.0 - math.exp(-mu / temp) / math.cosh(h)
    return p, ecoef, wcoef, etacoef


def stationary(delta, mu, omega, temp, gamma, contact):
    """Exact stationary GKLS solution, 4x4 density matrix, column-major vectorization."""
    Hloc = np.array([[delta, -omega, 0.0],
                     [-omega, 0.0, -omega],
                     [0.0, -omega, 0.0]], dtype=float)
    energies, U = eigh(Hloc)
    H = np.diag(np.r_[0.0, energies])
    n = 4
    eye = np.eye(n)
    L = -1j * (np.kron(eye, H) - np.kron(H.T, eye))

    def dissipator(A):
        Q = A.conj().T @ A
        return np.kron(A.conj(), A) - 0.5 * (np.kron(eye, Q) + np.kron(Q.T, eye))

    v = U[0, :]
    P = np.zeros((n, n), dtype=complex)
    P[1:, 1:] = np.outer(v.conj(), v)
    L += gamma * dissipator(P)
    for j, ej in enumerate(energies):
        f = 1.0 / (1.0 + math.exp(max(-700.0, min(700.0, (ej - mu) / temp))))
        weight = contact * abs(U[2, j]) ** 2
        inj = np.zeros((n, n), dtype=complex)
        ext = np.zeros((n, n), dtype=complex)
        inj[j + 1, 0] = math.sqrt(weight * f)
        ext[0, j + 1] = math.sqrt(weight * (1.0 - f))
        L += dissipator(inj) + dissipator(ext)
    row = np.eye(n).reshape(-1, order="F")
    A = L.copy()
    target = np.zeros(n * n, dtype=complex)
    A[0, :] = row
    target[0] = 1.0
    rho = np.linalg.solve(A, target).reshape((n, n), order="F")
    assert np.linalg.norm(L @ rho.reshape(-1, order="F")) < 5e-9
    assert np.linalg.norm(rho - rho.conj().T) < 5e-9
    assert abs(np.trace(rho) - 1) < 5e-9
    eigvals = np.linalg.eigvalsh(rho)
    assert eigvals[0] > -1e-10
    ene = float(np.real(np.trace(H @ rho)))
    passive = float(np.dot(np.sort(eigvals)[::-1], np.sort(np.r_[0., energies])))
    return rho, ene, ene - passive


def run():
    checks = 0
    for T in [0.6, 1.0, 2.0]:
        for m in [-2.0, -0.5, 0.0, 0.8, 1.0, 1.2, 2.0, 3.0]:
            p, e, w, eta = predicted(m, 1.0, T)
            a = math.exp((m + 1) / T)
            b = math.exp((m - 1) / T)
            assert abs(sum(p) - 1.0) < 1e-14
            assert abs(p[1] / p[0] - a) < 1e-10
            assert abs(p[2] / p[0] - b) < 1e-10
            assert abs(p[3] - (p[1] + p[2]) / 2) < 1e-14
            assert abs(w / e - eta) < 5e-14
            if m <= 1.0:
                assert abs(w - math.exp(m / T) * math.sinh(1 / T) /
                           (1 + 3 * math.exp(m / T) * math.cosh(1 / T))) < 1e-14
            else:
                assert w > math.exp(m / T) * math.sinh(1 / T) / (
                    1 + 3 * math.exp(m / T) * math.cosh(1 / T))
            checks += 7

    # Validate the analytic cusp, including its strictly positive right slope.
    for T in [0.4, 1.0, 3.0]:
        left = predicted(1.0 - 1e-5, 1, T)[3]
        mid = predicted(1.0, 1, T)[3]
        right = predicted(1.0 + 1e-5, 1, T)[3]
        assert abs(left - mid) < 1e-12
        assert right > mid
        assert abs((right - mid) / 1e-5 - (1 - math.tanh(1 / T)) / T) < 5e-5
        checks += 3

    # Compare against the entire 4x4 density-matrix GKLS generator, not the
    # reduced populations used in the proof. Asymptotic errors must decrease.
    cases = [(0.0, 1.0, 10.0, .1),
             (2.0, 1.0, 10.0, .1),
             (-2.0, 1.0, 10.0, .1),
             (1.3, 0.6, 2.0, .3),
             (1.5, 2.0, 5.0, .2),
             (-1.0, 1.4, 7.0, .4)]
    for mu, temp, gamma, contact in cases:
        p, e, w, eta = predicted(mu, 1.0, temp)
        errs = []
        for delta in [300.0, 900.0]:
            rho, en, work = stationary(delta, mu, 1.0, temp, gamma, contact)
            err = max(abs(en / delta - e), abs(work / delta - w))
            errs.append(err)
            checks += 3
        assert errs[-1] < errs[0]
        assert errs[-1] < .005
        checks += 2
    # Proper high-chemical-potential asymptote at fixed, nonzero T.
    for T in [0.5, 1.0, 2.0]:
        _, E, W, eta = predicted(12.0 * T, 1.0, T)
        assert abs(E - 1.0 / 3.0) < 0.0001
        assert 0 < eta < 1
        checks += 2
    print(f"PASS: {checks} deterministic analytic, normalization, positivity, and GKLS checks")


if __name__ == "__main__":
    run()
