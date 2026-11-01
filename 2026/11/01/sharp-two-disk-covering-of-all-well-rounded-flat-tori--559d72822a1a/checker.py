"""Exact-rational spot checks for the two-disk flat-torus covering formulas.

Finite diagnostics only; the continuum result is established analytically.
"""
from fractions import Fraction as F


def norm2(x, y, c):
    return x*x + y*y + 2*c*x*y


def nearest_two_cosets(s, t, c):
    # Norm squared in basis of equal-length generators and cosine c.
    ans = None
    for i in range(-2, 4):
        for j in range(-2, 4):
            for h in (F(0), F(1, 2)):
                v = norm2(s-i-h, t-j-h, c)
                ans = v if ans is None or v < ans else ans
    return ans


def main():
    tests = 0
    for cosine in (F(-1, 2), F(-2, 5), F(-1, 3), F(0), F(1, 3), F(2, 5), F(1, 2)):
        # u=(a+b)/2 and v=(a-b)/2 are orthogonal for any c.
        u2 = (1+cosine)/2
        v2 = (1-cosine)/2
        assert u2 + v2 == 1
        assert u2 > 0 and v2 > 0
        # The original lattice has shortest nonzero vector length 1.
        for i in range(-9, 10):
            for j in range(-9, 10):
                if (i,j)!=(0,0):
                    assert norm2(F(i), F(j), cosine) >= 1
                    tests += 1
        for s_n in range(21):
            for t_n in range(21):
                squared = nearest_two_cosets(F(s_n,20),F(t_n,20),cosine)
                assert squared <= F(1,4), (cosine,s_n,t_n,squared)
                tests += 1
        # a/2 and b/2 represent exactly the two furthest two-center points.
        assert nearest_two_cosets(F(1,2),F(0),cosine) == F(1,4)
        assert nearest_two_cosets(F(0),F(1,2),cosine) == F(1,4)
    print(f"PASS: {tests} exact-rational vector/sample checks across 7 Gram shapes; max squared distance 1/4.")


if __name__ == '__main__':
    main()
