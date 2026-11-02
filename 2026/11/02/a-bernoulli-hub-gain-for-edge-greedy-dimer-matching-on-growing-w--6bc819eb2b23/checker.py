#!/usr/bin/env python3
"""Exact small-order checks for greedy dimer matching on wheels and cycles.

Python standard library only. Run: python checker.py
Finite checks support but do not prove the all-order asymptotic theorem.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import exp, factorial
from random import Random

checks = 0

def verify(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

@lru_cache(None)
def path_mean(m):
    if m < 2:
        return Fraction(0)
    return Fraction(1) + Fraction(2, m-1) * sum((path_mean(j) for j in range(m-1)), Fraction(0))

def path_closed(m):
    if m < 2:
        return Fraction(0)
    return Fraction(m,2) - sum((Fraction((m-j)*(-2)**j, 2*factorial(j)) for j in range(m)), Fraction(0))

def cycle_mean(n):
    return 1 + path_mean(n-2)

def remaining_paths(n, mask):
    if mask == 0:
        return []
    full = (1<<n)-1
    if mask == full:
        raise ValueError('At least one rim vertex must be removed')
    start = next(i for i in range(n) if not(mask>>i & 1))
    j = (start+1)%n
    lengths = []
    while j != start:
        if mask>>j & 1:
            ell = 0
            while j != start and (mask>>j & 1):
                ell += 1
                j = (j+1)%n
            lengths.append(ell)
        else:
            j = (j+1)%n
    return lengths

def wheel_mean(n):
    full = (1<<n)-1
    @lru_cache(None)
    def unpaired_hub(mask):
        if not mask:
            return Fraction(0)
        total = Fraction(0)
        count = 0
        for i in range(n):
            if not(mask>>i & 1):
                continue
            after_spoke = mask & ~(1<<i)
            total += 1 + sum((path_mean(k) for k in remaining_paths(n, after_spoke)), Fraction(0))
            count += 1
            next_i = (i+1)%n
            if mask>>next_i & 1:
                total += 1 + unpaired_hub(mask & ~(1<<i) & ~(1<<next_i))
                count += 1
        return total/count
    return unpaired_hub(full)

def greedy(order, n, include_spokes):
    occupied = set()
    chosen = 0
    for u,v in order:
        if not include_spokes and (u == n or v == n):
            continue
        if u not in occupied and v not in occupied:
            occupied.add(u)
            occupied.add(v)
            chosen += 1
    return chosen

def wheel_edges(n):
    return [(i, (i+1)%n) for i in range(n)] + [(i,n) for i in range(n)]

for m in range(0,65):
    verify(path_mean(m) == path_closed(m), f'path formula at {m}')

for n in range(3,13):
    mean = wheel_mean(n)
    verify(Fraction(0) <= mean <= Fraction(n+1,2), f'wheel size at {n}')
    verify(mean >= cycle_mean(n) and mean <= cycle_mean(n)+1, f'wheel interval at {n}')
    if n in (3,4):
        edges = wheel_edges(n)
        wsum = 0
        csum = 0
        for perm in permutations(edges):
            w = greedy(perm,n,True)
            c = greedy(perm,n,False)
            verify(w-c in (0,1), f'coupled wheel increment at {n}')
            wsum += w
            csum += c
        fact = factorial(len(edges))
        verify(Fraction(wsum, fact) == mean, f'independent permutation wheel at {n}')
        verify(Fraction(csum, fact) == cycle_mean(n), f'independent permutation cycle at {n}')

# General deletion stability under arbitrary deterministic priority orders.
for n in (2,3,4):
    potential = list(combinations(range(n),2))
    for mask in range(1<<len(potential)):
        edges = [e for j,e in enumerate(potential) if mask>>j & 1]
        for order in permutations(edges):
            base = greedy(order,n,True)
            for removed in range(n):
                restricted = tuple(e for e in order if removed not in e)
                shorter = greedy(restricted,n,True)
                verify(base-shorter in (0,1), f'vertex-deletion stability n={n}')

random = Random(5017)
for n in (5,7,10):
    for _ in range(200):
        edges = [e for e in combinations(range(n),2) if random.random() < 0.38]
        random.shuffle(edges)
        removed = random.randrange(n)
        base = greedy(edges,n,True)
        restricted = greedy([e for e in edges if removed not in e],n,True)
        verify(base-restricted in (0,1), f'larger deletion case n={n}')

rho = (1-exp(-2))/2
for n in (7,8,9,10,11,12):
    difference = float(wheel_mean(n)-cycle_mean(n))
    verify(abs(difference-rho) < (3.0 if n < 9 else 2.0)/n, f'asymptotic diagnostic at {n}')

print('PASS', checks, 'exact checks and numerical asymptotic diagnostics')
print('density rho =', format(rho,'.12f'))
for n in (8,10,12):
    print(n, 'wheel',float(wheel_mean(n)), 'cycle',float(cycle_mean(n)),
          'gain',float(wheel_mean(n)-cycle_mean(n)))
