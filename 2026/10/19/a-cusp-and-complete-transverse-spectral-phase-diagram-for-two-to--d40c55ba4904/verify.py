"""Independent symbolic identities and sample root counts for the two-circle flow.

The rigorous continuum statement is supplied by the accompanying proof; this script
checks algebraic identities and illustrative parameter regimes only.
"""
from math import cos, sin, pi, sqrt
import sympy as s

x,y,z,a,b,c=s.symbols('x y z a b c',real=True)
t=s.symbols('t')
for sig in (-1,1):
    f=s.Matrix((z,z*(-a*y-b*y*y-c*x*z),x*x+y*y-sig*x))
    J=f.jacobian((x,y,z)).subs(z,0)
    Q=2*x-sig-2*a*y**2-2*b*y**3
    assert s.expand(J.charpoly(t).as_expr()-t*(t**2-Q))==0
    assert s.simplify(J**3-Q*J)==s.zeros(3)

u=s.symbols('u',positive=True)
v=s.sqrt(1-u*u)
A=2/v+6*v/u**2
Bm=2*a/u-4*v/u**3
Bp=2*a/u+4*v/u**3
assert s.simplify(s.diff(Bm,u)-2*(A-a)/u**2)==0
assert s.simplify(s.diff(Bp,u)+2*a/u**2+4/(u**2*v)+12*v/u**4)==0
assert s.simplify(s.diff(A,u)+2*(2*u**4-9*u**2+6)/(u**3*v**3))==0
ustar=s.sqrt((9-s.sqrt(33))/4)
a0=float(A.subs(u,ustar)); b0=float(Bm.subs({u:ustar,a:A.subs(u,ustar)}))
assert 7.81<a0<7.82 and 14.97<b0<14.99

# On each circle there are always two roots (one upper, one lower),
# except for the cusp-created lower pair. Count sign-changing roots
# by sampling densely and separately identify tangent roots at folds.
def value(th,aa,bb):
    return cos(th)-aa*sin(th)**2/2-bb*sin(th)**3/4

def roots(aa,bb,n=16001):
    # Dense grid is a diagnostic, not a proof of exhaustive root counts.
    h=2*pi/n
    return [j for j in range(n) if value(j*h,aa,bb)*value((j+1)*h,aa,bb)<0]
for aa,bb,want in ((4,4.5,2),(10,20,4),(7,15,2),(10,18,2),(10,22,2),(20,38,2)):
    got=len(roots(aa,bb))
    assert got==want,(aa,bb,got,want)

from fractions import Fraction as F
# Example with a=10,b=20: strict brackets create two additional
# roots on the bottom-right quadrant, in addition to its central root.
assert sqrt(1-float(F(3,4)**2))-5*float(F(3,4)**2*(1-F(3,4)))<0
assert sqrt(1-float(F(15,16)**2))-5*float(F(15,16)**2*(1-F(15,16)))>0

# At the full nilpotent spectrum Q=0, nonzero y guarantees nilpotency
# index exactly three.  A cusp or fold is spectral, not a Hopf theorem.
print('PASS: symbolic Jacobian/characteristic polynomial/J-cubic,')
print('      critical derivative identities, cusp threshold, and six sampled root regimes.')
print('a_star=%.12f; b_star=%.12f'%(a0,b0))
