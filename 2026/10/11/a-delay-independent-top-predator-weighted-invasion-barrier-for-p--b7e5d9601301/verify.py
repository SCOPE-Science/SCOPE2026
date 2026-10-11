from fractions import Fraction as F


def response(u, v, p):
    return u / (v + p*u)


def threshold(v, p, eta, e):
    assert eta > p*e
    return v*e / (eta - p*e)


def check_rearrangement(M, v, p, eta, e):
    lhs = response(M, v, p) - e/eta
    rhs = ((eta - p*e)*M - v*e) / (eta*(v + p*M))
    assert lhs == rhs
    th = threshold(v, p, eta, e)
    assert (lhs > 0) == (M > th)


# Representative exact instances of the algebraic threshold equivalence.
for vals in [
    (F(2), F(3), F(1), F(5), F(1)),
    (F(7, 3), F(11, 5), F(2, 7), F(9, 4), F(1, 3)),
    (F(5, 2), F(13, 4), F(3, 5), F(17, 6), F(2, 5)),
]:
    M, v, p, eta, e = vals
    check_rearrangement(M, v, p, eta, e)

# Printed numerical parameters from DOI 10.3934/math.2023378.
v = F(31, 10)
p = F(57, 50)
eta = F(11, 5)
e = F(1, 5)
th = threshold(v, p, eta, e)
assert th == F(155, 493)
assert eta > p*e
print('VERIFY_OK')
print('threshold =', th, '=', float(th))
