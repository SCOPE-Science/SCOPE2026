"""Reproduce conditional singleton-count laws at nonuniform coupon coverage.

Usage: python coupon_singletons_check.py
Requires: Python 3 and scipy for the optional independent integral test.
"""
from fractions import Fraction
from functools import lru_cache
from math import expm1, isclose
from random import Random

checks = 0

def check(cond, description):
    global checks
    assert cond, description
    checks += 1


def poisson_binomial(qs):
    a = [1.0]
    for q in qs:
        b = [0.0] * (len(a) + 1)
        for k, v in enumerate(a):
            b[k] += v * (1.0 - q)
            b[k + 1] += v * q
        a = b
    return a


def qvector(probs, t):
    return [p*t / expm1(p*t) for p in probs]


def conditional_pmf(probs, t):
    qs = qvector(probs, t)
    a = poisson_binomial(qs)
    Q = sum(qs)
    return [0.0] + [s*a[s]/Q for s in range(1, len(a))]


def winner_mixture_pmf(probs, t):
    qs = qvector(probs, t)
    Q = sum(qs)
    a = [0.0] * (len(qs)+1)
    for i, qi in enumerate(qs):
        law = poisson_binomial(qs[:i] + qs[i+1:])
        for j, v in enumerate(law):
            a[j+1] += (qi/Q)*v
    return a


def exact_discrete_stopping_law(ps):
    """Independent rational recursion on 0/1/at-least-two occupancies."""
    m = len(ps)
    @lru_cache(None)
    def F(state):
        if all(s != 0 for s in state):
            v = [Fraction(0)]*(m+1)
            v[sum(s == 1 for s in state)] = Fraction(1)
            return tuple(v)
        hold = sum(p for p,s in zip(ps,state) if s == 2)
        out = [Fraction(0)]*(m+1)
        for i,(p,s) in enumerate(zip(ps,state)):
            if s == 2:
                continue
            st = list(state)
            st[i] += 1
            sub = F(tuple(st))
            for k,v in enumerate(sub):
                out[k] += p*v
        return tuple(v/(1-hold) for v in out)
    return F((0,)*m)


def continuous_joint_probability(probs, singleton_count):
    from scipy.integrate import quad
    def integrand(t):
        qs = qvector(probs,t)
        coverage = 1.0
        for p in probs:
            coverage *= -expm1(-p*t)
        density = coverage * sum(p/expm1(p*t) for p in probs)
        pmf = poisson_binomial(qs)
        return density * singleton_count * pmf[singleton_count]/sum(qs)
    val,err = quad(integrand, 0, 600.0, epsabs=3e-11, epsrel=1e-10, limit=250)
    return val,err


def main():
    rng = Random(19371)
    for m in range(2,9):
        for case in range(40):
            w = [rng.uniform(.3, 2.0) for _ in range(m)]
            ps = [v/sum(w) for v in w]
            for t in (.15, 1.0, 3.0, 9.0, 25.0):
                a = conditional_pmf(ps,t)
                b = winner_mixture_pmf(ps,t)
                check(isclose(sum(a),1.0,abs_tol=2e-12), (m,case,t,'normalization'))
                for j in range(m+1):
                    check(isclose(a[j], b[j], abs_tol=2e-12), (m,case,t,j,'mixture'))
            for t1,t2 in ((.1,.2),(.2,1.0),(1.0,3.0),(3.0,10.0)):
                a,b = conditional_pmf(ps,t1),conditional_pmf(ps,t2)
                check(all(a[j]*b[j+1] <= a[j+1]*b[j]+1e-13 for j in range(1,m)),(m,case,t1,t2,'MLR'))
                check(any(a[j]*b[j+1] < a[j+1]*b[j]-1e-14 for j in range(1,m)),(m,case,t1,t2,'strict MLR'))
                for j in range(2,m+1):
                    check(sum(a[j:])>=sum(b[j:])-1e-12,(m,case,j,'tail'))
    families = (
        (Fraction(1,2),Fraction(1,3),Fraction(1,6)),
        (Fraction(1,2),Fraction(1,4),Fraction(1,8),Fraction(1,8)),
        (Fraction(2,5),Fraction(1,5),Fraction(1,5),Fraction(1,5)),
        (Fraction(1,3),Fraction(1,3),Fraction(1,3)),
    )
    for ps in families:
        exact = exact_discrete_stopping_law(ps)
        rate = [float(p) for p in ps]
        for s in range(1,len(ps)+1):
            v,err=continuous_joint_probability(rate,s)
            check(abs(v-float(exact[s])) < 4e-9, (ps,s,v,exact[s],err))
        check(sum(exact)==1,(ps,'sum'))
    print(f'PASS: {checks} assertions; exact recursion and independent numerical integration included')

if __name__ == '__main__':
    main()
