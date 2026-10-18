"""Standalone numerical cross-checks for a lossy dephased star.

Requires numpy and scipy. The analytic proof is independent of this script.
No network access, proprietary material, or external data are required.
"""
import numpy as np
from scipy.linalg import solve
from scipy.optimize import minimize_scalar


def mean_full(m, J, kappa, gamma, rho):
    """Numerically invert the full trace-decreasing Lindblad generator."""
    n = m + 1
    h = np.zeros((n, n), dtype=complex)
    h[0, 1:] = J
    h[1:, 0] = J
    E = np.eye(n)
    loss = np.zeros((n, n), dtype=complex)
    loss[0, 0] = kappa
    # Column-major vec: vec(A X B)=(B.T kron A) vec(X).
    L = -1j * (np.kron(E, h) - np.kron(h.T, E))
    L -= 0.5 * (np.kron(E, loss) + np.kron(loss.T, E))
    for j in range(n):
        P = np.zeros((n, n), dtype=complex)
        P[j, j] = 1.0
        L += gamma * (np.kron(P, P) - .5 * np.kron(E, P) - .5 * np.kron(P.T, E))
    integrated = solve(-L, rho.reshape(n*n, order='F'), assume_a='gen')
    integrated = integrated.reshape((n, n), order='F')
    return np.trace(integrated).real


def mean_claim(m, J, kappa, gamma, rho):
    s = np.real(np.sum(rho[1:, 1:]))
    return (m+1)/kappa + kappa/(4*J*J) + gamma/(2*J*J) + (m-s)/gamma


def main():
    rng = np.random.default_rng(73194)
    count = 0
    max_abs = 0.0
    max_rel = 0.0
    for m in (2, 3, 4, 5, 7):
        n = m+1
        for J in (.6, 1.7):
            for kappa in (.35, 2.4):
                for gamma in (.15, .73, 3.2):
                    states = []
                    bright = np.zeros(n, complex); bright[1:] = 1/np.sqrt(m)
                    states.append(np.outer(bright, bright.conj()))
                    localized = np.zeros(n, complex); localized[1] = 1
                    states.append(np.outer(localized, localized.conj()))
                    for _ in range(2):
                        v = rng.normal(size=m)+1j*rng.normal(size=m)
                        v = v / np.linalg.norm(v)
                        psi = np.zeros(n, complex); psi[1:] = v
                        states.append(np.outer(psi, psi.conj()))
                    v = rng.normal(size=(m, m))+1j*rng.normal(size=(m, m))
                    r = v@v.conj().T; r = r/np.trace(r)
                    rho_mix = np.zeros((n,n), complex); rho_mix[1:,1:] = r
                    states.append(rho_mix)
                    for rho in states:
                        actual = mean_full(m, J, kappa, gamma, rho)
                        expected = mean_claim(m, J, kappa, gamma, rho)
                        err = abs(actual-expected)
                        max_abs = max(max_abs, err)
                        max_rel = max(max_rel, err/max(1,abs(expected)))
                        assert np.isclose(actual,expected,rtol=2e-10,atol=3e-10), (m,J,kappa,gamma,actual,expected)
                        count += 1
        # Independent numerical minimization for initially localized leaf.
        rho = np.zeros((n,n), complex); rho[1,1] = 1
        s = 1
        for J, kappa in ((.4, .5),(1.1, 2.9)):
            optimum = J*np.sqrt(2*(m-s))
            r = minimize_scalar(lambda g: mean_full(m,J,kappa,g,rho),
                                bounds=(optimum*.25,optimum*3),method='bounded',
                                options={'xatol':1e-10})
            assert abs(r.x-optimum)/optimum < 2e-5, (m,r.x,optimum)
            count += 1
    # At zero dephasing the bright mode reduces exactly to a lossy two-level problem.
    for m in (2,3,5,10):
        for J in (.5,1.3):
            for kappa in (.7,3.0):
                # The explicit zero-noise result (derived analytically) is a boundary check.
                analytic_zero = 2/kappa+kappa/(4*m*J*J)
                limit_positive = (m+1)/kappa+kappa/(4*J*J)
                assert limit_positive > analytic_zero
                count += 1
    print(f'PASS: {count} independent checks; max_abs={max_abs:.3e}; max_rel={max_rel:.3e}')

if __name__ == '__main__':
    main()
