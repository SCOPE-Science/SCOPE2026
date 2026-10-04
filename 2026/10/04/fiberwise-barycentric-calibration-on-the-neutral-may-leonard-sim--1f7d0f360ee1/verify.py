from fractions import Fraction as F

# Sparse polynomial ring in x,y,z,alpha with beta eliminated by beta=2-alpha.
NVAR = 4

def var(i):
    e = [0] * NVAR
    e[i] = 1
    return {tuple(e): F(1)}

def const(q):
    return {(0,) * NVAR: F(q)}

def add(p, q):
    out = dict(p)
    for m, c in q.items():
        out[m] = out.get(m, F(0)) + c
        if out[m] == 0:
            del out[m]
    return out

def neg(p):
    return {m: -c for m, c in p.items()}

def sub(p, q):
    return add(p, neg(q))

def mul(p, q):
    out = {}
    for m, c in p.items():
        for n, d in q.items():
            k = tuple(m[i] + n[i] for i in range(NVAR))
            out[k] = out.get(k, F(0)) + c * d
    return {m: c for m, c in out.items() if c}

def scale(p, q):
    q = F(q)
    return {m: q * c for m, c in p.items() if q * c}

def eq(p, q):
    return sub(p, q) == {}

x, y, z, alpha = [var(i) for i in range(NVAR)]
one = const(1)
two = const(2)
beta = sub(two, alpha)

gx = sub(sub(sub(one, x), mul(alpha, y)), mul(beta, z))
gy = sub(sub(sub(one, y), mul(beta, x)), mul(alpha, z))
gz = sub(sub(sub(one, z), mul(alpha, x)), mul(beta, y))

xdot = mul(x, gx)
ydot = mul(y, gy)
zdot = mul(z, gz)

N = add(add(x, y), z)
Ndot = add(add(xdot, ydot), zdot)
assert eq(Ndot, sub(N, mul(N, N)))

# On N=1, replace 1-x with y+z algebraically.
gx_on_simplex = sub(add(y, z), add(mul(alpha, y), mul(beta, z)))
rhs_x = mul(sub(alpha, one), sub(z, y))
assert eq(gx_on_simplex, rhs_x)

gy_on_simplex = sub(add(x, z), add(mul(beta, x), mul(alpha, z)))
rhs_y = mul(sub(alpha, one), sub(x, z))
assert eq(gy_on_simplex, rhs_y)

gz_on_simplex = sub(add(x, y), add(mul(alpha, x), mul(beta, y)))
rhs_z = mul(sub(alpha, one), sub(y, x))
assert eq(gz_on_simplex, rhs_z)

pair = add(add(mul(sub(x, y), sub(x, y)),
               mul(sub(y, z), sub(y, z))),
           mul(sub(z, x), sub(z, x)))
rhs_pair = sub(scale(add(add(mul(x, x), mul(y, y)), mul(z, z)), 3), mul(N, N))
assert eq(pair, rhs_pair)

# Mean equations:
# Ey=(1-Ex)/2, Ez=(1-Ey)/2, Ex=(1-Ez)/2.
mx = F(1, 3)
my = F(1, 3)
mz = F(1, 3)
assert my == (1 - mx) / 2
assert mz == (1 - my) / 2
assert mx == (1 - mz) / 2

print("VERIFY_OK")
