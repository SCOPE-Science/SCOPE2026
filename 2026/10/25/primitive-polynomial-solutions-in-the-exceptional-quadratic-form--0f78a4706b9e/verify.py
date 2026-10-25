#!/usr/bin/env python3
"""Exact polynomial identity checks for the exceptional quadratic-form family.

Uses only the Python standard library.  Coefficients are integers and every
identity is checked as equality of sparse multivariate polynomials, not by
sampling numerical values.
"""

from dataclasses import dataclass
from typing import Dict, Tuple

Exp = Tuple[int, int, int, int]

@dataclass(frozen=True)
class Poly:
    terms: Dict[Exp, int]

    @staticmethod
    def const(k: int) -> "Poly":
        return Poly({(0, 0, 0, 0): k} if k else {})

    @staticmethod
    def var(i: int) -> "Poly":
        e = [0, 0, 0, 0]
        e[i] = 1
        return Poly({tuple(e): 1})

    def __add__(self, other):
        other = other if isinstance(other, Poly) else Poly.const(other)
        out = dict(self.terms)
        for e, c in other.terms.items():
            out[e] = out.get(e, 0) + c
            if out[e] == 0:
                del out[e]
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({e: -c for e, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, Poly) else -Poly.const(other))

    def __rsub__(self, other):
        return (other if isinstance(other, Poly) else Poly.const(other)) - self

    def __mul__(self, other):
        other = other if isinstance(other, Poly) else Poly.const(other)
        out = {}
        for e1, c1 in self.terms.items():
            for e2, c2 in other.terms.items():
                e = tuple(a + b for a, b in zip(e1, e2))
                out[e] = out.get(e, 0) + c1 * c2
        return Poly({e: c for e, c in out.items() if c})

    __rmul__ = __mul__

    def __pow__(self, k: int):
        if k < 0:
            raise ValueError("negative polynomial power")
        out = Poly.const(1)
        base = self
        while k:
            if k & 1:
                out = out * base
            base = base * base
            k >>= 1
        return out


def require_identity(lhs: Poly, rhs: Poly, label: str) -> None:
    if lhs != rhs:
        raise AssertionError(label)

n, c, u, v = (Poly.var(i) for i in range(4))
U = u + 1
A = 2 * U * v
B = U**2 - 2 * n * v**2
C = U**2 + 2 * n * v**2

# The parametrized conic identity is valid for every integer n.
require_identity(C**2, 2 * n * A**2 + B**2, "conic identity")

# Exceptional branch c != 0: F_c(x,y,z) = (x+y)^2 + c*y*z.
x = -c * n * A**2
y = -c * B**2
z = C**2
F = (x + y)**2 + c * y * z
t = c**2 * n**2 * A**3 * B * C
require_identity(F, c**2 * n**2 * A**4, "exceptional F identity")
require_identity(t**2, n * x * y * z * F, "exceptional square identity")

# Branch c = 0, with a separate primitive choice of x,y,z.
x0 = n * A**2
y0 = B**2
z0 = C**2
F0 = (x0 + y0)**2
t0 = n * A * B * C * (x0 + y0)
require_identity(t0**2, n * x0 * y0 * z0 * F0, "c=0 square identity")

print("VERIFY_OK: all polynomial identities hold symbolically.")
