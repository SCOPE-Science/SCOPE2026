# Census of order-8 Latin squares with diagonal order-7 autotopism.
# Symbols 0..6, 7=infty. sigma=(0 1 2 3 4 5 6) fixes 7. Theta=(sigma,sigma,sigma).
# Deterministic: no RNG. Run: python3 census.py  (writes census.json beside itself)
import json, os, time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))

def add(x, k):
    return 7 if x == 7 else (x + k) % 7

def enumerate_theta_invariant():
    """DFS over diagonal parameters. Returns (sols, nodes, elapsed).
    sols = list of (r, c, s) with r=L(7,0), c=L(0,7), s[d]=L(0,d).
    Lemma (used): r,c != 7, else row 7 / col 7 would be constant 7."""
    sols = []
    nodes = [0]
    def full_ok(s, r, c):
        for k in range(7):
            if len(set([add(s[d], k) for d in range(7)] + [add(c, k)])) != 8:
                return False
        for j in range(7):
            if len(set([add(s[(j - i) % 7], i) for i in range(7)] + [add(r, j)])) != 8:
                return False
        return True
    t0 = time.time()
    for r in range(7):
        for c in range(7):
            s = [-1] * 7
            def rec(d):
                nodes[0] += 1
                if d == 7:
                    if full_ok(s, r, c):
                        sols.append((r, c, tuple(s)))
                    return
                for v in range(8):
                    if v in s[:d]:
                        continue
                    if v == c:
                        continue
                    bd = 7 if v == 7 else (v - d) % 7
                    ok = True
                    for j in range(d):
                        bj = 7 if s[j] == 7 else (s[j] - j) % 7
                        if bj == bd:
                            ok = False
                            break
                    if not ok:
                        continue
                    s[d] = v
                    rec(d + 1)
                    s[d] = -1
            rec(0)
    return sols, nodes[0], time.time() - t0

def build(r, c, s):
    L = [[0] * 8 for _ in range(8)]
    for d in range(7):
        for k in range(7):
            L[k][(k + d) % 7] = add(s[d], k)
    for k in range(7):
        L[k][7] = add(c, k)
        L[7][k] = add(r, k)
    L[7][7] = 7
    return tuple(tuple(row) for row in L)

def is_latin(L):
    for i in range(8):
        if len(set(L[i])) != 8:
            return False
    for j in range(8):
        if len(set(L[i][j] for i in range(8))) != 8:
            return False
    return True

def is_theta_invariant(L):
    for i in range(8):
        for j in range(8):
            ii = 7 if i == 7 else (i + 1) % 7
            jj = 7 if j == 7 else (j + 1) % 7
            if L[ii][jj] != (7 if L[i][j] == 7 else (L[i][j] + 1) % 7):
                return False
    return True

def intercalates(L):
    n = 0
    for i1 in range(8):
        for i2 in range(i1 + 1, 8):
            for j1 in range(8):
                for j2 in range(j1 + 1, 8):
                    a, b = L[i1][j1], L[i1][j2]
                    cc, d = L[i2][j1], L[i2][j2]
                    if a == d and b == cc and a != b:
                        n += 1
    return n

def decide_wit(A, B):
    """Exhaustive isotopy decider. Returns (iso_bool, (a,b,g) or None, nodes)."""
    L1 = [list(r) for r in A]
    L2 = [list(r) for r in B]
    a = [-1] * 8
    b = [-1] * 8
    nodes = [0]
    wit = [None]
    def consistent(na, nb):
        gg = [-1] * 8
        ggi = [-1] * 8
        for i in range(na):
            if a[i] < 0:
                continue
            for j in range(nb):
                if b[j] < 0:
                    continue
                s1, s2 = L1[i][j], L2[a[i]][b[j]]
                if gg[s1] == -1 and ggi[s2] == -1:
                    gg[s1] = s2
                    ggi[s2] = s1
                elif gg[s1] != s2:
                    return False
        return True
    def rec(na, nb):
        nodes[0] += 1
        if na == 8 and nb == 8:
            g = [-1] * 8
            for i in range(8):
                for j in range(8):
                    g[L1[i][j]] = L2[a[i]][b[j]]
            wit[0] = (tuple(a), tuple(b), tuple(g))
            return True
        if na <= nb:
            i = na
            for r in range(8):
                if r in a[:na]:
                    continue
                a[i] = r
                if consistent(na + 1, nb) and rec(na + 1, nb):
                    return True
                a[i] = -1
            return False
        j = nb
        for cc in range(8):
            if cc in b[:nb]:
                continue
            b[j] = cc
            if consistent(na, nb + 1) and rec(na, nb + 1):
                return True
            b[j] = -1
        return False
    return rec(0, 0), wit[0], nodes[0]

def autotopisms(A, cap_order7=4):
    """Enumerate all autotopisms; return (total, list_of_order7 up to cap)."""
    L = [list(r) for r in A]
    a = [-1] * 8
    b = [-1] * 8
    total = [0]
    ord7 = []
    def consistent(na, nb):
        gg = [-1] * 8
        ggi = [-1] * 8
        for i in range(na):
            if a[i] < 0:
                continue
            for j in range(nb):
                if b[j] < 0:
                    continue
                s1, s2 = L[i][j], L[a[i]][b[j]]
                if gg[s1] == -1 and ggi[s2] == -1:
                    gg[s1] = s2
                    ggi[s2] = s1
                elif gg[s1] != s2:
                    return False
        return True
    def porder(p):
        from math import gcd
        vis = [0] * 8
        o = 1
        for i in range(8):
            if not vis[i]:
                q, n = i, 0
                while not vis[q]:
                    vis[q] = 1
                    q = p[q]
                    n += 1
                o = o * n // gcd(o, n)
        return o
    def rec(na, nb):
        if na == 8 and nb == 8:
            total[0] += 1
            g = [-1] * 8
            for i in range(8):
                for j in range(8):
                    g[L[i][j]] = L[a[i]][b[j]]
            from math import gcd
            o = 1
            for p in (tuple(a), tuple(b), tuple(g)):
                o = o * porder(p) // gcd(o, porder(p))
            if o == 7 and len(ord7) < cap_order7:
                ord7.append((tuple(a), tuple(b), tuple(g)))
            return
        if na <= nb:
            i = na
            for r in range(8):
                if r in a[:na]:
                    continue
                a[i] = r
                if consistent(na + 1, nb):
                    rec(na + 1, nb)
                a[i] = -1
        else:
            j = nb
            for cc in range(8):
                if cc in b[:nb]:
                    continue
                b[j] = cc
                if consistent(na, nb + 1):
                    rec(na, nb + 1)
                b[j] = -1
    rec(0, 0)
    return total[0], ord7

def reduced(L):
    L = [list(r) for r in L]
    g = [0] * 8
    for j in range(8):
        g[L[0][j]] = j
    ar = [g[L[i][0]] for i in range(8)]
    ai = [0] * 8
    for i in range(8):
        ai[ar[i]] = i
    return [[g[L[ai[i]][j]] for j in range(8)] for i in range(8)]

def main():
    t_all = time.time()
    sols, nodes, t_enum = enumerate_theta_invariant()
    M = len(sols)
    sqs = [build(r, c, s) for (r, c, s) in sols]
    for L in sqs:
        assert is_latin(L) and is_theta_invariant(L)
    # bucket by intercalate number, classify by exhaustive isotopy search
    buckets = {}
    for i, L in enumerate(sqs):
        buckets.setdefault(intercalates(L), []).append(i)
    cls_of = {}
    rep_wit = {}  # member idx -> (rep idx, a, b, g)
    reps = []
    for key in sorted(buckets):
        rlist = []
        for i in buckets[key]:
            hit = None
            for r in rlist:
                ok, w, _ = decide_wit(sqs[i], sqs[r])
                if ok:
                    hit = (r, w)
                    break
            if hit is None:
                rlist.append(i)
                reps.append(i)
                rep_wit[i] = (i, tuple(range(8)), tuple(range(8)), tuple(range(8)))
            else:
                rep_wit[i] = (hit[0],) + hit[1]
            cls_of[i] = rep_wit[i][0]
    N7 = len(reps)
    # re-verify every stored witness by direct substitution
    for i, (r, a, b, g) in rep_wit.items():
        A, B = sqs[i], sqs[r]
        for x in range(8):
            for y in range(8):
                assert B[a[x]][b[y]] == g[A[x][y]], (i, r)
    # rep pairs pairwise non-isotopic (fresh searches)
    noniso_nodes = {}
    R = sorted(reps)
    for x in range(len(R)):
        for y in range(x + 1, len(R)):
            ok, _, n = decide_wit(sqs[R[x]], sqs[R[y]])
            assert not ok, (R[x], R[y])
            noniso_nodes[f"{R[x]}-{R[y]}"] = n
    # autotopism data per rep
    rep_info = []
    for r in R:
        tot, o7 = autotopisms(sqs[r])
        assert len(o7) > 0
        o7w = o7[0]
        # verify witness directly
        A = sqs[r]
        for x in range(8):
            for y in range(8):
                assert A[o7w[0][x]][o7w[1][y]] == o7w[2][A[x][y]]
        rep_info.append({
            "rep_index": r,
            "param": {"r": sols[r][0], "c": sols[r][1], "s": list(sols[r][2])},
            "class_size_in_M": sum(1 for v in cls_of.values() if v == r),
            "intercalates": intercalates(sqs[r]),
            "autotopism_order": tot,
            "n_order7_autotopisms": len(o7),
            "order7_witness": [list(o7w[0]), list(o7w[1]), list(o7w[2])],
            "reduced": reduced(sqs[r]),
            "theta_invariant_square": [list(row) for row in sqs[r]],
        })
    # centralizer C(sigma)^3 orbits on M
    idx = {s: i for i, s in enumerate(sqs)}
    def cact(L, u, v, w):
        return tuple(tuple((7 if L[7 if i == 7 else (i - u) % 7][7 if j == 7 else (j - v) % 7] == 7
                            else (L[7 if i == 7 else (i - u) % 7][7 if j == 7 else (j - v) % 7] + w) % 7)
                           for j in range(8)) for i in range(8))
    seen = [False] * M
    corbs = []
    for i, L in enumerate(sqs):
        if seen[i]:
            continue
        orb = set()
        for u in range(7):
            for v in range(7):
                for w in range(7):
                    orb.add(idx[cact(L, u, v, w)])
        for j in orb:
            seen[j] = True
        corbs.append(sorted(orb))
    data = {
        "meta": {"deterministic": True, "rng_seed": None,
                 "M": M, "enum_nodes": nodes, "enum_seconds": round(t_enum, 3),
                 "N7": N7, "total_seconds": round(time.time() - t_all, 1)},
        "params_all": [[r, c] + list(s) for (r, c, s) in sols],
        "reps": rep_info,
        "witnesses_member_to_rep": {str(i): [r, list(a), list(b), list(g)]
                                    for i, (r, a, b, g) in rep_wit.items()},
        "rep_pair_nonisotopy_nodes": noniso_nodes,
        "centralizer": {"K": len(corbs),
                        "orbit_sizes": sorted([len(o) for o in corbs]),
                        "class_of_each_orbit": [sorted(set(cls_of[j] for j in o)) for o in corbs]},
        "class_sizes": {str(r): sum(1 for v in cls_of.values() if v == r) for r in R},
    }
    with open(os.path.join(HERE, "census.json"), "w") as f:
        json.dump(data, f, indent=1)
    print("M=%d N7=%d K=%d nodes=%d t_enum=%.2fs t_all=%.1fs" %
          (M, N7, len(corbs), nodes, t_enum, time.time() - t_all))
    print("class_sizes:", data["class_sizes"])

if __name__ == "__main__":
    main()
