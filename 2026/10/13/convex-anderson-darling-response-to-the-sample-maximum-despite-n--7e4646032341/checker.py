"""Separate finite diagnostics for Anderson-Darling / uniform-maximum identities.

Uses Python standard library only. Finite tests supplement the analytic proof.
"""
from fractions import Fraction
from math import log, log1p, isclose
from random import Random


def harmonic(k):
    return sum((Fraction(1, j) for j in range(1, k+1)), Fraction())


def mean_closed(n, t):
    assert n >= 1 and 0.0 < t < 1.0
    L = log1p(-t)
    J1 = t + (1 - t) * L
    J2 = -t-L
    return ((n-1)*J1+(n-1-n*t)**2*J2)/(n*t*t) + n*(-1-log(t)+t)


def beta_log_v(n, k, t, terms=500):
    """E log(1-t V), V ~ Beta(k,n-k), using beta moments."""
    assert 1 <= k <= n and 0 < t < 1
    if k == n:
        return log1p(-t)
    current = 1.0
    partial = 0.0
    tr = 1.0
    for r in range(1, terms+1):
        current *= (k+r-1)/(n+r-1)
        tr *= t
        partial -= tr*current/r
    return partial


def mean_order_stats(n, t):
    """Separate expression from ordered-sample Anderson-Darling log formula."""
    base = -n-n*log(t)
    for j in range(1, n):
        base -= (2*j-1)/n*float(harmonic(j-1)-harmonic(n-1))
    for k in range(1, n+1):
        base -= (2*n+1-2*k)/n*beta_log_v(n,k,t)
    return base


def cov_closed(n):
    return (Fraction(2*n,1)-Fraction(n+1,1)*harmonic(n))/(n*(n+1)**2)


def cov_rank_moments(n):
    """Separate order-statistic beta covariance calculation (exact fractions)."""
    tot = Fraction(0)
    for j in range(1, n+1):
        cov_log_order = Fraction(1,(n+1)**2)
        k = n+1-j
        cov_log_compl = -Fraction(k,(n-k+1)*(n+1)**2)
        tot -= Fraction(2*j-1,n)*(cov_log_order+cov_log_compl)
    return tot


def ad_sample(values):
    u=sorted(values)
    n=len(u)
    return -n-sum((2*j-1)*(log(u[j-1])+log1p(-u[n-j])) for j in range(1,n+1))/n


def run():
    condition_count=0
    for n in range(1,21):
        for t in (.07,.25,.5,.8,.9):
            a=mean_closed(n,t)
            b=mean_order_stats(n,t)
            assert isclose(a,b,rel_tol=1e-10,abs_tol=2e-10),(n,t,a,b)
            condition_count+=1
    moments_count=0
    for n in range(1,501):
        assert cov_closed(n)==cov_rank_moments(n),n
        if n==1:
            assert cov_closed(n)==0
        else:
            assert cov_closed(n)<0
        moments_count+=1
    rng=Random(19107)
    mc_count=0
    for n in (1,2,4,8):
        for t in (.25,.6,.85):
            draws=14000
            av=0.0
            for _ in range(draws):
                sample=[t*rng.random() for i in range(n-1)]+[t]
                av+=ad_sample(sample)
            av/=draws
            theoretical=mean_closed(n,t)
            assert abs(av-theoretical)<.09,(n,t,av,theoretical)
            mc_count+=1
    print('VERIFY_OK conditional_beta_series=',condition_count,'exact_beta_covariances=',moments_count,'seeded_conditional_cases=',mc_count)
    for n in (1,2,3,4,10,20):
        print('n=',n,'covariance=',cov_closed(n),'g(0.5)=',round(mean_closed(n,.5),10))

if __name__=='__main__':
    run()
