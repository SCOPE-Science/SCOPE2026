"""Reproducible numerical checks for the Hilbert-simplex joint-distance theorem.

Requires Python >= 3.9 and NumPy.  No stochastic check is used as a proof.
"""
from math import pi, log, exp, isclose
import numpy as np


def galambos_bivariate(x, y):
    return exp(-1.0/x - 1.0/y + 1.0/(x+y))


def finite_common_denominator(n, x, y):
    p = 1 - 1/(1+n*x) - 1/(1+n*y) + 1/(1+n*(x+y))
    return p**n


def cov_integrand(t):
    if t == 0.0 or t == 1.0:
        return 1.0
    return -log(1-t+t*t)/(t*(1-t))


def simpson(f, n=10000):
    assert n % 2 == 0
    h=1.0/n
    return h/3*(f(0.0)+f(1.0)+4*sum(f((2*j-1)*h) for j in range(1,n//2+1))
                +2*sum(f(2*j*h) for j in range(1,n//2)))


def run_checks():
    # Common-denominator pair CDF converges to the explicit bivariate limit.
    for x,y in [(0.3,0.8),(1.,1.),(2.,1.7)]:
        errs=[abs(finite_common_denominator(n,x,y)-galambos_bivariate(x,y))
              for n in [100,500,2000,10000]]
        assert errs[-1]<errs[0] and errs[-1]<5e-5,(x,y,errs)

    integral=simpson(cov_integrand,20000)
    assert isclose(integral,pi*pi/9,rel_tol=0,abs_tol=3e-9), integral
    assert isclose((pi*pi/9)/(pi*pi/3),1/3,abs_tol=1e-14)

    # Bounded moments of each directed centered maximum follow from exact tails.
    for n in [2,10,100,10000]:
        for t in [0,0.5,2,5]:
            F_lower=(1+exp(t)/n)**(-n)
            F_upper=(1+exp(-t)/n)**(-n)
            assert F_lower <= exp(-t)+1e-14
            assert 1-F_upper <= exp(-t)+1e-14

    # Direct independent simulations of four random points in a simplex.
    rng=np.random.default_rng(40231)
    n, reps, batch=4000,3000,60
    edge_pairs=[(0,1),(0,2),(1,2),(2,3)]
    samples=[]
    for start in range(0,reps,batch):
        b=min(batch,reps-start)
        log_e=np.log(rng.exponential(size=(b,4,n)))
        cur=[]
        for a,c in edge_pairs:
            dif=log_e[:,a,:]-log_e[:,c,:]
            cur.append(dif.max(axis=1)-dif.min(axis=1)-2*log(n))
        samples.append(np.stack(cur,axis=1))
    vals=np.concatenate(samples)
    co=np.cov(vals,rowvar=False)
    means=vals.mean(axis=0)
    assert max(abs(means-2*0.5772156649015329))<0.16,means
    assert abs(co[0,1]-pi*pi/9)<0.18,co
    assert abs(co[0,3])<0.16,co
    assert abs(co[0,0]-pi*pi/3)<0.25,co
    assert abs(co[0,1]/np.sqrt(co[0,0]*co[1,1])-1/3)<0.08,co

    print('PASS exact finite shared-denominator CDF and its limit (3 thresholds)')
    print('PASS covariance integral versus pi^2/9:',format(integral,'.12f'))
    print('PASS directed log-ratio tail bounds (16 cases)')
    print('PASS simulation: 4 points, %d coordinates, %d repetitions'%(n,reps))
    print('centered means:',means)
    print('covariance matrix:',co)
    print('shared-edge correlation:',co[0,1]/np.sqrt(co[0,0]*co[1,1]))

if __name__=='__main__': run_checks()
