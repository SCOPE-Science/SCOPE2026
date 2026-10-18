#!/usr/bin/env python3
"""Exact checks for nonlinear period softening in homogeneous Gray--Scott kinetics.

Requires SymPy. All verifications use exact rational/symbolic arithmetic,
except the reported decimal approximation of the unique minimizer.
"""
import sympy as S

I = S.I
F, k, v, u, t, w, z, zb = S.symbols('F k v u t w z zb', positive=True)
# At the Hopf point, t=F/k in (0,1).
Kh = t**2/(1+t)**4
Fh = t*Kh
vh = t/(1+t)**2
uh = t/(1+t)
fx = F*(1-u) -u*v**2
fy = u*v**2 -(F+k)*v
param = {F:Fh,k:Kh,u:uh,v:vh}
assert S.factor(fx.subs(param)) == 0
assert S.factor(fy.subs(param)) == 0
J = S.Matrix([fx,fy]).jacobian([u,v])
Jh = J.subs(param).applyfunc(S.factor)
assert S.factor(S.trace(Jh)) == 0
assert S.factor(Jh.det() - Kh**2*(1-t*t)) == 0
assert S.factor((Fh+Kh)*vh**2-Fh*vh+Fh*(Fh+Kh)) == 0

# Real coordinates x=v-vh, y=(F*x+k*((u-uh)+(v-vh)))/omega.
# In these coordinates, dot x=omega*y+N and dot y=-omega*x+(F/omega)*N.
A,B,C,D,eta,omega = S.symbols('A B C D eta omega', real=True, nonzero=True)
x=(z+zb)/2
y=(z-zb)/(2*I)
P2=S.expand((1+I*eta)*(A*x**2+B*x*y))
P3=S.expand((1+I*eta)*(C*x**3+D*x**2*y))
lam=-I*omega
H2=S.Integer(0)
for j in range(3):
    ell=2-j
    p=S.expand(P2).coeff(z,j).coeff(zb,ell)
    H2+=p/((j-1)*lam+ell*S.conjugate(lam))*z**j*zb**ell
H2=S.expand(H2)
H2bar=S.conjugate(H2).xreplace({S.conjugate(z):zb,S.conjugate(zb):z})
G=S.factor(S.expand(P3+S.diff(P2,z)*H2+S.diff(P2,zb)*H2bar).coeff(z,2).coeff(zb,1))

# Physical parameters: v_h=sqrt(k), omega^2=k^2-F^2.
s=S.symbols('s',positive=True)
physical={A:-(F+k)/s, B:2*omega/s, C:-(F+k)/k,
          D:omega/k, eta:F/omega}
G_real=S.factor(S.re(G).subs(physical).subs(s**2,k))
G_imag=S.factor(S.im(G).subs(physical).subs(s**2,k))
expected_real=(3*F-k)/(8*(k-F))
expected_imag=(9*F**2+6*F*k+5*k**2)/(24*omega*(k-F))
for actual,expected in [(G_real,expected_real),(G_imag,expected_imag)]:
    numer=S.together(actual-expected).as_numer_denom()[0]
    remainder=S.rem(S.Poly(numer,omega),S.Poly(omega**2-k**2+F**2,omega))
    assert remainder.as_expr().expand()==0, ('normal form',remainder)

# The real cubic coefficient vanishes exactly at the known Bautin ratio t=1/3.
assert S.factor(expected_real.subs(F,t*k)-(3*t-1)/(8*(1-t)))==0

# Frequency correction of a cycle relative to nearby linearized focus frequency.
# Since z=w+quadratic harmonics+..., the first harmonic of v has amplitude |w|+O(|w|^3).
Cfun=(9*t**2+6*t+5)*(1+t)**3/(24*t**2*(1-t)**2)
CfromG=(expected_imag/omega).subs(F,t*k).subs(omega**2,k*k*(1-t*t)).subs(k,Kh)
assert S.factor(CfromG-Cfun)==0
P=9*t**4-45*t**3-35*t**2-19*t+10
assert S.factor(S.diff(Cfun,t)- (t+1)**2*P/(24*t**3*(t-1)**3))==0
assert P.subs(t,0)>0 and P.subs(t,1)<0
# P'<0 throughout 0<t<1, since 36*t^3<=36*t^2 and all other terms negative.
assert S.factor(S.diff(P,t))==36*t**3-135*t**2-70*t-19
assert S.factor(Cfun.subs(t,S.Rational(1,3)))==16
r=S.nsolve(P,S.Rational(3,10),prec=40)
print('Hopf parameterization and equilibrium: PASS')
print('Quadratic homological equation and cubic normal form: PASS')
print('Radial cubic coefficient = (3F-k)/(8(k-F)): PASS')
print('Angular cubic coefficient = (9F^2+6Fk+5k^2)/(24omega(k-F)): PASS')
print('Unique strict global slope minimum: PASS')
print('t* =',r)
print('C(t*) =',S.N(Cfun.subs(t,r),30))
print('C(1/3) = 16: PASS')
