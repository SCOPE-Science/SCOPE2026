#!/usr/bin/env python3
"""Independent integral, Bessel, and collective-Fock checks of quantum reset purity."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ive, erfcx
from scipy.stats import poisson


def purity_bessel(z, alpha):
    """Exact purity, z=4 n a^2 m omega/hbar; alpha=r/omega."""
    if z < 0 or alpha <= 0:
        raise ValueError('requires z>=0 and alpha>0')
    if z == 0:
        return 1.0
    cap = max(100, int(16 * math.sqrt(z) + 60))
    k = np.arange(1, cap+1)
    return float(ive(0, z) + np.sum(2*ive(k,z)*alpha**2/(alpha**2+k**2)))


def purity_integral(z, alpha):
    """One-period Laplace integral of two independent exponential ages."""
    weight = alpha/(-math.expm1(-2*math.pi*alpha))
    f = lambda t: math.exp(-alpha*t - z*(1-math.cos(t)))
    left = quad(f, 0, math.pi, epsabs=3e-12, epsrel=3e-12, limit=200)[0]
    right = quad(f, math.pi, 2*math.pi, epsabs=3e-12, epsrel=3e-12, limit=200)[0]
    return weight*(left+right)


def purity_fock(z, alpha):
    """Direct collective-number-basis trace: Fock population is Poisson(z/2)."""
    x = z/2
    cap = max(40, int(x+14*math.sqrt(x+1)+25))
    ks = np.arange(cap)
    prob = poisson.pmf(ks,x)
    diffs = ks[:,None]-ks[None,:]
    return float(np.sum(np.outer(prob, prob)*(alpha**2/(alpha**2+diffs**2))))


def fixed_rate_constant(alpha):
    return math.sqrt(math.pi/2)*alpha/math.tanh(math.pi*alpha)


def critical_profile(c):
    return c*math.sqrt(math.pi/2)*erfcx(c/math.sqrt(2))


def check():
    checked=0
    for b in (0.45,1.4):
        for n in (1,2,4,9):
            z=b*n
            for alpha in (0.3,1.7,4.5):
                u=purity_integral(z,alpha)
                v=purity_bessel(z,alpha)
                w=purity_fock(z,alpha)
                assert abs(u-v)<3e-10,(z,alpha,u,v)
                assert abs(u-w)<3e-10,(z,alpha,u,w)
                assert 0<u<1,(z,alpha,u)
                checked+=3
    for z in (0.25,1.3,15,210):
        vals=[purity_bessel(z,alpha) for alpha in (0.2,0.6,1.5,5.0,10.0)]
        assert all(vals[i]<vals[i+1] for i in range(len(vals)-1)),(z,vals)
        checked+=4
    for b in (0.25,0.8,2.0):
        for alpha in (0.5,2.3):
            p1=purity_bessel(b,alpha)
            for n in (2,5,20):
                assert purity_bessel(b*n,alpha) > p1**n
                checked+=1
    for alpha in (0.35,1.4,3.1):
        qs=[purity_bessel(z,alpha)*math.sqrt(z)/fixed_rate_constant(alpha) for z in (1600,6400,25600)]
        assert abs(1-qs[-1]) < abs(1-qs[0]),(alpha,qs)
        assert abs(1-qs[-1]) < 0.03,(alpha,qs)
        checked+=2
    for c in (0.4,1.0,2.0):
        goal=critical_profile(c)
        vals=[purity_bessel(z,c*math.sqrt(z)) for z in (400,1600,6400)]
        assert abs(goal-vals[-1])<abs(goal-vals[0]),(c,goal,vals)
        assert abs(goal-vals[-1]) < 0.018,(c,goal,vals)
        checked+=2
    z=18000
    assert purity_bessel(z,1.5)<0.03
    assert purity_bessel(z,100*math.sqrt(z))>0.999
    checked+=2
    print('PASS:',checked,'analytical identity, positivity, ordering, and asymptotic checks')
    for alpha in (0.35,1.4):
        z=6400
        print('fixed-rate',alpha,'purity=',purity_bessel(z,alpha),'asymptotic=',fixed_rate_constant(alpha)/math.sqrt(z))
    for c in (0.4,1,2):
        z=6400
        print('crossover',c,'finite=',purity_bessel(z,c*math.sqrt(z)),'limit=',critical_profile(c))

if __name__=='__main__':
    check()
