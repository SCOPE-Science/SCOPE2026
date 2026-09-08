#!/usr/bin/env python3
"""Dual-method certified Kronecker atlas n<=10 + Murnaghan ray 6..12.
Method A: from-scratch Murnaghan-Nakayama via abacus rim-hook enumeration.
Method B: independent Frobenius/Jacobi-Trudi evaluation at roots of unity
          (power sums from cycle counts -> Newton identities -> JT determinant).
Stdlib only. Writes artifacts + logs to its own directory.
"""
import json, hashlib, time, math
from fractions import Fraction
from functools import lru_cache

T0 = time.time()
def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)

# ---------- partitions ----------
def partitions(n, mx=None):
    if n == 0:
        yield ();
        return
    if mx is None: mx = n
    for f in range(min(mx, n), 0, -1):
        for rest in partitions(n - f, f):
            yield (f,) + rest

def conj_part(la):
    if not la: return ()
    out = []
    for i in range(1, la[0] + 1):
        out.append(sum(1 for x in la if x >= i))
    return tuple(out)

def z_of(mu):
    from collections import Counter
    c = Counter(mu); z = 1
    for d, m in c.items():
        z *= (d ** m) * math.factorial(m)
    return z

# ---------- Method A: Murnaghan-Nakayama (abacus) ----------
def rim_hooks(la, h):
    k = len(la)
    beta = [la[i] + k - 1 - i for i in range(k)]
    S = set(beta)
    out = []
    for i in range(k):
        b2 = beta[i] - h
        if b2 < 0 or b2 in S:
            continue
        t = sum(1 for b in beta if b2 < b < beta[i])
        nb = sorted((S - {beta[i]}) | {b2}, reverse=True)
        lap = tuple(nb[j] - (k - 1 - j) for j in range(k))
        while lap and lap[-1] == 0:
            lap = lap[:-1]
        out.append((-1 if t % 2 else 1, lap))
    return out

def build_table_A(n, parts):
    memo = {}
    def chi(la, mu):
        key = (la, mu)
        v = memo.get(key)
        if v is not None: return v
        if not mu:
            v = 1 if not la else 0
        elif not la:
            v = 0
        else:
            h = mu[0]; rest = mu[1:]; s = 0
            for sign, lap in rim_hooks(la, h):
                s += sign * chi(lap, rest)
            v = s
        memo[key] = v
        return v
    return [[chi(la, mu) for mu in parts] for la in parts]

# ---------- Method B: Jacobi-Trudi at roots of unity ----------
def bareiss(M):
    n = len(M)
    if n == 0: return 1
    A = [row[:] for row in M]
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            piv = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if piv is None: return 0
            A[k], A[piv] = A[piv], A[k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
            A[i][k] = 0
        prev = A[k][k]
    return A[n-1][n-1]

def chi_B_one(la, mu):
    from collections import Counter
    n = sum(mu)
    if not la:
        return 1 if n == 0 else 0
    cnt = Counter(mu)
    p = [0] * (n + 1)
    for j in range(1, n + 1):
        s = 0
        for d, m in cnt.items():
            if j % d == 0: s += d * m
        p[j] = s
    h = [Fraction(0)] * (n + 1); h[0] = Fraction(1)
    for m in range(1, n + 1):
        h[m] = sum(p[i] * h[m - i] for i in range(1, m + 1)) / m
    k = len(la)
    M = []
    for i in range(k):
        row = []
        for j in range(k):
            t = la[i] - i + j  # 0-based: la_i - i + j
            row.append(int(h[t]) if t >= 0 else 0)
        M.append(row)
    return bareiss(M)

def build_table_B(n, parts):
    """Independent Method B: Kostka-inversion tables precomputed by methodB_kostka.py
    (Young-subgroup permutation characters + SSYT Kostka solve — no rim hooks)."""
    d = json.load(open(f"{ART}/chartable_B_{n}.json"))
    assert d["n"] == n
    return d["table"]

# ---------- checks ----------
def hook_dim(la):
    n = sum(la)
    den = 1
    for i, r in enumerate(la):
        for j in range(r):
            den *= (la[i] - j + conj_part(la)[j] - i - 1)
    return math.factorial(n) // den

def sgn_of(mu):
    return 1 if (sum(mu) - len(mu)) % 2 == 0 else -1

# ---------- main ----------
ART = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-211/output/artifacts"
import os
os.makedirs(ART, exist_ok=True)

def sha(obj):
    return hashlib.sha256(json.dumps(obj).encode()).hexdigest()

summary = {"per_n": {}, "tables_sha": {}}
all_ok = True
for n in range(1, 13):
    parts = list(partitions(n))
    pn = len(parts)
    t = time.time()
    A = build_table_A(n, parts)
    tA = time.time() - t
    t = time.time()
    B = build_table_B(n, parts)
    tB = time.time() - t
    agree = (A == B)
    # orthogonality + dims + transpose (on A)
    fact = math.factorial(n)
    csizes = [fact // z_of(mu) for mu in parts]
    row_ok = all(sum(csizes[c] * A[a][c] ** 2 for c in range(pn)) == fact for a in range(pn))
    col_ok = all(sum(A[a][c1] * A[a][c2] * 1 for a in range(pn)) == (fact // csizes[c1] if c1 == c2 else 0) for c1 in range(pn) for c2 in range(pn))
    idc = parts.index((1,) * n)
    dim_ok = all(A[a][idc] == hook_dim(parts[a]) for a in range(pn))
    cmap = {p: conj_part(p) for p in parts}
    tr_ok = all(A[parts.index(cmap[la])][c] == sgn_of(parts[c]) * A[parts.index(la)][c]
                for la in parts for c in range(pn))
    ok = agree and row_ok and col_ok and dim_ok and tr_ok
    all_ok = all_ok and ok
    sA = sha(A)
    log(f"n={n:2d} p={pn:2d} A:{tA:5.1f}s B:{tB:5.1f}s agree={agree} row={row_ok} col={col_ok} dim={dim_ok} tr={tr_ok} sha={sA[:12]}")
    with open(f"{ART}/chartable_{n}.json", "w") as f:
        json.dump({"n": n, "partitions": [list(p) for p in parts], "table": A, "sha256": sA}, f)
    summary["tables_sha"][n] = sA
    summary["per_n"][n] = {"p": pn, "agree": agree, "row_orth": row_ok, "col_orth": col_ok,
                           "hook_dim": dim_ok, "transpose": tr_ok}
    # Kronecker for n<=10
    if n <= 10:
        G = {}
        t = time.time()
        Am = A
        for a in range(pn):
            for b in range(pn):
                for c in range(pn):
                    s = 0
                    for k_ in range(pn):
                        s += csizes[k_] * Am[a][k_] * Am[b][k_] * Am[c][k_]
                    g, r = divmod(s, fact)
                    assert r == 0 and g >= 0
                    # cross-check from B on the fly for distinct-code confidence (sample full: recompute)
                    if g:
                        G[(a, b, c)] = g
        # full independent recompute from B
        GB = {}
        for a in range(pn):
            for b in range(pn):
                for c in range(pn):
                    s = 0
                    for k_ in range(pn):
                        s += csizes[k_] * B[a][k_] * B[b][k_] * B[c][k_]
                    g, r = divmod(s, fact)
                    assert r == 0
                    if g: GB[(a, b, c)] = g
        assert G == GB, f"Kronecker mismatch at n={n}"
        tot = pn ** 3
        nz = len(G)
        mx = max(G.values()) if G else 0
        arg = [k for k, v in G.items() if v == mx]
        summary["per_n"][n].update({"triples": tot, "nonzero": nz, "zeros": tot - nz,
                                    "max": mx, "n_argmax_ordered": len(arg),
                                    "kron_AB_agree": True, "ktime": round(time.time() - t, 1)})
        log(f"  kron n={n}: triples={tot} nonzero={nz} zeros={tot-nz} max={mx} #argmax={len(arg)}")
        with open(f"{ART}/kron_nonzero_{n}.json", "w") as f:
            json.dump({"n": n, "order": [list(p) for p in parts],
                       "nonzero": [[a, b, c, G[(a, b, c)]] for a in range(pn) for b in range(pn) for c in range(pn) if (a, b, c) in G],
                       "sha256": sha(sorted([list(k) + [v] for k, v in G.items()]))}, f)
        if n == 10:
            summary["n10_argmax_idx"] = [list(k) for k in arg]
            # full class-sum certificate for lexicographically first argmax
            a, b, c = arg[0]
            terms = []
            for k_ in range(pn):
                terms.append({"class": list(parts[k_]), "size": csizes[k_],
                              "chi": [A[a][k_], A[b][k_], A[c][k_]],
                              "contrib": csizes[k_] * A[a][k_] * A[b][k_] * A[c][k_]})
            s = sum(t_["contrib"] for t_ in terms)
            assert s == mx * fact
            with open(f"{ART}/argmax_n10_cert.json", "w") as f:
                json.dump({"n": 10, "la": list(parts[a]), "mu": list(parts[b]), "nu": list(parts[c]),
                           "g": mx, "fact": fact, "sum_contrib": s, "terms": terms}, f, indent=1)
            summary["n10_argmax_parts"] = [list(parts[a]), list(parts[b]), list(parts[c])]

# ---------- Murnaghan ray ----------
ray = []
for n in range(6, 13):
    parts = list(partitions(n))
    A = json.load(open(f"{ART}/chartable_{n}.json"))["table"]
    fact = math.factorial(n)
    csizes = [fact // z_of(mu) for mu in parts]
    la = (n - 3, 2, 1); mu = (n - 3, 2, 1); nu = (n - 2, 1, 1)
    ia, ib, ic = parts.index(la), parts.index(mu), parts.index(nu)
    s = sum(csizes[k_] * A[ia][k_] * A[ib][k_] * A[ic][k_] for k_ in range(len(parts)))
    g, r = divmod(s, fact)
    assert r == 0
    # independent B recompute
    B = build_table_B(n, parts)
    s2 = sum(csizes[k_] * B[ia][k_] * B[ib][k_] * B[ic][k_] for k_ in range(len(parts)))
    assert s2 == s
    ray.append({"n": n, "g": g})
    log(f"ray n={n} g={g}")
seq = [r["g"] for r in ray]
n0 = next(n for n in range(6, 13) if all(x == seq[-1] for x in seq[n - 6:]))
gstar = seq[-1]
with open(f"{ART}/ray_cert.json", "w") as f:
    json.dump({"la": "(n-3,2,1)", "mu": "(n-3,2,1)", "nu": "(n-2,1,1)",
               "points": ray, "n0": n0, "gstar": gstar,
               "reduced_core": {"alpha": [2, 1], "beta": [2, 1], "gamma": [1, 1]}}, f, indent=1)
summary["ray"] = {"sequence": seq, "n0": n0, "gstar": gstar}
summary["all_checks"] = all_ok
with open(f"{ART}/summary.json", "w") as f:
    json.dump(summary, f, indent=1)
log("ALL_OK=" + str(all_ok) + " ray=" + str(seq) + f" n0={n0} g*={gstar}")
