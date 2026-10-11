#!/usr/bin/env python3
from fractions import Fraction

checks = 0
for n in range(3, 201):
    m = n - 1
    M = n ** (2 * n)

    # Compare squared distances without floating point:
    # D_k^2 = (k*M/m - n^(2k+2))^2 * m / (k*(m-k)).
    dist2 = {}
    for k in range(1, m):
        slack = Fraction(k * M, m) - n ** (2 * (k + 1))
        assert slack > 0
        d2 = slack * slack * Fraction(m, k * (m - k))
        dist2[k] = d2
        checks += 1

    assert all(dist2[k] > dist2[1] for k in range(2, m))

    closed2 = Fraction(
        (n ** (2 * n) - (n - 1) * n ** 4) ** 2,
        (n - 1) * (n - 2),
    )
    assert dist2[1] == closed2

    # Original-coordinate center lies in both affine hyperplanes.
    p0 = -n ** (2 * n - 1)
    pi = Fraction(n ** (2 * n - 1), n - 1)
    assert p0 + (n - 1) * pi == 0
    assert sum(pi - p0 for _ in range(n - 1)) == M

print(f"VERIFY_OK rooted-star-poset-associahedron n=3..200 cardinality_checks={checks}")
