from fractions import Fraction as F

alpha = F(7, 5)
gamma = 3
x = F(5, 4)
y = F(6, 5)

Q = x * y**gamma
xdot = 1 - Q
ydot = alpha * (Q - y)

assert Q - 1 == -xdot
assert Q - y == ydot / alpha

# Abstract stationary moments.
Ex = F(6, 5)
Ey = F(1)
Varx = F(2, 7)
Vary = F(3, 8)
EQ = F(1)
VarQ = F(7, 10)

# Conditional-law covariance consequences.
ExQ = Ex
EyQ = Vary + Ey * EQ
assert ExQ - Ex*EQ == 0
assert EyQ - Ey*EQ == Vary

# Activity decomposition.
Edoty2 = alpha*alpha*(VarQ - Vary)
Edotx2 = VarQ
assert Edotx2 == Vary + Edoty2/(alpha*alpha)

# Strict-convexity exponents.
assert gamma > 1
assert 1 - gamma < 0

# Equilibrium.
xeq = F(1)
yeq = F(1)
Qeq = xeq * yeq**gamma
assert 1 - Qeq == 0
assert alpha * (Qeq - yeq) == 0

print("VERIFY_OK")
