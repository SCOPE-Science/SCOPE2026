"""Independent numerical checks for two-node power-exponential kernel quadrature.

Requires numpy and scipy. Algebraic arguments in RESULT.md establish the
continuous-parameter theorem; these numerical checks are corroborative only.
"""
import math
import numpy as np
from scipy.special import gamma, gammainc
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss

N = 76
ZN, WN = leggauss(N)
checks = 0

def verify(condition, msg):
    global checks
    if not condition:
        raise AssertionError(msg)
    checks += 1

def mean(x, a, lam=1.0):
    x = np.asarray(x)
    s = 1.0/a
    z = np.power(np.maximum(x,0.0), a)*lam
    w = np.power(np.maximum(1.0-x,0.0), a)*lam
    return (gamma(s)*lam**(-s)/a)*(gammainc(s,z)+gammainc(s,w))

def mean_prime(x,a,lam=1.0):
    return np.exp(-lam*np.power(x,a))-np.exp(-lam*np.power(1.0-x,a))

def weight_norm_expect(a, eta=0.0, lam=1.0):
    # Diagonal delta=(X-Y)>0 times two; 2*norm^2 cancels 1/2.
    def inner(delta):
        us = 0.5*delta+(1.0-delta)*(ZN+1.0)*0.5
        mu1 = mean(us+delta*0.5,a,lam)
        mu2 = mean(us-delta*0.5,a,lam)
        k = math.exp(-lam*delta**a)
        denom_m = eta + (-math.expm1(-lam*delta**a))
        return float((1-delta)*0.5*np.dot(WN, (mu1+mu2)**2/(1+eta+k)**2 + (mu1-mu2)**2/denom_m**2))
    # Transform delta=t^3 to soften near zero and split around nugget scale.
    def transformed(t):
        return 3*t*t*inner(t*t*t) if t>0 else 0.0
    if eta:
        p = min(0.99, (eta/lam)**(1.0/(3*a)))
        val = quad(transformed,0,p,epsrel=3e-7,epsabs=2e-8,limit=250)[0] + quad(transformed,p,1,epsrel=3e-7,epsabs=2e-8,limit=250)[0]
    else:
        val = quad(transformed,0,1,epsrel=8e-7,epsabs=2e-7,limit=250)[0]
    return val

def derivative_energy(a,lam=1.0):
    return quad(lambda u:mean_prime(u,a,lam)**2,0,1,epsabs=1e-12)[0]

def ridge_coefficient(a,lam=1.0):
    if a>1.5:
        return lam**(-3.0/a)*gamma(3.0/a)*gamma(2-3.0/a)/a*derivative_energy(a,lam)
    if a==1.5:
        return 2.0*lam**(-2.0)/3.0*derivative_energy(a,lam)
    return None

for a in (0.6,1.0,1.25,1.5,1.75,2.0):
    for x,y in ((0.12,0.59),(0.17,0.171),(0.23,0.91),(0.44,0.53)):
        m1,m2=mean(x,a),mean(y,a)
        kval=math.exp(-abs(x-y)**a)
        w1=(m1+m2)/(2*(1+kval))+(m1-m2)/(2*(1-kval))
        w2=(m1+m2)/(2*(1+kval))-(m1-m2)/(2*(1-kval))
        verify(abs(w1+kval*w2-m1)<2e-12,'K w=m first')
        verify(abs(kval*w1+w2-m2)<2e-12,'K w=m second')
        verify(abs((w1*w1+w2*w2)-0.5*((m1+m2)**2/(1+kval)**2+(m1-m2)**2/(1-kval)**2))<1e-9,'norm identity')
    for x in (0.13,0.31,0.69,0.91):
        h=1e-5
        d=(mean(x+h,a)-mean(x-h,a))/(2*h)
        verify(abs(d-mean_prime(x,a))<4e-9,'kernel-mean derivative')

for a in (0.6,1.0,1.25):
    val0=weight_norm_expect(a,0.0)
    val_eta=weight_norm_expect(a,1e-6)
    verify(math.isfinite(val0) and 0<val_eta<val0,'finite limit and ridge damping')
    verify(abs(val0-val_eta)/val0<0.06,'subcritical ridge convergence')
    print('FINITE_VARIANCE',a,val0,val_eta)

for a in (1.5,1.75,2.0):
    e1,e2=1e-5,1e-7
    v1,v2=weight_norm_expect(a,e1),weight_norm_expect(a,e2)
    coef=ridge_coefficient(a)
    verify(v2>v1>0,'diverging ridge variance')
    if a==1.5:
        estimate=(v2-v1)/math.log(e1/e2)
        verify(abs(estimate/coef-1)<0.22,'critical logarithm coefficient')
        print('LOG_COEFFICIENT',a,'predicted',coef,'estimate',estimate)
    else:
        power=3.0/a-2.0
        estimate=v2*(e2**(-power))
        verify(abs(estimate/coef-1)<0.25,'supercritical power coefficient')
        print('POWER_COEFFICIENT',a,'predicted',coef,'estimate',estimate)

# Gaussian-specialization consistency, a=2 and lambda=1.
gaussian_coefficient = (2*math.erf(0.5)-math.erf(1.0))
new_coefficient = (1/math.sqrt(math.pi))*quad(lambda u:abs(mean_prime(u,2.0)),0,1)[0]
verify(abs(gaussian_coefficient-new_coefficient)<1e-12,'Gaussian tail specialization')
print('CHECKS_PASS',checks)
