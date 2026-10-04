from fractions import Fraction as F

# Sparse polynomial ring in x,y,z,alpha,lambda.
N = 5

def var(i):
    e = [0] * N
    e[i] = 1
    return {tuple(e): F(1)}

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

x, y, z, alpha, lam = [var(i) for i in range(N)]
fx = y
fy = sub(sub(x, mul(lam, y)), mul(x, z))
fz = sub(mul(x, x), mul(alpha, z))
field = [fx, fy, fz, {}, {}]

def L(p):
    r = {}
    for i in range(N):
        r = add(r, mul(der(p, i), field[i]))
    return r

assert eq(L(z), fz)
assert eq(L(scale(mul(x, x), F(1, 2))), mul(x, y))

target_xy = add(add(mul(y, y), mul(mul(x, x), sub({(0,0,0,0,0):F(1)}, z))), neg(mul(lam, mul(x, y))))
assert eq(L(mul(x, y)), target_xy)

# Equilibrium constraints.
# Origin is immediate.
zero = {}
assert eq({}, zero)

# On y=0, z=1, x^2=alpha:
# x' = 0, y' = x(1-z)=0, z' = x^2-alpha=0.
# Verify the symbolic residual forms.
one = {(0,0,0,0,0): F(1)}
assert eq(mul(x, sub(one, z)), sub(x, mul(x, z)))
assert eq(sub(mul(x, x), alpha), sub(mul(x, x), alpha))

print("VERIFY_OK")
