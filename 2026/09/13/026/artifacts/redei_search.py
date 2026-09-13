"""Redei triple symbol search + certificate builder (lane-1557).

Method (Redei/Stevenhagen, normalized):
 For ordered base pair (a,b) of distinct primes =1 mod 4 with (a/b)=+1, find
 primitive integers x>0,y,z with:
    x^2 - a*y^2 - b*z^2 = 0,  y even,  x - y = 1 mod 4   (=> beta:=x+y*sqrt(a)
    is 1 mod 4*O_{Q(sqrt a)} and totally positive).
 Then K = Q(sqrt a, sqrt b, sqrt beta) is the Redei D8 extension of Q for
 {a,b} (ramified only at a,b). For a third prime c with (a/c)=(b/c)=+1,
 let r^2 = a mod c; the Redei symbol is s = Legendre(x+y*r, c) in {+1,-1}.
"""
import json, math, itertools, sys

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def primes_1mod4(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = b"\x00" * ((limit - i * i) // i + 1)
    return [i for i in range(5, limit + 1) if sieve[i] and i % 4 == 1]

def solve_redei(a, b, ymax=4000, zmax=4000):
    """Find normalized (x,y,z). Search z odd, y even, increasing footprint."""
    import numpy as np
    ys = np.arange(2, ymax + 1, 2, dtype=np.int64)
    ay2 = a * ys * ys  # int64 safe: 5000*16e6=8e10 << 9e18
    sols = []
    for z in range(1, zmax + 1, 2):
        V = ay2 + b * z * z
        X = np.sqrt(V.astype(np.float64)).astype(np.int64)
        # fix possible float rounding: check X-1..X+1
        for dx in (-2, -1, 0, 1, 2):
            Xc = X + dx
            hit = (Xc * Xc == V) & (Xc > 0)
            idx = np.nonzero(hit)[0]
            for j in idx:
                y = int(ys[j]); x = int(Xc[j])
                if math.gcd(math.gcd(x, y), z) != 1:
                    continue
                if (x - y) % 4 != 1:
                    continue
                sols.append((x, y, z))
        if sols:
            # return the one with smallest (x+y+z) among this z? keep scanning
            # a bit for smaller x? just return minimal so far if z large enough
            if z > 50:
                sols.sort(key=lambda t: t[0] + t[1] + t[2])
                return sols[0]
    if sols:
        sols.sort(key=lambda t: t[0] + t[1] + t[2])
        return sols[0]
    return None

def sqrt_mod(a, p):
    a %= p
    for r in range(p):
        if (r * r - a) % p == 0:
            return r
    return None

def redei_symbol(a, b, c, sol):
    """sol = normalized (x,y,z) for ordered pair (a,b)."""
    x, y, z = sol
    r = sqrt_mod(a, c)
    assert r is not None, "c must split in Q(sqrt a)"
    s1 = legendre(x + y * r, c)
    r2 = (-r) % c
    s2 = legendre(x + y * r2, c)
    assert s1 != 0 and s2 != 0, "ramified: beta divisible by prime above c"
    assert s1 == s2, f"reciprocity inconsistency: {s1} vs {s2}"
    return s1

def main():
    primes = primes_1mod4(5000)
    print("n primes 1mod4 below 5000:", len(primes))
    # calibration on known triple
    sol = solve_redei(13, 61)
    print("calibration (13,61) sol:", sol)
    assert sol == (23, 6, 1) or sol is not None
    x, y, z = sol
    assert x*x - 13*y*y - 61*z*z == 0
    assert math.gcd(math.gcd(x,y),z) == 1 and y % 2 == 0 and (x-y) % 4 == 1
    s = redei_symbol(13, 61, 937, sol)
    print("calibration [13,61,937] =", s)
    assert s == -1, "must reproduce Borromean -1"

if __name__ == "__main__":
    main()
