"""Exact-arithmetic checks for two/three-step last-snapshot SVRG quadratics.

Only Python's standard library is required. The infinite-parameter theorem
is proved analytically in RESULT.md; this program checks identities and
explicit rational witnesses, not a finite substitute for that proof.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def f2(t, z):
    return (1-t)**4 + z*t**4


def f3(t, z):
    return (1-t)**6 + z*t**4*((1-t)**2+(2-t)**2) + z*z*t**6


def enumerated_second_moment(t, q, steps):
    """Independently enumerate sampled component-curvature signs."""
    total = F(0)
    for signs in product([-1, 1], repeat=steps):
        x = F(1)
        for sign in signs:
            xi = sign*q
            x = (1-t*(1+xi))*x+t*xi
        total += x*x
    return total / 2**steps


def bernstein_f3(t, z):
    b = [F(1), F(0), F(0), F(0), z/3, 2*z/3, z*(1+z)]
    return sum(F(comb(6,k))*b[k]*t**k*(1-t)**(6-k) for k in range(7))


for q in [F(1, 16), F(1, 4), F(1, 2), F(3, 4), F(15, 16)]:
    z = q*q
    for t in [F(k, 11) for k in range(1, 33)]:
        assert enumerated_second_moment(t, q, 2) == f2(t,z)
        assert enumerated_second_moment(t, q, 3) == f3(t,z)
        assert bernstein_f3(t,z) == f3(t,z)


t, z = F(9,5), F(1,16)
assert f2(t,z)-1 == F(657,10000)
assert f3(t,z)-1 == -F(635391,4000000)

t,z = F(11,10), F(9,16)
assert f2(t,z)-1 == -F(5643,32000)
assert f3(t,z)-1 == F(483021,2048000)


def c(t):
    return 2*t**3-8*t*t+13*t-8


def p(z):
    return 128*z**3-41*z*z+6*z-1


tlo,thi=F(1396608252736,10**12),F(1396608252737,10**12)
zlo,zhi=F(256342606727,10**12),F(256342606728,10**12)
assert c(tlo)<0<c(thi)
assert p(zlo)<0<p(zhi)
assert -1+4/tlo-6/tlo**2+4/tlo**3 > zlo
assert -1+4/thi-6/thi**2+4/thi**3 < zhi

print('VERIFY_OK: exact random-branch moments, Bernstein identity, two rational stability reversals, root brackets')
