#!/usr/bin/env python3
"""Method B (independent): Kostka inversion route.
xi_la(mu) = permutation character of Young subgroup S_la at class mu
          = coefficient of x^la in prod_{d in mu} (x_1^d+...+x_r^d)
          = #{assignments of cycles to rows with row sums la_i}   (DP)
K[tau][wt] = # SSYT of shape tau, weight wt (horizontal-strip recursion)
xi_la = sum_tau K[tau][la] chi_tau  =>  chi = K^{-1} xi  (unitriangular solve)
Writes chartable_B_<n>.json per n. Stdlib only.
"""
import json, time, math
from functools import lru_cache

T0 = time.time()
def log(m): print(f"[{time.time()-T0:6.1f}s] {m}", flush=True)

def partitions(n, mx=None):
    if n == 0:
        yield (); return
    if mx is None: mx = n
    for f in range(min(mx, n), 0, -1):
        for rest in partitions(n - f, f):
            yield (f,) + rest

def subdiagrams(la):
    """All diagrams mu subset of la (row lengths mu_i<=la_i, nonincreasing)."""
    k = len(la)
    def rec(i, cap, cur):
        if i == k:
            yield tuple(cur); return
        for v in range(min(la[i], cap), -1, -1):
            cur.append(v)
            yield from rec(i + 1, v, cur)
            cur.pop()
    yield from rec(0, la[0] if la else 0, [])

def strip_removable(D, S):
    """Check D\\S is a diagram (S given as tuple of removed counts per row)."""
    R = tuple(D[i] - S[i] for i in range(len(D)))
    while R and R[-1] == 0: R = R[:-1]
    return all(R[i] >= R[i+1] for i in range(len(R)-1))

def removable_hstrips(D, w):
    """Removable horizontal strips of size w: S<=D per-row, no two removed cells
    in same column, D\\S a diagram. Removed cells in row i: rightmost S_i cells."""
    k = len(D); out = []
    def rec(i, rem, S):
        if i == k:
            if rem == 0 and strip_removable(D, tuple(S)): out.append(tuple(S))
            return
        for s in range(min(D[i], rem), -1, -1):
            # no two removed in same column: removed cols in row i are (D[i]-s, D[i]];
            # removed cols in row i-1 are (D[i-1]-S[i-1], D[i-1]]; need disjoint.
            if i > 0 and s > 0 and S[i-1] > 0:
                lo_prev = D[i-1] - S[i-1]
                lo_cur = D[i] - s
                # intervals (lo_prev, D[i-1]] and (lo_cur, D[i]] must be disjoint;
                # since D[i-1]>=D[i], disjoint iff D[i-1] - S[i-1] >= D[i]
                if D[i-1] - S[i-1] < D[i]:
                    # overlap: columns shared. Not allowed.
                    pass
                else:
                    S.append(s); rec(i+1, rem-s, S); S.pop()
                continue
            S.append(s); rec(i+1, rem-s, S); S.pop()
    rec(0, w, [])
    return out

def kostka_row(shape, weight):
    """# SSYT of given shape and weight via horizontal-strip recursion."""
    memo = {}
    def count(D, ws):
        D = tuple(D)
        while D and D[-1] == 0: D = D[:-1]
        D = D if D else ()
        if not ws: return 1 if not D else 0
        if not D: return 0
        if sum(ws) != sum(D): return 0
        key = (D, ws)
        v = memo.get(key)
        if v is not None: return v
        v = sum(count(tuple(D[i]-S[i] for i in range(len(D))), ws[1:])
                for S in removable_hstrips(D, ws[0]))
        memo[key] = v
        return v
    return count(tuple(shape), tuple(weight))

def perm_char(la, mu):
    """DP over cycles: assign each cycle to a row; row sums must equal la."""
    r = len(la)
    dp = {tuple([0]*r): 1}
    for d in mu:
        ndp = {}
        for state, c in dp.items():
            for i in range(r):
                if state[i] + d <= la[i]:
                    ns = state[:i] + (state[i]+d,) + state[i+1:]
                    ndp[ns] = ndp.get(ns, 0) + c
        dp = ndp
    return dp.get(tuple(la), 0)

ART = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-211/output/artifacts"

for n in range(1, 13):
    t = time.time()
    parts = list(partitions(n))
    pn = len(parts)
    # Kostka matrix K[shape][weight]
    K = [[kostka_row(s, w) for w in parts] for s in parts]
    # dominance order for triangular solve: sort indices by (sum of partial sums) key
    def domkey(p): return [sum(p[:i]) for i in range(1, len(p)+1)] + [0]*(n-len(p))
    order = sorted(range(pn), key=lambda i: domkey(parts[i]), reverse=True)
    pos = {o: i for i, o in enumerate(order)}
    # check unitriangularity structure: K[s][w] != 0 => shape s dominates w
    tri_ok = True
    for si in range(pn):
        for wi in range(pn):
            if K[si][wi] != 0:
                a, b = parts[si], parts[wi]
                if any(sum(a[:i]) < sum(b[:i]) for i in range(1, max(len(a), len(b))+1)):
                    tri_ok = False
    # permutation characters Xi[weight-la][mu]
    Xi = [[perm_char(la, mu) for mu in parts] for la in parts]
    # Solve the full system: for each class ci,
    # vector y_la = Xi[la][ci], matrix M[la][tau] = K[tau][la]; solve M x = y.
    Chib = [[0]*pn for _ in range(pn)]
    for ci in range(pn):
        y = [Xi[li][ci] for li in range(pn)]
        x = {}
        # process weights in order of increasing dominance (most-dominated first):
        # equation for la involves shapes tau dominating la; when processing la from
        # bottom (least dominant) up... K[tau][la]!=0 => tau dominates la, so tau is
        # at-or-above la in order. Process la from top (most dominant) first: then
        # tau==la term plus already-solved (more dominant) taus? No: tau dominates la
        # includes la itself and shapes ABOVE la = earlier in `order`. So iterate `order`
        # from first to last; at step la, unknowns x[tau] for tau above already known.
        for li in order:
            s = y[li] - sum(K[tau][li] * x[tau] for tau in order if pos[tau] < pos[li])
            d = K[li][li]
            assert d == 1, (n, parts[li])
            x[li] = s
        for si in range(pn):
            Chib[si][ci] = x[si]
    assert tri_ok
    with open(f"{ART}/chartable_B_{n}.json", "w") as f:
        json.dump({"n": n, "table": Chib}, f)
    log(f"n={n:2d} p={pn:2d} tri_ok={tri_ok} time={time.time()-t:.1f}s")
log("METHOD B DONE")
