#!/usr/bin/env python3
"""Reconstruct the four-cut complex of J(5,2) and its S5 character.

Finite exact enumeration and a complete acyclic discrete-Morse certificate.
Uses only the Python standard library; requires four_cut_certificate.json.
"""
from itertools import combinations, permutations
from collections import Counter, deque
from functools import lru_cache
from math import factorial, prod
from pathlib import Path
import json

E = tuple(combinations(range(5), 2))
ALL = (1 << 10) - 1

def adjacent(i, j):
    return bool(set(E[i]) & set(E[j]))

def connected(verts):
    vis = {verts[0]}
    todo = [verts[0]]
    while todo:
        i = todo.pop()
        for j in verts:
            if j not in vis and adjacent(i, j):
                vis.add(j); todo.append(j)
    return len(vis) == len(verts)

bad = tuple(t for t in combinations(range(10), 4) if not connected(t))
assert len(bad) == 10
# A disconnected quadruple is exactly a triangle of K5 plus the
# disjoint edge on its remaining two letters.
assert set(bad) == {
    tuple(sorted([E.index(edge) for edge in combinations(t, 2)] +
                 [E.index(tuple(i for i in range(5) if i not in t))]))
    for t in combinations(range(5), 3)
}
facets = tuple(ALL ^ sum(1 << i for i in t) for t in bad)
# Each facet is all six cross-edges of one 2+3 partition of five letters.
assert set(facets) == {
    sum(1 << E.index(tuple(sorted((a, b)))) for a in s for b in range(5) if b not in s)
    for s in combinations(range(5), 2)
}
F = set()
for facet in facets:
    face = facet
    while True:
        F.add(face)
        if face == 0: break
        face = (face - 1) & facet
assert len(F) == 371
sizes = [[s for s in sorted(F) if s.bit_count() == k] for k in range(7)]
assert [len(s) for s in sizes] == [1, 10, 45, 110, 135, 60, 10]

def f2rank(columns):
    pivots = {}
    for col in columns:
        while col:
            p = col.bit_length() - 1
            if p in pivots: col ^= pivots[p]
            else:
                pivots[p] = col
                break
    return len(pivots)
ranks = [0] * 7
for k in range(1, 7):
    lo = {s: i for i, s in enumerate(sizes[k - 1])}
    cols = []
    for s in sizes[k]:
        col = 0
        for v in range(10):
            if s & (1 << v): col ^= 1 << lo[s ^ (1 << v)]
        cols.append(col)
    ranks[k] = f2rank(cols)
assert ranks == [0, 1, 9, 36, 74, 50, 10]
assert [len(sizes[d+1]) - ranks[d+1] - (ranks[d+2] if d+2 < 7 else 0)
        for d in range(6)] == [0, 0, 0, 11, 0, 0]

# Explicit matching, including the empty simplex initially.
ORDER = tuple(reversed(range(10)))
unused = set(F)
pairs = []
for v in ORDER:
    bit = 1 << v
    for s in sorted(unused):
        if not (s & bit) and (s | bit) in unused:
            unused.remove(s); unused.remove(s | bit)
            pairs.append((s, s | bit))
assert len(pairs) == 180 and len(unused) == 11
assert all(s.bit_count() == 4 for s in unused)
assert len([p for p in pairs if p[0] == 0]) == 1
base = next(b for a,b in pairs if a == 0)
pairs = [(a,b) for a,b in pairs if a != 0]
assert len(pairs) == 179
critical = sorted(unused | {base})
assert Counter(s.bit_count() for s in critical) == {1:1,4:11}

# Full directed Hasse graph, matched arrows low to high, others high to low.
nodes = sorted(F - {0})
ind = {s:i for i,s in enumerate(nodes)}
matched = dict(pairs)
adj = [[] for _ in nodes]
indegree = [0] * len(nodes)
arrows = 0
for upper in nodes:
    for v in range(10):
        if upper & (1 << v):
            lower = upper ^ (1 << v)
            if lower == 0: continue
            a,b = (lower,upper) if matched.get(lower) == upper else (upper,lower)
            adj[ind[a]].append(ind[b]);indegree[ind[b]] += 1;arrows += 1
Q = deque(i for i,d in enumerate(indegree) if d == 0)
seen = 0
while Q:
    i = Q.popleft();seen += 1
    for j in adj[i]:
        indegree[j] -= 1
        if indegree[j] == 0:Q.append(j)
assert seen == 370
assert len(set(nodes) - {a for p in pairs for a in p}) == 12
cert = json.loads(Path(__file__).with_name('four_cut_certificate.json').read_text(encoding='utf-8'))
assert cert == {
    'vertices': [list(e) for e in E],
    'facets': sorted(facets),
    'element_order': list(ORDER),
    'matching_pairs': [[a,b] for a,b in pairs],
    'critical_faces': critical,
}
# One 0-cell and eleven 3-cells: all their attaching maps land at the point.
# Therefore the Morse CW model is a wedge of eleven 3-spheres.

def cycle_type(p):
    unseen = set(range(5)); sizes = []
    while unseen:
        i = min(unseen); x=i; count=0
        while x in unseen:
            unseen.remove(x);count += 1;x=p[x]
        sizes.append(count)
    return tuple(sorted(sizes,reverse=True))
def sign(a):
    return -1 if sum(a[i] > a[j] for i in range(len(a)) for j in range(i+1,len(a)))%2 else 1

def action_character(p):
    action = [E.index(tuple(sorted((p[a],p[b])))) for a,b in E]
    traces = []
    for k in range(1,7):
        trace = 0
        for mask in sizes[k]:
            inds = [i for i in range(10) if mask & (1 << i)]
            mapped = [action[i] for i in inds]
            if set(mapped) == set(inds): trace += sign(mapped)
        traces.append(trace)
    # Only reduced H3 is nonzero, so the unreduced Lefschetz number is 1 - chi_H3.
    return 1 - sum((-1)**d * x for d,x in enumerate(traces)), traces
values = {}
for p in permutations(range(5)):
    ct = cycle_type(p)
    char,traces = action_character(p)
    if ct in values: assert values[ct] == char
    else: values[ct] = char
expected = {
    (5,):1, (4,1):-1, (3,2):-1, (3,1,1):-1,
    (2,2,1):3, (2,1,1,1):-1, (1,1,1,1,1):11,
}
assert values == expected

# Independent Frobenius alternant calculation of all irreducible S5 characters.
# If lambda has length l, chi_lambda(mu) is the x^(lambda+delta)
# coefficient in det(x_i^(l-j)) * product_{m in mu}(sum_i x_i^m).
@lru_cache(None)
def irreducible_character(lam,mu):
    length = len(lam)
    delta = tuple(range(length-1,-1,-1))
    target = tuple(lam[i]+delta[i] for i in range(length))
    result = 0
    for powers in permutations(delta):
        need = tuple(target[i]-powers[i] for i in range(length))
        if min(need)<0: continue
        perm_sign = (-1)**(sum(powers[i]>powers[j] for i in range(length) for j in range(i+1,length)) + length*(length-1)//2)
        @lru_cache(None)
        def coeff(j,left):
            if j == len(mu): return int(not any(left))
            return sum(coeff(j+1,tuple(left[i]-(mu[j] if i==a else 0) for i in range(length)))
                       for a in range(length) if left[a] >= mu[j])
        result += perm_sign * coeff(0,need)
    return result

def partitions(n, ceiling=None):
    if n==0:
        yield ()
        return
    if ceiling is None: ceiling=n
    for k in range(min(ceiling,n),0,-1):
        for rest in partitions(n-k,k): yield (k,)+rest
mult = {}
for lam in partitions(5):
    score = 0
    for c, val in values.items():
        frequencies = Counter(c)
        classsize = factorial(5)//prod(i**v*factorial(v) for i,v in frequencies.items())
        score += classsize*val*irreducible_character(lam,c)
    assert score%120==0
    m = score//120
    assert m >= 0
    if m: mult[lam]=m
assert mult == {(3,2):1,(2,2,1):1,(1,1,1,1,1):1},mult
print('VERIFY_OK 4-cut J(5,2); 10 facets, 371 faces, 179 Morse pairs')
print('acyclic_nodes=370 arrows=%d critical_0=1 critical_3=11' % arrows)
print('mod2 boundary ranks=%s' % ranks)
print('S5 chars=%s' % values)
print('irreducibles=(3,2)+(2,2,1)+(1^5); all 120 elements checked')
