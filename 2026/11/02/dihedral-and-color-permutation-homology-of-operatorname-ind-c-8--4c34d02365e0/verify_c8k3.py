#!/usr/bin/env python3
"""Exact finite certificate for the C8 categorical K3 independence complex.

Requires Python 3.10+ standard library only.  Vertex (i,a) has label 3*i+a.
The complex contains all nonempty independent subsets of the 24 vertices.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import permutations

N = 24
ADJ = [0] * N
for u in range(N):
    i, a = divmod(u, 3)
    for v in range(N):
        j, b = divmod(v, 3)
        if (i-j) % 8 in (1, 7) and a != b:
            ADJ[u] |= 1 << v

all_faces = {0}
for v in range(N):
    bit = 1 << v
    all_faces |= {f | bit for f in list(all_faces) if not (f & ADJ[v])}
assert len(all_faces) == 18722
assert [Counter(f.bit_count()-1 for f in all_faces)[j] for j in range(12)] == [24,228,1112,3042,4848,4652,2880,1305,472,132,24,2]

# A deterministic partial matching of the nonempty face poset.
unmatched = set(all_faces) - {0}
mate = {}
for v in range(N):
    bit = 1 << v
    lowers = [f for f in unmatched if not (f & bit) and (f | bit) in unmatched]
    for lo in lowers:
        hi = lo | bit
        mate[lo] = hi
        mate[hi] = lo
    unmatched.difference_update(lowers)
    unmatched.difference_update(f | bit for f in lowers)
critical = set(unmatched)
assert len(mate) == 18706
assert Counter(f.bit_count()-1 for f in critical) == {0:1, 4:6, 5:8}

def boundary(mask):
    vertices = [v for v in range(N) if mask >> v & 1]
    return [(1 if pos % 2 == 0 else -1, mask ^ (1 << v))
            for pos, v in enumerate(vertices)]

# Orient unmatched Hasse covers downwards and matched covers upwards.
links = defaultdict(list)
indegree = defaultdict(int)
for upper in all_faces - {0}:
    for sign, lower in boundary(upper):
        if lower == 0:
            continue
        if mate.get(lower) == upper:
            src, dst = lower, upper
        else:
            src, dst = upper, lower
        links[src].append(dst)
        indegree[dst] += 1
q = deque(x for x in all_faces - {0} if indegree[x] == 0)
seen = 0
while q:
    u = q.popleft()
    seen += 1
    for v in links[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)
assert seen == len(all_faces) - 1, 'Matching is not acyclic'

# Projection along matched pairs, with integral incidence +/-1.
@lru_cache(None)
def project(mask):
    if mask in critical:
        return {mask:1}
    paired = mate[mask]
    if paired.bit_count() < mask.bit_count():
        return {}  # Matched upper cell.
    incidence = next(c for c, low in boundary(paired) if low == mask)
    out = defaultdict(int)
    for sign, low in boundary(paired):
        if low != mask:
            for basis, mult in project(low).items():
                out[basis] -= incidence * sign * mult
    return {basis:mult for basis,mult in out.items() if mult}

c4 = sorted(x for x in critical if x.bit_count() == 5)
c5 = sorted(x for x in critical if x.bit_count() == 6)
M = [[0 for _ in c5] for _ in c4]
for j, upper in enumerate(c5):
    projected_boundary = defaultdict(int)
    for sign, lower in boundary(upper):
        for cell, mult in project(lower).items():
            projected_boundary[cell] += sign * mult
    for i, cell in enumerate(c4):
        M[i][j] = projected_boundary[cell]
assert M == [
 [0,-1,0,0,0,-1,0,0],
 [0,0,-1,0,0,0,-1,0],
 [0,-1,0,-1,0,0,0,0],
 [0,0,-1,-1,0,0,0,0],
 [0,0,0,0,-1,0,-1,0],
 [0,0,0,0,-1,-1,0,0],
]
PHI = [-1,1,1,-1,-1,1]
assert all(sum(PHI[i]*M[i][j] for i in range(6)) == 0 for j in range(8))

def det(rows):
    if len(rows) == 1:
        return rows[0][0]
    return sum((-1 if j % 2 else 1) * a *
               det([r[:j]+r[j+1:] for r in rows[1:]])
               for j,a in enumerate(rows[0]) if a)
assert det([[M[i][j] for j in (1,2,3,4,5)] for i in (0,1,2,3,4)]) == 1
# The left-null vector and unimodular rank-five minor give rank five and
# five unit Smith invariants; hence H4=Z, H5=Z^3, with no torsion.

# Check that PHI after projection is a cocycle on every original 5-chain.
for upper in all_faces:
    if upper.bit_count() != 6:
        continue
    coefficient = defaultdict(int)
    for sign, lower in boundary(upper):
        for z,c in project(lower).items():
            coefficient[z] += sign*c
    assert sum(PHI[i]*coefficient[c4[i]] for i in range(6)) == 0

# Lift one critical 4-cell to a closed integral 4-chain.
low3 = [lo for lo, hi in mate.items()
        if lo.bit_count() == 4 and hi.bit_count() == 5]
low3set = set(low3)
assert len(low3set) == len(low3)
dep = defaultdict(list)
degree = {lo:0 for lo in low3}
for lo in low3:
    upper = mate[lo]
    for sign, low in boundary(upper):
        if low != lo and low in low3set:
            dep[lo].append(low)
            degree[low] += 1
q = deque(x for x in low3 if degree[x] == 0)
order = []
while q:
    lo = q.popleft()
    order.append(lo)
    for v in dep[lo]:
        degree[v] -= 1
        if degree[v] == 0:
            q.append(v)
assert len(order) == len(low3)

z = defaultdict(int, {c4[0]:1})
partial = defaultdict(int)
for sign, lower in boundary(c4[0]):
    partial[lower] += sign
for lo in order:
    amount = partial[lo]
    if amount:
        upper = mate[lo]
        incidence = next(c for c, y in boundary(upper) if y == lo)
        mult = -amount * incidence
        z[upper] += mult
        for sign, lower in boundary(upper):
            partial[lower] += sign * mult
assert all(v == 0 for v in partial.values())
z = {x:v for x,v in z.items() if v}
assert len(z) == 66

def phi_chain(chain):
    out = defaultdict(int)
    for cell, mult in chain.items():
        for crit, coeff in project(cell).items():
            out[crit] += mult * coeff
    return sum(PHI[i] * out[c4[i]] for i in range(6))
base = phi_chain(z)
assert base == -1

def sym_perm(shift=0, flip=0, color=(0,1,2)):
    return [3*(((-i if flip else i)+shift)%8)+color[a]
            for i in range(8) for a in range(3)]

def transport(face, permutation):
    indices = [i for i in range(N) if face>>i&1]
    images = [permutation[i] for i in indices]
    inv = sum(images[i] > images[j] for i in range(len(images))
              for j in range(i+1,len(images)))
    return sum(1<<j for j in images), (-1 if inv&1 else 1)

def action_on_H4(perm):
    chain = defaultdict(int)
    for cell, coefficient in z.items():
        transformed, orient = transport(cell, perm)
        chain[transformed] += coefficient * orient
    assert phi_chain(chain) % base == 0
    return phi_chain(chain) // base

cycle = sym_perm(shift=1)
mirror = sym_perm(flip=1)
swap = sym_perm(color=(1,0,2))
color3 = sym_perm(color=(1,2,0))
assert [action_on_H4(p) for p in (cycle,mirror,swap,color3)] == [-1,-1,-1,1]

# The signed fixed-face Lefschetz trace is evaluated for all 96 actions.
# Each group action preserves the graph, including adjacency/nonadjacency.
characters = {}
for color in permutations(range(3)):
    parity = sum(color[i]>color[j] for i in range(3)
                 for j in range(i+1,3)) % 2
    color_sign = -1 if parity else 1
    std_character = (sum(color[i] == i for i in range(3)) - 1)
    for flip in (0,1):
        for shift in range(8):
            perm = sym_perm(shift,flip,color)
            assert all(perm[i] != perm[j] and
                       bool(ADJ[i] & (1<<j)) == bool(ADJ[perm[i]] & (1<<perm[j]))
                       for i in range(N) for j in range(i+1,N))
            chi4 = (-1)**(shift+flip) * color_sign
            chi5 = (-1)**shift * (color_sign+std_character)
            assert action_on_H4(perm) == chi4
            L = 0
            for face in all_faces - {0}:
                mapped, orient = transport(face,perm)
                if mapped == face:
                    L += orient * (-1)**(face.bit_count()-1)
            assert L-1 == chi4-chi5
            characters[(color,flip,shift)] = (chi4,chi5)
assert len(characters) == 96
assert [sum(v[i] for v in characters.values())//96 for i in (0,1)] == [0,0]
assert [sum(characters[(c,0,0)][i] for c in
            ((0,1,2),(1,2,0),(2,0,1)))//3 for i in (0,1)] == [1,1]
print('C8_K3_INTEGRAL_MORSE_AND_96_ACTIONS_OK')
print('nonempty_faces',len(all_faces)-1,'matched_pairs',len(mate)//2,
      'critical_cells',dict(Counter(x.bit_count()-1 for x in critical)))
print('morse_boundary',M,'rank_five_unimodular_minor',1)
print('cycle_support',len(z),'H4_generator_actions',[-1,-1,-1,1],
      'full_group_quotient_reduced_rational_betti',(0,0))
