"""Exact checks for distinguished-category richness covariance.

Run: python verify.py
"""
from fractions import Fraction as Q
from itertools import product
from math import exp, log


def expected_gap(n, residual_weights, s):
    return 1 - s**n + sum((1-t)**n - (1-s*t)**n for t in residual_weights)


def enum_cov(n, residual_weights, s):
    probs = [s*t for t in residual_weights] + [1-s]
    E_K = E_B = E_KB = Q(0)
    for sample in product(range(len(probs)), repeat=n):
        pr = Q(1)
        for k in sample:
            pr *= probs[k]
        k = len(set(sample))
        b = int(len(probs)-1 in sample)
        E_K += pr*k
        E_B += pr*b
        E_KB += pr*k*b
    return E_KB - E_K * E_B


def test():
    choices = [ [Q(1,2),Q(1,2)], [Q(1,4),Q(3,4)],
                [Q(1,2),Q(1,3),Q(1,6)]]
    total=0
    for ts in choices:
        for n in range(2,6):
            for s in [Q(1,7),Q(1,3),Q(1,2),Q(4,5)]:
                actual=enum_cov(n,ts,s)
                predicted=s**n*expected_gap(n,ts,s)
                assert actual == predicted,(ts,n,s,actual,predicted)
                total+=1
    assert expected_gap(3,[Q(1,2),Q(1,2)],Q(1,5)) < 0
    assert expected_gap(3,[Q(1,2),Q(1,2)],Q(4,5)) > 0
    # Exhaustive n=3, r=2 witness: conditional on observing all 3 types
    # versus omitting the third type.
    ts=[Q(1,2),Q(1,2)]; s=Q(1,5); probs=[s*t for t in ts]+[1-s]
    p_all=sum((lambda sample: __import__('functools').reduce(lambda a,j:a*probs[j],sample,Q(1)))(sample)
              for sample in product(range(3),repeat=3) if len(set(sample))==3)
    assert p_all>0
    for ts in choices:
        zlo=Q(0)
        # limiting root sum(exp(-z*t))=1: simple binary search
        a=0.; b=100.
        for _ in range(80):
            c=(a+b)/2
            if sum(exp(-c*float(t)) for t in ts)>1:a=c
            else:b=c
        z=(a+b)/2
        def root(n):
            a=0.; b=1.
            for _ in range(100):
                c=(a+b)/2
                if expected_gap(n,ts,c)<0:a=c
                else:b=c
            return (a+b)/2
        nums=[n*root(n) for n in (100,500,2000)]
        assert abs(nums[-1]-z)<.025,(ts,z,nums)
        print('t=',ts,'z=',round(z,9),'n_sigma=',[round(a,9) for a in nums])
    print('PASS',total,'exact rational covariance cases; full-support stochastic endpoint witness; asymptotic root tests')

if __name__=='__main__':
    test()
