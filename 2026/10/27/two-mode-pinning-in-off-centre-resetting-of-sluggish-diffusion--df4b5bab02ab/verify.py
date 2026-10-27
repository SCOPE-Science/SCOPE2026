#!/usr/bin/env python3
"""Reproducible numerical checks for the off-centre resetting resolvent.
Requires Python 3, numpy, scipy. Finite tests are not a proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gammaln, iv, kv, kve


def quantities(alpha, rate):
    assert alpha > 0 and rate > 0
    a = alpha + 2.
    nu = 1./a
    c = 2.*math.sqrt(rate)/a
    h = math.exp(2*nu*math.log(c/2) + gammaln(1-nu)-gammaln(1+nu))
    pref_q = 2.*(c/2.)**nu/math.gamma(nu)
    pref_s = math.gamma(1-nu)*(c/2.)**nu
    def q(x):
        if x == 0: return 1.
        z = c*x**(a/2.)
        return pref_q*math.sqrt(x)*kv(nu,z)
    def s(x):
        if x == 0: return 1.
        z = c*x**(a/2.)
        return pref_s*math.sqrt(x)*(iv(-nu,z)+iv(nu,z))
    def f(z):
        return (a/2.)*z*(kve(1-nu,z)/kve(nu,z))-alpha
    zstar = brentq(f,1e-8,25.,xtol=1e-14)
    mode = ((a*zstar)/(2*math.sqrt(rate)))**(2/a)
    return q,s,h,mode,zstar


def density(x, alpha, rate, b, pack):
    q,s,h,_,_ = pack
    if x == 0: return 0.
    if x < 0: u=q(b)*q(-x)
    elif x < b: u=q(b)*s(x)
    else: u=s(b)*q(x)
    return rate*abs(x)**alpha*u/(2*h)


def run():
    checks=0
    for alpha,rate,b in ((.5,1.,.2),(.5,1.,3.),(1.,1.,.4),(1.,3.,1.2),(2.,.7,.7),(2.,2.,1.6),(.35,.3,1.3)):
        pack=quantities(alpha,rate)
        q,s,h,mode,z=pack
        p=lambda x:density(x,alpha,rate,b,pack)
        pleft=quad(lambda y:p(-y),0,np.inf,epsabs=5e-10,limit=250)[0]
        pmid=quad(p,0,b,epsabs=5e-10,limit=250)[0]
        pright=quad(p,b,np.inf,epsabs=5e-10,limit=250)[0]
        assert abs(pleft+pmid+pright-1)<1e-7,(alpha,rate,b,pleft+pmid+pright)
        checks+=1
        assert abs(pleft-q(b)/2)<1e-8,(alpha,pleft,q(b)/2)
        checks+=1
        assert s(.2)>q(.2)>0 and abs(q(0)-1)<1e-14 and abs(s(0)-1)<1e-14
        checks+=1
        for x in (0.05,.2,.7,2.1):
            assert p(x)>p(-x), (alpha,rate,b,x)
            checks+=1
        # Strict mode maxima checked by sampling on each smooth side.
        for scale in (.2,.8,1.2,2.5):
            if scale!=1:
                assert mode**alpha*q(mode)>(mode*scale)**alpha*q(mode*scale)
                checks+=1
        plusmax=max(b,mode)
        for x in (plusmax*.9,plusmax*1.1):
            assert p(plusmax)>p(x), (alpha,rate,b,plusmax,x,p(plusmax),p(x))
            checks+=1
        # Independent infinitesimal jump: u'= (p/x^alpha)' jumps by -rate at reset point.
        def u(x):return p(x)/x**alpha
        step=1e-5*min(b,1.)
        jump=((u(b+step)-u(b))/step-(u(b)-u(b-step))/step)
        assert abs(jump+rate)<8e-4,(alpha,rate,b,jump)
        checks+=1
        # Verify stationary equation integrated against bounded smooth probes.
        for f,d2f in ((lambda x: math.exp(-x*x),lambda x: (4*x*x-2)*math.exp(-x*x)),(math.sin,lambda x:-math.sin(x))):
            lhs=quad(lambda y: rate/(2*h)*q(b)*q(y)*d2f(-y),0,np.inf,limit=250)[0]
            lhs+=quad(lambda x: rate/(2*h)*q(b)*s(x)*d2f(x),0,b,limit=250)[0]
            lhs+=quad(lambda x: rate/(2*h)*s(b)*q(x)*d2f(x),b,np.inf,limit=250)[0]
            rhs=rate*(
                quad(lambda y:p(-y)*f(-y),0,np.inf,limit=250)[0]+
                quad(lambda x:p(x)*f(x),0,b,limit=250)[0]+
                quad(lambda x:p(x)*f(x),b,np.inf,limit=250)[0]-f(b))
            assert abs(lhs-rhs)<2e-8,(alpha,rate,b,lhs,rhs)
            checks+=1
        print('alpha=%g rate=%g b=%g | modes=(%0.7f,%0.7f) | negmass=%.8f | total=%.11f'%(alpha,rate,b,-mode,plusmax,pleft,pleft+pmid+pright))
    print('PASSED',checks,'deterministic numerical assertions (analytic proof separate).')

if __name__=='__main__':run()
