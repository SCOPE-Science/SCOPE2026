"""Full replay verifier (stdlib only). Rebuilds GF(16)/PG(2,16)/unital/secants/
cliques from scratch, checks filed instance consistency, K4-freeness, 35-set.
Usage: python3 verify.py  -> prints VERIFY_OK or raises AssertionError."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(D, "h4star.json")))
assert d["seed"] == 20260911 and d["n"] == 208
def gf_mul(a, b):
    p = 0
    while b:
        if b & 1: p ^= a
        a <<= 1
        if a & 0x10: a ^= 0x13
        b >>= 1
    return p & 0xF
def gf_pow(a, e):
    r = 1; x = a
    while e:
        if e & 1: r = gf_mul(r, x)
        x = gf_mul(x, x); e >>= 1
    return r
def gf_inv(a): return gf_pow(a, 14)
pts, index = [], {}
for z in range(16):
    for y in range(16):
        for x in range(16):
            if x == 0 and y == 0 and z == 0: continue
            if x != 0:
                inv = gf_inv(x); key = (1, gf_mul(y, inv), gf_mul(z, inv))
            elif y != 0:
                inv = gf_inv(y); key = (0, 1, gf_mul(z, inv))
            else: key = (0, 0, 1)
            if key not in index: index[key] = len(pts); pts.append(key)
assert len(pts) == 273, "PG(2,16) must have 273 points"
def p5(a): return gf_pow(a, 5)
H = [p for p in pts if (p5(p[0]) ^ p5(p[1]) ^ p5(p[2])) == 0]
assert len(H) == 65, "unital must have q^3+1=65 points"
def on_line(pt, ln):
    return (gf_mul(ln[0], pt[0]) ^ gf_mul(ln[1], pt[1]) ^ gf_mul(ln[2], pt[2])) == 0
secants = [ln for ln in pts if sum(1 for p in H if on_line(p, ln)) == 5]
tangents = [ln for ln in pts if sum(1 for p in H if on_line(p, ln)) == 1]
assert len(secants) == 208 and len(tangents) == 65
assert sorted(map(list, secants)) == sorted(map(list, d["secants"])), "secant ledger mismatch"
n = 208
vid = {tuple(s): i for i, s in enumerate(secants)}
rebuilt = []
for p in H:
    rebuilt.append(sorted(vid[tuple(s)] for s in secants if on_line(p, s)))
assert all(len(c) == 16 for c in rebuilt)
assert sorted(map(sorted, rebuilt)) == sorted(map(sorted, d["cliques"])), "clique ledger mismatch"
for i in range(65):
    Si = set(rebuilt[i])
    for j in range(i + 1, 65):
        assert len(Si & set(rebuilt[j])) <= 1
# instance consistency: adj must equal union of complete bipartites from parts
adj = d["adj"]; parts = d["parts"]
assert len(adj) == 208 and len(parts) == 65
expect = [0] * n
for k, c in enumerate(rebuilt):
    A, B = parts[k]
    assert sorted(A) == A and sorted(B) == B
    assert set(A) | set(B) == set(c) and not (set(A) & set(B)), f"partition {k} invalid"
    for u in A:
        for v in B:
            expect[u] |= (1 << v); expect[v] |= (1 << u)
assert expect == adj, "adjacency inconsistent with Section-3 bipartition ledger"
k4 = 0
for u in range(n):
    for v in range(u + 1, n):
        if (adj[u] >> v) & 1:
            cn = (adj[u] & adj[v]) >> (v + 1); lst = []; w = v + 1
            while cn:
                if cn & 1: lst.append(w)
                w += 1; cn >>= 1
            for i in range(len(lst)):
                ai = adj[lst[i]]
                for j in range(i + 1, len(lst)):
                    if (ai >> lst[j]) & 1: k4 += 1
assert k4 == 0, "instance must be K4-free"
LOWER = [8, 10, 13, 16, 17, 20, 27, 31, 39, 43, 45, 49, 51, 62, 63, 79, 84, 101,
         118, 124, 127, 128, 132, 133, 134, 139, 140, 151, 153, 165, 166, 170,
         175, 185, 197]
assert len(LOWER) == 35 and len(set(LOWER)) == 35 and all(0 <= v < 208 for v in LOWER)
for i in range(35):
    for j in range(i + 1, 35):
        assert not (adj[LOWER[i]] >> LOWER[j]) & 1, "witness not independent"
print("VERIFY_OK geometry(273/65/208/65) cliques(65x16,pairwise<=1) bipartition-consistent K4=0 alpha>=35>26")
