"""Standalone finite checks for the retraction census of a star two-step Lie algebra.

Only prime fields and the displayed small parameters are tested; the proof
for arbitrary finite fields and all dimensions is mathematical, not exhaustive.
"""
from fractions import Fraction
from itertools import product


def gaussian(n, r, q):
    f = Fraction(1)
    for j in range(r):
        f *= Fraction(q ** (n - j) - 1, q ** (r - j) - 1)
    return int(f)


def mul(A, B, q):
    return [[sum(a * b for a, b in zip(row, col)) % q
             for col in zip(*B)] for row in A]


def rank(A, q):
    a = [row[:] for row in A]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    piv = 0
    for c in range(cols):
        ix = next((i for i in range(piv, rows) if a[i][c] % q), None)
        if ix is None:
            continue
        a[piv], a[ix] = a[ix], a[piv]
        inv = pow(a[piv][c], -1, q)
        a[piv] = [(v * inv) % q for v in a[piv]]
        for i in range(rows):
            if i != piv:
                k = a[i][c]
                a[i] = [(x - k * y) % q for x, y in zip(a[i], a[piv])]
        piv += 1
        if piv == rows:
            break
    return piv


def bracket(x, y, m, q):
    """Star bracket in V(c,u_1,...,u_m) + Z(z_1,...,z_m)."""
    return [0] * (m + 1) + [((x[0] * y[i+1] - y[0] * x[i+1]) % q)
                             for i in range(m)]


def image_key(F, m, q):
    """Canonical span by closure under linear combinations (small cases only)."""
    cols = [tuple(row[j] for row in F) for j in range(2*m+1)]
    span = {(0,) * (2*m+1)}
    for v in cols:
        span = {tuple((x[i]+a*v[i]) % q for i in range(2*m+1))
                for x in span for a in range(q)}
    return tuple(sorted(span))


def check(q, m, enumerate_f=False, check_images=False):
    n = m+1
    map_count = {}
    A_count = {}
    distinct = {}
    for digits in product(range(q), repeat=n*n):
        A = [list(digits[i*n:(i+1)*n]) for i in range(n)]
        if mul(A, A, q) != A:
            continue
        a = A[0][0]
        ell = A[0][1:]
        w = [A[i+1][0] for i in range(m)]
        M = [row[1:] for row in A[1:]]
        if any((ell[i]*M[k][j] - ell[j]*M[k][i]) % q
               for i in range(m) for j in range(m) for k in range(m)):
            continue
        P = [[(a*M[i][j] - w[i]*ell[j]) % q for j in range(m)]
             for i in range(m)]
        assert mul(P, P, q) == P
        ra, rp = rank(A, q), rank(P, q)
        category = (ra, rp)
        A_count[category] = A_count.get(category, 0)+1
        predicted_lifts = q ** (ra*(m-rp) + (n-ra)*rp)
        map_count[category] = map_count.get(category, 0)+predicted_lifts
        if enumerate_f:
            actual_lifts = 0
            for fdigits in product(range(q), repeat=m*n):
                B = [list(fdigits[i*n:(i+1)*n]) for i in range(m)]
                BA, PB = mul(B, A, q), mul(P, B, q)
                if any((BA[i][j]+PB[i][j]-B[i][j]) % q
                       for i in range(m) for j in range(n)):
                    continue
                actual_lifts += 1
                F = [row + [0]*m for row in A]
                F.extend(B[i]+P[i] for i in range(m))
                # Directly check every defining basis bracket.
                basis = [[int(i == j) for i in range(2*m+1)]
                         for j in range(2*m+1)]
                columns = [[F[i][j] for i in range(2*m+1)]
                           for j in range(2*m+1)]
                for i in range(2*m+1):
                    for j in range(2*m+1):
                        lhs = [sum(F[k][h]*bracket(basis[i], basis[j], m, q)[h]
                                   for h in range(2*m+1)) % q
                               for k in range(2*m+1)]
                        assert lhs == bracket(columns[i], columns[j], m, q)
                if check_images:
                    key = image_key(F, m, q)
                    distinct.setdefault(category, {})[key] = (
                        distinct.setdefault(category, {}).get(key, 0)+1)
            assert predicted_lifts == actual_lifts
    expected = {(0, 0): 1, (1, 0): gaussian(m+1, 1, q)*q**(2*m)}
    for r in range(2, m+1):
        expected[(r, 0)] = gaussian(m, r, q)*q**(r*(2*m-r+1))
    for s in range(1, m+1):
        expected[(s+1, s)] = gaussian(m, s, q)*q**((3*s+2)*(m-s))
    assert map_count == expected, (q, m, map_count, expected)
    if check_images:
        expected_images = {(0, 0): (1, 1),
                           (1, 0): (gaussian(m+1, 1, q)*q**m, q**m)}
        for r in range(2, m+1):
            expected_images[(r, 0)] = (gaussian(m, r, q)*q**(m*r),
                                       q**(r*(m-r+1)))
        for s in range(1, m+1):
            expected_images[(s+1, s)] = (
                gaussian(m, s, q)*q**((s+2)*(m-s)),
                q**(2*s*(m-s)))
        assert {key: (len(fibers), next(iter(fibers.values())))
                for key, fibers in distinct.items()} == expected_images
        for fibers in distinct.values():
            assert len(set(fibers.values())) == 1
        print('IMAGE_VERIFY_OK', q, m, 'distinct', sum(map(len, distinct.values())))
    print('VERIFY_OK', q, m, 'total', sum(map_count.values()), 'strata', sorted(map_count.items()))


if __name__ == '__main__':
    check(2, 2, enumerate_f=True, check_images=True)
    check(3, 2, enumerate_f=True)
    check(2, 3)
