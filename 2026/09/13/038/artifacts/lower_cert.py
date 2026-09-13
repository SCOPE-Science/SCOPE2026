"""Standalone certified LOWER bound: cap(E_3) >= 0.221 (Robin V <= -ln 0.221).

Trial measure: piecewise-uniform on 16 cells (each E_3 interval halved), exact rational
cells; symmetric weights: each of the 2 cells in mirror group g carries mass q_g/2000,
q = (210,130,111,123,111,89,93,133), sum 1000 -> total mass 1.
I(mu) = sum w_i w_j Phi_ij/(l_i l_j), Phi exact via phi(u) = -(u^2/2)ln|u| + 3u^2/4,
upper-bounded with certified prime-logarithm enclosures. V <= I(mu) gives cap >= e^-I.
"""
import math, sys
from fractions import Fraction as F

E3K = (0, 2, 6, 8, 18, 20, 24, 26)
LOWER_Q = (210, 130, 111, 123, 111, 89, 93, 133)
LOWER_GROUPS = ((0, 15), (1, 14), (2, 13), (3, 12), (4, 11), (5, 10), (6, 9), (7, 8))
LOWER_DEN = 2000
TOL = 45

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
        a, m, b = F(k, 27), F(2*k+1, 54), F(k+1, 27)
        cells += [(a, m), (m, b)]
    assert sum(LOWER_Q) == 1000
    w = [F(0)]*16
    for g, qq in zip(LOWER_GROUPS, LOWER_Q):
        for i in g:
            w[i] = F(qq, LOWER_DEN)
    assert sum(w) == 1
    need = set([1000, 221])
    for (a1, b1) in cells:
        for (a2, b2) in cells:
            for u in (b1-a2, a1-a2, b1-b2, a1-b2):
                if u != 0:
                    need.add(abs(u.numerator)); need.add(abs(u.denominator))
    need.discard(0); need.discard(1)
    primes_all = sieve(max(need))
    divprimes = set()
    for v in need:
        for p in factorize(v, primes_all):
            divprimes.add(p)
    primes = sorted(divprimes)
    print(f"certifying {len(primes)} primes...", flush=True)
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
    loA = ln_lo(1000)-ln_up(221); hiA = ln_up(1000)-ln_lo(221)
    print(f"A=-ln(0.221) in [{float(loA):.9f},{float(hiA):.9f}]", flush=True)
    ls = [b-a for (a, b) in cells]
    Ihi = F(0)
    for i, (a1, b1) in enumerate(cells):
        for j, (a2, b2) in enumerate(cells):
            const = F(0)
            terms = []
            for sgn, u in ((+1, b1-a2), (-1, a1-a2), (-1, b1-b2), (+1, a1-b2)):
                if u == 0:
                    continue
                const += sgn*F(3)*u*u/4
                c = -(u*u)/2
                p, q = abs(u.numerator), abs(u.denominator)
                terms.append((sgn*c, p)); terms.append((sgn*(-c), q))
            e = const
            for c, nn in terms:
                e += c*(ln_up(nn) if c > 0 else ln_lo(nn))
            Ihi += w[i]*w[j]*e/(ls[i]*ls[j])
    print(f"LOWER: certified I(mu) <= {float(Ihi):.9f}; need < {float(loA):.9f}")
    ok = Ihi < loA
    print("LOWER:", "PASS" if ok else "FAIL",
          f"=> cap(E3) >= {math.exp(-float(Ihi)):.7f} (need >= 0.221)")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
