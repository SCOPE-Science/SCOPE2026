"""Independent algebraic and numerical checks of the local two-cycle threshold.
Run: python verify_curvature.py   (requires sympy and mpmath)
Finite checks are not a substitute for the analytic existence proof.
"""
import sympy as sp
import mpmath as mp
b=sp.symbols('b', nonzero=True)
r0sq=(b+1)/2
m0=b+sp.Rational(1,2)
a0=b**2+sp.Rational(5,2)*b+sp.Rational(5,4)
assert sp.simplify(a0-(m0+m0**2+r0sq))==0
assert sp.simplify(m0**2-b*m0-r0sq+sp.Rational(1,4))==0
r2=1/b+r0sq/b**2+2*r0sq*(3*b+1)**2/b**2
A2=sp.factor((1+2*m0)/b+r0sq/b**2+1+r2)
assert sp.simplify(A2-(b+1)*(3*b+1)*(3*b+2)/b**2)==0
curvature=sp.factor(A2*b**2/(b-1)**2)
assert sp.simplify(curvature-(b+1)*(3*b+1)*(3*b+2)/(b-1)**2)==0
assert sp.solve(sp.together(sp.factor(curvature)),b)==[-1,-sp.Rational(2,3),-sp.Rational(1,3)]


# Exact symbolic equivalence of the four orbit equations and reduced identities.
m,p,q,r,d,a=sp.symbols('m p q r d a', real=True)
u0,v0=m+p,q+r
u1,v1=m-p,q-r
E0=u1-a+u0**2+v0**2
E1=v1-d-2*(b-u0)*v0
E2=u0-a+u1**2+v1**2
E3=v0-d-2*(b-u1)*v1
assert sp.expand(E0+E2+2*(a-m-m**2-p**2-q**2-r**2))==0
assert sp.expand(E0-E2+2*((1-2*m)*p-2*q*r))==0
assert sp.expand(E1+E3-2*((1-2*(b-m))*q+2*p*r-d))==0
assert sp.expand(E1-E3+2*((1+2*(b-m))*r-2*p*q))==0
Jplus=sp.Matrix([[-2*m0,-2*sp.sqrt(r0sq)],[-2*sp.sqrt(r0sq),-1]])
Jminus=sp.Matrix([[-2*m0,2*sp.sqrt(r0sq)],[2*sp.sqrt(r0sq),-1]])
assert sp.simplify(sp.trace(Jminus*Jplus)-(4*b**2-2))==0
assert sp.simplify((Jminus*Jplus).det()-1)==0

mp.mp.dps=70
for B in ['-0.8','-0.5','-0.2']:
 B=mp.mpf(B)
 m=B+mp.mpf('0.5');r=mp.sqrt((B+1)/2)
 aBase=B*B+mp.mpf('2.5')*B+mp.mpf('1.25')
 c=(B+1)*(3*B+1)*(3*B+2)/(B-1)**2
 for ds in ['0.01','0.001']:
  d=mp.mpf(ds)
  def equation(u0,v0,u1,v1,a):
   K0=u0*u0-B*u0-v0*v0
   K1=u1*u1-B*u1-v1*v1
   return (u1-a+u0*u0+v0*v0,
           v1-d-2*(B-u0)*v0,
           u0-a+u1*u1+v1*v1,
           v0-d-2*(B-u1)*v1,
           16*K0*K1-1)
  z=mp.findroot(equation,(m,r,m,-r,aBase),tol=mp.mpf('1e-60'))
  assert max(abs(v) for v in equation(*z))<mp.mpf('1e-55')
  Cnum=(z[4]-aBase)/d**2
  assert abs(Cnum-c)<mp.mpf('0.0001')
  print('b',mp.nstr(B,4),'delta',ds,'measured',mp.nstr(Cnum,16),'formula',mp.nstr(c,16))
print('VERIFY_OK')
