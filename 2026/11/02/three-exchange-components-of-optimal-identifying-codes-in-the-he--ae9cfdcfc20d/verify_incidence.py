#!/usr/bin/env python3
"""Complete bitmask certificate for radius-one identifying-code exchanges on H."""
from collections import Counter, deque
from itertools import combinations

# P_0,...,P_6 and L_0,...,L_6. L_i contains P_i,P_(i+1),P_(i+3).
LINES = [frozenset(((i + d) % 7) for d in (0, 1, 3)) for i in range(7)]
assert len(set(LINES)) == 7
assert all(len(s) == 3 for s in LINES)
assert all(sum(p in l for l in LINES) == 3 for p in range(7))
assert all(sum({p,q} <= l for l in LINES) == 1 for p in range(7) for q in range(p + 1, 7))
closed = [(1 << v) for v in range(14)]
for li, line in enumerate(LINES):
    for p in line:
        closed[p] |= 1 << (7 + li)
        closed[7 + li] |= 1 << p
assert all(x.bit_count() == 4 for x in closed)

def is_code(mask):
    signatures = [mask & neighborhood for neighborhood in closed]
    return 0 not in signatures and len(set(signatures)) == 14

# The enumeration includes every subset of cardinality at most 7, hence
# excludes every smaller identifying code independently of any general bound.
counts = {}
for k in range(8):
    candidates = (sum(1 << v for v in tuple_) for tuple_ in combinations(range(14), k))
    good = [s for s in candidates if is_code(s)]
    counts[k] = len(good)
    if k == 7:
        states = sorted(good)
assert [counts[k] for k in range(8)] == [0,0,0,0,0,0,0,268]
assert len(states) == len(set(states))
assert Counter((s & 127).bit_count() for s in states) == {0:1,1:21,3:112,4:112,6:21,7:1}
assert all((s & 127).bit_count() != 2 and (s & 127).bit_count() != 5 for s in states)
triple_types = Counter()
for s in states:
    if (s & 127).bit_count() == 3:
        points = frozenset(i for i in range(7) if (s >> i) & 1)
        triple_types[points in LINES] += 1
assert triple_types == {True:28, False:84}
# Every line-supported three-point set extends to exactly four codes;
# every noncollinear point triple extends to exactly three.
triple_multiplicity = Counter()
for s in states:
    if (s & 127).bit_count() != 3: continue
    triple = frozenset(i for i in range(7) if s & (1 << i))
    triple_multiplicity[triple] += 1
assert len(triple_multiplicity) == 35
assert all(triple_multiplicity[t] == (4 if t in LINES else 3)
           for t in triple_multiplicity)

# A one-swap edge has a two-bit symmetric difference. At most two swaps means
# a nonzero difference of two OR four bits; exact-two means four bits only.
def exchange_graph(max_swaps, exact=False):
    nbr = [set() for _ in states]
    for a, sa in enumerate(states):
        for b in range(a + 1, len(states)):
            bits = (sa ^ states[b]).bit_count()
            if ((bits == 2 * max_swaps) if exact else (0 < bits <= 2 * max_swaps)):
                nbr[a].add(b)
                nbr[b].add(a)
    return nbr

def components(nbr):
    seen = set()
    answer = []
    for v in range(len(states)):
        if v in seen: continue
        comp = [v]
        seen.add(v)
        for a in comp:
            for b in nbr[a]:
                if b not in seen:
                    seen.add(b)
                    comp.append(b)
        answer.append(set(comp))
    assert sum(map(len, answer)) == len(states)
    return answer

def distances(nbr, start):
    dist = {start: 0}
    q = deque([start])
    while q:
        a = q.popleft()
        for b in nbr[a]:
            if b not in dist:
                dist[b] = dist[a] + 1
                q.append(b)
    return dist

r1 = exchange_graph(1)
assert sum(map(len, r1)) // 2 == 658
assert Counter(map(len, r1)) == {21:2,5:210,4:56}
comps = components(r1)
assert sorted(map(len, comps)) == [22,22,224]
assert sorted(sum(len(r1[i]) for i in cc) // 2 for cc in comps) == [63,63,532]
assert sorted((min(max(distances(r1,i).values()) for i in cc),
               max(max(distances(r1,i).values()) for i in cc)) for cc in comps) == [(1,2),(1,2),(6,6)]

# The two small components are K1 join L(H), where L(H) is the line graph of
# H. A leaf state is indexed by an incident point-line flag (p,l).
for cc in comps:
    if len(cc) != 22: continue
    center = next(i for i in cc if (states[i] & 127).bit_count() in (0,7))
    leaves = cc - {center}
    assert r1[center] == leaves
    flags = {}
    for i in leaves:
        s = states[i]
        pcount = (s & 127).bit_count()
        if pcount == 1:
            p = next(j for j in range(7) if (s >> j) & 1)
            l = next(j for j in range(7) if not (s >> (7 + j)) & 1)
        else:
            p = next(j for j in range(7) if not (s >> j) & 1)
            l = next(j for j in range(7) if (s >> (7 + j)) & 1)
        assert p in LINES[l]
        flags[i] = (p,l)
    assert len(set(flags.values())) == 21
    for i in leaves:
        for j in leaves:
            if i == j: continue
            (p,l),(q,m) = flags[i],flags[j]
            assert (j in r1[i]) == (p == q or l == m)

r2_exact = exchange_graph(2, exact=True)
assert sorted(map(len, components(r2_exact))) == [1,1,266]
r2 = exchange_graph(2)
assert len(components(r2)) == 1
assert sum(map(len,r2)) // 2 == 4438
r2_ecc = Counter(max(distances(r2,i).values()) for i in range(len(states)))
assert r2_ecc == {3:224,4:42,5:2}
assert max(r2_ecc) == 5
idx = {s:i for i,s in enumerate(states)}
all_points = (1 << 7) - 1
all_lines = ((1 << 14)-1) ^ all_points
assert distances(r2,idx[all_points])[idx[all_lines]] == 5
print('HEAWOOD_IDENTIFY_BITMASK_EXHAUSTIVE_PASS')
print('optimal=268 single_edges=658 single_components=22,22,224')
print('two_or_fewer_edges=4438 two_or_fewer_diameter=5')
