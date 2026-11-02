#!/usr/bin/env python3
"""Finite exact and numerical checks for Johnson-walk shadow-cover asymptotics.

Requires Python 3, NumPy. Run: python verify.py
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb
import numpy as np

checks = 0

def check(condition, msg='verification failure'):
    global checks
    assert condition, msg
    checks += 1

def special_chain(n, r, forbidden):
    S = sorted(set().union(*map(set, forbidden)))
    s = len(S)
    forbidden = [frozenset(e) for e in forbidden]
    states = [frozenset(B) for b in range(min(r, s) + 1)
              for B in combinations(S,b)
              if not any(e.issubset(B) for e in forbidden)]
    index = {B:i for i,B in enumerate(states)}
    Q = [[Fraction(0) for _ in states] for __ in states]
    for B in states:
        b = len(B); i = index[B]
        outside = n-s-r+b
        check(outside>=0)
        Q[i][i] += Fraction((r-b)*outside, r*(n-r))
        for u in B:
            C=B-{u}
            if C in index: Q[i][index[C]] += Fraction(outside, r*(n-r))
            for v in set(S)-B:
                C=(B-{u})|{v}
                if C in index: Q[i][index[C]] += Fraction(1, r*(n-r))
        for v in set(S)-B:
            C=B|{v}
            if C in index: Q[i][index[C]] += Fraction(r-b, r*(n-r))
    pi = [Fraction(comb(n-s,r-len(B)),comb(n,r)) for B in states]
    return states,Q,pi

def projected_survival(n, r, forbidden, steps):
    states,Q,pi=special_chain(n,r,forbidden)
    vec=pi
    for _ in range(steps):
        nxt=[Fraction(0) for _ in states]
        for i,p in enumerate(vec):
            for j,a in enumerate(Q[i]):
                nxt[j]+=p*a
        vec=nxt
    return sum(vec)

def full_survival(n,r,forbidden,steps):
    forbidden=[frozenset(e) for e in forbidden]
    states=[frozenset(H) for H in combinations(range(n),r)]
    safe={H for H in states if not any(e.issubset(H) for e in forbidden)}
    vec={H:Fraction(1,comb(n,r)) for H in safe}
    for _ in range(steps):
        nxt=defaultdict(Fraction)
        for H,p in vec.items():
            for u in H:
                for v in set(range(n))-H:
                    K=(H-{u})|{v}
                    if K in safe:
                        nxt[K]+=p*Fraction(1,r*(n-r))
        vec=nxt
    return sum(vec.values())

cases=[(7,3,[(0,1)]),(7,3,[(0,1),(0,2)]),
       (8,3,[(0,1),(2,3)]),(8,4,[(0,1,2)]),
       (8,4,[(0,1,2),(0,1,3)]),(9,4,[(0,1),(2,3)])]
for n,r,forbidden in cases:
    states,Q,pi=special_chain(n,r,forbidden)
    for steps in range(5):
        check(projected_survival(n,r,forbidden,steps)==full_survival(n,r,forbidden,steps),
              f'n={n},r={r},F={forbidden},steps={steps}')
    check(sum(pi)==Fraction(len([H for H in combinations(range(n),r)
                 if not any(set(e).issubset(H) for e in forbidden)]),comb(n,r)))
    for row in Q:
        check(sum(row)<=1)

# The leading killed eigenvalue has escape rate |F|*C(r-1,s-1)/C(n,s).
# At these moderate sizes the error is O(1/n) relative; overlapping targets
# are allowed and can cause a larger finite-size correction.
patterns=[(3,2,[(0,1)]),(3,2,[(0,1),(0,2)]),
          (3,2,[(0,1),(2,3)]),(4,2,[(0,1),(0,2)]),
          (4,3,[(0,1,2)]),(4,3,[(0,1,2),(0,3,4)])]
for r,s,F in patterns:
    for n in [200,600,1500]:
        states,Q,pi=special_chain(n,r,F)
        eigenvalues=np.linalg.eigvals(np.array(Q,dtype=float))
        lam=max(eigenvalues.real)
        predicted=len(F)*comb(r-1,s-1)/comb(n,s)
        normalized=(1-lam)/predicted
        check(abs(normalized-1)<max(0.25,120/n),
              f'spectral n={n},r={r},s={s},F={F}: {normalized}')
        check(max(eigenvalues.imag)<1e-8)
print(f'PASS: {checks} exact and spectral checks; {len(cases)} finite-chain cases and {len(patterns)} asymptotic patterns')
