from math import prod


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    m = n
    p = 2
    mu = 1
    while p * p <= m:
        if m % p == 0:
            m //= p
            mu = -mu
            if m % p == 0:
                return 0
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        mu = -mu
    return mu


def chi1(n):
    return 1


def chi5(n):
    r = n % 5
    if r == 0:
        return 0
    return 1 if r in (1, 4) else -1


def endpoint(ell, e, n, chi):
    k = ell - 2 * e
    return n ** (2 * e) * sum(chi(d) * d ** (k - 1) for d in divisors(n))


def inverse_weight(ell, d, chi):
    return mobius(d) * chi(d) * d ** (ell - 1)


def determinant_bareiss(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    denominator = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot_row = next(j for j in range(k + 1, n) if a[j][k] != 0)
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // denominator
        denominator = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]


def vandermonde_formula(r):
    x = [n * n for n in range(1, r + 1)]
    return prod(x) * prod(x[j] - x[i] for i in range(r) for j in range(i + 1, r))


def check(ell, r, chi, label):
    endpoint_matrix = [
        [endpoint(ell, e, n, chi) for n in range(1, r + 1)]
        for e in range(1, r + 1)
    ]
    transform = [[0] * r for _ in range(r)]
    for new_n in range(1, r + 1):
        for d in divisors(new_n):
            old_n = new_n // d
            transform[old_n - 1][new_n - 1] += inverse_weight(ell, d, chi)
    transformed = [
        [sum(endpoint_matrix[i][j] * transform[j][k] for j in range(r)) for k in range(r)]
        for i in range(r)
    ]
    vandermonde = [
        [n ** (2 * e) for n in range(1, r + 1)]
        for e in range(1, r + 1)
    ]
    assert transformed == vandermonde
    assert determinant_bareiss(transform) == 1
    det_v = determinant_bareiss(vandermonde)
    assert det_v == vandermonde_formula(r)
    assert det_v > 0
    print(f"{label}: ell={ell}, r={r}, transform_exact=True, det(T)=1, det(W)={det_v}")


for r in range(1, 7):
    check(24, r, chi1, "D=1")
for r in range(1, 8):
    check(24, r, chi5, "D=5")
