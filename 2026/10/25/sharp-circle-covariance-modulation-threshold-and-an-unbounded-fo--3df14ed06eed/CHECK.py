"""Reproduce finite diagnostics for a circular geodesic covariance theorem.

All proofs of claims over infinitely many modes are in RESULT.md, not here.
Uses Python 3 standard library only.
"""
from math import exp, pi, cos, sin, sqrt, tanh, isclose


def fourier_unmodulated(a, n):
    return a * (1 - (-1)**n * exp(-pi*a)) / (pi*(a*a+n*n))


def factor(A, x):
    return ((A+(x-1)**2)*(A+(x+1)**2))/((A+x*x)*(A+x*x+1))


def center(A):
    return sqrt((A+1+2*sqrt(4*A*A+5*A+1))/3)


def ratio(a, n):
    h = tanh(pi*a/2)
    return factor(a*a, n) * (h if n % 2 == 0 else 1/h)


def candidates(a):
    s = center(a*a)
    out = []
    for first in (1, 2):
        below = first
        if s >= first:
            below = first + 2*int((s-first)//2)
        out.extend((below, below+2))
    return sorted(set(out))


def integral_coeff(a, n, steps=12000):
    # Simpson on [0, pi], normalized even Fourier coefficient.
    dt = pi / steps
    z = exp(-a*pi)*cos(n*pi) + 1
    for k in range(1, steps):
        t = k*dt
        z += (4 if k & 1 else 2)*exp(-a*t)*cos(n*t)
    return dt*z/(3*pi)


def test():
    for a in (0.02, 0.12, 0.7, 1.0, 1.8, 2.9, 6.0):
        for n in (0, 1, 2, 3, 8):
            exact = fourier_unmodulated(a, n)
            assert abs(integral_coeff(a, n)-exact) < 2e-8, (a, n)
        for n in range(1, 30):
            num = 2*fourier_unmodulated(a, n)
            den = fourier_unmodulated(a, n-1) + fourier_unmodulated(a, n+1)
            assert isclose(num/den, ratio(a, n), rel_tol=2e-12)
        finite = min(ratio(a, n) for n in candidates(a))
        direct = min(ratio(a, n) for n in range(1, 2000))
        assert isclose(finite, direct, rel_tol=5e-13), (a, finite, direct)
        assert 0 < finite < tanh(pi*a/2)
    for n in range(2, 31):
        A = (-(n*n+3)+2*sqrt(4*n**4-n*n+1))/5
        a = sqrt(A)
        assert abs(center(A)-n) < 1e-11
        if n >= 8:
            winning = min(range(1, 150), key=lambda k: ratio(a, k))
            assert winning == n, (n, winning)
    for a in (0.0003, 0.001, 0.003):
        B = min(ratio(a,n) for n in candidates(a))
        assert abs(B/a - 9*pi/40) < 2e-3
    for a in (20., 50., 100.):
        B = min(ratio(a,n) for n in candidates(a))
        assert abs(a*a*(1-B)-9/16) < 0.01
    print('PASS: quadrature, ratio identities, finite mode selection, and sampled asymptotics')


if __name__ == '__main__':
    test()
