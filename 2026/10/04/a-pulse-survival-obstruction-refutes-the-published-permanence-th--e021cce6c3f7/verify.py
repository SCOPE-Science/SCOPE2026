#!/usr/bin/env python3
import math
from fractions import Fraction as F

a1 = F(20)
a2 = F(20)
b = F(1,10)
d1 = F(1,5)
d2 = F(2,5)
k1 = F(1,5)
k2 = F(3,5)
k3 = F(3,10)
r = F(1,2)
u1 = F(1,10)
u2 = F(1,10)

gamma = F(1,10)
omega = F(1,2)
T = F(1,100)

A = a2/k3 + u2
B = a2-d2
M3_source = r*b/k2
eta = b/(k2*A)

assert A == F(2003,30)
assert B == F(98,5)
assert M3_source == F(1,12)
assert eta == F(5,2003)

# Conditions (3.2), (3.6), (3.11), (3.12), (3.13), (3.14).
assert d2 > r*b/k2
assert a2 > d2
assert a1 > d1 + b*B/(k2*A)

Lgamma = math.log(1.0/(1.0-float(gamma)))
Lomega = math.log(1.0/(1.0-float(omega)))
assert Lgamma > float(eta)*Lomega

Tmax = (Lgamma - float(eta)*Lomega) / float(a1-d1-eta*B)
assert float(T) > Tmax
assert A > B + M3_source

q = (1.0-float(omega))*math.exp(float(B+r*b)*float(T))
assert q < 1.0
assert abs(Tmax - 0.005246815758790803) < 1e-15
assert abs(q - 0.608567660439097) < 1e-15

# The model's actual Holling gain has supremum rb, not rb/k2.
assert r*b == F(1,20)
assert M3_source != r*b

print("VERIFY_OK")
print("A", float(A))
print("B", float(B))
print("M3_source", float(M3_source))
print("Tmax", repr(Tmax))
print("T", float(T))
print("pulse_survival_multiplier", repr(q))
