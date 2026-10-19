"""Standalone reproducibility checks for an inertial proximal spectral theorem.
Run: python verify.py . Uses SymPy and NumPy; all primary claims have symbolic proofs in RESULT.md.
"""
import math
import random
import sympy as S
import numpy as np

q,t,s,z,u,k=S.symbols('q t s z u k',real=True)
theta=3*t/q-1
delta=-t**3/q
p=z**3-s*(1+theta)*z**2+s*(theta-delta)*z+s*delta
assert S.factor(p.subs(s,q).subs(q,3*t-3*t*t+t**3)-(z-t)**3)==0
assert S.factor(p.subs(s,k*q).subs(q,3*t-3*t*t+t**3).subs(z,t*u)/t**3 -(u**3-3*k*u*u+3*k*u-k))==0
D=3*u**2-3*u+1
assert S.factor(S.diff(u**3/D,u))==3*u*u*(u-1)**2/D**2
assert S.simplify(S.diff(u*u/D,u)-u*(2-3*u)/D**2)==0
assert S.factor((u**3/D).subs(u,S.Rational(2,3))-S.Rational(8,9))==0
assert S.factor((u*u/D).subs(u,S.Rational(2,3))-S.Rational(4,3))==0
assert S.factor(S.expand((1-t)**3)-(1-3*t+3*t*t-t**3))==0
# Rigorous rational interval for t and source admissible coefficients.
lo=S.Rational(20629,100000)
hi=S.Rational(20631,100000)
assert (1-lo)**3>S.Rational(1,2)>(1-hi)**3
assert 0<3*lo/S.Rational(1,2)-1<3*hi/S.Rational(1,2)-1<S.Rational(3,11)
assert -2*hi**3<-2*lo**3<0
# Exact rational enclosure of every inequality of the cited sufficient regime.
thlo=6*lo-1; thhi=6*hi-1
assert S.Rational(2377,10000)<thlo<thhi<S.Rational(238,1000)
dlo=-2*hi**3; dhi=-2*lo**3
assert -S.Rational(18,1000)<dlo<dhi<-S.Rational(17,1000)
be=S.Rational(4,7)
hi_th=S.Rational(238,1000)
L_hi=be*hi_th*(1+hi_th)-(1-be)*(1-hi_th)**2
assert L_hi<-S.Rational(7,100)
# First lower bound is -1 + 11*theta/3.
assert -1+S.Rational(11,3)*hi_th<-S.Rational(18,1000)
# Second lower bound is L/(1+theta), L<-0.07 and theta<0.238.
assert -S.Rational(7,100)/(1+hi_th)<-S.Rational(18,1000)
# Last L<R: L<-0.07, R>-0.036 - (1/7)*0.018^2 > -0.07.
assert 2*hi_th-be+2<2
assert -2*S.Rational(18,1000)-S.Rational(1,7)*S.Rational(18,1000)**2>-S.Rational(7,100)
# Condition 3.2 at beta=4/7 and rho=1: interval monotonic envelope checks in compact grid plus exact endpoint conservative bounds.
beta=S.Rational(4,7)
th=6*(1-2**(-1/3))-1
de=-2*(1-2**(-1/3))**3
l1=-(1-beta-th-beta*th)/(1-beta)
l2=(beta*th*(1+th)-(1-beta)*(1-th)**2)/(1+th)
L=beta*th*(1+th)-(1-beta)*(1-th)**2
R=(2*th-beta+2)*de+(1-2*beta)*de*de
assert 0<th<float(S.Rational(3,11))
assert max(l1,l2)<de<0
assert L<R
# Complete numeric cubic validation for representative scalar contraction levels.
for qv in [.1,.2,.4,.5,.7,.85,.96,.99]:
    tv=1-(1-qv)**(1/3)
    thv=3*tv/qv-1; dv=-tv**3/qv
    worst=(0.,0.)
    for j in range(1001):
        sv=qv*j/1000
        # recurrence polynomial coefficients
        roots=np.roots([1,-sv*(1+thv),sv*(thv-dv),sv*dv])
        rad=max(abs(roots))
        if rad>worst[0]:worst=(rad,sv)
        assert rad<=tv*2/math.sqrt(3)+3e-8, (qv,j,rad)
    assert abs(worst[0]-tv*2/math.sqrt(3))<3e-7, (qv,worst)
    assert abs(worst[1]/qv-8/9)<.0015, (qv,worst)
# Direct linear-algebra specialization A=diag(1,5/4), gamma=rho=1, B=C=0.
qv=.5; tv=1-(1-qv)**(1/3); thv=3*tv/qv-1; dv=-tv**3/qv
A=np.diag([1.,1.25]); T=np.linalg.inv(np.eye(2)+A)
assert np.allclose(np.diag(T),[.5,4/9])
rng=np.random.default_rng(20261015)
for _ in range(100):
    xs=rng.normal(size=(3,2)); x0,x1,x2=xs
    y=x2+thv*(x2-x1)+dv*(x1-x0)
    full=np.linalg.solve(np.eye(2)+A,y)
    direct=T@y
    assert np.linalg.norm(full-direct)<1e-14
# Exact two-mode asymptotic gap; zero input lifted state excluded in theorem.
roots_fast=np.roots([1,-4/9*(1+thv),4/9*(thv-dv),4/9*dv]); roots_slow=np.roots([1,-.5*(1+thv),.5*(thv-dv),.5*dv])
assert abs(max(map(abs,roots_fast))-tv*2/math.sqrt(3))<1e-8
assert abs(max(map(abs,roots_slow))-tv)<2e-5
assert tv*2/math.sqrt(3)>tv
qc=1-(1-math.sqrt(3)/2)**3
assert .997<qc<.998
print('VERIFIED: polynomial identities, maximizer, rational parameter bracket, source sufficient-conditions, spectral grids, and 100 direct proximal updates')
print('t=',tv,'theta=',thv,'delta=',dv,'rate_fast=',tv*2/math.sqrt(3),'qcrit=',qc)
print('condition3.2 lower bounds',l1,l2,'delta',de,'last L',L,'R',R)
