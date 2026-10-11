"""Supplementary numerical spot checks of exact path observability identities.

The universal theorem is analytic; these small cases are regression tests only.
Uses only Python's standard library.
"""
import math


def det(a):
    a = [row[:] for row in a]
    n = len(a)
    result = 1.0
    for k in range(n):
        pivot = max(range(k, n), key=lambda i: abs(a[i][k]))
        if abs(a[pivot][k]) < 1e-14:
            return 0.0
        if pivot != k:
            a[pivot], a[k] = a[k], a[pivot]
            result = -result
        d = a[k][k]
        result *= d
        for i in range(k + 1, n):
            c = a[i][k] / d
            for j in range(k + 1, n):
                a[i][j] -= c * a[k][j]
            a[i][k] = 0.0
    return result


def predicted(m, j, phi):
    d = math.gcd(j, m)
    if (m // d) % 2 == 0:
        return 0.0
    mu = [math.cos(math.pi * k / m) for k in range(m + 1)]
    v = [phi(x) for x in mu]
    vand = math.prod((v[k] - v[i])**2 for i in range(m + 1)
                     for k in range(i + 1, m + 1))
    endpoint = vand / (4 * m ** (m + 1))
    degree = 1 if j in (0, m) else 2
    return endpoint * degree ** (m + 1) * 2.0 ** (2 * (d - m))


def observed(m, j, phi):
    n = m + 1
    degree = 1 if j in (0, m) else 2
    eig = [math.cos(math.pi * k / m) for k in range(n)]
    amplitude = [math.sqrt(degree) * math.cos(math.pi * k * j / m)
                 / math.sqrt(2 * m if k in (0, m) else m)
                 for k in range(n)]
    matrix = [[phi(eig[k]) ** t * amplitude[k] for k in range(n)]
              for t in range(n)]
    return det(matrix) ** 2


def main():
    checks = 0
    for phi, max_m in ((lambda x: x, 9),
                       (lambda x: 2.0 * x + 1.0, 8),
                       (lambda x: math.exp(0.8 * x), 6)):
        for m in range(1, max_m + 1):
            for j in range(m + 1):
                want = predicted(m, j, phi)
                got = observed(m, j, phi)
                # Conditioned by the expected value: the small determinants
                # are the reason for restricting to small graphs here.
                if want == 0:
                    assert got < 1e-20, (m, j, got)
                else:
                    assert abs(got / want - 1.0) < 1e-5, (m, j, got, want)
                checks += 1
    for m in range(1, 50):
        for j in range(m + 1):
            d = math.gcd(j, m)
            if m // d % 2:
                ratio = (1 if j in (0, m) else 2) ** (m + 1) * 2 ** (2 * (d - m))
                assert ratio <= 1
                if m >= 4 and j not in (0, m):
                    assert ratio < 1
            checks += 1
    print('PASS: %d determinant, rank-parity, and optimal-placement checks' % checks)


if __name__ == '__main__':
    main()
