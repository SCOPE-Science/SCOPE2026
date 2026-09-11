"""Independent replay verifier for the DCLS(11) census (stdlib only).
Checks:
 1. seeds.json: 363 entries, each a normalized orthomorphism (theta(0)=0,
    theta|_{1..10} and psi(d)=theta(d)-d permutations of 1..10); canonical
    (orbit-min under theta^a(d)=a*theta(a^-1 d)); pairwise non-isomorphic;
    complete (fresh column-order enumeration of all 3441 normalized
    orthomorphisms, every orbit's min is in the archived set).
 2. count_log_A.json vs count_log_B.json: same seeds, byte-equal counts;
    recount every seed with a THIRD method (column-permutation S_n search:
    fix rows, iterate col permutations via itertools with symbol check)
    on a deterministic spot sample + full row/column/symbol Latin check of
    each square; verify spectrum.json aggregates.
 3. mate_certificate.json: M Latin; orthogonal to every seed square by pair
    enumeration; each T_m a transversal.
Run: python3 replay.py  -> prints REPLAY_OK or raises.
"""
import json, itertools

N = 11
seeds = json.load(open("seeds.json"))
logA = json.load(open("count_log_A.json"))
logB = json.load(open("count_log_B.json"))
spec = json.load(open("spectrum.json"))
mate = json.load(open("mate_certificate.json"))

# 1. seed validity + canonical + distinctness
S = [tuple(e) for e in seeds["seeds"]]
assert len(S) == seeds["C"] == 363 == len(set(S)), "seed count/uniqueness"
def apply_mul(t, a):
    inv = pow(a, -1, N)
    return tuple((a*t[(inv*d) % N]) % N for d in range(N))
for t in S:
    assert t[0] == 0 and sorted(t[1:]) == list(range(1, N)), f"theta not normalized perm: {t}"
    assert sorted((t[d]-d) % N for d in range(1, N)) == list(range(1, N)), f"psi fail: {t}"
    assert t == min(apply_mul(t, a) for a in range(1, N)), f"not canonical: {t}"
for i in range(len(S)):
    oi = {apply_mul(S[i], a) for a in range(1, N)}
    for j in range(i+1, len(S)):
        assert S[j] not in oi, f"isomorphic pair {i},{j}"
print("seeds valid/canonical/distinct: 363", flush=True)

# completeness: fresh enumeration in reverse value order (different path from run_all)
th = [-1]*N; th[0] = 0; ut = {0}; up = {0}; alls = []
import sys; sys.setrecursionlimit(10000)
def bt(i):
    if i == N: alls.append(tuple(th)); return
    for v in range(N-1, 0, -1):
        if v in ut: continue
        w = (v-i) % N
        if w == 0 or w in up: continue
        th[i] = v; ut.add(v); up.add(w); bt(i+1); ut.discard(v); up.discard(w)
bt(1)
assert len(alls) == 3441 == seeds["total_normalized"], f"total {len(alls)}"
assert {min(apply_mul(t, a) for a in range(1, N)) for t in alls} == set(S), "incomplete seed set"
print("completeness: 3441 orbits covered by 363 seeds", flush=True)

# 2. log agreement + Latin check + third-method spot recount
assert [e["seed"] for e in logA] == [e["seed"] for e in logB] == seeds["seeds"]
assert all(a["count"] == b["count"] for a, b in zip(logA, logB)), "A/B mismatch"
def square_of(th):
    return [[(th[(j-i) % N]+i) % N for j in range(N)] for i in range(N)]
for e in logA:
    L = square_of(e["seed"])
    assert all(sorted(r) == list(range(N)) for r in L)
    assert all(sorted(L[i][j] for i in range(N)) == list(range(N)) for j in range(N))
def count_rev(L):
    # THIRD method: backtrack rows in REVERSE order with integer bitmasks
    # (different traversal from A's forward order and B's MRV exact cover).
    n = len(L); cnt = [0]
    order = list(range(n-1, -1, -1))
    def rec(k, uc, us):
        if k == n: cnt[0] += 1; return
        row = L[order[k]]
        for c in range(n-1, -1, -1):
            b = 1 << c
            if uc & b: continue
            sb = 1 << row[c]
            if us & sb: continue
            rec(k+1, uc|b, us|sb)
    rec(0, 0, 0)
    return cnt[0]
import hashlib
for e in logA[::36]:  # 11 deterministic spot seeds incl. index 360 (group square)
    c = count_rev(square_of(e["seed"]))
    assert c == e["count"], f"third-method mismatch {e['seed']}: {c} vs {e['count']}"
print("A/B byte-agreement + Latin + 3rd-method spots ok", flush=True)
from collections import Counter
dist = dict(sorted(Counter(e["count"] for e in logA).items()))
assert {str(k): v for k, v in dist.items()} == spec["spectrum"], "spectrum mismatch"
assert spec["M_DCLS"] == max(dist) == 37851 and sum(1 for e in logA if e["count"] == 37851) == 9
assert spec["S_max"] in [e["seed"] for e in logA if e["count"] == 37851]
print("spectrum ok:", dist, flush=True)

# 3. mate certificate
M = mate["universal_mate"]
assert all(sorted(r) == list(range(N)) for r in M)
assert all(sorted(M[i][j] for i in range(N)) == list(range(N)) for j in range(N))
for th in S:
    L = square_of(list(th))
    assert len({(L[i][j], M[i][j]) for i in range(N) for j in range(N)}) == N*N
    for m in range(N):
        cells = [(i, (i+m) % N) for i in range(N)]
        assert len({L[i][j] for i, j in cells}) == N
assert mate["K"] == mate["C"] == 363
print("mates ok: K=363/363", flush=True)
print("REPLAY_OK")
