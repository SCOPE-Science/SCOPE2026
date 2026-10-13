"""Exact coefficient and rational-simplex checks for a renewal-mass minorant."""
from fractions import Fraction
from itertools import product

Z = (0, 0, 0, 0)

def atom(coefficient=1, power=Z):
    coefficient = Fraction(coefficient)
    return {} if coefficient == 0 else {power: coefficient}

def var(i):
    exponents = [0, 0, 0, 0]
    exponents[i] = 1
    return atom(1, tuple(exponents))

def add(*args):
    result = {}
    for poly in args:
        for key, value in poly.items():
            result[key] = result.get(key, Fraction(0)) + value
            if result[key] == 0:
                del result[key]
    return result

def neg(poly):
    return {key: -value for key, value in poly.items()}

def sub(left, right):
    return add(left, neg(right))

def mul(*args):
    result = atom()
    for poly in args:
        next_result = {}
        for x, vx in result.items():
            for y, vy in poly.items():
                key = tuple(i + j for i, j in zip(x, y))
                next_result[key] = next_result.get(key, Fraction(0)) + vx * vy
        result = {key: val for key, val in next_result.items() if val}
    return result

def times(c, poly):
    return mul(atom(c), poly)

def square(poly):
    return mul(poly, poly)

def value(poly, coords):
    return sum((coefficient * __import__('math').prod(x**e for x, e in zip(coords, monomial))
                for monomial, coefficient in poly.items()), Fraction(0))

a, b, c, d = [var(i) for i in range(4)]
total = add(a, b, c, d)
q = mul(a, add(a, b), add(a, b, c))
bump = times(2, mul(a, b, d))
p = add(q, bump)
u1 = mul(a, square(total))
u2 = add(mul(square(a), total), mul(b, square(total)))
u3 = add(mul(a, square(a)), times(2, mul(a, b, total)), mul(c, square(total)))

cert1 = mul(a, add(square(add(c, d)), mul(b, c), mul(a, add(c, times(2, d)))))
cert2 = add(mul(square(a), d), mul(b, add(square(add(b, c, d)), mul(a, add(b, c)))))
cert3 = add(mul(a, square(b)), mul(c, add(square(add(b, c, d)), mul(a, add(times(3, b), times(2, c), times(2, d))))))
for index, (u, certificate) in enumerate(zip((u1, u2, u3), (cert1, cert2, cert3)), 1):
    assert sub(u, p) == certificate, f'polynomial identity failed: {index}'
    assert all(coefficient > 0 for coefficient in certificate.values()), f'negative certificate coefficient: {index}'

count = 0
for n in range(1, 25):
    for aa in range(n + 1):
        for bb in range(n - aa + 1):
            for cc in range(n - aa - bb + 1):
                dd = n - aa - bb - cc
                prob = tuple(Fraction(v, n) for v in (aa, bb, cc, dd))
                qv, pv = value(q, prob), value(p, prob)
                uv = [value(U, prob) for U in (u1, u2, u3)]
                assert 0 <= qv <= pv <= min(uv) <= 1
                count += 1

quarter = (Fraction(1, 4),) * 4
assert value(p, quarter) - value(q, quarter) == Fraction(1, 32)
# On c=0, exactly u3-q=a*b*(b+2*d); this certifies coefficient 2 is sharp.
sharp = mul(a, b, add(b, times(2, d)))
assert {tuple((power[0], power[1], power[3])): coefficient
        for power, coefficient in sub(sub(u3, q), sharp).items() if power[2] == 0} == {}
trial = (Fraction(49, 100), Fraction(1, 100), Fraction(0), Fraction(1, 2))
u3_trial = value(u3, trial)
for lam in (Fraction(21, 10), Fraction(3), Fraction(7, 2)):
    assert value(add(q, times(lam, mul(a, b, d))), trial) > u3_trial
print(f'PASS: 3 exact polynomial identities; {count} rational simplex points; positive witness; sharpness cases')
