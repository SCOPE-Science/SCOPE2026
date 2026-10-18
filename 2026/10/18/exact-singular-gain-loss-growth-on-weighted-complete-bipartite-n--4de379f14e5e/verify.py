"""Reproduce exact and numerical checks for the weighted bipartite gain-loss model."""
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm


def hamiltonian(a, b, eta, gamma):
    assert a >= 3 and b >= 1 and eta >= 0 and gamma >= 0
    w = np.array([1., 1.] + [float(eta)] * (a - 2))
    h = np.zeros((a + b, a + b), dtype=complex)
    h[:a, a:] = w[:, None]
    h[a:, :a] = w[None, :]
    h[0, 0], h[1, 1] = 1j * gamma, -1j * gamma
    return h


def growth_rate(a, b, eta, gamma):
    c = a - 2
    A = b * (2 + c * eta ** 2) - gamma ** 2
    C = gamma ** 2 * b * c * eta ** 2
    root = math.hypot(A, 2 * math.sqrt(C))
    negative_square = 2 * C / (root + A) if (A >= 0 and C > 0) else (root - A) / 2
    return math.sqrt(negative_square)


def check():
    z, gam, b, c, eta = sp.symbols('z gamma b c eta', positive=True, real=True)
    r = sp.sqrt(2 * b)
    t = eta * sp.sqrt(b * c)
    B = sp.Matrix([[0, sp.I * gam, 0, 0],
                   [sp.I * gam, 0, 0, r],
                   [0, 0, 0, t],
                   [0, r, t, 0]])
    p = z**4 + (gam**2 - b * (2 + c * eta**2)) * z**2 - gam**2 * b * c * eta**2
    assert sp.simplify((z * sp.eye(4) - B).det() - p) == 0
    assert sp.factor(p.subs(eta, 0)) == z**2 * (z**2 + gam**2 - 2*b)
    n_spectral = 0
    for a in range(3, 9):
        for bb in range(1, 7):
            for ee in [0.001, 0.1, 0.7, 1., 3.]:
                for gg in [0.03, 0.7, 2., 5.]:
                    eig = np.linalg.eigvals(hamiltonian(a, bb, ee, gg))
                    mu = growth_rate(a, bb, ee, gg)
                    assert abs(np.max(eig.imag) - mu) < 2e-8
                    assert abs(np.min(eig.imag) + mu) < 2e-8
                    n_spectral += 1
    n_asymptotic = 0
    for a, bb in [(3, 1), (3, 3), (7, 4)]:
        for gg in [0.3, 0.95 * math.sqrt(2 * bb)]:
            target = gg * math.sqrt(bb * (a - 2) / (2 * bb - gg * gg))
            ee = 1e-5
            assert abs(growth_rate(a, bb, ee, gg) / (ee * target) - 1) < 1e-5
            n_asymptotic += 1
        for ee in [1e-3, 1e-4]:
            target = math.sqrt(bb) * (2*(a - 2)) ** .25
            assert abs(growth_rate(a, bb, ee, math.sqrt(2 * bb)) / math.sqrt(ee) / target - 1) < 2e-3
            n_asymptotic += 1
        for kk in [-5., 0., 4.]:
            ee = 1e-5
            gg = math.sqrt(2*bb + kk*ee)
            target = math.sqrt((math.hypot(kk, math.sqrt(8 * bb * bb * (a-2))) + kk) / 2)
            assert abs(growth_rate(a, bb, ee, gg) / math.sqrt(ee) / target - 1) < 2e-4
            n_asymptotic += 1
    n_jordan = 0
    for bb in [1, 2, 4]:
        h = hamiltonian(3, bb, 0, math.sqrt(2*bb))
        assert np.linalg.norm(np.linalg.matrix_power(h, 3)) < 1e-11
        assert np.linalg.norm(np.linalg.matrix_power(h, 2)) > 1e-3
        q1 = np.linalg.norm(expm(-1j*100*h), 2) / 100**2
        q2 = np.linalg.norm(expm(-1j*400*h), 2) / 400**2
        assert abs(q1-q2)/q2 < .03
        n_jordan += 1
    print('PASS: 1 symbolic quartic, 1 decoupled factorization,',
          n_spectral, 'full-matrix spectral checks,', n_asymptotic,
          'asymptotic checks,', n_jordan, 'third-order Jordan checks')


if __name__ == '__main__':
    check()
