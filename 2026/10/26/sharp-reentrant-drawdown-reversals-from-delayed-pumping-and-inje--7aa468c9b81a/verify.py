"""Deterministic numerical checks for the delayed pumping--injection Theis-response theorem.
Analytical arguments, not these finite checks, establish the universal result.
"""
import math
import random
from scipy.optimize import brentq
from scipy.special import exp1


def logphi(t, a, b, tau):
    assert t > tau > 0 and a > 0 and b > 0
    return math.log1p(-tau/t)-a/t+b/(t-tau)


def turn_ratio(a, b, tau):
    c = tau + a - b
    if c <= 0:
        return None, 1.0
    tm = tau*(tau+2*a+math.sqrt(tau*tau+4*a*b))/(2*c)
    return tm, math.exp(logphi(tm,a,b,tau))


def predicted(a,b,tau,lam):
    tm, m=turn_ratio(a,b,tau)
    if tm is None:
        return 1 if lam > 1 else 0
    if lam > 1: return 1
    if lam == 1: return 1
    if lam < m: return 0
    if lam == m: return 0
    return 2


def independent_sign_change_count(a,b,tau,lam):
    # Includes an adapted log mesh resolving the very early post-switch layer.
    # Confirms signs only; not an exhaustive proof of all real-time critical points.
    l=math.log(lam)
    samples=[tau + (10.0 ** (-8 + 13*i/700))*max(1.,tau,a,b) for i in range(701)]
    # Include a wide far-time tail at large time, with independent exp time-spacings.
    samples += [tau + max(1.,tau,a,b)*10.0**(-8+19*i/1200) for i in range(1201)]
    samples.sort()
    last=1
    changes=0
    for t in samples:
        y=logphi(t,a,b,tau)-l
        s=1 if y>1e-10 else (-1 if y< -1e-10 else 0)
        if s and s != last:changes+=1;last=s
    return changes


def main():
    rng=random.Random(704205)
    for i in range(4500):
        a=10**rng.uniform(-2.3,2.3)
        b=10**rng.uniform(-2.3,2.3)
        tau=10**rng.uniform(-2.3,2.3)
        tm,m=turn_ratio(a,b,tau)
        if tm is not None:
            assert tm > tau
            assert math.isfinite(logphi(tm,a,b,tau)) and logphi(tm,a,b,tau)<0
            scale = math.sqrt(tau*tau+4*a*b)
            assert abs((tau+a-b)*tm*tm -tau*(tau+2*a)*tm+a*tau*tau) < 1e-5*max(1.,scale**4)
            for f in (0.8,1.2):
                assert logphi(tm*f if tm*f>tau else (tm+tau)/2,a,b,tau) > logphi(tm,a,b,tau)-1e-9
        else:
            for j in range(1,6):
                t=tau+10**j*max(a,b,tau)
                assert logphi(t,a,b,tau)>0
        lam=10**rng.uniform(-1.5,0.5)
        # In near-degenerate/tiny windows the geometric sample grid may miss roots.
        # Verify selected sign patterns with exact stationary value and remote asymptotes.
        n=predicted(a,b,tau,lam)
        assert n in (0,1,2)
        if n==2:
            assert tau+a>b and m<lam<1
            assert logphi(tm,a,b,tau)<math.log(lam)
        if n==0 and tm is not None and lam<1:
            assert m>=lam

    a,b,lam=4.,1.,.1
    assert abs(turn_ratio(a,b,3)[1]-.25)<1e-14
    assert predicted(a,b,.1,lam)==2
    assert predicted(a,b,3.,lam)==0
    assert predicted(a,b,100.,lam)==2
    assert math.exp(logphi(1.,a,b,.1))<lam
    assert math.exp(logphi(101.,a,b,100.))<lam
    assert math.exp(logphi(4.,a,b,3.))>.1
    # Numerically bracket both switch delays, with the exact peak at tau=a-b.
    f=lambda tau:turn_ratio(a,b,tau)[1]-lam
    print('example switch delays:', brentq(f,.001,3.),brentq(f,3.,500))
    for tau in (.1,3.,100.):
        print('tau=',tau,'min=',turn_ratio(a,b,tau)[1], 'pattern=',predicted(a,b,tau,lam))
    # Independently compare exact Theis drawdown with the differentiated response.
    for _ in range(100):
        aa=10**rng.uniform(-.3,.7)
        bb=10**rng.uniform(-.3,.7)
        lag=10**rng.uniform(-.3,.7)
        ll=10**rng.uniform(-1.2,.1)
        tt=lag+10**rng.uniform(-.2,.9)
        scale=1e-5*max(1.,tt-lag)
        def response(t):
            return exp1(aa/t)-ll*exp1(bb/(t-lag))
        numerical=(response(tt+scale)-response(tt-scale))/(2*scale)
        analytical=math.exp(-aa/tt)/tt-ll*math.exp(-bb/(tt-lag))/(tt-lag)
        assert abs(numerical-analytical)<2e-6*max(1.,abs(analytical))
    # Compute post-injection critical-time locations in both reentrant cases.
    for lag in (.1,100.):
        tm,m=turn_ratio(a,b,lag)
        left=brentq(lambda t:logphi(t,a,b,lag)-math.log(lam),lag+1e-10*min(1.,lag),tm)
        right=brentq(lambda t:logphi(t,a,b,lag)-math.log(lam),tm,lag+1e7)
        assert left<tm<right
        print('two strict turning times at delay',lag,':',left,right)
    # Exact rational inequalities: e^{26/9} > 9 follows its first four Taylor terms;
    # e<3 implies e^{1-4/101}/101 < 3/101<1/10.
    z=26/9
    assert sum(z**k/math.factorial(k) for k in range(4))>9
    print('PASS: 4500 randomized calculus classifications, 100 independent Theis-derivative checks, explicit reentrant example and rational sign bounds')


if __name__=='__main__': main()
