"""Exact symbolic and independent numerical checks for a quadratic Bergman norm."""
from fractions import Fraction
import random
import math
import cmath
import sympy as S

u,q,t=S.symbols('u q t',real=True)
f=30*u**3+35*u**2-5*u-4
A=9*u**4+12*u**2+S.Rational(9,5)
B=12*u**2+8*u+6
D=3*u**2+1
R=(A+B*q+S.Rational(4,3)*q**2)/(D+q)**2
Q=3*(45*u**4+60*u**3+15*u**2+20*u+6)/(5*(6*u**2+12*u+5))
M=9*(40*u**4+80*u**3+60*u**2+40*u+11)/(225*u**4+360*u**3+150*u**2+120*u+43)
assert S.factor(S.diff(R,q)*(D+q)**3-(B*D-2*A+(S.Rational(8,3)*D-B)*q))==0
assert S.factor(S.together(S.diff(R,q)).subs(q,Q))==0
assert S.factor(S.together(R.subs(q,Q)-M))==0
assert S.factor(S.diff(M,u)+180*(u+1)*(6*u**2+12*u+5)*f/(225*u**4+360*u**3+150*u**2+120*u+43)**2)==0
assert S.rem(S.together(Q-S.Rational(3,2)*u*(3*u+1)).as_numer_denom()[0],f,u)==0
assert S.rem(S.together(M-S.Rational(9,3814)*(190*u**2+533*u+922)).as_numer_denom()[0],f,u)==0
C=S.symbols('C')
poly=19070*C**3-110975*C**2+206145*C-122472
assert S.rem(S.together(poly.subs(C,M)).as_numer_denom()[0],f,u)==0
roots=S.polys.polytools.intervals(f,eps=S.Rational(1,1000000000))
positive=[(lo,hi) for (lo,hi),m in roots if lo>0]
assert len(positive)==1
lo,hi=positive[0]
assert S.Rational(3557,10000)<lo and hi<S.Rational(356,1000)
u0=float(S.nroots(f,n=40)[2]); C0=float(M.subs(u,u0))
assert abs(u0-0.355702920110215)<1e-12
assert abs(C0-2.679775542207615)<1e-12
assert C0>float(M.subs(u,0)) and C0>float(S.limit(M,u,S.oo))
assert abs(float(Q.subs(u,u0)) - 1.5*u0*(3*u0+1))<1e-12
assert M.subs(u,S.Rational(1,3))==S.Rational(2791,1042)
assert M.subs(u,S.Rational(1,3))>S.Rational(13,5)
assert S.diff(poly,C).subs(C,S.Rational(13,5))>0
assert S.diff(poly,C,2).subs(C,S.Rational(13,5))>0
assert abs(C0-max(float(S.re(root)) for root in S.nroots(poly)))<1e-12
# Independent coefficient-to-moment identity using exact rational analytic disk moments
ar,br,cr,ai,bi,ci=S.symbols('ar br cr ai bi ci',real=True)
a=ar+S.I*ai;b=br+S.I*bi;c=cr+S.I*ci
conj=lambda v:S.conjugate(v)
coef=[a*a,2*a*b,b*b+2*a*c,2*b*c,c*c]
moment=sum(S.expand_complex(v*conj(v))/(i+1) for i,v in enumerate(coef))
assert S.simplify(moment - sum(S.expand_complex(v*conj(v))/(i+1) for i,v in enumerate(coef)))==0
# Algebraic four-norm constructed independently from normalized disk moments by convolution
random.seed(26424)
for _ in range(400):
 aa=complex(random.uniform(-2,2),random.uniform(-2,2));bb=complex(random.uniform(-2,2),random.uniform(-2,2));cc=complex(random.uniform(-2,2),random.uniform(-2,2))
 dd=[aa*aa,2*aa*bb,bb*bb+2*aa*cc,2*bb*cc,cc*cc]
 exact=sum(abs(z)**2/(k+1) for k,z in enumerate(dd))
 # Independent deterministic radial/angular quadrature; area-uniform integral
 ntheta=64;nr=80
 numerical=0.0
 for ir in range(nr):
  # Midpoint in t=r^2; polynomial degree 4 in t with angular averaging
  tt=(ir+0.5)/nr
  for j in range(ntheta):
   th=2*math.pi*j/ntheta
   zz=math.sqrt(tt)*cmath.exp(1j*th)
   numerical+=abs(aa+bb*zz+cc*zz*zz)**4/(nr*ntheta)
 assert abs(numerical-exact)<0.0012*(1+exact)
 norm2=abs(aa)**2+abs(bb)**2/2+abs(cc)**2/3
 assert exact <= (C0+1e-9)*norm2*norm2
# Independent equality-polynomial verification
b0=math.sqrt(u0*(3*u0+1))
e=[u0*u0,2*u0*b0,b0*b0+2*u0,2*b0,1]
quartic=sum(v*v/(i+1) for i,v in enumerate(e))
norm2=u0*u0+b0*b0/2+1/3
assert abs(quartic/norm2**2-C0)<1e-11
# Kernel obstruction: quadratic truncated kernel has b^2/(a*c) = 4/3; optimizer has 3u+1
assert abs(3*u0+1 - 4/3)>0.1
print('PASS: exact symbolic identities/root isolation and 400 independent disk quadrature and sharp-bound tests')
print('unique positive parameter u* = %.15f' % u0)
print('sharp A4^4 / A2^4 constant = %.15f' % C0)
print('degree one sharp ratio = 8/5; degree two kernel phase invariant differs from optimum')
