#!/usr/bin/env python3
"""Finite exact check of weak three-colouring reconfiguration of the Fano plane.

No third-party packages. Colourings are seven-tuples over {0,1,2};
point labels are the nonzero three-bit binary vectors 1,...,7.
"""
from collections import Counter, deque
from itertools import product, permutations

POINTS = tuple(range(1, 8))
LINES = tuple(sorted({tuple(sorted((a, b, a ^ b)))
                      for a in POINTS for b in POINTS if a < b}))
assert len(LINES) == 7 and all(len(line) == 3 for line in LINES)
assert all(sum(p in e for e in LINES) == 3 for p in POINTS)


def proper(x):
    return all(not (x[a-1] == x[b-1] == x[c-1]) for a,b,c in LINES)

assert sum(proper(x) for x in product(range(2), repeat=7)) == 0
C = tuple(x for x in product(range(3), repeat=7) if proper(x))
assert len(C) == 882
lookup = {x:i for i,x in enumerate(C)}
assert len(lookup) == len(C)

# The first edge construction uses explicit single-coordinate mutations.
adj = [set() for _ in C]
for i,x in enumerate(C):
    for at in range(7):
        for to in range(3):
            if to == x[at]:
                continue
            y = x[:at] + (to,) + x[at+1:]
            if y in lookup:
                adj[i].add(lookup[y])
assert all(i in adj[j] for i,ns in enumerate(adj) for j in ns)
assert sum(map(len,adj)) == 7812
assert Counter(map(len,adj)) == Counter({8:252, 9:504, 10:126})

# Independent edge construction: inspect each Hamming-one pair.
adj2 = [set() for _ in C]
for i in range(len(C)):
    for j in range(i+1,len(C)):
        if sum(a!=b for a,b in zip(C[i],C[j])) == 1:
            adj2[i].add(j); adj2[j].add(i)
assert adj == adj2

# Enumerate the 168 invertible linear maps of F_2^3 by images of a basis.
geom = []
for a in POINTS:
    for b in POINTS:
        for c in POINTS:
            if len({a,b,c,a^b,a^c,b^c,a^b^c}) != 7:
                continue
            img = tuple(((a if p&1 else 0) ^ (b if p&2 else 0) ^
                         (c if p&4 else 0)) for p in POINTS)
            geom.append(img)
geom = tuple(geom)
assert len(geom) == 168 and len(set(geom)) == 168
palette = tuple(permutations(range(3)))

# Group orbits of the colorings under Fano automorphisms and color relabelling.
unseen = set(range(len(C)))
orbits = []
while unseen:
    i = min(unseen)
    x = C[i]
    O = set()
    for g in geom:
        for perm in palette:
            y = [None]*7
            for p in POINTS:
                y[g[p-1]-1] = perm[x[p-1]]
            y = tuple(y)
            assert y in lookup
            O.add(lookup[y])
    assert O <= unseen
    unseen -= O
    orbits.append(O)
assert sorted(map(len,orbits)) == [126,252,504]

# Each orbit corresponds to one unordered color-class-size profile.
profiles = {}
for O in orbits:
    p = tuple(sorted(Counter(C[min(O)]).values()))
    assert all(tuple(sorted(Counter(C[i]).values())) == p for i in O)
    profiles[p] = O
assert {p:len(O) for p,O in profiles.items()} == {
    (1,2,4):126,(1,3,3):252,(2,2,3):504}
# A weak coloring has one rainbow line for each block lacking a same-color pair.
expected_rainbows = {(1,2,4):0, (1,3,3):1, (2,2,3):2}
for p, O in profiles.items():
    assert all(sum(len({C[i][point-1] for point in line}) == 3
                   for line in LINES) == expected_rainbows[p] for i in O)
assert {(p,tuple(sorted(Counter(tuple(sorted(Counter(C[j]).values()))
                               for j in adj[min(O)]).items())))
        for p,O in profiles.items()} == {
    ((1,2,4),(((1,2,4),2),((1,3,3),4),((2,2,3),4))),
    ((1,3,3),(((1,2,4),2),((2,2,3),6))),
    ((2,2,3),(((1,2,4),1),((1,3,3),3),((2,2,3),5)))}


def bfs(root):
    distance = [-1]*len(C)
    distance[root] = 0
    Q = deque([root])
    while Q:
        i = Q.popleft()
        for j in adj[i]:
            if distance[j] == -1:
                distance[j] = distance[i] + 1
                Q.append(j)
    return distance

# Orbit-reduced exhaustive proof. Both graph and Hamming metric have all
# automorphisms in the above group, so one source per orbit is sufficient.
exceptional_directed=0
for O in orbits:
    root=min(O)
    D=bfs(root)
    assert min(D)==0 and max(D)==7
    extra=0
    for i,x in enumerate(C):
        h=sum(a!=b for a,b in zip(C[root],x))
        assert 0 <= D[i]-h <= 1
        extra += D[i]-h
    exceptional_directed += len(O)*extra
assert exceptional_directed == 2*2268

# Completely independent source-by-source breadth-first checks. We count
# unordered pairs and record all distance/Hamming differences.
failures=Counter()
diameter=0
one_extra_example = None
seven_example = None
for root in range(len(C)):
    D = bfs(root)
    assert -1 not in D
    assert max(D) == 7
    diameter = max(diameter,max(D))
    for i in range(root+1,len(C)):
        h=sum(a!=b for a,b in zip(C[root],C[i]))
        delta=D[i]-h
        failures[delta]+=1
        assert delta in (0,1)
        if delta == 1 and one_extra_example is None:
            one_extra_example=(C[root],C[i],h,D[i])
        if D[i]==7 and seven_example is None:
            seven_example=(C[root],C[i],h,D[i])
assert failures == {0:386253,1:2268}
assert sum(failures.values()) == len(C)*(len(C)-1)//2
assert diameter == 7

# Independent inclusion-exclusion gives the weak-chromatic polynomial
# q^7-7q^5+21q^3-21q^2+6q. (A line enforces equality of its 3 colors.)
coeff=Counter()
for mask in range(1<<len(LINES)):
    parent=list(range(7))
    def find(i):
        while parent[i]!=i:
            i=parent[i]
        return i
    for k,(a,b,c) in enumerate(LINES):
        if mask & (1<<k):
            for p in (b,c):
                parent[find(p-1)] = find(a-1)
    components=len({find(i) for i in range(7)})
    coeff[components] += (-1)**mask.bit_count()
assert {k:v for k,v in coeff.items() if v} == {7:1,5:-7,3:21,2:-21,1:6}
assert sum(v*3**k for k,v in coeff.items()) == len(C)

print('PASS: Fano plane 7 lines, no proper 2-coloring')
print('PASS: 3-colorings = 882; edges = 3906; degree histogram = {8:252, 9:504, 10:126}')
print('PASS: automorphisms=168; color+geometry orbit sizes=126,252,504')
print('PASS: connected, radius = diameter = 7; exact additive Hamming excess in {0,1}')
print('PASS: unordered pairs with excess 1 = 2268, with excess 0 = 386253')
print('one-extra witness:',one_extra_example)
print('diameter witness:',seven_example)
print('PASS: independent pair construction and chromatic-polynomial count')
