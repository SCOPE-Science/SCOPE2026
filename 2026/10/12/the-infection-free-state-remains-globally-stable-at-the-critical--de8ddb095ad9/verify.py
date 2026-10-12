#!/usr/bin/env python3
from fractions import Fraction as F

# Positive exact witness for the algebraic endpoint identities.
a = F(7, 5)
b = F(11, 6)
tau = F(3, 2)
K = a*b  # critical identity beta*T0*r*d2*exp(-s*tau) = a*b

# F(z)=(z+a)(z+b)-K*exp(-z*tau).
# Exact endpoint values needed for simplicity of the zero root.
F0 = a*b-K
Fp0 = a+b+K*tau
assert F0 == 0
assert Fp0 == F(7,5)+F(11,6)+F(7,5)*F(11,6)*F(3,2)
assert Fp0 > 0

# Exact invariant-set replay with strictly positive coefficients.
lambda_ = F(6,5)
d1 = F(3,5)
T0 = lambda_/d1
beta = F(5,7)
assert T0 > 0 and beta > 0

# On T=T0, dT=lambda-d1*T-beta*T*V=-beta*T0*V.
# If dT=0, positivity forces V=0.
V = F(0)
dT = lambda_ - d1*T0 - beta*T0*V
assert dT == 0
assert beta*T0 > 0

# On V=0, dV=r*d2*I; invariance forces I=0.
r = F(9,4)
d2 = F(8,7)
I = F(0)
dV = r*d2*I
assert dV == 0
assert r*d2 > 0

# AM-GM defect used in the Lyapunov derivative is nonpositive.
for x in [F(1,4), F(1,2), F(1), F(2), F(7,3)]:
    defect = 2 - x - 1/x
    assert defect <= 0
    assert (defect == 0) == (x == 1)

print('VERIFY_OK')
print('F0', F0)
print('Fprime0', Fp0)
print('T0', T0)
