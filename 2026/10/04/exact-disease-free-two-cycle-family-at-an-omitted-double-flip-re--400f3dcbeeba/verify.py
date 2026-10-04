#!/usr/bin/env python3
from fractions import Fraction as F

A = F(1)
d = F(1, 5)
r = F(3, 10)
lam = F(3, 50)
h = F(10)

# Resonance parameters and disease-free threshold.
assert h == F(2, 1) / d
assert lam == d * r / A
R0 = A * lam / (d * (d + r))
assert R0 == F(3, 5)

x0 = A / d
assert x0 == F(5)

# Disease-free Jacobian.
j11 = 1 - h * d
j12 = -h * A * lam / d
j22 = 1 + h * (A * lam / d - d - r)
assert j11 == -1
assert j12 == -3
assert j22 == -1

# Transversality of the two equations mu_1+1=0 and mu_2+1=0
# in the parameter plane (h, lambda).
dphi1_dh = -d
dphi1_dlam = F(0)
dphi2_dh = A * lam / d - d - r
dphi2_dlam = h * A / d
trans_det = dphi1_dh * dphi2_dlam - dphi1_dlam * dphi2_dh
assert trans_det == -10
assert trans_det != 0

# Exact disease-free involution at h=2/d.
def F_boundary(x):
    return x + h * (A - d * x)

x_plus = F(6)
x_minus = F(4)
assert F_boundary(x_plus) == x_minus
assert F_boundary(x_minus) == x_plus

# Exact transverse factors and two-step Floquet multiplier.
def transverse(x):
    return 1 + h * (lam * x - d - r)

m_plus = transverse(x_plus)
m_minus = transverse(x_minus)
q = m_plus * m_minus
assert m_plus == F(-2, 5)
assert m_minus == F(-8, 5)
assert q == F(16, 25)

u = F(1)
q_formula = 1 - (2 * r * u / A) ** 2
assert q == q_formula

print("VERIFY_OK")
print("R0", R0)
print("E0", (x0, F(0)))
print("J", ((j11, j12), (F(0), j22)))
print("transversality_det", trans_det)
print("two_cycle", (x_plus, x_minus))
print("transverse_factors", (m_plus, m_minus))
print("two_step_transverse_multiplier", q)
