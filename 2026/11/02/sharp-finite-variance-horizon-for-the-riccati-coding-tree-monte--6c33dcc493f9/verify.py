"""Reproducibility checks for the exact Riccati coding-tree second moments.

Run with Python >=3.9: python verify.py
Uses only the standard library. All infinite statements require the accompanying proof.
"""
from math import exp, expm1, log, log1p, sqrt, isfinite, isclose
from random import Random

SQ2 = sqrt(2.0)
KAPPA = log(3.0 + 2.0 * SQ2) / (2.0 * SQ2)
Q = 3.0 - 2.0 * SQ2

def bisect(fn, lo, hi, iterations=100):
    assert fn(lo) * fn(hi) < 0
    for _ in range(iterations):
        mid = (lo + hi) / 2
        if fn(lo) * fn(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2

ZSTAR = bisect(lambda z: 2.0*(1.0 - 1.0/z) - log(z), 3.0, 6.0)

def horizon(a, lam):
    return log1p(KAPPA * (lam/a)**2) / lam

def exact(a, lam, t):
    x = expm1(lam*t) / (lam*lam)
    b = 2.0 * SQ2 * a * a
    r = Q * exp(b*x)
    assert r < 1
    f = (b*b/2.0) * r / ((1-r)**2)
    c = b * (1+r) / (1-r)
    return exp(lam*t)*f, exp(lam*t)*c, 4.0*exp(lam*t)

def rhs(a, lam, t, y):
    i, f, c = y
    return (lam*i + f/lam,
            lam*f + f*c/lam,
            lam*c + 4.0*exp(lam*t)*f/lam)

def rk4(a, lam, t, n=6000):
    h=t/n
    y=(a*a, a**4, 4*a*a)
    for j in range(n):
        x=j*h
        k1=rhs(a,lam,x,y)
        k2=rhs(a,lam,x+h/2,tuple(y[k]+h*k1[k]/2 for k in range(3)))
        k3=rhs(a,lam,x+h/2,tuple(y[k]+h*k2[k]/2 for k in range(3)))
        k4=rhs(a,lam,x+h,tuple(y[k]+h*k3[k] for k in range(3)))
        y=tuple(y[k]+h*(k1[k]+2*k2[k]+2*k3[k]+k4[k])/6 for k in range(3))
    return y

def simulate(code, t, a, lam, rng):
    """Direct independent exponential-clock tree, with depth limited only for tests."""
    if t <= 0:
        return (a, a*a, 2*a, 2.0, 0.0)[code]
    remaining=t
    stack=[(code,remaining)]
    product=1.0
    count=0
    while stack:
        code,remaining=stack.pop()
        count+=1
        assert count<50000, "abnormally large tree in finite test"
        tau=rng.expovariate(lam)
        if tau >= remaining:
            product *= (a,a*a,2*a,2.0,0.0)[code] * exp(lam*remaining)
        else:
            product /= lam * exp(-lam*tau)
            rem=remaining-tau
            if code==0: stack.append((1,rem))
            elif code==1:stack.extend(((1,rem),(2,rem)))
            elif code==2:stack.extend(((1,rem),(3,rem)))
            elif code==3:stack.extend(((1,rem),(4,rem)))
            else:stack.extend(((1,rem),(4,rem)))
        if product==0: return 0.0
    return product

def test():
    assert 0.62322<KAPPA<0.62323
    assert 4.92155<ZSTAR<4.92156
    opt_rate=sqrt((ZSTAR-1)/KAPPA)
    opt_horizon=sqrt(KAPPA)*log(ZSTAR)/sqrt(ZSTAR-1)
    assert 2.50845<opt_rate<2.50847
    assert 0.63530<opt_horizon<0.63531
    assert isclose(horizon(1,opt_rate),opt_horizon,rel_tol=1e-13)
    # Stationarity equation is the exact derivative, and the endpoint is a maximum.
    for ratio in [0.03,0.2,0.8,1.1,1.7,2.4,3.0,4.0,8.0,25.0,100.0]:
        assert horizon(1,ratio) <= opt_horizon*(1+3e-15)
    checks=0
    for a in [0.4,0.7,1.0,1.7,3.0]:
        for ratio in [0.2,0.7,1.0,2.0,4.0]:
            lam=ratio*a
            for frac in [0.05,0.3,0.65,0.85]:
                t=frac*horizon(a,lam)
                I,F,C=rk4(a,lam,t,n=3000)
                F0,C0,B0=exact(a,lam,t)
                assert isclose(F,F0,rel_tol=3e-8), (a,lam,t,F,F0)
                assert isclose(C,C0,rel_tol=3e-8), (a,lam,t,C,C0)
                assert I>exp(lam*t)*a*a
                assert I >= (a/(1-a*t))**2 - 1e-7
                assert isfinite(B0)
                checks+=3
    # Monte Carlo is an independent tree-level sanity check, never a proof.
    rng=Random(130729)
    a=1.0;lam=2.0;t=0.18
    vals=[simulate(0,t,a,lam,rng) for _ in range(80000)]
    m=sum(vals)/len(vals)
    v=sum(v*v for v in vals)/len(vals)
    I=rk4(a,lam,t,n=3000)[0]
    assert abs(m-a/(1-a*t)) < 0.035, m
    assert abs(v-I)/I < 0.09, (v,I)
    checks+=2
    # First-moment benchmark: source ODE is defined until 1/a, but L2 never that far.
    for a in [0.25,0.5,1,2,4]:
        assert horizon(a,a*opt_rate)<1/a
        assert isclose(horizon(a,a*opt_rate)*a,opt_horizon,rel_tol=1e-13)
        checks+=2
    print('PASS', checks, 'independent ODE / tree-sampling / optimization checks')
    print('kappa:',format(KAPPA,'.15g'))
    print('zstar:',format(ZSTAR,'.15g'))
    print('optimal rate per initial value:',format(opt_rate,'.15g'))
    print('maximal finite-variance time times initial value:',format(opt_horizon,'.15g'))
    print('first-moment solution at t=0.5 for a=1:',2.0)
    print('second-moment horizon at lambda=1, a=1:',horizon(1,1))
if __name__=='__main__':
    test()
