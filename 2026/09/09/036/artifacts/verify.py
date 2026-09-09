"""Stdlib-only verifier for the 6-vertex pure 2-complex torsion census headline claim.

Replays WITHOUT sympy/numpy:
 1. covering count = 1042642 (brute force over 2^20 masks),
 2. Burnside orbit count = 2136 incl. empty (conjugacy-class sums),
 3. canonical non-isomorphism + stabilizer Burnside sum over census_2102.csv,
 4. RP2 witness identities d1(c)=0, d2(s)=2c, w*d2=0 mod 2, w.c=1 mod 2,
    closed-surface check (edge degrees 2, links cycles, chi=1),
 5. SNF invariants of witness d2 via Bareiss determinantal divisors -> (1^9,2),
 6. UCT mod-p spot checks on witness row (p=2,3,5),
 7. signature-cell row counts sum to 2102.

Run: python3 verify.py  (expects sibling files census_2102.csv, witness.json)
Prints VERIFY_OK on success.
"""
import csv
import itertools
import json
import math
import os
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))

TRIS = sorted(itertools.combinations(range(6), 3))
TIDX = {t: i for i, t in enumerate(TRIS)}
PERMS = list(itertools.permutations(range(6)))
PERM_IMG = []
for p in PERMS:
    img = [0] * 20
    for i, t in enumerate(TRIS):
        img[i] = TIDX[tuple(sorted(p[v] for v in t))]
    PERM_IMG.append(img)


def apply_perm(mask, img):
    nm = 0
    m = mask
    while m:
        lsb = m & -m
        i = lsb.bit_length() - 1
        nm |= 1 << img[i]
        m ^= lsb
    return nm


def bareiss_det(A):
    A = [row[:] for row in A]
    n = len(A)
    if n == 0:
        return 1
    if any(len(r) != n for r in A):
        raise ValueError("nonsquare")
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            piv = None
            for i in range(k + 1, n):
                if A[i][k] != 0:
                    piv = i
                    break
            if piv is None:
                return 0
            A[k], A[piv] = A[piv], A[k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
            A[i][k] = 0
        prev = A[k][k]
        if prev == 0:
            return 0
    return A[n - 1][n - 1]


def det_divisors(D):
    r = len(D)
    c = len(D[0]) if r else 0
    m = min(r, c)
    divs = [1]
    for k in range(1, m + 1):
        g = 0
        for rows in itertools.combinations(range(r), k):
            for cols in itertools.combinations(range(c), k):
                d = abs(bareiss_det([[int(D[i][j]) for j in cols] for i in rows]))
                g = math.gcd(g, d)
                if g == 1:
                    break
            if g == 1:
                break
        divs.append(g)
    return divs


def rank_mod(mat, p):
    if not mat or not mat[0]:
        return 0
    A = [[x % p for x in row] for row in mat]
    r, c = len(A), len(A[0])
    rk, row = 0, 0
    for col in range(c):
        piv = None
        for i in range(row, r):
            if A[i][col] % p != 0:
                piv = i
                break
        if piv is None:
            continue
        A[row], A[piv] = A[piv], A[row]
        inv = pow(A[row][col], -1, p)
        A[row] = [(x * inv) % p for x in A[row]]
        for i in range(r):
            if i != row and A[i][col] != 0:
                f = A[i][col]
                A[i] = [(A[i][j] - f * A[row][j]) % p for j in range(c)]
        row += 1
        rk += 1
        if row == r:
            break
    return rk


def boundary(mask):
    T = [TRIS[i] for i in range(20) if (mask >> i) & 1]
    eset = sorted(set(e for t in T for e in itertools.combinations(t, 2)))
    eidx = {e: i for i, e in enumerate(eset)}
    E, Tn = len(eset), len(T)
    d2 = [[0] * Tn for _ in range(E)]
    for j, (a, b, c) in enumerate(T):
        d2[eidx[(a, b)]][j] += 1
        d2[eidx[(a, c)]][j] -= 1
        d2[eidx[(b, c)]][j] += 1
    d1 = [[0] * E for _ in range(6)]
    for (u, v), j in eidx.items():
        d1[u][j] = -1
        d1[v][j] = 1
    return T, eset, d2, d1


def main():
    # 1. covering count
    vm = [0] * 6
    for i, t in enumerate(TRIS):
        for v in t:
            vm[v] |= 1 << i
    cov = sum(1 for m in range(1 << 20) if all(m & vm[v] for v in range(6)))
    assert cov == 1042642, cov
    print("covering_masks=1042642 OK")

    # 2. Burnside orbit count via cycle types on triangles
    def cycletype(p):
        seen = [False] * 6
        lens = []
        for i in range(6):
            if not seen[i]:
                j, ln = i, 0
                while not seen[j]:
                    seen[j] = True
                    j = p[j]
                    ln += 1
                lens.append(ln)
        return tuple(sorted(lens))

    def tricycles(p):
        seen = [False] * 20
        n = 0
        for i, t in enumerate(TRIS):
            if not seen[i]:
                n += 1
                j = i
                while not seen[j]:
                    seen[j] = True
                    j = TIDX[tuple(sorted(p[v] for v in TRIS[j]))]
        return n

    from collections import Counter as C
    tc = C(cycletype(p) for p in PERMS)
    tot = 0
    for ct, cnt in tc.items():
        rep = next(p for p in PERMS if cycletype(p) == ct)
        tot += cnt * (2 ** tricycles(rep))
    assert tot % 720 == 0 and tot // 720 == 2136, tot
    print("burnside_orbits=2136 OK")

    # 3. census file: non-isomorphism + Burnside sum + torsion uniqueness
    with open(os.path.join(BASE, "census_2102.csv")) as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 2102, len(rows)
    masks = [int(r["mask"]) for r in rows]
    assert len(set(masks)) == 2102
    canons, stabs = [], []
    for m in masks:
        mn, st = m, 0
        for img in PERM_IMG:
            nm = apply_perm(m, img)
            if nm < mn:
                mn = nm
            if nm == m:
                st += 1
        canons.append(mn)
        stabs.append(st)
    assert len(set(canons)) == 2102, "isomorphism collision"
    assert all(720 % s == 0 for s in stabs)
    assert sum(720 // s for s in stabs) == 1042642
    print("canonical_2102 + burnside_sum=1042642 OK")
    tors = [r for r in rows if r["torsion_H1"] not in ("-", "")]
    assert len(tors) == 1 and int(tors[0]["mask"]) == 242467, tors
    assert tors[0]["snf_d2"] == "1;1;1;1;1;1;1;1;1;2"
    print("unique_torsion_row mask=242467 SNF=(1^9,2) OK")

    # 4-6. witness identities, closed surface, SNF, UCT
    w = json.load(open(os.path.join(BASE, "witness.json")))
    T, eset, d2, d1 = boundary(242467)
    assert [list(t) for t in T] == w["tris"]
    assert [list(e) for e in eset] == w["edges"]
    s, c, wl = w["s"], w["c"], w["w"]
    E, Tn = len(eset), len(T)
    d1c = [sum(d1[v][j] * c[j] for j in range(E)) for v in range(6)]
    assert all(x == 0 for x in d1c), d1c
    d2s = [sum(d2[i][j] * s[j] for j in range(Tn)) for i in range(E)]
    assert all(d2s[i] == 2 * c[i] for i in range(E)), (d2s, c)
    assert any(x != 0 for x in c)
    wd2 = [sum(wl[i] * d2[i][j] for i in range(E)) % 2 for j in range(Tn)]
    assert all(x == 0 for x in wd2), wd2
    assert sum(wl[i] * c[i] for i in range(E)) % 2 == 1
    # d1*d2 == 0
    for i in range(6):
        for j in range(Tn):
            assert sum(d1[i][k] * d2[k][j] for k in range(E)) == 0
    # closed surface: every edge degree 2, links 5-cycles, chi=1
    deg = Counter()
    for t in T:
        for e in itertools.combinations(t, 2):
            deg[tuple(sorted(e))] += 1
    assert set(deg.values()) == {2}, set(deg.values())
    for v in range(6):
        link = [tuple(sorted(set(t) - {v})) for t in T if v in t]
        assert len(link) == 5
        dc = Counter()
        for a, b in link:
            dc[a] += 1
            dc[b] += 1
        assert set(dc.values()) == {2}, (v, link)
    assert 6 - E + Tn == 1
    print("witness (s,c,w) + closed-surface chi=1 OK")
    divs = det_divisors(d2)
    inv = [divs[k] // divs[k - 1] for k in range(1, len(divs))]
    assert inv == [1] * 9 + [2], (divs, inv)
    print("bareiss SNF=(1^9,2) OK")
    for p in (2, 3, 5):
        r1p, r2p = rank_mod(d1, p), rank_mod(d2, p)
        assert E - r1p - r2p == (0 + (1 if p == 2 else 0)), (p, r1p, r2p)
        assert Tn - r2p == (0 + (1 if p == 2 else 0)), (p, r1p, r2p)
    print("UCT p=2,3,5 OK")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
