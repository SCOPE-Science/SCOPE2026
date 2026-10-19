"""Exact identities and numerical consistency for smoothed Lozi prime-two classification."""
import sympy as s
from math import sqrt
from fractions import Fraction
from itertools import product

a,c,e,b=s.symbols('a c e b',positive=True)
e1=(a-c)/(a*a+c*c)
e2=a/(a*a-a*c+2*c*c)
ef=2*a/(a*a+3*c*c)
assert s.factor(e2-e1)==2*c*(a*a-a*c+c*c)/((a*a+c*c)*(a*a-a*c+2*c*c))
assert s.factor(ef-e2)==a*(a-c)**2/((a*a+3*c*c)*(a*a-a*c+2*c*c))
assert s.factor(s.diff(s.Symbol('u')**2*a*a-2*c*c*e*s.Symbol('u')+a*a*e*e-2*(a-c)*e,e,2))==2*a*a
# Derive branch-symmetry matching and exact secant-level thresholds
assert s.simplify((a-c+2*c*c/a)*e2)==1
assert s.simplify(((a*a+c*c)/(a-c))*e1)==1
assert s.simplify((a*a+3*c*c)*ef/(2*a))==1
# Two-cycle midpoint equation at central region, and exact universal square-root prefactor.
t=c*e/a
d2=2*e/a-e*e*(1+3*c*c/(a*a))
assert s.simplify(d2.subs(e,ef))==0
assert s.simplify(s.diff(d2,e).subs(e,ef))==-2/a
assert s.simplify((t*t-d2)*a*a/e**2)==a*a+4*c*c-2*a/e
# Stability and boundary: Q product of derivatives
W=(1+b)**2
c_b=1-b
esm=2*a*a*(a-c)/(a**4+W**2+2*c*c*W)
esc=2*a/(a*a+4*c*c+W)
for aa,bb in product([0.8,1.2,1.5,2.0,3.0,5.0],[0.1,0.3,0.6,0.9]):
 cc=1-bb
 if aa<=cc: continue
 e1v=float(e1.subs({a:aa,c:cc}));e2v=float(e2.subs({a:aa,c:cc}));efv=float(ef.subs({a:aa,c:cc}))
 assert 0<e1v<e2v<efv
 def S(x,eps):return abs(x) if abs(x)>=eps else (x*x+eps*eps)/(2*eps)
 def coord(eps):
  if eps<=e1v:
   return (cc-aa)/(aa*aa+cc*cc),(cc+aa)/(aa*aa+cc*cc)
  if eps<e2v:
   q=sqrt(eps*(2*aa*aa*(aa-cc)-(aa**4-cc**4)*eps))
   u=(cc*cc*eps-q)/(aa*aa);return u,(1-cc*u)/aa
  t=cc*eps/aa
  d=sqrt(2*eps/aa-eps*eps*(1+3*cc*cc/(aa*aa)))
  return t-d,t+d
 for factor in [0.1,0.5,0.99,1,1.01,1.15]:
  for threshold in [e1v,e2v,efv]:
   eps=threshold*factor
   if eps>=efv:continue
   u,v=coord(eps)
   assert u<v
   assert abs(cc*v-1+aa*S(u,eps))<1e-9
   assert abs(cc*u-1+aa*S(v,eps))<1e-9
   m_u=aa*(u/eps if abs(u)<eps else (-1 if u<0 else 1))
   m_v=aa*(v/eps if abs(v)<eps else (-1 if v<0 else 1))
   tr=2*bb+m_u*m_v
   assert tr<1+bb*bb+1e-10
 if aa>1+bb:
  crit = float((esm if aa*aa-2*aa*cc <= (1+bb)**2 else esc).subs({a:aa,c:cc,b:bb}))
  assert e1v<crit<efv
  u,v=coord(crit)
  mu=aa*(u/crit if abs(u)<crit else -1)
  mv=aa*(v/crit if abs(v)<crit else 1)
  assert abs(mu*mv+(1+bb)**2)<2e-8
print('VERIFY_OK')
