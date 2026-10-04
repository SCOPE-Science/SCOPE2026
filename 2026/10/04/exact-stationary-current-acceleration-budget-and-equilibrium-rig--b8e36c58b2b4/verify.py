from fractions import Fraction as F

# Sparse polynomial ring in x,y,z,B,C,p.
N = 6

def var(i):
    e = [0] * N
    e[i] = 1
    return {tuple(e): F(1)}

def const(q):
    return {(0,) * N: F(q)}

def add(a, b):
    r = dict(a)
    for m, q in b.items():
        r[m] = r.get(m, F(0)) + q
        if r[m] == 0:
            del r[m]
    return r

def neg(a):
    return {m: -q for m, q in a.items()}

def sub(a, b):
    return add(a, neg(b))

def mul(a, b):
    r = {}
    for m, q in a.items():
        for n, s in b.items():
            k = tuple(m[i] + n[i] for i in range(N))
            r[k] = r.get(k, F(0)) + q * s
    return {m: q for m, q in r.items() if q}

def scale(a, q):
    q = F(q)
    return {m: q * s for m, s in a.items() if q * s}

def der(a, i):
    r = {}
    for m, q in a.items():
        if m[i]:
            n = list(m)
            n[i] -= 1
            n = tuple(n)
            r[n] = r.get(n, F(0)) + q * m[i]
    return {m: q for m, q in r.items() if q}

def eq(a, b):
    return sub(a, b) == {}

x, y, z, B, C, p = [var(i) for i in range(N)]

fx = sub(mul(B, y), mul(C, add(x, p)))
fy = sub(mul(x, z), y)
fz = sub(sub(const(1), z), mul(x, y))
field = [fx, fy, fz, {}, {}, {}]

def L(poly):
    out = {}
    for i in range(N):
        out = add(out, mul(der(poly, i), field[i]))
    return out

half_temp = scale(add(mul(y, y), mul(z, z)), F(1, 2))
target_temp = add(neg(mul(y, y)), sub(z, mul(z, z)))
assert eq(L(half_temp), target_temp)

xp = add(x, p)
half_xp2 = scale(mul(xp, xp), F(1, 2))
assert eq(L(half_xp2), mul(xp, fx))

# Cleared-denominator residual:
# B*(y - (C/B)(x+p)) = B*y - C*(x+p) = xdot.
residual_cleared = sub(mul(B, y), mul(C, xp))
assert eq(residual_cleared, fx)

# Standard asymmetric coefficient arithmetic.
B0 = F(102)
C0 = F(3)
assert C0 * C0 / (B0 * B0) == F(1, 1156)
assert F(1) / (B0 * B0) == F(1, 10404)

print("VERIFY_OK")
