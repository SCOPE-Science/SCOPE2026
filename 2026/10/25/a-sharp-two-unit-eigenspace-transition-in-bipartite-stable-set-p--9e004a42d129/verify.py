"""Exact, independent simplex-chamber second-moment checks for a polytope family.

Run: python verify.py. Uses only Python's standard library.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial


def formulas(p, q):
    d = p + q
    a, b = d + 1, d + 2
    tp = F((p + 1) * (p + 2), 12 * a * b)
    tq = F((q + 1) * (q + 2), 12 * a * b)
    up = F((p + 1) * (p*p + 4*p*q + 3*p + 2*q + 2), 12 * a*a*b)
    uq = F((q + 1) * (q*q + 4*p*q + 3*q + 2*p + 2), 12 * a*a*b)
    cross = -F((p + 1) * (q + 1), 4 * a*a*b)
    mu = [F(p+1, 2*a)] * p + [F(q+1, 2*a)] * q
    diag_p = (up + (p - 1)*tp)/p
    off_p = (up-tp)/p
    diag_q = (uq + (q - 1)*tq)/q
    off_q = (uq-tq)/q
    cov = [[diag_p if i == j else off_p for j in range(p)] + [cross]*q for i in range(p)]
    cov += [[cross]*p + [diag_q if i == j else off_q for j in range(q)] for i in range(q)]
    return mu, cov, tp, tq, up, uq, cross


def chamber_moments(p, q):
    """Integrate independently, treating each order chamber as a unit simplex.

    Build the nonzero vertices as indicator vectors of suffixes in both blocks;
    the origin is the (d+1)st simplex vertex.
    """
    d = p+q
    sums = [0]*d
    squares = [[0]*d for _ in range(d)]
    chambers = 0
    for sx in permutations(range(p)):
        for sy in permutations(range(q)):
            vertices = []
            for k in range(p):
                v = [0]*d
                for j in range(k, p):
                    v[sx[j]] = 1
                vertices.append(v)
            for k in range(q):
                v = [0]*d
                for j in range(k, q):
                    v[p+sy[j]] = 1
                vertices.append(v)
            total = [sum(v[i] for v in vertices) for i in range(d)]
            for i in range(d):
                sums[i] += total[i]
                for j in range(d):
                    squares[i][j] += total[i]*total[j] + sum(v[i]*v[j] for v in vertices)
            chambers += 1
    mean = [F(s, chambers*(d+1)) for s in sums]
    cov = [[F(squares[i][j], chambers*(d+1)*(d+2))-mean[i]*mean[j] for j in range(d)] for i in range(d)]
    return mean, cov, chambers


def run():
    count = 0
    ch = 0
    for p in range(2,5):
        for q in range(2,5):
            actual_mean, actual_cov, nc = chamber_moments(p,q)
            expected_mean, expected_cov, *_ = formulas(p,q)
            assert actual_mean == expected_mean, (p,q,'mean')
            assert actual_cov == expected_cov, (p,q,'covariance')
            assert nc == factorial(p)*factorial(q)
            count += 1
            ch += nc
    comparisons = 0
    for p in range(2,51):
        for q in range(2,51):
            _, _, tp, tq, up, uq, cross = formulas(p,q)
            d = p+q
            determinant = up*uq-F(p*q,1)*cross*cross
            predicted_det = F((p+1)*(q+1)*(2*p*q+p+q+2),72*(d+1)**2*(d+2)**2)
            assert determinant == predicted_det
            small = min(p,q)
            large = max(p,q)
            tm = min(tp,tq)
            determinant_shift = (up-tm)*(uq-tm)-F(p*q,1)*cross*cross
            predicted_shift = F(large*small*(small+1)*(large*large-small*small-3*small-3),48*(d+1)**3*(d+2)**2)
            assert determinant_shift == predicted_shift
            assert (determinant_shift > 0) == (large-small >= 2)
            assert (up-tm) > 0 and (uq-tm) > 0
            if p == q:
                # In this symmetric case the largest 2x2 eigenvalue is up-p*cross.
                assert up-p*cross == F(1,12)
                assert up+p*cross == F(p*p+p+1,12*(2*p+1)**2)
            comparisons += 1
    print(f'VERIFY_OK chamber_parameter_pairs={count} independent_chambers={ch} exact_matrix_entries={sum((p+q)**2 for p in range(2,5) for q in range(2,5))} rational_phase_cases={comparisons} balanced_lambda_max=1/12')


if __name__=='__main__':
    run()
