"""Reproduce exact two-state Euler-composition endpoint positivity law."""
import sympy as s
import random
x,y=s.symbols('x y', real=True)
E=s.Matrix([[1-x,x],[0,1]])
F=s.Matrix([[1,0],[y,1-y]])
M=s.simplify(E*F*E)
expected=s.Matrix([[(1-x)*(1-x+x*y),x*(2-x-y*(1-x))],[y*(1-x),1-y*(1-x)]])
assert s.simplify(M-expected)==s.zeros(2)
a,b,h=s.symbols('a b h',positive=True)
for aa,bb in [(1,1),(1,2),(1,4),(3,15),(4,1),(0.5,100)]:
 for k in range(1001):
  hh=(2/aa)*k/1000
  xx=aa*hh/2; yy=bb*hh
  P=E.subs({x:xx})*F.subs({y:yy})*E.subs({x:xx})
  rule=bb*hh*(1-aa*hh/2)<=1+1e-12
  direct=min(float(v) for v in P)>=-1e-10
  assert rule==direct,(aa,bb,hh,rule,direct)
print('VERIFY_OK: exact symbolic matrix and 6006 endpoint sign comparisons')
