#!/usr/bin/env python3
"""Exact finite certificate for three independent scaled Erlang completion times.

Python 3 standard library only.  The symbolic formulas and infinite-tail
inequalities are justified in RESULT.md; this program checks their finite
arithmetic predicates with exact rational numbers.
"""
from fractions import Fraction as F
from math import factorial


def probabilities(n):
    assert isinstance(n, int) and n >= 2
    r = lambda c: F(n, n + c)**n
    a = F(3*n + 2, n + 2)
    b = F(4*n + 3, n + 3)
    c = F(3*n + 3, n + 3)
    t2 = a*r(2) - F(4, 9)*b*r(3)
    tn = 1 - r(1) - a*r(2) + c*r(3)
    t1 = 1 - t2 - tn
    return t1, t2, tn


def direct_erlang_integral_for_second(n):
    # F_n(x)=1-exp(-n*x)*sum_{j=0}^{n-1}(n*x)^j/j!.
    # Integrate 4*x*exp(-2*x)*(1-exp(-x))*F_n(x) term by term.
    result = F(5, 9)
    for j in range(n):
        result -= 4*(j+1)*n**j*(F(1, (n+2)**(j+2))
                                   - F(1, (n+3)**(j+2)))
    return result


def direct_laplace_integral_for_last(n):
    r = lambda c: F(n, n+c)**n
    d = lambda c: F(n, n+c)*r(c)
    return 1 - r(1) - r(2) - 2*d(2) + r(3) + 2*d(3)


# Independently test the two closed forms against integral expansions.
for n in range(2, 33):
    t1, t2, tn = probabilities(n)
    assert t2 == direct_erlang_integral_for_second(n)
    assert tn == direct_laplace_integral_for_last(n)
    assert 0 < t1 < 1 and 0 < t2 < 1 and 0 < tn < 1
    assert t1 + t2 + tn == 1

# Finite range complementary to the proven analytic n >= 500 bounds.
for n in range(2, 500):
    t1, t2, tn = probabilities(n)
    assert t2 - t1 > F(1, 200), n
    if n == 2:
        assert tn == t2
    else:
        assert tn - t2 > F(1, 100), n

# Exact rational checks of constants used in the infinite-range proof.
E7 = sum(F(1, factorial(k)) for k in range(8))
E6 = sum(F(1, factorial(k)) for k in range(7))
E2_6 = sum(F(2**k, factorial(k)) for k in range(7))
assert E7 > F(125, 46)
assert E2_6 > F(125, 17)
assert E6 + F(1, 4410) < F(27183, 10000) < F(273, 100)
assert F(27183, 10000)**2 < F(10000, 1353)
assert F(125, 46)**3 > 20
assert F(273, 100)**3 < F(1000, 49)

# For n >= 500, the first bound dominates P_2 - P_1;
# the second (valid even for n >= 60) dominates P_n - P_2.
L21 = ((3 - F(4, 502))*F(1353, 10000)
       - F(46, 125)*F(1000, 999)
       - F(5, 9)*F(1, 20)*F(1000, 991))
L32 = (1 - F(46, 125)*F(120, 119)
       - 6*F(17, 125)*F(30, 29)
       + (F(43, 9) - F(10, 63))*F(49, 1000))
assert L21 == F(20931734927, 2484922590000)
assert L32 == F(114949, 10353000)
assert L21 > F(1, 200)
assert L32 > F(1, 100)

print('PASS: 498 finite n values (2..499); 31 independent integral cross-checks;')
print('      exponential-series rational bounds and two positive tail margins.')
print('n=2:', tuple(str(x) for x in probabilities(2)))
print('n=3:', tuple(str(x) for x in probabilities(3)))
print('n>=500 lower margins:', L21, L32)
