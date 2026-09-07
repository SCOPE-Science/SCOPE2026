#!/usr/bin/env python3
"""Exact two-monomer Kasteleyn census on 6xN rectangles (N=6..10).

Method (per orbit (N,u,v) with u,v opposite colours):
  A. Per-graph Kasteleyn orientation: enumerate planar faces by half-edge
     traversal, solve the GF(2) odd-clockwise system for flip variables,
     verify every finite face is odd-clockwise. (The fixed inherited
     orientation of the full grid FAILS on separated-hole faces, so
     per-graph solving is required -- see Lemma in DRAFT.md.)
  B. Exact integer Pfaffian via modular determinants + CRT:
     det(K) recovered exactly over 7 small primes, Pf=isqrt(det),
     assert Pf*Pf==det.
  C. Independent exact profile-DP enumeration (transfer matrix, 2^6 states);
     assert Pf==DP for every orbit.
Plus: pure-dimer baselines, correlation ratios, max-C witnesses with
validated coverings and flip-path logs, single-monomer parity checks,
and a Temperley-bijection cross-check on Temperleyan regions
(trees(m x n) == dimers((2m-1)x(2n-1) minus one corner)).

Deps: stdlib + numpy only. Runtime: seconds.
Usage: python3 kasteleyn_census.py [--outdir DIR]
Outputs: census.csv, summary.json, witnesses.json (JSON-serialisable certs).
"""
import argparse
import csv
import json
import math
import os
import sys
import time
from collections import deque

try:
    import numpy as np
except ImportError:
    sys.exit("numpy is required")

R = 6
NS = (6, 7, 8, 9, 10)
PRIMES = (100003, 100019, 100043, 100057, 100069, 100103, 100109)

# ---------------- grid ----------------

def color(v):
    return (v[0] + v[1]) % 2


def build_graph(N, holes):
    H = set(holes)
    V = [(r, c) for r in range(R) for c in range(N) if (r, c) not in H]
    S = set(V)
    E = []
    for (r, c) in V:
        if (r, c + 1) in S:
            E.append(((r, c), (r, c + 1)))
        if (r + 1, c) in S:
            E.append(((r, c), (r + 1, c)))
    return V, E


def sym_group(N):
    fns = [
        ("id", lambda r, c: (r, c)),
        ("rot180", lambda r, c: (R - 1 - r, N - 1 - c)),
        ("flipH", lambda r, c: (R - 1 - r, c)),
        ("flipV", lambda r, c: (r, N - 1 - c)),
    ]
    if R == N:
        fns += [
            ("transp", lambda r, c: (c, r)),
            ("anti", lambda r, c: (N - 1 - c, N - 1 - r)),
            ("rot90", lambda r, c: (c, N - 1 - r)),
            ("rot270", lambda r, c: (N - 1 - c, r)),
        ]
    return fns


def canon_pair(u, v, N):
    best = None
    for _, f in sym_group(N):
        a = f(*u)
        b = f(*v)
        key = tuple(sorted([a, b]))
        if best is None or key < best:
            best = key
    return best


def orbit_reps(N):
    Vall = [(r, c) for r in range(R) for c in range(N)]
    seen = set()
    reps = []
    for u in Vall:
        for v in Vall:
            if v <= u:
                continue
            if color(u) == color(v):
                continue
            c = canon_pair(u, v, N)
            if c not in seen:
                seen.add(c)
                reps.append((u, v))
    return reps


def stratum(v, N):
    r, c = v
    if (r in (0, R - 1)) and (c in (0, N - 1)):
        return "corner"
    if r in (0, R - 1) or c in (0, N - 1):
        return "edge"
    return "bulk"


# ---------------- exact profile-DP counter (ground truth) ----------------

def count_dp(N, holes):
    blocked = set(holes)

    def trans(col, inmask):
        occ = [False] * R
        for r in range(R):
            if (r, col) in blocked:
                if (inmask >> r) & 1:
                    return {}
                occ[r] = True
            elif (inmask >> r) & 1:
                occ[r] = True
        res = {}

        def dfs(r, outmask):
            while r < R and occ[r]:
                r += 1
            if r == R:
                res[outmask] = res.get(outmask, 0) + 1
                return
            if r + 1 < R and not occ[r + 1]:
                occ[r] = occ[r + 1] = True
                dfs(r + 1, outmask)
                occ[r] = occ[r + 1] = False
            if col + 1 < N and (r, col + 1) not in blocked:
                occ[r] = True
                dfs(r + 1, outmask | (1 << r))
                occ[r] = False

        dfs(0, 0)
        return res

    dp = {0: 1}
    for c in range(N):
        ndp = {}
        for inmask, w in dp.items():
            for outmask, k in trans(c, inmask).items():
                ndp[outmask] = ndp.get(outmask, 0) + w * k
        dp = ndp
    return dp.get(0, 0)


# ---------------- planar faces + Kasteleyn solver ----------------

def faces_of(V, E):
    adj = {v: [] for v in V}
    for (a, b) in E:
        adj[a].append(b)
        adj[b].append(a)
    ang = {}
    for v in V:
        (r, c) = v
        for w in adj[v]:
            ang[(v, w)] = math.atan2(-(w[0] - r), w[1] - c)
    order = {v: sorted(adj[v], key=lambda w: ang[(v, w)]) for v in V}
    visited = set()
    faces = []
    for v in V:
        for w in adj[v]:
            if (v, w) in visited:
                continue
            cyc = [v]
            cv, cw = v, w
            while True:
                visited.add((cv, cw))
                cyc.append(cw)
                u, vv = cv, cw
                lst = order[vv]
                nxt = lst[(lst.index(u) - 1) % len(lst)]
                cv, cw = vv, nxt
                if (cv, cw) == (v, w):
                    break
            faces.append(cyc)
    return faces


def signed_area(cyc):
    a = 0
    for i in range(len(cyc) - 1):
        a += cyc[i][1] * (-cyc[i + 1][0]) - cyc[i + 1][1] * (-cyc[i][0])
    return a / 2


def kasteleyn_solve(V, E, faces):
    """Solve GF(2) system for Kasteleyn flips. Returns (x, outer_idx, areas).
    Raises AssertionError if inconsistent (never happens for these graphs)."""
    idx = {v: i for i, v in enumerate(V)}
    eindex = {e: i for i, e in enumerate(E)}

    def ekey(a, b):
        return (a, b) if (a, b) in eindex else (b, a)

    areas = [signed_area(f) for f in faces]
    outer = min(range(len(faces)), key=lambda i: areas[i])
    rows = []
    rhs = []
    for fi, f in enumerate(faces):
        if fi == outer:
            continue
        k = len(f) - 1
        agree = 0
        members = []
        for i in range(k):
            a, b = f[i], f[i + 1]
            members.append(eindex[ekey(a, b)])
            if idx[a] < idx[b]:
                agree += 1
        cw = agree if areas[fi] < 0 else (k - agree)
        rows.append(members)
        rhs.append((1 + cw) % 2)
    n = len(E)
    m = len(rows)
    eqs = []
    for row, b in zip(rows, rhs):
        mask = 0
        for j in row:
            mask ^= 1 << j
        eqs.append([mask, b])
    where = [-1] * n
    r_ = 0
    for c_ in range(n):
        sel = -1
        for i in range(r_, m):
            if (eqs[i][0] >> c_) & 1:
                sel = i
                break
        if sel < 0:
            continue
        eqs[r_], eqs[sel] = eqs[sel], eqs[r_]
        where[c_] = r_
        for i in range(m):
            if i != r_ and ((eqs[i][0] >> c_) & 1):
                eqs[i][0] ^= eqs[r_][0]
                eqs[i][1] ^= eqs[r_][1]
        r_ += 1
    for i in range(r_, m):
        assert not (eqs[i][0] == 0 and eqs[i][1] == 1), "Kasteleyn system inconsistent"
    return ([eqs[where[c_]][1] if where[c_] >= 0 else 0 for c_ in range(n)],
            outer, areas)


def verify_kasteleyn(V, E, faces, x, outer, areas):
    idx = {v: i for i, v in enumerate(V)}
    eindex = {e: i for i, e in enumerate(E)}

    def ekey(a, b):
        return (a, b) if (a, b) in eindex else (b, a)

    for fi, f in enumerate(faces):
        if fi == outer:
            continue
        k = len(f) - 1
        cw = 0
        for i in range(k):
            a, b = f[i], f[i + 1]
            j = eindex[ekey(a, b)]
            fwd = ((idx[a] < idx[b]) ^ (x[j] == 1))
            if areas[fi] < 0:
                cw += 1 if fwd else 0
            else:
                cw += 0 if fwd else 1
        assert cw % 2 == 1, f"face {fi} not Kasteleyn-odd (cw={cw})"
    return True


def audit_pattern_dir(a, b):
    """The fixed inherited orientation from the audit plan: horizontal right,
    vertical alternating by column. NOT always Kasteleyn after deletion."""
    if a[0] == b[0]:
        return a[1] < b[1]
    c = a[1]
    if c % 2 == 0:
        return a[0] > b[0]
    return a[0] < b[0]


def audit_pattern_odd(V, E, faces):
    eindex = {e: i for i, e in enumerate(E)}

    def ekey(a, b):
        return (a, b) if (a, b) in eindex else (b, a)

    areas = [signed_area(f) for f in faces]
    outer = min(range(len(faces)), key=lambda i: areas[i])
    bad = []
    for fi, f in enumerate(faces):
        if fi == outer:
            continue
        k = len(f) - 1
        cw = 0
        for i in range(k):
            a, b = f[i], f[i + 1]
            fwd = audit_pattern_dir(a, b)
            if areas[fi] < 0:
                cw += 1 if fwd else 0
            else:
                cw += 0 if fwd else 1
        if cw % 2 == 0:
            bad.append((fi, areas[fi], k, cw))
    return bad


def build_K(V, E, x):
    idx = {v: i for i, v in enumerate(V)}
    eindex = {e: i for i, e in enumerate(E)}
    n = len(V)
    K = [[0] * n for _ in range(n)]
    for e, j in eindex.items():
        a, b = e
        i1, i2 = idx[a], idx[b]
        lo, hi = (i1, i2) if i1 < i2 else (i2, i1)
        s = 1 if x[j] == 0 else -1
        K[lo][hi] = s
        K[hi][lo] = -s
    return K


# ---------------- exact determinant via CRT ----------------

def det_mod(K, p):
    n = len(K)
    A = np.array(K, dtype=np.int64) % np.int64(p)
    det = np.int64(1)
    for i in range(n):
        nz = np.flatnonzero(A[i:, i])
        if len(nz) == 0:
            return 0
        piv = nz[0] + i
        if piv != i:
            A[[i, piv]] = A[[piv, i]]
            det = (-det) % np.int64(p)
        aii = int(A[i, i])
        det = (det * np.int64(aii)) % np.int64(p)
        inv = pow(aii, p - 2, p)
        if i + 1 < n:
            below = np.flatnonzero(A[i + 1:, i])
            if len(below):
                rows = below + i + 1
                f = (A[rows, i].astype(np.int64) * np.int64(inv)) % np.int64(p)
                blk = (A[np.ix_(rows, range(i, n))].astype(np.int64)
                       - f[:, None] * A[i, i:].astype(np.int64)) % np.int64(p)
                A[np.ix_(rows, range(i, n))] = np.int64(blk)
    return int(det) % p


def det_crt(K):
    rems = [det_mod(K, p) for p in PRIMES]
    M = 1
    x = 0
    for r_, p in zip(rems, PRIMES):
        inv = pow(M, -1, p)
        t = ((r_ - x) * inv) % p
        x = x + M * t
        M *= p
    return x, rems


def pfaffian_count(V, E, faces):
    x, outer, areas = kasteleyn_solve(V, E, faces)
    verify_kasteleyn(V, E, faces, x, outer, areas)
    K = build_K(V, E, x)
    D, rems = det_crt(K)
    pf = math.isqrt(D)
    assert pf * pf == D, f"det not a perfect square: {D}"
    return pf, D, x, outer, areas


# ---------------- spanning trees (Matrix-Tree, auxiliary) ----------------

def ntrees(m, n):
    N_ = m * n

    def idx(r, c):
        return r * n + c

    L = [[0] * N_ for _ in range(N_)]
    for r in range(m):
        for c in range(n):
            i = idx(r, c)
            d = 0
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                rr, cc = r + dr, c + dc
                if 0 <= rr < m and 0 <= cc < n:
                    L[i][idx(rr, cc)] = -1
                    d += 1
            L[i][i] = d
    M = [row[:-1] for row in L[:-1]]
    rems = [det_mod(M, p) for p in PRIMES]
    Mp = 1
    x = 0
    for r_, p in zip(rems, PRIMES):
        inv = pow(Mp, -1, p)
        t = ((r_ - x) * inv) % p
        x = x + Mp * t
        Mp *= p
    return x


# ---------------- witness tilings + flip paths ----------------

def find_tiling(N, holes):
    blocked = set(holes)
    occ = [[False] * N for _ in range(R)]
    for (r, c) in blocked:
        occ[r][c] = True
    tiling = []

    def rec():
        for r in range(R):
            for c in range(N):
                if not occ[r][c]:
                    goto = (r, c)
                    break
            else:
                continue
            break
        else:
            return list(tiling)
        r, c = goto
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            rr, cc = r + dr, c + dc
            if 0 <= rr < R and 0 <= cc < N and not occ[rr][cc]:
                occ[r][c] = occ[rr][cc] = True
                tiling.append(tuple(sorted([(r, c), (rr, cc)])))
                s = rec()
                if s is not None:
                    return s
                tiling.pop()
                occ[r][c] = occ[rr][cc] = False
        return None

    return rec()


def validate_tiling(N, holes, tiling):
    blocked = set(holes)
    seen = set()
    for e in tiling:
        a, b = e
        for v in (a, b):
            if v in blocked:
                return False, "covers monomer"
            if v in seen:
                return False, "overlap"
            seen.add(v)
        if abs(a[0] - b[0]) + abs(a[1] - b[1]) != 1:
            return False, "nonedge"
    for r in range(R):
        for c in range(N):
            if (r, c) not in blocked and (r, c) not in seen:
                return False, "uncovered"
    if len(tiling) != (R * N - len(blocked)) // 2:
        return False, "wrong domino number"
    return True, "ok"


def unit_squares(N, holes):
    H = set(holes)
    sq = []
    for r in range(R - 1):
        for c in range(N - 1):
            vs = [(r, c), (r, c + 1), (r + 1, c), (r + 1, c + 1)]
            if any(v in H for v in vs):
                continue
            sq.append((r, c))
    return sq


def flip_step(N, holes, S):
    out = []
    for (r, c) in unit_squares(N, holes):
        v00, v01, v10, v11 = (r, c), (r, c + 1), (r + 1, c), (r + 1, c + 1)
        h1 = tuple(sorted([v00, v01]))
        h2 = tuple(sorted([v10, v11]))
        g1 = tuple(sorted([v00, v10]))
        g2 = tuple(sorted([v01, v11]))
        if h1 in S and h2 in S:
            out.append(((r, c, "h2v"), (S - {h1, h2}) | {g1, g2}))
        elif g1 in S and g2 in S:
            out.append(((r, c, "v2h"), (S - {g1, g2}) | {h1, h2}))
    return out


def witness_pair(N, holes):
    A = find_tiling(N, holes)
    assert A is not None, "no tiling found (Z>0 expected)"
    ok, msg = validate_tiling(N, holes, A)
    assert ok, msg
    SA = set(tuple(sorted(e)) for e in A)
    for (face, S2) in flip_step(N, holes, SA):
        B = sorted(S2)
        ok2, msg2 = validate_tiling(N, holes, B)
        assert ok2, msg2
        return sorted(SA), B, [face]
    raise AssertionError("no flippable square in witness tiling")


# ---------------- main census ----------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default=os.path.dirname(os.path.abspath(__file__)))
    args = ap.parse_args()
    outdir = args.outdir
    os.makedirs(outdir, exist_ok=True)
    t0 = time.time()
    rows = []
    summary = {"boards": [], "temperley": [], "parity": [], "audit_pattern_counterexample": None}
    total_pf_dp_agree = 0

    for N in NS:
        # pure baseline
        V0, E0 = build_graph(N, [])
        F0 = faces_of(V0, E0)
        pf0, D0, _, _, _ = pfaffian_count(V0, E0, F0)
        dp0 = count_dp(N, [])
        assert pf0 == dp0 and pf0 * pf0 == D0
        reps = orbit_reps(N)
        best = (0, None)
        norb = 0
        for (u, v) in reps:
            V, E = build_graph(N, [u, v])
            F = faces_of(V, E)
            pf, D, _, _, _ = pfaffian_count(V, E, F)
            dp = count_dp(N, [u, v])
            assert pf == dp, f"Pf/DP mismatch N={N} {(u, v)}: {pf} vs {dp}"
            total_pf_dp_agree += 1
            c = canon_pair(u, v, N)
            rows.append({
                "N": N,
                "u0": c[0][0], "u1": c[0][1],
                "v0": c[1][0], "v1": c[1][1],
                "stratum_u": stratum(c[0], N),
                "stratum_v": stratum(c[1], N),
                "Z": dp, "C_num": dp, "C_den": dp0,
                "C": dp / dp0,
            })
            norb += 1
            if dp > best[0]:
                best = (dp, (c[0], c[1]))
        # maximizers (ties)
        maxs = [r_ for r_ in rows if r_["N"] == N and r_["Z"] == best[0]]
        # witness for first maximizer
        mu, mv = best[1]
        A, B, faces = witness_pair(N, [mu, mv])
        summary["boards"].append({
            "N": N, "pure_Z": dp0, "norbits": norb,
            "max_Z": best[0], "max_pair": [list(mu), list(mv)],
            "max_C": best[0] / dp0, "n_maximizers": len(maxs),
            "witness_flip": [list(f_) for f_ in faces],
        })
        print(f"N={N}: pure={dp0} orbits={norb} maxZ={best[0]} at "
              f"{mu},{mv} C={best[0]/dp0:.6f} (ties={len(maxs)})", flush=True)

    # parity checks: single monomer -> 0; same-colour spot checks -> 0
    for (N, h) in [(6, [(0, 0)]), (6, [(2, 3)]), (10, [(0, 0)])]:
        z = count_dp(N, h)
        assert z == 0
        summary["parity"].append({"N": N, "holes": h, "Z": z})
        print(f"parity: 6x{N} minus {h}: Z=0 OK", flush=True)
    for (N, h) in [(6, [(0, 0), (1, 1)]), (6, [(0, 0), (5, 5)]), (10, [(2, 2), (3, 3)])]:
        z = count_dp(N, h)
        assert z == 0
        summary["parity"].append({"N": N, "holes": h, "Z": z})
        print(f"parity: 6x{N} minus {h} (same colour): Z=0 OK", flush=True)

    # audit-pattern failure demo (Lemma): fixed orientation not Kasteleyn here
    Vb, Eb = build_graph(6, [(1, 1), (4, 4)])
    bad = audit_pattern_odd(Vb, Eb, faces_of(Vb, Eb))
    assert len(bad) > 0, "expected audit-pattern counterexample"
    summary["audit_pattern_counterexample"] = {
        "N": 6, "holes": [[1, 1], [4, 4]],
        "even_faces": [[fi, ar, k, cw] for (fi, ar, k, cw) in bad],
    }
    print(f"lemma: audit fixed orientation fails on {len(bad)} hole-face(s) "
          f"for 6x6 minus (1,1),(4,4) -- per-graph solve required", flush=True)

    # Temperley cross-check on Temperleyan regions
    for (m, n) in [(2, 2), (2, 3), (3, 3)]:
        t = ntrees(m, n)
        d = temperley_dimers(m, n)
        assert t == d, f"Temperley mismatch {(m, n)}: {t} vs {d}"
        summary["temperley"].append({"m": m, "n": n, "trees": t, "dimers": d})
        print(f"temperley: trees({m}x{n})={t} == dimers({2*m-1}x{2*n-1} minus corner)={d} OK",
              flush=True)

    # witnesses file (coverings for max pairs)
    wit = {}
    for b in summary["boards"]:
        N = b["N"]
        mu = tuple(b["max_pair"][0])
        mv = tuple(b["max_pair"][1])
        A, B, faces = witness_pair(N, [mu, mv])
        wit[str(N)] = {"pair": b["max_pair"], "A": [list(e_) for e_ in A],
                       "B": [list(e_) for e_ in B],
                       "flip": [list(f_) for f_ in faces]}
    with open(os.path.join(outdir, "witnesses.json"), "w") as f:
        json.dump(wit, f)

    with open(os.path.join(outdir, "census.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["N", "u_r", "u_c", "v_r", "v_c", "stratum_u", "stratum_v",
                    "Z", "C_num", "C_den", "C_float"])
        for r_ in rows:
            w.writerow([r_["N"], r_["u0"], r_["u1"], r_["v0"], r_["v1"],
                        r_["stratum_u"], r_["stratum_v"], r_["Z"],
                        r_["C_num"], r_["C_den"], f"{r_['C']:.12f}"])
    summary.update({"total_orbits": len(rows),
                    "pf_dp_agreements": total_pf_dp_agree,
                    "seconds": round(time.time() - t0, 2)})
    with open(os.path.join(outdir, "summary.json"), "w") as f:
        json.dump(summary, f, indent=1)
    print(f"WROTE {len(rows)} orbit rows; Pf==DP on {total_pf_dp_agree}/{len(rows)}; "
          f"{summary['seconds']}s", flush=True)


def temperley_dimers(m, n):
    """Dimers of (2m-1)x(2n-1) board minus corner (0,0), by profile DP."""
    RR, NN = 2 * m - 1, 2 * n - 1
    blocked = {(0, 0)}

    def trans(col, inmask):
        occ = [False] * RR
        for r in range(RR):
            if (r, col) in blocked:
                if (inmask >> r) & 1:
                    return {}
                occ[r] = True
            elif (inmask >> r) & 1:
                occ[r] = True
        res = {}

        def dfs(r, outmask):
            while r < RR and occ[r]:
                r += 1
            if r == RR:
                res[outmask] = res.get(outmask, 0) + 1
                return
            if r + 1 < RR and not occ[r + 1]:
                occ[r] = occ[r + 1] = True
                dfs(r + 1, outmask)
                occ[r] = occ[r + 1] = False
            if col + 1 < NN and (r, col + 1) not in blocked:
                occ[r] = True
                dfs(r + 1, outmask | (1 << r))
                occ[r] = False

        dfs(0, 0)
        return res

    dp = {0: 1}
    for c in range(NN):
        ndp = {}
        for inmask, w in dp.items():
            for outmask, k in trans(c, inmask).items():
                ndp[outmask] = ndp.get(outmask, 0) + w * k
        dp = ndp
    return dp.get(0, 0)


if __name__ == "__main__":
    main()
