"""Standalone scientific checks of the stated regular-polygon crossing equations.
Only scipy and numpy are required: python verify.py ."""
import math
import numpy as np
from scipy.special import lambertw
from scipy.integrate import solve_ivp

def edge_map(a,b,s):
    C=a/2+b; E=a/2-b
    if s==0: return 0.
    if abs(E)<1e-13: return s*math.exp(-a-C*s)
    z=E*s*math.exp(-a-C*s)
    w=lambertw(z,0)
    if abs(w.imag)>1e-9: raise ArithmeticError((a,b,s,z,w))
    return float(w.real/E)

def direct_flow(n,radius,lam,omega,mu,s):
    theta=2*math.pi/n
    p=np.array([radius,0.]); q=np.array([radius*math.cos(theta),radius*math.sin(theta)])
    d=q-p; L2=d@d; Delta=np.linalg.det(np.stack((p,q)))
    normal=np.array([d[1],-d[0]])
    a=lam*L2/omega; b=mu*Delta/omega; C=a/2+b; E=a/2-b
    if not (-1<s<1/C): raise ValueError('outside transverse forward domain')
    pred=edge_map(a,b,s)
    assert (s==0 and pred==0) or (s*pred>0 and abs(pred)<abs(s))
    time=(1+(C*s+E*pred)/a)/omega
    assert time>0
    initial=(1+s)*p
    def field(t,x):
        V=normal@(x-p)
        return (omega-mu*V)*d-lam*V*normal
    def event(t,x):
        xi=(x-p)@d/L2; V=normal@(x-p)
        return 1-xi+V/(2*Delta)
    event.terminal=True; event.direction=-1
    sol=solve_ivp(field,[0,1.5*time+1/omega],initial,events=event,rtol=4e-12,atol=2e-13,max_step=0.05/omega)
    assert len(sol.t_events[0])==1,(n,radius,lam,omega,mu,s,time,sol.message)
    x_end=sol.y_events[0][0]
    measured=x_end@q/radius**2-1
    err=max(abs(measured-pred),abs(sol.t_events[0][0]-time),np.linalg.norm(x_end-(1+pred)*q))
    return err

max_err=0.0;count=0
for n in [3,4,7,12]:
 for radius in [0.6,1.4]:
  for lam in [0.3,1.9,5.0]:
   for omega in [0.8,1.7]:
    for mu in [0.,0.3,2.]:
     theta=2*math.pi/n
     a=4*lam*radius**2*math.sin(theta/2)**2/omega
     b=mu*radius**2*math.sin(theta)/omega
     C=a/2+b
     for s in [-0.999,-0.5,-0.05,min(0.05,0.08/C),0.45/C,0.95/C]:
      err=direct_flow(n,radius,lam,omega,mu,s)
      assert err<5e-8,(n,radius,lam,omega,mu,s,err)
      max_err=max(max_err,err);count+=1
print('direct edge ODE versus Lambert W:',count,'cases; max abs error',max_err)

# Sharp three-way near-origin response at fixed a=3 and b>=0 (E=1.5,1,0.5,-0.5).
for b in [0.,0.5,1.,2.]:
 a=3.;C=a/2+b;E=a/2-b
 for u in [1.e-4,1.e-6,1.e-8]:
  v=1+edge_map(a,b,-1+u)
  if E<1:
   pred=(1+C)/(1-E)*u
  elif E==1:
   pred=math.sqrt(2*(1+C)*u)
  else:
   pred=1+lambertw(-E*math.exp(-E),0).real/E
  assert abs(v/pred-1)< (0.1 if u==1e-4 else 0.02),(b,u,v,pred)
print('all three near-center regimes verified for finite u')
for a in [0.5,1.,2.,4.,7.]:
 for b in [0.,0.5,2.]:
  C=a/2+b; E=a/2-b
  for s in [-0.95,-0.3,0.3/C,0.8/C]:
   f=edge_map(a,b,s)
   assert abs(math.log(abs(s/f))-a-C*s-E*f)<2.e-12
print('implicit identities and sharp positive-domain checks passed')
