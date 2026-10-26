#!/usr/bin/env python3
"""Finite exact and complex checks for a three-point Bergman determinant identity."""
import cmath
from fractions import Fraction
from itertools import product
from math import cos, sin, pi


def det3(m):
    return (m[0][0] * (m[1][1]*m[2][2] - m[1][2]*m[2][1])
            - m[0][1]*(m[1][0]*m[2][2] - m[1][2]*m[2][0])
            + m[0][2]*(m[1][0]*m[2][1] - m[1][1]*m[2][0]))


def predicted(u, v, w):
    return u*v*w*(6-2*(u+v+w)+u*v*w)

# The Cauchy/Szego-to-Bergman three-variable algebraic identity.
q_values = [Fraction(i, 9) for i in range(1, 9)]
for u, v, w in product(q_values, repeat=3):
    a, b, c = 1-u, 1-v, 1-w
    real_twice = u*v*w + 2-u-v-w
    recovered = 1-a*a-b*b-c*c + real_twice*real_twice-2*a*b*c
    assert recovered == predicted(u,v,w)
    P = 6-2*(u+v+w)+u*v*w
    assert P-2*u+u*v*w == 2*((1-u)*(2-v*w)+(1-v)*(1-w))
    assert P > 0 and P-2*u+u*v*w > 0
    assert -2*(u-v) == (P-2*u+u*v*w)-(P-2*v+u*v*w)

for numerator in range(1, 29):
    t = Fraction(numerator,30)
    u = 3*t/(1+t+t*t)
    closed = 81*t**3*(t**3+2)*(2*t**3+1)/(1+t+t*t)**6
    assert predicted(u,u,u) == closed

for t in (0.02, 0.14, 0.37, 0.73, 0.95):
    for angles in ((0., 1.2, 4.7), (.3, 2.1, 5.8), (0., 2*pi/3, 4*pi/3),
                   (.12, .2, 3.7), (0., .65, 1.4)):
        z = [t**.5*cmath.exp(1j*theta) for theta in angles]
        B = [[(1-t)**2/(1-z[i]*z[j].conjugate())**2
              for j in range(3)] for i in range(3)]
        uvs = [abs((z[i]-z[(i+1)%3])/(1-z[i]*z[(i+1)%3].conjugate()))**2
               for i in range(3)]
        direct = det3(B)
        calc = predicted(*uvs)
        assert abs(direct.imag) < 2e-11
        assert abs(direct.real-calc) < 3e-11
        exact_best = float(81*Fraction(round(t*100),100)**3
                           *(Fraction(round(t*100),100)**3+2)
                           *(2*Fraction(round(t*100),100)**3+1)
                           /(1+Fraction(round(t*100),100)
                             +Fraction(round(t*100),100)**2)**6)
        assert direct.real <= exact_best+3e-11
print('CHECK_OK: rational determinant/derivative identities, sharp values, and complex triples')
