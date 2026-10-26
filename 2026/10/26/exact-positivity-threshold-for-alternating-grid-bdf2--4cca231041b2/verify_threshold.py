from fractions import Fraction
from math import isqrt


def bdf2_alternating(r: Fraction, z: Fraction, nmax: int):
    """Exact scalar recurrence; first long step is backward Euler."""
    y = [Fraction(1), Fraction(1, 1) / (1 + r * z)]
    for n in range(2, nmax + 1):
        if n % 2 == 0:  # short step after a long step
            ratio, zn = 1 / r, z
        else:           # long step after a short step
            ratio, zn = r, r * z
        den = 1 + 2 * ratio + (1 + ratio) * zn
        y.append(((1 + ratio) ** 2 * y[-1] - ratio ** 2 * y[-2]) / den)
    return y


def main():
    for r_int in (1, 4, 9, 16):
        root = isqrt(r_int)
        assert root * root == r_int
        r = Fraction(r_int)
        z_star = Fraction(2, (root + 1) ** 2)
        at_boundary = bdf2_alternating(r, z_star, 300)
        assert all(value > 0 for value in at_boundary)
        above = bdf2_alternating(r, z_star + Fraction(1, 100), 500)
        assert any(value <= 0 for value in above)
        print(f"r={r_int}: boundary positive through n=300; above-boundary nonpositive value found")


if __name__ == "__main__":
    main()
