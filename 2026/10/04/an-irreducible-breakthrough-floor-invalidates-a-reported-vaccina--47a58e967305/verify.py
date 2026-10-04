#!/usr/bin/env python3
from decimal import Decimal, getcontext
getcontext().prec = 50

L = Decimal('250')
mu = Decimal('0.000042')
gamma = Decimal('0.11')
omega = Decimal('0.58')
a1 = Decimal('0.27')
a2 = Decimal('0.19')
b1 = Decimal('0.00815')
b2 = Decimal('0.00000049')

q = gamma * (Decimal(1) - omega) / ((gamma + mu) * (a1 + a2 + mu))
RS = L * q * b1 / mu
RV = L * q * b2 / mu
assert abs(q - Decimal('0.91261166930414770852453290207605256994701057668513')) < Decimal('1e-45')
assert abs(RS - Decimal('44272.530385885744')) < Decimal('1e-9')
assert abs(RV - Decimal('2.6617840354704308')) < Decimal('1e-15')
assert RV > 1 and RS > 1

def R_original(v, bb1=b1, bb2=b2):
    return (bb1 * L / (mu + v) + bb2 * v * L / (mu * (mu + v))) * q

def R_interp(v, rS=RS, rV=RV):
    return (mu * rS + v * rV) / (mu + v)

for s in ['0','0.00001','0.023','0.4','0.65','1','10']:
    v = Decimal(s)
    assert abs(R_original(v) - R_interp(v)) < Decimal('1e-40')
    assert R_original(v) > 1

R04 = R_original(Decimal('0.4'))
assert abs(R04 - Decimal('7.3096322146059')) < Decimal('1e-12')

intercept = mu / (L * q)
slope = Decimal(1) / (L * q) - b2 / mu
cutoff = -intercept / slope
assert abs(intercept - Decimal('1.8408706096e-7')) < Decimal('1e-25')
assert abs(slope - Decimal('-0.0072836414057142857142857142857')) < Decimal('1e-30')
assert abs(cutoff - Decimal('0.0000252740422964228992881634340693')) < Decimal('1e-32')
assert intercept + slope * Decimal('0.023') < 0

# Figure 1 values printed in the paragraph before Figure 1.
v = Decimal('0.4')
b1f = Decimal('0.000815')
b2f = Decimal('0.00000059')
Rfig = R_original(v, b1f, b2f)
assert abs(Rfig - Decimal('3.669481540689118')) < Decimal('1e-15')

S0 = L / (mu + v)
Vs0 = v * L / (mu * (mu + v))
force = b1f * S0 + b2f * Vs0
A = gamma + mu
B = a1 + a2 + mu
c = gamma * (Decimal(1) - omega)
trace = -(A + B)
det = A * B - force * c
assert det < 0
D = trace * trace - Decimal(4) * det
lambda_plus = (trace + D.sqrt()) / Decimal(2)
assert abs(lambda_plus - Decimal('0.18013390201978316636')) < Decimal('1e-20')

# Determinant identity through R0.
assert abs(det - A * B * (Decimal(1) - Rfig)) < Decimal('1e-40')

print('VERIFY_OK')
print('q', q)
print('R_S', RS)
print('R_V', RV)
print('R0_Table2_v0.4', R04)
print('boundary_intercept', intercept)
print('boundary_slope', slope)
print('boundary_nonnegative_cutoff_v', cutoff)
print('Figure1_R0', Rfig)
print('Figure1_positive_eigenvalue', lambda_plus)
