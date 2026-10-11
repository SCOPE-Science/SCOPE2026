from fractions import Fraction as F

h = F(123, 25)
nu1 = F(1)
nu2 = F(4)

x = F(7, 5)
y = F(-3, 2)
z = F(11, 6)

xdot = h*y - nu1*x - y*z
ydot = h*x - nu2*y + x*z
zdot = -z + x*y

assert x*y - z == zdot
assert y*(h-z) - nu1*x == xdot
assert x*(h+z) - nu2*y == ydot

sum_energy_dot = x*xdot + y*ydot
diff_energy_dot = x*xdot - y*ydot

assert sum_energy_dot == 2*h*x*y - nu1*x*x - nu2*y*y
assert diff_energy_dot == -nu1*x*x + nu2*y*y - 2*x*y*z

# Exact stationary linear solve.
m = F(7, 4)
q = F(19, 5)
Ex2 = (h*m - q) / nu1
Ey2 = (h*m + q) / nu2

assert nu1*Ex2 + nu2*Ey2 == 2*h*m
assert -nu1*Ex2 + nu2*Ey2 == 2*q

varz = q - m*m
assert varz + nu1*Ex2 == m*(h-m)

# Abstract conditional-regression variance decomposition:
# U = G + R with E[R]=0 and Cov(G,R)=0.
EG = F(2, 7)
EG2 = F(13, 11)
ER = F(0)
ER2 = F(5, 17)
EGR = F(0)

EU = EG + ER
EU2 = EG2 + 2*EGR + ER2
varU = EU2 - EU*EU
varG = EG2 - EG*EG
assert varU == varG + ER2

# Classical parameter specialization.
assert h == F(123, 25)
m0 = F(3, 2)
v0 = F(7, 10)
Ex20 = m0*(h-m0) - v0
assert v0 + Ex20 == m0*(h-m0)

print("VERIFY_OK")
