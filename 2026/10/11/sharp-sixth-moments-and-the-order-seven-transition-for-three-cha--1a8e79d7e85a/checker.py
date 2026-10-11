"""Reproducible finite checks for a three-character sixth-moment inequality.

Run: python checker.py
Only the Python standard library is required. Finite tests corroborate an
algebraic proof and do not establish its all-group quantifiers.
"""
import cmath
import itertools
import math
import random
from fractions import Fraction


def cubic_coeffs(a,b,c):
    # Cubic convolution, ordered by the exponent of the middle generator.
    return (a**3,3*a*a*b,3*a*a*c+3*a*b*b,
            b**3+6*a*b*c,3*a*c*c+3*b*b*c,3*b*c*c,c**3)


def poly_six(a,b,c):
    return sum(abs(v)**2 for v in cubic_coeffs(a,b,c))


def moment(n,a,b,c):
    return sum(abs(a+b*cmath.exp(2j*math.pi*j/n)
                   +c*cmath.exp(4j*math.pi*j/n))**6 for j in range(n))/n


def exact_polynomial(a,b,c):
    # For nonnegative coefficients, a,b,c are nonnegative integers.
    u=a*a+c*c
    w=b*b
    p=a*c
    return (u**3+9*u*u*w+9*u*w*w+w**3
            +(18*u*w+12*w*w)*p+(6*u+18*w)*p*p)


def run():
    assert (35*(math.sqrt(105)-3)/48)>5
    r=(math.sqrt(105)-5)/4
    K=35*(math.sqrt(105)-3)/48
    ratio=math.sqrt(r)
    checks=0
    for a,b,c in itertools.product(range(9),repeat=3):
        value=exact_polynomial(a,b,c)
        coeff=cubic_coeffs(a,b,c)
        assert value == sum(x*x for x in coeff)
        checks+=1
    rng=random.Random(20261009)
    for n in (7,8,9,10,11,12,13,14,17,19,23,31,47):
        for j in range(260):
            x=[complex(rng.uniform(-2,2),rng.uniform(-2,2)) for _ in range(3)]
            a,b,c=x
            lhs=moment(n,a,b,c)
            via=poly_six(a,b,c)
            scale=(abs(a)**2+abs(b)**2+abs(c)**2)**3
            assert abs(lhs-via)<8e-10*max(1,via)
            assert lhs <= K*scale + 8e-10*max(1,scale)
            checks+=2
        for j in range(11):
            theta=math.pi*j/17
            a=cmath.exp(1j*rng.uniform(-math.pi,math.pi))
            b=a*ratio*cmath.exp(1j*theta)
            c=a*cmath.exp(2j*theta)
            lhs=moment(n,a,b,c)
            den=(abs(a)**2+abs(b)**2+abs(c)**2)**3
            assert abs(lhs/den-K)<3e-12
            checks+=1
    a=1.0;b=ratio;c=1.0
    for n in range(3,7):
        assert moment(n,a,b,c)/(a*a+b*b+c*c)**3>K+1e-5
        checks+=1
    # The moment is independent of the group size in the collision-free range.
    print('VERIFY_OK checks={} constant={:.12f} inner_outer_modulus={:.12f}'.format(checks,K,ratio))

if __name__=='__main__':
    run()
