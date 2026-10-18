#!/usr/bin/env python3
"""Finite independent checks for closed-neighborhood concept lattices of path powers.
Run: python3 verify.py (Python standard library only).
"""
from collections import Counter
from itertools import product


def direct_extents(n, k):
    """Enumerate all intersections of columns directly as bit masks."""
    full = (1 << n) - 1
    neighbors = [sum(1 << j for j in range(n) if abs(j - i) <= k)
                 for i in range(n)]
    result = {full}
    for mask in range(1, 1 << n):
        x = full
        for i in range(n):
            if (mask >> i) & 1:
                x &= neighbors[i]
        result.add(x)
    return result


def prediction(n, k):
    """Closed extents predicted by the endpoint theorem; independent from intersections."""
    full = (1 << n) - 1
    predicted = {full}
    for a in range(1, n - k + 1):
        for b in range(k + 1, n + 1):
            if a <= b and b - a <= 2*k:
                predicted.add(sum(1 << (j-1) for j in range(a, b+1)))
    if n >= 2*k+2:
        predicted.add(0)
    return predicted


def formula(n, k):
    if n <= 2*k + 1:
        return (n-k)**2
    return (2*k+1)*n - 3*k*k - 2*k + 2


def prof(n, k):
    full = (1 << n) - 1
    r = Counter()
    for a in range(1, n-k+1):
        for b in range(k+1, n+1):
            if a <= b and b-a <= 2*k:
                r[b-a+1] += 1
    if n >= 2*k+2:
        r[0] += 1
        r[n] += 1
    return r


def compute_lattice_axioms(S, n):
    seq = list(S)
    joins = {(x,y): min((s for s in seq if ((x|y) & s) == (x|y)),
                        key=lambda s: s.bit_count()) for x in seq for y in seq}
    modular = distributive = True
    for x in seq:
        for y in seq:
            for z in seq:
                if joins[(x,y & z)] != (joins[(x,y)] & joins[(x,z)]):
                    distributive = False
                if (x & z) == x and joins[(x,y & z)] != (joins[(x,y)] & z):
                    modular = False
    return modular, distributive


def dense_grid(S, n, k):
    r = n-k
    pairs = {}
    for a in range(1,r+1):
        for b in range(k+1,n+1):
            if a>b:  # only possible when n=2k+2
                x = 0
            else:
                x = sum(1<<(j-1) for j in range(a,b+1))
            pairs[(a,b)] = x
    assert set(pairs.values()) == S
    assert len(pairs) == len(S)
    for p,x in pairs.items():
        for q,y in pairs.items():
            assert ((x & y) == x) == (p[0]>=q[0] and p[1]<=q[1])


cases = 0
subsets = 0
for n in range(1, 15):
    for k in range(n):
        S = direct_extents(n,k)
        assert S == prediction(n,k),(n,k, sorted(S ^ prediction(n,k)))
        assert len(S) == formula(n,k),(n,k,len(S),formula(n,k))
        assert Counter(x.bit_count() for x in S) == prof(n,k)
        if n <= 2*k+2:
            dense_grid(S,n,k)
        if 1 <= k and n >= 2*k+3:
            # A nonmodular witness: [k+1] <= [k+1,k+2], compared with [k+3].
            atom = (1<<k)
            z = (1<<k)|(1<<(k+1))
            y = (1<<(k+2))
            assert atom in S and z in S and y in S
            assert (z & y) == 0
        cases += 1
        subsets += (1 << n)
for n in range(2, 11):
    actual = [(len(direct_extents(n,k)),k) for k in range(n)]
    best, opt = max(actual)
    if n == 3:
        assert best == 5 and opt == 0
    else:
        q = (2*n+1)//6
        bound = n+2+(n-1)**2//3
        assert best == bound and opt == q,(n,actual,bound,q)
axiom_cases = 0
for n in range(2, 9):
    for k in range(n):
        S = direct_extents(n,k)
        modular, distributive = compute_lattice_axioms(S,n)
        predicted_mod = (k==0) or (n<=2*k+2)
        predicted_dis = (n<=2*k+2) if k>=1 else (n<=2)
        assert modular == predicted_mod, (n,k,'mod',modular,predicted_mod)
        assert distributive == predicted_dis, (n,k,'dis',distributive,predicted_dis)
        axiom_cases += 1
print('VERIFY_OK endpoint_profiles_cases=',cases,'subset_intersections=',subsets,
      'dense_grid_posets=PASS','modularity_distributivity_cases=',axiom_cases,
      'optimal_radius_n_2_to_10=PASS','all_equalities=PASS')
