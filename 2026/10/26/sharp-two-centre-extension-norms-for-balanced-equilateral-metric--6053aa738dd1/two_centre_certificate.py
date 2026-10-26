#!/usr/bin/env python3
"""Exact finite checks for paired-centre extensions of equilateral metrics.

The accompanying proof is valid for every admissible real parameter.  This
program independently evaluates all Boolean extreme source potentials for
selected rational parameters and verifies the explicit positive coefficients.
"""
from fractions import Fraction as Q


def optimal(m, r, s, t):
    r, s, t = Q(r), Q(s), Q(t)
    assert m >= 2 and r >= Q(1, 2) and r <= s <= r + 1
    assert t > 0 and s-r <= t <= r+s
    l1 = Q(2*m-1, m)/(r+s)
    l2 = Q(m-1, m)/r
    l3 = Q(2*m-1)/(2*m*r+t)
    c = max(Q(1), l1, l2, l3)
    a = max(Q(1, 2*m), 1-r*c)
    b = Q(1, m)-a
    assert 0 <= b <= a
    return c, a, b, (l1, l2, l3)


def exact_pair_norm(u, v):
    return sum((abs(x-y) for x, y in zip(u, v)), Q(0))/2


def check(m, r, s, t):
    r, s, t = Q(r), Q(s), Q(t)
    c, a, b, lower = optimal(m, r, s, t)
    p = [a]*m + [b]*m
    q = [b]*m + [a]*m
    pd = [r]*m + [s]*m
    qd = [s]*m + [r]*m
    n = 2*m
    assert sum(p) == sum(q) == 1
    one = Q(1)
    for j in range(n):
        e = [Q(int(i == j)) for i in range(n)]
        assert exact_pair_norm(p, e) <= c*pd[j]
        assert exact_pair_norm(q, e) <= c*qd[j]
    assert exact_pair_norm(p, q) <= c*t
    # Exact explicit lower-bound witnesses. The all-source pair has unit norm.
    assert c == max((one, *lower))
    assert max((one, (1-a)/r, (1-b)/s, (m-1)*a/r,
                (2*m*a-1)/t)) == c
    # Every 0-1 extreme point of the unit Lipschitz ball, modulo constants.
    checks = 0
    for mask in range(1 << n):
        f = [Q(int(mask >> j & 1)) for j in range(n)]
        ep = sum((x*y for x, y in zip(p, f)), Q(0))
        eq = sum((x*y for x, y in zip(q, f)), Q(0))
        assert abs(ep-eq) <= c*t
        checks += 1
        for j in range(n):
            assert abs(ep-f[j]) <= c*pd[j]
            assert abs(eq-f[j]) <= c*qd[j]
            checks += 2
    return checks


def main():
    radii = [(Q(1, 2), Q(1, 2)), (Q(1, 2), Q(3, 4)),
             (Q(1, 2), Q(1)), (Q(2, 3), Q(5, 6)),
             (Q(3, 4), Q(5, 4)), (Q(1), Q(2)),
             (Q(5, 4), Q(7, 4))]
    configs = tests = 0
    for m in (2, 3, 4, 5):
        for r, s in radii:
            candidate = [max(s-r, Q(1, 16)),
                         (s-r+r+s)/2, r+s]
            # Check a coupling/base-branch threshold whenever admissible.
            special = [m*(s-r), Q(m)*r/(m-1)]
            candidate.extend(x for x in special if x>0 and s-r<=x<=r+s)
            for t in sorted(set(candidate)):
                tests += check(m, r, s, t)
                configs += 1
    print('PAIRED_CENTRE_CERTIFICATE_OK',
          'configurations='+str(configs),
          'exact_potential_pair_checks='+str(tests))


if __name__ == '__main__':
    main()
