#!/usr/bin/env python3
"""Independent exact and quadrature checks for uniform interior pair-distance moments of triangles."""
import math
from fractions import Fraction
from itertools import product

import sympy as sp
import numpy as np

x, y, u, v = sp.symbols('x y u v')
A, B, C = sp.symbols('A B C')
Q = A*(x-u)**2 + B*(y-v)**2 + (A+B-C)*(x-u)*(y-v)


def integrate_product_simplex(poly):
    """Exact integral under two iid uniform barycentric pairs on the unit 2-simplex."""
    p = sp.Poly(sp.expand(poly), x, y, u, v)
    total = 0
    for exps, coefficient in p.terms():
        i, j, k, l = exps
        moment = sp.Rational(4*math.factorial(i)*math.factorial(j)*math.factorial(k)*math.factorial(l),
                             math.factorial(i+j+2)*math.factorial(k+l+2))
        total += coefficient*moment
    return sp.factor(total)

s1=A+B+C
s2=A*B+A*C+B*C
s3=A*B*C
formulas=[s1/18, (A*A+B*B+C*C)/60, (23*s1**3-62*s1*s2+20*s3)/4200]
for k, expected in enumerate(formulas,1):
    actual=integrate_product_simplex(Q**k)
    assert sp.simplify(actual-expected)==0, (k, actual, expected)

# Heron's formula and inverse moment identity, checked as polynomial identities.
area_sq=(4*s2-s1**2)/16
assert sp.simplify(area_sq-(sp.Rational(81,4)*formulas[0]**2-sp.Rational(15,2)*formulas[1]))==0

# Two distinct nondegenerate triangle shapes with precisely the same first two moments.
d=sp.Rational(1,4)
triples=((1+d,1-d/2,1-d/2),
         (1+sp.sqrt(3)*d/2, 1, 1-sp.sqrt(3)*d/2))
mm=[]
for t in triples:
    moments=[sp.simplify(z.subs({A:t[0],B:t[1],C:t[2]})) for z in formulas]
    aa, bb, cc=t
    assert sp.simplify(4*(aa*bb+bb*cc+cc*aa)-(aa+bb+cc)**2)>0
    assert all(z>0 for z in t)
    mm.append(moments)
assert mm[0][:2]==mm[1][:2] and mm[0][0]==sp.Rational(1,6)
assert mm[0][1]==sp.Rational(33,640)
assert sp.simplify(mm[0][2]-mm[1][2])==sp.Rational(1,53760)

# Independent 4D tensor Gaussian quadrature over independent area-uniform points.
# The transformation x=a, y=(1-a)b has Jacobian 1-a and covers the standard triangle.
from numpy.polynomial.legendre import leggauss
nodes, weights=leggauss(10)
nodes=(nodes+1)/2
weights=weights/2
pairs=[]
for ia in range(len(nodes)):
    for ib in range(len(nodes)):
        a,b=float(nodes[ia]),float(nodes[ib])
        pairs.append((a,(1-a)*b,float(2*(1-a)*weights[ia]*weights[ib])))
assert abs(sum(q[2] for q in pairs)-1)<1e-13
for a,b,c in [(1.,1.,1.),(3.,4.,5.),(2.,3.,4.),(1.1,1.7,2.3)]:
    abc={A:a*a,B:b*b,C:c*c}
    predicted=[float(f.subs(abc)) for f in formulas]
    observed=np.zeros(3)
    for x0,y0,w0 in pairs:
        for x1,y1,w1 in pairs:
            dx=x0-x1;dy=y0-y1
            q=a*a*dx*dx+b*b*dy*dy+(a*a+b*b-c*c)*dx*dy
            observed+=w0*w1*np.array([q,q*q,q*q*q])
    assert np.allclose(observed,predicted,rtol=1e-12,atol=1e-12),(a,b,c,observed,predicted)

# The two extreme isosceles fibers have equal lower moments and sharp cubic separation.
t = sp.symbols('t', positive=True)
endpoints = [(1+t, 1-t/2, 1-t/2), (1+t/2, 1+t/2, 1-t)]
end_moments = [[sp.factor(f.subs({A:a,B:b,C:c})) for f in formulas]
               for a,b,c in endpoints]
assert end_moments[0][:2] == end_moments[1][:2]
assert sp.simplify(end_moments[0][2]-end_moments[1][2]-t**3/sp.Integer(420))==0
assert sp.simplify((end_moments[0][2]+end_moments[1][2])/2
                   + sp.Rational(249,175)*end_moments[0][0]
                   *(6*end_moments[0][0]**2-5*end_moments[0][1]))==0

# The two moment-identical triangles have the same squared area, by both identities.
for moments in mm:
    m1,m2,_=moments
    assert sp.simplify(sp.Rational(81,4)*m1**2-sp.Rational(15,2)*m2)==sp.Rational(45,256)
print('VERIFY_OK: symbolic all-shape identities k=1,2,3; exact moment collision; independent 4D quadrature on 4 triangles')
