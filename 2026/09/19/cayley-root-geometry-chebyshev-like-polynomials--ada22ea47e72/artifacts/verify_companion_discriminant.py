"""Exact checks for the Cayley reduction and companion discriminant.

Requires SymPy 1.14 or compatible.
"""

import sympy as sp

z, u = sp.symbols("z u")


def p_source(n):
    return sp.expand(sum(
        (k + 1) * (z + 1) ** (2 * k) * (z - 1) ** (2 * n - 2 * k)
        for k in range(n + 1)
    ))


def q_source(n):
    if n == 0:
        return sp.Integer(1)
    return sp.expand(p_source(n) - (z**2 + 1) * p_source(n - 1))


def q_formula(n):
    Q = sum(u**k for k in range(n)) + (n + 2) * u**n
    # Clear the Cayley denominator exactly.
    return sp.expand(
        sp.Rational(1, 2)
        * (z - 1) ** (2 * n)
        * Q.subs(u, ((z + 1) / (z - 1)) ** 2)
    )


def disc_formula(n):
    return (
        (-1) ** n
        * 2 ** (4 * n * (n - 1))
        * (n + 2)
        * (n + 1) ** (2 * n - 2)
        * (((n + 2) ** n + n**n) // 2) ** 2
    )


for n in range(1, 7):
    q = q_source(n)
    assert sp.cancel(q - q_formula(n)) == 0
    assert sp.discriminant(q, z) == disc_formula(n)

print("all exact checks passed for n=1,...,6")
