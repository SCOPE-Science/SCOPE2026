"""Exact finite-field checks of the rank-one Grassmann-distance calculation.

Run: python3 verify.py
Each test is exact, but finite tests do not prove an infinite-degree theorem.
"""

P = 1000003


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def deriv(a):
    return trim([(j * a[j]) % P for j in range(1, len(a))] or [0])


def mult(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            c[i + j] = (c[i + j] + v * w) % P
    return trim(c)


def sub(a, b):
    return trim([((a[i] if i < len(a) else 0) -
                  (b[i] if i < len(b) else 0)) % P
                 for i in range(max(len(a), len(b)))])


def remainder(a, b):
    a = a[:]
    while len(a) >= len(b) and a != [0]:
        q = a[-1] * pow(b[-1], -1, P) % P
        step = len(a) - len(b)
        for j, v in enumerate(b):
            a[j + step] = (a[j + step] - q * v) % P
        trim(a)
    return a


def gcd(a, b):
    while b != [0]:
        a, b = b, remainder(a, b)
    return trim(a)


def check(n):
    assert n >= 2
    a = [((j + 1) ** 3 + (j + 2) ** 2 + 1) % P for j in range(n + 1)]
    S = [int(j % 2 == 0) for j in range(2 * n + 1)]
    A = a[:]
    W = sub(mult([2], mult(deriv(A), S)), mult(A, deriv(S)))
    assert len(W) - 1 == 3 * n - 2, (n, len(W))
    assert W[-1] == (-2 * a[n - 1]) % P
    for b, c in [(A, deriv(A)), (S, deriv(S)), (A, S),
                 (W, deriv(W)), (W, A), (W, S)]:
        assert len(gcd(b, c)) == 1, (n, b[:5], c[:5])
    return len(W) - 1, len(A) - 1


if __name__ == '__main__':
    values = [check(n) for n in range(2, 21)]
    assert values == [(3*n - 2, n) for n in range(2, 21)]
    print('VERIFY_OK: exact GF(1000003) polynomial checks for n=2..20;'
          ' W has degree 3n-2, is squarefree, and misses the cut and poles.')
