"""Exact-rational (stdlib Fractions only) verifier for lane-275.

Replays from the definitional Jacobi sum (DLMF 18.5.7):
  P_n^{(a,b)}(x) = sum_{k=0}^n (-n)_k (n+a+b+1)_k/(k! k!) * ((1-x)/2)^k
at n=6, a=0, b in {-19/10,-17/10,-3/2,-13/10,-11/10} and b+2.

Checks:
  (S) endpoint signs nonzero + opposite on every bracket (IVT),
  (T) Sturm count exactly 1 on each bracket, 6 total (completeness),
      full-rank degree chain 6,5,4,3,2,1,0,
  (H) HOLD endpoint chains at beta=-3/2,-13/10,-11/10,
  (B) BREAK witnesses at beta=-19/10,-17/10 (Sturm Y-count 0 on J),
  (M) sub-(-1) enclosure: exactly one X zero below -1 at every beta.
"""
from fractions import Fraction
from math import factorial, comb

N = 6
A = Fraction(0)
BETAS = [Fraction(-19, 10), Fraction(-17, 10), Fraction(-15, 10),
         Fraction(-13, 10), Fraction(-11, 10)]

BR = {
    (Fraction(-19, 10), "X"): [("-2043/2000", "-1021/1000"), ("-961/1000", "-1921/2000"),
        ("-569/1000", "-1137/2000"), ("-2/125", "-31/2000"),
        ("133/250", "213/400"), ("181/200", "1811/2000")],
    (Fraction(-19, 10), "Y"): [("-37/40", "-1849/2000"), ("-1297/2000", "-81/125"),
        ("-451/2000", "-9/40"), ("31/125", "497/2000"),
        ("333/500", "1333/2000"), ("933/1000", "1867/2000")],
    (Fraction(-17, 10), "X"): [("-2051/2000", "-41/40"), ("-1839/2000", "-919/1000"),
        ("-21/40", "-1049/2000"), ("19/1000", "39/2000"),
        ("1101/2000", "551/1000"), ("1817/2000", "909/1000")],
    (Fraction(-17, 10), "Y"): [("-1819/2000", "-909/1000"), ("-623/1000", "-249/400"),
        ("-399/2000", "-199/1000"), ("267/1000", "107/400"),
        ("27/40", "1351/2000"), ("187/200", "1871/2000")],
    (Fraction(-15, 10), "X"): [("-511/500", "-2043/2000"), ("-221/250", "-1767/2000"),
        ("-967/2000", "-483/1000"), ("103/2000", "13/250"),
        ("567/1000", "227/400"), ("73/80", "913/1000")],
    (Fraction(-15, 10), "Y"): [("-447/500", "-1787/2000"), ("-299/500", "-239/400"),
        ("-7/40", "-349/2000"), ("57/200", "571/2000"),
        ("1367/2000", "171/250"), ("937/1000", "15/16")],
    (Fraction(-13, 10), "X"): [("-203/200", "-2029/2000"), ("-1701/2000", "-17/20"),
        ("-89/200", "-889/2000"), ("41/500", "33/400"),
        ("233/400", "583/1000"), ("1831/2000", "229/250")],
    (Fraction(-13, 10), "Y"): [("-439/500", "-351/400"), ("-287/500", "-1147/2000"),
        ("-303/2000", "-151/1000"), ("151/500", "121/400"),
        ("173/250", "277/400"), ("1877/2000", "939/1000")],
    (Fraction(-11, 10), "X"): [("-2011/2000", "-201/200"), ("-1637/2000", "-409/500"),
        ("-817/2000", "-51/125"), ("221/2000", "111/1000"),
        ("597/1000", "239/400"), ("1837/2000", "919/1000")],
    (Fraction(-11, 10), "Y"): [("-431/500", "-1723/2000"), ("-11/20", "-1099/2000"),
        ("-257/2000", "-16/125"), ("159/500", "637/2000"),
        ("7/10", "1401/2000"), ("1881/2000", "941/1000")],
}


def jacobi_coeffs(n, a, b):
    cz = []
    for k in range(n + 1):
        neg = ((-1) ** k) * factorial(n) // factorial(n - k)
        rising = Fraction(1, 1)
        base = Fraction(n, 1) + a + b + 1
        for j in range(k):
            rising *= (base + j)
        ck = Fraction(neg, 1) * rising / (Fraction(factorial(k), 1) * Fraction(factorial(k), 1))
        cz.append(ck)
    cx = [Fraction(0)] * (n + 1)
    for k, ck in enumerate(cz):
        for i in range(k + 1):
            cx[i] += ck * Fraction(comb(k, i), 2 ** k) * ((-1) ** i)
    return cx


def peval(c, x):
    r = Fraction(0)
    for cc in reversed(c):
        r = r * x + cc
    return r


def pdeg(c):
    d = len(c) - 1
    while d > 0 and c[d] == 0:
        d -= 1
    return d


def prem(a, b):
    a = list(a)
    da = pdeg(a)
    db = pdeg(b)
    if da < db:
        return a[:da + 1]
    while da >= db:
        coeff = a[da] / b[db]
        for i in range(db + 1):
            a[da - db + i] -= coeff * b[i]
        da = pdeg(a)
        if da == 0 and a[0] == 0:
            return [Fraction(0)]
    return a[:da + 1]


def pderiv(c):
    return [Fraction(i) * c[i] for i in range(1, len(c))]


def sturm(c):
    seq = [list(c), pderiv(c)]
    while True:
        r = prem(seq[-2], seq[-1])
        if all(v == 0 for v in r):
            break
        seq.append([-v for v in r])
        if pdeg(seq[-1]) == 0:
            break
    return seq


def varcount(seq, x):
    signs = []
    for p in seq:
        if x == "pinf":
            v = p[pdeg(p)]
        elif x == "ninf":
            v = p[pdeg(p)] * ((-1) ** pdeg(p))
        else:
            v = peval(p, x)
        signs.append(0 if v == 0 else (1 if v > 0 else -1))
    nz = [s for s in signs if s != 0]
    return sum(1 for i in range(len(nz) - 1) if nz[i] != nz[i + 1])


def main():
    fails = []
    polys = {}
    for b in BETAS:
        for tag, bb in (("X", b), ("Y", b + 2)):
            c = jacobi_coeffs(N, A, bb)
            polys[(b, tag)] = c
            seq = sturm(c)
            degs = [pdeg(p) for p in seq]
            if degs != [6, 5, 4, 3, 2, 1, 0]:
                fails.append((str(b), tag, "degree chain", degs))
            tot = varcount(seq, "ninf") - varcount(seq, "pinf")
            if tot != 6:
                fails.append((str(b), tag, "total roots", tot))
            for lo_s, hi_s in BR[(b, tag)]:
                lo, hi = Fraction(lo_s), Fraction(hi_s)
                va, vb = peval(c, lo), peval(c, hi)
                if va == 0 or vb == 0 or va * vb >= 0:
                    fails.append((str(b), tag, "sign", (lo_s, hi_s)))
                    continue
                if varcount(seq, lo) - varcount(seq, hi) != 1:
                    fails.append((str(b), tag, "sturm1", (lo_s, hi_s)))
            pts = [Fraction(s) for p in BR[(b, tag)] for s in p]
            if not all(pts[i] < pts[i + 1] for i in range(len(pts) - 1)):
                fails.append((str(b), tag, "disjoint-order", None))
    # HOLD chains
    for b in (Fraction(-15, 10), Fraction(-13, 10), Fraction(-11, 10)):
        xs = [Fraction(s) for p in BR[(b, "X")] for s in p]
        ys = [Fraction(s) for p in BR[(b, "Y")] for s in p]
        chain = [xs[0], xs[1], ys[0], ys[1], xs[2], xs[3], ys[2], ys[3],
                 xs[4], xs[5], ys[4], ys[5], xs[6], xs[7], ys[6], ys[7],
                 xs[8], xs[9], ys[8], ys[9], xs[10], xs[11], ys[10]]
        if not all(chain[i] < chain[i + 1] for i in range(len(chain) - 1)):
            fails.append((str(b), "HOLD", "chain", None))
    # BREAK witnesses: J = [X1_lo, X2_hi] holds 2 X zeros, 0 Y zeros
    for b in (Fraction(-19, 10), Fraction(-17, 10)):
        cx, cy = polys[(b, "X")], polys[(b, "Y")]
        sx, sy = sturm(cx), sturm(cy)
        x1 = [Fraction(s) for s in BR[(b, "X")][0]]
        x2 = [Fraction(s) for s in BR[(b, "X")][1]]
        y1lo = Fraction(BR[(b, "Y")][0][0])
        a, cc = x1[0], x2[1]
        if not y1lo > cc:
            fails.append((str(b), "BREAK", "y1lo>x2hi", None))
        if peval(cy, a) == 0 or peval(cy, cc) == 0:
            fails.append((str(b), "BREAK", "Y-endpoint-nonzero", None))
        if varcount(sy, a) - varcount(sy, cc) != 0:
            fails.append((str(b), "BREAK", "Y-count-0", varcount(sy, a) - varcount(sy, cc)))
        if varcount(sx, a) - varcount(sx, cc) != 2:
            fails.append((str(b), "BREAK", "X-count-2", varcount(sx, a) - varcount(sx, cc)))
    # sub-(-1): exactly one X zero below -1
    for b in BETAS:
        xs = [Fraction(s) for p in BR[(b, "X")] for s in p]
        if not (xs[1] < Fraction(-1) < xs[2]):
            fails.append((str(b), "sub-1", "x1hi<-1<x2lo", None))
    if fails:
        print("VERIFY_FAIL")
        for f in fails:
            print(f)
        raise SystemExit(1)
    print("VERIFY_OK")
    print("totals: 10 polys x 6 roots; HOLD at -3/2,-13/10,-11/10; BREAK at -19/10,-17/10")
    for b in BETAS:
        d = Fraction(-1, 1) - Fraction(2) * (b + 1) / (b + 14)
        print("beta", b, "delta", d, float(d))


if __name__ == "__main__":
    main()
