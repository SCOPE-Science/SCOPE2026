#!/usr/bin/env python3
from fractions import Fraction as F
import math

# A concrete exact check of the generic CF integral algebra.
# These values are an algebraic replay only; no normalization convention is inferred.
A = F(2, 3)
B = F(2, 3)
Pi = F(2)
phi = F(1)
y0 = F(1)

yplus = (y0 + A*Pi) / (1 + A*phi)
rate = B*phi / (1 + A*phi)

assert yplus == F(7, 5)
assert rate == F(2, 5)
assert yplus != y0
assert (yplus == y0) == (y0 == Pi/phi)

# Check the integral relation numerically at several times.
def y_cf(t):
    return float(Pi/phi) + float(yplus - Pi/phi) * math.exp(-float(rate)*t)

def integral_forcing(t):
    # Pi - phi*y(s) = (Pi - phi*yplus) exp(-rate*s)
    amp = float(Pi - phi*yplus)
    return amp * (1-math.exp(-float(rate)*t))/float(rate)

for t in (0.1, 0.5, 1.0, 2.0):
    y = y_cf(t)
    lhs = y - float(y0)
    rhs = float(A)*(float(Pi)-float(phi)*y) + float(B)*integral_forcing(t)
    assert abs(lhs-rhs) < 1e-12

# Classical Caputo alpha=1/2 solution for the same scalar vector field.
# E_{1/2}(-phi*sqrt(t)) = exp(phi^2*t)*erfc(phi*sqrt(t)).
def y_caputo_half(t):
    ml = math.exp(float(phi*phi)*t) * math.erfc(float(phi)*math.sqrt(t))
    return float(Pi/phi) + float(y0-Pi/phi)*ml

cf1 = y_cf(1.0)
cap1 = y_caputo_half(1.0)
assert abs(cf1-cap1) > 1e-3
assert abs(y_caputo_half(0.0)-float(y0)) < 1e-15
assert abs(y_cf(0.0)-float(yplus)) < 1e-15

print("VERIFY_OK")
print("yplus", yplus)
print("rate", rate)
print("cf_t1", format(cf1, ".15f"))
print("caputo_half_t1", format(cap1, ".15f"))
print("difference", format(cf1-cap1, ".15f"))
