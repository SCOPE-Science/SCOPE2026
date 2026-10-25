#!/usr/bin/env python3
"""Standalone reproducibility checks for a binary aspiration mean-field theorem.

This checker illustrates the exact analytic proof; numerical root searches
are diagnostic, not certificates of unrestricted root counts or uniqueness.
"""
from decimal import Decimal, localcontext
from fractions import Fraction

# Exact rational lower bounds from the first four exponential-series terms.
def exp_taylor_3(x):
    return sum((x ** k) / {0:1,1:1,2:2,3:6}[k] for k in range(4))

assert exp_taylor_3(Fraction(3, 2)) == Fraction(67, 16)
assert exp_taylor_3(Fraction(9, 2)) == Fraction(493, 16)
assert Fraction(4) + Fraction(80, 493) < Fraction(67, 16)

with localcontext() as c:
    c.prec = 75
    ONE = Decimal(1)
    TWO = Decimal(2)
    THREE = Decimal(3)
    HALF = ONE / TWO

    def G(L, x):
        return ONE - TWO*x + (ONE-x)*(-L*(TWO-THREE*x)).exp() - x*(L*(ONE-THREE*x)).exp()

    def F(L, x):
        a = L*(THREE*x-TWO)
        b = L*(ONE-THREE*x)
        return (ONE-x)/(ONE+b.exp()) - x/(ONE+a.exp())

    def Gx(L, x):
        u = (-L*(TWO-THREE*x)).exp()
        v = (L*(ONE-THREE*x)).exp()
        return -TWO - u + (ONE-x)*THREE*L*u - v + x*THREE*L*v

    def Gxx(L, x):
        u = (-L*(TWO-THREE*x)).exp()
        v = (L*(ONE-THREE*x)).exp()
        return (ONE-x)*(THREE*L)**2*u - TWO*THREE*L*u - x*(THREE*L)**2*v + TWO*THREE*L*v

    def GL(L, x):
        return -(ONE-x)*(TWO-THREE*x)*(-L*(TWO-THREE*x)).exp() - x*(ONE-THREE*x)*(L*(ONE-THREE*x)).exp()

    # Finite exact-point identity checks (the identity itself is proved in RESULT.md).
    for Li in (Decimal('0.4'), THREE, Decimal('12.5')):
        for i in range(0, 21):
            x = Decimal(i) / Decimal(20)
            a = Li*(THREE*x-TWO)
            b = Li*(ONE-THREE*x)
            den = (ONE+a.exp())*(ONE+b.exp())
            assert abs(F(Li,x)*den-G(Li,x)) < Decimal('1e-65')
            assert abs(G(Li,ONE-x)+G(Li,x)) < Decimal('1e-65')
    L = THREE
    assert G(L,Decimal(0)) > 0
    assert G(L,ONE/Decimal(6)) < 0
    assert G(L,ONE/Decimal(3)) > 0
    assert G(L,HALF) == 0
    assert G(L,TWO/THREE) < 0
    assert G(L,Decimal(5)/Decimal(6)) > 0
    assert G(L,ONE) < 0

    # Diagnostic Newton solver for the analytically unique nondegenerate fold.
    LL, xx = Decimal('2.8'), Decimal('0.18')
    for _ in range(30):
        g, gx = G(LL,xx), Gx(LL,xx)
        gl = GL(LL,xx)
        gxx = Gxx(LL,xx)
        # A finite-difference derivative enters diagnostics only.
        h = Decimal('1e-18')
        gxl = (Gx(LL+h,xx)-Gx(LL-h,xx))/(TWO*h)
        det = gl*gxx - gx*gxl
        dL = (g*gxx-gx*gx)/det
        dx = (gl*gx-gxl*g)/det
        LL -= dL
        xx -= dx
    assert abs(G(LL,xx)) < Decimal('1e-55')
    assert abs(Gx(LL,xx)) < Decimal('1e-55')
    assert Decimal('2.80348') < LL < Decimal('2.80350')
    assert Decimal('0.18235') < xx < Decimal('0.18236')
    assert Gxx(LL,xx)>0 and GL(LL,xx)<0
    theta = ONE/(TWO*LL)
    assert Decimal('0.17834') < theta < Decimal('0.17836')
    print('PASS: exact exponential-series witness; 63 positive-denominator identities;')
    print('       63 symmetry checks; seven alternating sign checks; fold diagnostics.')
    print('Critical L diagnostic:',str(LL)[:37])
    print('Critical x diagnostic:',str(xx)[:37])
    print('Critical temperature diagnostic:',str(theta)[:37])
