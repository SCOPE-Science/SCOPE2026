#!/usr/bin/env python3
import sympy as s

d, p, eps = s.symbols("d p eps", positive=True)

# Normalized spherical moments E[U_1^(2k)].
E2 = 1/d
E4 = 3/(d*(d+2))
E6 = 15/(d*(d+2)*(d+4))

# H2 = x^2 - 1/d, H3 = x^3 - 3x/(d+2).
# First harmonic of H3 vanishes.
first_H3 = s.factor(E4 - 3*E2/(d+2))
assert first_H3 == 0

# Exact mixed moment E[x H2 H3].
mixed = s.factor(
    E6
    - (1/d + 3/(d+2))*E4
    + (3/(d*(d+2)))*E2
)
mixed_target = 6*(d-1)/(d*(d+2)**2*(d+4))
assert s.factor(mixed-mixed_target) == 0

# Only the 2 H2 H3 cross term contributes to E[x(H2+H3)^2].
M1 = s.factor(2*eps**2*mixed)
M1_target = 12*eps**2*(d-1)/(d*(d+2)**2*(d+4))
assert s.factor(M1-M1_target) == 0

# Implicit-function coefficient.
ift_coeff = s.factor(d*(p-2)*M1/2)
ift_target = 6*eps**2*(p-2)*(d-1)/((d+2)**2*(d+4))
assert s.factor(ift_coeff-ift_target) == 0

# The d=2 special case should reduce to (p-2) eps^2 / 16.
assert s.factor(ift_target.subs(d,2) - (p-2)*eps**2/16) == 0

# Planar spherical-harmonic reduction and curvature-density check.
theta = s.symbols("theta", real=True)
x = s.cos(theta)
H2_2 = s.trigsimp(x**2 - s.Rational(1,2))
H3_2 = s.trigsimp(x**3 - s.Rational(3,4)*x)
assert s.trigsimp(s.expand_trig(H2_2 - s.cos(2*theta)/2)) == 0
assert s.trigsimp(s.expand_trig(H3_2 - s.cos(3*theta)/4)) == 0

h = 1 + eps*(s.cos(2*theta)/2 + s.cos(3*theta)/4)
rho = s.trigsimp(h + s.diff(h, theta, 2))
rho_target = 1 - s.Rational(3,2)*eps*s.cos(2*theta) - 2*eps*s.cos(3*theta)
assert s.simplify(s.trigsimp(rho-rho_target)) == 0

# Crude planar positivity certificate:
# rho >= 1 - (3/2+2)|eps| = 1 - 7|eps|/2.
# Thus |eps| < 2/7 is sufficient.
bound = s.Rational(2,7)
assert s.simplify(1 - s.Rational(7,2)*bound) == 0

print("VERIFY_OK")
print("mixed_moment =", mixed_target)
print("support_square_first_moment =", M1_target)
print("large_ball_drift_coefficient =", ift_target)
print("planar_drift_coefficient =", (p-2)*eps**2/16)
print("planar_curvature_density =", rho_target)
