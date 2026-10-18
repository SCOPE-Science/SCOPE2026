"""Reproduce one-step stochastic Heun / PI gain distribution identities.
Requires Python 3, NumPy and SciPy; no external data or network.
"""
import math
import numpy as np
from scipy.stats import ncx2


def params(d, lam, g, h, x, tol, alpha, ki, kp, previous_error):
    x=np.asarray(x,dtype=float)
    assert x.shape==(d,) and lam>0 and g>0 and h>0 and tol>0
    assert alpha>0 and previous_error>0 and ki>=0 and kp>=0 and ki+kp>0
    mu=-(lam*lam*h*h/2)*x
    sd=lam*g*h**1.5/2
    nc=float(mu@mu)/sd**2
    b=alpha**ki*previous_error**kp
    return mu,sd,nc,b


def exact_survival(t,d,sd,nc,b,tol,k):
    q=(tol*math.sqrt(d)/sd)**2*(b/t)**(2/k)
    return float(ncx2.cdf(q,d,nc))


def asymptotic_coefficient(d,sd,nc,b,tol,k):
    return (math.exp(-nc/2)*
            (tol*math.sqrt(d)/sd)**d*b**(d/k)/
            (2**(d/2)*math.gamma(d/2+1)))


def run():
    rg=np.random.default_rng(20261014)
    alpha=.9; ki=.3; kp=.1; k=ki+kp
    for d in (1,2,4,8):
        lam=1.5; g=.7; h=.3
        x=np.linspace(-.2,.3,d)
        sd=lam*g*h**1.5/2
        tol=sd/alpha
        mu,sd,nc,b=params(d,lam,g,h,x,tol,alpha,ki,kp,alpha)
        N=400_000
        Z=rg.standard_normal((N,d))
        noise=g*math.sqrt(h)*Z
        first_step=-lam*h*x+noise
        euler=x+first_step
        heun=x+first_step-(lam*h/2)*first_step
        discrepancy=euler-heun
        expected_mu=-(lam**2*h**2/2)*x
        expected=expected_mu+sd*Z
        assert np.max(np.abs(discrepancy-expected))<1e-12
        err=np.linalg.norm(discrepancy,axis=1)/(tol*math.sqrt(d))
        raw=b/err**k
        capped=np.minimum(5.0,np.maximum(0.2,raw))
        assert np.all((capped>=.2)&(capped<=5))
        for threshold in (1.1, 1.5, 2.0, 5.0):
            empirical=np.mean(raw>threshold)
            expected_prob=exact_survival(threshold,d,sd,nc,b,tol,k)
            stderr=math.sqrt(max(expected_prob*(1-expected_prob),1e-8)/N)
            assert abs(empirical-expected_prob)<6*stderr+0.001, (d,threshold,empirical,expected_prob)
        C=asymptotic_coefficient(d,sd,nc,b,tol,k)
        for t in (10.,100.,1000.):
            exact=exact_survival(t,d,sd,nc,b,tol,k)
            assert exact>0
            ratio=exact*t**(d/k)/C
            assert abs(ratio-1)<.045, (d,t,ratio)
        print('d',d,'df',d,'noncentrality',round(nc,6),
              'upper_clip_probability',f'{exact_survival(5,d,sd,nc,b,tol,k):.12e}',
              'tail_exponent',d/k)
    # Test the rate convergence in the central, equilibrium-normalized case.
    from scipy.stats import chi2
    kk=.4
    for highcap in (1.2, 1.4):
        z=highcap**(-2/kk)
        predicted=(z-1-math.log(z))/2
        observed=-chi2.logcdf(800*z,800)/800
        assert np.isfinite(observed) and abs(observed-predicted)<.006, (highcap,observed,predicted)
    print('PASS: 16 Gaussian conditional CDF checks, 4 Heun identities, 12 tail asymptotic checks')

if __name__=='__main__':run()
