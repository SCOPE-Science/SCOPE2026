from fractions import Fraction as F


def coeffs(z):
    z = F(z)
    return (F(12) - 8*z)/(F(12) + 5*z), z/(F(12) + 5*z)


def replay(z, nmax):
    z = F(z)
    a, b = coeffs(z)
    y = [F(1), F(1)/(F(1)+z)]
    while len(y) <= nmax:
        y.append(a*y[-1] + b*y[-2])
    return y


def p_at_y1(z):
    z = F(z)
    a, b = coeffs(z)
    y1 = F(1)/(F(1)+z)
    direct = y1*y1 - a*y1 - b
    closed = -z*z*(z-F(6))/((z+F(1))**2*(F(12)+5*z))
    assert direct == closed
    return direct


def y2_closed(z):
    z = F(z)
    a, b = coeffs(z)
    direct = a/(F(1)+z) + b
    closed = (z-F(4))*(z-F(3))/((z+F(1))*(5*z+F(12)))
    assert direct == closed
    return direct

# Stable-interior sign-loss witness.
y = replay(F(2), 4)
assert y == [F(1), F(1,3), F(1,33), F(3,121), F(-7,3993)]
assert p_at_y1(F(2)) > 0

# Isolated resonance at the negative-real stability boundary.
y6 = replay(F(6), 10)
assert all(y6[n] == F(1, 7**n) for n in range(len(y6)))
assert p_at_y1(F(6)) == 0

a6, b6 = coeffs(F(6))
assert (a6, b6) == (F(-6,7), F(1,7))

# Characteristic-polynomial boundary checks: p(r)=r^2-a*r-b.
def p(z, r):
    a, b = coeffs(z)
    r = F(r)
    return r*r-a*r-b

for q in [F(1,10), F(1), F(3,2), F(2), F(5), F(6), F(7)]:
    assert p(q, F(1)) == F(12)*q/(F(12)+5*q)
    assert p(q, F(-1)) == -F(4)*(q-F(6))/(F(12)+5*q)
    y2_closed(q)

print('VERIFY_OK')
