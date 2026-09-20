"""Numerical check of the single-interval asymptotic in RESULT.md.

For the source strip |x1-x2|<eps, |x2|<1, the same-sign quadrant integral is

    Q(eps) = int_0^inf sin(eps*t)^2/t^2
                   [int_t^inf sin(p)^2/p^2 dp] dt.

The theorem predicts Q(eps)/eps^2 - 0.5*log(1/eps) -> 5/4.
"""

from math import log, pi
from scipy.integrate import quad
from scipy.special import sici


def tail(t):
    if t == 0.0:
        return pi / 2.0
    si, _ = sici(2.0 * t)
    return pi / 2.0 - si + ( __import__("math").sin(t) ** 2 ) / t


def q_eps(eps):
    from math import sin

    def integrand(t):
        if t == 0.0:
            return eps * eps * pi / 2.0
        return (sin(eps * t) ** 2 / (t * t)) * tail(t)

    cuts = (0.0, 1.0, 1.0 / eps, 20.0 / eps, 100.0 / eps)
    total = 0.0
    for a, b in zip(cuts[:-1], cuts[1:]):
        total += quad(integrand, a, b, limit=800, epsabs=1e-9, epsrel=1e-7)[0]
    return total


if __name__ == "__main__":
    for eps in (0.05, 0.02, 0.01):
        q = q_eps(eps)
        renormalized = q / (eps * eps) - 0.5 * log(1.0 / eps)
        print(f"eps={eps:g}  renormalized={renormalized:.9f}")
    print("predicted limit = 1.250000000")
