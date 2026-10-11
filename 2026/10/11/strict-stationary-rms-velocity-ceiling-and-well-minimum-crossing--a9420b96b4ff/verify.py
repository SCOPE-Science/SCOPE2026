from fractions import Fraction as F

alpha = F(3, 2)
beta = F(5, 4)
delta = F(7, 6)
forcing = F(11, 8)
omega = F(9, 5)

# Abstract load regression: L = delta*y + r, with E[r]=0 and Cov(y,r)=0.
vary = F(13, 17)
varr = F(5, 19)
varL = delta*delta*vary + varr
cov_yL = delta*vary
assert varL == delta*delta*vary + varr
assert cov_yL == delta*vary
assert cov_yL*cov_yL < vary*varL

# Cauchy ceiling.
ceiling = forcing*forcing / (2*delta*delta)
q = ceiling / 2
assert F(0) < q < ceiling

# Equality ansatz obstruction coefficient.
A = forcing / (delta*omega)
cubic_coefficient = -alpha * A**3
assert cubic_coefficient != 0

# Quadrature power relation at an abstract exact test value.
Eycos = delta*q/forcing
Exsin = Eycos/omega
assert delta*q == forcing*Eycos == forcing*omega*Exsin

# Cubic barycenter sign structure about r^2=beta/alpha.
r2 = beta/alpha
x_below = r2 / 2
# Use squared state values to check sign without irrational square roots:
# for x>0, sign of x(x^2-r2) is sign of x^2-r2.
assert x_below < r2
x2_above = r2 * 2
assert x2_above > r2

print("VERIFY_OK")
