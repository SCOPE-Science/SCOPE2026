"""Standalone checks of the diamond p-Bessel order-positivity identities.

Python 3 standard library only. Supplementary finite checks, not an infinite proof.
"""
from fractions import Fraction
from math import sin, cos, pi, factorial, isclose

checks = 0
for a in [Fraction(0), Fraction(1, 6), Fraction(2, 5), Fraction(1, 2), Fraction(3, 4), Fraction(1)]:
    b = 1 - a
    for k in range(16):
        polynomial = sum(a ** (2*j) * b ** (2*(k-j)) for j in range(k+1))
        if a != b:
            divided = (a**(2*k+2)-b**(2*k+2))/(a-b)
        else:
            divided = (2*k+2) * a**(2*k+1)
        assert polynomial == divided
        checks += 1

def source_series(order, a, r, terms=30):
    b = 1-a
    return 4*sum(((-1)**k)*r**(2*k+order)*sum(a**(2*j)*b**(2*(k-j)) for j in range(k+1))/factorial(2*k+order+1) for k in range(terms))

def h(r,x):
    if x==0:
        return r*r/6
    return (1-sin(r*x)/(r*x))/(x*x)

def closed_four(a,r):
    b=1-a
    if a==b:
        x=a
        return 4*(r*x*(2+cos(r*x))-3*sin(r*x))/(r*x**4)
    return 4*(h(r,a)-h(r,b))/(b-a)

for a in [.0,.12,.2,.4,.5,.7,1.0]:
    for r in [.75,1.25,2.0,3.5,5.0,7.0]:
        val=closed_four(a,r)
        series=source_series(4,a,r)
        assert val>0, (a,r,val)
        assert isclose(val,series,rel_tol=2e-5,abs_tol=1e-8), (a,r,val,series)
        checks+=2

# Exact phase witnesses follow analytically; numerical values only replay signs.
assert 4*sin(3*pi/2)/(3*pi/2)<0
assert 4*sin(3*pi/2)<0
assert -8*cos(4*pi/2)+16*sin(4*pi/2)/(4*pi)<0
assert -200/(9*pi)<0
checks+=4
print('PASS',checks,'supplementary checks: exact coefficients, independent series, phases')
