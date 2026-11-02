#!/usr/bin/env python3
"""Independent exact-algebra and finite-time tests of the stalled three-state rate engine.

Requires SymPy, NumPy and SciPy. No external data or services are needed.
The analytical all-time positivity lemma is proved in RESULT.md, not by this script.
"""
import math
import sympy as sy
import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad

r,b,d,w,u,v,s,x,y,z=sy.symbols('r b d w u v s x y z',positive=True)
a=r*b; c=r*d
Q=sy.Matrix([[-a-w,w,b],[w,-c-w,d],[a,c,-b-d]])
pi=sy.Matrix([1,1,r])/(r+2)
W=sy.Matrix([[0,w,0],[-w,0,0],[0,0,0]])
L=sy.Matrix([[0,0,0],[0,0,-v],[0,u,0]])
ones=sy.ones(1,3)
T=(1+r)*(b+d)+2*w
Z=(r+2)*(r*b*d+w*(b+d))
K=(1+r)*d+2*w-b
assert all(sy.simplify(a0)==0 for a0 in Q*pi)
assert sy.simplify((s*sy.eye(3)-Q).det()-s*(s*s+T*s+Z))==0
S0=sy.factor((ones*L*W*pi+ones*W*L*pi)[0])
S1=sy.factor((ones*L*Q*W*pi+ones*W*Q*L*pi)[0])
assert sy.simplify(S0+w*(u+r*v)/(r+2))==0
assert sy.simplify(S1+K*S0)==0
assert sy.simplify(T-K-(r+2)*b)==0
# Verify separately using a fully tilted two-field generator.
Qtilt=sy.Matrix([[-a-w,w*sy.exp(x),b],[w*sy.exp(-x),-c-w,d-v+v*sy.exp(-y)],[a,c-u+u*sy.exp(y),-b-d]])
p=(z*sy.eye(3)-Qtilt).det()
def dv(*xs): return sy.factor(sy.diff(p,*xs).subs({x:0,y:0,z:0}))
pz=dv(z);mx=sy.factor(-dv(x)/pz);my=sy.factor(-dv(y)/pz)
assert sy.simplify(mx)==0
assert sy.simplify(my-(u-r*v)/(r+2))==0
mixed=sy.factor(-(dv(x,y)+dv(x,z)*my+dv(y,z)*mx+dv(z,z)*mx*my)/pz)
variance=sy.factor(-(dv(x,x)+2*dv(x,z)*mx+dv(z,z)*mx**2)/pz)
assert sy.simplify(mixed+w*b*(u+r*v)/Z)==0
assert sy.simplify(variance-2*w*r*b*d/Z)==0
print('Symbolic generator, marked-jump, variance and inverse identities: PASS')

def check(r,b,d,w,u,v,t):
    assert 0<u<r*d and 0<v<d and t>0
    Q=np.array([[-r*b-w,w,b],[w,-r*d-w,d],[r*b,r*d,-b-d]])
    pi=np.array([1,1,r])/(r+2)
    W=np.array([[0,w,0],[-w,0,0],[0,0,0]])
    L=np.array([[0,0,0],[0,0,-v],[0,u,0]])
    T=(1+r)*(b+d)+2*w
    Z=(r+2)*(r*b*d+w*(b+d))
    K=(1+r)*d+2*w-b
    eig=np.linalg.eigvals(Q)
    lam=sorted([-float(z.real) for z in eig if abs(z)>1e-8])
    assert len(lam)==2
    lo,hi=lam
    if hi-lo<1e-8:
        f=lambda s: math.exp(-lo*s)*(1+(lo-K)*s)
    else:
        coef=(hi-K)/(hi-lo)
        f=lambda s: coef*math.exp(-lo*s)+(1-coef)*math.exp(-hi*s)
    pref=-w*(u+r*v)/(r+2)
    def S(s):
        mat=expm(Q*s)
        return np.ones(3)@L@mat@W@pi+np.ones(3)@W@mat@L@pi
    for at in [0,.1*t,.5*t,t]:
        assert abs(S(at)-pref*f(at))<1e-8*(1+abs(S(at)))
    H=quad(lambda s:(t-s)*f(s),0,t,epsabs=1e-11)[0]
    covariance=quad(lambda s:(t-s)*S(s),0,t,epsabs=1e-11)[0]
    assert H>0 and covariance<0
    assert abs(covariance-pref*H)<1e-8*(1+abs(covariance))
    plus=-(r+2)*covariance/(w*H)
    minus=(r+2)*((u-r*v)/(r+2))
    assert abs((plus+minus)/2-u)<1e-9
    assert abs((plus-minus)/(2*r)-v)<1e-9

cases=[(.5,4.,2.,1.4,.6,.6,4.),(.7,.3,5.,3.,1.,1.,1.5),(.4,10.,2.,3.,.5,1.,3.),(1.,2.,3.,5.,.5,.8,2.),(2.,.2,.9,.15,.8,.2,7.)]
rng=np.random.default_rng(20261028)
for _ in range(120):
    rr=10**rng.uniform(-1,.6);bb=10**rng.uniform(-1,1);dd=10**rng.uniform(-1,1);ww=10**rng.uniform(-1,1)
    cases.append((rr,bb,dd,ww,rr*dd*rng.uniform(.05,.90),dd*rng.uniform(.05,.90),10**rng.uniform(-1,.5)))
for case in cases:check(*case)
print('Independent finite-time matrix-exponential/quadrature comparisons: 125 PASS')
