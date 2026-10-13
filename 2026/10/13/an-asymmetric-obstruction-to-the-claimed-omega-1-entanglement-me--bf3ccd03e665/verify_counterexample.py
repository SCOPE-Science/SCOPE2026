from fractions import Fraction
from math import sqrt, log2

# Explicit witness: q0=3/10, q2=sqrt(39)/10, q4=1/5.
# Work with exact squares and products needed for determinants.
x = Fraction(9, 100)    # q0^2
y = Fraction(39, 100)   # q2^2
z = Fraction(4, 100)    # q4^2

assert 2*x + 2*y + z == 1

det_A = x * (4*y + z)
det_B = (x + y)**2 + x*z
assert det_A == Fraction(18, 125)
assert det_B == Fraction(117, 500)
assert det_B - det_A == (x-y)**2 == Fraction(9, 100)

# Eq. (39) uses C^2 = 4 det(rho_A).
C2 = 4*det_A
assert C2 == Fraction(72, 125)

def h2_from_det(d):
    d=float(d)
    lam=(1+sqrt(1-4*d))/2
    return -lam*log2(lam)-(1-lam)*log2(1-lam)

SA=h2_from_det(det_A)
SB=h2_from_det(det_B)
assert SB > SA
print('normalization=1')
print('det_rho_A=', det_A)
print('det_rho_B=', det_B)
print('gap=', det_B-det_A)
print('S_A_bits=%.12f' % SA)
print('S_B_bits=%.12f' % SB)
print('VERIFY_OK')
