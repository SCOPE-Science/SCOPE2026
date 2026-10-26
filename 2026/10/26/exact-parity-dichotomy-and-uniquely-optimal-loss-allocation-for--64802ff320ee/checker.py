"""Reproduce scattering and fixed-loss design checks for two absorbing lattice sites.

Requires Python 3 and NumPy. These finite tests corroborate, but do not
replace, the exact scattering and uniqueness arguments in RESULT.md.
"""
import math
import numpy as np


def exact_scattering(k, distance, gamma_left, gamma_right):
    x = gamma_left / (2.0 * math.sin(k))
    y = gamma_right / (2.0 * math.sin(k))
    z = np.exp(2j * k * distance)
    den = (1 + x) * (1 + y) - x * y * z
    t = 1 / den
    r = (-x * (1 + y) - y * (1 - x) * z) / den
    return r, t


def independent_matching(k, distance, gamma_left, gamma_right):
    # Unknowns: exterior reflection r, interior right-going a,
    # interior left-going c, exterior transmission t.
    E = -2 * math.cos(k)
    e = lambda j: np.exp(1j * k * j)
    d = distance
    M = np.zeros((4, 4), complex)
    q = np.zeros(4, complex)
    # Continuity at 0: 1+r = a+c.
    M[0] = [1, -1, -1, 0]
    q[0] = -1
    # Continuity at d: a*e^ikd+c*e^-ikd=t*e^ikd.
    M[1] = [0, e(d), e(-d), -e(d)]
    # Jump equation at 0.
    M[2] = [E + 1j * gamma_left + e(1), e(1), e(-1), 0]
    # Hopping is -1, so the left and right neighbor amplitudes
    # appear with positive signs when moved to the left side.
    q[2] = -e(-1) - (E + 1j * gamma_left)
    # Jump equation at d.
    M[3] = [0, e(d - 1), e(-(d - 1)), (E + 1j * gamma_right) * e(d) + e(d + 1)]
    r, a, c, t = np.linalg.solve(M, q)
    return r, t


def poly(b, x):
    return (b**3 * (1 - 2*x) + b**2 * (6*x*x - 6*x + 1)
            + b * (-6*x**3 + 9*x*x - 4*x + 1)
            + 2*x**4 - 4*x**3 + 3*x*x - 2*x)


def optimal_fraction(b):
    lo, hi = 0.0, b
    for _ in range(90):
        mid = (lo + hi) / 2
        if poly(b, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def phase_absorption(b, x, theta):
    y = b - x
    h = 1 - math.cos(theta)
    xy = x*y
    return (2*b + 4*xy*(1+y)*h) / ((1+b)**2 + 2*xy*(1+b+xy)*h)


def main():
    rng = np.random.default_rng(271828)
    for _ in range(500):
        k = float(rng.uniform(0.05, math.pi - 0.05))
        d = int(rng.integers(1, 14))
        g1 = float(10**rng.uniform(-2, 1.5))
        g2 = float(10**rng.uniform(-2, 1.5))
        r0, t0 = exact_scattering(k,d,g1,g2)
        r1, t1 = independent_matching(k,d,g1,g2)
        assert abs(r0-r1) < 2e-10, (k,d,g1,g2,r0,r1)
        assert abs(t0-t1) < 2e-10, (k,d,g1,g2,t0,t1)
        b = (g1+g2)/(2*math.sin(k))
        x = g1/(2*math.sin(k))
        a = 1-abs(r0)**2-abs(t0)**2
        assert abs(a-phase_absorption(b,x,2*k*d)) < 2e-10
        assert -1e-11 <= a <= 1+1e-11
    for b in np.geomspace(0.0001,1000,180):
        b = float(b)
        x = optimal_fraction(b)
        assert 0 < x < b
        a = phase_absorption(b,x,math.pi)
        for f in np.linspace(0,1,101):
            assert phase_absorption(b,b*f,math.pi) <= a + 1e-10
        for f in np.linspace(0.1,0.9,9):
            assert phase_absorption(b,b*f,0) < phase_absorption(b,b*f,math.pi)
        assert a > 2*b/(1+b)**2
    for b in [100,1000,10000]:
        x = optimal_fraction(b)
        a = phase_absorption(b,x,math.pi)
        assert abs(b*b*(1-a)-0.25) < 0.005
        assert abs(x - (0.5-1/(4*b))) < 0.0001
    for b in [0.001,0.01]:
        x = optimal_fraction(b)
        assert abs(x - (b/2-b*b/8)) < 1e-6
    print('PASS: 500 independent 4x4 scattering comparisons, 180 globally scanned budget checks, phase and asymptotic tests')

if __name__ == '__main__':
    main()
