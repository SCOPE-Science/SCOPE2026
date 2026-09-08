#!/usr/bin/env python3
"""Hochster-based verification of reg(S/I) for open ladders L_n and auxiliary
pendant ladders M_n, plus induced-matching numbers and deletion isomorphisms.

Method: Hochster's formula for edge ideals:
  reg(S/I(G)) = max over W subset V of (k(W)+1),
where k(W) = max{k : reduced H_k(Ind(G[W]); F_p) != 0}
(Ind = independence complex; W=empty contributes 0).
Homology of each independence complex is computed from its simplicial chain
complex over F_p, for p in {2, 7919, 32003} (characteristic-independence check).

Also brute-forces induced matching numbers nu(G) with explicit matchings, and
checks the four deletion isomorphisms used in the induction step of the proof.
"""
import json
import time

PRIMES = [2, 7919, 32003]

# ---------------------------------------------------------------- graphs

def ladder(n):
    """Open ladder L_n. 0-based: a(i)=i, b(i)=n+i."""
    N = 2 * n
    edges = [(i, n + i) for i in range(n)]
    edges += [(i, i + 1) for i in range(n - 1)]
    edges += [(n + i, n + i + 1) for i in range(n - 1)]
    return N, edges


def pendant(n):
    """M_n = L_n plus pendant vertex c adjacent to b_{n-1} (0-based)."""
    N, edges = ladder(n)
    c = N
    edges = list(edges) + [(2 * n - 1, c)]
    return N + 1, edges


def prism(n):
    """Closed ladder (prism) Y_n = C_n box K_2."""
    N, edges = ladder(n)
    edges = list(edges) + [(0, n - 1), (n, 2 * n - 1)]
    return N, edges


def mobius(n):
    """Twist-closed ladder: ladder plus cross edges a_0-b_{n-1}, b_0-a_{n-1}."""
    N, edges = ladder(n)
    edges = list(edges) + [(0, 2 * n - 1), (n, n - 1)]
    return N, edges


def neighbor_masks(N, edges):
    nmask = [0] * N
    for u, v in edges:
        nmask[u] |= 1 << v
        nmask[v] |= 1 << u
    return nmask


def induced_subgraph(N, edges, dead):
    dead = set(dead)
    mp = {}
    for v in range(N):
        if v not in dead:
            mp[v] = len(mp)
    e2 = []
    for u, v in edges:
        if u not in dead and v not in dead:
            e2.append((mp[u], mp[v]))
    return len(mp), e2


def check_iso(N1, e1, N2, e2, mp):
    """mp: dict keys = 0..N1-1 target ids (post-renumbering), values 0..N2-1."""
    assert N1 == N2, (N1, N2)
    assert sorted(mp.keys()) == list(range(N1))
    assert sorted(mp.values()) == list(range(N2))
    s1 = set()
    for u, v in e1:
        s1.add((mp[u], mp[v]))
    s2 = set()
    for u, v in e2:
        s2.add((min(u, v), max(u, v)))
    s1n = set((min(a, b), max(a, b)) for a, b in s1)
    assert s1n == s2, (s1n, s2)


def iso_map_in_subgraph(N, edges, dead, target_of_survivor):
    """Build renumbered (0..N1-1) map from survivor->target, survivors sorted."""
    surv = sorted(v for v in range(N) if v not in set(dead))
    mp = {i: target_of_survivor[v] for i, v in enumerate(surv)}
    return mp

# ------------------------------------------------------- induced matchings

def induced_matching_number(N, edges):
    adj = [[False] * N for _ in range(N)]
    for u, v in edges:
        adj[u][v] = adj[v][u] = True
    m = len(edges)
    best = 0
    bestset = []
    for mask in range(1 << m):
        idx = [i for i in range(m) if (mask >> i) & 1]
        if len(idx) <= best:
            continue
        used = set()
        ok = True
        for i in idx:
            u, v = edges[i]
            if u in used or v in used:
                ok = False
                break
            used.add(u)
            used.add(v)
        if not ok:
            continue
        for x in range(len(idx)):
            for y in range(x + 1, len(idx)):
                u, v = edges[idx[x]]
                w, z = edges[idx[y]]
                if adj[u][w] or adj[u][z] or adj[v][w] or adj[v][z]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            best = len(idx)
            bestset = [edges[i] for i in idx]
    return best, bestset

# ------------------------------------------------------------- homology

def rank_mod(mat, p):
    M = [[x % p for x in row] for row in mat]
    nrows = len(M)
    if nrows == 0:
        return 0
    ncols = len(M[0])
    if ncols == 0:
        return 0
    r = 0
    for c in range(ncols):
        piv = -1
        for i in range(r, nrows):
            if M[i][c] % p != 0:
                piv = i
                break
        if piv < 0:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], -1, p)
        if inv != 1:
            M[r] = [(x * inv) % p for x in M[r]]
        for i in range(nrows):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        r += 1
        if r == nrows:
            break
    return r


def hom_dims_of_W(W, nmask, N, p):
    """Reduced homology dims {k: dim} of Ind(G[W]) over F_p. W != empty."""
    # Simplex check (correct direction): W with no edges -> full simplex.
    m = W
    simplex = True
    while m:
        l = m & (-m)
        v = l.bit_length() - 1
        if nmask[v] & W:
            simplex = False
            break
        m ^= l
    if simplex:
        return {}
    bysize = {}
    stack = [(W, 0)]
    while stack:
        cand, chosen = stack.pop()
        if cand == 0:
            continue
        lsb = cand & (-cand)
        v = lsb.bit_length() - 1
        rest = cand ^ (1 << v)
        nc = chosen | (1 << v)
        bysize.setdefault(bin(nc).count("1"), []).append(nc)
        stack.append((rest & ~nmask[v], nc))
        stack.append((rest, chosen))
    sizes = sorted(bysize)
    nlev = {s: len(bysize[s]) for s in sizes}
    # R[k] = rank of d_k : C_k -> C_{k-1} (C_k spanned by (k+1)-sets);
    # R[0] = rank of augmented d_0 (all-ones row) = 1 since W nonempty.
    R = {0: 1}
    for d in range(1, max(sizes)):
        rows = bysize.get(d, [])
        cols = bysize.get(d + 1, [])
        if not rows or not cols:
            R[d] = 0
            continue
        ridx = {f: i for i, f in enumerate(rows)}
        mat = [[0] * len(cols) for _ in range(len(rows))]
        for j, F in enumerate(cols):
            m = F
            while m:
                l = m & (-m)
                G = F ^ l
                s = bin(F & (l - 1)).count("1")
                mat[ridx[G]][j] = (mat[ridx[G]][j] + (1 if s % 2 == 0 else p - 1)) % p
                m ^= l
        R[d] = rank_mod(mat, p)
    out = {}
    for s in sizes:
        k = s - 1  # reduced H_k from C_k level: dim ker(d_k) - rank(d_{k+1})
        h = nlev[s] - R.get(k, 0) - R.get(k + 1, 0)
        assert h >= 0, (W, s, nlev, R)
        if h:
            out[k] = h
    return out


def reg_bruteforce(N, edges, p):
    nmask = neighbor_masks(N, edges)
    best = 0
    wit = None
    for W in range(1, 1 << N):
        # skip independent W (simplex: no reduced homology)
        m = W
        has = False
        while m:
            l = m & (-m)
            v = l.bit_length() - 1
            if nmask[v] & W:
                has = True
                break
            m ^= l
        if not has:
            continue
        dims = hom_dims_of_W(W, nmask, N, p)
        for k, d in dims.items():
            if k + 1 > best:
                best = k + 1
                wit = {"W": [i for i in range(N) if (W >> i) & 1], "k": k, "dim": d}
    return best, wit


def extremal_check(N, edges, p, Wlist):
    """Homology of Ind(G[W]) for the odd-rung witness set."""
    W = 0
    for v in Wlist:
        W |= 1 << v
    nmask = neighbor_masks(N, edges)
    return hom_dims_of_W(W, nmask, N, p)


def odd_rungs(n):
    W = []
    for i in range(0, n, 2):
        W += [i, n + i]
    return W

# ------------------------------------------------------------------- main

def main():
    t0 = time.time()
    res = {"primes": PRIMES, "ladders": {}, "pendants": {},
           "twists": {}, "iso_checks": [], "extremal": {}}
    for n in range(1, 7):
        N, edges = ladder(n)
        nu, match = induced_matching_number(N, edges)
        entry = {"vertices": N, "edges": len(edges), "nu": nu,
                 "induced_matching": [sorted(e) for e in match], "reg": {}}
        for p in PRIMES:
            r, wit = reg_bruteforce(N, edges, p)
            entry["reg"][str(p)] = {"value": r, "witness": wit}
        res["ladders"][str(n)] = entry
        print(f"L_{n}: nu={nu} regs=" +
              ",".join(f"{p}:{entry['reg'][str(p)]['value']}" for p in PRIMES),
              flush=True)
    for n in range(1, 7):
        N, edges = pendant(n)
        nu, match = induced_matching_number(N, edges)
        entry = {"vertices": N, "edges": len(edges), "nu": nu,
                 "induced_matching": [sorted(e) for e in match], "reg": {}}
        for p in PRIMES:
            r, wit = reg_bruteforce(N, edges, p)
            entry["reg"][str(p)] = {"value": r, "witness": wit}
        res["pendants"][str(n)] = entry
        print(f"M_{n}: nu={nu} regs=" +
              ",".join(f"{p}:{entry['reg'][str(p)]['value']}" for p in PRIMES),
              flush=True)
    # extremal homology on odd-rung sets
    for n in range(1, 7):
        N, edges = ladder(n)
        W = odd_rungs(n)
        dd = {str(p): extremal_check(N, edges, p, W) for p in PRIMES}
        res["extremal"][str(n)] = {"W": W, "hom": dd}
        print(f"extremal L_{n} W={W} hom={dd}", flush=True)
    # twist remark: prism vs mobius for n=3,4
    for n in (3, 4):
        for name, fn in (("prism", prism), ("mobius", mobius)):
            N, edges = fn(n)
            nu, _ = induced_matching_number(N, edges)
            rr = {}
            for p in PRIMES:
                r, wit = reg_bruteforce(N, edges, p)
                rr[str(p)] = {"value": r, "witness": wit}
            res["twists"][f"{name}_{n}"] = {"vertices": N, "nu": nu, "reg": rr}
            print(f"{name}_{n}: nu={nu} regs=" +
                  ",".join(f"{p}:{rr[str(p)]['value']}" for p in PRIMES), flush=True)
    # deletion isomorphisms for the induction step (n=4 representative + n=3)
    for n in (3, 4, 5):
        N, e = ladder(n)
        # (i) L_n - a_{n-1} ≅ M_{n-1}: a_i->a'_i, b_i->b'_i (i<n-1), b_{n-1}->c'
        surv = [v for v in range(N) if v != n - 1]
        tgt = {}
        for i in range(n - 1):
            tgt[i] = i
            tgt[n + i] = (n - 1) + i
        tgt[2 * n - 1] = 2 * (n - 1)
        N1, e1 = induced_subgraph(N, e, [n - 1])
        N2, e2 = pendant(n - 1)
        check_iso(N1, e1, N2, e2,
                  iso_map_in_subgraph(N, e, [n - 1], tgt))
        res["iso_checks"].append(f"L_{n}-a_{n-1} = M_{n-1} ok")
        # (ii) L_n - N[a_{n-1}] ≅ M_{n-2}, b_{n-2} -> c'
        tgt = {}
        for i in range(n - 2):
            tgt[i] = i
            tgt[n + i] = (n - 2) + i
        tgt[2 * n - 2] = 2 * (n - 2)
        N1, e1 = induced_subgraph(N, e, [n - 1, n - 2, 2 * n - 1])
        N2, e2 = pendant(n - 2)
        check_iso(N1, e1, N2, e2,
                  iso_map_in_subgraph(N, e, [n - 1, n - 2, 2 * n - 1], tgt))
        res["iso_checks"].append(f"L_{n}-N[a] = M_{n-2} ok")
        # (iii) M_n - b_{n-1} ≅ M_{n-1} + isolate (swap a<->b, a_{n-1}->c', c->d)
        Nm, em = pendant(n)
        tgt = {}
        for i in range(n - 1):
            tgt[i] = (n - 1) + i     # a_i -> b'_i
            tgt[n + i] = i           # b_i -> a'_i
        tgt[n - 1] = 2 * (n - 1)       # a_{n-1} -> c'
        tgt[2 * n] = 2 * (n - 1) + 1   # c -> d (isolate)
        N1, e1 = induced_subgraph(Nm, em, [2 * n - 1])
        N2, e2 = pendant(n - 1)
        N2i, e2i = N2 + 1, list(e2)  # disjoint isolate d
        check_iso(N1, e1, N2i, e2i,
                  iso_map_in_subgraph(Nm, em, [2 * n - 1], tgt))
        res["iso_checks"].append(f"M_{n}-b = M_{n-1}+iso ok")
        # (iv) M_n - N[b_{n-1}] ≅ M_{n-2} (swap a<->b, a_{n-2} -> c')
        tgt = {}
        for i in range(n - 2):
            tgt[i] = (n - 2) + i
            tgt[n + i] = i
        tgt[n - 2] = 2 * (n - 2)
        dead = [2 * n - 1, 2 * n - 2, n - 1, 2 * n]
        N1, e1 = induced_subgraph(Nm, em, dead)
        N2, e2 = pendant(n - 2)
        check_iso(N1, e1, N2, e2, iso_map_in_subgraph(Nm, em, dead, tgt))
        res["iso_checks"].append(f"M_{n}-N[b] = M_{n-2} ok")
    res["seconds"] = round(time.time() - t0, 1)
    with open("reg_table.json", "w") as f:
        json.dump(res, f, indent=1)
    print("wrote reg_table.json in", res["seconds"], "s", flush=True)


if __name__ == "__main__":
    main()
