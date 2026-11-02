"""Exact identities and independent finite tests for a two-mode partially explicit wave integrator.
Run: python verify.py (requires SymPy >=1.10)."""
from fractions import Fraction
from math import sqrt
import random
import sympy as sp
A,B,C,t,w,x=sp.symbols('A B C t w x',real=True)
a,b,c=t*A,t*B,t*C
p=1+a/2
eta=1-w
W=sp.Matrix([[p,0],[eta*c/2,1]])
K=sp.Matrix([[A,C],[C,B]])
P=sp.expand((t*K-x*W).det())
S=sp.expand(a+p*b-eta*c**2/2)
R=sp.expand(a*b-c**2)
assert sp.simplify(P-(p*x*x-S*x+R))==0
assert sp.simplify(P.subs(x,4) - ((4+a)*(4-b)+(1-2*w)*c*c))==0
D=sp.expand(S*S-4*p*R)
assert sp.simplify(D-((a-p*b+eta*c*c/2)**2+(4+2*a*w)*c*c))==0
assert sp.simplify(P.subs(x,0)-t*t*(A*B-C*C))==0
# Independently reconstruct the three-level transfer polynomial from equations.
U=sp.Matrix([[p,0],[eta*c/2,1]])
V=2*W-t*K
assert sp.simplify((t*K-(2-sp.Symbol('z')-1/sp.Symbol('z'))*W).det() - (U*sp.Symbol('z') + (t*K-2*W) + U/sp.Symbol('z')).det())==0
# Three exact thresholds at A=B=1,C=3/5
A0=B0=sp.S.One;C0=sp.Rational(3,5)
q=lambda ww:sp.simplify(8/(sp.sqrt((A0+B0)**2+4*(2*ww-1)*C0**2)-(A0-B0)))
assert q(0)==5 and q(sp.Rational(1,2))==4 and q(1)==20/sp.sqrt(34)
# The sharp boundary is a double -1 temporal multiplier.
for ww in [sp.S.Zero,sp.Rational(1,2),sp.S.One]:
 tt=q(ww)
 # evaluation of det(4W-tK) is zero
 assert sp.simplify(P.subs({A:A0,B:B0,C:C0,w:ww,t:tt,x:4}))==0
# Random rational positive-definite matrices; verify iff condition by actual 4x4 transfer eigenvalues.
rng=random.Random(812237)
N=220
for k in range(N):
 aa=Fraction(rng.randrange(1,16),rng.randrange(1,8))
 bb=Fraction(rng.randrange(1,16),rng.randrange(1,8))
 cc=Fraction(rng.randrange(-8,9),10)*Fraction.from_float(sqrt(float(aa*bb))).limit_denominator(10**7)
 # choose truly SPD (ensure room)
 if cc*cc>=aa*bb: cc=Fraction(0)
 ww=Fraction(rng.randrange(0,11),10)
 tc=float(8/(sp.sqrt((float(aa)+float(bb))**2 + 4*(2*float(ww)-1)*float(cc)**2)-(float(aa)-float(bb))))
 for mult in [0.31,0.77,1.13,1.6]:
  tt=tc*mult
  af=tt*float(aa);bf=tt*float(bb);cf=tt*float(cc);pf=1+af/2
  ss=af+pf*bf-(1-float(ww))*cf*cf/2
  rr=af*bf-cf*cf
  dis=ss*ss-4*pf*rr
  assert dis>=-1e-8
  xxplus=(ss+sqrt(max(0,dis)))/(2*pf)
  xxminus=(ss-sqrt(max(0,dis)))/(2*pf)
  assert xxminus>0 and xxminus<2+1e-9
  assert (0<xxplus<4)==(mult<1)
print('VERIFY_OK: 5 symbolic identities, 3 exact boundary values,',N*4,'independent modal grids')
