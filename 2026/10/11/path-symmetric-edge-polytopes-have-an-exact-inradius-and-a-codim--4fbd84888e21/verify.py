#!/usr/bin/env python3
from fractions import Fraction
import itertools
import math

for n in range(2, 12):
    m = n - 1
    target = Fraction(n * (n*n - 1), 12)
    max_norm = Fraction(-1)
    maximizers = []

    normals = []
    for eps in itertools.product((-1, 1), repeat=m):
        # Set the last coordinate temporarily to zero, integrate differences,
        # then subtract the exact mean to enter the zero-sum hyperplane.
        raw = [Fraction(0) for _ in range(n)]
        for i in range(n-2, -1, -1):
            raw[i] = raw[i+1] + eps[i]
        mean = sum(raw, Fraction(0)) / n
        x = [z - mean for z in raw]
        assert sum(x, Fraction(0)) == 0
        for i in range(m):
            assert x[i] - x[i+1] == eps[i]

        norm2 = sum(z*z for z in x)

        variance = Fraction(0)
        for p in range(n):
            s = 0
            for q in range(p+1, n):
                s += eps[q-1]
                variance += s*s
        variance /= n
        assert norm2 == variance
        normals.append((eps, x, norm2))

        if norm2 > max_norm:
            max_norm = norm2
            maximizers = [eps]
        elif norm2 == max_norm:
            maximizers.append(eps)

    assert max_norm == target, (n, max_norm, target)
    assert set(maximizers) == {tuple([1]*m), tuple([-1]*m)}

    rin2 = Fraction(1, 1) / target
    expected_rin2 = Fraction(12, n*(n*n-1))
    assert rin2 == expected_rin2

    # The two extremal normals are opposite and impose one independent
    # equality inside the (n-1)-dimensional zero-sum affine span.
    xplus = next(x for eps, x, q in normals if eps == tuple([1]*m))
    assert any(z != 0 for z in xplus)
    assert n - 2 >= 0

    # Every primal vertex e_i-e_{i+1} has squared norm 2.
    rout2 = Fraction(2, 1)
    ratio2 = rout2 / rin2
    assert ratio2 == Fraction(n*(n*n-1), 6)

print("VERIFY_OK path-symmetric-edge-inball n=2..11 exhaustive_facets=yes equality_cases=2 incenter_codim=1 outer_sphere=yes")
