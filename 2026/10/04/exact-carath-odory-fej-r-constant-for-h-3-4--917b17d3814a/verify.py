from fractions import Fraction as F

# Exact arithmetic in Q[r]/(8*r^3 + 4*r^2 - 4*r - 1).
ZERO = (F(0), F(0), F(0))
ONE  = (F(1), F(0), F(0))
R    = (F(0), F(1), F(0))

def add(a, b):
    return tuple(a[i] + b[i] for i in range(3))

def neg(a):
    return tuple(-x for x in a)

def sub(a, b):
    return add(a, neg(b))

def scale(a, q):
    return tuple(q * x for x in a)

def mul(a, b):
    c = [F(0)] * 5
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x * y
    # r^3 = 1/8 + r/2 - r^2/2.  Reduce high degrees downward.
    for k in (4, 3):
        q = c[k]
        c[k] = F(0)
        c[k-3] += q * F(1, 8)
        c[k-2] += q * F(1, 2)
        c[k-1] -= q * F(1, 2)
    return tuple(c[:3])

def power(a, n):
    z = ONE
    for _ in range(n):
        z = mul(z, a)
    return z

def div_int(a, n):
    return scale(a, F(1, n))

def p_mul(a, b):
    c = [ZERO] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i+j] = add(c[i+j], mul(u, v))
    return c

def p_scale(a, q):
    return [mul(u, q) for u in a]

def det3(m):
    a = mul(m[0][0], sub(mul(m[1][1], m[2][2]), mul(m[1][2], m[2][1])))
    b = mul(m[0][1], sub(mul(m[1][0], m[2][2]), mul(m[1][2], m[2][0])))
    c = mul(m[0][2], sub(mul(m[1][0], m[2][1]), mul(m[1][1], m[2][0])))
    return add(sub(a, b), c)

r = R
lam = scale(r, F(2))
b = div_int(add(scale(ONE, F(3)), scale(r, F(-10))), 7)
c = div_int(scale(sub(r, ONE), F(4)), 7)
r2 = power(r, 2)
r3 = power(r, 3)
r4 = power(r, 4)
q = div_int(add(add(scale(ONE, F(5)), scale(r, F(2))), scale(r2, F(-4))), 4)
A = div_int(scale(sub(ONE, r), F(32)), 7)

# Chebyshev-form polynomial in x: 1 + lam*x + b*T3(x) + c*T4(x).
T = [
    add(ONE, c),
    add(lam, scale(b, F(-3))),
    scale(c, F(-8)),
    scale(b, F(4)),
    scale(c, F(8)),
]

# A*(x+1)*(x+r)^2*(q-x).
fac = p_scale(
    p_mul(
        p_mul([ONE, ONE], [r2, scale(r, F(2)), ONE]),
        [q, scale(ONE, F(-1))],
    ),
    A,
)
assert T == fac

# s = cos(pi/7) expressed in Q(r).
s = add(add(scale(r2, F(2)), r), scale(ONE, F(-1, 2)))
assert sub(add(ONE, s), mul(scale(r, F(2)), add(r, s))) == ZERO

# Contact identities: T3(-r)=s and T4(-r)=-s.
T3_minus_r = add(scale(r3, F(-4)), scale(r, F(3)))
T4_minus_r = add(add(scale(r4, F(8)), scale(r2, F(-8))), ONE)
assert sub(T3_minus_r, s) == ZERO
assert add(T4_minus_r, s) == ZERO

# Equality equations in unknowns (lambda,b,c): values at x=-1, x=-r,
# and derivative at x=-r.  Nonzero determinant proves uniqueness.
d3 = add(scale(r2, F(12)), scale(ONE, F(-3)))
d4 = add(scale(r3, F(-32)), scale(r, F(16)))
mat = [
    [scale(ONE, F(-1)), scale(ONE, F(-1)), ONE],
    [neg(r), s, neg(s)],
    [ONE, d3, d4],
]
det = det3(mat)
expected_det = scale(add(add(scale(r2, F(2)), neg(r)), neg(ONE)), F(7))
assert det == expected_det
assert det != ZERO

print("VERIFY_OK")
