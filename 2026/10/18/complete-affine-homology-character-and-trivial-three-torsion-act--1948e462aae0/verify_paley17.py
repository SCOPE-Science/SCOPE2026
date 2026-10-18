#!/usr/bin/env python3
"""Exact finite verification for an affine homology action on an open-neighborhood complex.

Python 3 standard library only. Every face, incidence, Morse pairing, and affine
cell action is reconstructed from the quadratic-residue definition. All numerical
checks use integer or prime-field arithmetic, not floating-point topology.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

P = 17
Q = {x*x % P for x in range(1, P)}
assert Q == {1, 2, 4, 8, 9, 13, 15, 16}

facemasks = set()
for v in range(P):
    nbr = sorted((v+s) % P for s in Q)
    for k in range(1, 9):
        for face in combinations(nbr, k):
            facemasks.add(sum(1 << x for x in face))
faces = sorted(facemasks, key=lambda x: (x.bit_count(), x))
levels = [[f for f in faces if f.bit_count() == k+1] for k in range(8)]
assert [len(L) for L in levels] == [17, 136, 612, 1122, 952, 476, 136, 17]
indices = [{f: i for i, f in enumerate(L)} for L in levels]


def verts(f):
    return [j for j in range(P) if (f >> j) & 1]


def bd(f):
    return [(f ^ (1 << v), 1 if i % 2 == 0 else -1)
            for i, v in enumerate(verts(f))]


def sparse_rank(cols, prime, track=False):
    piv, pchains, cycles, free = {}, {}, {}, []
    for j, col in enumerate(cols):
        v = {r: a % prime for r, a in col.items() if a % prime}
        chain = {j: 1} if track else None
        while v and min(v) in piv:
            r = min(v)
            scalar = v[r]
            for row, coeff in piv[r].items():
                value = (v.get(row, 0) - scalar * coeff) % prime
                if value:
                    v[row] = value
                else:
                    v.pop(row, None)
            if track:
                for pos, coeff in pchains[r].items():
                    value = (chain.get(pos, 0) - scalar * coeff) % prime
                    if value:
                        chain[pos] = value
                    else:
                        chain.pop(pos, None)
        if not v:
            free.append(j)
            if track:
                cycles[j] = chain
            continue
        r = min(v)
        inv = pow(v[r], -1, prime)
        piv[r] = {key: val * inv % prime for key, val in v.items()}
        if track:
            pchains[r] = {key: val * inv % prime for key, val in chain.items()}
    return len(piv), free, cycles


def dcols(d):
    return [{indices[d-1][sub]: coeff for sub, coeff in bd(f)}
            for f in levels[d]]


def rank_rows_mod3(rows):
    piv = {}
    for row in rows:
        v = {r: val % 3 for r, val in row.items() if val % 3}
        while v and min(v) in piv:
            r = min(v)
            scalar = v[r]
            for c, val in piv[r].items():
                value = (v.get(c, 0) - scalar * val) % 3
                if value:
                    v[c] = value
                else:
                    v.pop(c, None)
        if v:
            r = min(v)
            inv = pow(v[r], -1, 3)
            piv[r] = {c: val * inv % 3 for c, val in v.items()}
    return piv


def det_int(matrix):
    a = [list(map(int, row)) for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign, prev = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            swap = next((i for i in range(k+1, n) if a[i][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                q, remainder = divmod(a[i][j]*pivot - a[i][k]*a[k][j], prev)
                assert remainder == 0
                a[i][j] = q
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]

# Exact integral discrete Morse proof of homology groups.
unmatched = set(facemasks)
low_to_up, up_to_low = {}, {}
for v in range(P):
    bit = 1 << v
    for f in faces:
        if f & bit or f not in unmatched:
            continue
        h = f | bit
        if h in unmatched:
            low_to_up[f] = h
            up_to_low[h] = f
            unmatched.remove(f)
            unmatched.remove(h)
assert len(low_to_up) == 1711 and len(unmatched) == 46

# A complete topological sorting certifies acyclicity of the gradient field.
indegree = {f: 0 for f in faces}
adj = {f: [] for f in faces}
incidences = 0
for face in faces:
    if face.bit_count() == 1:
        continue
    for sub, _ in bd(face):
        # Unmatched codimension-one arrows go high -> low; a matched pair is reversed.
        source, target = (sub, face) if low_to_up.get(sub) == face else (face, sub)
        adj[source].append(target)
        indegree[target] += 1
        incidences += 1
assert incidences == 15300
queue = deque([f for f in faces if indegree[f] == 0])
visited = 0
while queue:
    f = queue.popleft()
    visited += 1
    for target in adj[f]:
        indegree[target] -= 1
        if indegree[target] == 0:
            queue.append(target)
assert visited == len(faces), 'Discrete Morse gradient is not acyclic'

two = sorted([f for f in unmatched if f.bit_count() == 3])
three = sorted([f for f in unmatched if f.bit_count() == 4])
assert sorted(f.bit_count() for f in unmatched) == [1]+[3]*5+[4]*40
assert two == [70, 262, 8202, 16390, 32780]
critical_triangle_index = {f:i for i,f in enumerate(two)}

@lru_cache(None)
def critical_projection(t):
    if t in critical_triangle_index:
        return {critical_triangle_index[t]: 1}
    if t in up_to_low:
        return {}
    assert t in low_to_up
    h = low_to_up[t]
    assert h.bit_count() == 4
    incidence = dict(bd(h))[t]
    result = {}
    for sub, s in bd(h):
        if sub == t:
            continue
        for i, x in critical_projection(sub).items():
            result[i] = result.get(i, 0) - incidence*s*x
    return {i:x for i,x in result.items() if x}

B = [[0]*40 for _ in range(5)]
for j, f in enumerate(three):
    for sub, s in bd(f):
        for i, x in critical_projection(sub).items():
            B[i][j] += s*x
assert sum(x != 0 for row in B for x in row) == 99
assert det_int([[B[i][j] for j in [0,1,3,4,8]] for i in range(5)]) == -3
assert det_int([[B[i][j] for j in [0,1,4,8]] for i in [0,1,2,3]]) == -1
assert sparse_rank([{i:B[i][j] for i in range(5)} for j in range(40)], 3)[0] == 4
assert sparse_rank([{i:B[i][j] for i in range(5)} for j in range(40)], 2)[0] == 5
# The nonzero integral Smith factors of B are (1,1,1,1,3).
# The Morse CW model thus has H_2 = Z/3, H_3 = Z^35 and other reduced H_i=0.

# Independent simplicial mod-3 cycle/cocycle calculation of the torsion action.
r2, free2, cycles = sparse_rank(dcols(2), 3, track=True)
assert r2 == 120 and len(free2) == 492
coord = {j:i for i,j in enumerate(free2)}
constraints = [ {coord[j]:val for j,val in col.items() if j in coord}
                for col in dcols(3) ]
piv = rank_rows_mod3(constraints)
assert len(piv) == 491
unconstrained = [j for j in range(len(free2)) if j not in piv]
assert len(unconstrained) == 1
L = {unconstrained[0]:1}
for j in sorted(piv, reverse=True):
    L[j] = (-sum(val*L.get(i,0) for i,val in piv[j].items() if i != j)) % 3
assert all(sum(val*L.get(j,0) for j,val in row.items()) % 3 == 0 for row in constraints)
chosen = next(j for j in free2 if L[coord[j]] != 0)
z = cycles[chosen]
assert all(sum(coeff*dcols(2)[j].get(i,0) for j,coeff in z.items()) % 3 == 0
           for i in range(len(levels[1])))


def mapped_sign(vs):
    return -1 if sum(vs[i] > vs[j] for i in range(len(vs))
                     for j in range(i+1,len(vs))) % 2 else 1


def mapmask(f, a, b):
    values = [(a*v+b) % P for v in verts(f)]
    return sum(1<<u for u in values), mapped_sign(values)


def torsion_scalar(a,b):
    value = 0
    for j, coefficient in z.items():
        m,s = mapmask(levels[2][j], a, b)
        out = indices[2][m]
        if out in coord:
            value += coefficient*s*L[coord[out]]
    return value * pow(L[coord[chosen]], -1, 3) % 3

# Rational character via signed cellular Lefschetz traces.
def char(a,b):
    ell = -1  # reduced trace: remove the fixed augmentation of C_0
    for d, layer in enumerate(levels):
        for f in layer:
            out, sign = mapmask(f,a,b)
            if out == f:
                ell += (-1)**d * sign
    return -ell  # rational reduced homology is concentrated in degree 3

# Standard 16-dimensional cyclotomic rational G-module Q(zeta_17).
def cyclotomic_character(a,b):
    if a != 1:
        return 0
    return 16 if b == 0 else -1

# Augmentation of the regular C4-module, inflated from G/T = C8 to C4.
def four_augmentation_character(a):
    k = next(k for k in range(8) if pow(2,k,17) == a)
    return 3 if k % 4 == 0 else -1

multipliers = [pow(2,k,17) for k in range(8)]
assert set(multipliers) == Q
counts = Counter()
for a in multipliers:
    for b in range(P):
        value = char(a,b)
        assert value == four_augmentation_character(a) + 2*cyclotomic_character(a,b)
        assert torsion_scalar(a,b) == 1
        counts[(a,value)] += 1
assert sum(counts.values()) == 136
assert char(1,0)==35
assert all(char(1,b)==1 for b in range(1,17))
assert all(char(16,b)==3 for b in range(17))
assert all(char(a,b)==-1 for a in multipliers if a not in (1,16) for b in range(17))
assert sum(char(a,b) for a in multipliers for b in range(17)) == 0
print('PASS: 3468 faces; 1711 acyclic Morse pairs; integral Smith (1,1,1,1,3).')
print('PASS: H2(Z)=Z/3, H3(Z)=Z^35; mod-3 H2 action trivial for all 136 elements.')
print('PASS: all 136 rational traces = 2 cyclotomic characters + C4 augmentation.')
print('Character by multiplier 2^k at any translation b (apart from k=0,b=0):')
print([(a, char(a,0)) for a in multipliers])
print('All exact finite checks passed.')
