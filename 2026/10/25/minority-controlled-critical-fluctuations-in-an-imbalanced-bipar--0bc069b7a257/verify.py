"""Independent finite-size and asymptotic checks for the critical bipartite Ising law."""
from itertools import product
from math import comb, cosh, exp, log, sqrt
import numpy as np
from scipy.special import gammaln, logsumexp
from scipy.integrate import quad


def exact_joint_enumeration(m, n, beta):
    """Enumerate all individual spin configurations, not the marginal formula."""
    mass = {s: 0.0 for s in range(-n, n+1, 2)}
    z = 0.0
    for spins in product((-1,1), repeat=m+n):
        a = sum(spins[:m]); b = sum(spins[m:])
        w = exp(beta*a*b/sqrt(m*n))
        mass[b] += w
        z += w
    return {s: w/z for s,w in mass.items()}


def exact_marginal(m, n, beta):
    """Independent grouped summation, exact up to floating precision."""
    vals = {s: 0.0 for s in range(-n, n+1, 2)}
    z = 0.0
    for s in vals:
        w = comb(n,(n+s)//2)*sum(comb(m,(m+a)//2)*exp(beta*a*s/sqrt(m*n))
                                      for a in range(-m,m+1,2))
        vals[s] = w; z += w
    return {s: w/z for s,w in vals.items()}


def reduced_marginal(m, n, beta):
    """Analytic integrated-out majority spin formula."""
    s = np.arange(-n,n+1,2, dtype=float)
    k = ((n+s)/2).astype(int)
    logw = (gammaln(n+1)-gammaln(k+1)-gammaln(n-k+1)
           +m*np.logaddexp(beta*s/sqrt(m*n),-beta*s/sqrt(m*n))
           -m*log(2))
    p = np.exp(logw-logsumexp(logw))
    return s,p


def cw_marginal(n, temp):
    s = np.arange(-n,n+1,2,dtype=float)
    k = ((n+s)/2).astype(int)
    logw = (gammaln(n+1)-gammaln(k+1)-gammaln(n-k+1)+ temp*s*s/(2*n))
    return s,np.exp(logw-logsumexp(logw))


def quartic_second_moment(lam):
    f=lambda x: exp(lam*x*x-x**4/12)
    z=2*quad(f,0,np.inf,epsabs=1e-12)[0]
    m2=2*quad(lambda x:x*x*f(x),0,np.inf,epsabs=1e-12)[0]/z
    return m2


def check():
    count=0
    for m in range(2,8):
        for n in range(2,7):
            for beta in (0.71,1.,1.13):
                e=exact_joint_enumeration(m,n,beta)
                g=exact_marginal(m,n,beta)
                s,p=reduced_marginal(m,n,beta)
                for x,pv in zip(s,p):
                    assert abs(e[int(x)]-pv)<3e-12, (m,n,beta,x)
                    assert abs(g[int(x)]-pv)<3e-12, (m,n,beta,x)
                    count+=2
    # TV convergence for sequences with vanishing minority fraction.
    for n,m in ((20,200),(50,2000),(100,10000),(200,100000)):
        for lam in (-0.7,0.,0.8):
            beta=1+lam/sqrt(n)
            s,p=reduced_marginal(m,n,beta)
            s,q=cw_marginal(n,beta**2)
            tv=np.abs(p-q).sum()/2
            assert tv<2*n/m, (m,n,lam,tv)
            count+=1
    for lam in (-0.8,0.,0.8):
        target=quartic_second_moment(lam)
        errors=[]
        for n in (100,400,1600):
            # Pure Curie-Weiss finite-size critical window; exact effective inverse temp.
            beta=1+lam/sqrt(n)
            s,q=cw_marginal(n,beta**2)
            obs=float(np.sum(q*(s/n**.75)**2))
            errors.append(abs(obs-target))
            count+=1
        assert errors[-1]<0.25 and errors[-1]<errors[-2]<errors[-3], (lam,errors,target)
    print('PASS:',count,'finite-state, reduction, TV and critical-window comparisons')
    print('quartic critical second moment:',quartic_second_moment(0.))

if __name__=='__main__': check()
