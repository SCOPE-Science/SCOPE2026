#!/usr/bin/env python3
"""Independent finite checks for the stated symmetric-star hitting-time design theorem.

The mathematical proof in RESULT.md, rather than these finite checks,
establishes the statement for all positive real prices and all star sizes.
"""
from fractions import Fraction
from math import isclose, sqrt
import random


def gauss(A, b):
    n = len(b)
    a = [list(row)+[b[i]] for i, row in enumerate(A)]
    for j in range(n):
        piv = next(i for i in range(j, n) if a[i][j] != 0)
        a[j], a[piv] = a[piv], a[j]
        z = a[j][j]
        a[j] = [v/z for v in a[j]]
        for i in range(n):
            if i != j:
                z = a[i][j]
                a[i] = [x-z*y for x, y in zip(a[i], a[j])]
    return [row[-1] for row in a]


def independent_hitting_times(r, target):
    k = len(r)
    Q = [[Fraction(0) for _ in range(k+1)] for _ in range(k+1)]
    for i, rate in enumerate(r, start=1):
        Q[0][i] = Q[i][0] = rate
        Q[0][0] -= rate
        Q[i][i] -= rate
    others = [s for s in range(k+1) if s != target]
    A = [[-Q[i][j] for j in others] for i in others]
    solution = gauss(A, [Fraction(1)]*k)
    out = [Fraction(0)]*(k+1)
    for i, h in zip(others, solution):
        out[i] = h
    return out


def optimum(prices, budget):
    k = len(prices)
    p = max(prices)
    P = sum(prices)-p
    if p <= k*P:
        rate = budget/(p+P)
        return [rate]*k, (k+1)*(p+P)/budget
    h = prices.index(p)
    t = sqrt(p/(k*P))
    rates = [budget/(P+p/t)]*k
    rates[h] = budget/(p+P*t)
    value = (k*p+P+2*sqrt(k*p*P))/budget
    return rates, value


def objective(rates):
    k = len(rates)
    return max(1/rates[i]+k/rates[j] for i in range(k) for j in range(k) if i != j)


def main():
    rng = random.Random(20261031)
    checks = 0
    for k in range(3, 9):
        for sample in range(20):
            r = [Fraction(rng.randrange(1, 40), rng.randrange(1, 20)) for _ in range(k)]
            for t in range(k+1):
                actual = independent_hitting_times(r,t)
                for s in range(k+1):
                    if s == t:
                        expected = Fraction(0)
                    elif t == 0:
                        expected = 1/r[s-1]
                    elif s == 0:
                        expected = k/r[t-1]
                    else:
                        expected = 1/r[s-1]+k/r[t-1]
                    assert actual[s] == expected, (k,s,t,r,actual[s],expected)
                    checks += 1
    for k in range(3, 11):
        for sample in range(150):
            prices = [10**rng.uniform(-2, 3) for _ in range(k)]
            if sample % 9 == 0:
                prices = [1.0]*k
            if sample % 9 == 1:
                prices[0] = (k*sum(prices[1:]))*(1+10**rng.uniform(-8, -2))
            if sample % 9 == 2:
                prices[0] = (k*sum(prices[1:]))*(1-10**rng.uniform(-8, -2))
            budget = 10**rng.uniform(-2,2)
            rates, value = optimum(prices,budget)
            assert all(rate > 0 for rate in rates)
            assert isclose(sum(p*r for p,r in zip(prices,rates)),budget,rel_tol=1e-12)
            assert isclose(objective(rates),value,rel_tol=1e-12)
            checks += 3
            for trial in range(200):
                competitor = [10**rng.uniform(-3,3) for _ in range(k)]
                scale = budget/sum(p*r for p,r in zip(prices,competitor))
                competitor = [r*scale for r in competitor]
                assert objective(competitor)>=value*(1-1e-10)
                checks += 1
    print('VERIFY_OK', checks, 'checks; exact rational hitting systems and finite optimization probes')

if __name__ == '__main__':
    main()
