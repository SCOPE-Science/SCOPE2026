from fractions import Fraction as F

# Pointwise residual identities at an exact rational state.
mu = F(3, 5)
a = F(16, 25)
x = F(11, 7)
y = F(13, 9)
z = F(17, 8)

xdot = -mu*x + y*z
ydot = -mu*y + x*(z-a)
zdot = 1 - x*y

assert y*z - mu*x == xdot
assert x*(z-a) - mu*y == ydot
assert x*y - 1 == -zdot

# Abstract conditional-regression Pythagoras.
EP = F(2, 7)
EP2 = F(13, 11)
ER = F(0)
ER2 = F(5, 19)
EPR = F(0)

varP = EP2 - EP*EP
Etotal = EP + ER
Etotal2 = EP2 + 2*EPR + ER2
varTotal = Etotal2 - Etotal*Etotal
assert varTotal == varP + ER2

cov_P_total = (EP2 + EPR) - EP*Etotal
assert cov_P_total == varP

# Choose rational parameters with the positive equilibrium height z_+=1:
# mu=3/5 and a=16/25 give z_+(z_+-a)=mu^2.
z_plus = F(1)
assert z_plus*(z_plus-a) == mu*mu

# Equilibrium algebra without irrational coordinates.
u = z_plus/mu              # x^2
v = mu/z_plus              # y^2
assert u*v == 1            # (xy)^2=1
assert mu*u == z_plus
assert v*z_plus == mu

print("VERIFY_OK")
