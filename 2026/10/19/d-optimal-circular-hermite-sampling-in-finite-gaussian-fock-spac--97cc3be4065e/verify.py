"""Reproduce exact determinant, angular optimum, radial equations, spectra and asymptotic for finite Gaussian-polynomial jet sampling.
Requires numpy and scipy. Run: python verify.py
"""
import numpy as np
from math import pi, factorial, lgamma, log, exp
from scipy.optimize import brentq
from scipy.special import logsumexp, gammaln

def stats(n,t):
    k=np.arange(2*n,dtype=float)
    a=k*np.log(t)-gammaln(k+1)
    p=np.exp(a-logsumexp(a))
    s0=np.exp(logsumexp(a)); s2=np.exp(logsumexp(a[1:]+2*np.log(k[1:])))
    return s0,s2, float(k@p),float((k**3)@p/((k**2)@p))

def radii(n):
    m=2*n-1
    h=brentq(lambda t:sum(stats(n,t)[2:])-m,0.00001,4*n,xtol=1e-12)
    s=brentq(lambda t:stats(n,t)[2]-m/2,0.00001,4*n,xtol=1e-12)
    return h,s

def logdet_hermite_opt(n,t):
    m=2*n-1; k=np.arange(2*n)
    a=k*np.log(t)-gammaln(k+1)
    return 4*n*log(n)+n*m*log(t)-n*(logsumexp(a)+logsumexp(a[1:]+2*np.log(k[1:]))) - float(np.sum(gammaln(k+1)))

def logdet_simple_opt(n,t):
    m=2*n-1; k=np.arange(2*n)
    a=k*np.log(t)-gammaln(k+1)
    return 2*n*log(2*n)+n*m*log(t)-2*n*logsumexp(a) - float(np.sum(gammaln(k+1)))

def direct_matrix(n,t,angles):
    k=np.arange(2*n,dtype=float)
    v=np.exp(0.5*k*np.log(t)-0.5*gammaln(k+1))
    s0,s2,*_=stats(n,t)
    p=np.exp(1j*np.outer(angles,k))*v
    # Ordinary derivative row divided by its norm has the same Gram spectrum/determinant as Euler rows.
    return np.vstack([p/np.sqrt(s0),p*k/np.sqrt(s2)])

def predicted_block(n,t,j):
    s0,s2,*_=stats(n,t)
    k=np.array([j,j+n],dtype=float)
    v=np.exp(0.5*k*np.log(t)-0.5*gammaln(k+1))
    return np.sqrt(n)*np.array([v/np.sqrt(s0),k*v/np.sqrt(s2)])

checks=0
maxerr=0
for n in range(2,9):
    h,s=radii(n)
    assert h<s
    assert abs(sum(stats(n,h)[2:])-(2*n-1))<1e-9
    angles=2*pi*np.arange(n)/n
    H=direct_matrix(n,h,angles)
    logd=np.linalg.slogdet(H)[1]*2
    err=abs(logd-logdet_hermite_opt(n,h));maxerr=max(maxerr,err)
    assert err<1e-7,(n,err)
    pred=[]
    for j in range(n):
        b=predicted_block(n,h,j)
        pred.extend(np.linalg.svd(b,compute_uv=False)**2)
    got=np.linalg.svd(H,compute_uv=False)**2
    err=max(abs(np.sort(pred)-np.sort(got)));maxerr=max(maxerr,err)
    assert err<1e-7,(n,err)
    # Nonuniform angles: confluent Vandermonde formula versus direct determinant.
    random_angles=angles+0.025*np.sin(np.arange(n)*1.3245)
    R=direct_matrix(n,h,random_angles)
    pair=np.prod([abs(np.exp(1j*random_angles[j])-np.exp(1j*random_angles[i])) for i in range(n) for j in range(i+1,n)])
    log_formula=(n*(2*n-1)*log(h)+8*log(pair)-sum(lgamma(k+1) for k in range(2*n))-n*sum(log(x) for x in stats(n,h)[:2]))
    err=abs(np.linalg.slogdet(R)[1]*2-log_formula);maxerr=max(maxerr,err)
    assert err<1e-7,(n,err)
    assert np.linalg.slogdet(R)[1]<np.linalg.slogdet(H)[1]+1e-8
    checks+=5
for n in [10,20,40,80,160]:
    h,s=radii(n)
    log_ratio=logdet_hermite_opt(n,h)-logdet_simple_opt(n,s)
    scaled=exp(log_ratio+n*log(4))
    assert 2.70<scaled<2.78
    assert abs((s-h)-1)<0.055
    checks+=2
print('PASS',checks,'tests; maximum direct algebraic discrepancy',format(maxerr,'.3g'))
print('n, t_jet, t_value, 4^n * (max determinant-squared jet)/(max determinant-squared value)')
for n in [2,3,5,10,20,40,80,160]:
    h,s=radii(n)
    log_ratio=logdet_hermite_opt(n,h)-logdet_simple_opt(n,s)
    print(n,format(h,'.9f'),format(s,'.9f'),format(exp(log_ratio+n*log(4)),'.9f'))
print('Limiting rescaled penalty target e =',format(exp(1),'.9f'))
