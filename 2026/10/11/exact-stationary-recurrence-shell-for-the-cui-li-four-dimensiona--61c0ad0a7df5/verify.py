from fractions import Fraction

NAMES = ("u", "v", "w", "p", "a", "b", "c", "d", "e", "m", "k")
N = len(NAMES)
ZERO_MON = (0,) * N

def clean(poly):
    return {m: q for m, q in poly.items() if q}

def const(q):
    q = Fraction(q)
    return {} if not q else {ZERO_MON: q}

def var(i):
    m = [0] * N
    m[i] = 1
    return {tuple(m): Fraction(1)}

def add(x, y):
    z = dict(x)
    for m, q in y.items():
        z[m] = z.get(m, Fraction(0)) + q
    return clean(z)

def neg(x):
    return {m: -q for m, q in x.items()}

def sub(x, y):
    return add(x, neg(y))

def mul(x, y):
    z = {}
    for mx, qx in x.items():
        for my, qy in y.items():
            m = tuple(a + b for a, b in zip(mx, my))
            z[m] = z.get(m, Fraction(0)) + qx * qy
    return clean(z)

def scale(q, x):
    return mul(const(q), x)

def power(x, n):
    out = const(1)
    for _ in range(n):
        out = mul(out, x)
    return out

def diff(x, i):
    z = {}
    for m, q in x.items():
        if m[i]:
            mm = list(m)
            factor = mm[i]
            mm[i] -= 1
            mm = tuple(mm)
            z[mm] = z.get(mm, Fraction(0)) + q * factor
    return clean(z)

def lie(obs, field):
    out = {}
    for i in range(4):
        out = add(out, mul(diff(obs, i), field[i]))
    return clean(out)

u, v, w, p, a, b, c, d, e, m, k = [var(i) for i in range(N)]

up = add(mul(a, sub(v, u)), mul(e, mul(v, w)))
vp = add(add(add(mul(c, u), mul(d, v)), neg(mul(u, w))), mul(m, p))
wp = add(neg(mul(b, w)), mul(u, v))
pp = neg(mul(k, add(u, v)))
field = [up, vp, wp, pp]

Q = scale(Fraction(1, 2), sub(power(u, 2), mul(e, power(w, 2))))
expected = add(add(neg(mul(a, power(u, 2))), mul(a, mul(u, v))), mul(mul(b, e), power(w, 2)))
assert lie(Q, field) == expected
assert wp == add(neg(mul(b, w)), mul(u, v))

# Stationary elimination:
# 0 = -a<U2> + a<UV> + be<W2>,  0 = -b<W> + <UV>.
# Substitution gives a<U2> = ab<W> + be<W2>.
# The completed-square shell is exactly the same relation divided by be.

A = Fraction(15)
B = Fraction(43)
E = Fraction(5)
center = A / (2 * E)
radius2 = center * center
activity = A / (B * E)
assert center == Fraction(3, 2)
assert radius2 == Fraction(9, 4)
assert activity == Fraction(3, 43)

print("VERIFY_OK")
print("center", center)
print("radius_squared", radius2)
print("activity_coefficient", activity)
