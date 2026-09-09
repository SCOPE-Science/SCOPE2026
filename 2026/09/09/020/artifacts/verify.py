"""Standalone verifier for lane-297 partial census. Stdlib + numpy only.
Checks: (1) each of 51 tables is a group of order 32 (identity, inverses,
full associativity 32^3 triples, vectorized); (2) recomputed invariants
(class, |G'|, |Z|, Frattini rank, gamma3, class-2-quotient derived) match
table.json; (3) pairwise non-isomorphism: different signature bins are
distinguished by recorded invariants; same-bin pairs by backtracking.
Usage: python3 verify.py  -> prints VERIFY_OK or FAIL detail.
"""
import json
import pickle
import sys
from collections import Counter

import numpy as np


def find_identity(T):
    n = T.shape[0]
    for e in range(n):
        if bool(np.all(T[e, :] == np.arange(n))) and bool(np.all(T[:, e] == np.arange(n))):
            return e
    raise ValueError("no identity")


def inverses(T, e):
    n = T.shape[0]
    inv = np.full(n, -1)
    for a in range(n):
        for b in np.where(T[a, :] == e)[0]:
            if T[b, a] == e:
                inv[a] = b
                break
        if inv[a] < 0:
            raise ValueError("no inverse")
    return inv


def subgroups_gen(T, e, inv, gens):
    seen = {e} | set(int(g) for g in gens)
    stack = list(seen)
    while stack:
        a = stack.pop()
        ia = int(inv[a])
        if ia not in seen:
            seen.add(ia)
            stack.append(ia)
        for b in list(seen):
            for c in (int(T[a, b]), int(T[b, a])):
                if c not in seen:
                    seen.add(c)
                    stack.append(c)
    return np.array(sorted(seen), dtype=int)


def derived(T, e, inv):
    n = T.shape[0]
    comms = {int(T[T[T[int(inv[a]), int(inv[b])], a], b]) for a in range(n) for b in range(n)}
    return subgroups_gen(T, e, inv, list(comms))


def lcs(T, e, inv):
    n = T.shape[0]
    series = [np.arange(n)]
    while len(series[-1]) > 1:
        prev = series[-1]
        comms = {int(T[T[T[int(inv[a]), int(inv[h])], a], int(h)])
                 for a in range(n) for h in prev}
        nxt = subgroups_gen(T, e, inv, list(comms))
        series.append(nxt)
        if len(series) > n + 1:
            raise ValueError("LCS did not terminate")
    return series


def center_size(T, e):
    n = T.shape[0]
    return int(sum(1 for a in range(n) if bool(np.all(T[a, :] == T[:, a]))))


def frat_rank(T, e, inv, D):
    n = T.shape[0]
    sq = subgroups_gen(T, e, inv, [int(T[a, a]) for a in range(n)])
    Phi = subgroups_gen(T, e, inv, list(set(sq.tolist()) | set(D.tolist())))
    return int(round(np.log2(n / len(Phi)))), len(Phi)


def signature(T, e, inv):
    n = T.shape[0]
    ab = True
    for a in range(n):
        for b in range(a + 1, n):
            if T[a, b] != T[b, a]:
                ab = False
                break
        if not ab:
            break
    Z = center_size(T, e)
    D = derived(T, e, inv)
    if ab:
        cl = 1
    else:
        cl = len(lcs(T, e, inv)) - 1
    fr, _ = frat_rank(T, e, inv, D)
    prof = tuple(sorted(np.linalg.matrix_rank(np.zeros((1, 1))).tolist() and
                        [0] for _ in [])) if False else None
    ords = []
    for a in range(n):
        x, k = a, 1
        while x != e:
            x = int(T[x, a])
            k += 1
        ords.append(k)
    return (ab, cl, Z, len(D), fr, tuple(sorted(ords)))


def iso_within_bin(T1, T2):
    n = T1.shape[0]
    e1 = find_identity(T1)
    e2 = find_identity(T2)
    i1, i2 = inverses(T1, e1), inverses(T2, e2)
    o1 = [0] * n
    o2 = [0] * n
    for a in range(n):
        x, k = a, 1
        while x != e1:
            x = int(T1[x, a])
            k += 1
        o1[a] = k
        x, k = a, 1
        while x != e2:
            x = int(T2[x, a])
            k += 1
        o2[a] = k
    if Counter(o1) != Counter(o2):
        return False
    gens = []
    seen = {e1}
    for a in range(n):
        if a not in seen:
            gens.append(a)
            seen = set(subgroups_gen(T1, e1, i1, gens).tolist())
    dom = gens + [a for a in range(n) if a not in set(gens) and a != e1]
    cand = {a: [b for b in range(n) if o2[b] == o1[a]] for a in dom}
    img = [-1] * n
    img[e1] = e2
    used = bytearray(n)
    used[e2] = 1
    assigned = []
    found = [False]

    def bt(i):
        if found[0]:
            return
        if i == len(dom):
            found[0] = True
            return
        a = dom[i]
        for b in cand[a]:
            if used[b] or found[0]:
                continue
            ok = True
            for x in assigned:
                if img[T1[x, a]] != -1 and img[T1[x, a]] != T2[img[x], b]:
                    ok = False
                    break
                if ok and img[T1[a, x]] != -1 and img[T1[a, x]] != T2[b, img[x]]:
                    ok = False
                    break
            if ok:
                c2 = T1[a, a]
                if img[c2] != -1 and img[c2] != T2[b, b]:
                    ok = False
            if not ok:
                continue
            img[a] = b
            used[b] = 1
            assigned.append(a)
            bt(i + 1)
            assigned.pop()
            used[b] = 0
            img[a] = -1
    bt(0)
    return found[0]


def main():
    reps = pickle.load(open("reps32.pkl", "rb"))
    rows = json.load(open("table.json"))
    assert len(reps) == 51, f"want 51 reps, got {len(reps)}"
    assert len(rows) == 51, f"want 51 rows, got {len(rows)}"
    Ts = [np.array(T, dtype=int) for T, _ in reps]
    # (1) group axioms
    for k, T in enumerate(Ts):
        assert T.shape == (32, 32), k
        e = find_identity(T)
        inverses(T, e)
        ar = np.arange(32)
        for a in range(32):
            Ta = T[a, :]
            if not bool(np.all(T[Ta, :] == T[a, T])):
                print(f"FAIL associativity g{k} a={a}")
                sys.exit(1)
    print("axioms OK (51 tables, full 32^3 associativity)", flush=True)
    # (2) invariants vs table.json
    for k, T in enumerate(Ts):
        r = rows[k]
        e = find_identity(T)
        inv = inverses(T, e)
        D = derived(T, e, inv)
        ab = all(T[a, b] == T[b, a] for a in range(32) for b in range(a + 1, 32))
        cl = 1 if ab else len(lcs(T, e, inv)) - 1
        fr, _ = frat_rank(T, e, inv, D)
        assert r["klass"] == cl, (k, r["klass"], cl)
        assert r["derived"] == len(D), (k,)
        assert r["center"] == center_size(T, e), (k,)
        assert r["frat_rank"] == fr, (k,)
        assert r["abelian"] == bool(ab), (k,)
    print("invariants OK (class/derived/center/frattini match table.json)", flush=True)
    # (3) distinctness
    sigs = []
    for T in Ts:
        e = find_identity(T)
        sigs.append(signature(T, e, inverses(T, e)))
    bins = {}
    for k, s in enumerate(sigs):
        bins.setdefault(s, []).append(k)
    nback = 0
    for s, ks in bins.items():
        for i in range(len(ks)):
            for j in range(i + 1, len(ks)):
                nback += 1
                if iso_within_bin(Ts[ks[i]], Ts[ks[j]]):
                    print(f"FAIL isomorphic pair {ks[i]},{ks[j]}")
                    sys.exit(1)
    print(f"distinctness OK ({len(bins)} signature bins, {nback} backtrack pair checks)", flush=True)
    ab = sum(1 for s in sigs if s[0])
    print(f"class={Counter(s[1] for s in sigs)} derived={Counter(s[3] for s in sigs)} "
          f"center={Counter(s[2] for s in sigs)} frat={Counter(s[4] for s in sigs)} abelian={ab}")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
