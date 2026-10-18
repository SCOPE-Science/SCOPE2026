"""Finite enumeration and quadrature checks for the critical block-information limit.

Run with Python 3 plus numpy and scipy: python verify.py
All calculations use natural logarithms. Numerical checks do not establish the asymptotic theorem.
"""
import math
import itertools
import numpy as np
from scipy.special import gammaln, logsumexp, roots_hermitenorm, roots_legendre, gamma


def log_binom(n):
    j=np.arange(n+1)
    return gammaln(n+1)-gammaln(j+1)-gammaln(n-j+1)


def finite_log_likelihoods(n,k):
    if not 1<=k<=n:
        raise ValueError('invalid n,k')
    idx=np.arange(n+1)
    logz=logsumexp(log_binom(n)+((2*idx-n)**2)/(2*n))
    j=np.arange(k+1)
    l=np.arange(n-k+1)
    s=2*(j[:,None]+l[None,:])-n
    lognumerator=logsumexp(log_binom(n-k)[None,:]+s*s/(2*n),axis=1)
    return k*math.log(2)+lognumerator-logz


def finite_kl(n,k):
    loglik=finite_log_likelihoods(n,k)
    logmass=log_binom(k)-k*math.log(2)
    return float(np.sum(np.exp(logmass+loglik)*loglik))


def limit_integral(alpha):
    # Gaussian standard-reference integration in z and high-order quadrature in quartic x.
    zz,ww=roots_hermitenorm(180)
    ww/=math.sqrt(2*math.pi)
    nodes,weights=roots_legendre(360)
    xx=nodes*7
    weights=weights*7*np.exp(-(xx**4)/12)
    weights/=np.sum(weights)
    loglik=(math.sqrt(alpha)*zz[:,None]*xx[None,:]-0.5*alpha*xx[None,:]**2)
    # Logsumexp prevents overflowing the mixture when |z| is large.
    logL=logsumexp(loglik+np.log(weights)[None,:],axis=1)
    ratio=np.exp(logL)
    d=float(np.sum(ww*ratio*logL))
    norm=float(np.sum(ww*ratio))
    variance=float(np.sum(ww*ratio*zz**2))
    return d,norm,variance


def small_n_brute(n,k):
    numer=np.zeros(k+1)
    denominator=0.
    for spins in itertools.product((-1,1),repeat=n):
        weight=math.exp(sum(spins)**2/(2*n))
        denominator+=weight
        numer[(sum(spins[:k])+k)//2]+=weight
    observed=numer/denominator
    analytical=np.exp(log_binom(k)-k*math.log(2)+finite_log_likelihoods(n,k))
    assert np.max(np.abs(observed-analytical))<1e-12
    return np.sum(observed*np.log(observed/np.exp(log_binom(k)-k*math.log(2))))


def run():
    cases=0
    for n in range(2,11):
        for k in range(1,n+1):
            got=finite_kl(n,k)
            expected=small_n_brute(n,k)
            assert abs(got-expected)<5e-12, (n,k,got,expected)
            assert got>=-1e-12
            cases+=1
    v=math.sqrt(12)*gamma(.75)/gamma(.25)
    assert abs(v-1.1708286566075286)<1e-12
    for a in (.125,.5,1.,2.,4.,8.):
        d,norm,second=limit_integral(a)
        assert d>0, (a,d)
        assert abs(norm-1)<2e-9,(a,norm)
        assert abs(second-(1+a*v))<1e-8,(a,second,1+a*v)
        print('alpha',a,'D_alpha',round(d,10))
        cases+=3
    ds=[limit_integral(a)[0] for a in (.125,.5,1.,2.,4.,8.)]
    assert all(x<y for x,y in zip(ds,ds[1:]))
    cases+=5
    for a in (.5,1.,2.):
        d=limit_integral(a)[0]
        for n in (256,1024,4096):
            k=round(a*math.sqrt(n))
            dn=finite_kl(n,k)
            print('finite n',n,'k',k,'alpha',a,'D_n',round(dn,9),'D_limit',round(d,9))
            # A deliberately loose consistency tolerance at accessible n.
            assert abs(dn-d)<.30,(n,k,dn,d)
            cases+=1
    ratio=limit_integral(.02)[0]/(.02**2)
    assert abs(ratio-v*v/4)<.013,(ratio,v*v/4)
    cases+=1
    print('PASSED',cases,'finite identity/quadrature/asymptotic checks')

if __name__=='__main__':
    run()
