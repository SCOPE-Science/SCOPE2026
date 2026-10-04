#!/usr/bin/env python3
from fractions import Fraction
import cmath
import math

# Exact modal-determinant bookkeeping for one admissible rational test tuple.
a11 = Fraction(1, 5)
a12 = Fraction(-3, 10)
a21 = Fraction(2, 5)
a22 = Fraction(-1, 4)
d1 = Fraction(1, 100)
d2 = Fraction(2, 1)
chi = Fraction(2, 1)
vstar = Fraction(7, 10)
mu = Fraction(1, 4)

P = (d1 + d2) * mu - (a11 + a22)
Q = (d1 * mu - a11) * (d2 * mu - a22) - a12 * a21
S = -a12 * chi * vstar * mu
R_printed = a12 * chi * vstar * mu
assert S > 0
assert R_printed == -S

# At zero delay the direct determinant must equal Q+S, matching the corrected sign.
det_direct = (d1 * mu - a11) * (d2 * mu - a22) - a12 * (a21 + chi * vstar * mu)
assert det_direct == Q + S
assert det_direct != Q + R_printed

# Phase replay: choose positive P, S, omega and construct Q so a Hopf phase exists.
P0 = 0.5
S0 = 1.0
omega = 0.8
sin_theta = P0 * omega / S0
assert 0.0 < sin_theta < 1.0
theta = math.asin(sin_theta)
cos_theta = math.cos(theta)
Q0 = omega * omega - S0 * cos_theta
tau_true = theta / omega
R0_printed = -S0
arg_printed = (omega * omega - Q0) / R0_printed
tau_printed = (2.0 * math.pi - math.acos(arg_printed)) / omega
assert abs((tau_printed - tau_true) - math.pi / omega) < 1e-12

lam = 1j * omega
res_true = lam * lam + P0 * lam + Q0 + S0 * cmath.exp(-lam * tau_true)
res_at_printed = lam * lam + P0 * lam + Q0 + S0 * cmath.exp(-lam * tau_printed)
assert abs(res_true) < 1e-12
assert abs(res_at_printed) > 1.0

print('VERIFY_OK')
