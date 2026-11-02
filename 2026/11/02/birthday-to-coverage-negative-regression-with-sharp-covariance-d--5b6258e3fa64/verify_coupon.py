"""Exact checks for first-collision versus complete-coupon-collection dependence.

The finite computations use rational arithmetic. The separate large-size
floating-point diagnostic illustrates, but does not prove, the limit theorem.
Run: python verify_coupon.py (Python 3 standard library only).
"""
from fractions import Fraction as F
from math import factorial, sqrt, pi

CHECK_COUNT = 0

def check(condition, explanation=''):
    global CHECK_COUNT
    CHECK_COUNT += 1
    if not condition:
        raise AssertionError(explanation or 'Verification condition failed')


def harmonic(k):
    return sum((F(1, j) for j in range(1, k + 1)), F(0))


def birthday_distribution(m):
    check(m >= 2)
    survival = F(1)
    result = {}
    for t in range(2, m + 1):
        survival *= F(m - t + 2, m)
        result[t] = survival * F(t - 1, m)
    result[m + 1] = survival / m
    check(sum(result.values()) == 1, 'First-collision probabilities fail to sum to one')
    check(result[m + 1] == F(factorial(m), m**m), 'Endpoint birthday mass')
    return result


def expected_waiting_after_k_seen(m):
    # Separate backward dynamic program, derived from the occupancy transitions.
    h = [F(0) for _ in range(m + 1)]
    for k in range(m - 1, -1, -1):
        h[k] = F(m, m - k) + h[k + 1]
        check(h[k] == 1 + F(k,m)*h[k] + F(m-k,m)*h[k+1],
              'First-step expected residual waiting time')
    return h


def exact_covariance(m):
    pmf = birthday_distribution(m)
    h = expected_waiting_after_k_seen(m)
    conditional_mean = {t:(F(t) + h[t-1] if t <= m else F(m))
                        for t in range(2, m + 2)}
    eb = sum((t*p for t,p in pmf.items()), F(0))
    ec = sum((p*conditional_mean[t] for t,p in pmf.items()), F(0))
    ebc = sum((t*p*conditional_mean[t] for t,p in pmf.items()), F(0))
    check(ec == m*harmonic(m), 'Unconditional coupon-collection mean')
    for t in range(2,m+1):
        check(conditional_mean[t] > conditional_mean[t+1],
              'Strict conditional mean reversal')
    covariance = ebc-eb*ec
    check(covariance < 0, 'Covariance must be negative')
    return covariance


def collection_cdfs(m, horizon):
    # Distribution-level occupancy Markov DP, independent of the mean formula.
    cdf = [[F(0)]*(horizon+1) for _ in range(m+1)]
    for s in range(horizon+1):
        cdf[m][s] = F(1)
    for s in range(1,horizon+1):
        for k in range(m-1,-1,-1):
            cdf[k][s] = (F(k,m)*cdf[k][s-1]
                         + F(m-k,m)*cdf[k+1][s-1])
    return cdf


def finite_checks():
    exact_reference = [F(-1,2),F(-8,9),F(-37,32),F(-844,625)]
    for m in range(2,37):
        result=exact_covariance(m)
        if m<=5:
            check(result==exact_reference[m-2], 'Boundary covariance table')
    for m in range(2,9):
        states=collection_cdfs(m,70)
        def conditional_cdf(b,cutoff):
            if b==m+1:
                return F(int(cutoff>=m))
            residual=cutoff-b
            return F(0) if residual<0 else states[b-1][residual]
        for b in range(2,m+1):
            saw_strict=False
            for cutoff in range(0,71):
                delta=conditional_cdf(b+1,cutoff)-conditional_cdf(b,cutoff)
                check(delta>=0,'Conditional CDFs do not satisfy stochastic ordering')
                saw_strict |= delta>0
            check(saw_strict,'Stochastic ordering is not strict')


def large_size_diagnostic(m):
    # Stable covariance using g(B)=m H_m+1-D(B) minus a rare endpoint.
    survive=1.0
    eb=ed=ebd=0.0
    decrement=0.0
    for b in range(2,m+1):
        survive *= (m-b+2)/m
        prob = survive*(b-1)/m
        if b>=3:
            decrement += (b-2)/(m-b+2)
        if prob < 1e-250:
            break
        eb += b*prob
        ed += decrement*prob
        ebd += b*decrement*prob
    # The omitted endpoint correction has probability m!/m^m and is
    # exponentially small at the large m used below.
    return -(ebd-eb*ed)/sqrt(m)

if __name__=='__main__':
    finite_checks()
    target=-sqrt(pi/8)
    for m,tolerance in ((100,0.002),(1000,0.0002),(10000,0.00003)):
        estimate=large_size_diagnostic(m)
        check(abs(estimate-target)<tolerance,'Asymptotic diagnostic tolerance')
        print('m=',m,'normalized covariance=',estimate,'target=',target)
    print('PASS:',CHECK_COUNT,'explicitly counted verification checks')
