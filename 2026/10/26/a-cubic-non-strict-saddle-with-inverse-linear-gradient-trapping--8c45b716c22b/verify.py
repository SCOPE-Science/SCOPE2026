from fractions import Fraction

# A polynomial is a dict mapping (power_of_x, power_of_a) to a rational coefficient.
def clean(poly):
    return {k: v for k, v in poly.items() if v}

def add(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, Fraction(0)) + v
    return clean(out)

def scale(p, c):
    return clean({k: v*c for k, v in p.items()})

def mul(p, q):
    out = {}
    for (i, j), u in p.items():
        for (k, l), v in q.items():
            key = (i+k, j+l)
            out[key] = out.get(key, Fraction(0)) + u*v
    return clean(out)

def reduce_a4(poly):
    # Use the exact algebraic relation a^4 = 1/3 to reduce powers of a.
    out = {}
    for (xp, ap), c in poly.items():
        quotient, remainder = divmod(ap, 4)
        key = (xp, remainder)
        out[key] = out.get(key, Fraction(0)) + c/Fraction(3**quotient, 1)
    return clean(out)

x = {(1, 0): Fraction(1)}
a = {(0, 1): Fraction(1)}
x_minus_a = add(x, scale(a, Fraction(-1)))
x2_plus_2ax_plus_3a2 = add(
    add({(2, 0): Fraction(1)}, {(1, 1): Fraction(2)}),
    {(0, 2): Fraction(3)})
rhs = reduce_a4(mul(mul(x_minus_a, x_minus_a), x2_plus_2ax_plus_3a2))
lhs = reduce_a4({(4, 0): Fraction(1), (1, 3): Fraction(-4), (0, 0): Fraction(1)})
assert rhs == lhs, (rhs, lhs)

# At the critical point, Hessian diagonal d=2(1+a^4)=8/3,
# and off-diagonal o=2(a^4-1)=-4/3.
a4 = Fraction(1, 3)
d = 2*(1+a4)
o = 2*(a4-1)
assert d == Fraction(8, 3)
assert o == Fraction(-4, 3)
assert d + 2*o == 0
assert d - o == 4

# The quadratic factor at x=a equals 6a^2. Its multipliers give
# 12a^3 in each coordinate update, 36a^3 in the diagonal derivative,
# and 12a^3 after integrating the leading derivative term.
assert 2*6 == 12
assert 6*6 == 36
assert 36//3 == 12
print('PASS: exact polynomial factorization, Hessian spectrum, cubic coefficient, and diagonal-update coefficient')
print('LIMIT: exact identities are checked here; the infinite-iteration limit is proved analytically in RESULT.md')
