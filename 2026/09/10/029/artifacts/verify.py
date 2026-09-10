"""Finite verification suite for lane-545 (Z^2 king-move Schreier cell).
Stdlib only. Replays all finite combinatorial facts used in the analysis.
Usage: python3 verify.py  -> prints VERIFY_OK on success.
"""
import itertools
import random
import sys

S = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if not (dx == 0 and dy == 0)]

def king_adj(u, v):
    return max(abs(u[0] - v[0]), abs(u[1] - v[1])) == 1

def grid_adj(u, v):
    return abs(u[0] - v[0]) + abs(u[1] - v[1]) == 1

# ---- 1. degree / generator count ----
assert len(S) == 8, "king generating set must have 8 moves"

# ---- 2. max clique of king graph on Z^2 is exactly 4 ----
# (a) 2x2 block is a K4
block = [(0, 0), (1, 0), (0, 1), (1, 1)]
for a, b in itertools.combinations(block, 2):
    assert king_adj(a, b), "2x2 block must be a clique"
# (b) no K5 anywhere: any clique has Chebyshev diameter <=1, x-projection is a
# set of integers pairwise within 1 -> at most 2 consecutive values; same for y.
# Hence every clique sits inside some 2x2 block (<=4 points). Verify the
# integer-line lemma and brute-force the 3x3 patch (every diameter-<=1 set
# translates into it).
def line_sets_bounded(vals):
    # integers pairwise within 1 take at most 2 distinct values
    return len(set(vals)) <= 2 and (not vals or max(vals) - min(vals) <= 1)
for trial in range(2000):
    vs = [random.randint(-3, 3) for _ in range(random.randint(1, 6))]
    if all(abs(a - b) <= 1 for a, b in itertools.combinations(vs, 2)):
        assert line_sets_bounded(vs), "integer-line clique lemma failed"
verts3 = [(x, y) for x in range(3) for y in range(3)]
maxc = 0
for r in range(1, 10):
    for s in itertools.combinations(verts3, r):
        if all(king_adj(a, b) for a, b in itertools.combinations(s, 2)):
            maxc = max(maxc, r)
assert maxc == 4, f"3x3 patch max clique must be 4, got {maxc}"
# diameter argument: any 5 points contain two at Chebyshev distance >= 2
pts = [(x, y) for x in range(4) for y in range(4)]
bad = 0
for s in itertools.combinations(pts, 5):
    if all(max(abs(a[0]-b[0]), abs(a[1]-b[1])) <= 1 for a, b in itertools.combinations(s, 2)):
        bad += 1
assert bad == 0, "a 5-clique would have to exist among diameter-<=1 sets"
print("clique facts: degree=8, omega(king Z^2)=4, no K5 (hence no K9)")

# ---- 3. ordinary chromatic number is exactly 4 (mod-2 coloring) ----
def mod2(v):
    return (v[0] % 2, v[1] % 2)
for u in verts3:
    for d in S:
        v = (u[0] + d[0], u[1] + d[1])
        if 0 <= v[0] < 3 and 0 <= v[1] < 3:
            assert mod2(u) != mod2(v), "mod-2 coloring must be proper"
print("chi(king Z^2)=4: K4 lower bound + (x mod 2, y mod 2) upper bound")

# ---- 4. Claim A fuzz test (core of king-adaptation) ----
# For ANY partition of a box into pieces, grid-interiors of distinct pieces
# are never king-adjacent. Fuzz over random guillotine rectangular partitions.
def random_rect_partition(W, H, cuts):
    rects = [(0, 0, W - 1, H - 1)]
    for _ in range(cuts):
        big = [r for r in rects if r[2] > r[0] or r[3] > r[1]]
        if not big:
            break
        r = random.choice(big)
        x0, y0, x1, y1 = r
        rects.remove(r)
        if x1 > x0 and (y1 == y0 or random.random() < 0.5):
            c = random.randint(x0, x1 - 1)
            rects += [(x0, y0, c, y1), (c + 1, y0, x1, y1)]
        elif y1 > y0:
            c = random.randint(y0, y1 - 1)
            rects += [(x0, y0, x1, c), (x0, c + 1, x1, y1)]
        else:
            rects.append(r)
    return rects

def piece_of(rects, p):
    for i, (x0, y0, x1, y1) in enumerate(rects):
        if x0 <= p[0] <= x1 and y0 <= p[1] <= y1:
            return i
    return None

random.seed(545)
for trial in range(300):
    W, H = random.randint(2, 8), random.randint(2, 8)
    rects = random_rect_partition(W, H, random.randint(1, 6))
    pts = [(x, y) for x in range(W) for y in range(H)]
    # grid boundary of the partition (relative to the box, interior edges count)
    in_box = set(pts)
    def is_bdry(p):
        for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = (p[0] + d[0], p[1] + d[1])
            if q not in in_box or piece_of(rects, q) != piece_of(rects, p):
                return True
        return False
    bdry = {p for p in pts if is_bdry(p)}
    comp = [p for p in pts if p not in bdry]
    for a in comp:
        for d in S:
            b = (a[0] + d[0], a[1] + d[1])
            if b in comp:
                assert piece_of(rects, a) == piece_of(rects, b), (
                    f"Claim A violated: king-adjacent interior points {a},{b} "
                    f"in different pieces")
print("Claim A fuzz: 300 random rectangular partitions, no cross-piece king edge")

# ---- 5. Marks free-product hypothesis fails: commuting 4-cycles present ----
# (0,0)-(1,0)-(1,1)-(0,1)-(0,0), each step a king move; uses commuting e1,e2.
cyc = [(0, 0), (1, 0), (1, 1), (0, 1)]
for i in range(4):
    assert king_adj(cyc[i], cyc[(i + 1) % 4]), "4-cycle must close"
print("commuting-generator 4-cycle present (free-product game lemma inapplicable)")

# ---- 6. finite boxes 4-colorable (no LOCAL obstruction at 8 colors) ----
for W, H in ((6, 6), (7, 5), (10, 10)):
    pts = [(x, y) for x in range(W) for y in range(H)]
    for u in pts:
        for d in S:
            v = (u[0] + d[0], u[1] + d[1])
            if 0 <= v[0] < W and 0 <= v[1] < H:
                assert mod2(u) != mod2(v)
print("finite king boxes 4-colorable by mod-2 (LOCAL 8-coloring unobstructed)")

# ---- 7. odd torus global-parity obstruction (context, not a Borel bound) ----
def torus_chi_le(m, k, budget=4000000):
    V = [(x, y) for x in range(m) for y in range(m)]
    adj = {v: set() for v in V}
    for (x, y) in V:
        for d in S:
            w = ((x + d[0]) % m, (y + d[1]) % m)
            if w != (x, y):
                adj[(x, y)].add(w)
    order = sorted(V, key=lambda v: -len(adj[v]))
    col = {order[0]: 0}
    rest = order[1:]
    nodes = [0]
    def bt(i):
        nodes[0] += 1
        if nodes[0] > budget:
            raise StopIteration
        if i == len(rest):
            return True
        v = rest[i]
        used = {col[u] for u in adj[v] if u in col}
        for c in range(k):
            if c not in used:
                col[v] = c
                if bt(i + 1):
                    return True
                del col[v]
        return False
    try:
        return bt(0), nodes[0]
    except StopIteration:
        return None, nodes[0]

ok4, n4 = torus_chi_le(5, 4)
ok5, n5 = torus_chi_le(5, 5)
assert ok4 is False, f"5x5 king torus must not be 4-colorable (got {ok4})"
assert ok5 is True, "5x5 king torus must be 5-colorable"
print(f"5x5 king torus: 4-UNSAT ({n4} nodes), 5-SAT ({n5} nodes) -> chi=5 (wrap artifact)")

print("VERIFY_OK")
