"""Fast replay for emergent claim: G=C14(1,3) reg(S/I)=3 (QQ), im=2, induced-C8 witness.
Runs in seconds: graph certs, exhaustive im census, exact-QQ H~_2 on witness W, C8 check."""
import itertools
from fractions import Fraction

n = 14
nbr = [set() for _ in range(n)]
for i in range(n):
    for d in (1, 3):
        nbr[i].add((i + d) % n)
        nbr[i].add((i - d) % n)
edges = sorted((a, b) for a in range(n) for b in nbr[a] if a < b)
assert len(edges) == 28, len(edges)
assert all(len(nbr[i]) == 4 for i in range(n))
# bipartite
color = [-1]*n; color[0] = 0
from collections import deque
q = deque([0])
while q:
    u = q.popleft()
    for w in nbr[u]:
        if color[w] == -1:
            color[w] = 1 - color[u]; q.append(w)
        else:
            assert color[w] != color[u]
assert sum(c == 0 for c in color) == 7
print("graph OK: 28 edges, 4-regular, bipartite 7+7")

adj = [[False]*n for _ in range(n)]
for a, b in edges:
    adj[a][b] = adj[b][a] = True

def is_matching(combo):
    vs = [v for e in combo for v in edges[e]]
    return len(set(vs)) == 2*len(combo)

def is_induced(combo):
    vs = [v for e in combo for v in edges[e]]
    cnt = sum(1 for k in range(len(vs)) for l in range(k+1, len(vs)) if adj[vs[k]][vs[l]])
    return cnt == len(combo)

c2 = sum(1 for c in itertools.combinations(range(28), 2) if is_matching(c) and is_induced(c))
c3 = sum(1 for c in itertools.combinations(range(28), 3) if is_matching(c) and is_induced(c))
c4 = sum(1 for c in itertools.combinations(range(28), 4) if is_matching(c) and is_induced(c))
print(f"induced matchings: size2={c2} size3={c3} size4={c4}")
assert c2 == 98 and c3 == 0 and c4 == 0
print("im(G)=2 OK")

# witness W
W = int("00110011100111", 2)
verts = [i for i in range(n) if (W >> i) & 1]
assert verts == [0, 1, 2, 5, 6, 7, 10, 11]
Hedges = [(a, b) for a in verts for b in nbr[a] if b in set(verts) and a < b]
assert len(Hedges) == 8
Hdeg = {v: sum(1 for (a, b) in Hedges if v in (a, b)) for v in verts}
assert all(d == 2 for d in Hdeg.values())
# single cycle check
nbrH = {v: sorted(w for w in nbr[v] if w in set(verts)) for v in verts}
seen = set(); cur, prev = verts[0], -1
for _ in range(8):
    seen.add(cur)
    nxt = [w for w in nbrH[cur] if w != prev][0]
    prev, cur = cur, nxt
assert cur == verts[0] and len(seen) == 8
print("H=G[W] is induced C8 OK:", Hedges)

# exact QQ homology of independence complex on W
def popcount(m): return bin(m).count("1")
ind = [F for F in range(1 << n)
       if all(not ((F >> i) & 1 and any((F >> w) & 1 for w in nbr[i] if w > i)) for i in range(n))]
faces = {}
for F in ind:
    if F | W == W:
        faces.setdefault(popcount(F) - 1, []).append(tuple(sorted(i for i in range(n) if (F >> i) & 1)))

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

maxd = max(faces)
pos = {d: {f: k for k, f in enumerate(faces.get(d, []))} for d in range(-1, maxd + 1)}
ranks = {}
for d in range(0, maxd + 2):
    R = faces.get(d - 1, []); C = faces.get(d, [])
    if not R or not C:
        ranks[d] = 0; continue
    M = [[0]*len(C) for _ in range(len(R))]
    for j, f in enumerate(C):
        for k in range(len(f)):
            g = f[:k] + f[k+1:]
            M[pos[d-1][g]][j] = (-1)**k
    ranks[d] = qq_rank(M)
print("QQ boundary ranks:", ranks)
assert (ranks[0], ranks[1], ranks[2], ranks[3]) == (1, 7, 13, 2)
b2 = len(faces.get(2, [])) - ranks[3] - ranks[2]
assert b2 == 1, b2
print("QQ dim H~_2(Ind(G[W])) = 1 OK => reg(S/I;QQ) >= 3")
print("Upper reg(S/I)<=3: exhaustive Fp=32003 & Fp=10007 Hochster over all 2^14 subsets (step2_hochster.py).")
print("VERIFY_OK")
