#!/usr/bin/env python3
"""Exact-rational finite consistency checks for mass-weighted short-cycle maximal variation.
The analytic coarea proof, not these finite checks, establishes the theorem.
"""
from fractions import Fraction
from itertools import product
from math import isclose

def variation(values):
    n = len(values)
    return sum(abs(values[i] - values[(i + 1) % n]) for i in range(n))

def maximal(values, weights):
    n = len(values)
    out = []
    for i in range(n):
        averages = []
        for radius in range(n // 2 + 1):
            ball = [j for j in range(n) if min((j-i) % n, (i-j) % n) <= radius]
            averages.append(sum((weights[j]*values[j] for j in ball), Fraction(0)) / sum(weights[j] for j in ball))
        out.append(max(averages))
    return out

def run():
    checks=0
    delta_checks=0
    for n in (3,4,5):
        for wt in product((1,2,3), repeat=n):
            w = tuple(Fraction(x) for x in wt)
            total=sum(w)
            lower=min(w)
            constant=1-lower/total
            for i in range(n):
                v=[Fraction(int(j==i)) for j in range(n)]
                gained=variation(maximal(v,w))/variation(v)
                if gained != 1-w[i]/total: raise AssertionError(('delta',n,wt,i,gained))
                delta_checks+=1
            for ftuple in product((0,1,2),repeat=n):
                f=tuple(Fraction(x) for x in ftuple)
                v=variation(f)
                if not v: continue
                Mf=maximal(f,w)
                avg=sum((w[i]*f[i] for i in range(n)),Fraction(0))/total
                assert variation(Mf) <= v - 2*(avg-min(f)), ('additive', n,wt,ftuple)
                assert variation(Mf) <= constant*v, ('constant',n,wt,ftuple)
                checks+=1
            witnesses=[i for i,x in enumerate(w) if x==lower]
            assert all(variation(maximal([Fraction(int(i==j)) for i in range(n)],w)) == 2*constant for j in witnesses)
    print(f'PASS: {checks} nonconstant exact-rational profiles; {delta_checks} exact delta ratios.')

if __name__=='__main__':
    run()
