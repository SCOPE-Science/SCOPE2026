"""Independent numerical checks of exact identities for the proportional-reset Brownian stationary law.
No stochastic simulation is used, and these checks do not replace the analytical proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

PI = math.pi
normal_density = lambda x: math.exp(-x*x/2.0)/math.sqrt(2.0*PI)
normal_cdf = lambda x: 0.5*math.erfc(-x/math.sqrt(2.0))
checks = 0

def approx(x, y, tol=1e-10):
    global checks
    assert abs(x-y) <= tol*max(1.0,abs(y)), (x,y)
    checks+=1

def positive(x):
    global checks
    assert x>0,x
    checks+=1

u = math.sqrt(3.0-math.sqrt(6.0))
v = math.sqrt(3.0+math.sqrt(6.0))
H3=lambda x: x*x*x-3.0*x
H4=lambda x: x**4-6.0*x*x+3.0
Ctv = math.sqrt(6.0)/4.0*(u*normal_density(u)+v*normal_density(v))
Ck = math.sqrt(6.0)/8.0*u*normal_density(u)
# Check normal-density Hermite integrals, including signs and normalization.
for x in (u,v,math.sqrt(3.0),0.0):
    approx(H4(x), (x*x*x*x-6.0*x*x+3.0))
approx(H4(u),0.0)
approx(H4(v),0.0)
approx(H3(math.sqrt(3.0)),0.0)
approx(quad(lambda x:abs(H4(x))*normal_density(x),-13.,13.,points=[-v,-u,u,v],epsabs=1e-12)[0],16.0*Ctv,2e-10)
approx(quad(lambda x:H4(x)*normal_density(x),-13.,13.,epsabs=1e-12)[0],0.0,2e-10)
positive(u*normal_density(u)-v*normal_density(v))
# Characteristic function and inversion are calculated from a finite geometric
# product with a rigorously controllable (although not here certified) tail.
for a in (0.0,0.5,0.9,0.97):
    q=a*a; w0=1-q
    K=1 if q==0 else math.ceil(math.log(2e-14)/math.log(q))
    weights=w0*q**np.arange(K)
    approx(sum(weights),1.0,5e-12)
    approx(sum(weights**2),(1-q)/(1+q),5e-12)
    approx(3.0*sum(weights**2),3.0*(1-q)/(1+q),5e-12)
    approx(3.0*sum(weights**2)**2+6.0*sum(weights**4),
           3.0*((1-q)/(1+q))**2+6.0*w0**4/(1-q**4),5e-12)
    def characteristic(t):
        return math.exp(-float(np.log1p(weights*t*t/2.0).sum()))
    for t in (0.25,1.0,2.0):
        approx(characteristic(t),characteristic(-t),1e-14)
        positive(characteristic(t))
    def discrepancy(z):
        def integrand(t):
            if t==0: return 0
            return (2.0/PI)*(math.sin(t*z)/t)*(characteristic(t)-math.exp(-t*t/2.0))
        return quad(integrand,0.,400.,epsabs=8e-9,limit=240)[0]
    positive(discrepancy(0.8))
    positive(-discrepancy(2.5))
    crossing=brentq(discrepancy,1.2,2.5,xtol=2e-7)
    assert 1.55 <crossing<1.8
    checks+=1
    print('a=%.2f, variance_mix=%.9f, crossing=%.9f, discrepancy_1=%.9f'%(a,(1-q)/(1+q),crossing,discrepancy(1.0)))
print('C_TV=%.12f, C_K=%.12f, limiting_interval_coverage=%.12f'%(Ctv,Ck,2*normal_cdf(math.sqrt(3.))-1))
print('PASS: %d numerical and algebraic checks'%checks)
