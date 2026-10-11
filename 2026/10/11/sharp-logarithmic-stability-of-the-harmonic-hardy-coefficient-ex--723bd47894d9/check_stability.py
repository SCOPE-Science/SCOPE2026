"""Finite quadrature consistency checks for the coefficient identities.
The universal bounds and asymptotics are proved analytically in RESULT.md.
"""
import math
import cmath


def evaluate(n, eta, N=240000):
    assert N % (4 * n) == 0
    a = 0j
    bbar = 0j
    target = 0.0
    unshifted = 0.0
    for j in range(N):
        t = 2 * math.pi * (j + .5) / N
        x = n * t
        c = math.cos(x)
        s = math.sin(x)
        w = abs(c)
        v = min(1.0, eta / w)
        G = 1 if c > 0 else -1
        F = G * cmath.exp(1j * (1 if s >= 0 else -1) * v)
        a += F * cmath.exp(-1j * x)
        bbar += F * cmath.exp(1j * x)
        target += 2 * w * (1 - math.cos(v))
        unshifted += abs(F - G)
    a /= N
    bbar /= N
    target /= N
    unshifted /= N
    delta = 4 / math.pi - abs(a) - abs(bbar)
    assert abs(a.imag) < 1e-10, (n, eta, a)
    assert abs(bbar.imag) < 1e-10, (n, eta, bbar)
    assert abs(a.real - bbar.real) < 1e-10
    assert abs(delta - target) < 1e-4, (n, eta, delta, target)
    assert 0 < delta < 1
    assert unshifted <= 5 * math.sqrt(delta * math.log(math.e / delta))
    return delta, unshifted


if __name__ == '__main__':
    for n in (1, 2, 3):
        for eta in (.04, .01, .003):
            delta, upperD = evaluate(n, eta)
            print('n=%d eta=%.4g delta=%.9g D_at_base=%.9g ratio_delta=%.5g' % (
                n, eta, delta, upperD, delta / (eta * eta * math.log(1 / eta))))
    print('All nine quadrature consistency tests passed; no infinite assertion relies on them.')
