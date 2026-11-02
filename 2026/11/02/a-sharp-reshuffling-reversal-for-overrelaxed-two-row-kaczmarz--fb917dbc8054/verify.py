"""Exact rational checks for a two-row relaxed Kaczmarz sampling comparison.

Usage: python3 verify.py. The analytical proof is contained in RESULT.md;
these finite checks do not establish the quantified theorem by enumeration.
"""
from fractions import Fraction as F

ZERO = F(0)
ONE = F(1)
I = ((ONE, ZERO), (ZERO, ONE))


def add(A, B):
    return tuple(tuple(A[i][j] + B[i][j] for j in range(2)) for i in range(2))


def neg(A):
    return scale(A, -ONE)


def sub(A, B):
    return add(A, neg(B))


def scale(A, c):
    return tuple(tuple(c * A[i][j] for j in range(2)) for i in range(2))


def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def mv(A, e):
    return tuple(sum(A[i][j] * e[j] for j in range(2)) for i in range(2))


def outer(v):
    return tuple(tuple(v[i] * v[j] for j in range(2)) for i in range(2))


def power(A, n):
    R = I
    for _ in range(n):
        R = mul(R, A)
    return R


def quadratic(A, e):
    w = mv(A, e)
    return sum(e[i] * w[i] for i in range(2))


def epoch_matrices(u, v, alpha):
    P, Q = outer(u), outer(v)
    B, C = sub(I, scale(P, alpha)), sub(I, scale(Q, alpha))
    cross1 = mul(mul(B, mul(C, C)), B)
    cross2 = mul(mul(C, mul(B, B)), C)
    E_iid = scale(add(add(power(B, 4), power(C, 4)), add(cross1, cross2)), F(1, 4))
    E_rr = scale(add(cross1, cross2), F(1, 2))
    return P, Q, E_iid, E_rr


def unit_rational_vector(t):
    # Rational parameterization of the first-quadrant unit circle.
    return ((ONE - t*t)/(ONE+t*t), (2*t)/(ONE+t*t))


def check():
    count = 0
    u = (ONE, ZERO)
    for t in [F(1, 7), F(1, 4), F(1, 3), F(1, 2), F(2, 3), F(3, 4)]:
        v = unit_rational_vector(t)
        rho = v[0]
        assert ZERO < rho < ONE
        assert sum(a*a for a in v) == ONE
        for alpha in [F(1, 5), F(3, 4), ONE, F(11, 10), F(5, 4), F(3, 2), F(7, 4), F(19, 10)]:
            P, Q, Ei, Er = epoch_matrices(u, v, alpha)
            D = sub(Ei, Er)
            beta = alpha * (2-alpha)
            formula = scale(sub(scale(add(P, Q), beta + alpha*alpha*rho*rho),
                                scale(add(mul(P, Q), mul(Q, P)), 2*alpha)), beta/4)
            assert D == formula, (t, alpha, 'matrix identity')
            ep = tuple(u[j]+v[j] for j in range(2))
            em = tuple(u[j]-v[j] for j in range(2))
            lp = alpha*alpha*(2-alpha)*(1-rho*rho)*(2-alpha*(1+rho))/4
            lm = alpha*alpha*(2-alpha)*(1-rho*rho)*(2-alpha*(1-rho))/4
            assert mv(D, ep) == tuple(lp*x for x in ep), (t, alpha, 'plus eigenspace')
            assert mv(D, em) == tuple(lm*x for x in em), (t, alpha, 'minus eigenspace')
            assert lm > 0
            assert (lp > 0) == (alpha < 2/(1+rho)) if alpha != 2/(1+rho) else lp == 0
            count += 4
    # An explicit fully rational nonzero initial error and stable overrelaxation.
    v = (F(3, 5), F(4, 5))
    e = (F(2), F(1))
    alpha = F(3, 2)
    _, _, Ei, Er = epoch_matrices(u, v, alpha)
    assert quadratic(Ei, e) == F(161, 100)
    assert quadratic(Er, e) == F(197, 100)
    assert quadratic(Er, e) - quadratic(Ei, e) == F(9, 25)
    assert quadratic(Ei, e) < 5 and quadratic(Er, e) < 5
    count += 4
    # At alpha=2, each update is an isometry and both expected Gram matrices equal I.
    for t in [F(1, 7), F(1, 2), F(3, 4)]:
        v = unit_rational_vector(t)
        _, _, Ei, Er = epoch_matrices(u, v, F(2))
        assert Ei == I and Er == I
        count += 2
    print(f'VERIFY_OK {count} exact rational matrix/eigenmode/witness checks')


if __name__ == '__main__':
    check()
