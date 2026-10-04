#!/usr/bin/env python3
from decimal import Decimal, getcontext
from math import log

def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out

p_plus  = [1, -2, 2, -4, 4]
p_minus = [1,  2, 2,  4, 4]
assert pmul(p_plus, p_minus) == [1, 0, 0, 0, -4, 0, 0, 0, 16]
assert [(a+b)//2 for a,b in zip(p_plus, p_minus)] == [1, 0, 2, 0, 4]

getcontext().prec = 60
root2 = Decimal(2).sqrt()
gcrit = Decimal(1) / root2

def mod2(sign, g):
    real = Decimal(1) - Decimal(sign)*g
    imag = Decimal(2*sign)*g*g - g
    return real*real + imag*imag

mp = mod2(1, gcrit).sqrt()
mm = mod2(-1, gcrit).sqrt()
tol = Decimal("1e-50")
assert abs(mp - (root2 - 1)) < tol
assert abs(mm - (root2 + 1)) < tol

def product(g):
    return mod2(1, g) * mod2(-1, g)

for g, expected_sign in [(Decimal("0.5"), -1), (Decimal("0.8"), 1)]:
    lam = 0.25 * log(float(product(g)))
    assert (lam < 0) if expected_sign < 0 else (lam > 0)

print("VERIFY_OK")
