"""Standalone certified UPPER bound: cap(E_3) <= 0.230 via Frostman minimum principle.

Trial measure: piecewise-uniform on 96 exact rational cells (literal rounded-cosine mesh),
symmetric rational weights from upper_weights.json (mirror pairs, total mass 1).
For probe [xl,xr] and cell (a,b), h(x) = (a-x)ln|a-x| - (b-x)ln|b-x| is enclosed by
PAIRED evaluation: s=(a-x) in [s0,s1], h=g(s)-g(s+l), g(t)=t ln|t|; h'(s)=ln|s|-ln|s+l|
vanishes only at s=-l/2 with singularities only at s in {-l,0}; splitting at
{-l,-l/2,0} makes h strictly monotone on each subpiece, so the range minimum is the
minimum over split-point values, each enclosed with certified prime-logarithm bounds.
U(x) = 1 + sum_j w_j h_j(x)/l_j; min over probes lower-bounds min_E U; cap <= exp(-minU).
All arithmetic exact (Fraction); ln certified via atanh series + geometric remainder.
"""
import math, sys, json, os
from fractions import Fraction as F

E3K = (0, 2, 6, 8, 18, 20, 24, 26)
R = [0, 29, 116, 253, 432, 640, 864, 1088, 1296, 1475, 1612, 1699, 1728]
UPPER_DEN = 200000
TOL = 45
S = 40

def sieve(n):
    bs = bytearray(b"\x01")*(n+1)
    bs[0:2] = b"\x00\x00"
    for p in range(2, int(n**0.5)+1):
        if bs[p]:
            bs[p*p:n+1:p] = b"\x00"*(((n - p*p)//p)+1)
    return [p for p in range(2, n+1) if bs[p]]

def factorize(n, primes):
    out = {}
    r = n
    for p in primes:
        if p*p > r:
            break
        if r % p == 0:
            e = 0
            while r % p == 0:
                r //= p; e += 1
            out[p] = e
    if r > 1:
        out[r] = out.get(r, 0) + 1
    return out

_ln2 = {}
def cert_ln2(tol):
    if tol in _ln2:
        return _ln2[tol]
    z = F(1, 3)
    N = 0
    while True:
        N += 1
        if z**(2*N+1)/((2*N+1)*(1-z*z)) < F(1, 2**tol):
            break
    s = sum(z**(2*k+1)/(2*k+1) for k in range(N))
    v = (2*s, 2*(s + z**(2*N+1)/((2*N+1)*(1-z*z))))
    _ln2[tol] = v
    return v

def cert_ln_int(n, tol):
    assert isinstance(n, int) and n >= 1
    if n == 1:
        return F(0), F(0)
    k = 0
    m = F(n, 1)
    while m >= 2:
        m /= 2; k += 1
    z = (m-1)/(m+1)
    N = 0
    while True:
        N += 1
        rem = z**(2*N+1)/((2*N+1)*(1-z*z)) if z > 0 else F(0)
        if rem < F(1, 2**tol):
            break
    s = sum(z**(2*k+1)/(2*k+1) for k in range(N)) if z > 0 else F(0)
    rr = (z**(2*N+1)/((2*N+1)*(1-z*z)) if z > 0 else F(0))
    lo2, hi2 = cert_ln2(tol)
    return 2*s + k*lo2, 2*(s+rr) + k*hi2

def main():
    cells = []
    for k in E3K:
        a = F(k, 27); l = F(1, 27)
        pts = [a + l*F(r, 1728) for r in R]
        for s in range(12):
            assert pts[s+1] > pts[s]
            cells.append((pts[s], pts[s+1]))
    N = len(cells)
    assert N == 96
    qpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "upper_weights.json")
    with open(qpath) as f:
        Q = json.load(f)["q"]
    assert sum(Q) == UPPER_DEN and len(Q) == N//2
    wu = [F(0)]*N
    for r in range(N//2):
        wu[r] = wu[N-1-r] = F(Q[r], UPPER_DEN*2)
    assert sum(wu) == 1, sum(wu)

    probes = []
    for k in E3K:
        a = F(k, 27); h = F(1, 27*S)
        for s in range(S):
            probes.append((a+s*h, a+(s+1)*h))
    cpts = set()
    for (a, b) in cells:
        cpts.add(a); cpts.add(b)
    refined = []
    for (xl, xr) in probes:
        inside = sorted(c for c in cpts if xl < c < xr)
        pts = [xl] + inside + [xr]
        for t in range(len(pts)-1):
            refined.append((pts[t], pts[t+1]))
    print(f"probes: {len(refined)}", flush=True)

    # collect integers that actually appear (split points s, s+l, thresholds)
    need = set([100, 23])
    sched = []
    for (xl, xr) in refined:
        for (a, b) in cells:
            l = b - a
            s0, s1 = a - xr, a - xl
            P = {s0, s1}
            for p in (-l, -l/2, F(0)):
                if s0 <= p <= s1:
                    P.add(p)
            P = sorted(P)
            sched.append((l, P))
            for s in P:
                for t in (s, s+l):
                    if t != 0:
                        at = abs(t)
                        need.add(at.numerator); need.add(at.denominator)
    need.discard(0); need.discard(1)
    primes_all = sieve(max(need))
    divprimes = set()
    for v in need:
        for p in factorize(v, primes_all):
            divprimes.add(p)
    primes = sorted(divprimes)
    print(f"certifying {len(primes)} primes from {len(need)} ints...", flush=True)
    PL = {p: cert_ln_int(p, TOL) for p in primes}
    FAC = {}
    def fac(n):
        if n not in FAC:
            FAC[n] = factorize(n, primes_all)
        return FAC[n]
    def ln_up(n):
        return F(0) if n == 1 else sum(e*PL[p][1] for p, e in fac(n).items())
    def ln_lo(n):
        return F(0) if n == 1 else sum(e*PL[p][0] for p, e in fac(n).items())
    def g_pt(s):
        if s == 0:
            return F(0), F(0)
        at = abs(s); p, q = at.numerator, at.denominator
        lo_ln = ln_lo(p)-ln_up(q); hi_ln = ln_up(p)-ln_lo(q)
        if s > 0:
            return s*lo_ln, s*hi_ln
        return s*hi_ln, s*lo_ln

    loB = ln_lo(100)-ln_up(23); hiB = ln_up(100)-ln_lo(23)
    print(f"B=-ln(0.230) in [{float(loB):.9f},{float(hiB):.9f}]", flush=True)

    idx = 0
    min_lo = None
    for (xl, xr) in refined:
        tot = F(1)
        for (a, b), wj in zip(cells, wu):
            l = b - a
            s0, s1 = a - xr, a - xl
            P = {s0, s1}
            for p in (-l, -l/2, F(0)):
                if s0 <= p <= s1:
                    P.add(p)
            best = None
            for s in P:
                lo1, hi1 = g_pt(s)
                lo2, hi2 = g_pt(s+l)
                val = lo1 - hi2
                if best is None or val < best:
                    best = val
            tot += wj*best/l
        if min_lo is None or tot < min_lo:
            min_lo = tot
        idx += 1
        if idx % 128 == 0:
            print(f"  {idx}/{len(refined)} min_so_far={float(min_lo):.6f}", flush=True)
    print(f"UPPER: certified min_E U >= {float(min_lo):.9f}; need > {float(hiB):.9f}")
    ok = min_lo > hiB
    print("UPPER:", "PASS" if ok else "FAIL",
          f"=> cap(E3) <= {math.exp(-float(min_lo)):.7f} (need <= 0.230)")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
