#!/usr/bin/env python3
"""Reproduce the integral Morse-chain spectrum of Frucht higher-independence complexes.
Python 3 standard library only. This script is mathematical reproducibility material.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N = 12
EDGES = ((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
         (4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))
ADJ = [0] * N
for u, v in EDGES:
    assert 0 <= u < v < N
    ADJ[u] |= 1 << v
    ADJ[v] |= 1 << u
assert all(a.bit_count() == 3 for a in ADJ)

def max_component(mask):
    unvisited, biggest = mask, 0
    while unvisited:
        comp = unvisited & -unvisited
        while True:
            new = comp
            for v in range(N):
                if comp & (1 << v):
                    new |= ADJ[v] & mask
            if new == comp:
                break
            comp = new
        biggest = max(biggest, comp.bit_count())
        unvisited &= ~comp
    return biggest

SIZES = [max_component(mask) for mask in range(1 << N)]
assert SIZES[0] == 0 and SIZES[-1] == N
assert all(SIZES[a] <= SIZES[a | b] for a in range(1 << N) for b in (1,2,4) if (a|b)<1 << N)

def boundary(mask):
    return [(mask ^ (1 << v), -1 if j % 2 else 1)
            for j, v in enumerate(v for v in range(N) if mask & (1 << v))]

def matching(faces):
    remaining = set(faces)
    pairs = []
    for v in range(N):
        bit = 1 << v
        for low in sorted(remaining):
            if low & bit:
                continue
            high = low | bit
            if high in remaining:
                remaining.remove(low)
                remaining.remove(high)
                pairs.append((low, high))
    assert len(remaining) + 2 * len(pairs) == len(faces)
    return remaining, pairs

def acyclic(faces, pairs):
    ups = dict(pairs)
    assert len(ups) == len(pairs)
    out = {x: [] for x in faces}
    indeg = {x: 0 for x in faces}
    incidences = 0
    for low in faces:
        for v in range(N):
            high = low | (1 << v)
            if high == low or high not in faces:
                continue
            u, w = (low, high) if ups.get(low) == high else (high, low)
            out[u].append(w)
            indeg[w] += 1
            incidences += 1
    q = deque(x for x in faces if indeg[x] == 0)
    done = 0
    while q:
        x = q.popleft()
        done += 1
        for y in out[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)
    assert done == len(faces), ('Morse cycle', len(faces) - done)
    return incidences

def unit_rank(A):
    """Unimodular integer elimination: every nonzero Smith factor must be a unit."""
    if not A:
        return 0
    a = [list(row) for row in A]
    nr, nc = len(a), len(a[0])
    assert all(len(row) == nc for row in a)
    k = 0
    while k < min(nr, nc):
        p = next(((i,j) for i in range(k,nr) for j in range(k,nc)
                  if abs(a[i][j]) == 1), None)
        if p is None:
            assert not any(a[i][j] for i in range(k,nr) for j in range(k,nc)), 'nonunit invariant factor'
            break
        i, j = p
        a[k], a[i] = a[i], a[k]
        for row in a:
            row[k], row[j] = row[j], row[k]
        pivot = a[k][k]
        assert abs(pivot) == 1
        for i in range(k+1, nr):
            f = a[i][k] // pivot
            if f:
                a[i] = [a[i][j] - f*a[k][j] for j in range(nc)]
        for j in range(k+1, nc):
            f = a[k][j] // pivot
            if f:
                for i in range(nr):
                    a[i][j] -= f*a[i][k]
        assert all(a[i][k] == 0 for i in range(k+1,nr))
        assert all(a[k][j] == 0 for j in range(k+1,nc))
        k += 1
    return k

EXPECTED_CRITICAL = {
 1: {2:4, 3:1}, 2:{3:2,4:1}, 3:{4:2,5:19},
 4:{4:1,5:6,6:4}, 5:{4:1,5:3,6:3,7:1}, 6:{5:36,6:3},
 7:{6:128}, 8:{7:135}, 9:{8:55}, 10:{9:11}, 11:{10:1}, 12:{}
}
EXPECTED_RANKS = {
 1:{3:1}, 2:{4:1}, 3:{5:2}, 4:{5:1,6:4},
 5:{5:0,6:2,7:1}, 6:{6:3}, 7:{},8:{},9:{},10:{},11:{},12:{}
}
EXPECTED_HOMOLOGY = {
 1:{2:3}, 2:{3:1}, 3:{5:17}, 4:{5:1},
 5:{4:1,5:1}, 6:{5:33}, 7:{6:128}, 8:{7:135},
 9:{8:55}, 10:{9:11}, 11:{10:1}, 12:{}
}
EXPECTED_COUNTS = {1:169, 2:825, 3:1593, 4:2281, 5:2798, 6:3211,
                   7:3540, 8:3827, 9:4017, 10:4083, 11:4095, 12:4096}

for r in range(1,13):
    faces = {x for x in range(1<<N) if SIZES[x] <= r}
    assert len(faces) == EXPECTED_COUNTS[r]
    assert all((y in faces) for x in faces for y,_ in boundary(x))
    critical, pairs = matching(faces)
    incidences = acyclic(faces, pairs)
    ups = dict(pairs)
    downs = {hi:lo for lo,hi in pairs}
    assert len(downs) == len(pairs)
    graded = defaultdict(list)
    for x in sorted(critical):
        assert x != 0  # empty simplex matched with a vertex
        graded[x.bit_count()-1].append(x)
    critical_dims = {d:len(v) for d,v in graded.items()}
    assert critical_dims == EXPECTED_CRITICAL[r], (r, critical_dims)

    @lru_cache(None)
    def reduce_face(face):
        """Integral Morse projection at the degree of `face`."""
        if face in critical:
            return {face:1}
        if face in downs:
            return {}
        high = ups[face]
        coef = dict(boundary(high))[face]
        assert abs(coef) == 1
        out = Counter()
        for lower, sign in boundary(high):
            if lower == face:
                continue
            for target, weight in reduce_face(lower).items():
                out[target] -= coef * sign * weight
        return {x:c for x,c in out.items() if c}

    matrices = {}
    ranks = {}
    for d in sorted(graded):
        if d <= 0 or not graded.get(d-1):
            continue
        lower = graded[d-1]
        index = {x:i for i,x in enumerate(lower)}
        mat = [[0] * len(graded[d]) for _ in lower]
        for j,face in enumerate(graded[d]):
            for f,sign in boundary(face):
                for target, coefficient in reduce_face(f).items():
                    if target in index:
                        mat[index[target]][j] += sign*coefficient
        matrices[d] = mat
        ranks[d] = unit_rank(mat)
    assert ranks == EXPECTED_RANKS[r],(r,ranks)
    for d, A in matrices.items():
        B = matrices.get(d-1)
        if B is None:
            continue
        assert len(B[0]) == len(A)
        assert all(sum(B[i][t]*A[t][j] for t in range(len(A))) == 0
                   for i in range(len(B)) for j in range(len(A[0])))
    betti = {d:c-ranks.get(d,0)-ranks.get(d+1,0)
             for d,c in critical_dims.items()}
    betti = {d:b for d,b in betti.items() if b}
    assert betti == EXPECTED_HOMOLOGY[r], (r,betti)
    print(f'r={r:2d} faces={len(faces):4d} pairs={len(pairs):4d} '
          f'incidences={incidences:5d} critical={dict(sorted(critical_dims.items()))} '
          f'ranks={ranks} reduced_integral_betti={betti}')
    if r == 2:
        assert sorted(critical) == [740,834,1100]
        assert sorted(matrices[4][i][0] for i in range(2)) == [0,1]
print('VERIFY_OK')

# Independently obtain persistence by direct integral boundary-column reduction
# in filtration order. Every pivot is a unit, making these barcodes valid
# over every coefficient field. The augmented empty face is excluded in output.
EXPECTED_BARS = {
 (2,1,2):3, (3,2,3):1, (4,5,6):1,
 (5,3,4):16, (5,3,7):1, (5,6,7):32,
 (6,7,8):128, (7,8,9):135, (8,9,10):55,
 (9,10,11):11, (10,11,12):1,
}
order = sorted(range(1 << N),key=lambda x:(SIZES[x],x.bit_count(),x))
assert len(order)==1<<N and order[0]==0
at = {x:i for i,x in enumerate(order)}
columns = {}
pairings = []
for j,face in enumerate(order):
    C = {at[f]:s for f,s in boundary(face)}
    while C:
        p = max(C)
        coef = C[p]
        if p not in columns:
            assert abs(coef) == 1, ('non-unit integral persistence pivot', j,p,coef)
            columns[p] = C
            pairings.append((p,j))
            break
        B = columns[p]
        assert abs(B[p]) == 1
        factor = coef * B[p]
        for i,b in B.items():
            C[i] = C.get(i,0) - factor*b
            if C[i] == 0:
                del C[i]
all_bars = Counter((order[i].bit_count()-1,SIZES[order[i]],SIZES[order[j]])
                   for i,j in pairings if SIZES[order[i]] < SIZES[order[j]])
assert dict((k,v) for k,v in all_bars.items() if k[0]>=0) == EXPECTED_BARS
assert len(pairings)==2048
print('integral_unit_pivots=',len(pairings), 'all_field_finite_bars=',len(EXPECTED_BARS))

# Separate mod-two reduction uses a bitset representation of boundary columns.
mod2 = {}
mod2_pairs = []
for j,face in enumerate(order):
    c = 0
    for f,_ in boundary(face):
        c ^= 1 << at[f]
    while c:
        p = c.bit_length()-1
        if p in mod2:
            c ^= mod2[p]
        else:
            mod2[p] = c
            mod2_pairs.append((p,j))
            break
assert pairings == mod2_pairs
print('MOD2_PERSISTENCE_OK')
print('COMPLETE_VERIFY_OK')
