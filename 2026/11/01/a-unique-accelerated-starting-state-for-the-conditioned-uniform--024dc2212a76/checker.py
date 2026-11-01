#!/usr/bin/env python3
"""Independent finite checks for the stated analytic spectral and mixing formulas."""
import math

pi = math.pi
checks = 0

def close(got, expected, tol=1e-10):
    global checks
    if not math.isfinite(got) or abs(got - expected) > tol:
        raise AssertionError(f'{got!r} != {expected!r} within {tol}')
    checks += 1

def simpson(fn, start, end, n=3000):
    assert n % 2 == 0
    dx=(end-start)/n
    return dx/3 * (fn(start)+fn(end)+4*sum(fn(start+dx*k) for k in range(1,n,2)) +2*sum(fn(start+dx*k) for k in range(2,n,2)))

def h(x):
    return math.sin(pi*(x+1)/4)

def phi(m,x):
    return math.sin((2*m+1)*pi*(x+1)/4)

def nu(m):
    return (-1)**m/(2*m+1)

def fm(m,x):
    return 2*m+1 if abs(x+1)<1e-14 else phi(m,x)/h(x)

def p(x,y):
    return (pi/4)*h(y)/h(x) if y>=-x else 0.0

def station(x):
    return h(x)**2

# K is the killed uniform transition kernel at a=1:
# (Kf)(x) = 1/2 integral_{-x}^1 f(y)dy.
for m in range(12):
    k=(2*m+1)*pi/4
    lam=2*(-1)**m/((2*m+1)*pi)
    for x in [-0.9,-0.65,-0.25,0,0.15,1/3,0.75,1.0]:
        direct=(math.cos(k*(1-x))-math.cos(2*k))/(2*k)
        close(direct,lam*phi(m,x),2e-14)

# Completeness is established analytically via mixed boundary Sturm-Liouville;
# these orthogonality tests are finite corroboration only.
for m in range(5):
    for j in range(5):
        close(simpson(lambda x:phi(m,x)*phi(j,x),-1,1),float(m==j),5e-12)
close(simpson(station,-1,1),1.0,1e-12)

# Doob transition is normalized and reversible.
for x in [-0.9,-0.5,-0.1,1/3,0.75,1.0]:
    close(simpson(lambda y:p(x,y),-x,1),1.0,2e-12)
    for y in [-0.95,-0.5,0,0.32,0.8,1.0]:
        close(station(x)*p(x,y),station(y)*p(y,x),3e-14)

# Direct two-step density formula, independent of spectral expansion:
# p2(x,z) = pi^2/16 * h(z)/h(x) * (1+min(x,z)).
for x in [-0.8,-0.2,1/3,0.9]:
    for z in [-0.9,-0.3,0.1,0.6,0.95]:
        direct = simpson(lambda y:p(x,y)*p(y,z),max(-x,-z),1,1200)
        explicit = (pi*pi/16)*h(z)/h(x)*(1+min(x,z))
        close(direct,explicit,2e-12)

# One-step density relative to stationarity has the exact spectral coefficients.
for x in [-0.75,-0.25,0.33,0.7,1.0]:
    for m in range(1,8):
        left=simpson(lambda y:p(x,y)*fm(m,y),-x,1,4000)
        close(left,nu(m)*fm(m,x),2e-10)

# Exact absolute eigenmode normalizations via sign-resolved integrals.
I1=(3*math.sqrt(3))/(2*pi)
I2=(5/(3*pi))*(math.sin(pi/5)+math.sin(2*pi/5))
close(simpson(lambda x:abs(phi(1,x)*h(x)),-1,1/3,4000) + simpson(lambda x:abs(phi(1,x)*h(x)),1/3,1,4000), I1,1e-11)
splits=[-1,4/5-1,8/5-1,1] # x from u = pi/5, 2pi/5, (x+1)pi/4
splits=[-1,-1/5,3/5,1] # correct mapping x=4/5 -1 = -1/5; x=8/5-1=3/5
close(sum(simpson(lambda x:abs(phi(2,x)*h(x)),splits[i],splits[i+1],4000) for i in range(3)),I2,1e-11)
close(fm(1,1/3),0.0,2e-15)
close(fm(2,1/3),-1.0,2e-15)
for x in [-0.9,-0.5,0,0.5,1.0]:
    close(fm(1,x),3-4*h(x)**2,2e-14)

# For sufficiently large n, TV can be evaluated accurately from the spectral
# series; compare rates and constants, not infinity via finite experiments.
def tv_spectral(n,x):
    def val(y):
        return abs(sum(nu(m)**n*fm(m,x)*fm(m,y) for m in range(1,45)))*station(y)
    return simpson(val,-1,1,12000)/2
for x in [-0.65,0.0,0.7,1.0]:
    coeff=abs(fm(1,x))*I1/2
    close(tv_spectral(18,x)/(3.0**(-18)),coeff,0.0003)
coeff=I2/2
close(tv_spectral(30,1/3)/(5.0**(-30)),coeff,0.0001)
print(f'PASS: {checks} finite checks')
print(f'I1={I1:.15f}; I2={I2:.15f}; TV_exception_coefficient={coeff:.15f}')
print('Scientific limits: finite computations do not establish the infinite spectral expansion or asymptotic bounds.')
