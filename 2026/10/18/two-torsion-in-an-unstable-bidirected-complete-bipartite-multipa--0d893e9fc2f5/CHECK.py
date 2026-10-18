#!/usr/bin/env python3
"""Exact chain certificate for the bidirected K(2,4) multipath complex.
Requires Python 3 and SymPy. Reconstructs every simplex and chain operation.
"""
from itertools import combinations
from collections import Counter, defaultdict
from sympy import zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form

N = 4
ARCS = [arc for a in range(2) for b in range(N)
        for arc in ((a, 2+b), (2+b, a))]

def admissible(indices):
    nxt, previous = {}, {}
    for j in indices:
        a, b = ARCS[j]
        if a in nxt or b in previous:
            return False
        nxt[a] = b
        previous[b] = a
    for a in nxt:
        visited = set()
        while a in nxt:
            if a in visited:
                return False
            visited.add(a)
            a = nxt[a]
    return True

# Simplices are encoded by their nonzero sixteen-bit arc incidence masks.
simplices = {}
for d in range(1, 5):
    for indices in combinations(range(len(ARCS)), d):
        if admissible(indices):
            mask = sum(1 << i for i in indices)
            simplices[mask] = d-1
assert Counter(simplices.values()) == {0:16, 1:80, 2:144, 3:72}

# Lexicographic vertex matching; at each arc index, pair each remaining
# simplex with the simplex obtained by adding that arc where possible.
remaining = set(simplices)
pairs = []
for p in range(len(ARCS)):
    for s in sorted(remaining, key=lambda x: (x.bit_count(), x)):
        t = s | (1 << p)
        if s & (1 << p) == 0 and t in remaining:
            pairs.append((s,t))
            remaining.remove(s)
            remaining.remove(t)
assert len(pairs) == 147
assert Counter(simplices[s] for s in remaining) == {0:1,1:1,2:12,3:4}

# Verify Forman acyclicity by orienting every Hasse incidence downward,
# except matched incidences, which are oriented upward.
partner = {t:s for s,t in pairs}
incoming = {s:0 for s in simplices}
adjacencies = {s:[] for s in simplices}
original_boundary = {}
for t, dim in simplices.items():
    ids = [j for j in range(len(ARCS)) if t & (1 << j)]
    bd = {}
    for i, j in enumerate(ids):
        s = t ^ (1 << j)
        if s in simplices:
            bd[s] = (-1)**i
            if partner.get(t) == s:
                head, tail = t,s
            else:
                head, tail = s,t
            adjacencies[tail].append(head)
            incoming[head] += 1
    original_boundary[t] = bd
queue = [s for s,indeg in incoming.items() if indeg == 0]
visited = 0
while queue:
    s = queue.pop()
    visited += 1
    for t in adjacencies[s]:
        incoming[t] -= 1
        if incoming[t] == 0:
            queue.append(t)
assert visited == len(simplices), 'matching would contain closed gradient paths'

# Each operation below is elementary cancellation of a unit incidence
# between adjacent cellular chain groups. Such cancellations are integral
# chain-homotopy equivalences; each old boundary is updated, not assumed.
boundary = {s:bd.copy() for s,bd in original_boundary.items()}
active = set(simplices)
pending = pairs[:]
for step in range(len(pairs)):
    eligible = next((i for i,(s,t) in enumerate(pending)
                     if abs(boundary[t].get(s,0)) == 1), None)
    assert eligible is not None
    s,t = pending.pop(eligible)
    pivot = boundary[t][s]
    bd = boundary[t].copy()
    degree = simplices[t]
    for u in sorted(active):
        if u != t and simplices[u] == degree:
            coefficient = boundary[u].get(s,0)
            if coefficient:
                factor = coefficient // pivot
                for v,z in bd.items():
                    x = boundary[u].get(v,0)-factor*z
                    if x:boundary[u][v] = x
                    else:boundary[u].pop(v,None)
        if simplices[u] == degree+1:
            boundary[u].pop(t, None)
    active.remove(s);active.remove(t)
    boundary.pop(s);boundary.pop(t)
assert active == remaining
# Verify d^2=0 on every surviving cell.
for s in active:
    composition = defaultdict(int)
    for t, a in boundary[s].items():
        for v,b in boundary[t].items():
            composition[v] += a*b
    assert not any(composition.values())

def matrix(level):
    cols = sorted(s for s in active if simplices[s]==level)
    rows = sorted(s for s in active if simplices[s]==level-1)
    r = {s:i for i,s in enumerate(rows)}
    result = zeros(len(rows),len(cols))
    for j,s in enumerate(cols):
        for t,coefficient in boundary[s].items():
            result[r[t],j] = coefficient
    return result

def invariant_factors(M):
    snf = smith_normal_form(M, domain=ZZ)
    return sorted(abs(int(snf[j,j])) for j in range(min(snf.rows,snf.cols))
                  if snf[j,j])

d2, d3 = matrix(2), matrix(3)
assert d2.shape == (1,12)
assert d3.shape == (12,4)
assert d2*d3 == zeros(1,4)
assert invariant_factors(d2) == [1]
assert invariant_factors(d3) == [1,1,1,2]
print('arcs', len(ARCS))
print('f-vector', [sum(x==j for x in simplices.values()) for j in range(4)])
print('acyclic matching pairs', len(pairs))
print('critical cells', dict(sorted(Counter(simplices[s] for s in active).items())))
print('reduced boundary 2 SNF', invariant_factors(d2))
print('reduced boundary 3 SNF', invariant_factors(d3))
print('H0: Z; H1: 0; H2: Z^7 direct_sum Z/2; H3: 0')
print('all exact integral chain and acyclicity assertions passed')
