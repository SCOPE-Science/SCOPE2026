"""Reproducible computational cross-checks for radial Itô diffusion with resetting.

The infinite-domain claims are proved analytically in the accompanying manuscript.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import kv, gamma

COUNT = 0

def check(condition, message):
    global COUNT
    assert bool(condition), message
    COUNT += 1

def density(r, d, a, rho):
    m=(a+2.)/2.
    nu=(d-2.)/(a+2.)
    omega=2*math.pi**(d/2.)/gamma(d/2.)
    beta=1+nu
    C=2*rho**(1+nu/2)/(omega*gamma(beta)*(a+2)**beta)
    return C*r**(a-(d-2)/2)*kv(nu, math.sqrt(rho)*r**m/m)

def heat_density(r,t,d,a):
    w=2*math.pi**(d/2)/gamma(d/2)
    be=(d+a)/(a+2)
    return (a+2)/(w*gamma(be)) * ((a+2)**2*t)**(-be)*r**a*math.exp(-r**(a+2)/((a+2)**2*t))

for d in (2,3,4,6):
  for a in (0, 0.4, max(0.,d-2), d-2+0.7):
    rho=1.3
    w=2*math.pi**(d/2)/gamma(d/2)
    integral=quad(lambda r: w*r**(d-1)*density(r,d,a,rho),0,np.inf,epsabs=2e-9,limit=500)[0]
    check(abs(integral-1)<2e-7, ('norm',d,a,integral))
    for r in (0.15,0.7,2.0):
      lap=quad(lambda u: rho*math.exp(-rho*math.exp(u))*heat_density(r,math.exp(u),d,a)*math.exp(u),-35,8,epsabs=1e-10,limit=400)[0]
      check(abs(lap-density(r,d,a,rho))<2e-7,('laplace',d,a,r,lap,density(r,d,a,rho)))
    grid=np.geomspace(1e-4,4,301)
    vals=np.array([density(r,d,a,rho) for r in grid])
    dif=np.diff(vals)
    if a<=d-2:
      check(np.all(dif<1e-12),('decreasing',d,a))
    else:
      signs=np.sign(dif)
      changes=np.where(np.diff(signs)!=0)[0]
      check(len(changes)==1 and signs[0]>0 and signs[-1]<0,('one mode',d,a,changes))
      crit=(a*(a+2-d)/rho)**(1/(a+2))
      imax=np.argmax(vals)
      check(grid[imax]<crit,('mode upper bound',d,a,grid[imax],crit))
    if d>=3:
      small=1e-7
      asym=rho/((d-2)*w)*small**(a+2-d)
      check(abs(density(small,d,a,rho)/asym-1)<0.002,('small r',d,a))
    elif a>0:
      small=1e-7
      asym=rho/(2*math.pi)*small**a*math.log(1/small)
      check(abs(density(small,d,a,rho)/asym-1)<.15,('planar small r',d,a))
print('PASS:',COUNT,'deterministic numerical checks')
