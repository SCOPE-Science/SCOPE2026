"""Exact-arithmetic checks of the four-point Pauli construction.

Uses only Python's standard library. The proof of the universal lower
bound is analytic and is not replaced by these finite checks.
"""
from fractions import Fraction as Q


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def conj(a):
    return (a[0], -a[1])


def auto(coeffs):
    return [tuple(sum(mul(coeffs[j + k], conj(coeffs[j]))[c]
                      for j in range(len(coeffs) - k)) for c in (0, 1))
            for k in range(len(coeffs))]


def family(s, t):
    return [(Q(1), Q(0)), (-t, s), (Q(1), -s * t), (-t, Q(0))]


checks = 0
for s in [Q(-3), Q(-1, 2), Q(1), Q(5, 3)]:
    for t in [Q(-4), Q(-2, 3), Q(2), Q(5, 2)]:
        a = family(s, t)
        b = [conj(x) for x in a]
        assert all(x != (0, 0) for x in a)
        assert [(x[0]**2 + x[1]**2) for x in a] == [
            (x[0]**2 + x[1]**2) for x in b]
        r = auto(a)
        assert r == auto(b)
        assert r == [((Q(1) + t**2) * (Q(2) + s**2), Q(0)),
                     (-t * (Q(3) + s**2), Q(0)),
                     (Q(1) + t**2, Q(0)),
                     (-t, Q(0))]
        assert a != b  # The first coefficient fixes global phase.
        assert abs(t) != Q(1)  # Reflection exchanges unequal endpoints.
        checks += 1

witness = family(Q(1), Q(2))
assert witness == [(Q(1), Q(0)), (Q(-2), Q(1)),
                   (Q(1), Q(-2)), (Q(-2), Q(0))]
assert auto(witness) == [(Q(15), Q(0)), (Q(-8), Q(0)),
                         (Q(5), Q(0)), (Q(-2), Q(0))]

# Three-point equispaced alternative is exactly conjugate reflection.
a = [(Q(1), Q(0)), (Q(2), Q(3)), (Q(-1), Q(0))]
b = [(Q(1), Q(0)), (Q(-2), Q(3)), (Q(-1), Q(0))]
assert auto(a) == auto(b)
assert b == [mul((Q(-1), Q(0)), conj(x)) for x in reversed(a)]
print('PASS:', checks, 'exact rational two-parameter instances;',
      'Gaussian-integer witness; three-point symmetry test')
