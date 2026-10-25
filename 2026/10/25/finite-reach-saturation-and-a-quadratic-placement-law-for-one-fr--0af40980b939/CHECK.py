"""Numerical spot checks for an exact one-aerator oxygen-sag theorem.

Only the theorem's analytic proof establishes global optimality.
Run: python3 CHECK.py (Python standard library only).
"""
import math
import random


def bisect(fun, lo, hi, steps=100):
    flo, fhi = fun(lo), fun(hi)
    if not (flo < 0 < fhi):
        raise ValueError(('missing bracket', lo, hi, flo, fhi))
    for _ in range(steps):
        mid = (lo + hi) / 2
        if fun(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def construct(a, b, q, L0):
    c = a * L0 / (b - a)
    t0 = math.log(b / a) / (b - a)
    g = lambda t: c * (math.exp(-a*t) - math.exp(-b*t))
    A = lambda s: q + (1-q) * math.exp((b-a)*s)
    h = lambda s: t0 + math.log(A(s))/(b-a)
    m = lambda s: g(t0) * A(s)**(-a/(b-a))
    si = bisect(lambda s: g(s)-m(s), 0, t0)
    tc = h(si)
    def s_opt(T):
        if T >= tc:
            return si
        return bisect(lambda s: g(s)*(1+(1-q)*math.exp(-b*(T-s)))-g(T),
                      0, min(T,t0))
    def risk(T,s):
        pre = g(min(s,t0))
        post_peak = max(s,min(T,h(s)))
        post = c*(math.exp(-a*post_peak)-A(s)*math.exp(-b*post_peak))
        return max(pre,post)
    return g, m, h, si, tc, s_opt, risk


def test():
    a,b,q,L0 = 1,2,.5,1
    g,m,h,si,tc,opt,risk = construct(a,b,q,L0)
    assert abs(si-math.log(math.sqrt(2))) < 1e-12
    assert abs(tc-math.log(1+math.sqrt(2))) < 1e-12
    assert abs(g(si)-(math.sqrt(2)-1)/2)<1e-12
    for T in [1e-6,1e-5,1e-4]:
        assert abs(opt(T)/T-1/(2-q)) < 1e-4
    J = (g(si+1e-6)-g(si-1e-6)-m(si+1e-6)+m(si-1e-6))/2e-6
    coeff = a*b*g(si)/(2*J)
    assert abs(coeff-.5)<1e-7
    assert abs((si-opt(tc-.001))/.001**2-coeff)<.001
    random.seed(1729)
    for _ in range(200):
        a=10**random.uniform(-1,1)
        b=a*(1+10**random.uniform(-2,1))
        q=random.uniform(.01,.99)
        L0=10**random.uniform(-1,1)
        g,m,h,si,tc,opt,risk=construct(a,b,q,L0)
        T=tc*random.uniform(.03,1.8)
        s=opt(T)
        val=risk(T,s)
        for j in range(101):
            candidate=risk(T,j*T/100)
            assert val <= candidate + 2e-11*(1+candidate), (a,b,q,L0,T,s,val,candidate)
    print('PASS: 200 randomized 101-point placement scans, exact example, endpoint checks')


if __name__=='__main__':
    test()
