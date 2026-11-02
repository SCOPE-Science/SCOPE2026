#!/usr/bin/env python3
"""Independent exact checks for the conditional last-preference shape theorem.

Requires only Python >= 3.10; no network or external data.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb, exp, log1p, sqrt


def weights(n):
    return [comb(n - 1, s) * (n - s) ** max(0, n - s - 2) *
            (s + 1) ** max(0, s - 1) for s in range(n)]


def law(n, p):
    w = weights(n)
    h = (n + 1) ** (n - 1)
    return [Fraction(2, n + 1) -
            (p * sum(w[n - j + 1:]) + (1 - p) * sum(w[:n - j])) / h
            for j in range(1, n + 1)]


def direct(n, p):
    @lru_cache(None)
    def finish(preferences, i, used):
        if i == n:
            return Fraction(1)
        pref = preferences[i]
        if pref not in used:
            return finish(preferences, i + 1, tuple(sorted((*used, pref))))
        forward = next((k for k in range(pref + 1, n + 1) if k not in used), None)
        backward = next((k for k in range(pref - 1, 0, -1) if k not in used), None)
        return ((p * finish(preferences, i + 1, tuple(sorted((*used, forward))))
                 if forward is not None else Fraction(0)) +
                ((1 - p) * finish(preferences, i + 1, tuple(sorted((*used, backward))))
                 if backward is not None else Fraction(0)))
    successes = [Fraction(0) for _ in range(n)]
    for preferences in product(range(1, n + 1), repeat=n):
        successes[preferences[-1] - 1] += finish(preferences, 0, ())
    total = sum(successes)
    assert total == (n + 1) ** (n - 1)
    return [v / total for v in successes]


def phi(k):
    return Fraction(k + 1, k) ** (k - 1)


def min_position(n, p):
    q = law(n, p)
    return {j + 1 for j, v in enumerate(q) if v == min(q)}


def do():
    assertions = 0
    examined = 0
    for n in range(2, 7):
        w = weights(n)
        for s in range(1, n):
            assert Fraction(w[s], w[s-1]) == phi(s) / phi(n-s)
            assertions += 1
        thresholds = [phi(j) / (phi(j) + phi(n-j)) for j in range(1,n)]
        assert all(thresholds[i] < thresholds[i+1] for i in range(len(thresholds)-1))
        assertions += 1
        for p in [Fraction(0),Fraction(1,5),Fraction(1,3),Fraction(1,2),
                  Fraction(2,3),Fraction(4,5),Fraction(1)]:
            exact = law(n, p)
            observed = direct(n,p)
            examined += n**n
            assert exact == observed, (n,p,exact,observed)
            assertions += n
            assert sum(exact)==1 and all(x>0 for x in exact)
            assertions += 2
            for j in range(1,n):
                expected_delta = ((1-p)*w[n-j-1]-p*w[n-j]) / (n+1)**(n-1)
                assert exact[j]-exact[j-1] == expected_delta
                assertions += 1
            if p != Fraction(1,2):
                if p < Fraction(1,2):
                    assert exact[-1]>exact[0]
                else:
                    assert exact[0]>exact[-1]
                assertions += 1
            for i in range(1,n):
                assert ((exact[i]-exact[i-1] > 0) == (p < thresholds[i-1])) if p != thresholds[i-1] else (exact[i]==exact[i-1])
                assertions += 1

    for n in range(7, 81):
        w = weights(n)
        for s in range(1,n):
            assert Fraction(w[s],w[s-1]) == phi(s) / phi(n-s)
            assertions += 1
        thresholds = [phi(j)/(phi(j)+phi(n-j)) for j in range(1,n)]
        assert all(thresholds[i]<thresholds[i+1] for i in range(n-2))
        assertions += 1
        for j in range(1,n):
            assert thresholds[j-1]+thresholds[n-j-1]==1
            assertions += 1

    for n in [500,1000,5000]:
        tt = [exp((j-1)*log1p(1/j)) for j in range(1,n+1)]
        for t in [-5,-1,0,1,5]:
            p = .5 + t/n
            jj = 1 + sum(tt[j-1]/(tt[j-1]+tt[n-j-1]) < p for j in range(1,n))
            u = .5 + t/(sqrt(2.25+4*t*t)+1.5)
            assert abs(jj/n-u)< .045, (n,t,jj/n,u)
            assertions+=1
    print('PASS:', assertions, 'assertions; direct enumerated preference vectors:',examined)

if __name__=='__main__':
    do()
