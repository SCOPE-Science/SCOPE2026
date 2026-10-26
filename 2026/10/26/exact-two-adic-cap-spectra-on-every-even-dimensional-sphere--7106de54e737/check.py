#!/usr/bin/env python3
"""Exact rational cross-check of cap-convolution eigenvalue identities.

Mathematical objects are defined in RESULT.md. SymPy 1.x required.
These finite tests supplement, and do not replace, the all-degree proof.
"""
import math
from fractions import Fraction
from sympy import Rational, Symbol, gegenbauer, integrate, factorial, binomial, simplify

x = Symbol('x')


def v2_integer(n):
    n = abs(int(n))
    assert n != 0
    return (n & -n).bit_length() - 1


def v2_rational(a):
    a = Rational(a)
    assert a != 0
    return v2_integer(a.p) - v2_integer(a.q)


cutoffs = [Rational(1, 2), Rational(-1, 2), Rational(3, 4),
           Rational(-3, 8), Rational(1, 6), Rational(3, 10),
           Rational(5, 14)]
N = 0
for k in range(1, 6):
    for c in cutoffs:
        q = int(c.q)
        s = v2_integer(q)
        assert s >= 1
        B = integrate((1-x*x)**(k-1), (x, c, 1))
        assert v2_rational(B) == -(2*k-1)*s
        N += 1
        for ell in range(0, 19):
            if ell == 0:
                eigen_direct = Rational(1)
            else:
                alpha = Rational(2*k-1, 2)
                base = gegenbauer(ell, alpha, x)
                cbase1 = base.subs(x, 1)
                numerator = integrate(base*(1-x*x)**(k-1), (x, c, 1))
                eigen_direct = simplify(numerator / (B * cbase1))
                cm = gegenbauer(ell-1, Rational(2*k+1, 2), c)
                assert v2_rational(cm) == -(ell-1)*s - v2_integer(math.factorial(ell-1))
                eigen_formula = simplify(Rational(2*k-1, ell*(ell+2*k-1)) *
                                         (1-c*c)**k * cm / (B*cbase1))
                assert simplify(eigen_direct-eigen_formula) == 0, (k,c,ell)
            predicted = -ell*s -v2_integer(math.factorial(ell+2*k-1)//math.factorial(2*k-2))
            assert v2_rational(eigen_direct) == predicted, (k,c,ell,eigen_direct,predicted)
            N += 1
print('PASS: exact even-sphere cap spectral formula and 2-adic valuations')
print(f'Verified {N} exact rational tests for k=1..5, 7 rational cutoffs, degrees 0..18.')
print('Examples:')
for k,c,ell in [(1,Rational(1,2),3),(2,Rational(1,2),1),(2,Rational(3,4),2),(3,Rational(-3,8),5)]:
    alpha = Rational(2*k-1,2)
    B = integrate((1-x*x)**(k-1), (x,c,1))
    eig = simplify(integrate(gegenbauer(ell,alpha,x)*(1-x*x)**(k-1),(x,c,1)) /
                   (B*gegenbauer(ell,alpha,1)))
    print('k,c,ell,eigen,v2 =',k,c,ell,eig,v2_rational(eig))
