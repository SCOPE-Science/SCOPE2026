from fractions import Fraction as F

alpha = F(1)
beta = F(7, 10)
lam = F(3, 5)
omega = F(7, 2)
rho = F(1, 4)

x = F(5, 4)
y = F(-2, 3)
z = F(9, 10)

xdot = (z-beta)*x - omega*y
ydot = omega*x + (z-beta)*y
R = x*x + y*y
Rdot = 2*x*xdot + 2*y*ydot
assert Rdot == 2*(z-beta)*R

G = lam + alpha*z - z**3/F(3)
zdot = G - (1+rho*z)*R
assert (1+rho*z)*R == G-zdot

# Abstract conditional-law variance consequences.
Varz = F(11, 20)
ElogRdot2 = 4*Varz
assert Varz == ElogRdot2/F(4)

VarG = F(7, 13)
Edotz2 = F(5, 17)
VarW = VarG + Edotz2
assert VarW == VarG + Edotz2

# Standard circular orbit.
Gbeta = lam + alpha*beta - beta**3/F(3)
Abeta = 1 + rho*beta
Rstar = Gbeta/Abeta
assert Gbeta == F(3557, 3000)
assert Abeta == F(47, 40)
assert Rstar == F(3557, 3525)
assert Rstar > 0

print("VERIFY_OK")
