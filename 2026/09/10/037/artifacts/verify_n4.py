"""Independent verifier for n4_certificate.json (separate code path, stdlib only).

Re-checks from scratch:
 (0) N4 = [I8|A4] ternary construction, rank 8, 3-connected.
 (1) Em = N4\\a\\b is 3-connected via FULL subset lambda scan (2..n-2, both sides).
 (2) Positive minor cert: S,C,D partition Em; contracted rank is 3, simple;
     line-set (6 triples) and full bases-set equal F7^- model up to stored perm.
 (3) Fragility: for each e, re-run exhaustive F7^--minor search on the side(s)
     the certificate marks negative (and confirm the positive side has a minor).
     Exhaustive = all 7-subsets S x all contraction subsets C of the complement,
     with direct line/bases isomorphism check (no shared code with n4_fragile.py).

Replay: python3 verify_n4.py  -> prints VERIFY_OK or fails loudly.
"""
import itertools, json

A4 = [
 [2,0,2,1,2,1,0,0],
 [2,1,0,2,0,2,2,0],
 [2,0,2,0,0,1,0,0],
 [2,0,2,2,2,2,2,2],
 [0,1,1,1,1,1,1,1],
 [2,1,0,0,0,2,0,0],
 [2,0,0,2,2,2,2,0],
 [1,0,1,2,1,2,1,1],
]
DIM = 8
V = []
for i in range(8):
    v = [0]*8; v[i] = 1; V.append(v)
for j in range(8):
    V.append([A4[r][j] % 3 for r in range(8)])
N = 16
FULL = (1 << N) - 1

def rank_of(mask):
    rows = [row[:] for i, row in enumerate(V) if mask & (1 << i)]
    r = 0
    R = len(rows)
    for c in range(DIM):
        p = -1
        for k in range(r, R):
            if rows[k][c] % 3:
                p = k; break
        if p < 0:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        inv = 1 if rows[r][c] % 3 == 1 else 2
        rows[r] = [(x*inv) % 3 for x in rows[r]]
        for k in range(R):
            if k != r and rows[k][c] % 3:
                f = rows[k][c] % 3
                rows[k] = [(rows[k][d]-f*rows[r][d]) % 3 for d in range(DIM)]
        r += 1
    return r

def rank3_of(rows):
    M = [list(map(int, r)) for r in rows]
    r = 0
    for c in range(3):
        p = -1
        for k in range(r, len(M)):
            if M[k][c] % 3:
                p = k; break
        if p < 0:
            continue
        M[r], M[p] = M[p], M[r]
        if M[r][c] % 3 == 2:
            M[r] = [(-x) % 3 for x in M[r]]
        for k in range(len(M)):
            if k != r and M[k][c] % 3:
                f = M[k][c] % 3
                M[k] = [(M[k][d]-f*M[r][d]) % 3 for d in range(3)]
        r += 1
    return r

F = [[1,0,0],[0,1,0],[0,0,1],[1,1,0],[0,1,1],[1,0,1],[1,1,1]]
FT = list(itertools.combinations(range(7), 3))
F_BASES = frozenset(t for t in FT if rank3_of([F[i] for i in t]) == 3)
F_LINES = frozenset(t for t in FT if rank3_of([F[i] for i in t]) <= 2)
assert len(F_BASES) == 29 and len(F_LINES) == 6, (len(F_BASES), len(F_LINES))

def iso_to_F(S, rfun):
    """S: 7-tuple. Returns perm mapping S-order to F-order, or None."""
    Sm = 0
    for i in S:
        Sm |= (1 << i)
    if rfun(Sm) != 3:
        return None
    for i in S:
        if rfun(1 << i) != 1:
            return None
    for x, y in itertools.combinations(S, 2):
        if rfun((1 << x) | (1 << y)) != 2:
            return None
    rk = {t: rfun((1 << S[t[0]]) | (1 << S[t[1]]) | (1 << S[t[2]])) for t in FT}
    lines = frozenset(t for t in FT if rk[t] <= 2)
    if lines != F_LINES and not (
            len(lines) == 6 and
            sorted(sum(1 for L in lines if i in L) for i in range(7)) ==
            sorted(sum(1 for L in F_LINES if i in L) for i in range(7))):
        if len(lines) != 6:
            return None
    B = frozenset(t for t in FT if rk[t] == 3)
    if len(B) != 29:
        return None
    for p in itertools.permutations(range(7)):
        if frozenset(tuple(sorted((p[a], p[b], p[c]))) for (a, b, c) in B) == F_BASES:
            return list(p)
    return None

def search_minor(Gmask, rfun):
    G = [i for i in range(N) if Gmask & (1 << i)]
    for S in itertools.combinations(G, 7):
        Sm = sum(1 << i for i in S)
        rest = [i for i in G if not (Sm & (1 << i))]
        for cb in range(1 << len(rest)):
            Cm = 0
            for k in range(len(rest)):
                if cb & (1 << k):
                    Cm |= (1 << rest[k])
            rC = rfun(Cm)
            if rfun(Sm | Cm) - rC != 3:
                continue
            def r2(m, _C=Cm, _r=rC):
                return rfun(m | _C) - _r
            p = iso_to_F(S, r2)
            if p is not None:
                return {"S": list(S), "C": [i for i in range(N) if Cm & (1 << i)],
                        "perm": p}
    return None

def main():
    cert = json.load(open("output/artifacts/n4_certificate.json"))
    a, b = cert["pair"]
    assert a != b and 0 <= a < 16 and 0 <= b < 16
    assert rank_of(FULL) == 8, "N4 rank must be 8"
    Em = FULL ^ ((1 << a) | (1 << b))
    assert bin(Em).count("1") == 14
    # (1) full 3-connectivity scan
    E = [i for i in range(N) if Em & (1 << i)]
    rE = rank_of(Em)
    worst = 99
    for r in range(2, len(E) - 1):
        for X in itertools.combinations(E, r):
            Xm = sum(1 << i for i in X)
            lam = rank_of(Xm) + rank_of(Em ^ Xm) - rE
            worst = min(worst, lam)
            assert lam >= 2, ("2-separation", X, lam)
    print("3-connectivity: min-lambda over all 2..12-sets =", worst)
    # (2) positive cert replay
    mc = cert["minor_cert"]
    S, C, D = mc["S"], mc["C"], mc["D"]
    assert len(S) == 7 and len(set(S)) == 7
    assert sorted(S + C + D) == sorted(E), "S,C,D must partition Em"
    Cm = sum(1 << i for i in C)
    rC = rank_of(Cm)
    Sm = sum(1 << i for i in S)
    assert rank_of(Sm | Cm) - rC == 3
    p = mc["perm"]
    def r2(m, _C=Cm, _r=rC):
        return rank_of(m | _C) - _r
    q = iso_to_F(tuple(S), r2)
    assert q is not None, "stored minor cert does not verify as F7^-"
    B = frozenset(t for t in FT
                  if r2((1 << S[t[0]]) | (1 << S[t[1]]) | (1 << S[t[2]])) == 3)
    Bmapped = frozenset(tuple(sorted((p[a_], p[b_], p[c_]))) for (a_, b_, c_) in B)
    assert Bmapped == F_BASES, "perm does not carry minor bases onto F7^- bases"
    print("minor cert: S=%s C=%s D=%s perm re-verified (bases match F7^- exactly)" % (S, C, D))
    # (3) fragility replay
    for row in cert["fragility"]:
        e = row["e"]
        Gd = Em ^ (1 << e)
        del_has = search_minor(Gd, rank_of) is not None
        re_ = rank_of(1 << e)
        if re_ == 0:
            con_has = del_has
        else:
            def rc(m, _e=e, _r=re_):
                return rank_of(m | (1 << _e)) - _r
            con_has = search_minor(Gd, rc) is not None
        assert del_has == row["del_has_minor"], ("del mismatch", e)
        assert con_has == row["con_has_minor"], ("con mismatch", e)
        assert ((not del_has) or (not con_has)), ("not fragile", e)
        print("e=%2d del_has=%s con_has=%s fragile OK" % (e, del_has, con_has))
    print("VERIFY_OK: pair (%d,%d), 14/14 fragile rows, minor + connectivity replayed" % (a, b))

if __name__ == "__main__":
    main()
