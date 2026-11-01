#!/usr/bin/env python3
"""Exhaustive integral Morse certificate for the Morse complex of the 3-cube.

Usage: python3 verify_cube_morse.py
Only Python standard library is required. A face is a bit mask on the 24
vertex-edge incidences (u, {u,v}), with u and v binary integers 0..7.
"""
import collections
import functools
import itertools

N = 8
neighbors = [[u ^ (1 << j) for j in range(3)] for u in range(N)]
undirected = [(u, v) for u in range(N) for v in neighbors[u] if u < v]
arcs = [(u, v) for u in range(N) for v in neighbors[u]]
arc_idx = {e: i for i, e in enumerate(arcs)}
assert len(undirected) == 12 and len(arcs) == 24


def acyclic_outmap(t):
    used_edges = set()
    for u, v in enumerate(t):
        if v == -1:
            continue
        e = (min(u, v), max(u, v))
        if e in used_edges:
            return False
        used_edges.add(e)
    for start in range(N):
        seen = set()
        v = start
        while v != -1:
            if v in seen:
                return False
            seen.add(v)
            v = t[v]
    return True


def to_mask(t):
    return sum(1 << arc_idx[u, v] for u, v in enumerate(t) if v != -1)


# Exhaustive enumeration via all 4^8 choices of a possible outgoing arc.
faces = set()
for choices in itertools.product(range(4), repeat=8):
    t = [neighbors[u][j-1] if j else -1 for u, j in enumerate(choices)]
    if acyclic_outmap(t):
        faces.add(to_mask(t))
assert len(faces) == 23625 and 0 in faces

# Independent enumeration via ALL undirected cube forests and all component
# roots. A root choice uniquely orients each tree towards its root.
faces2 = set()
for e_mask in range(1 << len(undirected)):
    parent = list(range(N))

    def root(x):
        while x != parent[x]:
            x = parent[x]
        return x

    adj = [[] for _ in range(N)]
    forest = True
    for i, (a, b) in enumerate(undirected):
        if e_mask >> i & 1:
            ra, rb = root(a), root(b)
            if ra == rb:
                forest = False
                break
            parent[ra] = rb
            adj[a].append(b)
            adj[b].append(a)
    if not forest:
        continue
    comps = collections.defaultdict(list)
    for v in range(N):
        comps[root(v)].append(v)
    for roots in itertools.product(*comps.values()):
        t = [-1] * N
        for r in roots:
            seen = {r}
            stack = [r]
            while stack:
                v = stack.pop()
                for w in adj[v]:
                    if w not in seen:
                        seen.add(w)
                        t[w] = v
                        stack.append(w)
        faces2.add(to_mask(t))
assert faces == faces2

fvector = tuple(sum(m.bit_count() == k + 1 for m in faces) for k in range(7))
assert fvector == (24, 240, 1296, 4080, 7488, 7424, 3072)
assert max(m.bit_count() for m in faces) == 7


def boundary(face):
    ones = [i for i in range(24) if face & (1 << i)]
    return [(face ^ (1 << bit), 1 if rank % 2 == 0 else -1)
            for rank, bit in enumerate(ones)]


# Compute all augmented mod-2 simplicial boundary ranks independently.
chains = [[m for m in sorted(faces) if m.bit_count() == n]
          for n in range(0, 8)]
mod2ranks = []
for k in range(1, 8):
    lower_index = {x: i for i, x in enumerate(chains[k - 1])}
    basis = {}
    for cell in chains[k]:
        v = 0
        for face, _ in boundary(cell):
            v ^= 1 << lower_index[face]
        while v:
            p = v.bit_length() - 1
            if p not in basis:
                basis[p] = v
                break
            v ^= basis[p]
    mod2ranks.append(len(basis))
assert mod2ranks == [1, 23, 217, 1079, 3001, 4487, 2933], mod2ranks

# Acyclic greedy pivot matching on ALL nonempty faces. It must be verified,
# rather than assumed acyclic on the strength of its construction.
remaining = faces - {0}
pairs = []
for pivot in range(24):
    chosen = [(f, f | (1 << pivot)) for f in sorted(remaining)
              if not (f & (1 << pivot)) and (f | (1 << pivot)) in remaining]
    assert len({v for p in chosen for v in p}) == 2 * len(chosen)
    for a, b in chosen:
        remaining.remove(a)
        remaining.remove(b)
    pairs.extend(chosen)

lower_to_upper = dict(pairs)
upper_to_lower = {b: a for a, b in pairs}
critical = set(remaining)
assert len(pairs) == 11697
assert collections.Counter(m.bit_count()-1 for m in critical) == {0: 1, 5: 47, 6: 182}

# Full directed Hasse graph: matched incidences lower->upper, others
# upper->lower. Kahn's algorithm must remove every nonempty simplex.
indeg = {m: 0 for m in faces if m}
succ = collections.defaultdict(list)
hasse = 0
for upper in indeg:
    if upper.bit_count() == 1:
        continue
    for low, _ in boundary(upper):
        if low == 0:
            continue
        if lower_to_upper.get(low) == upper:
            src, dst = low, upper
        else:
            src, dst = upper, low
        succ[src].append(dst)
        indeg[dst] += 1
        hasse += 1
q = collections.deque(v for v, d in indeg.items() if d == 0)
visited = 0
while q:
    v = q.popleft()
    visited += 1
    for w in succ[v]:
        indeg[w] -= 1
        if not indeg[w]:
            q.append(w)
assert visited == len(faces) - 1, (visited, len(faces)-1)

# The degree-(6 to 5) integral Morse boundary is the path-sum boundary.
# If a 5-face a is paired with 6-face b, solve its elementary incidence
# equation a= -s(a,b)^(-1) sum_{c!=a} s(c,b)c, recursively. If a is paired
# with a 4-face, it contributes zero in degree five.
crit5 = sorted(x for x in critical if x.bit_count() == 6)
crit6 = sorted(x for x in critical if x.bit_count() == 7)
i5 = {x: i for i, x in enumerate(crit5)}
active = set()

@functools.lru_cache(None)
def reduce5(a):
    if a in i5:
        return {i5[a]: 1}
    b = lower_to_upper.get(a)
    if b is None:
        assert a in upper_to_lower and a.bit_count() == 6
        return {}
    assert b.bit_count() == 7 and a not in active
    active.add(a)
    bd = boundary(b)
    s = next(s for x, s in bd if x == a)
    out = collections.defaultdict(int)
    for c, t in bd:
        if c == a:
            continue
        for i, val in reduce5(c).items():
            out[i] -= s * t * val
    active.remove(a)
    return {k: v for k, v in out.items() if v}

A = [[0] * len(crit6) for _ in crit5]
for j, cell in enumerate(crit6):
    for face, sign in boundary(cell):
        for i, val in reduce5(face).items():
            A[i][j] += sign * val
assert max(abs(x) for row in A for x in row) == 1

# Entirely integral row/column elimination. Every pivot must be exactly
# +1 or -1. Each step is a change of integral bases, so at termination the
# nonzero diagonal is the integral Smith form if the remaining block is zero.
B = [row[:] for row in A]
nr, nc = len(B), len(B[0])
unit_pivots = 0
for p in range(min(nr, nc)):
    opts = [(sum(B[i][k] != 0 for k in range(p, nc)) *
             sum(B[k][j] != 0 for k in range(p, nr)), i, j)
            for i in range(p, nr) for j in range(p, nc) if abs(B[i][j]) == 1]
    if not opts:
        break
    _, i, j = min(opts)
    B[p], B[i] = B[i], B[p]
    for row in B:
        row[p], row[j] = row[j], row[p]
    sign = B[p][p]
    if sign == -1:
        B[p] = [-a for a in B[p]]
    assert B[p][p] == 1
    for i in range(p+1, nr):
        mul = B[i][p]
        if mul:
            B[i] = [B[i][c] - mul * B[p][c] for c in range(nc)]
    for j in range(p+1, nc):
        mul = B[p][j]
        if mul:
            for i in range(nr):
                B[i][j] -= mul * B[i][p]
    assert all(B[i][p] == 0 for i in range(p+1, nr))
    assert all(B[p][j] == 0 for j in range(p+1, nc))
    unit_pivots += 1
assert unit_pivots == 43 and all(B[i][j] == 0 for i in range(unit_pivots, nr)
                                   for j in range(unit_pivots, nc))
assert all(B[i][i] == 1 for i in range(unit_pivots))
assert len(crit5) - unit_pivots == 4 and len(crit6) - unit_pivots == 139

print('FACE_VECTOR', fvector)
print('AUGMENTED_MOD2_BOUNDARY_RANKS', tuple(mod2ranks))
print('TOTAL_FACES', len(faces), 'MATCHING_PAIRS', len(pairs),
      'HASSE_INCIDENCES', hasse, 'DAG_VERTICES', visited)
print('CRITICAL_CELLS', {0: 1, 5: len(crit5), 6: len(crit6)})
print('SIGNED_MORSE_BOUNDARY', (len(A), len(A[0])),
      'NONZERO', sum(x != 0 for row in A for x in row))
print('INTEGER_UNIT_PIVOTS', unit_pivots, 'RESIDUAL_BLOCK_ZERO', True)
print('REDUCED_HOMOLOGY', {'H5': 'Z^4', 'H6': 'Z^139', 'other': '0'})
print('CUBE_MORSE_INTEGRAL_WEDGE_VERIFIED')
