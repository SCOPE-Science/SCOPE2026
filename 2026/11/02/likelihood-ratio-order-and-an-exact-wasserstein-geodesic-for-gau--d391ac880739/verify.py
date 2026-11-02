"""Deterministic numerical consistency checks for smooth Gaussian peak-height family.
Only corroborates analytic theorem; no finite check proves an infinite statement.
"""
import math
from statistics import NormalDist

phi = lambda x: math.exp(-x*x/2)/math.sqrt(2*math.pi)
Phi = NormalDist().cdf

def g(z):
    return phi(z) + z*Phi(z)

def density(eta, x):
    if eta == 1.0:
        return x*math.exp(-x*x/2) if x > 0 else 0.0
    s=math.sqrt(1-eta*eta)
    return math.sqrt(2*math.pi)*s*phi(x)*g(eta*x/s)

def deriv_F(eta, x):
    return -math.sqrt(2*math.pi)*phi(x)*Phi(eta*x/math.sqrt(1-eta*eta))

def simpson(f, a, b, n=1500):
    assert n%2==0
    h=(b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+h*j) for j in range(1,n,2))+2*sum(f(a+h*j) for j in range(2,n,2)))

def cdf_rayleigh_mixture(eta, x):
    if eta==1.0: return 1-math.exp(-x*x/2) if x>0 else 0.
    s=math.sqrt(1-eta*eta)
    return simpson(lambda r:r*math.exp(-r*r/2)*Phi((x-eta*r)/s),0,11,1500)

def cdf_parameter_derivative(eta,x):
    return Phi(x)+simpson(lambda e: deriv_F(e,x),0,eta,1500) if eta>0 else Phi(x)

count=0
# Independent density integration from normal-Rayleigh convolution.
for eta in (0, .1, .35, .6, .9, .98):
    for x in (-2.0,-1.,-.1,0.,.4,1.,2.5):
        s=math.sqrt(1-eta*eta)
        convol=simpson(lambda r:r*math.exp(-r*r/2)*phi((x-eta*r)/s)/s,0,11,1600)
        assert abs(convol-density(eta,x)) < 0.0000002, (eta,x,convol,density(eta,x))
        count+=1
# Independent CDF computations agree with analytic parameter derivative integration.
for eta in (.12,.37,.73,.94):
    for x in (-2.,-.7,0.,.7,2.):
        a=cdf_rayleigh_mixture(eta,x)
        b=cdf_parameter_derivative(eta,x)
        assert abs(a-b) < 0.0000003,(eta,x,a,b)
        count+=1
# Global log-likelihood monotonicity, not extrapolated beyond sampled arguments.
for a,b in ((0,.1),(.1,.35),(.35,.65),(.65,.92)):
    for x in [-3+i*.1 for i in range(61)]:
        y=x+1e-3
        assert density(b,y)/density(a,y)>density(b,x)/density(a,x), (a,b,x)
        count+=1
# Strict CDF order and agreement with analytic derivative sign.
for a,b in ((0,.1),(.1,.35),(.35,.65),(.65,.92)):
    for x in (-2,-1,0,.2,1,2.5):
        assert cdf_parameter_derivative(a,x)>cdf_parameter_derivative(b,x)
        count+=1
for eta in (.01,.24,.6,.96):
    for x in (-2,0,1.5):
        eps=1e-5
        numerical=(cdf_parameter_derivative(eta+eps,x)-cdf_parameter_derivative(eta-eps,x))/(2*eps)
        assert abs(numerical-deriv_F(eta,x))<3e-7
        count+=1
# Mean identity by exact representation, and direct numerical integral of density.
for eta in (0,.2,.5,.8,1.0):
    expected=eta*math.sqrt(math.pi/2)
    numerical=simpson(lambda x:x*density(eta,x),-11,11,6000)
    assert abs(numerical-expected)<3e-6, (eta,numerical,expected)
    count+=1
print('PASS:',count,'deterministic numerical consistency assertions')
print('Analytical MLR, strict stochastic ordering, and W1 equality require independent mathematical proof.')
