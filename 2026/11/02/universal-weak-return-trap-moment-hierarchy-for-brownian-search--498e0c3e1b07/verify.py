#!/usr/bin/env python3
"""Deterministic numerical checks of Brownian search with harmonic stochastic returns.

Requirements: Python 3.10+, numpy, scipy. Finite checks do not prove asymptotics.
"""
import math
from scipy.integrate import quad
from scipy.special import erfcx, roots_genlaguerre
import numpy as np

checks = 0

def close(a, b, tol, msg):
    global checks
    checks += 1
    assert abs(a-b) <= tol*max(1.0,abs(b)), (msg,a,b)

def scaled_ou_negative_moment(r,k,n,nodes,weights):
    # Ratio: k^(n-1/2) int_{x<0} rho_r(x) E[tau_k(x)^n] dx / H_r.
    # x=-y with a^2 y exp(-a*y) density; Gamma(shape=2) after y=u/a.
    a=math.sqrt(r)
    factor=2.0**(-n)*math.sqrt(2/math.pi)
    def integrand(t):
        if t==0.0: return 0.0
        J=float(np.dot(weights,np.exp(-k*(t/a)**2*nodes**2/2)))
        return math.log1p(t**(-2))**n * J
    return factor*(quad(integrand,0,1,epsabs=2e-9,limit=250)[0]+
                   quad(integrand,1,math.inf,epsabs=2e-9,limit=250)[0])

def mean_completion(r,k):
    a=math.sqrt(r)
    q=math.exp(-a)
    def rho(x): return a/2*(math.exp(-a*x)-math.exp(-a*(2-x)))
    def S(x): return quad(lambda y:math.exp(k*y*y/2),0,x,epsabs=1e-11)[0]
    def A(x):
        return quad(lambda z:math.exp(k*z*z/2)*quad(
                    lambda y:math.exp(-k*y*y/2),0,z,epsabs=1e-11)[0],0,x,epsabs=1e-11)[0]
    S1,A1=S(1),A(1)
    p=q+quad(lambda x:rho(x)*S(x)/S1,0,1,epsabs=1e-10)[0]
    pos=quad(lambda x:rho(x)*(A1*S(x)/S1-A(x)),0,1,epsabs=1e-10)[0]
    neg=(1-math.exp(-2*a))/2*math.sqrt(math.pi/(2*k))*quad(
        lambda y:math.exp(-a*y)*erfcx(math.sqrt(k/2)*y),0,math.inf,epsabs=1e-10)[0]
    return ((1-q)/r+pos+neg)/p

def main():
    a=math.sqrt(2/math.pi)
    # The normal-hitting integral and its first two exact coefficients.
    for r in (.25,1.,4.):
        s=math.sqrt(r)
        H=(1-math.exp(-2*s))/(2*s)
        rho=lambda x:s/2*(math.exp(-s*x)-math.exp(-s*(2-x)))
        p0=math.exp(-s)+quad(lambda x: x*rho(x),0,1)[0]
        close(p0,H,2e-12,'free-return success balance')
        for k in (1e-4,1e-5):
            est=math.sqrt(k)*mean_completion(r,k)
            close(est,math.sqrt(math.pi/2),.01,'mean weak-trap coefficient')
    nodes,weights=roots_genlaguerre(72,1)
    # The asymptotic moment integrals converge to exact r-independent targets.
    targets={1:math.sqrt(math.pi/2),
             2:math.sqrt(2*math.pi)*math.log(2),
             3:None}
    targets[3]=math.sqrt(2/math.pi)*3*quad(
        lambda theta:math.log(1/math.cos(theta))**2,
        0,math.pi/2,epsabs=1e-11)[0]
    for r in (.25,1.,4.):
        for n in (1,2,3):
            # k not too small: t-quadrature is stable without extrapolation.
            x=scaled_ou_negative_moment(r,1e-5 if n==1 else 1e-4,n,nodes,weights)
            close(x,targets[n],.01,'scaled OU return moment')
    print(f'PASS: {checks} deterministic weak-stiffness and renewal checks')
    print('C1 = %.15g, C2 = %.15g, C3 = %.15g'%(targets[1],targets[2],targets[3]))
    print('CV leading amplitude = %.15g'%(math.sqrt(targets[2]/targets[1]**2)))

if __name__=='__main__':
    main()
