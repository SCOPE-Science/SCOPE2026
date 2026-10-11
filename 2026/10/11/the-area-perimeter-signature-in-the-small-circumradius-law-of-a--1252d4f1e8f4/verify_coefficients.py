#!/usr/bin/env python3
"""Exact symbolic checks for the circumradius small-ball coefficient theorem.

These verify algebraic identities only; the geometric uniform remainder is proved
in the accompanying mathematical text, not by this program.
"""
import sympy as s

z=s.symbols('z', real=True)
J=(s.sin(z)+(s.pi-z)*s.cos(z))/2
I0=s.integrate(s.sin(z)*J, (z,0,s.pi))
I1=s.integrate(s.sin(z)**2*J, (z,0,s.pi))
assert s.simplify(I0-3*s.pi/8)==0, I0
assert s.simplify(I1-s.Rational(8,9))==0, I1
Ea=s.simplify(4*I0/s.pi**2)
Eap=s.simplify(24*I1/s.pi**2)
assert s.simplify(Ea-s.Rational(3,2)/s.pi)==0
assert s.simplify(Eap-s.Rational(64,3)/s.pi**2)==0

# The angle-integrated Jacobian coefficient and first erosion moment.
c0=s.simplify(2*(2*s.pi)**3*Ea)
c1=s.simplify(2*(2*s.pi)**3*Eap/(2*s.pi))
assert s.simplify(c0-24*s.pi**2)==0
assert s.simplify(c1-s.Rational(512,3))==0
A,P=s.symbols('A P',positive=True)
lead=s.simplify(c0/(4*A**2))
nextcoef=s.simplify(-c1*P/(5*A**3))
assert s.simplify(lead-6*s.pi**2/A**2)==0
assert s.simplify(nextcoef+512*P/(15*A**3))==0
assert s.simplify(lead.subs(A,s.pi)-6)==0
assert s.simplify(nextcoef.subs({A:s.pi,P:2*s.pi})+1024/(15*s.pi**2))==0

# Independent pointwise 6x6 Jacobian test at 3 distinct non-collinear angles.
cx,cy,r,th1,th2,th3=s.symbols('cx cy r th1 th2 th3', real=True)
angles=[th1,th2,th3]
coordinates=[]
for th in angles:
    coordinates += [cx+r*s.cos(th),cy+r*s.sin(th)]
Jmat=s.Matrix(coordinates).jacobian([cx,cy,r,th1,th2,th3])
subs={r:s.Rational(3,4),th1:0,th2:s.pi/2,th3:s.pi}
absdet=s.Abs(s.simplify(Jmat.subs(subs).det()))
u1=s.Matrix([s.cos(th1),s.sin(th1)]).subs(subs)
u2=s.Matrix([s.cos(th2),s.sin(th2)]).subs(subs)
u3=s.Matrix([s.cos(th3),s.sin(th3)]).subs(subs)
d=s.Matrix.hstack(u2-u1,u3-u1).det()
assert s.simplify(absdet-s.Abs(d)*subs[r]**3)==0,(absdet,d)
print('CIRCUMRADIUS_SMALL_T_AREA_PERIMETER_EXACT_OK')
