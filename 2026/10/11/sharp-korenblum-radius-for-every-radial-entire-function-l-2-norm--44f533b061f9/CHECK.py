"""Exact-rational finite checks accompanying the radial Fock domination theorem.

These checks illustrate the proof; the infinite-dimensional conclusion is proved
analytically in RESULT.md, not by the finite computations here.
"""
from fractions import Fraction as F
from math import factorial


def add(a, b):
    n = max(len(a), len(b))
    return [((a[k] if k < len(a) else F(0)) +
             (b[k] if k < len(b) else F(0))) for k in range(n)]


def scale(a, t):
    return [t * v for v in a]


def mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def shift(a, k):
    return a[k:] if k < len(a) else [F(0)]


def power_apply(poly, a, radius):
    """Evaluate a polynomial in radius times the backward coefficient shift."""
    result = [F(0)]
    for k, x in enumerate(poly):
        result = add(result, scale(shift(a, k), x * radius**k))
    return result


def reverse(poly, degree, radius):
    return [poly[degree-k] * radius**(degree-k)
            if degree-k < len(poly) else F(0) for k in range(degree+1)]


def moment(k):
    # W(t) = exp(-t) + (28/5) exp(-4t): m_1/m_0=9/16.
    return F(factorial(k)) * (1 + F(28, 5) / (4**(k + 1)))


def norm2(p):
    return sum((abs(x)**2 * moment(j) for j, x in enumerate(p)), F(0))


def test_pair(aa, bb, outer):
    r = F(3, 4)
    p, q = [outer], [F(1)]
    for a in (aa, bb):
        p = mul(p, [r, -a])
        q = mul(q, [-a * r, F(1)])
    k = [F(1), F(1, 2), F(1, 3)]
    f, g = mul(p, k), mul(q, k)
    d = len(q) - 1
    P, Q = reverse(p, d, r), reverse(q, d, r)
    lhs, rhs = power_apply(Q, f, r), power_apply(P, g, r)
    assert lhs == rhs, 'reverse-polynomial/backward-shift identity'
    assert norm2(f) < norm2(g), 'exterior Schur domination norm inequality'
    return norm2(g) - norm2(f)


def main():
    r = F(3, 4)
    assert moment(1) / moment(0) == r*r
    # Log convexity and sharp backward-shift bound in finite windows.
    for k in range(1, 25):
        assert moment(k)**2 <= moment(k-1) * moment(k+1)
        assert r*r * moment(k-1) <= moment(k)
    gaps = [
        test_pair(F(1, 3), F(1, 4), F(4, 5)),
        test_pair(F(0), F(2, 5), F(7, 9)),
        test_pair(F(3, 7), F(1, 8), F(1)),
    ]
    # The sharpness obstruction is f=c, g=z at comparison radius S=1.
    c = F(7, 8)
    assert r < c < 1
    assert c*c*moment(0) > moment(1)
    # Ring-concentrated radial weight W=1_[3/4,5/4].
    def ring_m(k):
        return ((F(5,4)**(k+1)-F(3,4)**(k+1))/(k+1))
    assert ring_m(1) == ring_m(0)
    for k in range(1, 25):
        assert ring_m(k)*ring_m(k) <= ring_m(k-1)*ring_m(k+1)
    print('EXACT_CHECK_OK')
    print('R_squared=', moment(1)/moment(0))
    print('strict_norm_gaps=', gaps)
    print('sharpness_norm_gap=', c*c*moment(0)-moment(1))


if __name__ == '__main__':
    main()
