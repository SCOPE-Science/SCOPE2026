"""Numerical checks for the Fourier-mean singularities of planar Fermat balls.

Requires Python 3 with SciPy. The analytic proof supplies the universal claims;
this script checks independent exact identities and oscillatory integrals.
"""
from math import pi, sqrt, sin, cos, gamma, isclose
from scipy.integrate import quad
from scipy.special import j1


def parameters(q):
    alpha = 1.0 + 1.0 / q
    exponent = 2.0 + 2.0 / q
    volume = 4.0 * gamma(alpha)**2 / gamma(1.0+2.0/q)
    amplitude = 4.0 * q**(1.0/q) * gamma(alpha)
    residue = 4.0 * (1.0+1.0/q) * q**(2.0/q) * gamma(1.0+2.0/q)
    return alpha, exponent, volume, amplitude, residue


def axial_fourier(q, frequency):
    return quad(lambda x: 4.0 * max(0.0, 1.0-x**q)**(1.0/q),
                0.0, 1.0, weight='cos', wvar=frequency,
                epsabs=8e-10, epsrel=8e-10, limit=800)[0]


def verify():
    checks = 0
    for q in (2, 4, 6, 8, 10):
        alpha, exponent, area, amplitude, residue = parameters(q)
        beta_area = 4.0 * quad(lambda t: (1-t**q)**(1.0/q),
                               0.0, 1.0, epsabs=1e-10)[0]
        assert isclose(area, beta_area, rel_tol=1.5e-9)
        checks += 1
        assert isclose(exponent*amplitude**2/(2*area), residue, rel_tol=2e-14)
        checks += 1
        for n in (10, 20, 30, 40, 60):
            frequency = 2*pi*n + pi*alpha/2
            got = axial_fourier(q, frequency)
            asymptotic = amplitude*frequency**(-alpha)
            assert abs(got/asymptotic-1) < 0.002
            checks += 1
    assert isclose(parameters(2)[-1], 12.0, rel_tol=1e-14)
    checks += 1
    assert isclose(parameters(4)[-1], 5*sqrt(pi), rel_tol=1e-14)
    checks += 1
    for frequency in (5.3, 21.2, 60.1, 205.7):
        got = axial_fourier(2, frequency)
        expect = 2*pi*j1(frequency)/frequency
        assert abs(got-expect) < 2e-8
        checks += 1
    for q in (100, 1000, 10000):
        assert abs(parameters(q)[-1]-4) < 0.5
        checks += 1
    assert isclose(2.0*2.0, 4.0, rel_tol=1e-14)  # square critical residue
    checks += 1
    print(f"PASS: {checks} checks of area, amplitude, residue, and endpoint models")


if __name__ == '__main__':
    verify()
