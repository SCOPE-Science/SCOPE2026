"""Numerical checks for a specific Hardy-space approximation theorem.

Standard-library only. Finite quadrature supplements, not replaces, the proof.
"""
import math


def moment_equation(p, t, samples=16384):
    total = 0.0
    for k in range(samples):
        x = math.cos(math.pi * (k + 0.5) / samples)
        a = (t + 2.0 * x)/(t + 2.0)
        total += (1.0 - x) * math.copysign(abs(a)**(p-1.0), a)
    return total / samples


def root(p, samples=16384):
    lo, hi = 0.0, 4.0
    assert moment_equation(p, lo, samples) < 0
    assert moment_equation(p, hi, samples) > 0
    for _ in range(64):
        mid = 0.5 * (lo + hi)
        if moment_equation(p, mid, samples) < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def check():
    t2 = root(2.0)
    t4 = root(4.0)
    assert abs(t2 - 1.0) < 3e-6, t2
    assert abs(t4 - 0.677814645373914) < 3e-6, t4
    assert abs(t4**3 - 3*t4**2 + 6*t4 - 3) < 5e-5
    print('p=2:', t2, 'p=4:', t4)

    for p in (3., 5., 6., 10., 20., 50., 100., 200., 400., 800.):
        t = root(p)
        q = p - 1.0
        offset = q*t - math.log(4.0*q)
        assert 0 < t < 4.0
        assert abs(moment_equation(p, t)) < 1e-10
        assert -2.0 < -(1.0+t) < -1.0 or p < 3.0
        print('p={:6.1f} t={:.12f} scaled-minus-log={:+.8f}'.format(p,t,offset))
        if p >= 50:
            assert abs(offset) < 0.5, (p,offset)
    print('PASS: 12 root checks, two published finite levels, and high-exponent comparison')

if __name__ == '__main__':
    check()
