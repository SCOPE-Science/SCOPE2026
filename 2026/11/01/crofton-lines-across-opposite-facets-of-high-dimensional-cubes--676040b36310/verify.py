"""Reproducible checks for the Crofton opposite-facet chord formulas.

Numerical checks support the analytic proof; no finite test certifies an asymptotic statement.
Run: python verify.py (requires numpy and scipy).
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import erf

MU = math.sqrt(2.0 / math.pi)


def F(x):
    if x <= 0:
        return 0.0
    return math.erf(x / math.sqrt(2.0)) - MU * (-math.expm1(-x*x/2)) / x


def saddle_scale(d):
    m = d-1
    q = (MU*m)**(1.0/3.0)
    action = 1.5*q*q + 0.5*MU*q + MU*MU/6.0
    return q,action


def saddle_integral(d, polynomial_power=0):
    """Return exp(action)*integral x exp(-x*x/2) F(x)^(d-1) (x-q)^power dx."""
    m = d-1
    q, action = saddle_scale(d)
    def f(s):
        x = q+s
        if x <= 0:
            return 0.0
        fx=F(x)
        if fx <= 0:
            return 0.0
        return (s**polynomial_power)*x*math.exp(-x*x/2 +m*math.log(fx)+action)
    low=-q
    return quad(f,low,max(18.0, q+12.0),epsabs=1e-9,epsrel=1e-9,limit=200)[0]


def p_exact(d):
    return math.exp(-saddle_scale(d)[1])*saddle_integral(d)


def p_asymptotic(d):
    q, action=saddle_scale(d)
    return math.sqrt(2*math.pi/3)*q*math.exp(-action)


def crofton_monte_carlo(d, trials=200000, seed=42):
    """Sample true isotropic affine lines conditioned on meeting [0,1]^d.

    Haar direction is acceptance-weighted by projection volume. Conditional on
    direction choose the entry facet with weights |u_i|, then choose a uniform
    point on this facet and trace the chord to its exit facet.
    """
    rng=np.random.default_rng(seed+d)
    events=0
    accepted=0
    batch=25000
    while accepted<trials:
        vectors=rng.normal(size=(batch,d))
        vectors/=np.linalg.norm(vectors,axis=1)[:,None]
        vabs=np.abs(vectors)
        cond=rng.random(batch)*math.sqrt(d) <vabs.sum(axis=1)
        u=vectors[cond]
        if len(u)==0:continue
        if len(u)>trials-accepted:u=u[:trials-accepted]
        accepted+=len(u)
        a=np.abs(u)
        rand=rng.random(len(u))*a.sum(axis=1)
        i=(np.cumsum(a,axis=1)<rand[:,None]).sum(axis=1)
        chosen=a[np.arange(len(u)),i]
        slopes=a/chosen[:,None]
        starts=rng.random(size=(len(u),d))
        ok=np.all((starts+np.where(u>=0,slopes,-slopes)>=0)&
                  (starts+np.where(u>=0,slopes,-slopes)<=1)
                  |(np.arange(d)[None,:]==i[:,None]),axis=1)
        events+=int(ok.sum())
    return events/trials


def main():
    assert abs(p_exact(2) - (math.sqrt(2)-1))<2e-12
    assert F(1)>0 and 0<F(6)<1
    for d in [2,3,5,10]:
        p=p_exact(d)
        observed=crofton_monte_carlo(d,trials=180000)
        standard_error=math.sqrt(p*(1-p)/180000)
        assert abs(observed-p) < 6*standard_error+0.0005, (d,p,observed)
        print(f'd={d}: exact={p:.10g}, independent Crofton-line MC={observed:.10g}')
    ratios=[]
    for d in [100,300,1000,5000,20000]:
        ratio=saddle_integral(d)/ (math.sqrt(2*math.pi/3)*saddle_scale(d)[0])
        z=saddle_integral(d)
        mean=saddle_integral(d,1)/z
        var=saddle_integral(d,2)/z-mean*mean
        ratios.append(ratio)
        print(f'd={d}: asymptotic ratio={ratio:.7f}, conditional saddle mean={mean:.6f}, variance={var:.6f}')
        assert 0.90 < ratio < 1.12
    assert all(ratios[i]>ratios[i+1] for i in range(len(ratios)-1))
    assert abs(ratios[-1]-1)<0.01
    print('ALL_CROFTON_HYPERCUBE_CHECKS_PASSED')

if __name__=='__main__':main()
