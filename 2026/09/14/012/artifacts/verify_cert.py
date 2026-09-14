"""Verify the dVLP alternation certificate with exact rational arithmetic.

Candidate: R(x) = P(t)/Q(t), t = x^2,
  P(t) = 0.279088 - 2.074492 t + 4.253844 t^2,
  Q(t) = 1 - 1.309050 t + 3.719230 t^2.
Checks: Q > 0 on [0,1]; error f2 - R alternates at 11 nodes with |e| > 0.025.
Run: python3 output/artifacts/verify_cert.py
"""
from fractions import Fraction

A0 = Fraction(279088, 10**6)
A1 = Fraction(-2074492, 10**6)
A2 = Fraction(4253844, 10**6)
B1 = Fraction(-1309050, 10**6)
B2 = Fraction(3719230, 10**6)
RHO = Fraction(1, 40)  # 0.025 > threshold 0.02

NODES = [Fraction(-1), Fraction(-856, 1000), Fraction(-622, 1000),
         Fraction(-1, 2), Fraction(-369, 1000), Fraction(0),
         Fraction(369, 1000), Fraction(1, 2), Fraction(622, 1000),
         Fraction(856, 1000), Fraction(1)]


def err_at(x):
    t = x * x
    P = A0 + A1 * t + A2 * t * t
    Q = 1 + B1 * t + B2 * t * t
    f = abs(t - Fraction(1, 4))
    return f - P / Q, Q


def main():
    # Q positivity on [0,1]: parabola vertex inside, minimum value > 0.
    tstar = -B1 / (2 * B2)
    assert Fraction(0) < tstar < Fraction(1), tstar
    qmin = 1 + B1 * tstar + B2 * tstar * tstar
    assert qmin > Fraction(4, 5), qmin
    assert 1 + B1 + B2 > 0 and Fraction(1) > 0
    print("Qmin =", float(qmin), "> 0.8: Q positive on [0,1]")

    prev = 0
    for x in NODES:
        e, Q = err_at(x)
        assert Q > 0, (x, Q)
        assert abs(e) > RHO, (x, e)
        s = 1 if e > 0 else -1
        assert prev == 0 or s == -prev, (x, e)
        prev = s
        print(f"x={float(x):+.3f} err={float(e):+.7f} sgn={s:+d} OK")
    print("CERTIFICATE VERIFIED: 11-point alternation, rho=0.025")


if __name__ == "__main__":
    main()
