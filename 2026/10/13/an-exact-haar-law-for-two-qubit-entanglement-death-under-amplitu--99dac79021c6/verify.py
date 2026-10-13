"""Finite reproducibility checks for the Haar amplitude-damping survival law.

Requires Python 3.10+ and NumPy 1.24+. These checks corroborate but do not
replace the exact Gaussian and concurrence arguments.
"""
import math
import numpy as np

S = np.kron(np.array([[0, -1j], [1j, 0]], dtype=complex),
            np.array([[0, -1j], [1j, 0]], dtype=complex))


def channel(psi, q):
    k0 = np.diag([1., math.sqrt(q)])
    k1 = np.array([[0., math.sqrt(1. - q)], [0., 0.]])
    rho = np.zeros((4, 4), dtype=complex)
    for k in (k0, k1):
        for h in (k0, k1):
            v = np.kron(k, h) @ psi
            rho += np.outer(v, v.conj())
    return rho


def concurrence_direct(rho):
    vals = np.linalg.eigvals(rho @ S @ rho.conj() @ S)
    ss = sorted((math.sqrt(max(0.0, float(z.real))) for z in vals), reverse=True)
    assert max(abs(z.imag) for z in vals) < 1e-8
    return max(0., ss[0] - sum(ss[1:]))


def ppt_min(rho):
    return np.linalg.eigvalsh(rho.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4))[0]


def analytic(q):
    u = 1. - q
    return (math.atan(u) / (2 * u) + 1 / (2 * (1+u*u))) if u else 1.


def main():
    rng = np.random.default_rng(20261009)
    cases = 0
    for q in (.04, .2, .57, .93, 1.):
        for _ in range(80):
            z = rng.normal(size=4) + 1j * rng.normal(size=4)
            psi = z / np.linalg.norm(z)
            a, b, c, d = psi
            expected = 2 * q * max(0., abs(a*d - b*c) - (1-q)*abs(d)**2)
            rho = channel(psi, q)
            assert abs(concurrence_direct(rho) - expected) < 8e-8
            assert (ppt_min(rho) < -1e-10) == (expected > 1e-9)
            cases += 1
    for u in (.02, .25, .66, 1.):
        xx = (np.arange(200000) + .5) / 200000
        riemann = float(np.mean((1 + u*u*xx*xx)**-2))
        assert abs(riemann - analytic(1-u)) < 1e-10
    count = 170000
    z = (rng.normal(size=(count,4)) + 1j*rng.normal(size=(count,4)))
    delta = abs(z[:,0]*z[:,3] - z[:,1]*z[:,2])
    for q in (.15, .45, .8):
        empirical = np.mean(delta > (1-q)*abs(z[:,3])**2)
        assert abs(empirical - analytic(q)) < .008
    plateau = (2+math.pi)/8
    for q in (1e-3, 3e-4):
        approx = plateau + math.pi*q/8
        assert abs(analytic(q) - approx) < q*q
    for t in (1e-3, 2e-3):
        short = 1 - 2*t*t/3
        assert abs(analytic(math.exp(-t)) - short) < 5*t**3
    print(f'VERIFY_OK direct_concurrence_and_PPT={cases} quadrature=4 Haar_ensemble=3 time_limits=4')


if __name__ == '__main__':
    main()
