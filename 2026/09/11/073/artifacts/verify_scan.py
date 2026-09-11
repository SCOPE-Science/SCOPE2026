"""Numeric sup-norm scan for the cubic pair (2^{1/3}, 2^{2/3}).

For each 1 <= q <= Q (default 200000) computes
    R(q) = sqrt(q) * max(||q*2^{1/3}||, ||q*2^{2/3}||)
and checks R(q) >= 1/500 (zero violations expected, with large margin).

Standard-library only. Run: python3 verify_scan.py [Q]
"""
import math
import sys

C0 = 1 / 500


def main(Q=200000):
    th = 2 ** (1 / 3)
    th2 = th * th
    worst = (None, float("inf"))
    viol = 0
    for q in range(1, Q + 1):
        e1 = abs(q * th - round(q * th))
        e2 = abs(q * th2 - round(q * th2))
        r = math.sqrt(q) * max(e1, e2)
        if r < worst[1]:
            worst = (q, r)
        if r < C0:
            viol += 1
    print(f"Q={Q} worst q={worst[0]} R={worst[1]:.6f} "
          f"margin_vs_1/500={worst[1] / C0:.2f}x violations={viol}")
    assert viol == 0, "unexpected violation of the 1/500 bound"
    assert worst[1] > 0.2, "margin unexpectedly small"
    print("SCAN_OK")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 200000)
