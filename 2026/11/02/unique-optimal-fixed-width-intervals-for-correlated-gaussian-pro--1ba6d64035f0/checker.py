"""Finite numerical consistency checks for optimal Gaussian-product intervals.
These checks supplement, not replace, the analytical proof.
"""
import math
from scipy.special import k0, k1
from scipy.optimize import brentq
from scipy.integrate import quad
euler_gamma = 0.5772156649015328606

checks=0

def test(condition, reason):
    global checks
    checks += 1
    if not condition: raise AssertionError(reason)

def density(rho, x):
    d=1-rho*rho
    return math.exp(rho*x/d)*k0(abs(x)/d)/(math.pi*math.sqrt(d))

def location(rho,h):
    d=1-rho*rho
    def gap(c): return 2*rho*h/d + math.log(k0((h+c)/d)) - math.log(k0((h-c)/d))
    return brentq(gap,-h*(1-1e-12), h*(1-1e-12), xtol=1e-15)

def mass(rho,h,c):
    return quad(lambda x:density(rho,x),c-h,0,epsabs=1e-12)[0] + quad(lambda x:density(rho,x),0,c+h,epsabs=1e-12)[0]

for rho in [-0.8,-0.4,0,0.2,0.65,0.9]:
    for h in [0.03,0.2,1,2.5]:
        c=location(rho,h)
        test(abs(c)<h,'interior')
        test(c*rho>=-1e-15,'orientation')
        test(abs(c+location(-rho,h))<1e-11,'symmetry')
        test(abs(density(rho,c+h)-density(rho,c-h))<1e-10,'endpoint equality')
        if rho==0: test(abs(c)<1e-12,'zero-correlation exact center')
        test(mass(rho,h,c)>mass(rho,h,0)-1e-10,'centered comparison')
for rho in [-0.7,0.3,0.8]:
    for h in [0.004,0.001,0.0002]:
        d=1-rho*rho
        c=location(rho,h)
        L=math.log(2*d/h)-euler_gamma
        test(abs(c/((rho/d)*h*h*L)-1)<0.05,'logarithmic displacement')
        test(mass(rho,h,c)>mass(rho,h,0),'strict probability gain')
print('PASS',checks,'finite numerical assertions')
