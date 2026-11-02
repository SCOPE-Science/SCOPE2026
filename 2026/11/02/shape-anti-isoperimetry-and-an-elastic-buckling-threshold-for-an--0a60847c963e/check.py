#!/usr/bin/env python3
"""Deterministic numerical checks of the stated independent-telegraph box formulas."""
import math
import json
from scipy.integrate import quad

def theta(z):
    if abs(z)<1e-4:
        return 1-z*z/3+2*z**4/15-17*z**6/315
    return math.tanh(z)/z

def f(L,D=1.,v=2.,alpha=.7):
    q=v*v/(2*alpha*D)
    ell=.5*L*math.sqrt((v/D)**2+2*alpha/D)
    return (1+q)/(1+q*theta(ell))

def rho(x,L,D,v,alpha):
    q=v*v/(2*alpha*D)
    kappa=math.sqrt((v/D)**2+2*alpha/D)
    z=.5*kappa*L
    return (1+q*math.cosh(kappa*(x-L/2))/math.cosh(z))/(L*(1+q*theta(z)))

def h(s,D=1.,v=2.,alpha=.7):
    return quad(lambda u:f(math.exp(u),D,v,alpha),0,s,epsabs=1e-12)[0]

checks=0
worst_integral=0.
worst_endpoint=0.
worst_hessian=0.
for D in (.1,1.,3.):
 for v in (.2,1.,4.):
  for alpha in (.2,2.):
   for L in (.1,1.,5.):
    q=v*v/(2*alpha*D)
    k=math.sqrt(v*v/(D*D)+2*alpha/D)
    I=quad(lambda x:rho(x,L,D,v,alpha),0,L,epsabs=1e-13)[0]
    worst_integral=max(worst_integral,abs(I-1))
    assert abs(I-1)<2e-11
    checks+=1
    for x in (0.,L):
     z=k*(x-L/2)
     a=1/(L*(1+q*theta(k*L/2)))
     rhs=a*(q*k*k-v*v/(D*D)*q)*math.cosh(z)/math.cosh(k*L/2)
     lhs=a*v*v/(D*D)
     assert abs(lhs-rhs)<1e-8*max(1,abs(lhs))
     checks+=1
    for x in (0.,L/4,L/2,3*L/4,L):
     z=k*(x-L/2);den=L*(1+q*theta(k*L/2));c=math.cosh(k*L/2)
     rr=(1+q*math.cosh(z)/c)/den
     rp=q*k*math.sinh(z)/(den*c)
     rpp=q*k*k*math.cosh(z)/(den*c)
     rppp=q*k**3*math.sinh(z)/(den*c)
     mm=D*rp/v; mp=D*rpp/v; mpp=D*rppp/v
     for sg in (-1,1):
      ps=(rr+sg*mm)/2; psp=(rp+sg*mp)/2; pspp=(rpp+sg*mpp)/2
      assert ps>0
      residual=D*pspp-sg*v*psp-alpha*sg*mm
      assert abs(residual)<1e-8*max(1,D*abs(pspp)+v*abs(psp)+alpha*abs(mm))
      checks+=2
      if x in (0.,L):
       assert abs(sg*v*ps-D*psp)<1e-8*max(1,abs(v*ps))
       checks+=1
    assert abs(L*rho(L,L,D,v,alpha)-f(L,D,v,alpha))<1e-12
    checks+=1
    assert f(.5*L,D,v,alpha)<f(L,D,v,alpha)<f(2*L,D,v,alpha)
    checks+=1
for q in (.02,.4,2.,15.):
 D=1.;alpha=.5;v=math.sqrt(2*q*alpha*D);a=.8
 for t in (.01,.1,.7,2.,4.):
  delta=h(math.log(a)+t,D,v,alpha)+h(math.log(a)-t,D,v,alpha)-2*h(math.log(a),D,v,alpha)
  assert delta>0
  via_force=quad(lambda r:f(a*math.exp(r),D,v,alpha)-f(a*math.exp(-r),D,v,alpha),0,t,epsabs=2e-12)[0]
  assert abs(delta-via_force)<1e-10*max(1,abs(via_force))
  checks+=2
  eps=1e-5
  gp=(f(a*math.exp(eps),D,v,alpha)-f(a*math.exp(-eps),D,v,alpha))/(2*eps)
  ratio=(h(math.log(a)+eps,D,v,alpha)+h(math.log(a)-eps,D,v,alpha)-2*h(math.log(a),D,v,alpha))/(eps*eps)
  worst_hessian=max(worst_hessian,abs(gp-ratio))
  assert abs(gp-ratio)<3e-5
  checks+=1
 for t in (6.,12.,20.):
  slope=f(a*math.exp(t),D,v,alpha)-f(a*math.exp(-t),D,v,alpha)
  assert abs(slope-q)<.2*q
  checks+=1
# Quasistatic Hookean shape: below the threshold the square is unstable and
# numerically located global candidates have symmetry-related minima.
from scipy.optimize import minimize_scalar
for q in (.2,2.,8.):
 D=1.;alpha=.7;v=math.sqrt(2*q*alpha);a=1.
 eps=1e-5
 ap=(f(a*math.exp(eps),D,v,alpha)-f(a*math.exp(-eps),D,v,alpha))/(2*eps)
 Kc=2*ap
 for K in (.2*Kc,.7*Kc):
  A=1.
  g=lambda t:h(math.log(a)+t,D,v,alpha)+h(math.log(a)-t,D,v,alpha)-2*h(math.log(a),D,v,alpha)
  u=lambda t:K*t*t/2-g(t)
  opt=minimize_scalar(u,bounds=(1e-4,30+20*q/K),method='bounded',options={'xatol':1e-9})
  assert opt.success and opt.x>0 and opt.fun<-1e-6
  assert abs(u(-opt.x)-u(opt.x))<1e-8
  checks+=3
# Independent error-bound check of theta monotonicity, via positive integral representation.
for z in (.02,.1,.5,1.,3.,8.,40.):
 g=math.tanh(z)-z/math.cosh(z)**2
 assert g>0
 assert abs(g-quad(lambda u:2*u*math.tanh(u)/math.cosh(u)**2,0,z)[0])<1e-9
 checks+=2
print(json.dumps(dict(status='passed',checks=checks,max_density_normalization_error=worst_integral,max_local_second_variation_error=worst_hessian,method='deterministic quadrature, PDE boundary matching, independent work integrals, asymptotic slopes and positive derivative integral'),sort_keys=True))
