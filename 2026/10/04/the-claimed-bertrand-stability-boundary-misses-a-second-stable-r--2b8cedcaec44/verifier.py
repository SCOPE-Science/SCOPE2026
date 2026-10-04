from fractions import Fraction as Q


def add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else Q(0)) + (b[i] if i < len(b) else Q(0)) for i in range(n)]


def neg(a):
    return [-x for x in a]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def evalp(a, x):
    s = Q(0)
    p = Q(1)
    for c in a:
        s += c * p
        p *= x
    return s

# Model parameters.
a = Q(1)
b = Q(1, 2)
c1 = c2 = Q(2)
d1 = d2 = Q(1, 3)
beta = Q(1, 2)
p1 = p2 = Q(3)

# Source assumptions and interior equilibrium checks.
assert Q(1) > b > d1 >= 0
assert Q(1) > b > d2 >= 0
assert a > b and c1 > 0 and c2 > 0
m1 = a + b*c1 - 2*b*p1 + d1*p2
m2 = a + b*c2 - 2*b*p2 + d2*p1
q1 = a - b*p1 + d1*p2
q2 = a - b*p2 + d2*p1
assert m1 == 0 and m2 == 0
assert q1 == q2 == Q(1, 2)

# Polynomial entries in ascending powers of t, reconstructed from the published Jacobian.
J11 = [Q(1), Q(-3)]
J12 = [Q(0), Q(1)]
J21 = [Q(0), Q(1), Q(-3, 2)]
J22 = [Q(1), Q(-3), Q(1, 2)]
trace = add(J11, J22)
det = sub(mul(J11, J22), mul(J12, J21))
assert trace == [Q(2), Q(-6), Q(1, 2)]
assert det == [Q(1), Q(-6), Q(17, 2), Q(0)]

one = [Q(1)]
jury_plus = add(add(one, trace), det)
jury_minus = add(sub(one, trace), det)
jury_det = sub(one, det)
assert jury_plus == [Q(4), Q(-12), Q(9), Q(0)]          # (3t-2)^2
assert jury_minus == [Q(0), Q(0), Q(8), Q(0)]          # 8t^2
assert jury_det == [Q(0), Q(6), Q(-17, 2), Q(0)]       # t(12-17t)/2

# Neutral flip point.
t0 = Q(2, 3)
tr0 = evalp(trace, t0)
det0 = evalp(det, t0)
assert evalp(jury_plus, t0) == 0
assert Q(1) + tr0 + det0 == 0                    # characteristic polynomial at lambda=-1

# Exact stable witness in the omitted second interval.
t = Q(7, 10)
assert Q(2, 3) < t < Q(12, 17)
tr = evalp(trace, t)
detv = evalp(det, t)
assert tr == Q(-391, 200)
assert detv == Q(193, 200)
assert evalp(jury_plus, t) == Q(1, 100) > 0
assert evalp(jury_minus, t) == Q(98, 25) > 0
assert evalp(jury_det, t) == Q(7, 200) > 0
assert tr*tr - 4*detv == Q(-1519, 40000) < 0
assert detv < 1

# Direct matrix at witness.
assert evalp(J11, t) == Q(-11, 10)
assert evalp(J12, t) == Q(7, 10)
assert evalp(J21, t) == Q(-7, 200)
assert evalp(J22, t) == Q(-171, 200)

print('VERIFY_OK')
