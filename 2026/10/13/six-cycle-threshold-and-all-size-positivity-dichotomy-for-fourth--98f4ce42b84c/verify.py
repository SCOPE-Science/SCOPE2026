"""Exact polynomial certificates for a fourth-order Gauss step on cycles.

Run: python verify.py. Requires only Python's standard library.
Each identity is checked coefficient-by-coefficient over the rationals.
"""
from fractions import Fraction as F


def polynomial(*coefficients):
    return [F(x) for x in coefficients]


def add(*polynomials):
    n = max(len(x) for x in polynomials)
    return trim([sum((x[i] if i < len(x) else 0) for x in polynomials)
                 for i in range(n)])


def trim(coefficients):
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    return coefficients


def mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def scale(a, c):
    return trim([F(c) * x for x in a])


def matmul(a, b):
    n = len(a)
    return [[add(*(mul(a[i][k], b[k][j]) for k in range(n)))
             for j in range(n)] for i in range(n)]


def matsum(*matrices):
    n = len(matrices[0])
    return [[add(*(a[i][j] for a in matrices)) for j in range(n)]
            for i in range(n)]


def matscale(a, q):
    return [[mul(x, q) for x in row] for row in a]


def identity(n):
    return [[polynomial(int(i == j)) for j in range(n)]
            for i in range(n)]


def cycle_generator(n):
    q = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        j = (i + 1) % n
        q[i][j] = q[j][i] = F(1)
    for i in range(n):
        q[i][i] = -sum(q[i][j] for j in range(n) if j != i)
    return [[polynomial(x) for x in row] for row in q]


def verify_symbolic(n, denominator, numerators_by_distance):
    q = cycle_generator(n)
    q2 = matmul(q, q)
    numerator = matsum(matscale(identity(n), polynomial(12)),
                       matscale(q, polynomial(0, 6)),
                       matscale(q2, polynomial(0, 0, 1)))
    denominator_matrix = matsum(matscale(identity(n), polynomial(12)),
                                matscale(q, polynomial(0, -6)),
                                matscale(q2, polynomial(0, 0, 1)))
    t_numerators = [[numerators_by_distance[min((i-j) % n, (j-i) % n)]
                     for j in range(n)] for i in range(n)]
    # A matrix identity over Q[h], not numerical sampling.
    left = matmul(denominator_matrix, t_numerators)
    right = matscale(numerator, denominator)
    for i in range(n):
        for j in range(n):
            assert left[i][j] == right[i][j], (n, i, j)
    # Independent stochasticity certificate: every numerator row adds to the denominator.
    for row in t_numerators:
        assert add(*row) == denominator
    print('EXACT_POLYNOMIAL_IDENTITY_OK', n)


D3 = polynomial(4, 6, 3)
verify_symbolic(3, D3, {
    0: polynomial(4, -2, 3),
    1: polynomial(0, 4)
})

D4 = mul(polynomial(3, 3, 1), polynomial(3, 6, 4))
verify_symbolic(4, D4, {
    0: polynomial(9, 9, 6, 3, 4),
    1: mul(polynomial(0, 3), polynomial(3, 3, 1)),
    2: scale(mul(polynomial(0, 0, 1), polynomial(1, 1)), 9)
})

D5 = polynomial(144, 360, 360, 150, 25)
verify_symbolic(5, D5, {
    0: polynomial(144, 72, 72, 30, 25),
    1: scale(mul(polynomial(0, 1), polynomial(2, 1)), 72),
    2: scale(mul(polynomial(0, 0, 1), polynomial(6, 5)), 12)
})

D6 = mul(mul(polynomial(12, 6, 1), polynomial(4, 6, 3)),
         polynomial(3, 6, 4))
F6 = polynomial(-72, -144, -102, -12, 5)
verify_symbolic(6, D6, {
    0: polynomial(144, 288, 276, 168, 121, 44, 12),
    1: scale(mul(polynomial(0, 1), F6), -2),
    2: scale(mul(polynomial(0, 0, 1), polynomial(36, 72, 48, 13)), 2),
    3: scale(mul(polynomial(0, 0, 0, 1), polynomial(24, 48, 19)), 2)
})


def evaluate(p, h):
    return sum(c * F(h) ** i for i, c in enumerate(p))

witness = -2 * 7 * evaluate(F6, 7) / evaluate(D6, 7)
assert witness == -F(25354, 4790839)
assert evaluate(F6, 6) < 0 < evaluate(F6, 7)
assert F6[-1] > 0 and all(c < 0 for c in F6[:-1])

# The following rational calculations corroborate, but do not prove,
# the all-size pseudoinverse identity established in the accompanying proof.
for n in range(3, 12):
    g = [F(n*n-1, 12*n)-F(d*(n-d), 2*n) for d in range(n)]
    assert sum(g) == 0
    for d in range(n):
        lap = 2*g[d] - g[(d-1) % n] - g[(d+1) % n]
        assert lap == (1 if d == 0 else 0) - F(1, n)

print('VERIFY_OK')
print('C6_h7_adjacent_probability', witness)
