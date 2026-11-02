#!/usr/bin/env python3
"""Exact checks for the frontier-growth root-degree law on a biclique."""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import comb, exp, pi, sqrt

checks = 0

def insist(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)


def birthday_weights(n):
    survival = Fraction(1)
    ans = {}
    for k in range(1, n + 1):
        survival *= Fraction(n - k + 1, n)
        ans[k] = survival * Fraction(k, n)
    return ans


def predicted_degree(n):
    ans = defaultdict(Fraction)
    for k, p in birthday_weights(n).items():
        m = n-k
        for j in range(m+1):
            ans[k+j] += p * Fraction(comb(m,j), 2**m)
    return dict(ans)


def exact_frontier(n):
    # Independent construction: enumerate ALL boundary-edge choices at every state.
    # The graph has two hubs 0,1 and n peripherals numbered 2,...,n+1.
    edges = [(i,j) for i in (0,1) for j in range(2,n+2)]
    full = (1 << (n+2))-1

    @lru_cache(None)
    def f(mask, root_degree):
        if mask == full:
            return {root_degree: Fraction(1)}
        boundary = [(i,j) for i,j in edges if bool(mask & (1<<i)) != bool(mask & (1<<j))]
        assert boundary
        p = Fraction(1, len(boundary))
        out = defaultdict(Fraction)
        for i,j in boundary:
            m2 = mask | (1<<i) | (1<<j)
            d2 = root_degree + int(i==0 or j==0)
            for d,q in f(m2,d2).items():
                out[d] += p*q
        return dict(out)
    return f(1<<0, 0)


def ust_degree(n):
    # Structural enumeration of all n*2^(n-1) trees:
    # one bridging peripheral (two incident edges), every other peripheral
    # chooses its incident hub independently and uniformly.
    return {d:Fraction(comb(n-1,d-1),2**(n-1)) for d in range(1,n+1)}

for n in range(1,9):
    pk = birthday_weights(n)
    pred = predicted_degree(n)
    enumer = exact_frontier(n)
    ust = ust_degree(n)
    insist(sum(pk.values())==1, f'birthday normalization n={n}')
    insist(sum(pred.values())==1, f'predict normalization n={n}')
    insist(sum(enumer.values())==1, f'enumer normalization n={n}')
    for d in range(1,n+1):
        insist(pred.get(d,0)==enumer.get(d,0), f'degree exact n={n} d={d}')
    # Compare both means to distinct finite computations.
    muK = sum(Fraction(k)*p for k,p in pk.items())
    muD = sum(Fraction(d)*p for d,p in enumer.items())
    insist(muD == Fraction(n,2)+muK/2, f'mean n={n}')
    varK = sum(Fraction(k*k)*p for k,p in pk.items())-muK**2
    varD = sum((Fraction(d)-muD)**2*p for d,p in enumer.items())
    insist(varD == (Fraction(n)-muK+varK)/4, f'variance n={n}')
    insist(sum(ust.values())==1, f'UST normalization n={n}')
    for threshold in range(1,n+1):
        fgreedy = sum(p for d,p in pred.items() if d<=threshold)
        fust = sum(p for d,p in ust.items() if d<=threshold)
        insist(fgreedy<=fust, f'stoch dominance n={n} threshold={threshold}')

# Verify the birthday-tail recurrence separately for every k via survival sums.
for n in range(1,70):
    pk = birthday_weights(n)
    s = Fraction(1)
    for k in range(1,n+1):
        s *= Fraction(n-k+1,n)
        insist(sum(p for j,p in pk.items() if j>=k)==s, f'tail n={n} k={k}')

# Asymptotic diagnostic comparisons only; analytical proof is in RESULT.md.
for n in (100,1000,10000):
    surv=1.0
    mean=0.0
    second=0.0
    for k in range(1,n+1):
        surv *= (n-k+1)/n
        mean += surv
        second += (2*k-1)*surv
        if surv<1e-250:
            break
    variance=second-mean*mean
    insist(abs(mean/sqrt(n)-sqrt(pi/2))<0.15, f'Rayleigh mean n={n}')
    insist(abs(variance/n-(4-pi)/2)<0.15, f'Rayleigh variance n={n}')

print(f'PASS: {checks} exact/computational assertions')
print('Proof limits: finite enumeration is diagnostic; the all-n law follows from the boundary-edge decomposition.')
