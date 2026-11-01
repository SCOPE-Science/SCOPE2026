#!/usr/bin/env python3
"""Exact integral homotopy certificate for the Clebsch closed-neighborhood complex.

Python 3 standard library.  Reconstructs every face and each elementary
simplicial collapse, then tracks elementary CW generator/relator cancellations.
"""
from itertools import combinations
from collections import Counter

V = [v for v in range(32) if v.bit_count() % 2 == 0]
assert len(V) == 16
N = [tuple(j for j, w in enumerate(V)
           if w == v or (v ^ w).bit_count() == 4) for v in V]
assert all(len(b) == 6 for b in N)
assert sum(1 for i in range(16) for j in range(i + 1, 16)
           if (V[i] ^ V[j]).bit_count() == 4) == 40

F = {sum(1 << j for j in face)
     for b in N for k in range(1, len(b) + 1)
     for face in combinations(b, k)}
assert dict(sorted(Counter(f.bit_count() - 1 for f in F).items())) == {
    0: 16, 1: 120, 2: 320, 3: 240, 4: 96, 5: 16}
assert all((a & (a - 1)) in F for a in F if a.bit_count() > 1)
print('INITIAL_FACES_OK', len(F), flush=True)

# Deterministic elementary collapses. Every candidate face is tested in the
# CURRENT face set, not in a stale list of the original maximal simplices.
steps = 0
while True:
    free = []
    for lo in F:
        neighbors = []
        for i in range(16):
            hi = lo | (1 << i)
            if hi != lo and hi in F:
                neighbors.append(hi)
                if len(neighbors) > 1:
                    break
        if len(neighbors) == 1:
            free.append((-lo.bit_count(), lo, neighbors[0]))
    if not free:
        break
    _, lo, hi = min(free)
    assert hi.bit_count() == lo.bit_count() + 1
    assert lo in F and hi in F
    assert sum((lo | (1 << i)) in F and not (lo >> i & 1)
               for i in range(16)) == 1
    F.remove(lo)
    F.remove(hi)
    steps += 1
assert steps == 256
assert dict(sorted(Counter(f.bit_count() - 1 for f in F).items())) == {
    0: 16, 1: 120, 2: 160}
assert all((f ^ (f & -f)) in F for f in F if f.bit_count() > 1)
print('ELEMENTARY_COLLAPSE_OK', steps, len(F), flush=True)

# Contract the 15-edge tree of edges {0,j}, 1<=j<=15. Remaining oriented
# edges of the complete graph give 105 free group generators.
EDGE = {(i, j): k + 1 for k, (i, j) in enumerate(
    (i, j) for i in range(1, 16) for j in range(i + 1, 16))}
assert len(EDGE) == 105

def edge(i, j):
    if i == 0 or j == 0: return 0
    return EDGE[(i, j)] if i < j else -EDGE[(j, i)]

def inverse(word): return [-z for z in word[::-1]]

def freely_reduce(word):
    stack = []
    for z in word:
        if z == 0: continue
        if stack and stack[-1] == -z:
            stack.pop()
        else:
            stack.append(z)
    return stack

def cyclically_reduce(word):
    word = freely_reduce(word)
    while len(word) > 1 and word[0] == -word[-1]:
        word = word[1:-1]
    return word

triangles = sorted(f for f in F if f.bit_count() == 3)
relators = []
for f in triangles:
    a, b, c = [i for i in range(16) if f >> i & 1]
    w = cyclically_reduce([edge(a,b), edge(b,c), edge(c,a)])
    assert w
    relators.append(w)
assert len(relators) == 160
remaining = set(EDGE.values())
removed = []
while True:
    best = None
    freq = Counter(abs(x) for r in relators for x in set(r))
    for i, word in enumerate(relators):
        c = Counter(map(abs, word))
        for g, count in c.items():
            if g in remaining and count == 1:
                key = ((len(word) - 1)*freq[g], len(word), freq[g], g, i)
                if best is None or key < best[0]: best = (key, g, i)
    if best is None: break
    _, g, i = best
    w = relators[i]
    pos = next(t for t, z in enumerate(w) if abs(z) == g)
    rot = w[pos:] + w[:pos]
    assert sum(abs(z) == g for z in rot) == 1
    sign, tail = rot[0], rot[1:]
    substitute = inverse(tail) if sign == g else tail
    # Eliminate exactly one 1-cell and its degree-one 2-cell; substitute the
    # resulting edge path into the other attaching maps, then freely reduce.
    new = []
    for j, rel in enumerate(relators):
        if j == i: continue  # cancelled 2-cell must NOT survive
        expanded = []
        for z in rel:
            if z == g: expanded.extend(substitute)
            elif z == -g: expanded.extend(inverse(substitute))
            else: expanded.append(z)
        new.append(cyclically_reduce(expanded))
    relators = new
    remaining.remove(g)
    removed.append(g)
assert len(removed) == 104 and len(remaining) == 1
assert len(relators) == 56
assert Counter(map(len, relators)) == {0: 42, 2: 14}
g = next(iter(remaining))
assert all(r == [g,g] or r == [-g,-g] or r == [] for r in relators)
assert 16-120+160 == 1 - 1 + 56 == 56
# Independent field-chain check on the 2D simplicial spine (not on its
# simplified presentation): each signed triangle boundary uses three edges.
EDGES = sorted(f for f in F if f.bit_count() == 2)
EDGE_ROWS = {f: i for i, f in enumerate(EDGES)}
def boundary_rank(p):
    pivot = {}
    for f in triangles:
        a, b, c = [i for i in range(16) if f >> i & 1]
        col = {EDGE_ROWS[(1 << a) | (1 << b)]: 1 % p,
               EDGE_ROWS[(1 << b) | (1 << c)]: 1 % p,
               EDGE_ROWS[(1 << a) | (1 << c)]: -1 % p}
        col = {k: v for k, v in col.items() if v}
        while col:
            row = min(col)
            if row not in pivot:
                inv = pow(col[row], -1, p)
                pivot[row] = {k: (v * inv) % p for k, v in col.items()}
                break
            mult = col[row]
            for k, v in pivot[row].items():
                nextv = (col.get(k, 0) - mult * v) % p
                if nextv: col[k] = nextv
                elif k in col: del col[k]
    return len(pivot)
assert (boundary_rank(2), boundary_rank(3), boundary_rank(5)) == (104,105,105)
print('FIELD_HOMOLOGY_OK p2: (H1=1,H2=56); p3,p5: (H1=0,H2=55)', flush=True)
print('CW_CANCEL_OK', len(removed), 'one generator,',
      len(relators), 'two-cells,', Counter(map(len, relators)), flush=True)
print('HOMOTOPY_OK RP2 wedge 55 S2; pi1=Z/2, H1=Z/2, H2=Z^55', flush=True)
print('ALL_VERIFY_OK', flush=True)
