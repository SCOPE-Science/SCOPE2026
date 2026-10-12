"""Exact-rational verification of cover time / terminal singleton covariance.

Runs independent finite-state first-step equations for capped coupon counts.
This is finite verification, not a substitute for the all-parameter proof.
"""
from fractions import Fraction
from itertools import product
from functools import lru_cache
from math import prod


def exact_moments(weights):
    p = tuple(Fraction(a, sum(weights)) for a in weights)
    n = len(p)
    assert n >= 2 and all(x > 0 for x in p) and sum(p) == 1

    @lru_cache(None)
    def rec(state):
        if all(s > 0 for s in state):
            return Fraction(0), Fraction(sum(s == 1 for s in state)), Fraction(0)
        loop = sum(p[i] for i in range(n) if state[i] == 2)
        children = []
        for i in range(n):
            if state[i] < 2:
                nxt = list(state)
                nxt[i] += 1
                children.append((p[i], rec(tuple(nxt))))
        den = 1 - loop
        en = (1 + sum(w*v[0] for w,v in children)) / den
        es = sum(w*v[1] for w,v in children) / den
        ens = (sum(w*(v[1]+v[2]) for w,v in children) + loop*es) / den
        return en, es, ens

    en, es, ens = rec((0,)*n)
    return en, es, ens, ens-en*es


def uniform_formula(n):
    h = sum((Fraction(1,k) for k in range(1,n+1)), Fraction(0))
    h2 = sum((Fraction(1,k*k) for k in range(1,n+1)), Fraction(0))
    return n*h,h,n*(h2-h)


def verify():
    cases=0
    for n in range(2,6):
        for w in product((1,2,3), repeat=n):
            # Remove copies that differ only by relabelling.
            if tuple(sorted(w))!=w:
                continue
            en, es, ens, cov=exact_moments(w)
            assert cov < 0, (w,cov)
            assert ens==en*es+cov
            if len(set(w))==1:
                q=uniform_formula(n)
                assert (en,es,cov)==q, (w,(en,es,cov),q)
            cases+=1
    for w in ((1,29),(1,1,98),(1,2,97),(1,2,3,94),(7,13,17,23,41),
              (1,1,1,1,96),(1,1,1,1,1,95)):
        assert exact_moments(w)[3]<0, w
        cases+=1
    print(f'PASS: {cases} exact rational state-space cases; zero failures.')
    for w in ((1,1),(1,2),(1,1,1),(1,2,3)):
        en,es,ens,cov=exact_moments(w)
        print(f'weights={w}, E[N]={en}, E[S]={es}, Cov={cov}')

if __name__=='__main__': verify()
