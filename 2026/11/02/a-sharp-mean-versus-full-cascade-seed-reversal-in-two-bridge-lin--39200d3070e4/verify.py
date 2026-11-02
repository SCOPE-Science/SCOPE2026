#!/usr/bin/env python3
"""Exact audit of a six-site threshold-cascade calculation.

Run: python verify.py
Needs only Python 3 standard library and SymPy.
No stochastic sampling is used.
"""
from itertools import combinations, product
from fractions import Fraction
import sympy as sp

VERTICES = tuple(range(6))
EDGES = [(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(2,3)]
NEIGHBORS = {v:set() for v in VERTICES}
for u,v in EDGES:
    NEIGHBORS[u].add(v)
    NEIGHBORS[v].add(u)

# Representatives of the four automorphism orbits of unordered seed pairs:
# A: both in the same triangle; B: bridge/ordinary opposite triangle;
# C: ordinary/ordinary opposite triangles; D: both bridge endpoints.
REP = {'A':(0,1), 'B':(0,3), 'C':(0,4), 'D':(2,3)}
EXPECTED_H = {'A':(3,13,25,21,6), 'B':(4,20,34,24,6),
              'C':(2,24,36,24,6), 'D':(2,16,32,24,6)}
EXPECTED_J = {'A':(0,0,2,3,1), 'B':(0,2,5,4,1),
              'C':(0,4,6,4,1), 'D':(0,0,4,4,1)}
COUNT = 0

def check(statement, note):
    global COUNT
    assert statement, note
    COUNT += 1

def direct_closure(seeds, thresholds):
    activated = set(seeds)
    while True:
        newcomers = {v for v in VERTICES if v not in activated
                    and len(NEIGHBORS[v] & activated) >= thresholds[v]}
        if not newcomers: return frozenset(activated)
        activated.update(newcomers)

def closed_superset_intersection(seeds, thresholds):
    """Independent characterization: intersect all stable supersets of seeds."""
    stable = []
    base = set(seeds)
    for mask in range(1 << len(VERTICES)):
        chosen = {v for v in VERTICES if mask & (1 << v)}
        if not base <= chosen: continue
        if all(len(NEIGHBORS[v] & chosen) < thresholds[v]
               for v in VERTICES if v not in chosen):
            stable.append(chosen)
    assert stable
    common = set(VERTICES)
    for c in stable: common.intersection_update(c)
    return frozenset(common)

def orbit_type(pair):
    a,b = pair
    if {a,b} == {2,3}: return 'D'
    left = {0,1,2}; right = {3,4,5}
    if (a in left and b in left) or (a in right and b in right):
        return 'A'
    if (a in {2,3}) or (b in {2,3}):
        return 'B'
    return 'C'

def counts(seed):
    other = [v for v in VERTICES if v not in seed]
    H = [0]*5; J = [0]*5
    for bits in product((1,2), repeat=4):
        th = dict(zip(other,bits))
        activated = direct_closure(seed, th)
        alternate = closed_superset_intersection(seed, th)
        check(activated == alternate, ('independent closures disagree',seed,bits))
        k = bits.count(1)
        H[k] += len(activated)
        J[k] += int(len(activated) == 6)
    return tuple(H), tuple(J)

P = sp.symbols('p', real=True)
def weighted(v):
    return sp.expand(sum(z*P**k*(1-P)**(4-k) for k,z in enumerate(v)))

seen = {'A':0,'B':0,'C':0,'D':0}
for pair in combinations(VERTICES,2):
    typ = orbit_type(pair)
    seen[typ] += 1
    h,j = counts(pair)
    check(h == EXPECTED_H[typ],('spread coefficient mismatch',pair,h))
    check(j == EXPECTED_J[typ],('full coefficient mismatch',pair,j))
check(seen == {'A':6,'B':4,'C':4,'D':1},seen)

A,B,C,D = (weighted(EXPECTED_H[k]) for k in 'ABCD')
FA,FB,FC,FD = (weighted(EXPECTED_J[k]) for k in 'ABCD')
for lhs,rhs,tag in [
    (A,3+P+4*P**2-2*P**3,'A mean'),
    (B,4+4*P-2*P**2,'B mean'),
    (C,6-4*(1-P)**4,'C mean'),
    (D,2+8*P-4*P**2,'D mean'),
    (FA,P**2*(2-P),'A full'),
    (FB,P*(2-P),'B full'),
    (FC,P*(2-P)*(1+(1-P)**2),'C full'),
    (FD,P**2*(2-P)**2,'D full'),
    (B-A,(1-P)*(1+4*P-2*P**2),'B beats A'),
    (B-D,2*(1-P)**2,'B beats D'),
    (B-C,2*(1-P)**2*(2*P**2-4*P+1),'mean crossing'),
    (FC-FA,P*(1-P)*(2-P)**2,'full beats A'),
    (FC-FB,P*(2-P)*(1-P)**2,'full beats B'),
    (FC-FD,2*P*(2-P)*(1-P)**2,'full beats D'),
]:
    check(sp.simplify(lhs-rhs) == 0,tag)

critical = 1-sp.sqrt(2)/2
check(sp.simplify(2*critical**2-4*critical+1) == 0,'threshold root')
check(0 < critical < 1,'root domain')
check(sp.diff(2*P**2-4*P+1,P).subs(P,sp.Rational(1,2)) < 0,'crossing orientation')

for k in range(1,30):
    q = sp.Rational(k,30)
    expected = max(A.subs(P,q), B.subs(P,q), C.subs(P,q),D.subs(P,q))
    actual = B.subs(P,q) if q < critical else C.subs(P,q)
    check(expected == actual,('mean winner',q))
    check(FC.subs(P,q) > max(FA.subs(P,q),FB.subs(P,q),FD.subs(P,q)),
          ('full winner',q))

# Trivial boundaries are described explicitly and not extrapolated as strict.
for q in (0,1):
    vals = [z.subs(P,q) for z in (A,B,C,D)]
    check(all(z >= 2 for z in vals),('boundary bounds',q))
print('PASS: %d exact assertions; 240 threshold assignments checked twice'%COUNT)
print('Critical p =',critical, '~',sp.N(critical,16))
print('Mean spread classes:', {k:str(v) for k,v in zip('ABCD',(A,B,C,D))})
print('Full spread classes:', {k:str(v) for k,v in zip('ABCD',(FA,FB,FC,FD))})
