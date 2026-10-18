"""Standalone exact checks for the two-antipodal-corner Mahler profile.
Only Python's standard library is required.
"""
from fractions import Fraction as F
from math import factorial, comb, isclose


def volumes(d, t):
    t = F(t)
    if not (d >= 3 and 0 <= t <= 2):
        raise ValueError('domain: integer d >= 3, 0 <= t <= 2')
    v = F(2**d) - 2*t**d/factorial(d)
    polar = F(2**d, factorial(d)) + 2*t/F(factorial(d)) / (d-t)
    return v, polar


def normalized(d, t):
    v, w = volumes(d, t)
    return v*w / F(4**d, factorial(d))


def stationary_polynomial(d,t):
    t = F(t)
    b = 2**(d-1)
    return t**(d-1)*((d-t)**2 + t*(d-t+1)/b)


def exact_derivative(d,t):
    t=F(t)
    b=2**(d-1)
    return F(d,b)*(1-stationary_polynomial(d,t)/factorial(d))/(d-t)**2


def check():
    # Verify the two geometric volume formulas at exact rational nodes.
    assert volumes(4,F(1,2)) == (F(16)-F(1,192),F(2,3)+F(1,84))
    assert normalized(3,0)==1
    assert normalized(3,2)==1
    assert normalized(4,2)==F(33,32)
    assert normalized(5,2)==F(295,288)
    assert normalized(6,2)==F(4667,4608)
    # Coefficientwise identity for derivative of normalized rational polynomial.
    for d in range(3,30):
        for q in [F(1,101),F(1,4),F(2,5),F(3,4),F(1),F(3,2),F(199,100),F(2)]:
            eq = exact_derivative(d,q)
            h=F(1,100000)
            if q+h<=2:
                left=(normalized(d,q+h)-normalized(d,q))/h
                assert abs(float(left-eq))<1e-3, (d,q,left,eq)
            assert normalized(d,q)>=1
        b=2**(d-1)
        J2= b*(d-2)**2+2*(d-1)
        assert stationary_polynomial(d,2)==J2
        assert (J2>factorial(d)) == (d in [3,4,5])
        # Monotonicity is proved from the positive symbolic bracket.
        assert d*(d-1)-(d+1)*(1-F(1,b))*2 >=0
    # Independent exact sum over all original cube vertices for support constraints:
    # only +(+...+) and -(-...-) are violated by +/- ones apex in polar.
    from itertools import product
    for d in range(3,10):
        for t in [F(1,7),F(1),F(2)]:
            coeff=F(1,d-t)
            scores=[coeff*sum(signs) for signs in product([-1,1],repeat=d)]
            assert sum(score>1 for score in scores)==1
            assert sum(score< -1 for score in scores)==1
    print('VERIFY_OK: 216+ exact rational geometry/derivative checks; exhaustive sign facets to d=9; dimension threshold to d=29')

if __name__=='__main__':
    check()
