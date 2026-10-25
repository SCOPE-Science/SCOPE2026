"""Exact small certificates for the planar lattice-width/Ehrhart-root theorem.

Run: python3 verify_planar_width_roots.py
The universal statement relies on the published planar isominwidth inequality,
Pick's theorem, and the proof in RESULT.md; these tests check the finite
low-discriminant Hermite forms and independent lattice-point counts.
"""
from math import gcd


def triangle_width(a, determinant):
    # A primitive direction (p,q) of width at most determinant can have
    # |p|<=determinant and |a*p+determinant*q|<=determinant.
    best = determinant
    minimizers = []
    for p in range(-determinant, determinant + 1):
        for q in range(-determinant - abs(a) - 2, determinant + abs(a) + 3):
            if gcd(p, q) != 1:
                continue
            heights = (0, p, a*p + determinant*q)
            width = max(heights) - min(heights)
            if width < best:
                best, minimizers = width, [(p, q)]
            elif width == best:
                minimizers.append((p,q))
    return best, minimizers


def lattice_points(a, determinant, scale):
    # (x,y) in scale * conv((0,0),(1,0),(a,determinant))
    # iff y>=0, determinant*x-a*y>=0,
    # determinant*(scale-x)+(a-1)*y>=0.
    pts = []
    for y in range(0, scale * determinant + 1):
        for x in range(0, scale * max(1, a) + 1):
            if determinant*x-a*y >= 0 and determinant*(scale-x)+(a-1)*y >= 0:
                pts.append((x,y))
    return pts


def check_hnf(det, expected):
    got = {}
    for a in range(1, det):
        if gcd(a, det) > 1 or gcd(a-1,det) > 1:
            continue
        w, directions = triangle_width(a, det)
        B = 1 + gcd(a,det) + gcd(a-1,det)
        assert B == 3
        I = (det-B+2)//2
        assert det == 2*I+B-2
        h1 = I+B-3
        discr = h1*h1-4*I
        got[a] = (w,discr)
        for n in (0,1,2,3):
            actual = len(lattice_points(a,det,n))
            pick_ehrhart = (det*n*n+B*n)//2 + 1
            assert actual == pick_ehrhart, (det,a,n,actual,pick_ehrhart)
    assert got == expected, (det,got,expected)
    return got


def main():
    assert check_hnf(7, {2:(2,-3),3:(3,-3),4:(2,-3),5:(3,-3),6:(2,-3)})
    assert check_hnf(9, {2:(2,0),5:(2,0),8:(2,0)})
    for I in range(1, 20):
        for B in range(3, 20):
            disc=(I+B-3)**2-4*I
            if disc<0:
                assert (I,B) in {(1,3),(2,3),(3,3)}
            if disc==0:
                assert (I,B) in {(1,4),(4,3)}
    # Explicit affine-unimodular identification: a=3 ↔ a=5 at det 7.
    M = ((5,-2),(7,-3)) # det=-1; maps (3,7)->(1,0); (1,0)->(5,7)
    assert M[0][0]*M[1][1]-M[0][1]*M[1][0] == -1
    assert tuple(row[0]*3+row[1]*7 for row in M)==(1,0)
    assert tuple(row[0] for row in M)==(5,7)
    print('PLANAR_WIDTH_ROOTS_OK det7=5 det9=3 low_discriminant_pairs=5')

if __name__ == '__main__':
    main()
