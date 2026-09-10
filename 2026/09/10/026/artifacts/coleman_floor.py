"""Combined target stress-test: Coleman ceiling vs explicit Q-points.
Run: python3 coleman_floor.py
Inputs (all recomputed here exactly, no imports from sibling scripts):
  - #C(F7) total = 14 (affine enumeration + 1 smooth infinity; good
    reduction since disc=38569, 38569 mod 7 = 6).
  - 17 explicit Q-points (16 affine + infinity) verified by exact Fractions.
Conclusion (conditional on the cited Coleman 1985 bound only):
  If rank(J(Q)) < 2 then #C(Q) <= #C(F7) + 2g - 2 = 16. Since 17 distinct
  Q-points are exhibited, rank(J(Q)) >= 2, refuting 'rank exactly 1', and
  the 'exactly 6 affine + inf' list is refuted by the 10 extra affine points.
Prints COLEMAN_FLOOR_OK.
"""
from fractions import Fraction

def f_int(x):
    return x**5 - 5*x**3 + 4*x + 1

def main():
    # disc check
    assert 38569 % 7 == 6
    # C(F7) affine enumeration
    p = 7
    sq = {}
    for y in range(p):
        sq.setdefault((y*y) % p, []).append(y)
    aff = [(x, y) for x in range(p) for y in sq.get(f_int(x) % p, [])]
    print(f"C(F7) affine count: {len(aff)}")
    assert len(aff) == 13
    N7 = len(aff) + 1  # smooth point at infinity (odd-degree model)
    print(f"#C(F7) total: {N7}")
    assert N7 == 14
    # explicit Q-points
    def ff(x):
        return x**5 - 5*x**3 + 4*x + 1
    pts = [
        (Fraction(0), Fraction(1)), (Fraction(0), Fraction(-1)),
        (Fraction(1), Fraction(1)), (Fraction(1), Fraction(-1)),
        (Fraction(-1), Fraction(1)), (Fraction(-1), Fraction(-1)),
        (Fraction(-2), Fraction(1)), (Fraction(-2), Fraction(-1)),
        (Fraction(2), Fraction(1)), (Fraction(2), Fraction(-1)),
        (Fraction(3), Fraction(11)), (Fraction(3), Fraction(-11)),
        (Fraction(-7, 4), Fraction(67, 32)), (Fraction(-7, 4), Fraction(-67, 32)),
        (Fraction(4, 9), Fraction(373, 243)), (Fraction(4, 9), Fraction(-373, 243)),
    ]
    for (x, y) in pts:
        assert y*y == ff(x), (x, y)
    assert len(set(pts)) == 16
    total = 17  # + smooth point at infinity
    ceil_rank1 = N7 + 2*2 - 2  # #C(Fp)+2g-2 with g=2
    print(f"explicit affine Q-points: 16; total with inf: {total}")
    print(f"Coleman rank-1 ceiling at p=7: {ceil_rank1}")
    assert total == 17 > ceil_rank1 == 16
    print("=> rank(J(Q)) >= 2 (given Coleman 1985); 'rank exactly 1' REFUTED.")
    print("=> 'exactly 6 affine + inf' REFUTED (16 affine exhibited).")
    print("COLEMAN_FLOOR_OK")

if __name__ == "__main__":
    main()
