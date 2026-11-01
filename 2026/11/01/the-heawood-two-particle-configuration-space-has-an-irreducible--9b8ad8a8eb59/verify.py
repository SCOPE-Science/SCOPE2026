#!/usr/bin/env python3
"""Exact combinatorial verification of Heawood two-configuration homology characters.
Runs with the Python 3 standard library; requires no external data.
"""
from collections import Counter, defaultdict
from itertools import combinations, product

F = range(1, 8)
lines = sorted({tuple(sorted((a, b, a ^ b))) for a, b in combinations(F, 2)})
assert len(lines) == 7 and all(len(set(q)) == 3 for q in lines)
lix = {L: i for i, L in enumerate(lines)}
E = sorted((p - 1, 7 + i) for i, L in enumerate(lines) for p in L)
eix = {e: i for i, e in enumerate(E)}
V0 = list(combinations(range(14), 2))
V1 = [(v, i) for v in range(14) for i, (a, b) in enumerate(E) if v != a and v != b]
V2 = [(i, j) for i, j in combinations(range(21), 2) if len(set(E[i] + E[j])) == 4]
v0ix, v1ix, v2ix = ({v: i for i, v in enumerate(z)} for z in (V0, V1, V2))
assert (len(E), len(V0), len(V1), len(V2)) == (21, 91, 252, 168)

D1 = []
for v, i in V1:
    a, b = E[i]
    D1.append({v0ix[tuple(sorted((v, b)))]: 1,
               v0ix[tuple(sorted((v, a)))]: -1})
D2 = []
for i, j in V2:
    a, b = E[i]; c, d = E[j]
    D2.append({v1ix[(b, j)]: 1, v1ix[(a, j)]: -1,
               v1ix[(d, i)]: -1, v1ix[(c, i)]: 1})
for col in D2:
    chain = defaultdict(int)
    for row, coeff in col.items():
        for vertex, val in D1[row].items():
            chain[vertex] += coeff * val
    assert all(x == 0 for x in chain.values())

def modular_rank(cols, prime):
    pivots = {}
    for col in cols:
        vec = {k: (c % prime) for k, c in col.items() if c % prime}
        while vec:
            k = max(vec)
            c = vec[k]
            if k not in pivots:
                ic = pow(c, -1, prime)
                pivots[k] = {j: (v * ic) % prime for j, v in vec.items()}
                break
            for j, v in pivots[k].items():
                d = (vec.get(j, 0) - c * v) % prime
                if d: vec[j] = d
                else: vec.pop(j, None)
    return len(pivots)

assert modular_rank(D1, 3) == 90
assert modular_rank(D2, 3) == 154
assert modular_rank(D2, 2) == 153
N = {v: set() for v in range(14)}
for a, b in E:
    N[a].add(b); N[b].add(a)

def canonical(s):
    r = list(reversed(s))
    return min(
        [tuple(s[i:] + s[:i]) for i in range(6)] +
        [tuple(r[i:] + r[:i]) for i in range(6)])

cycles = set()
def search(path):
    if len(path) == 6:
        if path[0] in N[path[-1]]:
            cycles.add(canonical(path))
        return
    for w in sorted(N[path[-1]]):
        if w not in path: search(path + [w])
for s in range(14): search([s])
assert len(cycles) == 28
cycle_chains = []
for t in sorted(cycles):
    z = {}
    for i in range(6):
        a, b = t[i], t[(i + 1) % 6]
        z[eix[tuple(sorted((a, b)))]] = 1 if a < b else -1
    cycle_chains.append((set(t), z))
assert modular_rank([z for _, z in cycle_chains], 3) == 8

tori = []
for i, (v, a) in enumerate(cycle_chains):
    for j, (w, b) in enumerate(cycle_chains):
        if i >= j or v & w: continue
        col = {}
        for x, sx in a.items():
            for y, sy in b.items():
                u, z = sorted((x, y))
                col[v2ix[(u, z)]] = sx * sy * (1 if x < y else -1)
        assert len(col) == 36
        boundary = defaultdict(int)
        for square, coeff in col.items():
            for row, val in D2[square].items():
                boundary[row] += coeff * val
        assert all(n == 0 for n in boundary.values())
        tori.append(col)
assert len(tori) == 42
assert modular_rank(tori, 3) == 14
# Rank(D2)>=154 over Q by the nonzero characteristic-three minors.
# The 14 torus cycles show dim ker(D2)>=14, hence rank(D2)=154 over Q.
# Connectedness follows from rank(D1)=90 over Q. Thus b=(1,8,14).

apply = lambda rows, v: sum(((m & v).bit_count() & 1) << i for i, m in enumerate(rows))
linear = []
for m in product(range(8), repeat=3):
    if set(apply(m, p) for p in F) != set(F): continue
    points = {p: apply(m, p) for p in F}
    image = [points[p] - 1 for p in F]
    image.extend(7 + lix[tuple(sorted(points[p] for p in L))] for L in lines)
    linear.append(tuple(image))
assert len(set(linear)) == 168
normals = {i: next(w for w in F if all((w & p).bit_count() % 2 == 0 for p in L))
           for i, L in enumerate(lines)}
normal_index = {w: i for i, w in normals.items()}
dual = tuple([7 + normal_index[p] for p in F] + [normals[i] - 1 for i in range(7)])
assert tuple(dual[dual[i]] for i in range(14)) == tuple(range(14))
G = linear + [tuple(dual[g[v]] for v in range(14)) for g in linear]
assert len(set(G)) == 336

def ord_g(g):
    out = list(range(14))
    for k in range(1, 17):
        out = [g[v] for v in out]
        if out == list(range(14)): return k
    raise AssertionError('unrecognized group order')

classes = Counter()
ch1, ch2 = [], []
for idx, g in enumerate(G):
    assert {tuple(sorted((g[a], g[b]))) for a, b in E} == set(E)
    fix_v = sum(g[v] == v for v in range(14))
    emap, esign = [], []
    signed_fixed_edges = 0
    for a, b in E:
        c, d = g[a], g[b]
        target = eix[tuple(sorted((c, d)))]
        emap.append(target)
        esign.append(1 if c < d else -1)
    for i in range(21):
        if emap[i] == i: signed_fixed_edges += esign[i]
    t1 = signed_fixed_edges - fix_v + 1
    t0cells = sum(tuple(sorted((g[a], g[b]))) == (a, b) for a, b in V0)
    t1cells = sum(esign[i] for v, i in V1 if g[v] == v and emap[i] == i)
    t2cells = 0
    for i, j in V2:
        if (emap[i], emap[j]) == (i, j):
            t2cells += esign[i] * esign[j]
        if (emap[i], emap[j]) == (j, i):
            t2cells -= esign[i] * esign[j]
    t2 = t0cells - t1cells + t2cells - 1 + t1
    ch1.append(t1); ch2.append(t2)
    classes[('collineation' if idx < 168 else 'duality', ord_g(g), t1, t2)] += 1
expected = {
    ('collineation',1,8,14):1,
    ('collineation',2,0,-2):21,
    ('collineation',3,-1,-1):56,
    ('collineation',4,0,2):42,
    ('collineation',7,1,0):48,
    ('duality',2,-2,-2):28,
    ('duality',6,1,1):56,
    ('duality',8,0,0):84,
}
assert dict(classes) == expected
inner = lambda a, b: sum(x*y for x,y in zip(a,b))
w6 = [a - b for a, b in zip(ch2, ch1)]
assert (inner(ch1,ch1),inner(ch2,ch2),inner(ch1,ch2),inner(w6,w6)) == (336,672,336,336)
assert sum(ch1) == sum(ch2) == sum(w6) == 0
print('cells: C0=91 C1=252 C2=168; rank over F3: d1=90 d2=154')
print('28 hexagons; 42 disjoint-cycle product tori; torus rank over F3=14')
print('rational Betti ranks: (1,8,14)')
for key, count in sorted(classes.items()): print('character class', key, 'size', count)
print('character pairings |G|=336: <H1,H1>=1 <H2,H2>=2 <H1,H2>=1 <W6,W6>=1')
print('VERIFY_OK')
