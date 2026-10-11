#!/usr/bin/env python3
"""Exact small-alphabet autocorrelation checks for triangular quadratic Fourier support.

Only Python 3 standard library is required. The analytic bounds and continuous
phase classification are proved in RESULT.md, not inferred from this enumeration.
"""
from itertools import product
from collections import defaultdict
from math import cos, pi, sin

S = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]
# Write a+b*omega as (a,b), omega^2+omega+1=0.
ZERO = (0, 0)
ONE = (1, 0)
OMEGA = (0, 1)
OMEGA2 = (-1, -1)
ROOTS3 = (ONE, OMEGA, OMEGA2)
ROOTS2 = (ONE, (-1, 0))


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def mul(a, b):
    x, y = a
    z, t = b
    return x*z-y*t, x*t+y*z-y*t


def conj(a):
    return a[0]-a[1], -a[1]


def norm(a):
    x, y = a
    return x*x-x*y+y*y


def autocorrelation(coeff):
    out = defaultdict(lambda: ZERO)
    for a, va in coeff.items():
        for b, vb in coeff.items():
            d = a[0]-b[0], a[1]-b[1]
            out[d] = add(out[d], mul(va, conj(vb)))
    return dict(out)


def moment(coeff):
    return sum(norm(x) for x in autocorrelation(coeff).values())


def gauge_coeff(u, v, w):
    return dict(zip(S, (ONE, ONE, ONE, u, v, w)))


def identity_value(u, v, w):
    first = add(add(ONE, u), v)
    second = add(add(ONE, v), w)
    third = add(add(ONE, mul(u, conj(v))), mul(v, conj(w)))
    return 48 + 2*(norm(first)+norm(second)+norm(third))


def run():
    assert len(S) == 6
    diff_counts = defaultdict(int)
    for a in S:
        for b in S:
            diff_counts[(a[0]-b[0], a[1]-b[1])] += 1
    assert diff_counts[(0, 0)] == 6 and len(diff_counts) == 19
    positive = [d for d in diff_counts if d != (0, 0) and
                (d[0] > 0 or (d[0] == 0 and d[1] > 0))]
    assert len(positive) == 9
    assert sorted(diff_counts[d] for d in positive) == [1]*6 + [3]*3
    assert all((i, j) == (k, l) for m in (5, 7, 11) for n in (5, 7)
               for i, j in diff_counts for k, l in diff_counts
               if ((i-k) % m == 0 and (j-l) % n == 0))

    checks = 0
    for alphabet, expected_min, expected_count in ((ROOTS2, 54, 4), (ROOTS3, 48, 2)):
        minimizers = []
        moments = []
        for u, v, w in product(alphabet, repeat=3):
            coeff = gauge_coeff(u, v, w)
            m1 = moment(coeff)
            m2 = identity_value(u, v, w)
            assert m1 == m2
            assert 48 <= m1 <= 102
            checks += 1
            moments.append(m1)
            if m1 == expected_min:
                minimizers.append((u, v, w))
        assert min(moments) == expected_min
        assert max(moments) == 102
        assert len(minimizers) == expected_count
        if alphabet is ROOTS3:
            assert set(minimizers) == {
                (OMEGA, OMEGA2, OMEGA),
                (OMEGA2, OMEGA, OMEGA2),
            }
        else:
            assert set(minimizers) == {
                ((-1, 0), (-1, 0), ONE),
                ((-1, 0), ONE, (-1, 0)),
                (ONE, (-1, 0), (-1, 0)),
                (ONE, (-1, 0), ONE),
            }

    # Cross-check the continuous Haar identity by deterministic discrete
    # quadrature on a no-alias finite torus, not as evidence for all tori.
    u, v, w = OMEGA, OMEGA2, OMEGA
    as_complex = lambda a: complex(a[0] - .5*a[1], .5*(3**.5)*a[1])
    for m, n in ((5, 5), (5, 7), (7, 5)):
        total = 0.0
        for k in range(m):
            z = complex(cos(2*pi*k/m), sin(2*pi*k/m))
            for l in range(n):
                t = complex(cos(2*pi*l/n), sin(2*pi*l/n))
                q = sum(as_complex(a)*(z**i)*(t**j)
                        for (i, j), a in gauge_coeff(u, v, w).items())
                total += abs(q)**4
        assert abs(total/(m*n)-48) < 1e-8
        checks += m*n
    print('PASS: exact difference profile; algebraic L4 identity; full binary and ternary normalized enumerations; no-alias checks; supplementary finite Fourier grids.')
    print('Algebraic phase configurations checked:', 2**3+3**3)
    print('Supplementary grid points checked:', 5*5+5*7+7*5)
    print('Total main and grid numerical assertions:', checks)


if __name__ == '__main__':
    run()
