"""Reproduce numeric spot checks for the Laplace Gabor Zak spectral law.
Requires Python 3.9+, scipy. Analytical proof is in RESULT.md.
"""
import cmath
import math
from scipy.integrate import quad
from scipy.optimize import brentq


def zak_window(lam, x, w, N=55):
    return sum(math.exp(-lam * abs(x + k)) * cmath.exp(-2j * math.pi * k * w)
               for k in range(-N, N + 1))


def symbol(lam, x, theta):
    r = math.exp(-2 * lam)
    u = math.cos(theta)
    D = 1 - 2 * r * u + r * r
    P = (1 - r * r) / D
    Q = r * ((1 + r * r) * u - 2 * r) / (D * D)
    H = math.cosh(lam * (1 - 2 * x)) / math.sinh(lam)
    return 2 * (H * P + 4 * Q)


def density(lam, energy):
    r = math.exp(-2 * lam)
    low, high = 1 / math.sinh(lam), 1 / math.tanh(lam)
    def PQ(theta):
        u = math.cos(theta)
        den = 1 - 2 * r * u + r * r
        return (1 - r * r) / den, r * ((1 + r * r) * u - 2 * r) / den**2
    def ef(theta, h):
        p, q = PQ(theta)
        return 2 * (h * p + 4 * q)
    ends = [0, math.pi]
    for h in [low, high]:
        f0, f1 = ef(0, h) - energy, ef(math.pi, h) - energy
        if f0 * f1 < 0:
            ends.append(brentq(lambda t: ef(t, h) - energy, 0, math.pi))
    ends.sort()
    def integrand(theta):
        p, q = PQ(theta)
        h = (energy / 2 - 4 * q) / p
        if not low < h < high:
            return 0.0
        return 1 / (2 * math.pi * lam * p * math.sqrt(h * h - low * low))
    return sum(quad(integrand, a, b, epsabs=2e-8, epsrel=2e-8, limit=220)[0]
               for a, b in zip(ends, ends[1:]))


def invariants(lam):
    r = math.exp(-2 * lam)
    low = 1 / math.sinh(lam)
    xx = 8 * lam * lam * low * (1 + r) / (1 - r)
    tt = 4 * r * (low * (1 + r) / (1 - r)**3
                  + 2 * (1 + 4 * r + r*r) / (1-r)**4)
    a = 4 * lam * math.tanh(lam)
    b = 1.5 * math.tanh(lam)**2 / math.cosh(lam)**2
    return (2 / (math.cosh(lam)-1), 2 * math.tanh(lam)**2,
            1 / (math.pi * math.sqrt(xx * tt)),
            2 / (math.pi * a * math.sqrt(b)))


if __name__ == '__main__':
    checks = 0
    for lam in [0.6, 1.0, 2.0]:
        for x in [0.11, 0.37, 0.73]:
            for w in [0.071, 0.139, 0.377]:
                direct = (abs(zak_window(lam, x, w))**2
                          + abs(zak_window(lam, x, w + 0.5))**2)
                assert abs(direct - symbol(lam, x, 4 * math.pi * w)) < 2e-10
                checks += 1
    # Quantitative verification on both sides of a logarithmic saddle.
    for lam in [0.6, 1.0, 2.0]:
        saddle, corner, logc, cuspc = invariants(lam)
        delta = min(1e-5, 1e-4 * abs(saddle - corner))
        for sign in [-1, 1]:
            d1 = density(lam, saddle + sign * delta)
            d2 = density(lam, saddle + sign * delta / 100)
            measured = (d2 - d1) / math.log(100)
            assert abs(measured - logc) < 0.008, (lam, measured, logc)
            checks += 1
        # Sharp one-sided square-root cusp at the nonanalytic Zak seam.
        measured = (density(lam, corner - delta) - density(lam, corner + delta)) / math.sqrt(delta)
        assert abs(measured - cuspc) < 0.04, (lam, measured, cuspc)
        checks += 1
    root = brentq(lambda c: c**3 - 2*c*c-c+1, 2, 3, xtol=2e-15, rtol=9e-16)
    lam = math.acosh(root)
    saddle, corner, _, _ = invariants(lam)
    assert abs(saddle-corner) < 2e-14
    assert abs(root-(1+2*math.cos(2*math.pi/7))) < 2e-14
    checks += 2
    print('PASS:', checks, 'independent Zak, spectral-singularity and cubic-transition checks')
