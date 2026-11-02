#!/usr/bin/env python3
"""Independent combinatorial verification of binary Fano-incidence majority dynamics."""
from collections import Counter, deque
from itertools import combinations

POINTS = frozenset(range(1, 8))
LINES = tuple(sorted({tuple(sorted((a, b, a ^ b)))
                      for a in POINTS for b in POINTS if a != b}))
assert len(LINES) == 7 and all(len(t) == 3 for t in LINES)

def forward(S):
    return frozenset(j for j, line in enumerate(LINES)
                     if len(S.intersection(line)) >= 2)

def backward(T):
    return frozenset(p for p in POINTS
                     if sum(p in LINES[j] for j in T) >= 2)

sets = [frozenset(p for p in POINTS if bits & (1 << (p-1)))
        for bits in range(128)]
line_sets = [frozenset(j for j in range(7) if bits & (1 << j))
             for bits in range(128)]
proj = {S: backward(forward(S)) for S in sets}
projected = {S for S in sets if proj[S] == S}
assert all(proj[proj[S]] == proj[S] for S in sets)
assert len(projected) == 58
noncollinear_triples = {S for S in sets if len(S) == 3 and all(S != frozenset(L) for L in LINES)}
assert len(noncollinear_triples) == 28
expected = {frozenset(), POINTS} | noncollinear_triples | {POINTS - S for S in noncollinear_triples}
assert projected == expected
fibers = Counter(proj.values())
assert Counter(fibers.values()) == Counter({1:56, 36:2})

image_forward = {forward(S) for S in sets}
image_backward = {backward(T) for T in line_sets}
assert len(image_forward) == len(image_backward) == 72
assert {forward(S) for S in projected} == {T for T in line_sets if forward(backward(T)) == T}

# Complete explicit state transition in a different representation than the
# combinatorial projection above.
adj = [[] for _ in range(14)]
for j, line in enumerate(LINES):
    for p in line:
        adj[p-1].append(j+7)
        adj[j+7].append(p-1)
assert all(len(a) == 3 for a in adj)
def update(x):
    result=0
    for i, neighbors in enumerate(adj):
        if sum((x>>u)&1 for u in neighbors) >= 2:
            result |= 1 << i
    return result

N=1<<14
F=[update(x) for x in range(N)]
F2=[F[F[x]] for x in range(N)]
assert all(F[F[F2[x]]] == F2[x] for x in range(N))  # F^4=F^2
assert len(set(F)) == 72**2
assert len(set(F2)) == 58**2
assert  any(F2[x] != F[x] for x in range(N))
assert sum(F[x]==x for x in range(N)) == 58
assert sum(F2[x]==x and F[x]!=x for x in range(N)) == 3306

# Dynamical first-entry times and basins by path following from every state.
period=[]
entry=[]
orbit=[]
for x in range(N):
    history=[]
    loc={}
    y=x
    while y not in loc:
        loc[y]=len(history)
        history.append(y)
        y=F[y]
    t=loc[y]
    d=len(history)-t
    assert d in (1,2) and t<=2
    period.append(d)
    entry.append(t)
    orbit.append(tuple(sorted(history[t:])))
T=Counter((entry[x],period[x]) for x in range(N))
assert dict(T) == {(0,1):58,(0,2):3306,(1,1):126,(1,2):1694,(2,1):2464,(2,2):8736}
cycs={o for o in orbit}
assert Counter(map(len,cycs)) == {1:58,2:1653}
by_basin=Counter((len(o),sum(z==o for z in orbit)) for o in cycs)
assert by_basin == {(1,1296):2,(1,1):56,(2,2592):1,(2,72):112,(2,2):1540}
assert sum(k[1]*v for k,v in by_basin.items()) == N

# Finite-geometric proof certificate: six-cycles biject noncollinear triples.
def sixcycles():
    paths=set()
    for v in range(14):
        def rec(path):
            if len(path)==6:
                if v in adj[path[-1]]:
                    cyc=tuple(path)
                    reps=[tuple(cyc[i:]+cyc[:i]) for i in range(6)]
                    rev=list(reversed(cyc))
                    reps.extend(tuple(rev[i:]+rev[:i]) for i in range(6))
                    paths.add(min(reps))
                return
            for w in adj[path[-1]]:
                if w not in path:rec(path+[w])
        rec([v])
    return paths
C=sixcycles()
assert len(C)==28
assert {frozenset(x) for x in C} == {frozenset(range(14)) & frozenset({p-1 for p in S}|{j+7 for j in forward(S)}) for S in noncollinear_triples}
print('fano_lines:',LINES)
print('seven_site_projection: 58 fixed subsets, fibers 36,36, then 56 unit fibers')
print('one_step_image_per_shore: 72; two_step_image_per_shore: 58')
print('fixed_points: 58; primitive_two_cycles: 1653; periodic_states: 3364')
print('first_entry_by_eventual_period:',dict(sorted(T.items())))
print('orbit_basin_size_histogram:',dict(sorted(by_basin.items())))
print('heawood_six_cycles:',len(C),'and all nonconstant stable configurations are indicators/complements of six-cycles')
print('sharp identity: F^4=F^2, F^3 != F')
print('ALL ASSERTIONS PASSED')
