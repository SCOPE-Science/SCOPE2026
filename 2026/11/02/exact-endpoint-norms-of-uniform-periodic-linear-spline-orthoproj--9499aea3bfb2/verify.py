"""Exact finite-size checks for periodic degree-one spline orthoprojectors.

Run with Python 3 (standard library only): python verify.py
The infinite-dimensional claims are proved analytically in RESULT.md, not by this script.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext


def gram_six(n):
    assert n >= 3
    a = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        a[i][i] += 4
        a[i][(i - 1) % n] += 1
        a[i][(i + 1) % n] += 1
    return a


def solve(A, rhs):
    """Independent rational Gaussian elimination (no floating point)."""
    n = len(A)
    a = [list(row) + [rhs[i]] for i, row in enumerate(A)]
    for j in range(n):
        k = next(i for i in range(j, n) if a[i][j])
        a[k], a[j] = a[j], a[k]
        d = a[j][j]
        for t in range(j, n + 1):
            a[j][t] /= d
        for i in range(n):
            if i == j or not a[i][j]:
                continue
            b = a[i][j]
            for t in range(j, n + 1):
                a[i][t] -= b * a[j][t]
    return [a[i][n] for i in range(n)]


def F_closed(a, b):
    if a * b >= 0:
        return (abs(a) + abs(b)) / 2
    return (a*a + b*b) / (2 * (abs(a) + abs(b)))


def F_split(a, b):
    """Integrate |a+(b-a)t| via separate positive and negative linear pieces."""
    def prim(t):
        return a * t + (b - a) * t*t / 2
    if a*b < 0:
        t0 = -a / (b-a)
        return abs(prim(t0) - prim(Q(0))) + abs(prim(Q(1)) - prim(t0))
    return abs(prim(Q(1)) - prim(Q(0)))


def a_closed(n):
    with localcontext() as c:
        c.prec = 65
        r = Decimal(2) - Decimal(3).sqrt()
        q = -r
        c3 = Decimal(3).sqrt()
        return [c3 * (q**j + q**(n-j))/(1-q**n) for j in range(n)]


def run():
    checks = 0
    examples = {}
    for n in range(3, 26):
        A = gram_six(n)
        row = solve(A, [Q(6) if i == 0 else Q(0) for i in range(n)])
        for i in range(n):
            assert sum(A[i][j] * row[j] for j in range(n)) == (Q(6) if i == 0 else Q(0))
            checks += 1
        assert sum(row) == 1
        checks += 1
        formula = a_closed(n)
        for i in range(n):
            with localcontext() as ctx:
                ctx.prec=65
                assert abs(Decimal(row[i].numerator)/Decimal(row[i].denominator) - formula[i]) < Decimal('1e-45')
            checks += 1
        L = Q(0)
        for i in range(n):
            a, b = row[i], row[(i+1)%n]
            assert F_closed(a,b) == F_split(a,b)
            L += F_split(a,b)
            checks += 1
        assert Q(1) < L < Q(2)
        checks += 1
        # Independent rectangular quadrature of each piece via midpoint samples.
        approximate = Q(0)
        pieces = 1024
        for i in range(n):
            a,b = row[i],row[(i+1)%n]
            approximate += sum(abs(a+(b-a)*Q(2*k+1,2*pieces)) for k in range(pieces))/pieces
        assert abs(float(approximate-L)) < 3e-6
        checks += 1
        if n <= 10: examples[n] = str(L)
    for n,v in {3:'16/9',4:'17/9',5:'257/132',6:'2923/1485',7:'14659/7380',8:'8083/4059'}.items():
        assert examples[n] == v
        checks += 1
    print('PASS: {} exact and high-precision finite checks, dimensions 3..25'.format(checks))
    print('Exact operator norms:',examples)
    print('Analytical strict-2 bound, attainment and infinite-period limit are in RESULT.md.')

if __name__ == '__main__':
    run()
