"""Finite-matrix checks for the lossy two-sublattice quantum-walk result.

Dependencies: numpy and scipy. Checks are finite corroboration, not a proof
of the all-size strong-loss and logarithmic-limit statements.
"""
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh, solve_continuous_lyapunov


def blocks(n, a, b):
    """Real-space Hermitian blocks, consistent with open endpoints."""
    A = np.zeros((n, n), dtype=complex)
    W = np.eye(n, dtype=complex) * a
    for j in range(n - 1):
        A[j + 1, j] = 1j * b / 2
        A[j, j + 1] = -1j * b / 2
        W[j, j + 1] = W[j + 1, j] = b / 2
    return A, W


def zeno_limit(n, source, a, b, weights):
    """Spectral-projector construction independent of sine formulas."""
    A, W = blocks(n, a, b)
    _, U = eigh(A)
    B = W @ U
    f = abs(B) ** 2 / weights[:, None]
    return (f / f.sum(axis=0)[None, :]) @ abs(U[source - 1, :]) ** 2


def sine_formula(n, source, a, b, weights):
    ks = np.arange(1, n + 1)
    q = np.pi * ks / (n + 1)
    initial = 2 * np.sin(source * q) ** 2 / (n + 1)
    f = np.array([(a*a*np.sin(j*q)**2 + b*b*np.sin(q)**2*np.cos(j*q)**2) / weights[j-1]
                  for j in range(1, n + 1)])
    return (f / f.sum(axis=0)[None, :]) @ initial


def finite_loss(n, source, a, b, weights, gamma):
    A, W = blocks(n, a, b)
    H = np.block([[A, W], [W, -A - 1j * gamma * np.diag(weights)]])
    M = -1j * H
    rho = np.zeros((2*n, 2*n), dtype=complex)
    rho[source-1, source-1] = 1
    integrated_density = solve_continuous_lyapunov(M, -rho)
    return 2 * gamma * weights * np.real(np.diag(integrated_density)[n:])


def coefficient(a, b):
    return 4 / np.pi * quad(
        lambda q: np.sin(q)**4 * (a*a + b*b*np.cos(q)**2)
        / (a*a + b*b*np.sin(q)**2), 0, np.pi, epsabs=1e-12)[0]


def main():
    sample_count = 0
    max_modal_difference = 0
    max_mirror_residual = 0
    max_finite_difference = 0
    for n in range(2, 12):
        for s in sorted({1, n, (n+1)//2}):
            rng = np.random.default_rng(300*n+s)
            w = rng.uniform(.4, 2.2, n)
            a, b = .3 + .07*(n % 3), .5 + .06*(s % 3)
            p = zeno_limit(n, s, a, b, w)
            q = sine_formula(n, s, a, b, w)
            max_modal_difference = max(max_modal_difference, np.max(abs(p-q)))
            max_mirror_residual = max(max_mirror_residual,
                max(abs(w[j]*q[j]-w[n-j-1]*q[n-j-1]) for j in range(n)))
            assert np.all(q > 0) and abs(sum(q)-1) < 2e-12
            if n <= 8:
                observed = finite_loss(n, s, a, b, w, 1500)
                max_finite_difference = max(max_finite_difference, np.max(abs(observed-q)))
                assert abs(sum(observed)-1) < 1e-5
            sample_count += 1
    assert max_modal_difference < 1e-12, max_modal_difference
    assert max_mirror_residual < 1e-12, max_mirror_residual
    assert max_finite_difference < 0.008, max_finite_difference
    c = coefficient(.3, .5)
    assert 0.7374 < c < 0.7376
    for n in (60, 120, 500, 1200):
        w = np.arange(1, n+1, dtype=float)
        p = sine_formula(n, n, .3, .5, w)
        assert abs(p[0]/p[-1]-n) < 1e-7
        print(f"N={n}: endpoint_loss={p[0]:.10f}; "+
              f"logN_times_endpoint={np.log(n)*p[0]:.10f}; ratio={p[0]/p[-1]:.8f}")
    print('integral_constant:', f'{c:.12f}')
    print('small_size_configs:', sample_count)
    print('max_spectral_formula_difference:', f'{max_modal_difference:.3g}')
    print('max_weighted_mirror_residual:', f'{max_mirror_residual:.3g}')
    print('max_abs_error_gamma_1500:', f'{max_finite_difference:.5g}')
    print('All finite verification checks passed.')


if __name__ == '__main__':
    main()
