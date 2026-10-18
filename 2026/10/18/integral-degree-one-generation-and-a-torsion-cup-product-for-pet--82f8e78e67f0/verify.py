"""Exact integral cup-product verification for two unordered particles on the Petersen graph.
Run: python3 verify.py. Standard library only.
"""
from itertools import combinations, permutations

VERTICES = list(combinations(range(5), 2))
EDGES = [(u, v) for u, v in combinations(range(10), 2)
         if set(VERTICES[u]).isdisjoint(VERTICES[v])]
ZERO = list(combinations(range(10), 2))
ONE = [(e, v) for e in range(15) for v in range(10) if v not in EDGES[e]]
TWO = [(e, f) for e, f in combinations(range(15), 2)
       if set(EDGES[e]).isdisjoint(EDGES[f])]
assert (len(ZERO), len(ONE), len(TWO)) == (45, 120, 75)
# The configuration one-skeleton is connected (hence boundary-one rank is 44).
from collections import deque
adj = {i: set() for i in range(45)}
for e, v in ONE:
    a, b = EDGES[e]
    u, w = ZERO.index(tuple(sorted((a, v)))), ZERO.index(tuple(sorted((b, v))))
    adj[u].add(w); adj[w].add(u)
seen = {0}; q = deque([0])
while q:
    for w in adj[q.popleft()]:
        if w not in seen: seen.add(w); q.append(w)
assert len(seen) == 45

zeroindex = {v: i for i, v in enumerate(ZERO)}
oneindex = {v: i for i, v in enumerate(ONE)}
twoindex = {v: i for i, v in enumerate(TWO)}
D1 = [[0] * 120 for _ in range(45)]
D2 = [[0] * 75 for _ in range(120)]
for c, (e, v) in enumerate(ONE):
    a, b = EDGES[e]
    D1[zeroindex[tuple(sorted((a, v)))]][c] -= 1
    D1[zeroindex[tuple(sorted((b, v)))]][c] += 1
for c, (i, j) in enumerate(TWO):
    a, b = EDGES[i]; u, v = EDGES[j]
    for cell, sg in [((j, b), 1), ((j, a), -1), ((i, v), -1), ((i, u), 1)]:
        D2[oneindex[cell]][c] += sg
for c in range(75):
    z = [sum(D1[r][k] * D2[k][c] for k in range(120)) for r in range(45)]
    assert not any(z)
DD = [list(row) for row in zip(*D2)]

# The following six edges complement the lexicographically first spanning tree.
TREE = [0, 1, 2, 3, 4, 5, 6, 7, 9]
CHORDS = [8, 10, 11, 12, 13, 14]
assert len(TREE) == 9 and len(CHORDS) == 6
parent = list(range(10))
def root(i):
    while i != parent[i]: i = parent[i]
    return i
for e in TREE:
    u, v = EDGES[e]; ru, rv = root(u), root(v)
    assert ru != rv
    parent[ru] = rv
assert len({root(i) for i in range(10)}) == 1
# Every fundamental graph cycle admits an unused parking vertex. Its
# one-particle motion proves surjectivity of the total-edge-motion H1 map.
treeadj = {i: [] for i in range(10)}
for ei in TREE:
    u, v = EDGES[ei]; treeadj[u].append(v); treeadj[v].append(u)
spares = []
for ei in CHORDS:
    u, v = EDGES[ei]; q = deque([(u, [u])]); path = None
    while q:
        w, pth = q.popleft()
        if w == v: path = pth; break
        for z in treeadj[w]:
            if z not in pth: q.append((z, pth + [z]))
    assert path is not None and len(path) < 10
    spares.append(next(z for z in range(10) if z not in path))
assert spares == [3, 0, 5, 0, 2, 2]

PAIRS = list(combinations(CHORDS, 2))
CUP = [[int(pair == face) for pair in PAIRS] for face in TWO]
# Every chord-edge sum is a closed integral 1-cochain.
for e in CHORDS:
    for c in range(75):
        assert sum(D2[k][c] for k, (f, _) in enumerate(ONE) if f == e) == 0
AUG = [DD[i] + CUP[i] for i in range(75)]

def modular_rank(A, p):
    if not A: return 0
    a = [[z % p for z in row] for row in A]
    m, n = len(a), len(a[0]); r = 0
    for col in range(n):
        pivot = next((k for k in range(r, m) if a[k][col]), None)
        if pivot is None: continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][col], -1, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for k in range(r + 1, m):
            t = a[k][col]
            if t: a[k] = [(x - t * y) % p for x, y in zip(a[k], a[r])]
        r += 1
        if r == m: break
    return r

def determinant(M):
    # Fraction-free Bareiss algorithm, with row swaps, exact divisions.
    a = [row[:] for row in M]; n = len(a)
    assert all(len(row) == n for row in a)
    sign = 1; prev = 1
    for k in range(n - 1):
        if not a[k][k]:
            swap = next((i for i in range(k + 1, n) if a[i][k]), None)
            if swap is None: return 0
            a[k], a[swap] = a[swap], a[k]; sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            xik = a[i][k]
            for j in range(k + 1, n):
                numerator = pivot * a[i][j] - xik * a[k][j]
                assert numerator % prev == 0
                a[i][j] = numerator // prev
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]

# Full-rank 70x70 minor of the second coboundary, determinant -2.
D_ROWS = list(range(70))
D_COLS = [0,1,2,3,4,5,6,8,9,10,11,12,13,14,16,17,18,19,20,21,22,24,25,26,27,28,29,30,32,33,34,35,36,37,38,41,42,43,44,45,46,48,49,50,51,52,53,54,56,57,58,59,60,61,62,66,67,68,69,70,75,76,77,83,84,91,92,100,101,109]
assert len(D_ROWS) == len(D_COLS) == 70
minor2 = determinant([[DD[r][c] for c in D_COLS] for r in D_ROWS])
assert abs(minor2) == 2, minor2
assert modular_rank(DD, 2) == 69
assert modular_rank(DD, 101) == 70

# All pentagonal simple cycles in Petersen, with canonical orientation.
cycles = {}
for path in permutations(range(10), 5):
    if path[0] != min(path) or path[1] > path[-1]: continue
    if all(tuple(sorted((path[i], path[(i + 1) % 5]))) in EDGES for i in range(5)):
        coeff = {}
        for i in range(5):
            x, y = path[i], path[(i + 1) % 5]
            e = EDGES.index(tuple(sorted((x, y))))
            coeff[e] = 1 if x < y else -1
        cycles[path] = coeff
assert len(cycles) == 12
TORI = []
for a, b in combinations(cycles, 2):
    if set(a).isdisjoint(b):
        z = [0] * 75
        for ei, ci in cycles[a].items():
            for ej, cj in cycles[b].items():
                index = twoindex[(min(ei, ej), max(ei, ej))]
                z[index] += ci * cj * (1 if ei < ej else -1)
        assert all(sum(D2[i][c] * z[c] for c in range(75)) == 0 for i in range(120))
        TORI.append(z)
assert len(TORI) == 6
assert modular_rank([list(x) for x in zip(*TORI)], 101) == 5
# Six torus classes span rank five, so Q-rank(DD)=70 exactly.
assert modular_rank(DD, 101) == 70

# A 75x75 unimodular minor of [coboundaries | cup cocycles].
UNIMOD_COLS = [120,121,122,124,126,128,129,130,132,133,134,0,1,2,3,4,5,6,8,9,10,11,12,13,14,16,17,18,19,20,21,22,24,25,26,27,28,29,30,32,33,34,35,36,37,38,41,42,43,44,45,46,48,49,50,51,52,53,54,56,57,58,59,60,61,62,66,68,69,70,75,76,83,84,92]
assert len(UNIMOD_COLS) == 75 and len(set(UNIMOD_COLS)) == 75
unimod = determinant([[AUG[r][c] for c in UNIMOD_COLS] for r in range(75)])
assert abs(unimod) == 1, unimod

# The explicit torsion cup class -a_8 a_10 + a_8 a_14 + a_10 a_13.
TAU = [-(row[0]) + row[4] + row[8] for row in CUP]
assert all(sum(z[c] * TAU[c] for c in range(75)) == 0 for z in TORI)
# Tau pairs trivially with H2 (rank 5), yet is not a coboundary mod 2.
assert modular_rank([DD[i] + [TAU[i]] for i in range(75)], 2) == 70
# Since DD's Smith group has exactly one Z/2 and all other invariants 1,
# tau is the nonzero 2-torsion H^2 class.
print('VERIFY_OK', 'cells', (45,120,75), 'minor_D', minor2,
      'mod2_coboundary_rank',69, 'torus_rank',5,
      'unimodular_cup_minor',unimod, 'tau_order',2)
