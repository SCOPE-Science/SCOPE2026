"""Reproducible finite checks for the two-community Galam theorem.

Python 3 standard library only. The analytical proof in RESULT.md supplies
unbounded quantifiers; these are exact identities and finite numerical tests.
"""
from fractions import Fraction as F


def source_map(p, u, v):
    return ((1-u)*p**3 + 3*(1-v)*p**2*(1-p)
            + 3*v*p*(1-p)**2 + u*(1-p)**3)


def coeff(u, v):
    return F(3, 2)*(u+v-1), (3*v-1-u)/2


def P(z, a, b):
    return a*z-b*z**3


profiles = [(F(9, 10), F(9, 10)), (F(19, 20), F(9, 10)),
            (F(5, 6), F(5, 6)), (F(3, 4), F(3, 4)),
            (F(1), F(1)), (F(11, 12), F(5, 6))]
for u, v in profiles:
    a, b = coeff(u, v)
    assert a > 0 and b > 0 and a-3*b == 3*(u-v)
    assert P(F(1), a, b) == 2*u-1
    for numerator in range(-9, 10):
        z = F(numerator, 10)
        assert 2*source_map((1+z)/2, u, v)-1 == -P(z, a, b)

# Nonlinear two-step Taylor coefficient via exact polynomial arithmetic.
from itertools import product

def poly_mul(f, g, maxdeg):
    h = [F(0)]*(maxdeg+1)
    for i, x in enumerate(f):
        for j, y in enumerate(g):
            if i+j <= maxdeg:
                h[i+j] += x*y
    return h

for (uA, vA), (uB, vB) in product(profiles, repeat=2):
    aA, bA = coeff(uA, vA)
    aB, bB = coeff(uB, vB)
    # G_A(x) = P_A(P_B(x))
    inner = [F(0), aB, F(0), -bB]
    cube = poly_mul(poly_mul(inner, inner, 5), inner, 5)
    assert aA*inner[1]-bA*cube[1] == aA*aB
    assert aA*inner[3]-bA*cube[3] == -(aA*bB+bA*aB**3)

# Below, at, and above threshold, checked with exact rational parameters.
sub = ((F(3, 4), F(3, 4)), (F(3, 4), F(3, 4)))
critical = ((F(5, 6), F(5, 6)), (F(5, 6), F(5, 6)))
supercrit = ((F(19, 20), F(9, 10)), (F(9, 10), F(9, 10)))
assert coeff(*sub[0])[0]*coeff(*sub[1])[0] < 1
assert coeff(*critical[0])[0]*coeff(*critical[1])[0] == 1
assert coeff(*supercrit[0])[0]*coeff(*supercrit[1])[0] == F(153, 100)

# Illustrative generic positive/negative basin tests; not an infinite proof.
uA, vA = supercrit[0]; uB, vB = supercrit[1]
aA, bA = map(float, coeff(uA, vA))
aB, bB = map(float, coeff(uB, vB))

def step(x, y):
    return -P(y, aA, bA), -P(x, aB, bB)

for x0, y0 in [(0.4, 0.5), (-0.7, -0.6), (0.4, -0.5), (-0.7, 0.6)]:
    x, y = x0, y0
    for t in range(500):
        x, y = step(x, y)
    if x0*y0 > 0:
        xx, yy = step(x, y)
        assert x*xx < 0 and y*yy < 0
        xxx, yyy = step(xx, yy)
        assert abs(xxx-x)+abs(yyy-y) < 1e-10
    else:
        xx, yy = step(x, y)
        assert x*y < 0 and abs(xx-x)+abs(yy-y) < 1e-10
print("VERIFY_OK: exact triad reduction, 36 composition certificates and four basins")
