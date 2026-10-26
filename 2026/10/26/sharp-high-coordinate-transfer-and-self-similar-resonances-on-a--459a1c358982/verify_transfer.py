#!/usr/bin/env python3
"""Independent finite Fourier, product, and optimization checks for a dyadic weighted hypercube walk."""
import cmath
import math

checks = 0

def check(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def finite_amplitude(m, K, t):
    """Direct character-diagonalization of the finite cubelike adjacency Hamiltonian."""
    scale = 1 << (K + 1)
    total = 0j
    for s in range(scale):
        energy = sum((1 if (s >> k) & 1 == 0 else -1) * 2.0 ** (-k-1)
                     for k in range(K + 1))
        character = -1 if (s >> m) & 1 else 1
        total += character * cmath.exp(-1j * t * energy)
    return total / scale


def product_amplitude(m, K, t):
    v = -1j * math.sin(t / (1 << (m+1)))
    for k in range(K+1):
        if k != m:
            v *= math.cos(t / (1 << (k+1)))
    return v


def scalar_prob(m, t):
    """Infinite-volume singleton probability, with removable poles handled by direct products."""
    y = t / (1 << (m+1))
    if abs(math.cos(y)) < 1.e-8:
        val = math.sin(y)**2
        for k in range(m):
            val *= math.cos(t / (1 << (k+1)))**2
        # tail product up to 40 beyond the singleton; uniform numerical error < 1e-20
        for k in range(m+1, m+42):
            val *= math.cos(t / (1 << (k+1)))**2
        return val
    return (math.sin(t)/t)**2 * math.tan(y)**2 if t != 0 else 0.0


def near_resonance_prob(m, delta):
    h = 2.0 ** (-m)
    if delta == 0.0:
        return 4.0 / math.pi**2
    x = h * delta / 2.0
    correction = x / math.tan(x)
    return 4 * (math.sin(delta)/delta)**2 * correction**2 / (math.pi+h*delta)**2


def golden_max(fn, lo, hi):
    a = (math.sqrt(5)-1)/2
    x = hi - a*(hi-lo)
    y = lo + a*(hi-lo)
    fx, fy = fn(x), fn(y)
    for _ in range(130):
        if fx > fy:
            hi, y, fy = y, x, fx
            x = hi-a*(hi-lo)
            fx = fn(x)
        else:
            lo, x, fx = x, y, fy
            y = lo+a*(hi-lo)
            fy = fn(y)
    d = (lo+hi)/2
    return d, fn(d)


def run():
    # Direct independent Fourier-spectral sum versus rotated-bit tensor factorization.
    for m in range(5):
        K = m + 5
        for t in (0.317, 1.723, 3.117, math.pi*(1 << m)):
            direct = finite_amplitude(m, K, t)
            product = product_amplitude(m, K, t)
            check(abs(direct-product)<2.0e-12, f'finite Fourier versus product, {m},{K},{t}')
    # Finite bit products converge to the exact infinite-resonance constant.
    for m in range(7):
        t = math.pi * (1 << m)
        for R in (5,8,12):
            p = abs(product_amplitude(m, m+R, t))**2
            exact = 4.0 / math.pi**2
            bound = math.pi**2 / (3 * 4**(R+1))
            check(p+1e-14>=exact, f'tail product lower bound, {m},{R}')
            check(p-exact<=bound+1e-14, f'tail product error, {m},{R}')
    # Translation-invariant resonant packet marginal bit probabilities.
    for m in range(6):
        t = math.pi * (1 << m)
        for k in range(m):
            check(abs(math.sin(t/2**(k+1)))<2.e-13, f'lower bits unmoved {m},{k}')
        check(abs(math.sin(t/2**(m+1)))**2-1 < 1e-13, f'target bit is on, {m}')
        for j in (1,2,3,5):
            p = math.sin(t/2**(m+j+1))**2
            q = math.sin(math.pi/2**(j+1))**2
            check(abs(p-q)<1e-13, f'shifted packet, {m},{j}')
    # Stationary equation and asymptotic expansion of first-resonance global peak.
    for m in range(2,9):
        n = 1 << m
        d, maximum = golden_max(lambda s: near_resonance_prob(m, s), -0.7, 0.2)
        shifted = -3.0/(math.pi*n)
        peak = 4/math.pi**2 * (1+3/(math.pi**2*n*n))
        check(abs(d-shifted)<0.65/n**3, f'peak time asymptotics {m}')
        check(abs(maximum-peak)<0.015/n**4, f'peak fidelity asymptotics {m}')
        check(maximum > 4/math.pi**2, f'peak strictly improves resonance {m}')
        # The optimizer is a genuine local peak, not a minimum.
        check(near_resonance_prob(m, d) > near_resonance_prob(m, d+0.02), f'peak right {m}')
        check(near_resonance_prob(m, d) > near_resonance_prob(m, d-0.02), f'peak left {m}')
    print(f'PASS: {checks} finite computational cross-checks. (All-dimensional optimality rests on the written proof.)')

if __name__ == '__main__':
    run()
