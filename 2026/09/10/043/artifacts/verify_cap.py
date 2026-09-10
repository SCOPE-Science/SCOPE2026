"""Exact-integer verification of the Evra-Kaufman certificate cap at d=3.

Checks (stdlib only, no numpy):
  C0 = 1/960 exactly; C1 = 160 exactly.
  eps_bar(beta) = (1/3)(beta/160)^d <= (1/3)(2/160)^3 = 1/1536000 for beta<=2.
  mu(beta) = (C0 (beta/160)^d)^{16} <= (1/491520000)^{16} < 10^{-139} < 0.08.
  Monotonicity: both bounds are increasing in beta on [0,2].
"""
from fractions import Fraction


def max_caps(d=3, beta_max=Fraction(2)):
    C0 = Fraction(1, 3 * (d + 2) * 2 ** (d + 3))
    C1 = (d + 2) * 2 ** (d + 2)
    assert C0 == Fraction(1, 960) and C1 == 160, (C0, C1)
    eps_bar_max = Fraction(1, 3) * (beta_max / C1) ** d
    mu_max = (C0 * (beta_max / C1) ** d) ** (2 ** (d + 1))
    return C0, C1, eps_bar_max, mu_max


def main():
    C0, C1, ebar, mu = max_caps()
    print("C0 =", C0, " C1 =", C1)
    print("eps_bar_max =", ebar, "=", float(ebar))
    print("mu_max = (1/491520000)^16 ; log10 =", __import__("math").log10(float(ebar * 0 + 1)) if False else "(see below)")
    # exact comparisons
    assert ebar == Fraction(1, 1536000), ebar
    assert ebar < Fraction(8, 100), "must be < 0.08"
    assert mu == (Fraction(1, 491520000)) ** 16, mu
    assert mu < Fraction(1, 10 ** 139), "mu < 1e-139"
    assert mu < Fraction(8, 100), "mu < 0.08"
    # monotonicity spot-checks (exact): beta=1 and beta=1/2 give smaller values
    for b in (Fraction(1), Fraction(1, 2)):
        e = Fraction(1, 3) * (b / 160) ** 3
        m = (Fraction(1, 960) * (b / 160) ** 3) ** 16
        assert e <= ebar and m <= mu, (b, e, m)
    print("VERIFY_OK: EK d=3 caps are eps_bar<=1/1536000<0.08 and mu=(1/491520000)^16<1e-139<0.08")


if __name__ == "__main__":
    main()
