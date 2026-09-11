"""Exact integer/rational audit of the closed-form inequalities in DRAFT.md.

(T1) 126^3 > 2*10^6                       (theta < 1.26)
(T2) 1259^3 < 2*10^9 < 1260^3             (1.259 < theta < 1.26)
(T3) 10000+12600+15876 <= 38500           (K = 1+theta+theta^2 <= 77/20)
(T4) 77^4 <= 16*10^7                       (Dani dual ledger: K^4 <= 1000)
(T5) 63^3 > 500^2                         (Dani simultaneous ledger, delta = 1/63)
(T6) 259*500 >= 1000                      (q=1 case: theta-1 > 0.259 >= 1/500)
(T7) det(mult-matrix) == norm formula: hand expansion in DRAFT.md + 500
       random-triple symbolic cross-check below
(T8) 2*5929*226^3 <= 2*10^11              (large-q tail: 2K^2(2.26)^3 <= 500)
(T9) F polynomial coefficients positive   (Siegel tail: F(s) > 0 for all s >= 0)

Stdlib only. Run: python3 verify_integers.py
"""
import random


def check(name, cond, detail=""):
    print(("PASS" if cond else "FAIL") + "  " + name + "  " + detail)
    assert cond, name


check("T1: 126^3 > 2*10^6", 126**3 > 2 * 10**6, str(126**3))
check("T2a: 1259^3 < 2*10^9", 1259**3 < 2 * 10**9, str(1259**3))
check("T2b: 1260^3 > 2*10^9", 1260**3 > 2 * 10**9, str(1260**3))
check("T3: K <= 77/20", 10000 + 12600 + 15876 <= 38500, "38476 <= 38500")
check("T4: dual Dani K^4<=1000", 77**4 <= 16 * 10**7,
      "%d <= %d" % (77**4, 16 * 10**7))
check("T5: simultaneous Dani delta 1/63", 63**3 > 500**2,
      "%d > %d" % (63**3, 500**2))
check("T6: q=1 case", 259 * 500 >= 1000, "129500 >= 1000")

random.seed(20260911)
n = 0
for _ in range(500):
    a = random.randint(-12, 12)
    b = random.randint(-12, 12)
    c = random.randint(-12, 12)
    det = (a * (a * a - 2 * c * b) - 2 * c * (b * a - 2 * c * c)
           + 2 * b * (b * b - a * c))
    form = a**3 + 2 * b**3 + 4 * c**3 - 6 * a * b * c
    assert det == form, (a, b, c, det, form)
    n += 1
print("PASS  T7: det==norm-formula on %d random triples" % n)

check("T8: tail 2K^2(2.26)^3<=500", 2 * 5929 * 226**3 <= 2 * 10**11,
      "%d <= %d" % (2 * 5929 * 226**3, 2 * 10**11))
# F(s) = 0.487424 s^3 + 25.9584 s^2 + 47.04 s + 2 (exact decimal expansion of
# (2.24s+3)^3 - 6(1.12s+2)(1.6s^2+2) - 1); verify scaled-integer coefficients.
c3 = 11239424 - 10752000
c2 = 45158400 - 19200000
c1 = 60480000 - 13440000
c0 = 27000000 - 24000000 - 1000000
check("T9: F coeffs positive", c3 > 0 and c2 > 0 and c1 > 0 and c0 > 0,
      "%d %d %d %d" % (c3, c2, c1, c0))

print("ALL_INTEGER_CHECKS_OK")
