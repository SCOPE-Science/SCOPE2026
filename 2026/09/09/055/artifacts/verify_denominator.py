#!/usr/bin/env python3
"""Verifier: denominator lemma for C0: y^2 = x^6+3x^4-5x^2+7.

Claim: let x = a/b with coprime integers a,b, b > 0. Put
N(a,b) = a^6+3a^4b^2-5a^2b^4+7b^6, so that x satisfies y^2 = f(x) for some
y in Q iff N(a,b)/b^6 is a square in Q. Since b^6 = (b^3)^2 is a square in Q,
this holds iff N(a,b) is a square in Q; N(a,b) in Z then forces N(a,b) to be
a square in Z (if N = (u/v)^2 in lowest terms, v^2 divides 1, so v = 1).
We verify the congruence obstruction: if 4 does not divide b then N(a,b) is a
quadratic non-residue mod 4 or mod 8, hence not a square in Z. Conclusion: any
affine C(Q) point has 4 | b.

Checks (stdlib only, exact integer arithmetic):
  (A) q odd, p even  -> N = 3 mod 4 (non-QR).
  (B) both odd       -> N = 2 mod 4 (non-QR).
  (C) v2(q)=1,p odd  -> N = 5 mod 8 (non-QR, QR8={0,1,4}).
  (D) exhaustive: every (a,b) mod 8 with not-both-even and b%4!=0 is
      obstructed mod 4 or mod 8 (covers all 4∤b coprime lifts).
Exit 0 + VERIFY_OK iff all pass.
"""
import math

def Npq(a, b):
    return a**6 + 3*a**4*b*b - 5*a*a*b**4 + 7*b**6

def check_formulas():
    # A: b odd, a even, all residues mod 4
    for a in [0, 2, 4, 6]:
        for b in [1, 3, 5, 7]:
            assert Npq(a, b) % 4 == 3, (a, b)
    # B: both odd
    for a in [1, 3, 5, 7]:
        for b in [1, 3, 5, 7]:
            assert Npq(a, b) % 4 == 2, (a, b)
    # C: v2(b)=1 (b=2 mod 4 lifts), a odd -> 5 mod 8
    for a in [1, 3, 5, 7]:
        for b in [2, 6, 10, 14]:
            assert Npq(a, b) % 8 == 5, (a, b, Npq(a, b) % 8)
    # odd squares are 1 mod 8 (used in case C by hand proof)
    assert {(x*x) % 8 for x in range(8) if x % 2 == 1} == {1}
    print("formulas A/B/C over all residues OK")

def check_exhaustive():
    QR4 = {0, 1}
    QR8 = {0, 1, 4}
    unob = []
    for a in range(8):
        for b in range(8):
            if a % 2 == 0 and b % 2 == 0:
                continue  # not coprime at 2; lifts of coprime pairs never land here
            if b % 4 == 0:
                continue  # excluded conclusion case (4 | q residue)
            n = Npq(a, b)
            if n % 4 not in QR4 or n % 8 not in QR8:
                continue  # obstructed
            unob.append((a, b))
    assert unob == [], unob
    print("exhaustive mod-8: all 4∤b residue classes obstructed OK")

def check_squareness_logic():
    # sanity: residues 2,3 mod 4 and 5 mod 8 are indeed non-QR
    assert 2 not in {0, 1} and 3 not in {0, 1}
    assert 5 not in {0, 1, 4}
    # spot: N values at the three hand cases are non-squares over Z
    import math as m
    for a, b in [(0, 1), (1, 1), (1, 2)]:
        v = Npq(a, b)
        r = m.isqrt(v)
        assert r*r != v, (a, b, v)
    print("non-squareness sanity OK")

if __name__ == "__main__":
    check_formulas()
    check_exhaustive()
    check_squareness_logic()
    print("VERIFY_OK")
