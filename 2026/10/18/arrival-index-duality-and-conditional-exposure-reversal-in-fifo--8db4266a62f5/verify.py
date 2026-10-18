"""Standalone scientific checks for the FIFO overlap identity and M/D/1 formulas."""
import math
import numpy as np


def counts(arrivals, departures, ell):
    n = len(arrivals)
    before = [0] * n
    after = [0] * n
    for i in range(n):
        for j in range(i):
            if departures[j] - arrivals[i] > ell:
                before[i] += 1
                after[j] += 1
    return before, after


def check_exact_paths():
    # Exhaust many finite monotone arrival sequences and FIFO service sequences.
    from itertools import product
    assertions = 0
    for gaps in product((1, 2, 3), repeat=4):
        for services in product((1, 2, 4), repeat=5):
            arr = [0]
            for gap in gaps:
                arr.append(arr[-1] + gap)
            dep = []
            for a, svc in zip(arr, services):
                dep.append(max(a, dep[-1] if dep else a) + svc)
            for ell in (0, 0.5, 1, 2, 3.5, 6):
                b, f = counts(arr, dep, ell)
                n = len(arr)
                for i in range(n):
                    for k in range(1, i + 1):
                        assert (b[i] >= k) == (f[i-k] >= k)
                        assertions += 1
    return assertions


def risk_before(t, p, ell):
    if t == 1:
        return 0.
    m = math.floor(t - 1)
    r = t - 1 - m
    assert 0 < r < 1
    b = m + int(r > ell)
    return 1 - (1-p) ** b


def risk_after(t, lam, p, ell):
    return -math.expm1(-lam*p*(t-ell))


def exact_unconditional(lam, p, ell):
    s = lam*p
    laplace = (1-lam)*p / (p-1+math.exp(-s))
    return 1-math.exp(-s*(1-ell))*laplace


def check_conditional_reversal():
    num=0
    for lam,p,ell in ((.2,.1,.1),(.7,.4,.3),(.9,.8,.7),(.95,.3,.8)):
        a=-math.log1p(-p)
        critical=(2*a-lam*p*ell)/(a-lam*p)
        assert critical>2
        for t in (1,1+ell/3,1+ell*.8):
            assert risk_before(t,p,ell)==0
            assert risk_after(t,lam,p,ell)>0
            num+=2
        for t in (critical+.1,critical+1.23,critical+10.7):
            # Avoid accidental integral times at which one formula is handled by continuity.
            if abs(t-round(t))<1e-10:
                t+=.001
            assert risk_before(t,p,ell)>risk_after(t,lam,p,ell)
            num+=1
        pr=exact_unconditional(lam,p,ell)
        assert 0<pr<1
        num+=1
    return num


def check_simulation():
    rng = np.random.default_rng(473921)
    n=550000
    lam,p,ell=.7,.4,.3
    arr=np.cumsum(rng.exponential(1/lam,n))
    dep=np.empty(n)
    last=0.
    for i in range(n):
        last=max(last,arr[i])+1
        dep[i]=last
    ids=np.arange(2000,n-2000)
    # The number of previous departures strictly after a+ell.
    b=ids-np.searchsorted(dep,arr[ids]+ell,side='right')
    b=np.maximum(b,0)
    f=np.searchsorted(arr,dep[ids]-ell,side='left')-ids-1
    f=np.maximum(f,0)
    estimate_before=np.mean(1-(1-p)**b)
    estimate_after=np.mean(1-(1-p)**f)
    exact=exact_unconditional(lam,p,ell)
    assert abs(estimate_before-exact)<.006
    assert abs(estimate_after-exact)<.006
    assert abs(estimate_before-estimate_after)<.0005
    return exact,estimate_before,estimate_after


if __name__=='__main__':
    a=check_exact_paths()
    b=check_conditional_reversal()
    e,x,y=check_simulation()
    print('exact pathwise rank assertions:',a)
    print('conditional risk assertions:',b)
    print('M/D/1 risk (closed form / before / after):',e,x,y)
    print('All checks passed; finite tests do not replace the proof.')
