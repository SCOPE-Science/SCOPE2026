"""Standalone high-precision checks for the exponential closed-FSBP theorem.
Run: python verify.py (Python 3.11+, standard library only).
These checks supplement, and do not replace, the analytic proof.
"""
from decimal import Decimal, localcontext

PREC = 95
ONE = Decimal(1)
TWO = Decimal(2)
ZERO = Decimal(0)


def sinh(x):
    return (x.exp() - (-x).exp()) / TWO


def cosh(x):
    return (x.exp() + (-x).exp()) / TWO


def acosh(x):
    return (x + (x * x - ONE).sqrt()).ln()


def data(lam):
    c = cosh(lam)
    mu = sinh(lam) / lam
    mu2 = ONE / TWO + sinh(TWO * lam) / (Decimal(4) * lam)
    v = mu2 - mu * mu
    delta = c - mu
    t = mu - v / delta
    a = acosh(t) / lam
    we = v / (delta * delta + v)
    wi = ONE - we
    assert ZERO < v and ONE < t < mu < c
    assert ZERO < a < ONE and ZERO < we < ONE and ZERO < wi < ONE
    return a, we, wi


def solve(mat, y):
    n = len(mat)
    A = [list(mat[i]) + [y[i]] for i in range(n)]
    for col in range(n):
        p = max(range(col, n), key=lambda k: abs(A[k][col]))
        assert A[p][col] != ZERO
        A[p], A[col] = A[col], A[p]
        pv = A[col][col]
        for j in range(col, n + 1):
            A[col][j] /= pv
        for i in range(n):
            if i == col:
                continue
            fac = A[i][col]
            for j in range(col, n + 1):
                A[i][j] -= fac * A[col][j]
    return [A[i][n] for i in range(n)]


def check(lam):
    a, we, wi = data(lam)
    x = [-ONE, -a, a, ONE]
    weights = [we, wi, wi, we]
    max_quad = ZERO
    for k in (-2, -1, 0, 1, 2):
        target = TWO if k == 0 else TWO * sinh(Decimal(k) * lam) / (Decimal(k) * lam)
        approx = sum((weights[j] * (Decimal(k) * lam * x[j]).exp() for j in range(4)), ZERO)
        err = abs(approx - target) / (ONE + abs(target))
        max_quad = max(max_quad, err)
    assert max_quad < Decimal('1e-55'), (lam, max_quad)

    V = [[ONE, (lam * x[i]).exp(), (-lam * x[i]).exp()] for i in range(4)]
    Vp = [[ZERO, lam * V[i][1], -lam * V[i][2]] for i in range(4)]
    Bdiag = [Decimal(-1), ZERO, ZERO, ONE]
    K = [[weights[i] * Vp[i][k] - Bdiag[i] * V[i][k] / TWO for k in range(3)] for i in range(4)]
    pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    rows = []
    rhs = []
    for i in range(4):
        for k in range(3):
            row = []
            for p, q in pairs:
                row.append((V[q][k] if i == p else -V[p][k] if i == q else ZERO))
            rows.append(row)
            rhs.append(K[i][k])
    G = [[sum((row[p] * row[q] for row in rows), ZERO) for q in range(6)] for p in range(6)]
    b = [sum((row[p] * rhs[r] for r, row in enumerate(rows)), ZERO) for p in range(6)]
    vals = solve(G, b)
    residual = max(abs(sum((rows[r][j] * vals[j] for j in range(6)), ZERO) - rhs[r]) for r in range(12))
    scale = ONE + max(abs(z) for z in rhs)
    assert residual / scale < Decimal('1e-52'), (lam, residual / scale)
    S = [[ZERO for _ in range(4)] for _ in range(4)]
    for (i, j), value in zip(pairs, vals):
        S[i][j], S[j][i] = value, -value
    Q = [[S[i][j] + (Bdiag[i] / TWO if i == j else ZERO) for j in range(4)] for i in range(4)]
    err_q = max(abs(Q[i][j] + Q[j][i] - (Bdiag[i] if i == j else ZERO)) for i in range(4) for j in range(4))
    err_d = max(abs(sum((Q[i][j] * V[j][k] for j in range(4)), ZERO) / weights[i] - Vp[i][k]) for i in range(4) for k in range(3))
    assert err_q == ZERO
    assert err_d / (ONE + max(abs(z) for r in Vp for z in r)) < Decimal('1e-51')
    c = cosh(lam)
    mass3 = TWO * sinh(lam) * (c + TWO) / (lam * (TWO * c + ONE))
    assert mass3 > TWO
    return max_quad, residual / scale


def main():
    with localcontext() as ctx:
        ctx.prec = PREC
        samples = [Decimal('0.0625'), Decimal('0.125'), Decimal('0.25'), Decimal('0.5'), ONE,
                   TWO, Decimal('3'), Decimal('5'), Decimal('8')]
        for lam in samples:
            q, r = check(lam)
            print('lambda=', str(lam), 'quadrature_relative=', format(q, '.2E'),
                  'SBP_relative=', format(r, '.2E'))
        for lam in [Decimal(24), Decimal(48), Decimal(96), Decimal(192)]:
            a, we, _ = data(lam)
            estimate = lam * (ONE - a) - (TWO * lam).ln()
            print('asymptotic lambda=', str(lam), 'inner_layer_offset=', format(estimate, '.8E'),
                  'lambda_times_endpoint_weight=', format(lam * we, '.12f'))
        print('PASS: exact-exponential moments, positive weights, four-point SBP matrices, three-point mass defect, asymptotic trends')


if __name__ == '__main__':
    main()
