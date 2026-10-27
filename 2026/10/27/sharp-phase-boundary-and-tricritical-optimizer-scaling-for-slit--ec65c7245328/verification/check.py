#!/usr/bin/env python3
"""Standalone algebraic and numerical spot checks for the slit diffusion threshold.
Only finite algebraic identities are proved by this program; asymptotic arguments
and global optimization are established in RESULT.md.
"""
from fractions import Fraction
from math import sqrt, isclose
import sympy as s

t,r,a,eta,b,z=s.symbols('t r a eta b z', positive=True)
L=eta*r+2
K=a*eta*r+2*a+2
P=L*t**2+r*K*t+2*a*r**2
h=t*(t+r)/P
D=t*r*(t+r+eta*b*t*(t+a*r))/((t+r)*(t+a*r)*(eta*t+2))
N=t*(t+r)-b*P
delta=(1-a)*eta*r-2*a
assert s.cancel(D/r-b-N/((t+r)*(t+a*r)*(eta*t+2))) == 0
assert s.simplify(s.diff(h,t)-r*(-delta*t**2+4*a*r*t+2*a*r**2)/P**2)==0
Az=1-b*L
Bz=r*(1-b*K)
Cz=-2*a*b*r**2
Dz=(1+r*z)*(1+a*r*z)*(eta+2*z)
assert s.cancel((D/r-b).subs(t,1/z)-(Az*z+Bz*z**2+Cz*z**3)/Dz)==0
assert s.factor(Bz.subs(b,1/L)-r*delta/L)==0

# Three exact rational parameter regimes, with a symbolic radical threshold in the jump case.
for av,rv,etav in [(s.Rational(1),1,2),(s.Rational(1,2),1,2),(s.Rational(1,2),10,2)]:
    dv=s.simplify(delta.subs({a:av,r:rv,eta:etav}))
    lv=s.simplify(L.subs({a:av,r:rv,eta:etav}))
    b0=1/lv
    if dv>0:
        tc=s.simplify(rv*(2*av+s.sqrt(2*av*(1-av)*etav*rv))/dv)
        bc=s.simplify(h.subs({t:tc,a:av,r:rv,eta:etav}))
        assert s.simplify(s.diff(h,t).subs({t:tc,a:av,r:rv,eta:etav}))==0
        assert s.simplify(D.subs({t:tc,a:av,r:rv,eta:etav,b:bc})-rv*bc)==0
        assert float(bc)>float(b0)
        print('jump', 'tc=',s.N(tc,14),'bc=',s.N(bc,14),'vc=',s.N(s.sqrt(bc),14))
    elif dv==0:
        c=rv*s.sqrt(6*av)/lv
        assert float(c)>0
        print('tricritical', 'coefficient of (b0-b)^(-1/2):',s.N(c,14))
    else:
        c=-2*rv*dv/lv**2
        assert float(c)>0
        print('continuous', 'coefficient of (b0-b)^(-1):',s.N(c,14))
print('All exact algebraic assertions passed.')
