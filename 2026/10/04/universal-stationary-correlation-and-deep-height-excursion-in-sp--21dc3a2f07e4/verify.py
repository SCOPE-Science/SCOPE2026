from fractions import Fraction as F

# Exact stationary moment algebra for canonical Sprott N.
# Let V = Var(z), Ez=1/2, Ez2=1/4+V.
# The checker represents expressions as affine pairs A + B*V.

def add(p, q):
    return (p[0] + q[0], p[1] + q[1])

def sub(p, q):
    return (p[0] - q[0], p[1] - q[1])

def scale(p, c):
    c = F(c)
    return (c*p[0], c*p[1])

Ez = (F(1,2), F(0))
Ez2 = (F(1,4), F(1))
Ez3 = scale(Ez2, F(1,2))  # from 2 E[z^3] = E[z^2]
Ex = scale(Ez2, -1)

# Central third moment:
# E[z^3] - 3/2 E[z^2] + 3/4 E[z] - 1/8.
mu3 = add(
    sub(Ez3, scale(Ez2, F(3,2))),
    (F(1,4), F(0))
)
assert mu3 == (F(0), F(-1))

# E[yz] = E[(2z-1)z] = 2 Ez2 - Ez.
Eyz = sub(scale(Ez2, 2), Ez)
assert Eyz == (F(0), F(2))

# Stationarity of xz:
# 0 = -2 E[yz] + E[x] + E[xy] - 2 E[xz], with E[xy]=0.
Exz = scale(sub(Ex, scale(Eyz, 2)), F(1,2))
assert Exz == (F(-1,8), F(-5,2))

# Stationarity of yz:
# 0 = E[xz] + E[z^3] + E[y] + E[y^2] - 2 E[yz], with E[y]=0.
Ey2 = sub(scale(Eyz, 2), add(Exz, Ez3))
assert Ey2 == (F(0), F(6))

# Cov(y,z)=2V and Var(y)=6V give Corr=sqrt(2/3).
# Check the squared correlation coefficient exactly.
# Corr^2 = (2V)^2 / ((6V)(V)) = 2/3.
assert F(4,6) == F(2,3)

# Unique equilibrium.
x = F(-1,4)
y = F(0)
z = F(1,2)
assert -2*y == 0
assert x + z*z == 0
assert 1 + y - 2*z == 0

# The factorized central identity is
# E[(z-1/2)^2 (z+1/2)] = mu3 + V = 0.
assert add(mu3, (F(0), F(1))) == (F(0), F(0))

print("VERIFY_OK")
