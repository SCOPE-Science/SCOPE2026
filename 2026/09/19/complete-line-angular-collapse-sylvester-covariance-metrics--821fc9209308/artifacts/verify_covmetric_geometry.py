"""Numerical checks for the covariance-metric completeness/angular formulas.

Requires Python 3 and NumPy.  The checks use only explicit kernel identities and
the two-dimensional isospectral rotation path stated in RESULT.md.
"""
import math
import numpy as np


def phi(p, q, x, y):
    return 0.5 * 4.0 ** ((p - q) ** 2) * (x**p * y**q + x**q * y**p)


def normalized_phi_on_complete_line(a, x, y):
    return x * y * math.cosh(0.5 * a * math.log(x / y))


def quarter_turn_length(a, kappa):
    s = math.sqrt(kappa)
    t = 1.0 / s
    return (
        math.pi
        / math.sqrt(2.0)
        * (s - t)
        / math.sqrt(math.cosh(0.5 * a * math.log(kappa)))
    )


def direct_rotation_speed(a, kappa):
    s = math.sqrt(kappa)
    t = 1.0 / s
    D = np.diag([s, t])
    Omega = np.array([[0.0, -1.0], [1.0, 0.0]])
    U = Omega @ D - D @ Omega
    vals = [s, t]
    g = 0.0
    for i in range(2):
        for j in range(2):
            g += U[i, j] ** 2 / normalized_phi_on_complete_line(
                a, vals[i], vals[j]
            )
    return math.sqrt(g)


rng = np.random.default_rng(12345)
max_homogeneity_residual = 0.0
max_inversion_residual = 0.0
for _ in range(1000):
    p, q = rng.normal(size=2)
    x, y = np.exp(rng.normal(size=2))
    scale = math.exp(rng.normal())
    degree = p + q
    hom = phi(p, q, scale * x, scale * y) / (
        scale**degree * phi(p, q, x, y)
    )
    inv = x * x * y * y * phi(p, q, 1.0 / x, 1.0 / y) / phi(
        2.0 - p, 2.0 - q, x, y
    )
    max_homogeneity_residual = max(max_homogeneity_residual, abs(hom - 1.0))
    max_inversion_residual = max(max_inversion_residual, abs(inv - 1.0))

print("max relative homogeneity residual:", max_homogeneity_residual)
print("max relative inversion-kernel residual:", max_inversion_residual)

for a in [1.0, 2.0, 3.0, 4.0]:
    print(f"\na = {a:g}")
    for kappa in [1e2, 1e4, 1e8]:
        length = quarter_turn_length(a, kappa)
        exponent = (2.0 - abs(a)) / 4.0
        scaled = length / (kappa**exponent)
        print(
            f"kappa={kappa:.0e}  Lbar={length:.15g}  "
            f"Lbar/kappa^(({2.0-abs(a):g})/4)={scaled:.15g}"
        )
    direct = direct_rotation_speed(a, 123.0)
    s = math.sqrt(123.0)
    t = 1.0 / s
    closed = math.sqrt(2.0) * (s - t) / math.sqrt(
        math.cosh(0.5 * a * math.log(123.0))
    )
    print("direct speed:", direct)
    print("closed-form speed:", closed)
    print("speed discrepancy:", abs(direct - closed))

print("\nmean-kernel monotonicity boundary")
for a in [1.9, 2.0, 2.1, 3.0]:
    s = np.linspace(-30.0, 30.0, 20001)
    dlogx = 0.5 + (a / 4.0) * np.tanh(a * s / 2.0)
    dlogy = 0.5 - (a / 4.0) * np.tanh(a * s / 2.0)
    print(f"a={a:g}  min derivatives=({dlogx.min():.15g}, {dlogy.min():.15g})")
