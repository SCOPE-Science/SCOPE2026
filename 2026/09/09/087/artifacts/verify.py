"""Auditable replay for C_{8,2} full e-vector (preset fallback).
Steps:
 1. Build C_{8,2}, check circular-indifference membership (Ellzey Def 5.1) + edge count.
 2. S_8 G-descent/inv enumeration (Thm 3.1): delta(k,l) table; Cor 3.3 t-chromatic cross-check at m=2,3,4
    against direct proper-coloring enumeration.
 3. Exact e-coefficients via proper ordered-partition scan + exact e-basis solve (stdlib Fractions).
 4. Thm 6.5 row-sum check: sum_{l(lam)=k} c_lam(t) vs acyclic-orientation sink distribution (2^16 scan).
 5. Nonnegativity + palindromicity (center |E|/2=8) + unimodality checks.
 6. Byte-identity: compare against committed output/artifacts/ctable_82.json.
Writes output/artifacts/verify_log.json. Prints VERIFY_OK on success.
"""
import sys, json, itertools
sys.path.insert(0, 'output/artifacts')
from fractions import Fraction
from collections import Counter, defaultdict
from math import factorial
from ellzey import build, check_circular_indifference, stats
from sym import partitions, e_basis_monomial_matrix, invert_matrix

N, K = 8, 2
arcs, adj = build(N, K)
ok, ngen, nedge = check_circular_indifference(N, K)
assert ok and nedge == 16, (ok, ngen, nedge)
print(f"[1] membership OK: generated={ngen} edges={nedge}")

# ---- Step 2: S8 G-descent/inv census ----
delta = Counter(); invdist = Counter()
for sigma in itertools.permutations(range(N)):
    _, des, inv = stats(list(sigma), arcs, adj)
    delta[(len(des), inv)] += 1
    invdist[inv] += 1
assert sum(delta.values()) == 40320
print(f"[2] S8 census OK: 40320 perms, distinct (k,l) cells={len(delta)}")

def chi_cor33(m):
    from math import comb
    tot = Counter()
    for (k, l), c in delta.items():
        tot[l] += c * comb(m + k, N)
    return tot
def chi_direct(m):
    tot = Counter()
    for kappa in itertools.product(range(m), repeat=N):
        good = True
        for a in range(N):
            for b in range(a + 1, N):
                if adj[a][b] and kappa[a] == kappa[b]:
                    good = False; break
            if not good: break
        if not good: continue
        asc = sum(1 for (u, v) in arcs if kappa[u] < kappa[v])
        tot[asc] += 1
    return tot
for m in (2, 3):
    a, b = chi_cor33(m), chi_direct(m)
    assert a == b, (m, dict(a), dict(b))
    print(f"[2] Cor3.3 chi(m={m}) match OK: {dict(sorted(a.items()))}")
# m=4 direct is 4^8=65536, also cheap
a, b = chi_cor33(4), chi_direct(4)
assert a == b
print(f"[2] Cor3.3 chi(m=4) match OK: terms={len(a)} total={sum(a.values())}")

# ---- Step 3: e-coefficients ----
indep = []
for mask in range(1, 1 << N):
    vs = [v for v in range(N) if mask >> v & 1]
    if all(not adj[vs[a]][vs[b]] for a in range(len(vs)) for b in range(a + 1, len(vs))):
        indep.append(mask)
by_min = defaultdict(list)
for msk in indep:
    v = (msk & (-msk)).bit_length() - 1
    by_min[v].append(msk)
full = (1 << N) - 1
W = defaultdict(Counter)
stack = [(0, [])]
while stack:
    used, blocks = stack.pop()
    if used == full:
        for perm in itertools.permutations(blocks):
            rank = [0] * N
            for r, B in enumerate(perm):
                mm = B
                while mm:
                    lsb = mm & (-mm); v = lsb.bit_length() - 1
                    rank[v] = r; mm ^= lsb
            asc = sum(1 for (u, v) in arcs if rank[u] < rank[v])
            mu = tuple(sorted(([bin(B).count('1') for B in blocks]), reverse=True))
            W[mu][asc] += 1
        continue
    v = next(v for v in range(N) if not (used >> v & 1))
    for B in by_min[v]:
        if B & used == 0:
            stack.append((used | B, blocks + [B]))
parts = list(partitions(N))
amat = {}
for mu in parts:
    tmu = tuple(mu)
    c = Counter(mu); l = len(mu)
    norders = factorial(l)
    for v in c.values(): norders //= factorial(v)
    amat[tmu] = defaultdict(Fraction)
    for pwr, cnt in W.get(tmu, {}).items():
        amat[tmu][pwr] = Fraction(cnt, norders)
for mu in parts:
    for pwr, v in amat[tuple(mu)].items():
        assert v.denominator == 1, (mu, pwr, v)
maxdeg = max(max(d.keys()) for d in W.values() if d)
_, E = e_basis_monomial_matrix(N, q=N)
Einv = invert_matrix(E)
cpolys = {tuple(lam): defaultdict(Fraction) for lam in parts}
for pwr in range(maxdeg + 1):
    avec = [amat[tuple(mu)].get(pwr, Fraction(0)) for mu in parts]
    cvec = [sum(Einv[i][j] * avec[j] for j in range(len(parts))) for i in range(len(parts))]
    for i, lam in enumerate(parts):
        if cvec[i] != 0:
            cpolys[tuple(lam)][pwr] = cvec[i]
ctab = {str(tuple(l)): {str(p): int(v) for p, v in sorted(d.items())} for l, d in cpolys.items()}
print(f"[3] e-solve OK: nonzero lambdas={[l for l in ctab]}")
for l, d in sorted(ctab.items()):
    print(f"    {l}: {d}")

# ---- Step 4: Thm 6.5 row sums via acyclic orientations ----
edges = sorted({tuple(sorted((u, v))) for (u, v) in arcs})
assert len(edges) == 16
areset = set(arcs)
rowsinks = defaultdict(Counter)
nacy = 0
for bits in range(1 << 16):
    # orient edge i from a->b if bit else b->a
    succ = [[] for _ in range(N)]
    for i, (a, b) in enumerate(edges):
        if (bits >> i) & 1: succ[a].append(b)
        else: succ[b].append(a)
    # acyclicity via Kahn
    indeg = [0] * N
    for a in range(N):
        for b in succ[a]: indeg[b] += 1
    q = [a for a in range(N) if indeg[a] == 0]
    seen = 0
    qi = 0
    while qi < len(q):
        a = q[qi]; qi += 1; seen += 1
        for b in succ[a]:
            indeg[b] -= 1
            if indeg[b] == 0: q.append(b)
    if seen < N: continue
    nacy += 1
    nsinks = sum(1 for a in range(N) if not succ[a])
    asc = sum(1 for (u, v) in arcs if v in succ[u])
    rowsinks[nsinks][asc] += 1
print(f"[4] acyclic orientations: {nacy}")
for k in sorted(rowsinks):
    lhs = Counter()
    for lam, d in cpolys.items():
        if len(lam) == k:
            for p, v in d.items(): lhs[p] += v
    rhs = rowsinks[k]
    assert set(lhs) == set(rhs) and all(lhs[p] == rhs[p] for p in lhs), (k, dict(lhs), dict(rhs))
    print(f"[4] row l={k} match OK: {dict(sorted((p, int(v)) for p, v in lhs.items()))}")

# ---- Step 5: nonnegativity / palindromicity / unimodality ----
ED = len(arcs)
for lam, d in cpolys.items():
    for p, v in d.items():
        assert v >= 0 and v.denominator == 1, (lam, p, v)
    if d:
        ps = sorted(d)
        assert ps[0] + ps[-1] == ED, (lam, ps)
        for p in ps:
            assert d.get(ED - p, 0) == d[p], (lam, p)
        seq = [int(d[p]) for p in range(ps[0], ps[-1] + 1)]
        peak = max(range(len(seq)), key=lambda i: seq[i])
        assert all(seq[i] <= seq[i+1] for i in range(peak)) and all(seq[i] >= seq[i+1] for i in range(peak, len(seq)-1)), (lam, seq)
print(f"[5] nonneg + palindromic(center {ED}/2=8) + unimodal OK for all nonzero c_lam")

# ---- Step 6: byte identity vs committed table ----
committed = json.load(open('output/artifacts/ctable_82.json'))
mine = {str(tuple(sorted(lam, reverse=True))): {str(p): int(v) for p, v in sorted(d.items())} for lam, d in cpolys.items()}
# committed stores only nonzero; normalize keys
assert set(committed) == set(mine), (set(committed) ^ set(mine))
for lam in committed:
    assert committed[lam] == mine[lam], lam
print("[6] byte-identity vs ctable_82.json OK")
json.dump({"status": "VERIFY_OK", "n": N, "k": K, "edges": ED,
           "acyclic_orientations": nacy, "e_table": mine,
           "delta_cells": len(delta)},
          open('output/artifacts/verify_log.json', 'w'), indent=1, sort_keys=True)
print("VERIFY_OK")
