"""Exact rational polygon tests for a piecewise-affine second-quadrant survivor law.

The finite tests corroborate but do not replace the proof for all real parameters.
Run with standard Python: python check_exact.py
"""
from fractions import Fraction as Q

A = ((-1, -1), (1, -1))


def mat_mul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def mat_vec(a, v):
    return tuple(sum(a[i][k]*v[k] for k in range(2)) for i in range(2))


def constraints(n, alpha, beta):
    a = ((1, 0), (0, 1))
    for _ in range(n):
        # x < 0, y > 0 for p_b + A^j w.
        yield a[0][0], a[0][1], alpha
        yield -a[1][0], -a[1][1], beta
        a = mat_mul(A, a)


def clip(poly, halfspace):
    aa, bb, cc = halfspace
    def residual(v):
        return cc - aa*v[0] - bb*v[1]
    result = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        r, s = residual(p), residual(q)
        if r >= 0:
            result.append(p)
        if (r < 0 < s) or (r > 0 > s):
            result.append(tuple((p[i]*s - q[i]*r)/(s-r) for i in (0, 1)))
    return result


def polygon(n, b):
    alpha, beta = (b+2)/5, (2*b-1)/5
    assert beta > 0 and beta < 2*alpha
    r = Q(1000)*(alpha+beta)
    poly = [(-r, -r), (r, -r), (r, r), (-r, r)]
    for h in constraints(n, alpha, beta):
        poly = clip(poly, h)
    return poly


def area(poly):
    return abs(sum(x1*y2-y1*x2 for (x1,y1), (x2,y2)
                   in zip(poly, poly[1:]+poly[:1])))/2


def expected_three(b):
    return (2*b-1)**2/8 if b <= 1 else (b*b+2*b-2)/8


def polygon_vertices(poly):
    # Canonical exact vertex set ignoring redundant collinear boundary points.
    a = []
    for p in poly:
        if p not in a:
            a.append(p)
    return set(p for j, p in enumerate(a)
               if (a[j][0]-a[j-1][0])*(a[(j+1)%len(a)][1]-p[1])
               != (a[j][1]-a[j-1][1])*(a[(j+1)%len(a)][0]-p[0]))


def inverse_image(poly):
    inverse = ((Q(-1,2), Q(1,2)), (Q(-1,2), Q(-1,2)))
    return [mat_vec(inverse, p) for p in poly]


def check():
    for b in [Q(51,100), Q(3,4), Q(1), Q(5,4), Q(2), Q(10), Q(101,2)]:
        s3 = polygon(3, b)
        assert area(s3) == expected_three(b), (b, 'three-visit area')
        for n in range(3, 11):
            sn = polygon(n, b)
            nextp = polygon(n+1, b)
            assert area(sn) == expected_three(b)/2**(n-3), (b,n)
            assert polygon_vertices(nextp) == polygon_vertices(inverse_image(sn)), (b,n)
    # A^-1 S_2 is not wholly inside Q2 at a finite parameter,
    # showing that the onset index three cannot be reduced to two.
    b=Q(2)
    a,c=(b+2)/5,(2*b-1)/5
    witness=(a,a+c)
    w_inv=mat_vec(((Q(-1,2), Q(1,2)), (Q(-1,2), Q(-1,2))),witness)
    assert w_inv[1] < -c
    print('Q2_EXACT_RATIONAL_POLYGON_CHECK_OK')


if __name__ == '__main__':
    check()
