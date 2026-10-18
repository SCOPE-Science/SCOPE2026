"""Reproduce symbolic octahedral covariogram identities and independent 3D volume checks.

Requires Python 3, sympy, numpy, scipy. Finite checks corroborate, not replace, the proof.
"""
from itertools import product
from math import factorial, sqrt

import numpy as np
import sympy as S
from scipy.spatial import ConvexHull, HalfspaceIntersection

q, R, r = S.symbols('q R r', real=True, nonnegative=True)

# Derive base 3D lens by integrating the three z-coordinate regimes.
base = (
    2*S.integrate((2*R-3*q)*(R-q), (R, S.Rational(3,2)*q, 1))
    + (2-3*q)*(q-S.Rational(3,4)*q**2)
)
assert S.simplify(base-(S.Rational(4,3)-3*q+S.Rational(3,2)*q**2)) == 0

# Symbolic all-dimensional shell integration, first for d=3 and then 4..12.
def exact_formula(d,k):
    v=S.Rational(2)**d/factorial(d)
    if k==1:
        return v*(1-q/2)**d
    if k==2:
        return v*(1-q)**(d-1)*(1+S.Rational(d-2,2)*q)
    a=3*q/2
    A=1-a
    return v*A**(d-2)*(A*A+S.Rational(d,2)*a*A+S.Rational(d*(d-1),12)*a*a)

for d in range(3, 13):
    a=S.Rational(3,2)*q
    integrand=S.Rational(2,3)*(1-r)*(1-r-a)*(2*(1-r)-a)
    shell=(S.Rational(2)**(d-3)/factorial(d-4))*r**(d-4) if d>3 else None
    if d>3:
        val=S.integrate(shell*integrand, (r, 0, 1-a))
        assert S.simplify(val-exact_formula(d,3))==0, ('k3',d)
    for k in (1,2,3):
        assert S.simplify(exact_formula(d,k).subs(q,0)-S.Rational(2)**d/factorial(d))==0
        assert S.simplify(exact_formula(d,k).subs(q,S.Rational(2,k)))==0

# Independently reconstruct each 3D intersection from all eight facet inequalities.
signs=list(product((-1,1), repeat=3))
N=0
for k in (1,2,3):
    v=np.array([1]*k+[0]*(3-k),dtype=float)
    ts=[S.Rational(1,13),S.Rational(1,5),S.Rational(1,3),S.Rational(2,5),S.Rational(1,2),S.Rational(3,5)]
    for t in ts:
        if t>=S.Rational(2,k):
            continue
        z=float(t)
        planes=[]
        for e in signs:
            e=np.array(e,dtype=float)
            b=min(1.0,1.0+z*np.dot(e,v))
            planes.append([*e,-b])
        verts=HalfspaceIntersection(np.array(planes), z*v/2).intersections
        measured=ConvexHull(verts).volume
        expected=float(exact_formula(3,k).subs(q,t))
        assert abs(measured-expected)<2e-12, (k,str(t),measured,expected)
        N+=1

# Check exact orientation comparisons and crossing locations.
s=S.symbols('s', real=True, nonnegative=True)
h1=exact_formula(3,1).subs(q,s)
h2=exact_formula(3,2).subs(q,s/S.sqrt(2))
h3=exact_formula(3,3).subs(q,s/S.sqrt(3))
assert S.simplify(h1-h2 + s*((1+S.sqrt(2))*s**2-6*s+12-6*S.sqrt(2))/6)==0
assert S.simplify(h1-h3 + s*(s**2-3*s+12-6*S.sqrt(3))/6)==0
assert S.simplify(h2-h3 - s*(S.sqrt(2)*s**2-3*s+6*(S.sqrt(3)-S.sqrt(2)))/6)==0
assert 57<24*sqrt(6)
s13=(3-S.sqrt(24*S.sqrt(3)-39))/2
s12=(3-S.sqrt(9-6*S.sqrt(2)))/(1+S.sqrt(2))
assert 0<float(s13)<float(s12)<2/sqrt(3)<sqrt(2)<2
print('OCTAHEDRAL_COVARIOGRAM_OK')
print('all_dimension_symbolic_checks=3..12; independent_3d_convex_hulls=',N)
print('sharp_crossovers_s13=',S.N(s13,14),'s12=',S.N(s12,14))
