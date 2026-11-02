"""Independent numerical consistency checks for stationary reset-modulus covariance.

Requires Python 3.10+ and scipy.  The proof is analytic; these checks are finite.
"""
from math import pi, sqrt, asin, expm1, log1p, isfinite
from scipy.integrate import quad
from scipy.special import gamma


def h(q):
    assert 0 <= q <= 1
    # Algebraically identical to sqrt(1-q*q)+q*asin(q)-1,
    # but avoids subtractive cancellation for small q.
    return q*asin(q)-q*q/(1+sqrt(1-q*q))


def terms(beta, t, rate=1., K=1.):
    assert 0 < beta < 2 and t > 0 and rate > 0 and K > 0
    b=beta/2
    mean=gamma(b+1)/rate**b

    def age_integrand(u):
        a=u/rate
        z=t**b*expm1(b*log1p(a/t))
        return (a**b-mean)*z*__import__('math').exp(-u)

    def intrinsic_integrand(u):
        a=u/rate
        q=(a/(a+t))**b
        return (a**b)*((a+t)**b)*h(q)*__import__('math').exp(-u)

    age=quad(age_integrand,0,100,epsabs=1e-13,epsrel=1e-12,limit=350)[0]
    intrinsic=quad(intrinsic_integrand,0,100,epsabs=1e-13,epsrel=1e-12,limit=350)[0]
    factor=4*K/pi
    return factor*age,factor*intrinsic


def asymptotic(beta, rate=1., K=1.):
    b=beta/2
    age=4*K/pi*b*b*gamma(1+b)/rate**(1+b)
    intrinsic=2*K/pi*gamma(1+3*b)/rate**(3*b)
    if beta < 1: return intrinsic,-b
    if beta > 1: return age,b-1
    return age+intrinsic,-.5


def run():
    checks=0
    def check(condition, msg):
        nonlocal checks
        assert bool(condition),msg
        checks+=1

    # A separate integration representation: the unconditioned bivariate
    # folded-Gaussian moment minus the product of the two conditional means.
    def direct(beta,t,r=1.,K=1.):
        b=beta/2
        m=gamma(b+1)/r**b
        def integrand(u):
            a=u/r
            q=(a/(a+t))**b
            joint=(a*(a+t))**b*(1+h(q))
            return (joint-m*(a+t)**b)*__import__('math').exp(-u)
        return 4*K/pi*quad(integrand,0,100,epsabs=1e-12,epsrel=1e-12,limit=350)[0]

    for beta in (.25,.5,.8,1.,1.2,1.6,1.9):
        for t in (.3,2.,8.):
            age,within=terms(beta,t)
            d=direct(beta,t)
            check(age>0 and within>0, f'positive decomposition {beta},{t}')
            check(abs(age+within-d) <= 4e-9*max(1.,abs(d)),f'direct identity {beta},{t}: {age+within} vs {d}')

    for beta in (.4,.8,1.,1.2,1.6):
        rate=1.3;K=.7
        coeff,power=asymptotic(beta,rate,K)
        ratios=[]
        for t in (200,2000,20000):
            age,within=terms(beta,t,rate,K)
            ratio=(age+within)/(coeff*t**power)
            ratios.append(ratio)
            check(isfinite(ratio) and .5<ratio<2.2, f'asymptotic ratio {beta},{t}')
        # At larger time the magnitude of deviation decreases.
        check(abs(ratios[-1]-1)<abs(ratios[0]-1),f'convergence {beta}')
        print(f'beta={beta:.1f}: scaled covariance / leading term = '+', '.join(f'{z:.8f}' for z in ratios))

    for t in (100,2000,20000):
        age,within=terms(1.,t)
        check(abs(age/(age+within)-.25)<.002, 'critical one-quarter age fraction')

    # Analytic constants at beta=1: total 2K/(sqrt(pi)*r**(3/2)).
    coeff,power=asymptotic(1.,1.,1.)
    check(abs(coeff-2/sqrt(pi)) < 2e-14 and power == -.5,'critical coefficient')
    # h(q)/q^2 approaches 1/2 and is strictly positive.
    for q in (.0001,.01,.1,.5,.9,.999):
        check(h(q)>0,'h positivity')
    check(abs(h(.0001)/(.0001**2)-.5)<1e-8,'small-correlation coefficient')
    print(f'All {checks} finite numerical and identity checks passed.')

if __name__=='__main__':run()
