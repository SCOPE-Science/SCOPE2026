"""Exact-rational consistency checks for the quadratic APAPC stability frontier.

No numerical eigensolver or external package is required. The general theorem
rests on the singular-mode decomposition and the quadratic Schur criterion.
"""
from fractions import Fraction as Q
from itertools import product


def mode(a, gamma, mu, lam, tau, s):
    r = 1 / (1 + a * gamma * mu)
    d = 1 / (1 + tau / (a * lam))
    c = a * gamma * s
    b = tau * s / a
    m = b * c
    # Assemble the update directly by propagating basis vectors rather
    # than inserting the claimed closed matrix formula.
    def update(z, v):
        zhat = r * (z - c * v)
        vnew = d * (v + b * zhat)
        znew = r * (z - c * vnew)
        return znew, vnew
    z1, v1 = update(Q(1), Q(0))
    z2, v2 = update(Q(0), Q(1))
    M = ((z1, z2), (v1, v2))
    assert M == ((r * (1 - d * m * r), -r * c * d * (1 - m * r)),
                 (d * b * r, d * (1 - m * r)))
    trace = M[0][0] + M[1][1]
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    assert trace == r + d - d * m * r * (1 + r)
    assert det == r * d * (1 - m * r)
    j1, j2, j3 = 1 - trace + det, 1 - det, 1 + trace + det
    assert j1 == (1 - r) * (1 - d) + d * m * r
    assert j2 == 1 - r * d + d * m * r * r
    assert j3 == (1 + r) * (1 + d) - d * m * r * (1 + 2 * r)
    assert j1 > 0 and j2 > 0
    alpha = a * gamma * mu
    threshold = (1 + alpha) * (2 + alpha) * (2 + tau / (a * lam)) / (3 + alpha)
    assert (j3 > 0) == (gamma * tau * s * s < threshold)
    assert (j3 == 0) == (gamma * tau * s * s == threshold)
    assert (j3 < 0) == (gamma * tau * s * s > threshold)
    return M, j3


def main():
    cases = 0
    for a, gamma, mu, lam, tau, s in product(
            (Q(1), Q(2), Q(5)),
            (Q(1, 5), Q(1), Q(7, 3)),
            (Q(1, 4), Q(1), Q(3)),
            (Q(1, 9), Q(1), Q(4)),
            (Q(1, 7), Q(1), Q(3), Q(30)),
            (Q(0), Q(1, 2), Q(2))):
        mode(a, gamma, mu, lam, tau, s)
        cases += 1
    assert cases == 3 * 3 * 3 * 3 * 4 * 3
    M, j3 = mode(Q(1), Q(1), Q(1), Q(1), Q(6, 5), Q(2))
    assert j3 == 0
    assert (1 + M[0][0]) * (1 + M[1][1]) - M[0][1] * M[1][0] == 0
    assert M == ((Q(-1, 22), Q(7, 11)),
                 (Q(6, 11), Q(-7, 11)))
    assert mode(Q(1), Q(1), Q(1), Q(1), Q(2), Q(2))[1] < 0
    # Strong curvature permits all finite dual steps in this example.
    for tau in (Q(1), Q(2), Q(10), Q(1000), Q(10**10)):
        assert mode(Q(1), Q(1), Q(1), Q(1), tau, Q(1))[1] > 0
    print('VERIFY_OK', cases, 'exact-rational parameter tuples')


if __name__ == '__main__':
    main()
