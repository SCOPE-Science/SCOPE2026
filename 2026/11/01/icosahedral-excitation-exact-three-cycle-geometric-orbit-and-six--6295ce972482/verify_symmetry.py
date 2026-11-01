"""Finite certificate for the full spatial quotient of three-cycles on the icosahedron.

Uses only Python's standard library; reads the labelled edge list, two explicit
permutations, cycle representatives produced by enumerate.cpp, and the CSV certificate.
"""
import collections
import csv
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
G = json.loads((BASE/'graph.json').read_text())
N = 12
assert G['n'] == N
edges = {tuple(sorted(e)) for e in G['edges']}
assert len(edges) == 30
adj = [set() for _ in range(N)]
for a,b in edges:
    assert 0 <= a < b < N
    adj[a].add(b)
    adj[b].add(a)
assert all(len(u) == 5 for u in adj)
for root in range(N):
    # Each vertex link is an induced 5-cycle. This bounds its stabilizer by 10.
    link = adj[root]
    assert len(link) == 5 and all(len(adj[v] & link) == 2 for v in link)
    dist = {root:0}; q = [root]
    for v in q:
        for w in adj[v]:
            if w not in dist: dist[w]=dist[v]+1; q.append(w)
    assert list(collections.Counter(dist.values()).values())  # nonempty
    assert collections.Counter(dist.values()) == {0:1, 1:5, 2:5, 3:1}
    # Each vertex at distance 2 is uniquely specified by its two root-neighbors.
    pairs = [frozenset(adj[v] & link) for v in range(N) if dist[v] == 2]
    assert len(set(pairs)) == 5 and all(len(pair) == 2 for pair in pairs)
# Stabilizer of root injects into D_5: distance-2 vertices are identified by
# their two root-neighbors, and the antipode is unique. Hence |Aut| <= 12*10.
perms = [tuple(map(int, line.split())) for line in (BASE/'aut_generators.txt').read_text().splitlines()]
assert len(perms) == 2
for p in perms:
    assert sorted(p) == list(range(N))
    assert {tuple(sorted((p[a],p[b]))) for a,b in edges} == edges
identity = tuple(range(N))
def compose(p, q): return tuple(p[q[i]] for i in range(N))
closure={identity}; stack=[identity]
while stack:
    p=stack.pop()
    for q in perms:
        r=compose(p,q)
        if r not in closure: closure.add(r); stack.append(r)
assert len(closure) == 120
# The upper and lower bounds identify the full graph automorphism group.
pw = [3**i for i in range(N)]
def step(s):
    x = [(s//pw[i])%3 for i in range(N)]
    return sum(((u+1)%3 if u else int(any(x[j] == 1 for j in adj[i])))*pw[i]
               for i,u in enumerate(x))
def temporal_rep(s):
    a=step(s); b=step(a)
    assert step(b) == s
    return min(s,a,b)
def permute_state(s,p):
    return sum(((s//pw[i])%3)*pw[p[i]] for i in range(N))
rep_section=(BASE/'stats.txt').read_text().split('reps period state\n')[1].splitlines()
three_reps={int(s) for p,s in (line.split() for line in rep_section) if int(p)==3}
assert len(three_reps) == 48400
all_orbits={temporal_rep(s) for s in three_reps}
assert len(all_orbits) == 48400
visited=set(); classes=[]
for s in sorted(all_orbits):
    if s in visited:continue
    grouporbit={s};queue=[s]
    for v in queue:
        for p in perms:
            t=temporal_rep(permute_state(v,p))
            if t not in grouporbit:grouporbit.add(t);queue.append(t)
    assert grouporbit <= all_orbits
    visited.update(grouporbit)
    classes.append((s,len(grouporbit)))
assert len(visited)==len(all_orbits)==48400
assert len(classes)==473
hist=collections.Counter(z for _,z in classes)
assert hist == {5:2,20:4,30:11,40:10,60:99,120:347}
with (BASE/'symmetry_classes.csv').open() as f:
    recorded = [(int(row['representative_ternary_integer']),int(row['spatial_orbit_size']))
                for row in csv.DictReader(f)]
assert classes == recorded
# The 60 states attaining first-entry time six comprise one spatial orbit.
late_line=next(line for line in (BASE/'direct_output.txt').read_text().splitlines() if line.startswith('late_states '))
late={int(x) for x in late_line[len('late_states '):].split(',') if x}
assert len(late)==60
late_orbit={permute_state(min(late),p) for p in closure}
assert late_orbit == late
print('AUT_ORDER 120; THREE_CYCLES 48400; GEOMETRIC_CLASSES 473')
print('EXTREMAL_TRANSIENT_STATES 60; ONE_SPATIAL_ORBIT')
print('CLASS_SIZES',dict(sorted(hist.items())))
print('CHECK_OK')
