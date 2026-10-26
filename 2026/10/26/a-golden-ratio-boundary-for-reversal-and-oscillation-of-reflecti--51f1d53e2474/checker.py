"""Reproducible algebraic and semigroup checks for reflecting partial resetting with rests."""
from math import sqrt,exp,cos,sin,log,pi
import sympy as s
import numpy as np
from scipy.linalg import expm

u,q=s.symbols('u q', positive=True)
A=s.Matrix([[-1,-u],[q,-q]])
h=q*(1+u)/(q+u*u)
d=(1-q)**2-4*q*u
assert s.simplify(A.charpoly().as_expr() - (s.Symbol('lambda')**2+(1+q)*s.Symbol('lambda')+q*(1+u)))==0
assert s.factor(h**2-(1+q)*h+q*(1+u)) == q*u*(u+1)**2*(q+u*u-u)/(q+u*u)**2
assert s.factor(s.diff(h,q)) != 0
q0=u*(1-u)
assert s.simplify(h.subs(q,q0)-(1-u*u))==0
assert s.simplify((1+q0)-(1-u*u)-u)==0
assert s.simplify(d.subs(q,q0) - (1-u-u*u)**2)==0
# dimensionless moment generator balance: p_A=q/(1+q), M_A=2D p_A/[r(1-u^2)], M_R=(u^2/q)M_A.
D,r=s.symbols('D r', positive=True)
p=q/(1+q)
MA=2*D*p/(r*(1-u*u));MR=u*u*MA/q
assert s.simplify(2*D*p-r*MA+r*q*MR)==0
assert s.simplify(r*u*u*MA-r*q*MR)==0
assert s.simplify((-r*(1+u)*MA)/(MA+MR) +r*h)==0

count=8
for uu in [.01,.1,.2,.4,.5,.618033988749895,.7,.9,.99]:
 qm=(sqrt(1+uu)-sqrt(uu))**2
 qp=1/qm
 for qq in [.001,.5*uu*(1-uu),uu*(1-uu),(.5*(uu*(1-uu)+qm)),qm, .5*(qm+qp), qp,qp+1,10]:
  if qq<=0:continue
  for Dd,rr in [(1.,1.),(2.,.3),(0.7,3.)]:
   BB=np.array([[-rr,-rr*uu],[qq*rr,-qq*rr]])
   P=qq/(1+qq);mA=2*Dd*P/(rr*(1-uu**2));mR=uu**2*mA/qq; c0=mA+mR
   assert np.allclose(BB@np.array([1.,1.]),[-rr*(1+uu),0.],atol=1e-12)
   for t in [.002,.17, .7,2,8]:
    observed=np.array([mA,mR])@expm(BB*t)@np.ones(2)/c0
    ht=qq*(1+uu)/(qq+uu*uu);de=(1-qq)**2-4*qq*uu
    kt=(1+qq)/2
    T=rr*t
    if de<-1e-10:
     w=sqrt(-de)/2
     predicted=exp(-kt*T)*(cos(w*T)+(kt-ht)*sin(w*T)/w)
    elif de>1e-10:
     w=sqrt(de)/2
     predicted=exp(-kt*T)*(cosh_approx:=np.cosh(w*T)+(kt-ht)*np.sinh(w*T)/w)
    else: predicted=exp(-kt*T)*(1+(kt-ht)*T)
    assert abs(observed-predicted)<2e-10,(uu,qq,t,observed,predicted)
    count+=1
  # low-rate one-cross strip only if below golden u_*
  uc=(sqrt(5)-1)/2
  if uu<uc-1e-7:
   qq=(uu*(1-uu)+qm)/2
   ht=qq*(1+uu)/(qq+uu*uu)
   de=(1-qq)**2-4*qq*uu
   fast=(1+qq+sqrt(de))/2
   assert ht>fast
   Afast=(ht-(1+qq-sqrt(de))/2)/sqrt(de)
   Aslow=1-Afast
   assert Afast>1 and Aslow<0
   tzero=log(Afast/(-Aslow))/sqrt(de)
   val=lambda T:Afast*exp(-fast*T)+Aslow*exp(-((1+qq-sqrt(de))/2)*T)
   assert val(tzero-.01)>0 and val(tzero+.01)<0
   count+=3
  if uu>uc+1e-7:
   qq=(uu*(1-uu)+qm)/2
   de=(1-qq)**2-4*qq*uu
   ht=qq*(1+uu)/(qq+uu*uu)
   slow=(1+qq-sqrt(de))/2
   assert ht<slow
   count+=1

print('PASS',count,'deterministic semigroup/algebra assertions')
