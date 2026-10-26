"""Independent finite-matrix checks for Fock localization shape curvature.
These checks corroborate a theorem proved analytically; they do not prove its infinite-dimensional scope.
Requires numpy, scipy and mpmath.
"""
import math
import numpy as np
import mpmath as mp
from scipy.special import gammainc, gammaln
from scipy.stats import norm, poisson

def ratio(n,s):
    term=1.0
    sm=1.0
    for j in range(1,n):
        term *= (n-j+1)/s
        sm += term
    return 1/sm

mp.mp.dps=85

def d(n,s):
    s=mp.mpf(s)
    a=s**n/mp.factorial(n)
    A=mp.fsum(s**k/mp.factorial(k) for k in range(1,n+1))
    return 1-a/A

def top(s,eps,terms,nang=192,nbasis=23):
    theta=2*np.pi*np.arange(nang)/nang
    h=sum(a*np.cos(k*theta)+b*np.sin(k*theta) for k,a,b in terms)
    assert abs(np.mean(h)) < 1e-13
    r2=s+eps*h
    assert np.min(r2)>0
    n=np.arange(nbasis)[:,None]
    m=np.arange(nbasis)[None,:]
    q=(n+m)/2+1
    factors=np.exp(gammaln(q)-(gammaln(n+1)+gammaln(m+1))/2)
    M=np.zeros((nbasis,nbasis),complex)
    for j,t in enumerate(r2):
        M+=factors*gammainc(q,t)*np.exp(1j*(n-m)*theta[j])/nang
    M=(M+M.conj().T)/2
    return np.linalg.eigvalsh(M)[-1]

checks=0
for s in (0.7,1.7,3.0):
    for ts in [[(2,1,0)],[(1,1,0)],[(2,0.8,0.3),(4,-0.6,0.2)]]:
        pred=math.exp(-s)*sum((a*a+b*b)/4*float(d(n,s)) for n,a,b in ts if n>=2)
        for eps in (0.08,0.04,0.02):
            observed=(1-math.exp(-s)-top(s,eps,ts))/(eps**2)
            if pred>1e-8:
                assert abs(observed-pred)<0.025*pred+1e-5,(s,ts,eps,observed,pred)
            else:
                assert abs(observed)<2e-4,(s,ts,eps,observed)
            checks+=1

for s in (0.1,0.8,1.7,20,100,300):
    v=[d(n,s) for n in range(1,35)]
    assert abs(v[0])<mp.mpf('1e-78')
    assert all(v[i+1]>v[i] for i in range(33))
    assert abs(v[1]-2/(mp.mpf(s)+2))<mp.mpf('1e-70')
    checks+=35

for s in (500,2000):
    for alpha in (0.25,0.6,1.3):
        n=round(alpha*s)
        val=1-ratio(n,s)
        target=min(alpha,1)
        assert abs(val-target)<0.015,(s,alpha,val,target)
        checks+=1
    for u in (-1.,0.,1.):
        n=round(s+u*math.sqrt(s))
        scaled=math.sqrt(s)*ratio(n,s)
        target=norm.pdf(u)/norm.cdf(u)
        assert abs(scaled-target)<0.20,(s,u,scaled,target)
        checks+=1
print(f'PASS {checks} independent finite and high-precision checks')
