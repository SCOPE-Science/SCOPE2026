"""Independent numerical checks of a weak-rescaling stationary large-deviation law.

Dependencies: Python 3, scipy, numpy. This checks exact finite-s generating
functions and the candidate limiting rate, not an infinite-limit proof.
"""
import math
from scipy.optimize import brentq
from scipy.special import spence

def dilog(t):
    return float(spence(1.0-t))

def qseries_scaled(s, t):
    """Exact stationary scaled log-MGF for |theta|^2 D/lambda=t<1."""
    q=(1.0-s)**2
    terms=math.ceil(math.log(1e-13)/math.log(q))
    return -s*sum(math.log1p(-t*q**j) for j in range(terms+1))

def rate(c):
    if c==0: return 0.0, 0.0
    def f(y):return y*y/(-math.expm1(-y))-c
    y=brentq(f,1e-12,2+2*math.sqrt(c),xtol=1e-14)
    t=-math.expm1(-y)
    return y-0.5*dilog(t),y

def rate_legendre(c):
    """Independent one-dimensional numerical Legendre optimization."""
    from scipy.optimize import minimize_scalar
    rho=math.sqrt(c)
    # radial scaled mgf: Lambda(theta)=0.5 Li_2(theta^2) for theta in [0,1)
    f=lambda th: -(rho*th-0.5*dilog(th*th))
    m=minimize_scalar(f,bounds=(0.0,1.0),method='bounded',options={'xatol':1e-13})
    return -m.fun

def checks():
    for t in [0.15,0.35,0.75]:
        lim=0.5*dilog(t)
        errors=[]
        for s in [0.16,0.08,0.04,0.02]:
            g=qseries_scaled(s,t)
            errors.append(abs(g-lim))
        assert errors[-1]<errors[0]/5,(t,errors)
        assert errors[-1]<0.015,(t,errors)
        print('MGF argument',t,'limiting',round(lim,10),'errors',[round(e,8) for e in errors])
    for c in [0.05,0.25,1.0,2.0,7.0,25.0]:
        direct,y=rate(c)
        by_dual=rate_legendre(c)
        assert abs(direct-by_dual)<2e-8,(c,direct,by_dual)
        assert direct>0
        print('rate',c,'value',round(direct,10),'root_y',round(y,8))
    for c in [0.1,0.5,1.5,4.0]:
        base,_=rate(c)
        for k in [2,3,6]:
            joint,_=rate(k*c)
            assert 0<joint<k*base,(c,k,joint,base)
    # Small- and large-argument asymptotic structures are consistent.
    for c in [1e-5,1e-6]:
        h,_=rate(c)
        assert abs(h/(c/2)-1)<0.0001
    c=1e6
    h,_=rate(c)
    assert abs(h-(math.sqrt(c)-math.pi**2/12))<1e-8
    print('All finite-s pressure and dual-rate checks passed.')

if __name__=='__main__':checks()
