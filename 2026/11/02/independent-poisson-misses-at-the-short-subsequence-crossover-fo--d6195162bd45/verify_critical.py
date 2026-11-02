"""Exact finite-n evaluation of common-subsequence transition probabilities.
Computes whole automaton distributions then inclusion-exclusion, no sampling.
"""
from collections import defaultdict
from itertools import product
from math import comb, exp


def exact_distribution_of_contained_masks(r, n):
    patterns = list(product((0,1), repeat=r))
    states = {(0,) * len(patterns): 1}
    for _ in range(n):
        new = defaultdict(int)
        for state, multiplicity in states.items():
            for bit in (0,1):
                after=tuple(i + (i<r and bit == patterns[j][i]) for j,i in enumerate(state))
                new[after] += multiplicity
        states = new
    masks = [0] * (1 << len(patterns))
    for state, count in states.items():
        mask=sum(1<<j for j,pos in enumerate(state) if pos==r)
        masks[mask] += count
    assert sum(masks)==(1<<n)
    return masks


def exact_probability_some_universal_pattern(r, n, d):
    vals=exact_distribution_of_contained_masks(r,n)
    total=1<<n
    p=0.0
    m=len(vals)
    for s in range(1,m):
        num=sum(c for mask,c in enumerate(vals) if mask & s == s)
        p+=(-1 if s.bit_count()%2==0 else 1)*(num/total)**d
    return p


if __name__=='__main__':
    for r,n in ((1,12),(1,16),(2,12),(2,16),(2,20),(3,14),(3,18)):
        a=sum(comb(n,j) for j in range(r))/(1<<n)
        d=round(1/a)
        predicted=1-(1-exp(-d*a))**(1<<r)
        actual=exact_probability_some_universal_pattern(r,n,d)
        print(f'r={r} n={n} d={d} lambda_exact={d*a:.8f} exact_P_LCS_at_least_r={actual:.10f} poisson_prediction={predicted:.10f} abs_error={abs(actual-predicted):.10f}')
        assert 0<=actual<=1+1e-8
    print('PASS')
