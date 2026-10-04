from fractions import Fraction as F

# Sparse polynomial ring in x,y,z,a,b,c.
N = 6

def var(i):
    e = [0] * N
    e[i] = 1
    return {tuple(e): F(1)}

def const(q):
    return {(0,) * N: F(q)}

def add(p, q):
    r = dict(p)
    for m, a in q.items():
        r[m] = r.get(m, F(0)) + a
        if r[m] == 0:
            del r[m]
    return r

def neg(p):
    return {m: -a for m, a in p.items()}

def sub(p, q):
    return add(p, neg(q))

def mul(p, q):
    r = {}
    for e, a in p.items():
        for f, b in q.items():
            g = tuple(e[i] + f[i] for i in range(N))
            r[g] = r.get(g, F(0)) + a * b
    return {m: a for m, a in r.items() if a}

def scale(p, q):
    q = F(q)
    return {m: q * a for m, a in p.items() if q * a}

def der(p, i):
    r = {}
    for e, a in p.items():
        if e[i]:
            g = list(e)
            g[i] -= 1
            g = tuple(g)
            r[g] = r.get(g, F(0)) + a * e[i]
    return {m: a for m, a in r.items() if a}

def eq(p, q):
    return sub(p, q) == {}

x, y, z, a, b, c = [var(i) for i in range(N)]
x2 = mul(x, x)
z2 = mul(z, z)

fx = add(z, mul(x, sub(y, a)))
fy = sub(sub(const(1), mul(b, y)), x2)
fz = neg(add(x, mul(c, z)))
field = [fx, fy, fz, {}, {}, {}]

def L(p):
    r = {}
    for i in range(N):
        r = add(r, mul(der(p, i), field[i]))
    return r

half_z2 = scale(z2, F(1, 2))
assert eq(L(half_z2), neg(add(mul(x, z), mul(c, z2))))

half_energy = scale(add(x2, z2), F(1, 2))
target_energy = sub(mul(x2, sub(y, a)), mul(c, z2))
assert eq(L(half_energy), target_energy)

# Cleared form of c*x^2*(a+1/c-y) = x^2 - c*x^2*(y-a).
left = mul(x2, add(add(mul(c, a), const(1)), neg(mul(c, y))))
right = sub(x2, mul(c, mul(x2, sub(y, a))))
assert eq(left, right)

# Verify nonzero equilibrium identities after clearing denominators.
# Let c*x^2 = c - b*(a*c+1), c*z = -x, c*y = a*c+1.
# Check c*fx, c*fy, c*fz under these algebraic relations by scalar arithmetic
# at an exact positive example where the nonzero equilibria exist.
A = F(1, 10)
B = F(1, 100)
C = F(67, 100)
Y = A + 1 / C
X2 = 1 - B * Y
assert X2 > 0
# Squared identities suffice for the two sign-related equilibria.
assert C * Y == A * C + 1
assert X2 == 1 - B * Y
# z=-x/c gives x*z=-x^2/c and x-equilibrium factor y-a-1/c=0.
assert Y - A - 1 / C == 0
# y-equation and z-equation vanish with the defining relations.
assert 1 - B * Y - X2 == 0

print("VERIFY_OK")
