#!/usr/bin/env python3
"""Exact checks for conditional pairwise dependence of comparison signs.

Uses descent-mask counts from independent enumeration of all permutations,
and checks every feasible conditioning pattern on any subset of other edges.
"""
from itertools import permutations, combinations
from math import factorial
from collections import Counter


def count_permutation_descent_masks(n):
    counts = [0] * (1 << (n-1))
    for p in permutations(range(n)):
        mask = sum((p[k] > p[k+1]) << k for k in range(n-1))
        counts[mask] += 1
    assert sum(counts) == factorial(n)
    return counts


def verify(n):
    masses = count_permutation_descent_masks(n)
    m = n - 1
    cases = 0
    negatives = 0
    zeros = 0
    for i, j in combinations(range(m), 2):
        free = [t for t in range(m) if t not in (i,j)]
        for states in __import__('itertools').product((None,0,1), repeat=len(free)):
            observed = sum(1 << free[t] for t, state in enumerate(states) if state is not None)
            fixed_one = sum(1 << free[t] for t,state in enumerate(states) if state == 1)
            q = [[0,0],[0,0]]
            for mask, count in enumerate(masses):
                if count and (mask & observed) == fixed_one:
                    q[(mask >> i)&1][(mask >> j)&1] += count
            assert sum(map(sum,q)) > 0
            delta = q[1][1]*q[0][0] - q[1][0]*q[0][1]
            fully_observed = all(observed & (1 << t) for t in range(i+1,j))
            if fully_observed:
                assert delta < 0, ('negative',n,i,j,states,q,delta)
                negatives+=1
            else:
                assert delta == 0, ('zero',n,i,j,states,q,delta)
                zeros+=1
            cases += 1
    return cases, negatives, zeros


def nonstability_witness():
    # Descent-set multiaffine generating polynomial at z=(-3,-3,2,-3).
    counts = count_permutation_descent_masks(5)
    z = (-3,-3,2,-3)
    def deriv(bits):
        s=0
        for mask, cnt in enumerate(counts):
            if (mask & bits) != bits: continue
            term=cnt
            for k in range(4):
                if (mask & (1<<k)) and not (bits & (1<<k)):
                    term *= z[k]
            s+=term
        return s
    # Derivatives w.r.t. variables indexed 2 and 4 (one-based).
    f,a,b,c=deriv(0),deriv(1<<1),deriv(1<<3),deriv((1<<1)|(1<<3))
    assert (f,a,b,c) == (76,16,-44,-9), (f,a,b,c)
    assert a*b-f*c == -20
    return 6


if __name__ == '__main__':
    total=neg=zero=0
    for n in range(3,11):
        cases,a,b=verify(n)
        total+=cases;neg+=a;zero+=b
        print(f'n={n} cases={cases} strict_negative={a} zero={b}')
    extras=nonstability_witness()
    print('PASS',total,'conditional-covariance signs;',neg,'negative;',zero,'zero;',extras,'nonstability certificate checks')
