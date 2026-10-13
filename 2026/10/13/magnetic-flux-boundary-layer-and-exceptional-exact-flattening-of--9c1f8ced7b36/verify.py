#!/usr/bin/env python3
"""Reproduce finite checks for magnetic-flux time-average cycle formulas.

Scientific proof of general statements is analytic; these are independent
finite-size evaluations and numerical illustrations only.
"""
import math
import cmath

PI = math.pi


def integral_kernel(z):
    if abs(z) < 1e-14:
        return 1.0 + 0.0j
    return cmath.exp(0.5j*z) * math.sin(0.5*z)/(0.5*z)


def energies(n, alpha):
    return [2.0*math.cos(2*PI*(k+alpha)/n) for k in range(n)]


def finite_window(n, duration, alpha):
    """Exact time integral of the Fourier spectral pair sum."""
    e = energies(n, alpha)
    out = []
    for j in range(n):
        s = 0j
        for k in range(n):
            for l in range(n):
                s += (cmath.exp(2j*PI*(k-l)*j/n)
                      * integral_kernel(-duration*(e[k]-e[l])))
        out.append((s/(n*n)).real)
    return out


def limiting_profile(n, tau):
    out = []
    for j in range(n):
        s = 1.0/n
        for k in range(n):
            if (2*k) % n == 0:
                continue
            arg = (8*PI*tau/n)*math.sin(2*PI*k/n)
            s += (cmath.exp(4j*PI*k*j/n)*integral_kernel(arg)).real/(n*n)
        out.append(s)
    return out


def pointwise_probabilities(n, t, alpha):
    e = energies(n, alpha)
    out = []
    for j in range(n):
        amplitude = sum(cmath.exp(2j*PI*k*j/n-1j*e[k]*t)
                        for k in range(n))/n
        out.append(abs(amplitude)**2)
    return out


def simpson_average(n, duration, alpha, intervals=4096):
    if intervals % 2:
        raise ValueError('Simpson integration requires even intervals')
    accumulated = [0.0]*n
    for m in range(intervals+1):
        w = 1 if m == 0 or m == intervals else (4 if m % 2 else 2)
        p = pointwise_probabilities(n, duration*m/intervals, alpha)
        for j in range(n):
            accumulated[j] += w*p[j]
    return [v/(3*intervals) for v in accumulated]


def near(v, w, tol):
    return max(abs(a-b) for a, b in zip(v, w)) < tol


def test():
    # Direct Born-probability quadrature vs the exact finite spectral integral.
    for n in (3, 4, 6, 8):
        for a, duration in ((0.11, 3.7), (0.27, 7.3)):
            exact = finite_window(n, duration, a)
            quad = simpson_average(n, duration, a)
            assert near(exact, quad, 1e-7), (n, a, exact, quad)
            assert abs(sum(exact)-1.0) < 1e-10
            assert min(exact) >= -1e-10

    # Every integer multiple in each of the three exceptional families.
    for n, base in ((3, math.sqrt(3)/2), (4, 0.5),
                    (6, math.sqrt(3)/2)):
        for multiple in (1, 2, 3):
            p = limiting_profile(n, multiple*base)
            assert near(p, [1/n]*n, 2e-12), (n, multiple, p)

    # Comparison with exact unfluxed limiting return probabilities.
    for n in range(3, 15):
        p0 = limiting_profile(n, 0.0)
        expected_return = 1.0/n + (n-1-(1 if n % 2 == 0 else 0))/(n*n)
        assert abs(p0[0]-expected_return) < 1e-12
        assert abs(sum(p0)-1) < 1e-12
        assert abs(max(p0)-1/n) > 1e-5

    # Finite-duration functions converge to their near-degenerate profile.
    for n in range(3, 13):
        for tau in (0.15, 0.67, 1.31):
            q = limiting_profile(n, tau)
            approx = finite_window(n, 5000.0, tau/5000.0)
            assert near(q, approx, 0.001), (n, tau)
            assert abs(sum(q)-1.0) < 1e-11
            assert min(q) >= -1e-12

    # Fixed generic flux has a uniform long-time average.
    for n in range(3, 13):
        p = finite_window(n, 10000.0, 0.123)
        assert near(p, [1/n]*n, 0.002), (n, p)

    # Illustrative non-resonances (not a numerical proof of the classification).
    for n in (5, 7, 8, 9, 10, 11, 12):
        p = limiting_profile(n, 1.0)
        assert max(abs(v-1/n) for v in p) > 1e-4

    print('VERIFY_OK chiral_cycle_flux_window=passed')


if __name__ == '__main__':
    test()
