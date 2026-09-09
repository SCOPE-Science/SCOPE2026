"""Independent verifier for the [22,10,8] Golay-shortening witness package (stdlib only).
Replays: code tally (1024), dual tally (4096), term-by-term MacWilliams/Krawtchouk,
syndrome coset-leader BFS (4096 syndromes). Prints VERIFY_OK on full agreement."""
from math import comb
from collections import Counter, deque

# Committed 10x22 generator (systematic RREF, pivots cols 0..9), rows as bitmasks (bit c = col c)
G = [2422785, 1805314, 3610628, 3951624, 2810896, 504864, 1009728, 2019456, 4038912, 2702848]
N, K = 22, 10
WC_EXPECT = {0: 1, 8: 330, 12: 616, 16: 77}
WD_EXPECT = {0: 1, 6: 77, 7: 352, 8: 330, 10: 616, 11: 1344, 12: 616, 14: 330, 15: 352, 16: 77, 22: 1}

def wt(x): return bin(x).count("1")

# (1) code tally over all 2^10 codewords
S = {0}
for r in G:
    S = S | {x ^ r for x in S}
assert len(S) == 1024, len(S)
wc = Counter(wt(w) for w in S)
assert dict(wc) == WC_EXPECT, dict(wc)
assert min(wt(w) for w in S if w) == 8
print("(1) code tally OK: sum=1024, min-weight 8, W_C =", sorted(wc.items()))

# (2) parity check from RREF of G; dual tally over 2^12 words
M = list(G)
piv = []
row = 0
for c in range(N):
    p = next((i for i in range(row, K) if (M[i] >> c) & 1), None)
    if p is None: continue
    M[row], M[p] = M[p], M[row]
    for i in range(K):
        if i != row and ((M[i] >> c) & 1): M[i] ^= M[row]
    piv.append(c); row += 1
assert piv == list(range(10)), piv
free = [c for c in range(N) if c not in piv]
H = []
for f in free:
    v = (1 << f)
    for ri, pc in enumerate(piv):
        if (M[ri] >> f) & 1: v |= (1 << pc)
    H.append(v)
assert len(H) == 12
# orthogonality G*H^T = 0
for g in G:
    for h in H:
        assert wt(g & h) % 2 == 0
D = {0}
for h in H:
    D = D | {x ^ h for x in D}
assert len(D) == 4096, len(D)
wd = Counter(wt(w) for w in D)
assert dict(wd) == WD_EXPECT, dict(wd)
print("(2) dual tally OK: sum=4096, W_dual =", sorted(wd.items()))

# (3) term-by-term binary MacWilliams/Krawtchouk over integers
A = [0] * (N + 1)
for w, c in wc.items(): A[w] = c
B = [0] * (N + 1)
for w, c in wd.items(): B[w] = c
def Kraw(j, i):
    s = 0
    for t in range(max(0, j - (N - i)), min(j, i) + 1):
        s += (1 if t % 2 == 0 else -1) * comb(i, t) * comb(N - i, j - t)
    return s
for j in range(N + 1):
    s = sum(A[i] * Kraw(j, i) for i in range(N + 1))
    assert s % 1024 == 0 and s // 1024 == B[j], (j, s, B[j])
print("(3) MacWilliams term-by-term OK (23/23 identities, exact integers)")

# (4) syndrome coset-leader BFS: columns of H as 12-bit syndromes
cols = []
for c in range(N):
    s = 0
    for j, h in enumerate(H):
        if (h >> c) & 1: s |= (1 << j)
    cols.append(s)
dist = [-1] * (1 << 12)
dist[0] = 0
q = deque([0])
while q:
    s = q.popleft()
    for col in cols:
        ns = s ^ col
        if dist[ns] == -1:
            dist[ns] = dist[s] + 1
            q.append(ns)
assert all(d >= 0 for d in dist)
assert sum(1 for d in dist if d <= 3) == 1 + 22 + 231 + 1540 == 1794
assert max(dist) == 7
print("(4) syndrome BFS OK: leaders<=3 count 1794, covering radius 7;",
      "leader dist =", sorted(Counter(dist).items()))
print("VERIFY_OK")
