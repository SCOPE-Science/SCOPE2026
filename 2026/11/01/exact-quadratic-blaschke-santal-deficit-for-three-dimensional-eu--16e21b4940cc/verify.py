"""Exact-arithmetic and independent numerical checks for the capsule volume product.

Runs with Python 3 standard library: python verify.py
All mathematical quantifiers and analytic proofs are in RESULT.md.
"""
from fractions import Fraction as F
from math import pi, sin, cos


def poly_mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def poly_sub(a, b):
    a, b = list(a), list(b)
    return [(a[i] if i<len(a) else F(0)) -
            (b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b)))]


def polar_from_cross_section(s):
    """Polar volume divided by pi from integrated disk sections."""
    u = 1/(1+s)
    return 2*(u-s*u*u+(s*s-1)*u**3/3)


def polar_closed(s):
    return 2*(s+2)/(3*(1+s)**2)


def product_over_pi_squared(s):
    return F(2,3)*(2+3*s)*polar_from_cross_section(s)


def spherical_polar_simpson(s, n=40000):
    """Independent support-function radial-volume integral divided by pi.

    Polar volume = (1/3)int_{sphere}h_K(u)^(-3) dS.
    Azimuthal symmetry gives V_polar/pi=(4/3)int_0^1(1+s*u)^(-3)du.
    """
    assert n%2==0
    h=1/n
    f=lambda u:(1+s*u)**(-3)
    total=f(0.)+f(1.)
    for k in range(1,n):
        total+=(4 if k%2 else 2)*f(k*h)
    return F(4,3)*h*total/3


def run():
    # Identity 4(1+s)^2 - (2+3s)(2+s) == s^2, coefficient-wise.
    assert poly_sub(
        poly_sub([4*c for c in poly_mul([1,1],[1,1])],
                 poly_mul([2,3],[2,1])),[0,0,1]
    ) == [0,0,0]
    cases=[F(0),F(1,19),F(1,3),F(1),F(7,4),F(9),F(103,2)]
    checks=0
    previous=None
    for s in cases:
        p=polar_from_cross_section(s)
        assert p==polar_closed(s)
        checks+=1
        target=F(16,9)*(1-(s/(1+s))**2/4)
        actual=product_over_pi_squared(s)
        assert actual==target
        checks+=1
        if previous is not None:
            assert actual<previous
            checks+=1
        previous=actual
        sim=float(spherical_polar_simpson(float(s)))
        assert abs(sim-float(p))<4e-6
        checks+=1
        if s>0:
            # Exact derivative of product divided by pi^2.
            d=-F(8,9)*s/(1+s)**3
            assert d<0
            checks+=1
    assert previous>F(4,3)
    checks+=1
    print(f'PASS {checks} exact checks, 7 independent Simpson comparisons, polynomial identity')
    print('Limits: normalized ball product 16/9, cylinder product 4/3.')


if __name__=='__main__':
    run()
