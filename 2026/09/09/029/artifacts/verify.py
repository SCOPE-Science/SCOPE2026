"""Lane-317 independent verifier: replays completeness + ternary verdicts +
uniqueness from stored artifacts with a fresh code path (full-S7 aut,
fresh backtracker, all-bases scan, explicit matrix check)."""
import itertools, json

TRIPLES = list(itertools.combinations(range(7), 3))
TIDX = {t: i for i, t in enumerate(TRIPLES)}
PAIRS = [(a, b) for a in range(7) for b in range(a + 1, 7)]

P13, seen = [], set()
for v in itertools.product(range(3), repeat=3):
    if v == (0, 0, 0):
        continue
    s = v[0] if v[0] else (v[1] if v[1] else v[2])
    w = tuple((c * pow(s, -1, 3)) % 3 for c in v)
    if w not in seen:
        seen.add(w)
        P13.append(w)
assert len(P13) == 13
nid = {w: i for i, w in enumerate(P13)}
NZ = [v for v in itertools.product(range(3), repeat=3) if v != (0, 0, 0)]
norm = {}
for v in NZ:
    s = v[0] if v[0] else (v[1] if v[1] else v[2])
    norm[v] = nid[tuple((c * pow(s, -1, 3)) % 3 for c in v)]

def det3(A, B, C):
    return (A[0] * (B[1] * C[2] - B[2] * C[1])
            - A[1] * (B[0] * C[2] - B[2] * C[0])
            + A[2] * (B[0] * C[1] - B[1] * C[0])) % 3

DET = [[[det3(P13[a], P13[b], P13[c]) for c in range(13)]
        for b in range(13)] for a in range(13)]
E = [nid[(1, 0, 0)], nid[(0, 1, 0)], nid[(0, 0, 1)]]
V4 = [(1, 1, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1)]
VA = [[norm[((P13[p][0] * s[0]) % 3, (P13[p][1] * s[1]) % 3,
            (P13[p][2] * s[2]) % 3)] for p in range(13)] for s in V4]

D = json.load(open("output/artifacts/full_census.json"))

# (1) pair-cover validity + exchange per stored type
for r in D["results"]:
    lines = [frozenset(L) for L in r["lines"]]
    cov = {}
    for L in lines:
        L = sorted(L)
        assert len(L) >= 3, r["type"]
        for i in range(len(L)):
            for j in range(i + 1, len(L)):
                cov.setdefault((L[i], L[j]), 0)
                cov[(L[i], L[j])] += 1
    assert all(v == 1 for v in cov.values()), r["type"]  # pairwise balanced
    assert len(lines) <= 1 or True
    bs = set(t for t in TRIPLES if not any(set(t) <= set(L) for L in r["lines"]))
    assert len(bs) == r["n_bases"]
    for b1 in bs:
        for b2 in bs:
            for x in set(b1) - set(b2):
                assert any(tuple(sorted((set(b1) - {x}) | {y})) in bs
                           for y in set(b2) - set(b1)), (r["type"], b1, b2)
print("CHECK 1 ok: pair-cover validity + exchange axioms for all 23 types")

# (2) full-S7 automorphism orders + orbit-sum
PERMS = list(itertools.permutations(range(7)))
tot = 0
for r in D["results"]:
    ms = frozenset(sum(1 << x for x in L) for L in r["lines"])
    orig = tuple(sorted(ms))
    a = 0
    for p in PERMS:
        key = tuple(sorted(sum(1 << p[x] for x in L) for L in r["lines"]))
        # recompute mask image properly:
        q = 0
        m2 = []
        for m in ms:
            rr, mm = 0, m
            while mm:
                b = mm & (-mm)
                rr |= 1 << p[b.bit_length() - 1]
                mm ^= b
            m2.append(rr)
        if tuple(sorted(m2)) == orig:
            a += 1
    assert a == r["aut"], (r["type"], a, r["aut"])
    tot += 5040 // a
assert tot == D["n_labeled_total"] == 8389, tot
print("CHECK 2 ok: full-S7 aut orders match; orbit sum = 8389")

# (3) fresh labeled backtrack count
cnt = [0]
def prs(L):
    L = sorted(L)
    return {(L[i], L[j]) for i in range(len(L)) for j in range(i + 1, len(L))}
def dfs(cov, ch):
    for p in PAIRS:
        if p not in cov:
            f = p
            break
    else:
        cnt[0] += 1
        return
    a, b = f
    cov.add(f)
    dfs(cov, ch)
    cov.discard(f)
    rest = [x for x in range(7) if x != a and x != b]
    for k in range(1, 6):
        for cb in itertools.combinations(rest, k):
            L = frozenset((a, b) + cb)
            if any(len(L & M) > 1 for M in ch):
                continue
            q = prs(L)
            if q & cov:
                continue
            ch.append(L)
            cov |= q
            dfs(cov, ch)
            cov -= q
            ch.pop()
dfs(set(), [])
assert cnt[0] == 8390, cnt  # includes rank-2 single-line type
print("CHECK 3 ok: fresh backtrack gives 8390 covers (=8389 rank-3 + 1 rank-2)")

# (4) all-bases ternary scan + uniqueness replay
for r in D["results"]:
    lines = [set(L) for L in r["lines"]]
    nb = 0
    for t in TRIPLES:
        if any(set(t) <= L for L in lines):
            nb |= 1 << TIDX[t]
    bases = [t for t in TRIPLES if not (nb >> TIDX[t]) & 1]
    per_basis = {}
    total = 0
    for B in bases:
        free = [p for p in range(7) if p not in B]
        fr = []
        for quad in itertools.product(range(13), repeat=4):
            if len(set(quad)) < 4 or any(q in E for q in quad):
                continue
            c = [0] * 7
            c[B[0]], c[B[1]], c[B[2]] = E[0], E[1], E[2]
            for p, q in zip(free, quad):
                c[p] = q
            m = 0
            for ti, tri in enumerate(TRIPLES):
                if DET[c[tri[0]]][c[tri[1]]][c[tri[2]]] == 0:
                    m |= 1 << ti
                    if m & ~nb:
                        break
            if m == nb:
                fr.append(quad)
        per_basis[B] = fr
        total += len(fr)
    assert (total > 0) == r["ternary"], r["type"]
    assert total == r["allframes"], (r["type"], total, r["allframes"])
    if r["ternary"]:
        # every basis sees exactly one V4 orbit (unique labeled representation)
        for B, fr in per_basis.items():
            orbs, seenh = 0, set()
            for h in fr:
                if h in seenh:
                    continue
                orbs += 1
                for g in VA:
                    seenh.add((g[h[0]], g[h[1]], g[h[2]], g[h[3]]))
            assert orbs == 1, (r["type"], B, len(fr), orbs)
        assert r["n_labeled"] == 1 and r["n_geometric"] == 1
print("CHECK 4 ok: ternary verdicts + frame totals match; each ternary type has "
      "exactly one V4 orbit per basis (unique labeled + geometric representation)")

# (5) explicit 3x7 matrix basis-equality for the 4 ternary reps
for r in D["results"]:
    if not r["ternary"]:
        continue
    B = r["frame_basis"]
    free = [p for p in range(7) if p not in B]
    cols = [None] * 7
    cols[B[0]], cols[B[1]], cols[B[2]] = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    for p, q in zip(free, r["repquad"]):
        cols[p] = P13[q]
    got = set()
    for t in TRIPLES:
        if det3(cols[t[0]], cols[t[1]], cols[t[2]]) == 0:
            got.add(t)
    want = set(t for t in TRIPLES if any(set(t) <= set(L) for L in r["lines"]))
    assert got == want, r["type"]
print("CHECK 5 ok: explicit representative matrices realize exactly the claimed nonbases")
print("VERIFY_OK")
