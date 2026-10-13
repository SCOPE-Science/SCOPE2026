#!/usr/bin/env python3
from fractions import Fraction
from math import comb, exp, log, sinh, tanh, sqrt, expm1

def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def add(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])

def sub(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0) for i in range(n)])

def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)

def scale(a, c):
    return trim([c*x for x in a])

def shift(a):
    return [0] + a

def deriv(a):
    return trim([i*a[i] for i in range(1, len(a))] or [0])

def S_poly(m):
    return [1] * m

def S_value(m, r):
    return sum((r**j for j in range(m)), Fraction(0, 1))

exact_cases = 0
for k in range(2, 13):
    for r in (Fraction(3,2), Fraction(5,3), Fraction(2,1)):
        sk = S_value(k, r)
        sm = S_value(k-1, r)
        A = r**(k-1) / sm
        B = Fraction(1,1) / (r*sm)
        L = sk**k / (r*sm**(k+1))
        assert A > B > 0
        assert A / B == r**k
        assert A * (1+B)**k == L
        assert B * (1+A)**k == L
        exact_cases += 1

derivative_orders = 0
for k in range(2, 31):
    sk = S_poly(k)
    sm = S_poly(k-1)
    # r*Sk*Sm*d(log Lambda)/dr
    # = k*r*Sk'*Sm - Sk*Sm - (k+1)*r*Sm'*Sk
    lhs = sub(sub(scale(mul(shift(deriv(sk)), sm), k),
                  mul(sk, sm)),
              scale(mul(shift(deriv(sm)), sk), k+1))
    q = [comb(min(j, 2*k-4-j)+3, 3) for j in range(2*k-3)]
    rhs = mul([-1, 1], q)
    assert trim(lhs) == trim(rhs)
    assert all(c > 0 for c in q)
    derivative_orders += 1

max_err = 0.0
for k in range(2, 13):
    s = 1.0e-4
    def logsinhc(z):
        return log(sinh(z)/z)
    logrel = (
        k * logsinhc(k*s/2.0)
        - (k+1) * logsinhc((k-1)*s/2.0)
        + logsinhc(s/2.0)
    )
    delta = tanh(k*s/2.0)
    observed = delta / sqrt(expm1(logrel))
    target = sqrt(6.0*k/(k+1.0))
    max_err = max(max_err, abs(observed-target))
assert max_err < 2.0e-6

print(f"VERIFY_OK exact_cases={exact_cases} derivative_orders={derivative_orders} onset_max_error={max_err:.3e}")
