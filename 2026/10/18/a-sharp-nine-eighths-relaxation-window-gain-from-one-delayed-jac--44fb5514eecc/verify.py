#!/usr/bin/env python3
"""Reproduce exact characteristic/stability identities for three Jacobi message schedules.

Requires sympy and numpy. This is a deterministic executable comparison, not
an exhaustive numerical proof of stability over all real parameters.
"""
import math
import numpy as np
import sympy as sp

checks = 0

def eq(a, b):
    global checks
    assert sp.simplify(a - b) == 0, (a, b)
    checks += 1

z = sp.symbols('z'); h, r = sp.symbols('h r', real=True)
a = 1-h; b = h*r
S = sp.Matrix([[a,-b],[-b,a]])
O = sp.Matrix([[a,0,-b],[-b,a,0],[0,1,0]])
B = sp.Matrix([[a,0,-b,0],[0,a,0,-b],[0,1,0,0],[1,0,0,0]])
eq(S.charpoly(z).as_expr(), (z-a)**2-b**2)
eq(O.charpoly(z).as_expr(), z*(z-a)**2-b**2)
eq(B.charpoly(z).as_expr(), (z*z-a*z+b)*(z*z-a*z-b))
eq((sp.Rational(9,8))**2*(1+sp.sqrt(1+8*r*r))**2,
   sp.Rational(81,64)*(1+sp.sqrt(1+8*r*r))**2)
# Universal gain 9/8: exact nonnegative polynomial gap.
eq(81*(1+8*r*r)-(7+16*r)**2, 8*(7*r-2)**2)
eq(sp.Rational(4,1)/(1+sp.sqrt(1+8*(sp.Rational(2,7))**2)), sp.Rational(7,4))
eq(2/(1+sp.Rational(2,7)), sp.Rational(14,9))
lim=O.subs({h:sp.Rational(7,4),r:sp.Rational(2,7)})
eq(lim.charpoly(z).as_expr(), (z-sp.Rational(1,4))*(z*z+sp.Rational(7,4)*z+1))

for rval in [sp.Rational(1,13),sp.Rational(1,4),sp.Rational(2,7),sp.Rational(2,5),sp.Rational(3,4),sp.Rational(99,100)]:
    rr = float(rval)
    ts=2/(1+rr)
    to=4/(1+math.sqrt(1+8*rr*rr))
    assert to>ts
    checks += 1
    for case,hh in [('below',ts*0.9),('inside',(ts+to)/2),('above',to*1.01)]:
        matrices=[np.array(v.subs({h:hh,r:rr}),dtype=float) for v in [S,O,B]]
        rad=[max(abs(np.linalg.eigvals(mat))) for mat in matrices]
        should=[[True,True,True],[False,True,False],[False,False,False]][['below','inside','above'].index(case)]
        for rad1,expect in zip(rad,should):
            assert (rad1<1)==expect,(rr,hh,rad,case)
            checks += 1

# Single and double-delayed companion updates equal the stated histories.
for rval in [0.2,0.5,0.8]:
 for hh in [0.5,1.0,1.5]:
  x0,x1,prev0,prev1 = 0.3,-0.4,0.7,-0.6
  aa=1-hh; bb=hh*rval
  lhs=np.array([aa*x0-bb*prev1,aa*x1-bb*x0,x1]);
  rhs=np.array(O.subs({h:hh,r:rval}),dtype=float)@np.array([x0,x1,prev1]);
  assert np.allclose(lhs,rhs)
  checks+=1
  lhs=np.array([aa*x0-bb*prev1,aa*x1-bb*prev0,x1,x0]);
  rhs=np.array(B.subs({h:hh,r:rval}),dtype=float)@np.array([x0,x1,prev1,prev0]);
  assert np.allclose(lhs,rhs)
  checks+=1

# At beta=1, exact spectral factors for all three schedules.
for rr in [.1,.2,.5,.7,.95]:
 for mat,expected in zip([S,O,B],[rr,rr**(2/3),rr**.5]):
  rad=max(abs(np.linalg.eigvals(np.array(mat.subs({h:1,r:rr}),dtype=float))))
  assert abs(rad-expected)<1.e-10,(rr,rad,expected)
  checks+=1

# Concrete rational witness at coupling 2/7, relaxation 5/3.
for mat,expected in zip([S,O,B],[False,True,False]):
 rr=max(abs(np.linalg.eigvals(np.array(mat.subs({h:sp.Rational(5,3),r:sp.Rational(2,7)}),dtype=float))))
 assert (rr<1)==expected
 checks+=1

print('PASS: %d symbolic and numerical comparisons' % checks)
