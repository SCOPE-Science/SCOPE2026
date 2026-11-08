#!/usr/bin/env python3
"""Exact independent finite checks for symmetric two-agent chore allocations.

No nonstandard dependencies. All arithmetic is integral; rational parameters are
represented as numerator/denominator pairs. This verifies finite instances,
not the universal or asymptotic claims.
"""
from fractions import Fraction
from itertools import product
from math import comb


def predicted(t, r):
    if r == 1:
        return comb(2*t, t), None
    z = Fraction(t, 2) - Fraction(t-1, 1) / (2*r)
    u = z.numerator // z.denominator
    return 2*sum(comb(t,j) for j in range(u+1)) - 1, u


def direct_count(t, r):
    p,q = r.numerator, r.denominator
    costs = ((q,)*t + (p,)*t, (p,)*t + (q,)*t)
    count = 0
    # Weighted-cost certificates: each of three ratios is checked itemwise.
    # Their sufficiency follows from positive-weighted-sum minimization;
    # exhaustive failures are also compared against a cross-exchange witness.
    witnesses = ((p,q),(1,1),(q,p))
    for alloc in product((0,1), repeat=2*t):
        # 0 means agent 1 and 1 means agent 2.
        bundles = ((i for i,a in enumerate(alloc) if a == 0),
                   (i for i,a in enumerate(alloc) if a == 1))
        bundles = tuple(tuple(b) for b in bundles)
        efx = True
        for agent in range(2):
            own = sum(costs[agent][j] for j in bundles[agent])
            others = sum(costs[agent][j] for j in bundles[1-agent])
            if any(own-costs[agent][j] > others for j in bundles[agent]):
                efx = False
                break
        fpo = False
        for w1,w2 in witnesses:
            weights = (w1,w2)
            if all(weights[alloc[j]]*costs[alloc[j]][j] <=
                   weights[1-alloc[j]]*costs[1-alloc[j]][j]
                   for j in range(2*t)):
                fpo = True
                break
        no_cross = not (any(alloc[j] == 1 for j in range(t))
                        and any(alloc[j] == 0 for j in range(t,2*t)))
        assert fpo == (r == 1 or no_cross), (t,r,alloc)
        if efx and fpo:
            count += 1
    return count


def main():
    count_cases=0
    count_allocs=0
    for t in range(1,8):
        ratios={Fraction(1),Fraction(1001,1000),Fraction(4,3),Fraction(3,2),
                Fraction(2), Fraction(3),Fraction(4),Fraction(5),Fraction(10)}
        for j in range(1,(t-1)//2 + 1):
            critical=Fraction(t-1,t-2*j)
            ratios.update((critical,critical-Fraction(1,10000),critical+Fraction(1,10000)))
        for r in sorted(ratios):
            if r < 1:continue
            prediction,u=predicted(t,r)
            observed=direct_count(t,r)
            assert observed==prediction,(t,str(r),u,observed,prediction)
            count_cases+=1
            count_allocs+=2**(2*t)
    print('PASS: '+str(count_cases)+' exact parameter instances, '
          +str(count_allocs)+' allocation evaluations, 1..7 chore pairs')
    for t in range(1,8):
        print('t=',t,'r=1:',predicted(t,Fraction(1))[0],
              'r=2:',predicted(t,Fraction(2))[0],
              'r=100:',predicted(t,Fraction(100))[0])

if __name__ == '__main__':main()
