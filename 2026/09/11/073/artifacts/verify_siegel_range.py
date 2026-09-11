"""Finite-range exact-integer audit for the Siegel/transfer constants.

Covers every integer q in [3, 40000):
  (S) A(q) = least A >= 1 with (2A+1)^3 > 6*A*P(q)+1, P(q) = floor(8q/5)+2;
  (C) with H = 2*A(q) and K = 385/100: 4*K^4*H^6 <= 250000*q^3
      (i.e. q/(2*K^2*H^3) >= 1/(500*sqrt(q))), checked as
      4*385^4*H^6 <= 250000*q^3*100^4 in exact integers.

The large-q tail (q >= 40000) is proved analytically in DRAFT.md:
A(q) <= ceil(1.12*sqrt(q))+1 via the all-positive-coefficient polynomial F,
and 2*(77/20)^2*(2.26)^3 <= 500 (integer check T8 below).

Stdlib only. Run: python3 verify_siegel_range.py  (takes ~1 s)
"""
import math
import time

K4 = 385 ** 4
D = 100 ** 4


def min_siegel_A(q):
    P = (8 * q) // 5 + 2
    A = 1
    while (2 * A + 1) ** 3 <= 6 * A * P + 1:
        A += 1
    return A


def main():
    t = time.time()
    n = 0
    for q in range(3, 40000):
        A = min_siegel_A(q)
        H = 2 * A
        assert (2 * A + 1) ** 3 > 6 * A * ((8 * q) // 5 + 2) + 1
        assert 4 * K4 * H ** 6 <= 250000 * (q ** 3) * D, (q, A, H)
        n += 1
    # tail anchor used by the analytic argument
    assert 2 * 5929 * 226 ** 3 <= 2 * 10 ** 11  # 2K^2(2.26)^3<=500, K=77/20
    print("SIEGEL_RANGE_OK  checked=%d  (%.1fs)" % (n, time.time() - t))


if __name__ == "__main__":
    main()
