"""Exact finite verification of equivariant Fano-matroid homology.

Run with Python 3 using only the standard library.
"""
from itertools import combinations, product
from collections import Counter, defaultdict

V = tuple(range(1, 8))

def act(g, v):
    w = 0
    for i in range(3):
        if v & (1 << i):
            w ^= g[i]
    return w

def compose(g, h):
    return tuple(act(g, act(h, 1 << i)) for i in range(3))

E = (1, 2, 4)
G = [g for g in product(V, repeat=3) if len({act(g, v) for v in range(8)}) == 8]
assert len(G) == 168 and E in G

def perm(g):
    return {v: act(g, v) for v in V}

def cycle_type(p):
    unseen = set(p)
    result = []
    while unseen:
        v = min(unseen)
        w = v
        count = 0
        while w in unseen:
            unseen.remove(w)
            count += 1
            w = p[w]
        result.append(count)
    return tuple(sorted(result, reverse=True))

def parity(seq):
    return -1 if sum(a > b for i, a in enumerate(seq) for b in seq[i + 1:]) % 2 else 1

lines = sorted({tuple(sorted((a, b, a ^ b))) for a in V for b in V if a != b})
assert len(lines) == 7 and all(len(line) == 3 for line in lines)
triangles = [s for s in combinations(V, 3) if s not in lines]
assert len(triangles) == 28
fano = [()] + [(v,) for v in V] + list(combinations(V, 2)) + triangles

# Independent sets of the point-line incidence (Heawood) graph.
heawood = []
for mask in range(1 << 14):
    points = [V[i] for i in range(7) if mask & (1 << i)]
    selected_lines = [lines[i] for i in range(7) if mask & (1 << (7 + i))]
    if all(v not in line for v in points for line in selected_lines):
        heawood.append(tuple(i for i in range(14) if mask & (1 << i)))
assert Counter(map(len, heawood)) == {0: 1, 1: 14, 2: 70, 3: 154, 4: 147, 5: 56, 6: 14, 7: 2}

# Binary boundary ranks give an upper bound on rational Betti numbers.
def boundary_ranks(faces):
    by_size = defaultdict(list)
    for s in faces:
        by_size[len(s)].append(s)
    rank = {0: 0}
    for k in sorted(by_size):
        if not k:
            continue
        ids = {s: i for i, s in enumerate(by_size[k - 1])}
        piv = {}
        for simplex in by_size[k]:
            vector = 0
            for i in range(k):
                facet = simplex[:i] + simplex[i + 1:]
                vector ^= 1 << ids[facet]
            while vector:
                j = vector.bit_length() - 1
                if j in piv:
                    vector ^= piv[j]
                else:
                    piv[j] = vector
                    break
        rank[k] = len(piv)
    betti = {k - 1: len(by_size[k]) - rank[k] - rank.get(k + 1, 0)
             for k in range(1, max(by_size) + 1)}
    return [len(by_size[k]) for k in range(max(by_size) + 1)], rank, betti

f_counts, f_ranks, f_betti = boundary_ranks(fano)
h_counts, h_ranks, h_betti = boundary_ranks(heawood)
assert f_counts == [1, 7, 21, 28] and f_ranks == {0:0,1:1,2:6,3:15}
assert f_betti == {0:0,1:0,2:13}
assert h_ranks == {0:0,1:1,2:13,3:57,4:97,5:44,6:12,7:2}
assert h_betti == {0:0,1:0,2:0,3:6,4:0,5:0,6:0}

# Both rational homology groups are concentrated in their displayed degrees:
# mod-two Betti numbers dominate rational Betti numbers degree-by-degree,
# and the Euler characteristic forces the displayed rational ranks.
def reduced_euler(faces):
    return sum((-1) ** (len(s) - 1) for s in faces)
assert reduced_euler(fano) == 13
assert reduced_euler(heawood) == -6

def reduced_lefschetz(faces, q):
    t = 0
    for simplex in faces:
        if not simplex:
            t -= 1
            continue
        image = [q[v] for v in simplex]
        if set(image) == set(simplex):
            t += (-1) ** (len(simplex) - 1) * parity(image)
    return t

def order(g):
    x = E
    for i in range(1, 169):
        x = compose(g, x)
        if x == E:
            return i
    raise AssertionError('not a finite-order matrix')

ordmap = {g: order(g) for g in G}
assert Counter(ordmap.values()) == {1:1,2:21,3:56,4:42,7:48}

# All eight Sylow 7-subgroups are built from the matrix action, not assumed.
subgroups = set()
for g in G:
    if ordmap[g] != 7:
        continue
    elements, x = [E], E
    for _ in range(6):
        x = compose(x, g)
        elements.append(x)
    subgroups.add(frozenset(elements))
assert len(subgroups) == 8

def inverse(g):
    x = E
    for _ in range(ordmap[g] - 1):
        x = compose(x, g)
    assert compose(x, g) == E
    return x

character = defaultdict(Counter)
for g in G:
    p = perm(g)
    cls = cycle_type(p)
    q_fano = p
    q_heawood = {i: V.index(p[v]) for i, v in enumerate(V)}
    q_heawood.update({7 + i: 7 + lines.index(tuple(sorted(p[v] for v in line)))
                      for i, line in enumerate(lines)})
    cf = reduced_lefschetz(fano, q_fano)
    ch = -reduced_lefschetz(heawood, q_heawood)
    gi = inverse(g)
    fixed = sum(frozenset(compose(compose(g, h), gi) for h in subgroup) == subgroup
                for subgroup in subgroups)
    cs = fixed - 1
    assert cf == ch + cs
    character[cls][(cf, ch, cs)] += 1

expected = {
    (1,1,1,1,1,1,1): (1, (13,6,7)),
    (2,2,1,1,1): (21, (-3,-2,-1)),
    (3,3,1): (56, (1,0,1)),
    (4,2,1): (42, (1,2,-1)),
    (7,): (48, (-1,-1,0)),
}
assert set(character) == set(expected)
for cls, (number, val) in expected.items():
    assert character[cls] == Counter({val:number}), (cls, character[cls])

# The eight-Sylow augmentation character is complex irreducible.
# The Heawood character is the conjugate pair of degree-three characters.
chi_h = [(1,6),(21,-2),(56,0),(42,2),(48,-1)]
chi_s = [(1,7),(21,-1),(56,1),(42,-1),(48,0)]
assert sum(n * a * a for n,a in chi_h) == 336  # norm^2 = 2
assert sum(n * b * b for n,b in chi_s) == 168  # norm^2 = 1
assert sum(n * a * b for (n,a), (_,b) in zip(chi_h,chi_s)) == 0
print('VERIFY_OK; |G|=168; rank(Fano H2)=13; rank(Heawood H3)=6; Sylow count=8')
print('CLASS_DATA', sorted(((c,n,v) for c,(n,v) in expected.items()), key=lambda x:-x[1]))
