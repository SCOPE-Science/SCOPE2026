from fractions import Fraction as F

# Sparse polynomial ring in x,y,a,b.
N = 4

def var(i):
    e = [0] * N
    e[i] = 1
    return {tuple(e): F(1)}

def const(q):
    return {(0,) * N: F(q)}

def add(p, q):
    r = dict(p)
    for m, c in q.items():
        r[m] = r.get(m, F(0)) + c
        if r[m] == 0:
            del r[m]
    return r

def neg(p):
    return {m: -c for m, c in p.items()}

def sub(p, q):
    return add(p, neg(q))

def mul(p, q):
    r = {}
    for e, c in p.items():
        for f, d in q.items():
            g = tuple(e[i] + f[i] for i in range(N))
            r[g] = r.get(g, F(0)) + c * d
    return {m: c for m, c in r.items() if c}

def eq(p, q):
    return sub(p, q) == {}

x, y, a, b = [var(i) for i in range(N)]
x2 = mul(x, x)

fx = add(neg(x), add(mul(a, y), mul(x2, y)))
fy = sub(b, add(mul(a, y), mul(x2, y)))

# Mass balance.
assert eq(add(fx, fy), sub(b, x))

# Cleared residual:
# y * (x^2 - (b/y-a)) = y*x^2 - b + a*y = -ydot.
left = sub(add(mul(y, x2), mul(a, y)), b)
assert eq(left, neg(fy))

# Equilibrium, checked exactly at several rational positive parameter pairs.
tests = [(F(1,10),F(3,5)), (F(2,3),F(5,7)), (F(7,5),F(4,3))]
for A, B in tests:
    Y = B / (A + B*B)
    assert -B + A*Y + B*B*Y == 0
    assert B - A*Y - B*B*Y == 0

# Harmonic-defect moment algebra, exact rational witnesses.
for A, B, V in [(F(1,10),F(3,5),F(2,7)), (F(2,3),F(5,7),F(4,9))]:
    E1Y = (A + B*B + V) / B
    EX2 = B*E1Y - A
    assert EX2 - B*B == V
    assert B*(E1Y - (A+B*B)/B) == V

print("VERIFY_OK")
