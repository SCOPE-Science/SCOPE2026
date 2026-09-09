"""Self-contained verifier for PG(2,13) minimal blocking-set witnesses (stdlib only).

Replays from polynomials alone:
  (1) builds PG(2,13) (183 points, 183 lines) with exact incidence;
  (2) builds each Redei blocking set B = U union D (U = graph of f, D = slope set on z=0);
  (3) checks |B|, direction set D vs claimed, blocking (every line meets B),
      minimality (every point has a tangent line meeting B only there),
      line-intersection spectrum, Redei-line count, and Redei divisibility
      (for y not in D, {f(x)-x*y : x} is all of F_13).
Usage: python3 verify.py
"""
import sys

P = 13

def norm(t):
    for c in t:
        if c % P != 0:
            inv = pow(c, -1, P)
            return tuple((v * inv) % P for v in t)
    raise ValueError("zero vector")

def build_plane():
    PTS, idx, LNS, lidx = [], {}, [], {}
    for x in range(P):
        for y in range(P):
            for z in range(P):
                if x == y == z == 0:
                    continue
                n = norm((x, y, z))
                if n not in idx:
                    idx[n] = len(PTS)
                    PTS.append(n)
    for a in range(P):
        for b in range(P):
            for c in range(P):
                if a == b == c == 0:
                    continue
                n = norm((a, b, c))
                if n not in lidx:
                    lidx[n] = len(LNS)
                    LNS.append(n)
    assert len(PTS) == 183 and len(LNS) == 183
    ptlines = [set() for _ in PTS]
    linepts = [set() for _ in LNS]
    for j, (a, b, c) in enumerate(LNS):
        for i, (x, y, z) in enumerate(PTS):
            if (a * x + b * y + c * z) % P == 0:
                linepts[j].add(i)
                ptlines[i].add(j)
    return PTS, idx, LNS, lidx, ptlines, linepts

def ev(poly, x):
    return sum(c * pow(x, e, P) for e, c in poly.items()) % P

# Witnesses: {name: (poly {exp: coeff}, claimed_D, claimed_size, claimed_spectrum)}
WITNESSES = {
    "W21": ({7: 1}, [1, 3, 4, 5, 8, 9, 10, 12], 21,
            {1: 126, 2: 18, 3: 36, 8: 3}),
    "W23": ({9: 1, 5: 1}, [0, 1, 2, 3, 4, 5, 9, 10, 11, 12], 23,
            {1: 96, 2: 52, 3: 32, 6: 1, 10: 2}),
    "W24": ({7: 1, 3: 2}, [0, 1, 2, 3, 4, 6, 7, 9, 10, 11, 12], 24,
            {1: 91, 2: 59, 3: 16, 4: 14, 6: 2, 11: 1}),
}

def main():
    PTS, idx, LNS, lidx, ptlines, linepts = build_plane()
    linf = lidx[norm((0, 0, 1))]
    ok_all = True
    for name, (poly, D_claim, size_claim, spec_claim) in WITNESSES.items():
        f = [ev(poly, x) for x in range(P)]
        D = set()
        for x in range(P):
            for y in range(x + 1, P):
                D.add(((f[x] - f[y]) * pow((x - y) % P, -1, P)) % P)
        Ds = sorted(D)
        raw = [(x, f[x], 1) for x in range(P)] + [(1, m, 0) for m in Ds]
        Bpts = [norm(t) for t in raw]
        Bset = set(idx[t] for t in Bpts)
        checks = []
        checks.append(("distinct|B|==claim", len(Bset) == len(Bpts) == size_claim))
        checks.append(("D==claim", Ds == D_claim))
        checks.append(("|B cap l_inf|==|D|", len(Bset & linepts[linf]) == len(Ds)))
        blk = all(len(Bset & lp) > 0 for lp in linepts)
        checks.append(("blocking", blk))
        tang = {}
        for i in Bset:
            t = next((j for j in ptlines[i] if len(Bset & linepts[j]) == 1), None)
            tang[i] = t
        checks.append(("minimal(all essential)", all(t is not None for t in tang.values())))
        from collections import Counter
        spec = dict(sorted(Counter(len(Bset & lp) for lp in linepts).items()))
        checks.append(("spectrum==claim", spec == spec_claim))
        rediv = True
        for y in range(P):
            if y not in D:
                if sorted((f[x] - x * y) % P for x in range(P)) != list(range(P)):
                    rediv = False
        checks.append(("Redei-divisibility", rediv))
        stat = "PASS" if all(v for _, v in checks) else "FAIL"
        if stat == "FAIL":
            ok_all = False
        print(f"{name} poly={poly} size={len(Bset)} N={len(Ds)} D={Ds} -> {stat}")
        for c, v in checks:
            print(f"    [{'OK' if v else 'FAIL'}] {c}")
        print(f"    spectrum={spec}")
    print("OVERALL:", "PASS" if ok_all else "FAIL")
    sys.exit(0 if ok_all else 1)

if __name__ == "__main__":
    main()
