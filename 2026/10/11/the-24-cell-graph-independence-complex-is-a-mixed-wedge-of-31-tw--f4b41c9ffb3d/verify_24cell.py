#!/usr/bin/env python3
"""Exact integral discrete-Morse verification for the 24-cell graph's independence complex.

Uses only the Python standard library. Run: python3 verify_24cell.py
The output is independently reconstructible from the graph coordinates below.
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product

# The 24 long roots of D4, in a deterministic coordinate/sign order.
vertices = []
for i, j in combinations(range(4), 2):
    for a, b in product((-1, 1), repeat=2):
        v = [0, 0, 0, 0]
        v[i], v[j] = a, b
        vertices.append(tuple(v))
assert len(vertices) == len(set(vertices)) == 24
n = len(vertices)

def dot(u, v):
    return sum(a*b for a, b in zip(u, v))

adj = [0] * n
edges = 0
for i in range(n):
    for j in range(i+1, n):
        if dot(vertices[i], vertices[j]) == 1:
            adj[i] |= 1 << j
            adj[j] |= 1 << i
            edges += 1
assert edges == 96 and all(a.bit_count() == 8 for a in adj)

# Recursive enumeration visits every independent set exactly once.
cells = set()
def enumerate_faces(face, remaining):
    if face:
        assert face not in cells
        cells.add(face)
    while remaining:
        bit = remaining & -remaining
        remaining ^= bit
        enumerate_faces(face | bit, remaining & ~adj[bit.bit_length()-1])

enumerate_faces(0, (1 << n)-1)
fvec = tuple(sum(f.bit_count() == d+1 for f in cells) for d in range(8))
assert fvec == (24, 180, 488, 474, 216, 84, 24, 3)
assert len(cells) == 1493

# A deterministic staged vertex-toggle matching on the nonempty face poset.
unmatched = set(cells)
paired_lower = {}
paired_upper = {}
for i in range(n):
    bit = 1 << i
    for f in sorted(unmatched):
        if f not in unmatched or f & bit:
            continue
        g = f | bit
        if g in unmatched:
            assert g.bit_count() == f.bit_count()+1
            unmatched.remove(f)
            unmatched.remove(g)
            paired_lower[f] = g
            paired_upper[g] = f
assert len(paired_lower) == 717
critical = Counter(f.bit_count()-1 for f in unmatched)
assert critical == {0: 1, 2: 34, 3: 24}

# Complete Hasse-digraph acyclicity certificate, not a sample of paths.
indeg = {f: 0 for f in cells}
out = defaultdict(list)
incidences = 0
for upper in cells:
    for i in range(n):
        if not upper & (1 << i):
            continue
        lower = upper ^ (1 << i)
        if not lower:
            continue
        incidences += 1
        if paired_lower.get(lower) == upper:
            u, v = lower, upper
        else:
            u, v = upper, lower
        out[u].append(v)
        indeg[v] += 1
queue = deque(f for f, d in indeg.items() if not d)
visited = 0
while queue:
    f = queue.popleft()
    visited += 1
    for g in out[f]:
        indeg[g] -= 1
        if not indeg[g]:
            queue.append(g)
assert visited == len(cells)

# Integral Morse boundary d_3, calculated by the signed gradient-path recurrence.
c2 = sorted(f for f in unmatched if f.bit_count() == 3)
c3 = sorted(f for f in unmatched if f.bit_count() == 4)
positions = {f: i for i, f in enumerate(c2)}

def boundary(face):
    inds = [i for i in range(n) if face & (1 << i)]
    return tuple((face ^ (1 << i), (-1)**j) for j, i in enumerate(inds))

@lru_cache(None)
def project(face):
    """Gradient-path coefficient of a 2-face on the critical 2-cells."""
    if face in positions:
        return {positions[face]: 1}
    if face not in paired_lower:
        return {}  # upper member of a pair with a 1-cell
    coface = paired_lower[face]
    assert coface.bit_count() == 4
    bdry = boundary(coface)
    coeff = next(sign for f, sign in bdry if f == face)
    result = {}
    for f, sign in bdry:
        if f == face:
            continue
        for j, x in project(f).items():
            result[j] = result.get(j, 0) - coeff*sign*x
    return {j: x for j, x in result.items() if x}

matrix = [[0 for _ in c3] for _ in c2]
for j, face in enumerate(c3):
    for f, sign in boundary(face):
        for i, x in project(f).items():
            matrix[i][j] += sign*x

def exact_rank(a):
    a = [[Fraction(x) for x in row] for row in a]
    r = 0
    for j in range(len(a[0])):
        k = next((k for k in range(r, len(a)) if a[k][j]), None)
        if k is None:
            continue
        a[r], a[k] = a[k], a[r]
        pivot = a[r][j]
        for k in range(r+1, len(a)):
            if a[k][j]:
                x = a[k][j]/pivot
                for c in range(j, len(a[0])):
                    a[k][c] -= x*a[r][c]
        r += 1
        if r == len(a):
            break
    return r

def det3(b):
    return (b[0][0]*(b[1][1]*b[2][2]-b[1][2]*b[2][1])
           -b[0][1]*(b[1][0]*b[2][2]-b[1][2]*b[2][0])
           +b[0][2]*(b[1][0]*b[2][1]-b[1][1]*b[2][0]))

assert len(matrix) == 34 and all(len(row) == 24 for row in matrix)
a, b, c = ([0]*24 for _ in range(3))
for j, v in {0:-1, 1:1, 2:1, 4:1, 6:1, 15:-1, 19:-1}.items(): a[j]=v
for j, v in {0:1, 15:1, 19:1}.items(): b[j]=v
for j, v in {0:-1, 9:1, 11:1}.items(): c[j]=v
expected = [a,a,[-x for x in a],b,b,[-x for x in b],
            c,c,[-x for x in c]] + [[0]*24 for _ in range(25)]
assert matrix == expected, 'integral path-count boundary disagrees with explicit sparse certificate'
assert exact_rank(matrix) == 3
minor_rows, minor_cols = (0, 3, 6), (0, 1, 9)
minor = [[matrix[i][j] for j in minor_cols] for i in minor_rows]
assert det3(minor) == -1
# Rank three plus a unit maximal minor proves Smith invariants (1,1,1).
# Hence the Morse complex is homotopy equivalent to 31 S^2 and 21 S^3.
print('24-cell 24 vertices, 96 edges, degree 8; all 1493 faces verified')
print('face vector',fvec, '; Hasse incidences',incidences)
print('matching pairs',len(paired_lower), '; critical',dict(critical))
print('directed Hasse topological sort',visited,'/',len(cells))
print('integral Morse boundary shape (34,24), rank',exact_rank(matrix),
      'unit minor',minor_rows,minor_cols,det3(minor))
print('homotopy wedge: 31 copies of S^2, 21 copies of S^3')
