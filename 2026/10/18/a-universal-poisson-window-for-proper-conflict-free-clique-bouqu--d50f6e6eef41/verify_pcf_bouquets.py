#!/usr/bin/env python3
"""Independent finite checks of proper conflict-free colorings of clique bouquets.

Run with Python 3.10+; no third-party packages are required.
"""
from itertools import product
from math import comb, factorial
from collections import Counter


def falling(n, h):
    if h < 0 or h > n: return 0
    out = 1
    for t in range(h): out *= n-t
    return out


def coeff_product(sizes, r, j):
    # Coefficient [u^j] in product of block polynomials.
    a = [1] + [0]*j
    for s in sizes:
        b = [0]*(j+1)
        for h in range(min(j, s)+1):
            v = comb(s,h)*falling(r-j,s-h)
            for d in range(j-h+1): b[d+h] += a[d]*v
        a = b
    return a[j]


def formula(sizes, q):
    r = q-1
    if r < max(sizes): return 0
    val = sum((-1)**(j+1)*comb(r,j)*factorial(j)*coeff_product(sizes,r,j)
              for j in range(1,r+1))
    return q*val


def build(sizes):
    total = 1+sum(sizes)
    adj = [set() for _ in range(total)]
    v = 1
    for s in sizes:
        block = range(v,v+s)
        for a in block:
            adj[0].add(a); adj[a].add(0)
            for b in block:
                if a != b: adj[a].add(b)
        v += s
    assert v == total
    return [tuple(sorted(a)) for a in adj]


def graph_pcf(coloring, adj):
    for v, nbr in enumerate(adj):
        for w in nbr:
            if coloring[w] == coloring[v]: return False
        counts = Counter(coloring[w] for w in nbr)
        if not any(c == 1 for c in counts.values()): return False
    return True


def direct(sizes,q):
    adj = build(sizes)
    valid = 0
    total = 0
    for f in product(range(q), repeat=len(adj)):
        total += 1
        valid += graph_pcf(f,adj)
    return valid,total


def direct_proper(sizes, q):
    # Independent enumeration of proper colorings of each clique, then graph predicate.
    from itertools import permutations
    r = q-1
    if r < max(sizes): return 0
    adj = build(sizes)
    for_center = 0
    for choices in product(*(list(permutations(range(1,r+1),s)) for s in sizes)):
        f = (0,) + tuple(c for seq in choices for c in seq)
        for_center += graph_pcf(f,adj)
    return q*for_center


def threshold_uniform(s, b):
    q = s+2
    if b==2: return q*(factorial(s)**b)*(s+1)*s
    return q*(factorial(s)**b)*(s+1)*b*s


def factorial_moment(sizes, r, j):
    # In a uniformly random proper coloring with a fixed hub color, target
    # colors are distributed without replacement inside each clique.
    a = [1.0] + [0.0]*j
    for s in sizes:
        b = [0.0]*(j+1)
        den = float(falling(r,s))
        for h in range(min(j,s)+1):
            v = comb(s,h)*falling(r-j,s-h)/den
            for d in range(j-h+1): b[d+h] += a[d]*v
        a = b
    return falling(r,j)*factorial(j)*a[j]


def run():
    brute_assignments = 0
    brute_cases = 0
    proper_cases = 0
    for sizes in [(1,1),(1,1,1),(1,1,1,1),(1,2),(1,2,1),(2,2),(2,2,1),(2,2,2),(1,2,3),(1,1,2,2),(3,3)]:
        for q in (2,3,4,5):
            if q**(1+sum(sizes)) > 900000: continue
            observed, tot = direct(sizes,q)
            expected = formula(sizes,q)
            assert observed==expected,(sizes,q,observed,expected)
            brute_assignments +=tot
            brute_cases +=1
    for sizes in [(1,1,1,1,1),(2,2,2,2),(3,3,3),(2,3,4),(1,2,4),(1,3,3,2),(3,1,1,1),(4,4)]:
        for q in (max(sizes)+1,max(sizes)+2,max(sizes)+3):
            if q*max(1,__import__('math').prod(falling(q-1,s) for s in sizes))>1000000: continue
            observed = direct_proper(sizes,q)
            expected = formula(sizes,q)
            assert observed == expected,(sizes,q,observed,expected)
            proper_cases +=1
    for s in range(1,5):
        for b in range(2,8):
            a = formula((s,)*b,s+2)
            expected = threshold_uniform(s,b)
            assert a == expected,(s,b,a,expected)
            assert formula((s,)*b,s+1)==0
    print(f'All graph-predicate exhaustive comparisons passed: {brute_cases} cases, {brute_assignments:,} total assignments.')
    print(f'All additional proper-coloring comparisons passed: {proper_cases} cases.')
    print('All 24 uniform exact minimum-palette comparisons passed (s=1..4, blocks=2..7).')
    print('Example W_(2,3), q=4: ',formula((2,2,2),4))
    print('Example W_(2,2), q=4: ',formula((2,2),4))
    import math
    for b in (120,480,1920):
        sizes=tuple(2+(i%2) for i in range(b))
        S=sum(sizes);r=round(S/math.log(S))
        c=S/r-math.log(S); target=math.exp(-c)
        fm1=factorial_moment(sizes,r,1);fm2=factorial_moment(sizes,r,2)
        assert abs(fm1-target)<0.55 and abs(fm2-target**2)<0.9
        print(f'Critical example S={S}, r={r}: factorial moments E[X]={fm1:.6f}, E[(X)_2]={fm2:.6f}; predicted mean={target:.6f}')
    for s,b in [(1,3),(2,3),(2,6),(3,5)]:
        q=s+2; r=q-1
        fraction = __import__('fractions').Fraction(formula((s,)*b,q),q*falling(r,s)**b)
        print(f'At optimum s={s}, blocks={b}, fraction of proper colorings PCF = {fraction}')

if __name__=='__main__': run()
