#!/usr/bin/env python3
"""Independent finite-state checks and exact profile checks for P3 adsorption.
Run with python3 verify_trimers.py; standard library only.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import erf, sqrt

checks = 0

def check(cond, description):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(description)

@lru_cache(None)
def profile(t, a):
    """Two-dimensional first-event recurrence (rational arithmetic)."""
    if a < t or a > 2*t:
        return Fraction(0)
    if t == 1:
        return Fraction(1)
    return ((a-1)*profile(t-1,a-2)
            + (3*t-a-1)*profile(t-1,a-1))/ (3*t-2)


def full_labeled(a, b):
    """Independent full-subset Markov-chain first-event calculation.
    Enumerates explicitly all labeled length-two path vertex triples;
    uses no count-lumping or profile recurrence.
    """
    N = a+b
    triples=[]
    for i, j in combinations(range(a), 2):
        for k in range(a, N):
            triples.append((1 << i) | (1 << j) | (1 << k))
    for i in range(a):
        for j, k in combinations(range(a, N), 2):
            triples.append((1 << i) | (1 << j) | (1 << k))

    @lru_cache(None)
    def dp(remaining):
        if remaining == 0:
            return Fraction(1)
        available = [v for v in triples if (v & remaining) == v]
        if not available:
            return Fraction(0)
        return sum((dp(remaining ^ v) for v in available), Fraction())/len(available)
    return dp((1 << N)-1)

# The labeled calculation is strictly independent of the two-count recurrence.
for t in range(1, 5):
    for a in range(1, 3*t):
        b = 3*t-a
        check(full_labeled(a,b) == profile(t,a), f'labeled vs reduced: t={t}, a={a}')

for t in range(1, 61):
    p = [profile(t,a) for a in range(3*t+1)]
    s = sum(p, Fraction())
    target_s = Fraction(1)
    for j in range(1,t+1):
        target_s *= Fraction(3*j-1,3*j-2)
    check(s==target_s, f'normalization at t={t}')
    check(all(p[a] == p[3*t-a] for a in range(3*t+1)), f'symmetry t={t}')
    check(all(p[a+1]>p[a] for a in range(t, (3*t)//2)), f'increasing t={t}')
    check(all(p[a]==0 for a in list(range(t))+list(range(2*t+1,3*t+1))),f'support t={t}')
    edge = Fraction(1)
    for j in range(1,t+1):
        edge*=Fraction(2*j-1,3*j-2)
    check(p[t]==edge, f'edge product t={t}')
    if t>=2:
        check(p[t+1]/p[t]==Fraction(t+2,3),f'boundary adjacent t={t}')
    mean = sum((Fraction(a)*p[a] for a in range(3*t+1)),Fraction()) /s
    check(mean == Fraction(3*t,2), f'mean t={t}')
    variance = sum((((Fraction(a)-mean)**2)*p[a] for a in range(3*t+1)), Fraction())/s
    h=Fraction(1)
    for j in range(1,t):
        h *=Fraction(3*j+4,3*j+2)
    check(variance == Fraction(3*t+2,4)-h, f'variance t={t}')

# The limiting normal statement is proved analytically; these are illustrations.
for t in (100, 300, 800):
    p = [float(profile(t,a)) for a in range(t,2*t+1)]
    z = sum(p)
    for x in (0.5,1.,2.):
        prob=sum(v for j,v in enumerate(p) if abs(t+j-1.5*t)<=x*sqrt(t))/z
        goal=erf(x/sqrt(2*0.75))
        check(abs(prob-goal)<0.14, f'CLT numerical check t={t} x={x}: {prob} vs {goal}')

print('PASSED',checks,'checks, including full labeled-state exact fractions')
