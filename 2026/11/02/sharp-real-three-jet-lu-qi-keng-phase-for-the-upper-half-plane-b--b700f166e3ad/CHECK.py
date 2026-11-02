#!/usr/bin/env python3
"""Supplementary finite tests for three-jet upper-half-plane Bergman Gram kernels.

Usage: python CHECK.py. Standard-library only. Exact symbolic reasoning is
provided in RESULT.md; these finite tests do not prove the universal theorem.
"""
import cmath
import math
from fractions import Fraction

assertions = 0


def check(condition, why):
    global assertions
    if not condition:
        raise AssertionError(why)
    assertions += 1


def coeffs_from_mixed_derivatives(a, b):
    xi = [Fraction(1), a, b]
    coefficients = [Fraction(0)] * 5
    for j in range(3):
        for k in range(3):
            coefficients[j+k] += (
                (-1)**j * math.factorial(j+k+1) * xi[j]*xi[k]
                / (math.factorial(j)*math.factorial(k))
            )
    return coefficients


def factor(t, a, b):
    return 1+6*(b-a*a)*t*t+30*b*b*t**4


def kernel(z, w, a, b):
    u = z-w.conjugate()
    return -factor(1/u,a,b)/(math.pi*u*u)


def lower_roots(a, b):
    if b == 0:
        if a == 0:
            return []
        return [-1/(math.sqrt(6)*abs(a)), 1/(math.sqrt(6)*abs(a))]
    discr = (a*a-b)**2-(10/3)*b*b
    square = cmath.sqrt(discr)
    x1 = ((a*a-b)+square)/(10*b*b)
    x2 = ((a*a-b)-square)/(10*b*b)
    return [cmath.sqrt(x1),-cmath.sqrt(x1),cmath.sqrt(x2),-cmath.sqrt(x2)]


for a in [Fraction(0),Fraction(1,3),Fraction(-2,5),Fraction(7,4)]:
    for b in [Fraction(0),Fraction(3,5),Fraction(-1,2),Fraction(2)]:
        c=coeffs_from_mixed_derivatives(a,b)
        check(c==[1,0,6*(b-a*a),0,30*b*b], 'factorial coefficient expansion')

for ia in range(-12,13):
    for ib in range(-12,13):
        a=ia/4
        b=ib/4
        if b==0:
            roots=lower_roots(a,b)
            check(all(abs(r.imag if isinstance(r,complex) else 0)<1e-10 for r in roots),'pure first jet roots')
            continue
        threshold=b+math.sqrt(10/3)*abs(b)
        if abs(a*a-threshold)<1e-7:
            continue
        roots=lower_roots(a,b)
        lower=[z for z in roots if z.imag < -1e-8]
        expected=0 if a*a>threshold else 2
        check(len(lower)==expected,'lower-half-plane zero count')
        for root in roots:
            check(abs(factor(root,a,b))<2e-7, 'quartic root substitution')
        if expected==2:
            for root in lower:
                u=1/root
                z=(u.real+1j*u.imag)/2
                w=(-u.real+1j*u.imag)/2
                check(z.imag>0 and w.imag>0,'realized pair in upper half-plane')
                check(abs(kernel(z,w,a,b))<2e-6,'realized kernel zero')

for b in [1.0,-1.0,0.25,-4.0]:
    a=math.sqrt(b+math.sqrt(10/3)*abs(b))
    x=(30*b*b)**(-0.5)
    for sign in [-1,1]:
        t=sign*math.sqrt(x)
        check(abs(factor(t,a,b))<1e-9,'threshold zero')
        check(abs(12*(b-a*a)*t+120*b*b*t**3)<1e-8,'threshold multiplicity')
        check(abs(12*(b-a*a)+360*b*b*t*t)>1e-5,'no higher multiplicity')

for a,b in [(0,0),(1,0),(0,1),(2,1),(0,-1),(1,-1),(1.25,.75),(-1.5,-.5)]:
    z=.25+1.1j
    w=-.43+.71j
    check(abs(kernel(z,w,a,b)-kernel(w,z,a,b).conjugate())<1e-8,'Hermitian')
    check(kernel(z,z,a,b).real>0,'strictly positive diagonal')
    check(abs(kernel(z,z,a,b).imag)<1e-8,'real diagonal')
    det=kernel(z,z,a,b)*kernel(w,w,a,b)-abs(kernel(z,w,a,b))**2
    check(det.real> -1e-7,'Gram two-by-two positivity')

print('CHECK_OK',assertions)
