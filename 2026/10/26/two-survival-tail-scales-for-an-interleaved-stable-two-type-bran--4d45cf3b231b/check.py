#!/usr/bin/env python3
"""Numerical illustrations for the interleaved stable-branching example.

The infinite-time conclusions follow from the written proof, not this script.
Uses only the Python standard library.
"""
import math

PI = math.pi
A2 = 4 * math.e**2
A3 = ((math.sqrt(A2) + 1) * math.exp(math.sqrt(A2))) ** 2
R2, R3 = math.sqrt(A2), math.sqrt(A3)
L_APPROX = 2 * (1 - 1 / R2) + 2 / R3
# The absolute error in replacing the second A_2 interval by [a_3,infinity)
# is at most 2/sqrt(a_4), where sqrt(a_4)=(sqrt(a_3)+1)exp(sqrt(a_3)).
LOG_TAIL_BOUND = math.log(2) - math.log(R3 + 1) - R3


def j_finite(z, a, b):
    """Integral of (1-exp(-z*x))*x**(-3/2) from a to b."""
    sa, sb = math.sqrt(a), math.sqrt(b)
    return (2 * (-math.expm1(-z * a) / sa + math.expm1(-z * b) / sb)
            + 2 * math.sqrt(PI * z) *
            (math.erf(math.sqrt(z * b)) - math.erf(math.sqrt(z * a))))


def j_tail(z, a):
    return (2 * (-math.expm1(-z * a)) / math.sqrt(a)
            + 2 * math.sqrt(PI * z) * math.erfc(math.sqrt(z * a)))


def phi2(z):
    if z <= 0:
        return 0.0
    return j_finite(z, 1.0, A2) + j_tail(z, A3)


def drift(x, y):
    p2 = phi2(max(0, x)) + phi2(max(0, y))
    full = 2 * math.sqrt(PI) * (math.sqrt(max(0, x)) + math.sqrt(max(0, y)))
    return full - p2, p2


def rk4(x, y, h):
    a, b = drift(x, y)
    c, d = drift(x + a*h/2, y + b*h/2)
    e, f = drift(x + c*h/2, y + d*h/2)
    g, k = drift(x + e*h, y + f*h)
    return x + h*(a + 2*c + 2*e + g)/6, y + h*(b + 2*d + 2*f + k)/6


def check():
    assert 0 < L_APPROX < 2
    assert LOG_TAIL_BOUND < -1000
    for z in [1e-8, 1e-4, 0.01, 1, 10, 1000]:
        p = phi2(z)
        assert -1e-12 <= p <= L_APPROX + 1e-10
        assert p <= 2*math.sqrt(PI*z) + 1e-10
    x = y = 1e-12
    dt = 0.01
    print('L', format(L_APPROX,'.13g'), 'absolute error smaller than exp(',round(LOG_TAIL_BOUND,2),')')
    for step in range(20000):
        x, y = rk4(x, y, dt)
        t = (step + 1)*dt
        if step+1 in [100,1000,10000,20000]:
            total=x+y
            lo=(math.sqrt(2e-12) + math.sqrt(PI)*t)**2
            hi=(math.sqrt(2e-12) + math.sqrt(2*PI)*t)**2
            # Tolerance accounts for a finite-step approximation of the ODE.
            assert lo*(1-1e-3) <= total <= hi*(1+1e-3)
            assert y <= 2*L_APPROX*t + 1e-3
            print('t',round(t), 'total/t^2',round(total/t**2,9),
                  'u1/t^2',round(x/t**2,9),'u2/t',round(y/t,9))
    print('All finite numerical checks passed; no infinite-time conclusion is inferred.')

if __name__ == '__main__':
    check()
