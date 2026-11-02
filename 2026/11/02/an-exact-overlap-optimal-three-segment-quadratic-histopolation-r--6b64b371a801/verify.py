"""Exact-rational checks for the three-interval quadratic histopolation theorem.

No third-party libraries required. Finite checks support, but do not replace,
the analytic all-parameter proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt

checks = 0

def average_monomial(left, right, power):
    return (right**(power + 1) - left**(power + 1)) / ((power + 1) * (right - left))

def weights(e, x):
    a = 1 - e
    d = 1 + a
    l = (3*x*x - 2*x - a*a) / (2*d)
    r = (3*x*x + 2*x - a*a) / (2*d)
    o = (d + a*a - 3*x*x) / d
    return l, o, r

def data_weights(e, x):
    d = e * (1-e)
    h = x*x - F(1, 3)
    return (1 + 3*h/d, -x/e - 3*h/(2*d), x/e - 3*h/(2*d))

for denominator in range(2, 44):
    for numerator in range(1, denominator):
        e = F(numerator, denominator)
        a = 1 - e
        d = 1 + a
        # Exact polynomial reproduction from three actual overlapping segments.
        for power in range(3):
            m0 = average_monomial(F(-1), F(1), power)
            ml = average_monomial(F(-1), F(1)-e, power)
            mr = average_monomial(F(-1)+e, F(1), power)
            c2 = 3*(m0 - (ml + mr)/2)/(e*(1-e))
            c1 = (mr-ml)/e
            c0 = m0 - c2/3
            assert (c0,c1,c2) == tuple(F(int(power == j)) for j in range(3))
            checks += 1
        n0 = 1 + 2*a*a/d
        n1 = 1 + 2*e*(3-e)/d
        bound = max(n0, n1)
        lebesgue = 1 + 4/(e*(1-e))
        for ix in range(0, 41):
            x = F(ix-20, 20)
            wl, wo, wr = weights(e,x)
            assert wl + wo + wr == 1
            norm = abs(wl) + abs(wo) + abs(wr)
            assert norm <= bound
            cfull, cl, cr = data_weights(e,x)
            assert abs(cfull)+abs(cl)+abs(cr) <= lebesgue
            # Coefficients of the original overlapping data, evaluated
            # against disjoint left/core/right cell signals, are identical.
            for fl, fo, fr in product((-1,1),repeat=3):
                total = e*fl + 2*(1-e)*fo + e*fr
                m0 = total/2
                ml = (e*fl+2*(1-e)*fo)/(2-e)
                mr = (e*fr+2*(1-e)*fo)/(2-e)
                reconstructed = cfull*m0 + cl*ml + cr*mr
                assert reconstructed == wl*fl + wo*fo + wr*fr
                checks += 1
            checks += 3
        for x in (F(0), F(-1), F(1)):
            wl, wo, wr = weights(e,x)
            assert abs(wl)+abs(wo)+abs(wr) == (n0 if x==0 else n1)
            checks += 1
        assert sum(abs(v) for v in data_weights(e,F(1))) == lebesgue
        checks += 1

root = (sqrt(17)-1)/4
opt_e = 1-root
optimum = 1.5*(sqrt(17)-3)
assert 0 < opt_e < 1 and abs((1+2*root*root/(1+root)) - optimum) < 1e-12
for j in range(1001):
    eps = (j+1)/1002
    a = 1-eps
    nm = max(1+2*a*a/(1+a), 1+2*eps*(3-eps)/(2-eps))
    assert nm >= optimum - 1e-12
    checks += 1
print(f"PASS: {checks} exact-rational coefficient/reproduction/norm/overlap checks and numerical optimum comparisons")
