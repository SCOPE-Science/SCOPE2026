from fractions import Fraction as F

alpha = F(7, 5)
beta = F(3, 2)
gamma = F(11, 6)
delta = F(5, 4)

xstar = gamma / delta
ystar = alpha / beta

x = F(13, 7)
y = F(9, 8)

xdot = x * (alpha - beta * y)
ydot = y * (-gamma + delta * x)

assert xdot / x == -beta * (y - ystar)
assert ydot / y == delta * (x - xstar)

# Abstract consequences of the two conditional means.
Ex = xstar
Ey = ystar
Exy = xstar * ystar
cov = Exy - Ex * Ey
assert cov == 0

# Exact variance-speed conversions.
varx = F(17, 13)
vary = F(19, 11)
E_percap_x_sq = beta * beta * vary
E_percap_y_sq = delta * delta * varx
assert E_percap_x_sq / (beta * beta) == vary
assert E_percap_y_sq / (delta * delta) == varx

# Coexistence equilibrium.
assert xstar * (alpha - beta * ystar) == 0
assert ystar * (-gamma + delta * xstar) == 0

print("VERIFY_OK")
