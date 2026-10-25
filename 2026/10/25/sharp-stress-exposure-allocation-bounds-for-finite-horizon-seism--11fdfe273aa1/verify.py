"""Reproduce finite-horizon Dieterich-model stress-allocation checks.

Standard library only. Randomized finite tests are diagnostics, not a proof.
"""
from math import exp, expm1, log1p, sqrt
from random import Random


def clip(x, lo, hi):
    return min(hi, max(lo, x))


def budget_dimensionless(c, q, s_cap):
    p = lambda z: max(0.0, z)**2
    return (p(c) - p(c-q) - p(c-s_cap) + p(c-s_cap-q))/2.0


def minimizer_parameter(T, a, s_cap, budget):
    q, b = T/a, budget/a
    lo, hi = 0.0, s_cap+q
    for _ in range(100):
        mid = (lo+hi)/2
        if budget_dimensionless(mid,q,s_cap) < b:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def bounds(T, a, s_cap, budget, background_rate=1.0):
    q, b = T/a, budget/a
    c = minimizer_parameter(T,a,s_cap,budget)
    u, v = clip(c-s_cap,0,q), clip(c,0,q)
    jmin_over_a = exp(s_cap)*expm1(u) + exp(c)*(v-u) + exp(q)-exp(v)
    jmax_over_a = expm1(q)+expm1(s_cap)*(exp(q)-exp(q-b/s_cap))
    return c, background_rate*a*log1p(jmin_over_a), background_rate*a*log1p(jmax_over_a)


def piecewise_count(profile,T,a,background_rate=1.0):
    n=len(profile); step=T/n
    # Exact time integral for every piecewise constant stress segment.
    v=1.0
    for i,level in enumerate(profile):
        left=i*step/a; right=(i+1)*step/a
        v += exp(level+left)*expm1(step/a)
    kernel_count = background_rate*a*__import__('math').log(v)
    # Independently propagate the seismicity-state ODE and integrate R(t).
    gamma=1.0; old_level=0.0; count=0.0
    for level in profile:
        gamma *= exp(old_level-level)
        count += background_rate*a*__import__('math').log((exp(step/a)+gamma-1.0)/gamma)
        gamma=1+(gamma-1)*exp(-step/a)
        old_level=level
    assert abs(count-kernel_count)<2e-9*(1+abs(kernel_count))
    return kernel_count


def run():
    T,a,s_cap,budget = 2.0,1.0,1.5,2.0
    c,n_min,n_max=bounds(T,a,s_cap,budget)
    assert abs(c-(3.5-sqrt(2)))<2e-13
    assert abs(budget_dimensionless(c,T/a,s_cap)-budget/a)<1e-12
    assert abs(n_min-2.7697692817085997)<2e-12
    assert abs(n_max-3.270862688849766)<2e-12
    assert n_min<T<n_max or T<n_min<n_max
    rng=Random(180597)
    checked=0
    for k in range(600):
        T=0.3+3.7*rng.random()
        a=0.4+2.0*rng.random()
        s_cap=0.4+2*rng.random()
        fraction=0.06+0.88*rng.random()
        budget=T*s_cap*fraction
        c,lower,upper=bounds(T,a,s_cap,budget)
        assert 0<c<s_cap+T/a
        assert abs(budget_dimensionless(c,T/a,s_cap)-budget/a)<2e-11
        n=60
        vals=[rng.random()*2-1 for _ in range(n)]
        # Shift-and-clip a random vector to the exact fixed stress-time budget.
        lo,hi=-5*s_cap,5*s_cap
        for _ in range(80):
            mid=(lo+hi)/2
            avg=sum(clip(s_cap*(x+mid),0,s_cap) for x in vals)/n
            if avg<s_cap*fraction:lo=mid
            else:hi=mid
        levels=[clip(s_cap*(x+(lo+hi)/2),0,s_cap) for x in vals]
        assert abs(sum(levels)/n-s_cap*fraction)<1e-10
        got=piecewise_count(levels,T,a)
        assert lower-5e-9<=got<=upper+5e-9,(k,lower,got,upper)
        checked+=1
    print('VERIFICATION_OK; exact example C=',3.5-sqrt(2),
          '; N_min=',2.7697692817085997,
          '; N_max=',3.270862688849766,
          '; randomized feasible protocols=',checked,
          '; ODE-vs-kernel consistency checked')

if __name__=='__main__':
    run()
