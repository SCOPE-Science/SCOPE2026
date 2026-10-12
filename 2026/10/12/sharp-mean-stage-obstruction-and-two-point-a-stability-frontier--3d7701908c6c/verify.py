#!/usr/bin/env python3
"""Exact coefficient and rational-point checks for a random-stage stability theorem.

Run: python3 verify.py. Uses only the Python standard library.
The analytic proofs in RESULT.md, not point tests, justify universal claims.
"""
from fractions import Fraction as Q

NVAR = 3


class Poly:
    def __init__(self, terms=None):
        self.d = {k: Q(v) for k, v in (terms or {}).items() if v}

    @staticmethod
    def const(v):
        return Poly({(0,) * NVAR: Q(v)})

    @staticmethod
    def var(index):
        e = [0] * NVAR
        e[index] = 1
        return Poly({tuple(e): Q(1)})

    @staticmethod
    def lift(v):
        return v if isinstance(v, Poly) else Poly.const(v)

    def __add__(self, other):
        other = Poly.lift(other)
        d = dict(self.d)
        for k, v in other.d.items():
            d[k] = d.get(k, Q(0)) + v
        return Poly(d)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.d.items()})

    def __sub__(self, other):
        return self + (-Poly.lift(other))

    def __rsub__(self, other):
        return Poly.lift(other) - self

    def __mul__(self, other):
        other = Poly.lift(other)
        d = {}
        for k, v in self.d.items():
            for ell, w in other.d.items():
                m = tuple(i + j for i, j in zip(k, ell))
                d[m] = d.get(m, Q(0)) + v * w
        return Poly(d)

    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result = Poly.const(1)
        for _ in range(n):
            result *= self
        return result

    def __eq__(self, other):
        return self.d == Poly.lift(other).d


def amp_square(t, u, y):
    """Squared modulus of R(-u+iy,t), exact rational arithmetic."""
    s = u * u + y * y
    return (1 - 2 * (1 - t) * u + (1 - t) ** 2 * s) / (
        1 + 2 * t * u + t * t * s
    )


def main():
    t, u, s = (Poly.var(i) for i in range(NVAR))
    q = 1 - 8 * (t - Q(1, 2)) + 12 * (t - Q(1, 2)) ** 2
    # Identity valid for all real t after clearing the denominator t^2.
    assert (1 - t) ** 2 - t ** 2 * q == (1 - t) * (2 * t - 1) ** 2 * (3 * t + 1)

    a = t
    da = 1 + 2 * a * u + a * a * s
    d1 = 1 + 2 * u + s
    na = -2 * u + (1 - 2 * a) * s
    n1 = -2 * u - s
    positive = (1 - 2 * a) * (1 + a) * s + 2 * a * s * u + 4 * a * u ** 2 + 2 * (1 - a) * u
    # Multiply the boundary-mixture numerator by (1-a)^2.
    assert a ** 2 * na * d1 + ((1 - a) ** 2 - a ** 2) * n1 * da == -(1 - a) * positive

    ntests = 0
    for aa in [Q(1, 6), Q(1, 4), Q(1, 3), Q(2, 5), Q(49, 100)]:
        pc = (aa / (1 - aa)) ** 2
        for uu in [Q(1, 100), Q(1, 3), Q(1), Q(5), Q(100)]:
            for yy in [Q(0), Q(1, 3), Q(2), Q(11)]:
                Fa = amp_square(aa, uu, yy)
                F1 = amp_square(Q(1), uu, yy)
                for p in [Q(0), pc / 2, pc]:
                    F = p * Fa + (1 - p) * F1
                    assert F < 1, (aa, p, uu, yy, F)
                    ntests += 1
        badp = (pc + Q(1)) / 2
        assert badp * amp_square(aa, Q(10**8), Q(0)) + (1 - badp) * amp_square(Q(1), Q(10**8), Q(0)) > 1
        ntests += 1

    for eps in [Q(1, n) for n in [10, 100, 1000, 10000]]:
        left = (Q(1, 2) - eps) / (1 - eps)
        mean = (1 - eps) * left + eps
        var = (1 - eps) * (left - Q(1, 2)) ** 2 + eps * Q(1, 4)
        g = (1 - eps) * ((1 - left) / left) ** 2
        assert mean == Q(1, 2)
        assert g >= 1 + 12 * var
        assert (g - 1) / var > 12
        ntests += 1

    print('PASS exact polynomial identities: 2')
    print(f'PASS rational boundary/stability and sharpness tests: {ntests}')
    print('LIMIT: finite rational tests do not replace the proof for all parameters.')


if __name__ == '__main__':
    main()
