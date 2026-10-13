from collections import deque
from itertools import combinations

# Exact finite model for odd theta characteristics of a genus-three curve.
def bits(x):
    return [(x >> i) & 1 for i in range(6)]

def q0(x):
    b = bits(x)
    return b[0]*b[3] ^ b[1]*b[4] ^ b[2]*b[5]

def pairing(x, y):
    a, b = bits(x), bits(y)
    return (a[0]*b[3] ^ a[1]*b[4] ^ a[2]*b[5]
            ^ a[3]*b[0] ^ a[4]*b[1] ^ a[5]*b[2])

odd = [x for x in range(64) if q0(x) == 1]
assert len(odd) == 28
idx = {x: i for i, x in enumerate(odd)}

def hexad_members(v):
    members = [m for m in odd if q0(m ^ v) == 1]
    assert len(members) == 12
    return tuple(sorted(idx[m] for m in members))

hexads = {v: hexad_members(v) for v in range(1, 64)}
assert len(set(hexads.values())) == 63
hexad_by_set = {frozenset(h): v for v, h in hexads.items()}

v = 1
Hv = [odd[i] for i in hexads[v]]
seen, pairs = set(), []
for m in Hv:
    if m in seen:
        continue
    n = m ^ v
    assert n in Hv
    pairs.append((m, n))
    seen.update((m, n))
assert len(pairs) == 6
Hlist = [m for pair in pairs for m in pair]
Hpos = {idx[m]: i for i, m in enumerate(Hlist)}

def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))

def transvection(w):
    out = []
    for m in odd:
        qm = q0(w) ^ pairing(m, w)
        m2 = m if qm == 1 else m ^ w
        assert q0(m2) == 1
        out.append(idx[m2])
    return tuple(out)

def generated(gens, n):
    identity = tuple(range(n))
    group, queue = {identity}, deque([identity])
    while queue:
        g = queue.popleft()
        for s in gens:
            h = compose(s, g)
            if h not in group:
                group.add(h)
                queue.append(h)
    return group

# Stabilizer of the distinguished nonzero two-torsion class.
Uv = generated([transvection(w) for w in range(1, 64) if pairing(v, w) == 0], 28)
assert len(Uv) == 23040
restriction = {}
for g in Uv:
    r = tuple(Hpos[g[idx[m]]] for m in Hlist)
    assert r not in restriction or restriction[r] == g
    restriction[r] = g
assert len(restriction) == 23040

# Standard permutation generators for transitive group 12T31.
def cycle_perm(n, cycles):
    p = list(range(n))
    for cycle in cycles:
        c = [x - 1 for x in cycle]
        for i, a in enumerate(c):
            p[a] = c[(i + 1) % len(c)]
    return tuple(p)

a = cycle_perm(12, [(1,10,7,4), (3,6,9,12)])
b = cycle_perm(12, [(1,5,9), (2,6,10), (3,7,11), (4,8,12)])
H12 = generated([a, b], 12)
assert len(H12) == 48

# Find all invariant partitions into six two-element blocks.
block_systems = set()
for pair in combinations(range(12), 2):
    orbit = {tuple(sorted((g[pair[0]], g[pair[1]]))) for g in H12}
    if len(orbit) == 6:
        flat = [x for block in orbit for x in block]
        if len(flat) == 12 and len(set(flat)) == 12:
            block_systems.add(tuple(sorted(orbit)))
assert len(block_systems) == 1
blocks = next(iter(block_systems))
assert blocks == ((0,6),(1,7),(2,8),(3,9),(4,10),(5,11))

label = {}
for k, (x, y) in enumerate(blocks):
    label[x], label[y] = 2*k, 2*k + 1

def relabel(p):
    r = [0] * 12
    for i in range(12):
        r[label[i]] = label[p[i]]
    return tuple(r)

aH, bH = relabel(a), relabel(b)
assert aH in restriction and bH in restriction
A, B = restriction[aH], restriction[bH]
H28 = generated([A, B], 28)
assert len(H28) == 48

# Induced action on the 63 Steiner hexads / nonzero two-torsion classes.
def induced_v(g, u):
    image = frozenset(g[i] for i in hexads[u])
    return hexad_by_set[image]

Av = tuple(induced_v(A, u) - 1 for u in range(1, 64))
Bv = tuple(induced_v(B, u) - 1 for u in range(1, 64))
assert len(generated([Av, Bv], 63)) == 48

def orbit_sizes(gens, n):
    unseen, sizes = set(range(n)), []
    while unseen:
        start = min(unseen)
        orbit, queue = {start}, deque([start])
        while queue:
            x = queue.popleft()
            for g in gens:
                y = g[x]
                if y not in orbit:
                    orbit.add(y)
                    queue.append(y)
        sizes.append(len(orbit))
        unseen -= orbit
    return sorted(sizes)

assert orbit_sizes([A, B], 28) == [12, 16]
assert orbit_sizes([Av, Bv], 63) == [1, 6, 16, 16, 24]
fixed_nonzero = [u for u in range(1, 64) if induced_v(A, u) == u and induced_v(B, u) == u]
assert fixed_nonzero == [1]
print('VERIFY_OK Uv=23040 H=48 bitangent_orbits=12+16 torsion_orbits=1+6+16+16+24 rational_2torsion=2 unique_steiner=true')
