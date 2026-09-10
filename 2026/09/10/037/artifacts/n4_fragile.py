"""N4 F7^- fragile-doubleton search (exact GF(3) linear algebra, stdlib only).

N4 = ternary [I8 | A4] (A4 from Brettell Matroid Union blog = Brettell-Pendavingh
Sec 5 matrices; N4 self-dual so transpose ambiguity harmless).
F7^- model: e1,e2,e3,(1,1,0),(0,1,1),(1,0,1),(1,1,1) over GF(3) (6 three-point
lines verified in-script; F7 has 7, so this is the non-Fano).

Rank oracle: linear rank over GF(3), memoized on bitmasks.
Minor rank: r_{M/C\\D}(X) = r(X u C) - r(C); contraction M/e: r'(X)=r(Xu{e})-r({e}).
3-connectivity: min lambda(X)=r(X)+r(E\\X)-r(E) over 2<=|X|<=|E|-2 >= 2.
F7^- minor: exhaustive (S 7-set) x (C subset of complement) search with
  line-count/degree filter + full S7 permutation isomorphism check.
Fragility: for each e, at least one of M\\e, M/e has no F7^- minor.

Replay: python3 n4_fragile.py  (writes n4_certificate.json + log to stdout)
"""
import itertools, json, sys, time

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
VECS = []
for i in range(8):
    v = [0]*8; v[i] = 1; VECS.append(tuple(v))
for j in range(8):
    VECS.append(tuple(A4[r][j] % 3 for r in range(8)))
N = 16
FULL = (1 << N) - 1

def gf3_rank_vecs(rows):
    M = [list(r) for r in rows]
    r = 0
    nrows = len(M)
    for c in range(DIM):
        piv = -1
        for k in range(r, nrows):
            if M[k][c] % 3 != 0:
                piv = k; break
        if piv < 0:
            continue
        M[r], M[piv] = M[piv], M[r]
        if M[r][c] % 3 == 2:
            M[r] = [(-x) % 3 for x in M[r]]
        for k in range(nrows):
            if k != r and M[k][c] % 3 != 0:
                f = M[k][c] % 3
                M[k] = [(M[k][d] - f*M[r][d]) % 3 for d in range(DIM)]
        r += 1
        if r == DIM:
            break
    return r

_R = {}
def R(mask):
    v = _R.get(mask)
    if v is None:
        rows = [VECS[i] for i in range(N) if mask & (1 << i)]
        v = gf3_rank_vecs(rows)
        _R[mask] = v
    return v

def bits(mask):
    return [i for i in range(N) if mask & (1 << i)]

def popcnt(m):
    return bin(m).count("1")

# ---- F7^- model ----
F = [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(0,1,1),(1,0,1),(1,1,1)]
def gf3_rank3(rows):
    M = [list(r) for r in rows]
    r = 0
    for c in range(3):
        piv = -1
        for k in range(r, len(M)):
            if M[k][c] % 3 != 0:
                piv = k; break
        if piv < 0:
            continue
        M[r], M[piv] = M[piv], M[r]
        if M[r][c] % 3 == 2:
            M[r] = [(-x) % 3 for x in M[r]]
        for k in range(len(M)):
            if k != r and M[k][c] % 3 != 0:
                f = M[k][c] % 3
                M[k] = [(M[k][d] - f*M[r][d]) % 3 for d in range(3)]
        r += 1
    return r

F_TRIPLES = list(itertools.combinations(range(7), 3))
F_BASES = frozenset(t for t in F_TRIPLES if gf3_rank3([F[i] for i in t]) == 3)
F_LINES = [t for t in F_TRIPLES if gf3_rank3([F[i] for i in t]) <= 2]
def degseq(lines):
    d = [0]*7
    for t in lines:
        for i in t:
            d[i] += 1
    return sorted(d)
F_DEG = degseq(F_LINES)
print("F model: rank=%d lines=%d deg=%s nbases=%d" % (
    gf3_rank3(F), len(F_LINES), F_DEG, len(F_BASES)), flush=True)
assert gf3_rank3(F) == 3 and len(F_LINES) == 6, "F model must be non-Fano (6 lines)"
print("F lines:", F_LINES, flush=True)

PERMS = list(itertools.permutations(range(7)))
# permuted bases set of F for fast compare
F_BASES_PERMUTED = set()
for p in PERMS:
    F_BASES_PERMUTED.add(frozenset(tuple(sorted((p[a], p[b], p[c]))) for (a, b, c) in F_BASES))

def minor_pattern_match(S, rfun):
    """S: ordered list of 7 elements. Check rfun-minor on S (C already folded
    into rfun) is isomorphic to F. Returns perm or None."""
    # simplicity + rank
    for i in S:
        if rfun(1 << i) != 1:
            return None
    for a, b in itertools.combinations(S, 2):
        if rfun((1 << a) | (1 << b)) != 2:
            return None
    if rfun(sum(1 << i for i in S)) != 3:
        return None
    rk = {}
    for t in F_TRIPLES:
        m = (1 << S[t[0]]) | (1 << S[t[1]]) | (1 << S[t[2]])
        rk[t] = rfun(m)
    lines = [t for t in F_TRIPLES if rk[t] <= 2]
    if len(lines) != 6 or degseq(lines) != F_DEG:
        return None
    B = frozenset(t for t in F_TRIPLES if rk[t] == 3)
    if B in F_BASES_PERMUTED:
        for p in PERMS:
            if frozenset(tuple(sorted((p[a], p[b], p[c]))) for (a, b, c) in B) == F_BASES:
                return p
    return None

def has_minor(Gmask, rfun, want_cert=False):
    """Exhaustive search for F7^- minor of matroid on ground Gmask with rank
    oracle rfun(mask)->int. Returns cert dict or None."""
    G = bits(Gmask)
    for S in itertools.combinations(G, 7):
        Smask = sum(1 << i for i in S)
        rest = [i for i in G if not (Smask & (1 << i))]
        # quick: S must be able to span rank 3 after some contraction;
        # loop over C subsets of rest
        nr = len(rest)
        for cb in range(1 << nr):
            Cmask = 0
            for k in range(nr):
                if cb & (1 << k):
                    Cmask |= (1 << rest[k])
            rC = rfun(Cmask)
            if rfun(Smask | Cmask) - rC != 3:
                continue
            def r2(m, _C=Cmask, _r=rC):
                return rfun(m | _C) - _r
            p = minor_pattern_match(list(S), r2)
            if p is not None:
                Dmask = (Gmask ^ Smask) & ~Cmask
                return {"S": list(S), "C": bits(Cmask), "D": bits(Dmask),
                        "perm": list(p)}
    return None

def is_3connected(Emask):
    E = bits(Emask)
    n = len(E)
    rE = R(Emask)
    for i in E:
        if R(1 << i) == 0:
            return False, ("loop", i)
    for a, b in itertools.combinations(E, 2):
        if R((1 << a) | (1 << b)) <= 1:
            # parallel pair -> 2-separation unless tiny; record lambda
            lam = R(1 << a) + R(Emask ^ (1 << a)) - rE
            return False, ("parallel", (a, b))
    # subsets X, 2<=|X|<=n-2 (use |X|<=n//2 by symmetry)
    for r in range(2, n // 2 + 1):
        for X in itertools.combinations(E, r):
            Xm = sum(1 << i for i in X)
            lam = R(Xm) + R(Emask ^ Xm) - rE
            if lam < 2:
                return False, ("sep", (list(X), lam))
    return True, ("ok", rE)

def main():
    t0 = time.time()
    print("N4 rank:", R(FULL), " valido:", popcnt(FULL), flush=True)
    assert R(FULL) == 8
    c3, _ = is_3connected(FULL)
    print("N4 3-connected:", c3, flush=True)
    # scan pairs
    found = []
    for idx, (a, b) in enumerate(itertools.combinations(range(16), 2)):
        Em = FULL ^ ((1 << a) | (1 << b))
        ok, info = is_3connected(Em)
        if not ok:
            continue
        cert = has_minor(Em, R)
        print("pair (%d,%d): 3conn + minor=%s" % (a, b, cert is not None),
              flush=True)
        if cert is not None:
            found.append((a, b, cert))
            break  # take first; fragility next
    if not found:
        print("NO_PAIR_FOUND", flush=True)
        return
    a, b, cert = found[0]
    print("CHOSEN_PAIR %d %d cert=%s" % (a, b, json.dumps(cert)), flush=True)
    Em = FULL ^ ((1 << a) | (1 << b))
    # fragility table
    table = []
    allok = True
    for e in bits(Em):
        Gdel = Em ^ (1 << e)
        c_del = has_minor(Gdel, R)
        del_has = c_del is not None
        re_ = R(1 << e)
        if re_ == 0:
            c_con = c_del
        else:
            def rc(m, _e=e, _re=re_):
                return R(m | (1 << _e)) - _re
            c_con = has_minor(Gdel, rc)
        con_has = c_con is not None
        fragile_e = (not del_has) or (not con_has)
        allok = allok and fragile_e
        table.append({"e": e, "del_has_minor": del_has,
                      "con_has_minor": con_has, "fragile": fragile_e})
        print("e=%d del_has=%s con_has=%s" % (e, del_has, con_has), flush=True)
    print("FRAGILE_ALL:", allok, flush=True)
    out = {"N4": {"A4": A4, "rank": 8},
           "pair": [a, b], "minor_cert": cert, "fragility": table,
           "fragile": allok, "F_lines": F_LINES, "F_deg": F_DEG,
           "seconds": round(time.time() - t0, 1),
           "memo_size": len(_R)}
    with open("output/artifacts/n4_certificate.json", "w") as f:
        json.dump(out, f, indent=1)
    print("wrote output/artifacts/n4_certificate.json", flush=True)
    print("TOTAL_S %.1fs" % (time.time() - t0), flush=True)

if __name__ == "__main__":
    main()
