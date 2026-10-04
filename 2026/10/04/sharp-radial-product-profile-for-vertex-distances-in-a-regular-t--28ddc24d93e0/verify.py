import math
import random
from fractions import Fraction

ROOT3 = math.sqrt(3.0)
VERTICES = [
    (1 / ROOT3, 1 / ROOT3, 1 / ROOT3),
    (1 / ROOT3, -1 / ROOT3, -1 / ROOT3),
    (-1 / ROOT3, 1 / ROOT3, -1 / ROOT3),
    (-1 / ROOT3, -1 / ROOT3, 1 / ROOT3),
]

def norm(v):
    return math.sqrt(sum(q * q for q in v))

def product_distance(x, u):
    p = tuple(x * q for q in u)
    ans = 1.0
    for v in VERTICES:
        ans *= norm(tuple(p[j] - v[j] for j in range(3)))
    return ans

def lower(x):
    return abs(1.0 - x) * (1.0 + x * x + 2.0 * x / 3.0) ** 1.5

def upper(x):
    return (1.0 + x) * (1.0 + x * x - 2.0 * x / 3.0) ** 1.5

def main():
    rng = random.Random(20261001)
    xs = [0.0, 1e-8, 0.01, 0.1, 0.25, 0.5, 0.9, 1.0, 1.1, 2.0, 5.0, 20.0]
    xs.extend(10.0 ** rng.uniform(-3.0, 1.5) for _ in range(3000))
    max_bound_violation = 0.0
    max_equality_error = 0.0
    max_factor_error = 0.0
    checks = 0

    for x in xs:
        lo = lower(x)
        hi = upper(x)
        for _ in range(8):
            z = [rng.gauss(0.0, 1.0) for _ in range(3)]
            nz = norm(z)
            u = tuple(q / nz for q in z)
            value = product_distance(x, u)
            scale = max(1.0, hi)
            max_bound_violation = max(
                max_bound_violation,
                (lo - value) / scale,
                (value - hi) / scale,
            )
            if value < lo - 2e-11 * scale or value > hi + 2e-11 * scale:
                raise AssertionError((x, value, lo, hi, u))
            checks += 1
        if x > 0.0:
            for v in VERTICES:
                toward = product_distance(x, v)
                away = product_distance(x, tuple(-q for q in v))
                max_equality_error = max(
                    max_equality_error,
                    abs(toward - lo) / max(1.0, lo),
                    abs(away - hi) / max(1.0, hi),
                )
                checks += 2

    for k in range(1, 401):
        q = Fraction(k, 37)
        a = (q - 1) ** 2 * (q * q + 1 + Fraction(2, 3) * q) ** 3
        b = (q + 1) ** 2 * (q * q + 1 - Fraction(2, 3) * q) ** 3
        c = (q ** 4 + Fraction(2, 3) * q * q + 1) ** 2
        rhs1 = -Fraction(64, 27) * q ** 3 * (q * q + q + 1)
        rhs2 = Fraction(64, 27) * q ** 3 * (q * q - q + 1)
        rhs3 = -Fraction(128, 27) * q ** 3 * (q * q + 1)
        for lhs, rhs in ((a - c, rhs1), (b - c, rhs2), (a - b, rhs3)):
            if lhs != rhs:
                raise AssertionError((q, lhs, rhs))
            checks += 1
    max_factor_error = 0.0

    print("VERIFY_OK")
    print("checks", checks)
    print("max_normalized_bound_violation", f"{max(0.0, max_bound_violation):.3e}")
    print("max_normalized_equality_error", f"{max_equality_error:.3e}")
    print("max_normalized_branch_factorization_error", f"{max_factor_error:.3e}")

if __name__ == "__main__":
    main()
