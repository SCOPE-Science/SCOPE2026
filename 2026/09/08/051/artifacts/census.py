"""Exhaustive Walsh-Hadamard census:
  (a) all 2^16 Boolean functions in n=4,
  (b) all 256 rotation-symmetric Boolean functions (RSBF) in n=5 (8 rotation orbits).
Exact integer arithmetic only (stdlib). Emits joint (nl x resiliency) CSVs,
orbit list, certified witnesses, and a run log with SHA-256 hashes.
"""
import csv, hashlib, itertools, json, os

HERE = os.path.dirname(os.path.abspath(__file__))

def fwht(a):
    h = list(a)
    step = 1
    n = len(h)
    while step < n:
        for i in range(0, n, 2 * step):
            for j in range(i, i + step):
                u, v = h[j], h[j + step]
                h[j], h[j + step] = u + v, u - v
        step *= 2
    return h

def popcount(i):
    return bin(i).count("1")

def walsh_stats(tt, n):
    N = 1 << n
    a = [1 if ((tt >> i) & 1) == 0 else -1 for i in range(N)]
    W = fwht(a)
    assert sum(w * w for w in W) == (1 << (2 * n))
    m = max(abs(w) for w in W)
    assert m % 2 == 0
    nl = (1 << (n - 1)) - m // 2
    balanced = (W[0] == 0)
    if not balanced:
        res = -1
    else:
        res = 0
        for mm in range(1, n + 1):
            if all(W[u] == 0 for u in range(N) if 1 <= popcount(u) <= mm):
                res = mm
            else:
                break
    return W, m, nl, balanced, res

def resiliency_direct(tt, n):
    """Independent definition: f balanced and every subfunction obtained by
    fixing r (1<=r<=m) coordinates is balanced. Returns -1 if unbalanced."""
    N = 1 << n
    bits = [(tt >> i) & 1 for i in range(N)]
    if sum(bits) != (1 << (n - 1)):
        return -1
    best = 0
    for m in range(1, n):
        ok = True
        for r in range(1, m + 1):
            for S in itertools.combinations(range(n), r):
                for fix in range(1 << r):
                    c = 0
                    for x in range(N):
                        match = True
                        for k, s in enumerate(S):
                            if ((x >> s) & 1) != ((fix >> k) & 1):
                                match = False
                                break
                        if match:
                            c += bits[x]
                    if c != (1 << (n - r - 1)):
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                break
        if ok:
            best = m
        else:
            break
    return best

def anf_degree(tt, n):
    N = 1 << n
    g = [(tt >> i) & 1 for i in range(N)]
    for j in range(n):
        for i in range(N):
            if (i >> j) & 1:
                g[i] ^= g[i ^ (1 << j)]
    return max([popcount(u) for u in range(N) if g[u]] + [0])

def rot5(i):
    b = [(i >> j) & 1 for j in range(5)]
    r = 0
    for j in range(5):
        r |= (b[(j + 1) % 5] << j)
    return r

def rotation_orbits_n5():
    seen = [False] * 32
    orbits = []
    for i in range(32):
        if not seen[i]:
            cur, s = i, set()
            for _ in range(5):
                s.add(cur)
                cur = rot5(cur)
            orb = sorted(s)
            for k in orb:
                seen[k] = True
            orbits.append(orb)
    orbits.sort(key=lambda o: (len(o), o))
    return orbits

def main():
    # ---- n = 4 full census ----
    n4, N4 = 4, 16
    hist4 = {}
    for tt in range(1 << N4):
        _, _, nl, _, res = walsh_stats(tt, n4)
        key = (nl, res)
        hist4[key] = hist4.get(key, 0) + 1
    assert sum(hist4.values()) == 65536
    # independent fixing-definition cross-check over all of n=4
    for tt in range(1 << N4):
        if resiliency_direct(tt, n4) != walsh_stats(tt, n4)[4]:
            raise AssertionError(f"n=4 resiliency mismatch at tt={tt}")

    # ---- RSBF n = 5 census ----
    n5 = 5
    orbits = rotation_orbits_n5()
    assert len(orbits) == 8 and sum(len(o) for o in orbits) == 32
    hist5 = {}
    for mask in range(1 << len(orbits)):
        tt = 0
        for j, o in enumerate(orbits):
            if (mask >> j) & 1:
                for x in o:
                    tt |= (1 << x)
        _, _, nl, _, res = walsh_stats(tt, n5)
        key = (nl, res)
        hist5[key] = hist5.get(key, 0) + 1
    assert sum(hist5.values()) == 256
    for mask in range(1 << len(orbits)):
        tt = 0
        for j, o in enumerate(orbits):
            if (mask >> j) & 1:
                for x in o:
                    tt |= (1 << x)
        if resiliency_direct(tt, n5) != walsh_stats(tt, n5)[4]:
            raise AssertionError(f"RSBF n=5 resiliency mismatch at mask={mask}")

    # ---- witnesses ----
    # bent n=4: Maiorana-McFarland x0x1+x2x3 (unbalanced, as all bent functions are)
    tt_bent = 0
    for i in range(N4):
        x = [(i >> j) & 1 for j in range(4)]
        if (x[0] & x[1]) ^ (x[2] & x[3]):
            tt_bent |= (1 << i)
    Wb, mb, nlb, balb, resb = walsh_stats(tt_bent, n4)
    assert nlb == 6 and all(abs(w) == 4 for w in Wb)

    # RSBF n=5 slice maximum + lex-first balanced witness at the maximum
    maxnl = max(nl for (nl, _) in hist5)
    bal_cands, unbal_cands = [], []
    for mask in range(1 << len(orbits)):
        tt = 0
        for j, o in enumerate(orbits):
            if (mask >> j) & 1:
                for x in o:
                    tt |= (1 << x)
        W, m, nl, bal, res = walsh_stats(tt, n5)
        if nl == maxnl:
            (bal_cands if bal else unbal_cands).append((mask, tt, W, m, res))
    bal_cands.sort()
    unbal_cands.sort()
    assert bal_cands, "no balanced RSBF at slice maximum"
    bmask, btt, bW, bm, bres = bal_cands[0]
    umask, utt = unbal_cands[0][0], unbal_cands[0][1]

    # ---- write artifacts ----
    def write_joint(path, hist):
        with open(path, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["nl", "resiliency", "count"])
            for (nl, res) in sorted(hist):
                w.writerow([nl, res, hist[(nl, res)]])

    p4 = os.path.join(HERE, "n4_joint.csv")
    p5 = os.path.join(HERE, "rsbf5_joint.csv")
    porb = os.path.join(HERE, "rsbf5_orbits.csv")
    pwit = os.path.join(HERE, "witnesses.json")
    plog = os.path.join(HERE, "run_log.json")
    write_joint(p4, hist4)
    write_joint(p5, hist5)
    with open(porb, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["orbit_index", "size", "representative", "members"])
        for j, o in enumerate(orbits):
            w.writerow([j, len(o), o[0], ";".join(map(str, o))])
    witnesses = {
        "bent_n4": {"anf": "x0*x1+x2*x3", "truth": tt_bent, "n": 4,
                    "max_abs_W": mb, "nl": nlb, "balanced": balb,
                    "resiliency": resb, "anf_degree": anf_degree(tt_bent, n4),
                    "spectrum": Wb, "parseval": sum(v * v for v in Wb)},
        "rsbf5_balanced_max": {"orbit_mask": bmask, "truth": btt, "n": 5,
                    "max_abs_W": bm, "nl": maxnl, "balanced": True,
                    "resiliency": bres, "anf_degree": anf_degree(btt, n5),
                    "spectrum": bW, "parseval": sum(v * v for v in bW)},
        "rsbf5_unbalanced_max": {"orbit_mask": umask, "truth": utt, "n": 5,
                    "nl": maxnl},
        "rsbf5_slice_max_nl": maxnl,
        "rsbf5_num_at_max": sum(c for (nl, _), c in hist5.items() if nl == maxnl),
        "rsbf5_num_balanced_at_max": len(bal_cands),
    }
    with open(pwit, "w") as f:
        json.dump(witnesses, f, indent=2)

    def sha(p):
        with open(p, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

    log = {
        "n4_total": sum(hist4.values()),
        "n4_bent_count": sum(c for (nl, _), c in hist4.items() if nl == 6),
        "n4_nl_marginal": {str(nl): sum(c for (n, _), c in hist4.items() if n == nl)
                           for nl in sorted({n for (n, _) in hist4})},
        "n4_res_marginal": {str(r): sum(c for (_, rr), c in hist4.items() if rr == r)
                            for r in sorted({rr for (_, rr) in hist4})},
        "n4_resiliency_crosscheck": "all 65536 agree (Walsh-zero vs fixing definition)",
        "rsbf5_total": sum(hist5.values()),
        "rsbf5_nl_marginal": {str(nl): sum(c for (n, _), c in hist5.items() if n == nl)
                              for nl in sorted({n for (n, _) in hist5})},
        "rsbf5_res_marginal": {str(r): sum(c for (_, rr), c in hist5.items() if rr == r)
                               for r in sorted({rr for (_, rr) in hist5})},
        "rsbf5_resiliency_crosscheck": "all 256 agree (Walsh-zero vs fixing definition)",
        "covering_radius_RM14": 6,
        "sha256": {os.path.basename(p): sha(p) for p in (p4, p5, porb, pwit)},
    }
    with open(plog, "w") as f:
        json.dump(log, f, indent=2)
    print(json.dumps({k: v for k, v in log.items() if k != "sha256"}, indent=2))
    print("SHA256:", json.dumps(log["sha256"], indent=2))

if __name__ == "__main__":
    main()
