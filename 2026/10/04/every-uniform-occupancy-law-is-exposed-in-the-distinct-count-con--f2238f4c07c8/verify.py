from fractions import Fraction


def stirling2(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0 or k > n:
        return 0
    row = [0] * (k + 1)
    row[0] = 1
    for i in range(1, n + 1):
        nxt = [0] * (k + 1)
        for j in range(1, min(i, k) + 1):
            nxt[j] = row[j - 1] + j * row[j]
        row = nxt
    return row[k]


def mul(a, b):
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def p_poly(n, k):
    s = Fraction(stirling2(n, k))
    p = [Fraction(0)] * (n - k) + [s]
    for j in range(1, k):
        p = mul(p, [Fraction(1), Fraction(-j)])
    p += [Fraction(0)] * (n - len(p))
    return p


def solve_basis(polys, target):
    n = len(polys)
    A = [[polys[col][row] for col in range(n)] + [target[row]] for row in range(n)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if A[r][col] != 0)
        A[col], A[pivot] = A[pivot], A[col]
        q = A[col][col]
        A[col] = [v / q for v in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                q = A[r][col]
                A[r] = [A[r][j] - q * A[col][j] for j in range(n + 1)]
    return [A[i][-1] for i in range(n)]


def eval_poly(p, x):
    acc = Fraction(0)
    for a in reversed(p):
        acc = acc * x + a
    return acc


def lincomb(coeffs, polys):
    n = len(polys)
    out = [Fraction(0)] * n
    for c, p in zip(coeffs, polys):
        for j, a in enumerate(p):
            out[j] += c * a
    return out


for n in range(3, 16):
    polys = [p_poly(n, k) for k in range(1, n + 1)]
    for k, p in enumerate(polys, start=1):
        d = n - k
        assert all(p[j] == 0 for j in range(d))
        assert p[d] == stirling2(n, k)
    total = [sum(p[j] for p in polys) for j in range(n)]
    assert total == [Fraction(1)] + [Fraction(0)] * (n - 1)

    for m0 in range(1, 9):
        a = Fraction(1, m0)
        target = [-a * a, 2 * a, Fraction(-1)] + [Fraction(0)] * (n - 3)
        coeffs = solve_basis(polys, target)
        assert lincomb(coeffs, polys) == target
        assert eval_poly(target, a) == 0
        assert eval_poly(target, Fraction(0)) < 0
        for m in range(1, 13):
            x = Fraction(1, m)
            if m == m0:
                assert eval_poly(target, x) == 0
            else:
                assert eval_poly(target, x) < 0

    target_inf = [Fraction(0), Fraction(-1)] + [Fraction(0)] * (n - 2)
    coeffs_inf = solve_basis(polys, target_inf)
    assert lincomb(coeffs_inf, polys) == target_inf
    assert eval_poly(target_inf, Fraction(0)) == 0
    for m in range(1, 13):
        assert eval_poly(target_inf, Fraction(1, m)) < 0

print('VERIFY_OK')
