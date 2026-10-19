"""Exact arithmetic checks for the priced barbell resistance allocation theorem.

Run with Python 3 and SymPy 1.14 or compatible.
This finite checker corroborates, but does not replace, the analytic proof.
"""
from fractions import Fraction
import sympy as sp


def laplacian(m, a, b, c):
    N = 2 * (m + 1)
    L = sp.zeros(N, N)
    def add_edge(i, j, x):
        L[i, i] += x
        L[j, j] += x
        L[i, j] -= x
        L[j, i] -= x
    for hub in (0, m + 1):
        for i in range(hub + 1, hub + m + 1):
            add_edge(hub, i, a)
        for i in range(hub + 1, hub + m + 1):
            for j in range(i + 1, hub + m + 1):
                add_edge(i, j, b)
    add_edge(0, m + 1, c)
    return L


def kirchhoff_index(L):
    N = L.rows
    J = sp.ones(N, N) / N
    return sp.factor(N * sp.trace((L + J).inv() - J))


def closed_index(m, a, b, c):
    return ((m + 1)**2 / c + 2 * (m + 2) / a
            + 4 * (m + 1) * (m - 1) / (a + m * b))


def exact0(q):
    assert sp.simplify(sp.radsimp(q)) == 0, sp.simplify(q)

checks = 0
for m in (2, 3, 4, 5):
    for a, b, c in ((sp.Rational(2, 5), sp.Rational(1, 3), sp.Rational(7, 8)),
                    (sp.Rational(2, 3), sp.S.Zero, sp.Rational(1, 3)),
                    (sp.Rational(11, 6), sp.Rational(1, 8), sp.Rational(4, 3))):
        exact0(kirchhoff_index(laplacian(m, a, b, c)) - closed_index(m, a, b, c))
        checks += 1

for m in range(2, 13):
    mm = sp.Integer(m)
    tcrit = 4 * (mm + 1) / (2 * mm + 1)
    A = (mm + 1)**2
    C = 2 * (mm + 2)
    D = 4 * (mm + 1) * (mm - 1)
    S0 = (mm + 1) + 2 * mm * sp.sqrt(2 * mm + 1)
    for B in (sp.S.One, sp.Rational(7, 3)):
        for t in (sp.Rational(1, 3), sp.S.One, tcrit / 2,
                  tcrit, tcrit + sp.Rational(1, 5), sp.Integer(5)):
            if t < tcrit:
                w = 2 * mm - t * (mm - 1)
                v = t * (mm - 1)
                S = sp.sqrt(C * w) + sp.sqrt(D * v) + sp.sqrt(A)
                a = B * sp.sqrt(C / w) / S
                u = B * sp.sqrt(D / v) / S
                b = (u - a) / mm
                c = B * sp.sqrt(A) / S
                assert float(sp.N(b)) > 0
                exact0(2 * mm * a + t * mm * (mm - 1) * b + c - B)
                exact0(closed_index(mm, a, b, c) - S * S / B)
                lagrange_multiplier = A / (c * c)
                exact0(C / a**2 + D / (a + mm*b)**2 - 2 * mm * lagrange_multiplier)
                exact0(D / (a + mm*b)**2 - t * (mm - 1) * lagrange_multiplier)
                checks += 4
            else:
                a = B * sp.sqrt(2 * mm + 1) / S0
                b = sp.S.Zero
                c = B * (mm + 1) / S0
                exact0(2 * mm * a + c - B)
                exact0(closed_index(mm, a, b, c) - S0**2 / B)
                lagrange_multiplier = A / c**2
                exact0((C + D) / a**2 - 2 * mm * lagrange_multiplier)
                dir_deriv = (-mm*D/a**2
                             + lagrange_multiplier*t*mm*(mm-1))
                expected_deriv = (mm * (mm - 1) * ((2*mm+1)*t - 4*(mm+1)) / a**2)
                exact0(dir_deriv - expected_deriv)
                assert dir_deriv >= 0 or float(sp.N(dir_deriv)) > -1e-11
                checks += 5
        w = 2*mm - tcrit*(mm-1)
        v = tcrit*(mm-1)
        Scrit = sp.sqrt(C*w) + sp.sqrt(D*v) + sp.sqrt(A)
        exact0(Scrit - S0)
        checks += 1

print(f"VERIFY_OK {checks} exact Kirchhoff/feasibility/KKT/equality certificates; m=2..12")
