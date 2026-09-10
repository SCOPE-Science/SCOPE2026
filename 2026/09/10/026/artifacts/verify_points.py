"""Exact verification that C(Q) contains >= 17 points, refuting the admitted
6-affine+infinity list. Run: python3 verify_points.py
Uses only fractions.Fraction (exact). Prints VERIFY_POINTS_OK.
"""
from fractions import Fraction

def f_frac(x):
    return x**5 - 5*x**3 + 4*x + 1

KNOWN_TARGET = [
    (Fraction(0), Fraction(1)), (Fraction(0), Fraction(-1)),
    (Fraction(1), Fraction(1)), (Fraction(1), Fraction(-1)),
    (Fraction(-1), Fraction(1)), (Fraction(-1), Fraction(-1)),
]
EXTRA = [
    (Fraction(-2), Fraction(1)), (Fraction(-2), Fraction(-1)),
    (Fraction(2), Fraction(1)), (Fraction(2), Fraction(-1)),
    (Fraction(3), Fraction(11)), (Fraction(3), Fraction(-11)),
    (Fraction(-7, 4), Fraction(67, 32)), (Fraction(-7, 4), Fraction(-67, 32)),
    (Fraction(4, 9), Fraction(373, 243)), (Fraction(4, 9), Fraction(-373, 243)),
]

def main():
    for (x, y) in KNOWN_TARGET + EXTRA:
        assert y*y == f_frac(x), (x, y)
        print(f"on-curve: ({x}, {y})  f(x) = {f_frac(x)} = ({y})^2")
    aff = set(KNOWN_TARGET) | set(EXTRA)
    print(f"distinct affine Q-points verified: {len(aff)}")
    assert len(aff) == 16
    xs = sorted(set(x for x, y in aff))
    print("x-values:", [str(v) for v in xs])
    assert len(xs) == 8
    print("total with infinity: 17 > admitted 7 and > Coleman rank-1 ceiling 16")
    print("VERIFY_POINTS_OK")

if __name__ == "__main__":
    main()
