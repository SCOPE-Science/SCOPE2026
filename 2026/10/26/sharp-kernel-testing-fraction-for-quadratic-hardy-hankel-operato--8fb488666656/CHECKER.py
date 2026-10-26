"""Deterministic finite checks for quadratic Hardy Hankel kernel testing.

Run: python3 CHECKER.py.  Numerical checks support, but do not prove, the
universal inequality; the analytic envelope argument is the proof.
"""
import cmath
import math
import random
from fractions import Fraction


def radius_max(t):
    if t == 0.0:
        return 0.0
    lo, hi = 0.0, 1.0
    for _ in range(90):
        r = (lo + hi) / 2
        poly = t - (t*t)*r - 3*t*(r*r) - 2*r*r*r
        if poly > 0:
            lo = r
        else:
            hi = r
    return (lo + hi) / 2


def norm_operator(a, b):
    return (abs(a) + math.hypot(abs(a), 2*abs(b))) / 2


def norm_on_kernel(a, b, w):
    r2 = abs(w)**2
    return math.sqrt((1-r2) * (abs(a+b*w)**2 + abs(b)**2))


def g_ratio(t):
    x = (t + math.hypot(t, 2))/2
    r = radius_max(t)
    return math.sqrt((1-r*r)*((t+r)**2+1))/x


def test():
    optimum = 5/(3*math.sqrt(3))
    assert Fraction(5, 6)*Fraction(5, 3) / Fraction(3, 2) == Fraction(25, 27)
    assert abs(g_ratio(1/math.sqrt(6)) - optimum) < 2e-14
    assert abs(radius_max(1/math.sqrt(6)) - 1/math.sqrt(6)) < 2e-14
    checks = 3
    for k in range(5000):
        t = math.exp(-14 + k*28/4999)
        z = g_ratio(t)
        assert z > optimum-2e-12, (t, z)
        assert z < 1+2e-12, (t,z)
        checks += 2
    rng = random.Random(416290)
    for _ in range(10000):
        a = (rng.random()*2-1) + 1j*(rng.random()*2-1)
        b = (rng.random()*2-1) + 1j*(rng.random()*2-1)
        w = math.sqrt(rng.random())*cmath.exp(2j*math.pi*rng.random())
        n = norm_operator(a,b)
        g = norm_on_kernel(a,b,w)
        assert g <= n+1e-11, (n,g,a,b,w)
        checks += 1
    # Optimizing phase for the exact extremal ratio.
    for k in range(300):
        ang1 = 2*math.pi*k/300
        ang2 = 2*math.pi*((37*k)%300)/300
        a = cmath.exp(1j*ang1)/math.sqrt(6)
        b = cmath.exp(1j*ang2)
        w = a*b.conjugate()/(abs(a)*abs(b)*math.sqrt(6))
        assert abs(norm_on_kernel(a,b,w)/norm_operator(a,b)-optimum)<2e-14
        checks += 1
    print(f'PASS {checks} deterministic checks; sharp ratio={optimum:.16f}')

if __name__ == '__main__':
    test()
