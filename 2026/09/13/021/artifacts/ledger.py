"""Tabulated Rayleigh-quotient ledger for lane-1511 TARGET proof.

Route: pushforward of a FIXED interior bump under the anisotropic dilation.
  a(z) = psi((z-q)/r), psi(zz) = (1-|zz|^2)^3_+, q = (-1/2,1), r = 1/16,
  alpha = a dbar z2 on W_pi, u_delta = (D_delta^{-1})^* alpha on Omega_delta.
Closed-form Beta integrals give Q_delta = delta^2*A + delta*B <= C*delta,
C = 24/(5 r^2) = 6144/5 = 1228.8. See output/DRAFT.md for the full proof.
"""
from fractions import Fraction
from math import factorial

r = Fraction(1, 16)
C_exact = Fraction(24, 5) / (r * r)
print(f"r = {r}, C = 24/(5 r^2) = {C_exact} = {float(C_exact)}")
assert C_exact == Fraction(6144, 5)

def beta_int(a, b):
    # B(a,b) for positive integers = (a-1)!(b-1)!/(a+b-1)!
    return Fraction(factorial(a - 1) * factorial(b - 1), factorial(a + b - 1))

# ||psi||^2 = pi^2 * B(2,7) ; each first-derivative norm = (9/2) pi^2 B(3,5)
norm2_over_pi2 = beta_int(2, 7)
deriv_over_pi2 = Fraction(9, 2) * beta_int(3, 5)
print(f"||psi||^2/pi^2 = {norm2_over_pi2} (expect 1/56)")
print(f"||d psi||^2/pi^2 (each) = {deriv_over_pi2} (expect 3/70)")
assert norm2_over_pi2 == Fraction(1, 56)
assert deriv_over_pi2 == Fraction(3, 70)
A = deriv_over_pi2 / norm2_over_pi2 / (r * r)  # A = B = 12/(5 r^2)
print(f"A = B = {A} = {float(A)} (expect 3072/5)")
assert A == Fraction(3072, 5)
assert A + A == C_exact

# Worm interior-ball check: B(q,1/16) subset W_pi, q=(-1/2,1)
import math
Lmax = 2 * max(abs(math.log(15/16)), abs(math.log(17/16)))
thetamax = math.pi * Lmax
bound = 0.5 + 1/16 + thetamax  # |z1+e^{iθ}| <= 1/2+|u|+|θ|
print(f"|L|<={Lmax:.4f}<1 (so eta=0), |z1+e^(iθ)|<={bound:.4f}<1: {bound < 1}")
assert Lmax < 1 and bound < 1

# Sample Rayleigh-quotient ledger: Q_delta <= C*delta, C = 6144/5
C = float(C_exact)
print("\n delta        Q_delta <=")
for e in [0, 1, 2, 3, 4, 6]:
    d = 10.0 ** (-e) if e > 0 else 1.0
    print(f" 1e-{e:<2} {d:10.6f}  {C*d:14.6f}")
print("All ledger checks passed.")
