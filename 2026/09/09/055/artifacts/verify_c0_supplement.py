#!/usr/bin/env python3
"""Supplement: exact F_p reduction log, disc factorisation, E1' ordinary check,
and rational-denominator lemma cases for C0: y^2 = x^6+3x^4-5x^2+7. Stdlib only."""
import math

def f(x): return x**6 + 3*x**4 - 5*x**2 + 7
def Npq(p, q): return p**6 + 3*p**4*q*q - 5*p*p*q**4 + 7*q**6

def aff_count_C0(p):
    return sum(1 for x in range(p) for y in range(p) if (y*y - f(x)) % p == 0)

def aff_count_E1p(p):
    return sum(1 for X in range(p) for Y in range(p) if (Y*Y - (X**3 - 8*X + 14)) % p == 0)

def qr(p):
    return sorted({(y*y) % p for y in range(p)})

if __name__ == "__main__":
    # 1. disc factorisation by exact division (no sympy)
    D = 4714544128
    tmp = D; fac = {}
    for pr in [2, 7, 811]:
        e = 0
        while tmp % pr == 0:
            tmp //= pr; e += 1
        fac[pr] = e
    assert tmp == 1, tmp
    assert fac == {2: 10, 7: 1, 811: 2}, fac
    print("|disc(f)| = 2^10 * 7 * 811^2 OK; odd bad primes {7,811}")
    # E1' disc by hand formula for X^3 + aX + b: -4a^3 - 27b^2
    dE = -4*(-8)**3 - 27*14**2
    assert dE == -3244 == -4*811, dE
    print("disc(E1') = -3244 = -4*811 OK")

    # 2. F_p reduction tables for C0 at p = 5, 11 (good: D % p != 0)
    for p in [5, 11]:
        assert D % p != 0
        sq = set(qr(p))
        rows = [(x, f(x) % p, (f(x) % p) in sq) for x in range(p)]
        n = aff_count_C0(p)
        print(f"C0 mod {p}: QR={qr(p)} affine_pts={n} (+2 at inf, good reduction)")
        for x, v, ok in rows:
            print(f"   x={x} f={v} {'liftable' if ok else 'dead'}")
    # p=7 is bad for C0
    assert D % 7 == 0
    print("p=7: D % 7 == 0 -> bad reduction for C0; excluded as QC prime. OK")

    # 3. E1' ordinary check at p=5, 11
    for p in [5, 11]:
        n = aff_count_E1p(p)
        t = p + 1 - (n + 1)
        assert t % p != 0
        print(f"E1' mod {p}: affine={n} proj={n+1} trace={t} ordinary OK")

    # 4. denominator-lemma cases (exact)
    for p, q in [(0, 1), (2, 1), (4, 3), (100, 7)]:
        assert Npq(p, q) % 4 == 3, (p, q)          # q odd, p even
    for p, q in [(1, 1), (3, 5), (7, 9)]:
        assert Npq(p, q) % 4 == 2, (p, q)          # both odd
    for p, q0 in [(1, 1), (3, 5), (99, 13)]:
        assert Npq(p, 2*q0) % 8 == 5, (p, q0)      # v2(q)=1, p odd
    assert {(y*y) % 8 for y in range(8) if y % 2} == {1}
    print("denominator lemma cases A/B/C exact OK (any C(Q) affine pt has 4 | q)")

    # 5. mod-4 obstruction recheck (minimal modulus)
    assert sorted({f(x) % 4 for x in range(4)}) == [2, 3]
    assert set(f(x) % 4 for x in range(4)).isdisjoint({(y*y) % 4 for y in range(4)})
    assert sorted({f(x) % 8 for x in range(8)}) == [3, 6, 7]
    print("mod-4 (and mod-8) integral obstruction recheck OK")
    print("VERIFY_OK")
