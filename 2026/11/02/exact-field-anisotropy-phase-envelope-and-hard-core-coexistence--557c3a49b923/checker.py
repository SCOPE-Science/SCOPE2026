#!/usr/bin/env python3
"""Exact, standard-library replay of the Petersen spin-one phase envelope.
Run: python3 checker.py (with convex_certificate.json in this directory).
All arithmetic is integral or rational; no optimization package is required.
"""
from itertools import combinations, product
from fractions import Fraction as Q
from collections import Counter, defaultdict
import json
from pathlib import Path

V = list(combinations(range(5), 2))
assert len(V) == 10
EDGES = [(i, j) for i in range(10) for j in range(i+1, 10)
         if set(V[i]).isdisjoint(V[j])]
assert len(EDGES) == 15 and all(sum(i in e for e in EDGES) == 3 for i in range(10))

# Independent implementation one: full Cartesian ternary enumeration.
h1 = Counter()
for s in product((-1, 0, 1), repeat=10):
    b = sum(s[i]*s[j] for i,j in EDGES)
    k = sum(v*v for v in s)
    m = sum(s)
    h1[b,k,m] += 1
assert sum(h1.values()) == 3**10

# Independent implementation two: disjoint positive- and negative-spin masks,
# computing edge contributions only from the masks, not the first loop's states.
h2 = Counter()
for plus in range(1 << 10):
    free = ((1 << 10)-1) ^ plus
    neg = free
    while True:
        k = plus.bit_count()+neg.bit_count()
        m = plus.bit_count()-neg.bit_count()
        b = sum(((1 if (plus >> i)&1 else (-1 if (neg >> i)&1 else 0))
                 * (1 if (plus >> j)&1 else (-1 if (neg >> j)&1 else 0)))
                for i,j in EDGES)
        h2[b,k,m] += 1
        if neg == 0:
            break
        neg = (neg-1) & free
assert h1 == h2 and len(h1) == 318

# The table covers all distinct nonnegative total-magnetization occupancies.
bmin = {(k,m): min(b for b,kk,mm in h1 if kk==k and mm==m)
        for k in range(11) for m in range(k%2,k+1,2)}
assert len(bmin) == 36
cert = json.loads(Path(__file__).with_name('convex_certificate.json').read_text('utf-8'))
refs = {name: tuple(values) for name,values in cert['reference_triples'].items()}
assert refs == {'A':(-9,10,2),'B':(-6,6,0),'C':(-3,4,2),
                'D':(0,4,4),'E':(3,6,6),'F':(15,10,10),'Z':(0,0,0)}
assert all(h1[t] > 0 for t in refs.values())
assert len(cert['witnesses']) == 36
seen = set()
for row in cert['witnesses']:
    key = (row['k'], row['m'])
    assert key not in seen
    seen.add(key)
    assert key in bmin and row['b_min'] == bmin[key]
    weights = {name: Q(f) for name,f in row['weights'].items()}
    assert all(v >= 0 and name in refs for name,v in weights.items())
    assert sum(weights.values()) == 1
    assert sum(refs[n][1]*v for n,v in weights.items()) == key[0]
    assert sum(refs[n][2]*v for n,v in weights.items()) >= key[1]
    assert sum(refs[n][0]*v for n,v in weights.items()) <= bmin[key]
assert set(bmin) == seen

# Each reference branch has a genuinely strict interior witness for h>=0.
witnesses = {'A':(-2,1),'B':(Q(9,10),Q(1,10)),
             'C':(Q(9,8),Q(9,8)),'D':(1,2),'E':(1,3),
             'F':(1,6),'Z':(2,0)}
def en(t, r, u):
    b,k,m = t
    return b+r*k-u*m
for name,(r,u) in witnesses.items():
    r,u = Q(r),Q(u)
    energies = {lab:en(t,r,u) for lab,t in refs.items()}
    assert energies[name] < min(value for lab,value in energies.items() if lab!=name)
    emin = min(en(t,r,u) for t in h1)
    assert energies[name] == emin
    assert sum(c for t,c in h1.items() if en(t,r,u)==emin) == h1[refs[name]]

# Exact independence polynomial and two hardness-free saturation boundaries.
independent = Counter()
for mask in range(1 << 10):
    if all(not ((mask>>i)&1 and (mask>>j)&1) for i,j in EDGES):
        independent[mask.bit_count()] += 1
assert [independent[k] for k in range(5)] == [1,10,30,30,5]
assert sum(independent.values()) == 76
assert sum(2**k*c for k,c in independent.items()) == 461
for r,u,expected in [(Q(-2),Q(3),76),(Q(0),Q(3),461),
                     (Q(1,2),Q(7,2),76),(Q(2),Q(5),76)]:
    emin = min(en(t,r,u) for t in h1)
    assert sum(c for t,c in h1.items() if en(t,r,u)==emin) == expected

nodes = [(-0,3,461),(Q(3,4),0,30),(Q(3,4),Q(9,4),85),
         (1,0,21),(1,Q(1,2),36),(1,Q(3,2),20),
         (Q(3,2),Q(3,2),86)]
for r,u,expected in nodes:
    r,u=Q(r),Q(u)
    emin = min(en(t,r,u) for t in h1)
    assert sum(c for t,c in h1.items() if en(t,r,u)==emin) == expected
print('VERIFIED: 59049 ternary states, 318 triples, 36 rational dominance certificates,')
print('          7 strict sectors, 7 critical points, independent-set polynomial.')
print('REFERENCE INTERIOR COUNTS:',{label:h1[t] for label,t in refs.items()})
print('SATURATION DEGENERACY: 76 (r<0), 461 (r=0), 76 (r>0).')
