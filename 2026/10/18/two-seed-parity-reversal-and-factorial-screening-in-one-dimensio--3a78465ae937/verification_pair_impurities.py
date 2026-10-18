"""Finite independent checks for seeded dimer random sequential adsorption.
Python 3 standard library only. Run: python verification_pair_impurities.py
"""
from itertools import permutations
from fractions import Fraction
from collections import Counter
from math import factorial, exp


def path_mean_formula(n):
    return sum((Fraction((-1)**(k-1)*2**(k-1)*(n-k), factorial(k))
                for k in range(1, n)), Fraction(0))


def path_mean_recurrence(n):
    vals = [Fraction(0), Fraction(0)]
    for j in range(2,n+1):
        vals.append(1+sum((2*vals[i] for i in range(j-1)),Fraction(0))/(j-1))
    return vals[n]


def accept_cycle(n, ordered_edges):
    occupied=0
    accepted=0
    for edge in ordered_edges:
        bits=(1<<edge)|(1<<((edge+1)%n))
        if not occupied & bits:
            occupied|=bits
            accepted+=1
    return accepted


def direct_checks():
    distributions=0
    full_orders=0
    forced_checks=0
    for n in range(4,10):
        # Independently enumerate permutations of the non-distinguished edges.
        # For each possible rank of edge 0, the distribution must be identical.
        rank_laws=[Counter() for _ in range(n)]
        for other in permutations(range(1,n)):
            for k in range(n):
                count=accept_cycle(n, other[:k]+(0,)+other[k:])
                rank_laws[k][count]+=1
                full_orders+=1
        assert all(d==rank_laws[0] for d in rank_laws)
        distributions += n-1
        total=Fraction(sum(s*m for s,m in rank_laws[0].items()),factorial(n-1))
        assert total==1+path_mean_formula(n-2), (n,total)
        assert path_mean_formula(n)==path_mean_recurrence(n)
        for d in range(2,n-1):
            observed=Fraction(sum(accept_cycle(n, (0,d)+p)
                 for p in permutations(e for e in range(n) if e not in (0,d))),factorial(n-2))
            analytic=2+path_mean_formula(d-2)+path_mean_formula(n-d-2)
            assert observed==analytic, (n,d,observed,analytic)
            forced_checks+=1
    return distributions,full_orders,forced_checks


def integral_trapezoid(m, intervals=40000):
    step=1/intervals
    vals=[]
    for j in range(intervals+1):
        x=j*step
        val=x*(1-x)**(m-1)*exp(-2*x)
        vals.append((0.5 if j in (0,intervals) else 1)*val)
    return step*sum(vals)


def sign_checks():
    a=(1-exp(-2))/2
    count=0
    for d in range(3,19):
        m=d-2
        delta=float(path_mean_formula(m))-a*m+exp(-2)
        integral=(-1)**m*(2**m/factorial(m-1))*integral_trapezoid(m)
        assert abs(delta-integral)<3e-8, (d,delta,integral)
        assert (-1)**d*delta>0
        bound=2**m/factorial(m+1)
        assert exp(-2)*bound<(-1)**d*delta<bound
        count+=1
    return count

if __name__=='__main__':
    a,b,c=direct_checks()
    d=sign_checks()
    print('PASS: rank-distribution comparisons',a)
    print('PASS: direct priority-order evaluations',b)
    print('PASS: paired-seed finite comparisons',c)
    print('PASS: alternating integral/bounds checks',d)
    print('No finite check is a substitute for the analytic all-size argument.')
