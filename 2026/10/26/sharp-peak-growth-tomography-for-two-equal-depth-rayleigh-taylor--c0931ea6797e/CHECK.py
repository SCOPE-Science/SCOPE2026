import numpy as np
from scipy.optimize import minimize_scalar,brentq

def theta(x):
    return 2*x/np.sinh(2*x) if x<350 else 0.
def eta(x):
    return 2*np.tanh(x)/(3+theta(x))
def direct(A,B,H):
    kc=np.sqrt(A/B)
    f=lambda k: (A*k-B*k**3)*np.tanh(k*H)
    sol=minimize_scalar(lambda k:-f(k),bounds=(0,kc),method='bounded',options={'xatol':1e-13})
    return sol.x,np.sqrt(f(sol.x))

def inverse(A,k,gamma):
    y=gamma**2/(A*k)
    if not (0<y<2/3): raise ValueError('outside realization')
    x=brentq(lambda z:eta(z)-y,1e-14,1000)
    b=(1+theta(x))/(3+theta(x))
    return x/k,A*b/k**2

c=0; maxerr=0
for rho_hi in (2,4,15):
 for rho_lo in (1,1.5):
  if rho_hi<=rho_lo: continue
  A=(rho_hi-rho_lo)*9.81/(rho_hi+rho_lo)
  for H in (0.04,.2,1,5,30):
   for B in (.01,.15,2,6):
    k,gamma=direct(A,B,H)
    if k*H>5: continue
    Hr,Br=inverse(A,k,gamma)
    err=max(abs(Hr/H-1),abs(Br/B-1))
    if k*H>5: continue
    maxerr=max(maxerr,err)
    assert err<5e-6,(A,B,H,k,gamma,Hr,Br,err)
    c+=1
for A in (.01,1,20):
 for k in (.02,1,20):
  for y in (1e-6,0.01,.15,.3,.5,.6,.666):
   H,B=inverse(A,k,np.sqrt(A*k*y))
   kr,gr=direct(A,B,H)
   assert abs(kr/k-1)<8e-6 and abs(gr**2/(A*k)-y)<2e-8, (A,k,y,H,B,kr,gr)
print('OK direct inverse tests',c,'max_rel_error',maxerr,'and 63 constructed peak checks')
print('eta vals',[(x,eta(x), (1+theta(x))/(3+theta(x))) for x in (.001,.1,1,4,30)])
