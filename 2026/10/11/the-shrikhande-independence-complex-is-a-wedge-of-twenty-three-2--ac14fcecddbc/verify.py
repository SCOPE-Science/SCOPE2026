#!/usr/bin/env python3
from collections import Counter, deque
import json

V = list(range(16))
coord = lambda i: (i // 4, i % 4)
D = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
adj = [0] * 16
edges = []
for u in V:
    a,b = coord(u)
    for v in range(u+1,16):
        c,d = coord(v)
        if ((c-a) % 4, (d-b) % 4) in D:
            edges.append((u,v))
            adj[u] |= 1 << v
            adj[v] |= 1 << u

assert len(edges) == 48
assert all(x.bit_count() == 6 for x in adj)
for u in V:
    for v in range(u+1,16):
        assert (adj[u] & adj[v]).bit_count() == 2

faces = []
bydim = {}
for m in range(1, 1 << 16):
    ok = True
    x = m
    while x:
        bit = x & -x
        u = bit.bit_length() - 1
        if adj[u] & (m ^ bit):
            ok = False
            break
        x -= bit
    if ok:
        faces.append(m)
        bydim.setdefault(m.bit_count()-1, []).append(m)

f_vector = tuple(len(bydim.get(d, [])) for d in range(max(bydim)+1))
assert len(faces) == 200
assert f_vector == (16,72,96,16)

# Repeated vertex toggles on the current unmatched face set.
order = [1,8,2,14,12,7,10,3,6,9,0,13,4,11,15,5]
unmatched = set(faces)
pairs = []
for v in order:
    bit = 1 << v
    for f in sorted(list(unmatched)):
        if f not in unmatched or (f & bit):
            continue
        g = f | bit
        if g in unmatched:
            unmatched.remove(f)
            unmatched.remove(g)
            pairs.append((f,g))

critical = sorted(unmatched)
critical_dimensions = Counter(m.bit_count()-1 for m in critical)
assert len(pairs) == 88
assert critical_dimensions == Counter({2:23,0:1})

face_set = set(faces)
covers = []
for g in faces:
    if g.bit_count() < 2:
        continue
    x = g
    while x:
        bit = x & -x
        f = g ^ bit
        if f in face_set:
            covers.append((f,g))
        x -= bit
assert len(covers) == 496

# Forman orientation: reverse matched Hasse arrows and retain all others downward.
pairset = set(pairs)
out = {f: [] for f in faces}
indeg = {f: 0 for f in faces}
for f,g in covers:
    a,b = (f,g) if (f,g) in pairset else (g,f)
    out[a].append(b)
    indeg[b] += 1
q = deque(x for x in faces if indeg[x] == 0)
seen = 0
while q:
    x = q.popleft()
    seen += 1
    for y in out[x]:
        indeg[y] -= 1
        if indeg[y] == 0:
            q.append(y)
assert seen == len(faces)

def gf2_rank(columns):
    basis = {}
    for x in columns:
        while x:
            p = x.bit_length()-1
            if p in basis:
                x ^= basis[p]
            else:
                basis[p] = x
                break
    return len(basis)

ranks = []
for d in range(1, max(bydim)+1):
    lower = bydim[d-1]
    idx = {m:i for i,m in enumerate(lower)}
    columns = []
    for g in bydim[d]:
        col = 0
        x = g
        while x:
            bit = x & -x
            col ^= 1 << idx[g ^ bit]
            x -= bit
        columns.append(col)
    ranks.append(gf2_rank(columns))
assert ranks == [15,57,16]

n = [len(bydim[d]) for d in range(max(bydim)+1)]
rr = [0] + ranks + [0]
betti = [n[d] - rr[d] - rr[d+1] for d in range(len(n))]
assert betti == [1,0,23,0]

summary = {
    'vertices': 16,
    'edges': 48,
    'srg_parameters': [16,6,2,2],
    'nonempty_faces': len(faces),
    'f_vector': list(f_vector),
    'hasse_covers': len(covers),
    'morse_pairs': len(pairs),
    'critical_cells_by_dimension': {str(k):v for k,v in sorted(critical_dimensions.items())},
    'mod2_boundary_ranks': ranks,
    'ordinary_mod2_betti': betti,
}
print(json.dumps(summary, sort_keys=True))
print('VERIFY_OK')
