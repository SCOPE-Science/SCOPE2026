"""Standalone quadrature checks for noncentral Gaussian spectrogram zeros."""
import numpy as np
from scipy.special import roots_legendre, logsumexp, exp1
from scipy.optimize import brentq
P=np.pi
x,w=roots_legendre(640)

def moments(omega,kind):
    shape=np.ones_like(x) if kind=='flat' else (1-x*x)**2
    logterms=np.log(w*shape)-2*P*x*x+4*P*omega*x
    logm=logsumexp(logterms)
    weights=np.exp(logterms-logm)
    mean=np.dot(weights,x)
    var=np.dot(weights,(x-mean)**2)
    return logm,mean,var

def stats(omega,c,f0,kind):
    logm,mean,var=moments(omega,kind)
    logq=2*np.log(c)-2*P*f0*f0+4*P*omega*f0-logm
    q=np.exp(np.clip(logq,-700,700))
    factor=np.exp(-q)
    density=4*P*factor*(var+q*(f0-mean)**2)
    flux=factor*mean+(1-factor)*f0
    return logq,density,flux,mean,var

def center(c,f0,kind):
    sign=1 if f0>1 else -1
    def f(t):return stats(sign*t,c,f0,kind)[0]
    return sign*brentq(f,-200,200,xtol=1e-12)

k=0
for kind in ['flat','quadratic']:
 for f0 in [-2.,2.]:
    errors=[]
    for c in [1e-2,1e-6,1e-12,1e-30]:
      w0=center(c,f0,kind)
      lq,_,_,_,_=stats(w0,c,f0,kind)
      assert abs(lq)<1e-9
      errs=[]
      for ss in [-.3,0,.3]:
        omega=w0+np.sign(f0)*ss
        _,den,_,_,_=stats(omega,c,f0,kind)
        q=np.exp(4*P*ss)
        gumbel=4*P*q*np.exp(-q)
        assert den>0 and np.isfinite(den)
        errs.append(abs(den-gumbel)/(1+abs(gumbel)))
        k+=1
      errors.append(max(errs))
      k+=1
    assert errors[-1]<errors[0]/3, (kind,f0,errors)
    print('PROFILE',kind,f0,'errors',errors)
for kind in ['flat','quadratic']:
    f0=2.; c=.05; omega=center(c,f0,kind)
    def potential(a):
        m,_,_=moments(a,kind)
        lq=2*np.log(c)-2*P*f0*f0+4*P*a*f0-m
        q=np.exp(lq)
        return m+lq+exp1(q)
    h=1e-3
    second=(potential(omega+h)-2*potential(omega)+potential(omega-h))/h**2/(4*P)
    _,rho,_,_,_=stats(omega,c,f0,kind)
    assert abs(second-rho)<.0003,(kind,second,rho)
    h=1e-4
    fp=stats(omega+h,c,f0,kind)[2]
    fm=stats(omega-h,c,f0,kind)[2]
    assert abs((fp-fm)/(2*h)-rho)<1e-5
    k+=2
print('VERIFY_OK',k,'quadrature flux, noncentral Gaussian potential and Gumbel profile checks')
