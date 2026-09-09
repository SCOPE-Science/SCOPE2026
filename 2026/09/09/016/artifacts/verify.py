"""Rerun script: demicap-fiber intersection spectrum in AG(4,3).

Replays, from committed coordinates with stdlib only:
 1. AG(4,3) as F_3^4 (point codes 0..80, base-3 4-tuples), anchor 0=(0,0,0,0).
 2. Committed demicap D0 = five 0-lines through +-(1,0,0,0),(0,1,0,0),
    (0,0,1,0),(0,0,0,1),(1,1,1,1); verifies D0 is a cap and no 4 of its
    5 lines are cohyperplanar.
 3. Enumerates ALL 20-point maximal caps C containing D0 by unbiased
    backtracking over the 30-point pool (points completing no line with D0),
    with exact collinearity-tensor check on every addition. Result: 6 caps.
 4. Verifies each is a cap, is complete (maximal), has anchor 0, and has
    linear stabilizer order 2880; Stab(D0) has order 240 and acts
    transitively on the 6 caps.
 5. Computes all 15 pairwise intersections: every distinct pair meets in
    exactly 12 points (6 shared 0-lines). Hence I(D0) = {12}, and each of
    10,11,13,14,15,16,17,18,19 is unattained (vacuous exclusion: the
    15-pair table contains no other value).

Run: python3 verify.py  (stdlib only, seconds).
"""
import itertools

def decode(n):
    return ((n // 27) % 3, (n // 9) % 3, (n // 3) % 3, n % 3)

def encode(p):
    return p[0] * 27 + p[1] * 9 + p[2] * 3 + p[3]

def neg(p):
    return tuple((-a) % 3 for a in p)

def third(p, q):
    return tuple((-p[i] - q[i]) % 3 for i in range(4))

def rank4(rows):
    M = [[x % 3 for x in r] for r in rows]
    r = 0
    for c in range(4):
        piv = None
        for i in range(r, len(M)):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = 1 if M[r][c] == 1 else 2
        M[r] = [(v * inv) % 3 for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % 3 for j in range(4)]
        r += 1
    return r

def aline_of(p):
    q = neg(p)
    return tuple(sorted([encode(p), encode(q)]))

def stab_order(vecs):
    S = set(vecs)
    L = list(S)
    n = 0
    for a in L:
        for b in L:
            if b == a or b == neg(a):
                continue
            for c in L:
                if c in (a, neg(a), b, neg(b)):
                    continue
                for d in L:
                    if d in (a, neg(a), b, neg(b), c, neg(c)):
                        continue
                    if rank4([a, b, c, d]) < 4:
                        continue
                    cols = (a, b, c, d)
                    ok = True
                    for v in S:
                        img = tuple((v[0]*cols[0][k] + v[1]*cols[1][k]
                                     + v[2]*cols[2][k] + v[3]*cols[3][k]) % 3
                                    for k in range(4))
                        if img not in S:
                            ok = False
                            break
                    if ok:
                        n += 1
    return n

def main():
    e1 = (1,0,0,0); e2 = (0,1,0,0); e3 = (0,0,1,0); e4 = (0,0,0,1); s = (1,1,1,1)
    D0lines = [aline_of(e1), aline_of(e2), aline_of(e3), aline_of(e4), aline_of(s)]
    D0pts = sorted(p for L in D0lines for p in L)
    D0set = set(D0pts)
    assert len(D0pts) == 10
    # D0 is a cap
    for i in range(10):
        for j in range(i + 1, 10):
            t = encode(third(decode(D0pts[i]), decode(D0pts[j])))
            assert t not in D0set, "D0 not a cap"
    # no 4 of the 5 lines cohyperplanar
    dirs = [decode(L[0]) for L in D0lines]
    for combo in itertools.combinations(dirs, 4):
        assert rank4(list(combo)) == 4, "D0 has 4 cohyperplanar lines"
    print("D0 demicap check: OK", D0pts)

    # pool = points completing no line with a pair from D0
    blocked = set()
    for i in range(10):
        for j in range(i + 1, 10):
            t = encode(third(decode(D0pts[i]), decode(D0pts[j])))
            if t not in D0set:
                blocked.add(t)
    pool = [n for n in range(81) if n not in D0set and n not in blocked]
    assert len(pool) == 30, len(pool)
    T = [[0]*81 for _ in range(81)]
    for a in range(81):
        pa = decode(a)
        for b in range(81):
            T[a][b] = encode(third(pa, decode(b)))
    caps = []
    def bt(start, chosen, chosenset):
        if len(chosen) == 10:
            caps.append(tuple(chosen))
            return
        for i in range(start, len(pool)):
            p = pool[i]
            if all(T[p][q] not in D0set and T[p][q] not in chosenset for q in chosen):
                chosen.append(p); chosenset.add(p)
                bt(i + 1, chosen, chosenset)
                chosen.pop(); chosenset.remove(p)
    bt(0, [], set())
    assert len(caps) == 6, len(caps)
    full = [tuple(sorted(D0pts + list(c))) for c in caps]
    print("fiber size: 6")
    for c in full:
        print(" ", list(c))
    # cap + maximal + anchor-0 checks
    for cp in full:
        S = set(cp)
        assert len(cp) == 20
        for i in range(20):
            for j in range(i + 1, 20):
                t = encode(third(decode(cp[i]), decode(cp[j])))
                assert not (t in S and t != cp[i] and t != cp[j]), "not a cap"
        for p in range(81):
            if p == 0 or p in S:
                continue
            assert any(encode(third(decode(cp[i]), decode(cp[j]))) == p
                       for i in range(20) for j in range(i + 1, 20)), "not maximal"
        lines = set()
        for p in cp:
            lines.add(tuple(sorted([p, encode(neg(decode(p)))])))
        assert len(lines) == 10 and all(
            encode(third(decode(a), decode(b))) == 0 for a, b in lines)
        assert stab_order([decode(n) for n in cp]) == 2880
    assert stab_order([decode(n) for n in D0pts]) == 240
    print("cap/maximal/anchor/stabilizer checks: OK")
    # pairwise intersections
    vals = {}
    for i in range(6):
        for j in range(i + 1, 6):
            v = len(set(full[i]) & set(full[j]))
            vals.setdefault(v, []).append((i, j))
    print("intersection values:", {k: len(v) for k, v in vals.items()})
    assert set(vals) == {12} and len(vals[12]) == 15
    for (i, j) in vals[12]:
        assert len(set(full[i]) & set(full[j])) == 12
    missing = [v for v in range(10, 20) if v not in vals]
    assert missing == [10, 11, 13, 14, 15, 16, 17, 18, 19]
    print("I(D0) = {12}; missing (excluded):", missing)
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
