"""Step 3 (target-directed): QQ recheck of Hochster witness + analyze H=G[W8]."""
import itertools
from fractions import Fraction

n = 14
nbr = [set() for _ in range(n)]
for i in range(n):
    for d in (1, 3):
        nbr[i].add((i + d) % n)
        nbr[i].add((i - d) % n)

def popcount(m): return bin(m).count("1")

# witness W from step2: 0b00110011100111, bit i = vertex i
W = int("00110011100111", 2)
print("W =", W, "binary:", format(W, "014b"))
verts = [i for i in range(n) if (W >> i) & 1]
print("verts:", verts, "|W| =", len(verts))

# Exact QQ rank via Fraction Gauss elimination
def qq_rank(rows):
    if not rows or not rows[0]:
        return 0
    A = [[Fraction(x) for x in r] for r in rows]
    r, c = len(A), len(A[0])
    rk = 0
    for j in range(c):
        piv = next((i for i in range(rk, r) if A[i][j] != 0), None)
        if piv is None:
            continue
        A[rk], A[piv] = A[piv], A[rk]
        for i in range(r):
            if i != rk and A[i][j] != 0:
                f = A[i][j] / A[rk][j]
                for k in range(j, c):
                    A[i][k] -= f * A[rk][k]
        rk += 1
    return rk

# faces of independence complex restricted to W
ind = [F for F in range(1 << n) if all(not ((F >> i) & 1 and any((F >> w) & 1 for w in nbr[i] if w > i)) for i in range(n))]
faces = {}
for F in ind:
    if F | W == W:
        faces.setdefault(popcount(F) - 1, []).append(tuple(sorted(i for i in range(n) if (F >> i) & 1)))
maxd = max(faces)
print("dims present:", sorted(faces))
pos = {d: {f: k for k, f in enumerate(faces.get(d, []))} for d in range(-1, maxd + 1)}
ranks = {}
for d in range(0, maxd + 2):
    rows_L = faces.get(d - 1, [])
    cols_L = faces.get(d, [])
    if not rows_L or not cols_L:
        ranks[d] = 0; continue
    M = [[0]*len(cols_L) for _ in range(len(rows_L))]
    for j, f in enumerate(cols_L):
        for k in range(len(f)):
            g = f[:k] + f[k+1:]
            M[pos[d-1][g]][j] = (-1)**k
    ranks[d] = qq_rank(M)
    print(f"rank d_{d} (C_{d}->C_{d-1}): {ranks[d]}  (C_{d} dim={len(cols_L)})")
for d in range(-1, maxd + 1):
    nd = len(faces.get(d, []))
    b = nd - ranks.get(d + 1, 0) - ranks.get(d, 0) if d >= 0 else nd - ranks.get(0, 0)
    print(f"QQ dim H~_{d} = {b}")
print("=> reg(S/I) over QQ >=", None)

# Analyze H = G[W]
Hedges = [(a, b) for a in verts for b in nbr[a] if b in set(verts) and a < b]
print("\nH edges:", Hedges, "count:", len(Hedges))
Hdeg = {v: sum(1 for (a, b) in Hedges if v in (a, b)) for v in verts}
print("H degrees:", Hdeg)
# girth / cycles of H
nbrH = {v: [w for w in nbr[v] if w in set(verts)] for v in verts}
print("H adjacency:", {v: sorted(nbrH[v]) for v in verts})
# check: is H a single cycle C8?
if all(len(nbrH[v]) == 2 for v in verts):
    print("H is 2-regular: disjoint union of cycles")
    seen = set(); cyc = []
    for v in verts:
        if v not in seen:
            cur = v; prev = -1; L = []
            while cur not in seen:
                seen.add(cur); L.append(cur)
                nxt = [w for w in nbrH[cur] if w != prev][0] if len([w for w in nbrH[cur] if w != prev]) else None
                prev, cur = cur, nxt
                if cur is None: break
            cyc.append(L)
    print("cycle decomposition:", cyc)
# induced matching of H
import math
adjH = {v: set(nbrH[v]) for v in verts}
def eok(e, f):
    return not any(w in adjH[u] for u in e for w in f)
best = 0; wit = None
E = Hedges
for k in range(len(E), 0, -1):
    found = None
    for combo in itertools.combinations(range(len(E)), k):
        ee = [E[i] for i in combo]
        vs = [v for e in ee for v in e]
        if len(set(vs)) != 2*k: continue
        if all(eok(ee[a], ee[b]) for a in range(k) for b in range(a+1, k)):
            found = ee; break
    if found:
        best = k; wit = found; break
print("im(H) =", best, wit)
