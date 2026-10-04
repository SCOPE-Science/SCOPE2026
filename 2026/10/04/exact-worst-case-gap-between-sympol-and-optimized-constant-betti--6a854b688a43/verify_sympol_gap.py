from __future__ import annotations
import math
import random


def A_values(e):
    n = len(e)
    coeff = [1.0] + [0.0] * n
    for x in e:
        for j in range(n, 0, -1):
            coeff[j] += x * coeff[j - 1]
    return [coeff[k] / math.comb(n, k) for k in range(n + 1)]


def product_stat(e, lam):
    out = 1.0
    for x in e:
        out *= 1.0 - lam + lam * x
    return out


def bernstein_sum(A, lam):
    n = len(A) - 1
    return sum(math.comb(n, k) * lam**k * (1.0 - lam)**(n-k) * A[k]
               for k in range(n + 1))


def b(n, k):
    if k == 0 or k == n:
        return 1.0
    return math.comb(n, k) * (k / n)**k * ((n-k) / n)**(n-k)


def central_factor(n):
    return 1.0 / b(n, n // 2)


def sparse_ratio(n, k, L):
    e = [L] * k + [0.0] * (n-k)
    A = A_values(e)
    S = max(A)
    if k == 0:
        K = 1.0
    else:
        # Exact maximizer of (1+(L-1)lambda)^k(1-lambda)^(n-k), clipped to [0,1].
        if L == 1.0:
            lam = 0.0
        else:
            lam = (k * L - n) / (n * (L - 1.0))
            lam = min(1.0, max(0.0, lam))
        K = product_stat(e, lam)
    return S / K


random.seed(31)
for n in range(1, 41):
    vals = [b(n, k) for k in range(n + 1)]
    mn = min(vals)
    assert abs(mn - vals[n // 2]) < 1e-12
    if n % 2 == 0:
        m = n // 2
        closed = 4.0**m / math.comb(2*m, m)
    else:
        m = n // 2
        closed = (2*m + 1.0)**(2*m + 1) / (math.comb(2*m+1, m) * (m**m if m else 1.0) * (m+1.0)**(m+1))
    assert abs(closed / central_factor(n) - 1.0) < 1e-11

for n in range(2, 15):
    for _ in range(20):
        e = [10.0 ** random.uniform(-1.5, 1.5) for _ in range(n)]
        A = A_values(e)
        k = max(range(n + 1), key=lambda j: A[j])
        lam = k / n
        lhs = product_stat(e, lam)
        rhs = bernstein_sum(A, lam)
        assert abs(lhs - rhs) <= 1e-9 * max(1.0, abs(lhs), abs(rhs))
        assert lhs + 1e-12 >= b(n, k) * A[k]
        assert lhs + 1e-12 >= min(b(n, j) for j in range(n + 1)) * max(A)

for n in [2, 3, 4, 5, 10, 11, 20, 21]:
    k = n // 2
    target = central_factor(n)
    r1 = sparse_ratio(n, k, 1e4)
    r2 = sparse_ratio(n, k, 1e8)
    assert r2 >= r1 * (1.0 - 1e-8)
    assert abs(r2 / target - 1.0) < 5e-6

print('VERIFY_OK')
