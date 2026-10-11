#!/usr/bin/env python3
"""Symbolic algebraic checks for ES9 cylinder dynamics (SymPy required)."""
import sympy as sp
x,y,z,a,b=sp.symbols('x y z a b',real=True)
f=1-x*x-y*y
F=sp.Matrix([f*(y*y-a*x*y),f*x*z,f*(1-b*y*y)])
D=lambda h: sp.expand(sp.diff(h,x)*F[0]+sp.diff(h,y)*F[1]+sp.diff(h,z)*F[2])
B=1+1/a**2
phi=z+2*x/a**2
assert sp.simplify(D(phi)-f*(f+(x-y/a)**2+(B-b)*y**2))==0
assert sp.simplify(D(f)+2*f*x*y*(y-a*x+z))==0
phi0=z+b*x
assert sp.simplify(D(phi0).subs(a,0)-f)==0
for aa in [sp.Rational(1,2),sp.Integer(-2),sp.Integer(5)]:
 bb=1+aa**-2+sp.Rational(1,7)
 yp=1/sp.sqrt(bb)
 for s in (-1,1):
  pp={a:aa,b:bb,x:s*yp/aa,y:s*yp,z:0}
  assert all(sp.simplify(v.subs(pp))==0 for v in F)
  assert sp.simplify(f.subs(pp))>0
  assert sp.simplify(f.subs({x:s/(aa*sp.sqrt(1+aa**-2)), y:s/sp.sqrt(1+aa**-2)}))==0
print('PASS: Lyapunov identity, cylinder factor, a=0 identity, sharp interior equilibria and endpoint')
