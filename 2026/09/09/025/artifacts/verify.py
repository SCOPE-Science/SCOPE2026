"""Independent exact verifier for the Littlewood-Pisot census (stdlib only, except
numpy used SOLELY for initial center guesses, never trusted: every verdict is
settled by exact Fraction inequalities re-derived here from scratch).

Usage:
  python3 verify.py --pisot-only            # replay all stored Pisot records + phi comparison (fast)
  python3 verify.py --tally N A B           # re-derive classification for degree N, masks [A,B), assert vs stored tallies
  python3 verify.py --check-identity        # validate Chebyshev R,S tables via |P(i)|^2 identity on samples

Record semantics:
  E1 : P(1)==0 or P(-1)==0 -> unit-circle root -> NOT Pisot.
  G  : G=gcd(R,S) nontrivial; Gr separable part has m>=1 roots in (-1,1) (exact Sturm)
       -> P vanishes at e^{+-i arccos t0} -> NOT Pisot.
  D  : circle-free (G trivial, P(+-1)!=0) + Rouche disks (centers+RF re-derived or stored):
       L(z)=P(c0)+P'(c0)(z-c0), E=P-L, K=sum k(k-1)/2|p_k|(|c0|+RF)^{k-2},
       A1=|ReA|+|ImA|; REQUIRE B^2 RF^2 > (K RF^2+A1)^2  => exactly one root/disk.
       Disjointness + strict locations (|c0|^2 vs (1-/+RF)^2) + count==n => certified (N_in,N_out).
       Pisot additionally: one outside disk meeting real axis + Sturm count in (1,2)==1
       + bisection enclosure [lo,hi] with P(lo),P(hi) opposite nonzero signs.
"""
from fractions import Fraction
import json, sys

# ---------- exact polynomial helpers (lowest-first, Fractions) ----------
def pdeg(a):
    d = len(a) - 1
    while d > 0 and a[d] == 0:
        d -= 1
    return d

def pmod(A, B):
    A = [Fraction(x) for x in A]; B = [Fraction(x) for x in B]
    da, db = pdeg(A), pdeg(B)
    while not (da == 0 and A[0] == 0) and da >= db:
        c = A[da] / B[db]; s = da - db
        for i in range(db + 1):
            A[s + i] -= c * B[i]
        da = pdeg(A)
    while len(A) > 1 and A[-1] == 0:
        A.pop()
    return A

def pgcd(A, B):
    A = list(A); B = list(B)
    while not (pdeg(B) == 0 and B[0] == 0):
        A, B = B, pmod(A, B)
    d = pdeg(A); lc = A[d]
    return [Fraction(x) / lc for x in A[:d + 1]]

def pdiv(A, B):
    A = [Fraction(x) for x in A]; B = [Fraction(x) for x in B]
    da, db = pdeg(A), pdeg(B)
    if da < db:
        return None
    Q = [Fraction(0)] * (da - db + 1)
    while not (da == 0 and A[0] == 0) and da >= db:
        c = A[da] / B[db]; s = da - db; Q[s] = c
        for i in range(db + 1):
            A[s + i] -= c * B[i]
        da = pdeg(A)
    if da == 0 and A[0] == 0:
        return Q
    return None

def psub(a, b):
    n = max(len(a), len(b))
    A = list(a) + [Fraction(0)] * (n - len(a)); B = list(b) + [Fraction(0)] * (n - len(b))
    return [x - y for x, y in zip(A, B)]

def padd2(a, b):
    n = max(len(a), len(b))
    A = list(a) + [Fraction(0)] * (n - len(a)); B = list(b) + [Fraction(0)] * (n - len(b))
    return [x + y for x, y in zip(A, B)]

# Corrected Chebyshev: T_{k+1} = 2x T_k - T_{k-1}; U_{-1}=0,U_0=1,U_m=2xU_{m-1}-U_{m-2}
_TCH = [[Fraction(1)], [Fraction(0), Fraction(1)]]
for _k in range(1, 24):
    _TCH.append(psub(padd2([Fraction(0)] + list(_TCH[_k]), [Fraction(0)] + list(_TCH[_k])), _TCH[_k - 1]))
_UL = [[Fraction(0)], [Fraction(1)], [Fraction(0), Fraction(2)]]
for _k in range(2, 25):
    _UL.append(psub(padd2([Fraction(0)] + list(_UL[_k]), [Fraction(0)] + list(_UL[_k])), _UL[_k - 1]))

def RS_of(c):
    n = pdeg(c)
    R = [Fraction(0)] * (n + 1); S = [Fraction(0)] * max(n, 1)
    for k in range(n + 1):
        for i, v in enumerate(_TCH[k]):
            R[i] += Fraction(c[k]) * v
        if k >= 1:
            for i, v in enumerate(_UL[k]):
                if i < len(S):
                    S[i] += Fraction(c[k]) * v
                else:
                    S.append(Fraction(c[k]) * v)
    while len(R) > 1 and R[-1] == 0:
        R.pop()
    while len(S) > 1 and S[-1] == 0:
        S.pop()
    return R, S

def sval(P, x):
    r = Fraction(0)
    for a in reversed(P):
        r = r * x + a
    return r

def sturm_seq(P):
    P = [Fraction(x) for x in P]
    seq = [P, [(i + 1) * P[i + 1] for i in range(len(P) - 1)]]
    while not (pdeg(seq[-1]) == 0 and seq[-1][0] == 0):
        seq.append([-x for x in pmod(seq[-2], seq[-1])])
    return seq

def var_at(seq, x):
    prev = None; v = 0
    for P in seq:
        s = sval(P, x)
        if s == 0:
            continue
        cur = 1 if s > 0 else -1
        if prev is not None and cur != prev:
            v += 1
        prev = cur
    return v

def count_open(P, a, b):
    if pdeg(P) == 0:
        return 0
    assert sval(P, a) != 0 and sval(P, b) != 0
    seq = sturm_seq(P)
    return var_at(seq, a) - var_at(seq, b)

def gpowk(cx, cy, k):
    rr, ri = Fraction(1), Fraction(0)
    for _ in range(k):
        rr, ri = rr * cx - ri * cy, rr * cy + ri * cx
    return rr, ri

def check_disk(c, cx, cy, RF):
    """Exact Rouche check. Returns True iff disk provably holds exactly one root."""
    Are = Aim = Bre = Bim = Fraction(0)
    for k, a in enumerate(c):
        pr, pi = gpowk(cx, cy, k)
        Are += a * pr; Aim += a * pi
        if k >= 1:
            qr, qi = gpowk(cx, cy, k - 1)
            Bre += k * a * qr; Bim += k * a * qi
    Bn2 = Bre * Bre + Bim * Bim
    C0 = abs(cx) + abs(cy); CR = C0 + RF; K = Fraction(0)
    for k, a in enumerate(c):
        if k >= 2:
            K += Fraction(k * (k - 1), 2) * abs(a) * CR ** (k - 2)
    A1 = abs(Are) + abs(Aim); KR2 = K * RF * RF
    return Bn2 * RF * RF - (KR2 + A1) * (KR2 + A1) > 0

def classify_exact(c, centers=None):
    """Full exact classification. centers: optional list of (complex) guesses (untrusted)."""
    c = [Fraction(x) for x in c]; n = pdeg(c)
    P1 = sum(c); Pm1 = sum(a if j % 2 == 0 else -a for j, a in enumerate(c))
    if P1 == 0:
        return {"t": "E1", "z": 1}
    if Pm1 == 0:
        return {"t": "E1", "z": -1}
    R, S = RS_of(c)
    G = pgcd(R, S)
    if not (pdeg(G) == 0 and G[0] != 0):
        Gd = [(i + 1) * G[i + 1] for i in range(len(G) - 1)] if pdeg(G) >= 1 else [Fraction(0)]
        g2 = pgcd(G, Gd); Gr = pdiv(G, g2)
        assert Gr is not None
        if pdeg(Gr) >= 1 and sval(Gr, Fraction(-1)) != 0 and sval(Gr, Fraction(1)) != 0:
            m = count_open(Gr, Fraction(-1), Fraction(1))
            if m >= 1:
                return {"t": "G", "m": m}
    # Disk route
    import numpy as np
    rts = np.roots([float(x) for x in c[::-1]])
    dmin = min(abs(a - b) for i, a in enumerate(rts) for b in rts[i + 1:]) if n >= 2 else 2.0
    assert dmin > 1e-9, "roots too close; needs manual treatment"
    rho = min(1e-4, dmin / 4)
    gs = []
    for r in (centers if centers is not None else rts):
        z = complex(r)
        for _ in range(50):
            Pv = sum(float(a) * z ** k for k, a in enumerate(c))
            Dv = sum(float(k * a) * z ** (k - 1) for k, a in enumerate(c) if k >= 1)
            if Dv == 0 or abs(Pv) < 1e-14:
                break
            z = z - Pv / Dv
        gs.append(z)
    RF = Fraction(int(rho * 10 ** 12), 10 ** 12)
    for _ in range(8):
        disks = []
        ok = True
        for z in gs:
            cx = Fraction(z.real).limit_denominator(10 ** 15)
            cy = Fraction(z.imag).limit_denominator(10 ** 15)
            if not check_disk(c, cx, cy, RF):
                ok = False; break
            disks.append((cx, cy))
        if not ok:
            RF = RF / 10; continue
        dj = True
        for i in range(n):
            for j in range(i + 1, n):
                dx = disks[i][0] - disks[j][0]; dy = disks[i][1] - disks[j][1]
                if not (dx * dx + dy * dy > (2 * RF) * (2 * RF)):
                    dj = False; break
            if not dj:
                break
        if not dj:
            RF = RF / 10; continue
        locs = []; amb = False
        for (cx, cy) in disks:
            C2 = cx * cx + cy * cy
            if C2 < (1 - RF) * (1 - RF):
                locs.append("in")
            elif C2 > (1 + RF) * (1 + RF):
                locs.append("out")
            else:
                amb = True; break
        if amb:
            RF = RF / 10; continue
        rec = {"t": "D", "RF": str(RF), "nin": locs.count("in"), "nout": locs.count("out")}
        if rec["nout"] == 1 and rec["nin"] == n - 1:
            j = locs.index("out"); cx, cy = disks[j]
            if abs(cy) > RF:
                rec["pisot"] = False
            else:
                assert sum(c) != 0 and sum(a * (2 ** k) for k, a in enumerate(c)) != 0
                m = count_open(c, Fraction(1), Fraction(2))
                if m == 1:
                    lo = hi = None
                    lo, hi = Fraction(1), Fraction(2); flo = sval(c, lo)
                    for _ in range(80):
                        mid = (lo + hi) / 2
                        if (sval(c, mid) < 0) == (flo < 0):
                            lo = mid
                        else:
                            hi = mid
                    assert sval(c, lo) != 0 and sval(c, hi) != 0
                    assert (sval(c, lo) < 0) != (sval(c, hi) < 0)
                    rec.update(pisot=True, lo=str(lo), hi=str(hi),
                               cen=[(str(x), str(y)) for x, y in disks], loc=locs)
                else:
                    rec["pisot"] = False
        else:
            rec["pisot"] = False
        return rec
    raise AssertionError("rho adaptation stalled")

def replay_pisot_record(c, rec):
    """Replay a stored Pisot D-record using ONLY stored rationals (no numpy)."""
    c = [Fraction(x) for x in c]
    RF = Fraction(rec["RF"])
    disks = [(Fraction(x), Fraction(y)) for x, y in rec["cen"]]
    assert len(disks) == pdeg(c)
    for (cx, cy) in disks:
        assert check_disk(c, cx, cy, RF), "Rouche inequality FAILED"
    n = len(disks)
    for i in range(n):
        for j in range(i + 1, n):
            dx = disks[i][0] - disks[j][0]; dy = disks[i][1] - disks[j][1]
            assert dx * dx + dy * dy > (2 * RF) * (2 * RF), "overlap"
    locs = []
    for (cx, cy) in disks:
        C2 = cx * cx + cy * cy
        if C2 < (1 - RF) * (1 - RF):
            locs.append("in")
        elif C2 > (1 + RF) * (1 + RF):
            locs.append("out")
        else:
            raise AssertionError("disk straddles circle")
    assert locs == rec["loc"], (locs, rec["loc"])
    assert locs.count("out") == 1 and locs.count("in") == n - 1
    assert count_open(c, Fraction(1), Fraction(2)) == 1
    lo, hi = Fraction(rec["lo"]), Fraction(rec["hi"])
    assert sval(c, lo) != 0 and sval(c, hi) != 0
    assert (sval(c, lo) < 0) != (sval(c, hi) < 0)
    assert lo >= 1 and hi <= 2
    return True

def coeffs_of(n, mask):
    c = [0] * (n + 1); c[n] = 1
    for i in range(n):
        c[i] = -1 if (mask >> i) & 1 else 1
    return c

if __name__ == "__main__":
    from pathlib import Path
    HERE = Path(__file__).resolve().parent
    CENSUS = HERE / "census_le12.json"
    WIT = HERE / "pisot_13_14.json"
    mode = sys.argv[1]
    if mode == "--pisot-only":
        tab = json.load(open(CENSUS))
        houses_le12 = []
        for key, rec in tab["pisot_records"].items():
            n, mask = (int(x) for x in key.split("/"))
            c = coeffs_of(n, mask)
            assert replay_pisot_record(c, rec), key
            houses_le12.append((Fraction(rec["lo"]), Fraction(rec["hi"]), n, mask))
            print(f"OK Pisot n={n} mask={mask} house=[{float(Fraction(rec['lo'])):.10f},{float(Fraction(rec['hi'])):.10f}]")
        # degree-13 + degree-14 witness records (witness-only, no minimality claim there)
        wit = json.load(open(WIT))
        assert set(wit) == {"13/8191", "14/16383"}, set(wit)
        houses_hi = []
        for key, rec in wit.items():
            assert rec.get("pisot"), key
            n, mask = (int(x) for x in key.split("/"))
            c = coeffs_of(n, mask)
            assert replay_pisot_record(c, rec), key
            houses_hi.append((Fraction(rec["lo"]), Fraction(rec["hi"]), n, mask))
            print(f"OK Pisot n={n} mask={mask} house=[{float(Fraction(rec['lo'])):.10f},{float(Fraction(rec['hi'])):.10f}]")
        houses_le12.sort()
        lo0, hi0, n0, m0 = houses_le12[0]
        assert (n0, m0) == (2, 3), (n0, m0)
        for (lo, hi, n, m) in houses_le12[1:]:
            assert lo > hi0, (n, m)  # every other degree<=12 house strictly above phi's enclosure
        for (lo, hi, n, m) in houses_hi:
            assert lo > hi0, (n, m)  # witnesses lie above phi; no minimality claimed at 13/14
        print(f"MINIMALITY OK (degrees<=12): least house = degree-2 x^2-x-1, phi in [{float(lo0):.12f},{float(hi0):.12f}]; "
              f"{len(houses_le12)-1} other degree<=12 Pisot houses all strictly above; "
              f"{len(houses_hi)} degree-13/14 witnesses above, witness-only.")
        print("VERIFY_OK --pisot-only")
    elif mode == "--tally":
        N, A, B = (int(x) for x in sys.argv[2:5])
        tall = {"D": 0, "G": 0, "E1": 0, "F": 0}; pcnt = 0
        for mask in range(A, B):
            c = coeffs_of(N, mask)
            try:
                r = classify_exact(c)
            except AssertionError as e:
                tall["F"] += 1; print("FALLBACK", N, mask, e); continue
            tall[r["t"]] += 1
            if r.get("pisot"):
                pcnt += 1
                assert mask == 2 ** N - 1, (N, mask)
        print(f"TALLY n={N}[{A},{B}): {tall} pisot={pcnt}")
        # stored expectations
        exp = json.load(open(CENSUS))["tallies"].get(str(N))
        if exp and A == 0 and B == 2 ** N:
            assert tall == exp["records"], (tall, exp["records"])
            assert pcnt == exp["pisot"]
            print("TALLY MATCHES STORED CENSUS")
        print("VERIFY_OK --tally")
    elif mode == "--check-identity":
        # |P(i)|^2 = R(0)^2 + S(0)^2 with P(i) exact gaussian integer
        import itertools
        cnt = 0
        for n in range(1, 9):
            for mask in range(2 ** n):
                c = coeffs_of(n, mask)
                R, S = RS_of([Fraction(x) for x in c])
                # P(i): re = sum_{even} c_k i^k, im likewise
                re = sum(c[k] * (1 if (k // 2) % 2 == 0 else -1) for k in range(0, n + 1, 2))
                im = sum(c[k] * (1 if ((k - 1) // 2) % 2 == 0 else -1) for k in range(1, n + 1, 2))
                assert sval(R, Fraction(0)) ** 2 + sval(S, Fraction(0)) ** 2 == re * re + im * im, (n, mask)
                cnt += 1
        print(f"IDENTITY OK on {cnt} patterns")
        print("VERIFY_OK --check-identity")
