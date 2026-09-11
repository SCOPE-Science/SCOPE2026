"""Construct the q=4 Section-3 Hermitian-unital host instance H_4^* (seed 20260911).
Stdlib only. Writes h4star.json. Verifies: |H|=65, 208 secants, 65 tangents,
per-point 16-cliques pairwise sharing <=1 vertex, instance K4-free.
"""
import json, os, random
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "h4star.json")
SEED = 20260911
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
assert len(pts) == 273
def p5(a): return gf_pow(a, 5)
H = [p for p in pts if (p5(p[0]) ^ p5(p[1]) ^ p5(p[2])) == 0]
assert len(H) == 65
def on_line(pt, ln):
    return (gf_mul(ln[0], pt[0]) ^ gf_mul(ln[1], pt[1]) ^ gf_mul(ln[2], pt[2])) == 0
secants = [ln for ln in pts if sum(1 for p in H if on_line(p, ln)) == 5]
tangents = [ln for ln in pts if sum(1 for p in H if on_line(p, ln)) == 1]
assert len(secants) == 208 and len(tangents) == 65
vid = {s: i for i, s in enumerate(secants)}
cliques = []
for p in H:
    m = sorted(vid[s] for s in secants if on_line(p, s))
    assert len(m) == 16
    cliques.append(m)
for i in range(65):
    Si = set(cliques[i])
    for j in range(i + 1, 65):
        assert len(Si & set(cliques[j])) <= 1
n = 208
rng = random.Random(SEED)
adj = [0] * n; parts = []
for c in cliques:
    Aset = {v for v in c if rng.random() < 0.5}
    A = sorted(Aset); B = sorted(set(c) - Aset)
    parts.append([A, B])
    for u in A:
        for v in B:
            adj[u] |= (1 << v); adj[v] |= (1 << u)
k4 = 0
for u in range(n):
    for v in range(u + 1, n):
        if (adj[u] >> v) & 1:
            cn = adj[u] & adj[v]
            cn >>= (v + 1); lst = []; w = v + 1
            while cn:
                if cn & 1: lst.append(w)
                w += 1; cn >>= 1
            for i in range(len(lst)):
                for j in range(i + 1, len(lst)):
                    if (adj[lst[i]] >> lst[j]) & 1: k4 += 1
assert k4 == 0, "instance not K4-free"
json.dump({"seed": SEED, "n": n, "secants": secants, "cliques": cliques,
           "parts": parts, "adj": adj}, open(OUT, "w"))
print("wrote", OUT, "edges:", sum(bin(x).count("1") for x in adj) // 2, "K4:", k4)
