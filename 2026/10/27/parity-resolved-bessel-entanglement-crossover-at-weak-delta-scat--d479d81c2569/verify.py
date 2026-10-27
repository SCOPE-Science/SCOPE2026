"""Reproduce finite-step and Bessel-limit checks for a homogeneous delta-scattering walk.

Run: python verify.py (requires numpy and scipy).  Finite checks do not prove
uniform convergence over all sequence lengths.
"""
import numpy as np
from scipy.special import j1, jv


def limiting_radius(tau, odd):
    b = 1.0 if tau == 0.0 else float(j1(2.0 * tau) / tau)
    return (1.0 + (-1.0 if odd else 1.0) * b) / 2.0


def finite_coin_density(n, theta, points=4096):
    q = np.arange(points) * (2 * np.pi / points) - np.pi
    z = np.exp(1j * q)
    a = 1j * np.sin(theta)
    b = np.cos(theta)
    psi = np.ones((points, 2), dtype=complex) / np.sqrt(2)
    for _ in range(n):
        psi = np.column_stack((z * (a * psi[:, 0] + b * psi[:, 1]),
                               z.conjugate() * (b * psi[:, 0] + a * psi[:, 1])))
    return psi.conjugate().T @ psi / points


def position_coin_density(n, theta):
    # Full lattice recurrence, independent of momentum-space quadrature.
    amplitudes = {0: np.array([1.0, 1.0], complex) / np.sqrt(2)}
    a, b = 1j * np.sin(theta), np.cos(theta)
    for _ in range(n):
        nxt = {}
        for x, (plus, minus) in amplitudes.items():
            nxt.setdefault(x + 1, np.zeros(2, complex))[0] += a * plus + b * minus
            nxt.setdefault(x - 1, np.zeros(2, complex))[1] += b * plus + a * minus
        amplitudes = nxt
    return sum(np.outer(v, np.conj(v)) for v in amplitudes.values())


def main():
    checks = 0
    for n in range(0, 12):
        for theta in (0.0, 0.2, 0.45):
            a, b = finite_coin_density(n, theta, points=2048), position_coin_density(n, theta)
            assert np.linalg.norm(a-b, ord='fro') < 1e-12
            checks += 1
    for tau in (0.0, .1, .5, 1., 2., 3., 5., 8.):
        b_int = np.mean((np.sin(np.arange(32768) * 2 * np.pi / 32768) ** 2)
                            * np.cos(2 * tau * np.cos(np.arange(32768) * 2 * np.pi / 32768)))
        b_bessel = .5 if tau == 0 else j1(2*tau)/(2*tau)
        assert abs(b_int-b_bessel) < 1e-12
        assert abs((jv(0,2*tau)+jv(2,2*tau))/2 - b_bessel) < 1e-12
        checks += 2
        for n in (200, 201, 400, 401, 800, 801):
            rho=finite_coin_density(n, np.arctan(tau / n))
            r=(rho[0,1]+rho[1,0]).real
            target=limiting_radius(tau, bool(n%2))
            assert abs(np.trace(rho).real-1)<1e-12
            assert abs(rho[0,0]-0.5)<1e-12
            assert abs(rho[1,1]-0.5)<1e-12
            assert abs(r-target)<0.004
            checks+=4
    print('PASS: {} direct finite-step / lattice / Bessel checks'.format(checks))

if __name__ == '__main__':
    main()
