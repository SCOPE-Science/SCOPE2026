#!/usr/bin/env python3
"""Supplementary exact and numerical checks for the hat-spline Gabor bounds.

Requires only the Python standard library. Finite samples do not certify global extrema;
the analytic proof in RESULT.md establishes those facts.
"""
from fractions import Fraction as F
import cmath


def pos(t):
    return max(t, F(0))


def direct(b, x, z):
    """Finite Laurent sum b^(3/2)*Zak with physical integer translates."""
    total = 0j
    for k in range(-4, 5):
        total += float(pos(b-abs(x-F(k)))) * z**k
    return total


def polynomials(b, x, z):
    U, L = F(2)-b, b-F(3, 2)
    left = (float(b-1-x)/z + float(b-x) + float(b-1+x)*z + float(pos(x-U))*z*z)
    right = (float(pos(L-x))/z + float(b-F(1,2)-x)
             + float(b-F(1,2)+x)*z + float(x+L)*z*z)
    return left, right


checks = 0
for j in range(21):
    b = F(3, 2)+F(j, 80)
    L, U = b-F(3,2), F(2)-b
    A = 2*(F(7,4)-b)**2 / b**3
    B = ((3*b-2)**2+(4*b-4)**2) / b**3
    for k in range(41):
        x = F(k, 80)
        for r in range(16):
            z = cmath.exp(2j*cmath.pi*r/16)
            p, q = polynomials(b,x,z)
            assert abs(p-direct(b,x,z))<1e-11
            assert abs(q-direct(b,x+F(1,2),z))<1e-11
            H=(abs(p)**2+abs(q)**2)/float(b**3)
            assert float(A)-5e-10<=H<=float(B)+5e-10
            checks+=1
        p, q = polynomials(b,x,-1)
        assert abs(p-float(pos(U-x)))<1e-11
        assert abs(q+float(pos(x-L)))<1e-11
        p, q = polynomials(b,x,1)
        assert abs(p-float((3*b-2-x) if x<=U else (4*b-4)))<1e-11
        assert abs(q-float((4*b-4) if x<=L else (3*b-F(5,2)+x)))<1e-11
        checks+=4
    p, q = polynomials(b,F(1,4),-1)
    assert abs((abs(p)**2+abs(q)**2)/float(b**3)-float(A))<1e-12
    for x in (F(0),F(1,2)):
        p,q=polynomials(b,x,1)
        assert abs((abs(p)**2+abs(q)**2)/float(b**3)-float(B))<1e-12
    if b==F(7,4):
        assert A==0
    else:
        assert B/A==((3*b-2)**2+(4*b-4)**2)/(2*(F(7,4)-b)**2)
print(f'PASS: {checks} coefficient/phase/fiber checks; 21 exact endpoint identities')
