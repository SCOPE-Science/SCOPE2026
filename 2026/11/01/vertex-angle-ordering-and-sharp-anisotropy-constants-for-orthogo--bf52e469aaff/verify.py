#!/usr/bin/env python3
"""Independent numerical checks for orthogonal-simplex vertex angles.
Requires Python 3.9+ and scipy. All universal inequalities are proved in RESULT.md.
"""
import math
import itertools
from scipy.integrate import quad
from scipy.special import ndtr

CHECKS = 0

def check(statement, description):
    global CHECKS
    if not statement:
        raise AssertionError(description)
    CHECKS += 1


def p3_triedral(L, b, c):
    denom = (L + math.hypot(L, b)) * (L + math.hypot(L, c))
    return math.atan((b*c)/denom) / (2*math.pi)


def p3_gaussian(L,b,c):
    # Integrate conditional Gaussian probability over two positive coordinates.
    # Compared with *independent* spherical trihedral formula.
    def outer(x):
        f=lambda y: math.exp(-y*y/2)*ndtr(-(L/b*x+L/c*y)) / math.sqrt(2*math.pi)
        return math.exp(-x*x/2)/math.sqrt(2*math.pi)*quad(f,0,8,epsabs=2e-10)[0]
    return quad(outer,0,8,epsabs=2e-10)[0]


def lower_const(d):
    if d == 2:
        return 1/8
    if d == 3:
        return math.atan(3 - 2*math.sqrt(2))/(2*math.pi)
    raise ValueError


def upper_const(d):
    return math.gamma(d/2)/(2*math.factorial(d-1)*math.pi**(d/2))


def all_vertex_angles_3(a):
    angles=[1/8]
    for i in range(3):
        others=[a[j] for j in range(3) if j!=i]
        angles.append(p3_triedral(a[i],*others))
    return angles

for a in [(1.,1.,1.),(4.,1.,1.),(1.,1.8,3.),(0.21,0.6,1.3),
          (5.,5.,0.09),(1.,0.01,0.0001),(9.,3.,1.)]:
    vals=all_vertex_angles_3(a)
    check(min(vals)==min(vals[1:]), 'origin cannot minimize')
    longest=max(a)
    for i in range(3):
        for j in range(3):
            check((a[i]>a[j]) == (vals[i+1]<vals[j+1]), 'wrong strict vertex-order')
    q=math.prod(a)/longest**3
    p=min(vals[1:]); c=lower_const(3); u=upper_const(3)
    check(c*q-1e-14<=p<=u*q+1e-14, 'sharp bounds violated')
    if not (min(a)==max(a)):
        check(c*q+1e-13<p<u*q-1e-13,'strict bounds violated')

for L,b,c in [(1.,1.,1.),(2.,1.,1.),(3.,1.,2.),(7.,0.5,0.7),
              (1.,0.21,0.24),(4.,2.,4.)]:
    v=p3_triedral(L,b,c)
    integral=p3_gaussian(L,b,c)
    check(abs(v-integral)<3e-9,f'Gaussian and solid geometry conflict: {L,b,c} {v} {integral}')

for d in range(2,10):
    u=upper_const(d)
    val=quad(lambda r: r**(d-1)*math.exp(-r*r/2),0,20,epsabs=1e-13)[0]
    val/=math.factorial(d-1)*(2*math.pi)**(d/2)
    check(abs(u-val)<1e-13, 'upper integral gamma calculation')

for t in [10**(-q) for q in range(1,7)]:
    p=p3_triedral(1.,t,t)
    check(abs(p/t**2-upper_const(3))<0.15*t, 'asymptotic constant')

for t in [k/20 for k in range(1,21)]:
    p=math.atan(t)/(2*math.pi)
    check(1/8*t-1e-14<=p<=t/(2*math.pi)+1e-14,'d2 profile bounds')
check(abs(lower_const(3)-p3_triedral(1,1,1))<1e-15,'equal-leg lower equality')
print(f'PASS: {CHECKS} deterministic numerical and analytic-identity checks')
