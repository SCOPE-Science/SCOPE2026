#!/usr/bin/env python3
"""Independent numerical and exact-arithmetic checks for a Hill-inhibition allocation theorem.

The analytic proof is in RESULT.md; finite tests do not certify all real parameters.
No external dependencies, network, or environmental data are needed.
"""
from fractions import Fraction
from itertools import product
from math import exp, log1p
import random


def partitions(total, slots):
    if slots == 1:
        yield (total,)
    else:
        for i in range(total + 1):
            for rest in partitions(total-i, slots-1):
                yield (i,) + rest


def exact_check():
    count = 0
    for h in (2, 3, 4):
        for n in (2, 3, 4):
            for grid_total in range(1, 23):
                budget = Fraction(grid_total, 4)
                candidates = [(1 + (budget / k) ** h) ** k for k in range(1,n+1)]
                predicted = max(candidates)
                for comp in partitions(grid_total, n):
                    actual = Fraction(1)
                    for v in comp:
                        actual *= (1 + Fraction(v, 4) ** h)
                    assert actual <= predicted, (h, n, grid_total, comp, actual, predicted)
                    count += 1
    return count


def positive_peak(h):
    def F(z):
        return h * z ** h / (1 + z ** h) - log1p(z ** h)
    lo, hi = 0.01, 2.0
    while F(lo) <= 0:
        lo /= 2.0
    while F(hi) >= 0:
        hi *= 2.0
    for _ in range(120):
        mid = (lo + hi) / 2
        if F(mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def t_boundaries(h, n):
    z = positive_peak(h)
    result = []
    for k in range(1, n):
        # Difference between the normalized values of adjacent equal-support strategies.
        def d(t):
            return log1p((t / k) ** h) / (t / k) - log1p((t / (k+1)) ** h) / (t / (k+1))
        a,b = k*z,(k+1)*z
        assert d(a) > 0 and d(b) < 0, (h,k,d(a),d(b))
        for _ in range(100):
            mid = (a+b)/2
            if d(mid)>0:a=mid
            else:b=mid
        val = (a+b)/2
        assert k*z < val < (k+1)*z
        result.append(val)
    assert all(a<b for a,b in zip(result,result[1:]))
    return z,result


def numerical_checks():
    rng = random.Random(20261027)
    checks = 0
    for h in (0.6,1.0,1.01,1.1,1.5,2.0,3.0,4.5,10.0):
        for n in (2,3,4,6,9):
            for t in (0.05,0.7,2.0,5.0,13.0,30.0):
                theoretical=max(k*log1p((t/k)**h) for k in range(1,n+1))
                for _ in range(80):
                    weights=[rng.expovariate(1) for _ in range(n)]
                    denom=sum(weights)
                    x=[t*w/denom for w in weights]
                    actual=sum(log1p(v**h) for v in x)
                    assert actual <= theoretical+2e-12, (h,n,t,actual,theoretical)
                    checks += 1
    return checks


def main():
    count=exact_check()
    numerical=numerical_checks()
    for h in (1.05,1.1,1.5,2.0,2.25,3.0,5.0,10.0):
        z, steps=t_boundaries(h,8)
        assert abs(steps[0]-2*(2**h-2)**(1/h))<1e-10
        print('h=',h,'peak=',round(z,10),'first three switch budgets=',tuple(round(v,10) for v in steps[:3]))
    print('PASS: ',count,'exact rational grid comparisons;',numerical,'floating random allocations; 56 threshold brackets')

if __name__ == '__main__':main()
