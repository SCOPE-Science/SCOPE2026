"""Exact rational checks for covariance and contact identities of convex free joins.

The checks use cubes as factors (whose John contact normals are ±coordinate
vectors). They are finite algebraic tests, not substitutes for the proof.
"""
from itertools import product
from sympy import Matrix, Rational, zeros, eye


def verify(dimensions):
    k = len(dimensions)
    n = sum(dimensions) + k - 1
    N = n + 1
    alpha = [m + 1 for m in dimensions]
    t = Matrix([Rational(a, N) for a in alpha])
    D = Matrix.diag(*t)
    C = (D - t * t.T) / n
    q = [Rational(m * (m + 1), n * N) for m in dimensions]
    assert C * Matrix([1] * k) == zeros(k, 1)
    assert C * D.inv() * C == C / n
    assert all(q[i] + C[i, i] == t[i]**2 for i in range(k))

    # Work in ambient sum-zero coordinates: covariance Q is singular in
    # the extrinsic barycentric direction but positive on its intrinsic space.
    off = sum(dimensions)
    Q = zeros(off + k)
    r = 0
    for m, qi in zip(dimensions, q):
        for h in range(m):
            Q[r + h, r + h] = qi
        r += m
    for i in range(k):
        for j in range(k):
            Q[off + i, off + j] = C[i, j]

    first = zeros(off + k, 1)
    second = zeros(off + k)
    r = 0
    for i, m in enumerate(dimensions):
        for h in range(m):
            for sign in (-1, 1):
                v = zeros(off + k, 1)
                v[r + h] = sign
                v[off + i] = -1
                # Each coordinate ±contact of a cube has John weight 1/2.
                weight = t[i]**2 / (2 * q[i])
                assert (v.T * Q * v)[0] == t[i]**2
                ellipsoid_contact = Q * v / t[i]
                first += weight * ellipsoid_contact
                second += weight * ellipsoid_contact * ellipsoid_contact.T
        r += m
    assert first == zeros(off + k, 1)
    assert second == Q
    assert all(t[i] > C[i, i] / t[i] for i in range(k))
    return True


def main():
    cases = 0
    for k in (2, 3, 4, 5):
        for ds in product((1, 2, 3), repeat=k):
            verify(ds)
            cases += 1
    print(f"PASS: {cases} exact rational covariance, feasibility-margin and John-contact certificates")


if __name__ == '__main__':
    main()
