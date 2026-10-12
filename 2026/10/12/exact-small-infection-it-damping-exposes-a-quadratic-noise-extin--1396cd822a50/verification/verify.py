#!/usr/bin/env python3
import math

# Example 5.2 values from the source.
K = 0.8
mu = 0.15
alpha = 0.2
m = 1.2
s21 = s31 = 0.2
s22 = s32 = 1.0

rho1 = alpha*K/(mu*(1.0+m*K)*(alpha+mu))
rho2 = K/(mu*(1.0+m*K))

delta = (s21*s21*s31*s31)/(2.0*(s21*s21+s31*s31))
assert abs(delta - 0.01) < 1e-15

a = s31*s31/(s21*s21+s31*s31)
b = s21*s21/(s21*s21+s31*s31)
assert abs(a+b-1.0) < 1e-15
assert abs(a-0.5) < 1e-15
assert abs(b-0.5) < 1e-15

def Q(E,I):
    P = rho1*E + rho2*I
    return 0.5*((rho1*E*(s21+s22*E)/P)**2 +
                (rho2*I*(s31+s32*I)/P)**2)

previous = None
for eps in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-8]:
    E = a*eps/rho1
    I = b*eps/rho2
    value = Q(E,I)
    assert value >= delta
    if previous is not None:
        assert value < previous
    previous = value

assert abs(previous-delta) < 1e-8
assert previous < 0.011
assert previous < 0.25

published = -0.0651
repaired_same_envelope = published + 0.25 - delta
assert abs(repaired_same_envelope - 0.1749) < 1e-12
assert repaired_same_envelope > 0.0

print("VERIFY_OK")
