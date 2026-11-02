#!/usr/bin/env python3
"""Independent numerical checks of the wedge-distance formulation (no external data)."""
import numpy as np
from scipy.integrate import quad

def d(x,y,a):
    c=np.cos(a); t=np.clip((x*x-x*y*c)/(x*x+y*y-2*x*y*c),0,1)
    return float(np.sqrt(x*x*(1-t)**2+y*y*t*t+2*x*y*t*(1-t)*c))

def wedge_tail(a,r):
    def integrand(u):
        v=d(u,1-u,a)
        z=r/v
        return (1+z)*np.exp(-z)
    return quad(integrand,0,1,epsabs=2e-12,epsrel=1e-10,limit=300,points=[.1,.5,.9])[0]

def polygon_logcdf(angles,r):
    return sum(np.log1p(-wedge_tail(a,r)) for a in angles)

a=np.pi/2
b=np.pi/3
rect=[a]*4
rhomb=[b,np.pi-b,b,np.pi-b]
for r in (0.002,0.005,.02,.15,.3,.6,1,1.5,2,4,8):
    l1=polygon_logcdf(rect,r); l2=polygon_logcdf(rhomb,r)
    print('r=',r,'cdf regular=',np.exp(l1),'cdf rhombus=',np.exp(l2),'ratio=',np.exp(l2-l1))
assert polygon_logcdf(rhomb,.002)>polygon_logcdf(rect,.002)
assert polygon_logcdf(rhomb,8)<polygon_logcdf(rect,8)
for a in (np.pi/4,np.pi/2,2*np.pi/3,5*np.pi/6):
    c=1 if a<=np.pi/2 else np.sin(a)
    vals=[(1-wedge_tail(a,r))/r for r in (.002,.001,.0005)]
    print('angle',a,'CDF/r numerical',vals,'predicted',2/c)
    assert abs(vals[-1]-2/c)<.035
print('NUMERICAL_CHECKS_PASSED')
