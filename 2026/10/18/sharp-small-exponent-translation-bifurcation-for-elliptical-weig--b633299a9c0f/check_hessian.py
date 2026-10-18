"""Independent numerical checks of the explicit mathematical Hessian integrals.
Run: python check_hessian.py (requires numpy and scipy).
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

def hessian(p, epsilon):
    a,b=1+epsilon,1-epsilon
    def integrand(theta,axis):
        co,si=np.cos(theta),np.sin(theta)
        x,y=a*co,b*si
        r2=x*x+y*y
        w=np.hypot(a*si,b*co)
        v=x if axis==0 else y
        return p*(r2**(p/2-1))*(1+(p-2)*v*v/r2)*w
    return np.array([4*quad(lambda t:integrand(t,i),0,np.pi/2,
                 epsabs=1e-12,epsrel=1e-12)[0] for i in range(2)])

for p in (0.03, 0.01, 0.003):
    for c in (0.5, 2.0):
        eps=c*p
        ev=hessian(p,eps)/(np.pi*p*p)
        target=np.array([1+c,1-c])
        assert max(abs(ev-target))<20*p
        assert ev[0]>0
        assert (ev[1]>0)==(c<1)
for p in (0.01,0.005):
    eps=brentq(lambda e:hessian(p,e)[1],p/2,2*p)
    assert abs((eps-p)/p**2-1.5)<10*p
print('PASS: quadratures, signs, sharp coefficient; 10 cases')
