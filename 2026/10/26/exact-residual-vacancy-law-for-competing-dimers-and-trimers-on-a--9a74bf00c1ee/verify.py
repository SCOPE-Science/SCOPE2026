#!/usr/bin/env python3
"""Finite consistency tests for competitive 2-site/3-site RSA on a complete substrate.
All checks are supporting computations; the infinite-volume statement is proved analytically.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, exp, pi, sqrt, log


def reduced(n, lam):
    x = [Fraction(0), Fraction(1), Fraction(0)]
    for k in range(3, n + 1):
        q = Fraction(3, 1) / (3 + lam * (k - 2))
        x.append(q*x[k-2] + (1-q)*x[k-3])
    return x


def labelled(n, lam):
    @lru_cache(None)
    def f(mask):
        sites = tuple(i for i in range(n) if mask & (1 << i))
        k = len(sites)
        if k <= 1:
            return Fraction(k)
        z = Fraction(comb(k, 2)) + lam*comb(k, 3)
        numerator = Fraction(0)
        for grp in combinations(sites, 2):
            nxt = mask ^ sum(1 << i for i in grp)
            numerator += f(nxt)
        for grp in combinations(sites, 3):
            nxt = mask ^ sum(1 << i for i in grp)
            numerator += lam*f(nxt)
        return numerator/z
    return f((1 << n)-1)


def kfun(t):
    # K'(t)=t/(1+t+t^2) and K(0)=0
    from math import atan
    return 0.5*log(1+t+t*t) - (atan((2*t+1)/sqrt(3))-pi/6)/sqrt(3)


def numerical_limit(lam):
    import mpmath as mp
    mp.mp.dps = 50
    lam=mp.mpf(str(lam)); alpha=3/lam; aa=alpha-1
    def K(t):
        return mp.log(1+t+t*t)/2 - (mp.atan((2*t+1)/mp.sqrt(3))-mp.pi/6)/mp.sqrt(3)
    if aa > 0:
        B=aa*mp.quad(lambda t: t**(aa-1)*mp.exp(-alpha*K(t)), [0,1])
    elif aa == 0:
        B=mp.mpf(1)
    else:
        B=1+aa*mp.quad(lambda t: t**(aa-1)*mp.expm1(-alpha*K(t)), [0,1])
    return mp.exp(alpha*K(1))*B/3


def run():
    tests=0
    for lam in [Fraction(1,2), Fraction(1), Fraction(3,2), Fraction(3), Fraction(5)]:
        r=reduced(120,lam)
        for n in range(2,10):
            assert labelled(n,lam) == r[n], ('label',n,lam)
            tests+=1
        for k in range(0,119):
            def at(j): return r[j] if j>=0 else Fraction(0)
            lhs=lam*k*at(k) - lam*(k-3)*at(k-3) + (3-2*lam)*at(k) -3*at(k-2) -lam*at(k-3)
            rhs=(3-lam) if k==1 else 0
            assert lhs==rhs, ('ode',k,lam,lhs,rhs)
            tests+=1
    for lam,expected in [(0.2,0.4920534966322707),(1,0.4662381863691282),
                         (2,0.4432135747348162),(3,0.4267290381001358),
                         (5,0.4049633676467166),(10,0.3784298754566748)]:
        v=numerical_limit(lam)
        assert abs(float(v)-expected)<8e-15, (lam,v)
        tests+=1
    l3=exp((0.5*log(3)-pi/(6*sqrt(3))))/3
    assert abs(l3-float(numerical_limit(3)))<1e-14
    tests+=1
    for lam in [0.5,1,2,3]:
        x=[0.,1.,0.]
        for n in range(3,250001):
            q=3/(3+lam*(n-2))
            x.append(q*x[-2]+(1-q)*x[-3])
        estimate=sum(x[-3:])/3
        tol={0.5:2e-5,1:2e-5,2:2e-5,3:2e-5}[lam]
        assert abs(estimate-float(numerical_limit(lam)))<tol,(lam,estimate)
        tests+=1
    print(f'PASS: {tests} exact labelled-state / generating-function / high-precision / asymptotic checks')
    for l in [0.2,1,2,3,5,10]:
        print('lambda',l,'limit',numerical_limit(l))

if __name__=='__main__': run()
