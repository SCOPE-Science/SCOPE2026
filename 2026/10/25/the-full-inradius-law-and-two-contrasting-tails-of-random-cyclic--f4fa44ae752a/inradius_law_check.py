"""Independent numerical checks for the unit-circumradius cyclic-triangle inradius law.

Only supplementary finite checks: the accompanying mathematical proof is decisive.
Run: python inradius_law_check.py (requires numpy, scipy, mpmath).
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import roots_legendre
import mpmath as mp

PI=math.pi

def survival(t:float)->float:
    if not 0<=t<=0.5: raise ValueError('t must be in [0,1/2]')
    if t==0: return 1.
    if t==.5: return 0.
    d=math.sqrt(1-2*t)
    xl=math.asin((1-d)/2)
    xr=math.asin((1+d)/2)
    def integrand(x):
        s=math.sin(x)
        a=s+t/(2*s)
        return math.acos(min(1.,max(-1.,a)))
    value,err=quad(integrand,xl,xr,epsabs=1.e-12,epsrel=1.e-11,limit=250)
    return 8/PI**2*value

# Independent direct Cartesian construction, not using the half-angle formula.
rg=np.random.default_rng(20261021)
N=360_000
angles=rg.random((N,3))*(2*PI)
xy=np.stack((np.cos(angles),np.sin(angles)),axis=-1)
edges=np.linalg.norm(xy-np.roll(xy,-1,axis=1),axis=2)
sp=0.5*edges.sum(axis=1)
e1=xy[:,1]-xy[:,0]
e2=xy[:,2]-xy[:,0]
a2=np.abs(e1[:,0]*e2[:,1]-e1[:,1]*e2[:,0])*.5
rin=a2/sp
assert (rin>=0).all() and (rin<=.5+1.e-14).all()

# Independent circular-spacings/triangle-angle realization; checks the structural identity.
ordered=np.sort(angles,axis=1)
gaps=np.column_stack((ordered[:,1]-ordered[:,0],ordered[:,2]-ordered[:,1],2*PI+ordered[:,0]-ordered[:,2]))
xs=gaps/4
rin_angles=4*np.prod(np.sin(xs),axis=1)
assert np.max(np.abs(rin-rin_angles))<1.e-12
print('DIRECT_CARTESIAN_AND_DIRICHLET_ANGLE_IDENTITY_OK',N)

# One-dimensional angular integrations versus unconstrained Cartesian sampling.
for t in (.05,.1,.2,.3,.4):
    sf=survival(t)
    empirical=float(np.mean(rin>t))
    stderr=math.sqrt(sf*(1-sf)/N)
    assert abs(sf-empirical)<6*stderr+0.0006,(t,sf,empirical)
    print('CDF',t,'analytic',format(1-sf,'.12f'),'Cartesian',format(1-empirical,'.12f'))
print('FIVE_INDEPENDENT_CDF_CHECKS_OK')

# The moments below were published previously; they are used solely as consistency checks.
m1=12/PI**2-1
m2=5/2-24/PI**2
assert abs(float(rin.mean())-m1)<.002
assert abs(float(np.mean(rin**2))-m2)<.002
assert abs(float(np.var(rin))-(3/2-144/PI**4))<.002
print('KNOWN_INRADIUS_MOMENTS_REPRODUCED_OK')

# One-dimensional survival integration independently reproduces known moments.
x,w=roots_legendre(480)
t=.25*(1+x)
weights=.25*w
m1_quad=float(np.dot(weights,[survival(float(ti)) for ti in t]))
m2_quad=float(np.dot(2*t*weights,[survival(float(ti)) for ti in t]))
assert abs(m1_quad-m1)<4.e-7,(m1_quad,m1)
assert abs(m2_quad-m2)<4.e-7,(m2_quad,m2)
print('CDF_INTEGRATED_MOMENTS_OK')

# The strict upper tail has a finite nonzero density limit, computed from a Hessian.
upper_constant=8/(PI*math.sqrt(3))
for e in (1.e-2,1.e-3,1.e-4):
    ratio=survival(.5-e)/e
    assert abs(ratio/upper_constant-1)<6*e,(e,ratio,upper_constant)
print('SHARP_EQUILATERAL_ENDPOINT_COEFFICIENT_OK')

# The lower tail has a logarithmic singularity: check high-precision CDF ratios.
mp.mp.dps=55

def survival_mp(t):
    d=mp.sqrt(1-2*t)
    lo=mp.asin((1-d)/2);hi=mp.asin((1+d)/2)
    return 8/mp.pi**2*mp.quad(lambda x:mp.acos(min(mp.mpf(1),mp.sin(x)+t/(2*mp.sin(x)))),[lo,hi])

lower_constant=6/mp.pi**2
low=[]
for tstr in ('1e-4','1e-6','1e-8'):
    ti=mp.mpf(tstr)
    rat=(1-survival_mp(ti))/(ti*mp.log(1/ti))
    low.append(float(rat/lower_constant))
assert low[0]>low[1]>low[2]>1
assert low[2]<1.16,low
print('LOGARITHMIC_THIN_ENDPOINT_COEFFICIENT_TREND_OK',low)
print('ALL_CYCLIC_INRADIUS_LAW_CHECKS_OK')
