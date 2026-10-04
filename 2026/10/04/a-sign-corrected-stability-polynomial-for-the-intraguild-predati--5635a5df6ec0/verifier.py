from fractions import Fraction as F

# Exact positive coexistence equilibrium in the dimensionless IGP system.
R = F(1,2)
C1 = F(1)
C2 = F(1)
r = F(8,3)
a1 = a2 = a3 = a4 = F(1)
w1 = F(4)
w2 = w3 = F(1)
m1 = m2 = F(5,6)

# Equilibrium residuals.
g1 = r*R*(1-R) - R*C1/(a1*R+1) - R*C2/(a2*R+1)
g2 = w1*R*C1/(a1*R+1) - a4*C1*C2/(a3*C1+1) - m1*C1
g3 = w2*R*C2/(a2*R+1) + w3*C1*C2/(a3*C1+1) - m2*C2
assert (g1,g2,g3) == (0,0,0)

# Jacobian at the exact equilibrium.
b11 = r*(1-2*R) - C1/(a1*R+1)**2 - C2/(a2*R+1)**2
b12 = -R/(a1*R+1)
b13 = -R/(a2*R+1)
b21 = w1*C1/(a1*R+1)**2
b22 = w1*R/(a1*R+1) - a4*C2/(a3*C1+1)**2 - m1
b23 = -a4*C1/(a3*C1+1)
b31 = w2*C2/(a2*R+1)**2
b32 = w3*C2/(a3*C1+1)**2
b33 = w2*R/(a2*R+1) + w3*C1/(a3*C1+1) - m2
J = [[b11,b12,b13],[b21,b22,b23],[b31,b32,b33]]
assert J == [[F(-8,9),F(-1,3),F(-1,3)],
             [F(16,9),F(1,4),F(-1,2)],
             [F(4,9),F(1,4),F(0)]]

# Source definitions in Supplementary Eqs. (S4)-(S5).
sigma2 = b11+b22+b33
sigma1 = b12*b21+b13*b31+b23*b32 - b22*b33 - b11*(b22+b33)
sigma0 = b12*b23*b31+b13*b21*b32-b11*b23*b32-b12*b21*b33+b11*b22*b33-b13*b22*b31
assert (sigma2,sigma1,sigma0) == (F(-23,36),F(-139,216),F(-4,27))

# True characteristic polynomial det(lambda I-J)=lambda^3+a1c lambda^2+a2c lambda+a3c.
# For any 3x3 matrix these coefficients are -tr(J), sum principal 2x2 minors, -det(J).
a1c = -sigma2
a2c = -sigma1
a3c = -sigma0
assert (a1c,a2c,a3c) == (F(23,36),F(139,216),F(4,27))

# Exact cubic Routh-Hurwitz test: all roots have negative real part.
assert a1c > 0 and a2c > 0 and a3c > 0
assert a1c*a2c > a3c
assert a1c*a2c == F(3197,7776)
assert a3c == F(1152,7776)

# The source's stated supplement test uses sigma0>0 and sigma2>0 (among its conditions),
# so it labels this exact stable positive equilibrium unstable.
source_declares_stable = (sigma0 > 0 and sigma2 > 0 and sigma1*sigma2 > (sigma1*sigma2-sigma0))
assert not source_declares_stable

# Correct source-notation Hurwitz test.
corrected = (sigma2 < 0 and sigma1 < 0 and sigma0 < 0 and sigma1*sigma2 + sigma0 > 0)
assert corrected

print('VERIFY_OK')
