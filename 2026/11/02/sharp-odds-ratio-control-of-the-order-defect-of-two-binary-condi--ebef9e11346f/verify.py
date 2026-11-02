"""Exact-rational verification of four-state conditional-expectation commutator identities.

Run with Python 3.9+: python verify.py
No nonstandard dependencies are required.
The all-positive-parameter theorem is proved algebraically in RESULT.md;
these exact tests independently reconstruct conditional expectations.
"""
from fractions import Fraction as F
from itertools import product


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4))
             for j in range(4)] for i in range(4)]


def commutator(a, b, c, d):
    w = (F(a), F(b), F(c), F(d))
    P = [[F(0) for _ in range(4)] for _ in range(4)]
    Q = [[F(0) for _ in range(4)] for _ in range(4)]
    for group in ((0, 1), (2, 3)):
        mass = sum(w[j] for j in group)
        for i in group:
            for j in group:
                P[i][j] = w[j] / mass
    for group in ((0, 2), (1, 3)):
        mass = sum(w[j] for j in group)
        for i in group:
            for j in group:
                Q[i][j] = w[j] / mass
    PQ = mm(P, Q)
    QP = mm(Q, P)
    return [[PQ[i][j] - QP[i][j] for j in range(4)] for i in range(4)]


def predicted_matrix(a, b, c, d):
    a, b, c, d = map(F, (a, b, c, d))
    u, v = b/(a+b), d/(c+d)
    r, s = c/(a+c), d/(b+d)
    dx, dy = s-r, v-u
    return [
        [F(0), -u*dx, r*dy, u*dx-r*dy],
        [(1-u)*dx, F(0), s*dy-(1-u)*dx, -s*dy],
        [-(1-r)*dy, (1-r)*dy-v*dx, F(0), v*dx],
        [(1-v)*dx-(1-s)*dy, (1-s)*dy, -(1-v)*dx, F(0)],
    ]


def exact_norm_formula(a, b, c, d):
    a, b, c, d = map(F, (a, b, c, d))
    u, v = b/(a+b), d/(c+d)
    r, s = c/(a+c), d/(b+d)
    return 2*max(abs(s-r)*max(u, v, 1-u, 1-v),
                 abs(v-u)*max(r, s, 1-r, 1-s))


def true_norm(K):
    return max(sum(abs(t) for t in row) for row in K)


def prove_radical_bound_exact(a, b, c, d, norm):
    """Avoid floating point square roots by squaring positive sides."""
    ad, bc = F(a)*d, F(b)*c
    if ad == bc:
        assert norm == 0
        return
    g = norm / 2
    assert F(0) < g < 1
    lo, hi = sorted((ad, bc))
    assert (1+g)**2 * lo < (1-g)**2 * hi


def main():
    cases = 0
    for a, b, c, d in product(range(1, 9), repeat=4):
        K = commutator(a, b, c, d)
        assert K == predicted_matrix(a, b, c, d)
        norm = true_norm(K)
        assert norm == exact_norm_formula(a, b, c, d)
        assert all(sum(row) == 0 for row in K)
        prove_radical_bound_exact(a, b, c, d, norm)
        cases += 1

    limits = 0
    for root in (F(2), F(1, 3), F(3, 2), F(1, 2), F(5)):
        theta = root*root
        target = 2*abs(root-1)/(root+1)
        for t in (2**12, 2**18, 2**24):
            # a=sqrt(theta)*t, b=t, c=1/sqrt(theta), d=1.
            # Explicit proof gives the target as the supremum.
            norm = true_norm(commutator(root*t, t, 1/root, 1))
            assert 0 <= target-norm < F(8, t)
            limits += 1
    print('VERIFY_OK; exact_four_cell_tables=', cases,
          'matrix_and_row_checks=', 3*cases,
          'sharp_sequence_checks=', limits)


if __name__ == '__main__':
    main()
