#!/usr/bin/env python3
"""Reproducible numerical checks for the Haff-cooling reset covariance theorem.
Only the Python standard library is needed. Numerical checks support, not replace,
the analytical proof of the infinite-lag and all-derivative statements.
"""
import math


def simpson(fn, b=40.0, n=6000):
    assert n % 2 == 0
    h = b / n
    terms = [fn(0.0) + fn(b)]
    terms.extend((4 if i % 2 else 2) * fn(i * h) for i in range(1, n))
    return math.fsum(terms) * h / 3.0


def close(a, b, rtol=1e-7, atol=1e-13):
    assert math.isfinite(a) and math.isfinite(b), (a, b)
    assert abs(a-b) <= atol+rtol*max(abs(a),abs(b)), (a, b, abs(a-b))


def exp_age_expect(fn, r):
    return simpson(lambda z: math.exp(-z)*fn(z/r))


def temp(age, T0, tau, exponent):
    return T0*(1.0 + age/tau)**(-exponent)


def mean(r, tau, T0, q):
    return exp_age_expect(lambda a: temp(a,T0,tau,q), r)


def mean_derivative(r,tau,T0,q):
    return exp_age_expect(lambda a: (1.0/r-a)*temp(a,T0,tau,q), r)


def covariance_unreset_scaled(lag, r, tau, T0, q):
    m=mean(r,tau,T0,q)
    f0=temp(lag,T0,tau,q)
    return exp_age_expect(
        lambda a:(temp(a,T0,tau,q)-m)*(temp(a+lag,T0,tau,q)-f0),r)


def gamma_spectral_q2_scaled(lag, r, tau, T0):
    # Inverse-Laplace gamma-mixture representation for exponent q=2.
    # Each gamma rate is z/tau where z has density z exp(-z).
    limit=36.0
    n=1600
    h=limit/n
    nodes=[i*h for i in range(n+1)]
    weights=[(1 if i in (0,n) else (4 if i%2 else 2))*h/3 for i in range(n+1)]
    score=0.0
    for z,wz in zip(nodes,weights):
        if z==0.0: continue
        lam=z/tau
        outer=wz*z*math.exp(-z-lag*lam)
        inner=0.0
        for y,wy in zip(nodes,weights):
            if y==0.0: continue
            eta=y/tau
            kernel=r*lam*eta/((r+lam+eta)*(r+lam)*(r+eta))
            inner+=wy*y*math.exp(-y)*kernel
        score+=outer*inner
    return T0*T0*score


def expint_E1(x):
    # E1(x)=integral_x^infty exp(-y)/y dy; substitute y=x+z.
    return math.exp(-x)*simpson(lambda z:math.exp(-z)/(x+z))


def run():
    checks=0
    r,tau,T0,q=0.7,1.2,1.0,2.0
    m=mean(r,tau,T0,q)
    mp=mean_derivative(r,tau,T0,q)
    x=r*tau
    E1=expint_E1(x)
    close(m,T0*x*(1-x*math.exp(x)*E1),rtol=1e-7);checks+=1
    close(mp,T0*tau*(1+x-(x*x+2*x)*math.exp(x)*E1),rtol=1e-7);checks+=1
    assert 0<m<T0 and mp>0;checks+=1
    for lag in (0.,0.2,1.,3.,8.):
        direct=covariance_unreset_scaled(lag,r,tau,T0,q)
        spec=gamma_spectral_q2_scaled(lag,r,tau,T0)
        close(direct,spec,rtol=6e-5); checks+=1
        assert direct>0; checks+=1
    # Exact stationary marginal variance, given by primary source's one-time moments.
    var=exp_age_expect(lambda age:temp(age,T0,tau,q)**2,r)-m*m
    close(covariance_unreset_scaled(0.,r,tau,T0,q),var,rtol=1e-7);checks+=1
    # Strict complete monotonicity checked by finite differences for low orders.
    # Infinite-order statement is established in the written spectral proof.
    h=0.05
    f=lambda s: math.exp(-r*s)*covariance_unreset_scaled(s,r,tau,T0,q)
    for n in range(1,5):
        for t in (0.3,1.0,3.0):
            finite_diff=sum(((-1)**k)*math.comb(n,k)*f(t+(n-k)*h) for k in range(n+1))
            assert ((-1)**n)*finite_diff > 1e-12,(n,t,finite_diff)
            checks+=1
    # The effective logarithmic relaxation rate strictly decreases to r.
    def eff(t):
        h=0.004
        return -(math.log(f(t+h))-math.log(f(t-h)))/(2*h)
    lam=[eff(t) for t in (0.3,1.0,3.0,12.0,80.0)]
    assert all(lam[i]>lam[i+1]>r for i in range(len(lam)-1)),lam
    checks+=1
    K=q*T0*(tau**q)*mp
    for t,tol in ((80.,0.14),(250.,0.06),(1000.,0.017)):
        scaled=covariance_unreset_scaled(t,r,tau,T0,q)
        ratio=scaled/(K*t**(-q-1))
        assert abs(ratio-1)<tol,(t,ratio)
        checks+=1
    # A noninteger cooling exponent: second independent parameter domain check.
    for q in (0.7,3.5):
        mp=mean_derivative(0.9,0.8,2.0,q)
        assert mp>0
        for t in (0.,0.1,1.,7.):
            assert covariance_unreset_scaled(t,0.9,0.8,2.0,q)>0
            checks+=1
        checks+=1
    print(f'PASS: {checks} numerical assertions; q=2 mean, spectral covariance, derivative signs, asymptotic coefficient; q noninteger positivity.')


if __name__=='__main__':
    run()
