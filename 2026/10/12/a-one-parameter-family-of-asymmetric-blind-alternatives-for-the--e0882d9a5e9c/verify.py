from fractions import Fraction as F


def add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0)) for i in range(n)]


def scale(a, c):
    return [c*x for x in a]


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def integ01(a):
    return sum(c / F(i+1) for i, c in enumerate(a))

# Polynomials use ascending powers of u.
rhoF3 = [F(0), F(4), F(-3)]
rhoG3 = [F(1), F(2), F(-3)]
W3 = add(mul(rhoF3, rhoF3), scale(mul(rhoG3, rhoG3), F(-1)))
assert W3 == [F(-1), F(-4), F(18), F(-12), F(0)]

# h(u) = (2u-1)^3 - (15/28)(2u-1)
h = [F(-13,28), F(69,14), F(-12), F(8)]
assert integ01(W3) == 0
assert integ01(mul(W3, h)) == 0

# Global positivity bound: endpoint absolute value dominates both interior critical values.
endpoint_sq = F(13,28)**2
critical_sq = F(125,5488)  # |h|^2 at z^2=5/28
assert endpoint_sq > critical_sq

rhoF4 = [F(0), F(0), F(6), F(-4)]
# rhoG4(u) = rhoF4(1-u) = 2 - 6u^2 + 4u^3
rhoG4 = [F(2), F(0), F(-6), F(4)]
W4 = add(mul(rhoF4, rhoF4), scale(mul(rhoG4, rhoG4), F(-1)))
assert integ01(W4) == 0
assert integ01(mul(W4, h)) == F(2,35)

# Population contrast includes the factor one half.
assert F(1,2) * integ01(mul(W4, h)) == F(1,35)
print('VERIFY_OK')
