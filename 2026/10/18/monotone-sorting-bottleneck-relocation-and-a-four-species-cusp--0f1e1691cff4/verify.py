"""Exact rational enclosure of the four-species bottleneck crossing.

Run: python3 verify.py
Uses only the Python standard library. Finite checks support the analytic theorem.
"""
from fractions import Fraction as Q

SPEED_COUNT = 4


def phi(a, m, z):
    v = [-a, Q(0), Q(1), Q(2)]
    assert 1 <= m <= 3 and v[m - 1] < z < v[m]
    return sum(1 / (z - x) for x in v[:m]) + sum(1 / (x - z) for x in v[m:])


def phi_prime(a, m, z):
    v = [-a, Q(0), Q(1), Q(2)]
    assert 1 <= m <= 3 and v[m - 1] < z < v[m]
    return (-sum(1 / (z - x) ** 2 for x in v[:m])
            + sum(1 / (x - z) ** 2 for x in v[m:]))


def enclosure(a, m, iterations=22):
    """Certified [lower, upper] for C_m, from exact strong convexity.

    Uses phi'' >= 32/(v_m-v_{m-1})**3 at every interior z.
    The lower bound is phi(z) - phi'(z)**2/(2*mu).
    """
    assert a > 0
    v = [-a, Q(0), Q(1), Q(2)]
    left, right = v[m - 1], v[m]
    lo, hi = left, right
    for _ in range(iterations):
        z = (lo + hi) / 2
        if phi_prime(a, m, z) < 0:
            lo = z
        else:
            hi = z
    z = (lo + hi) / 2
    mu = Q(32) / (right - left) ** 3
    upper = phi(a, m, z) / SPEED_COUNT
    lower = (phi(a, m, z) - phi_prime(a, m, z) ** 2 / (2 * mu)) / SPEED_COUNT
    assert lower <= upper
    return lower, upper


def check():
    assert phi(Q(1), 2, Q(1, 2)) == Q(16, 3)
    assert phi(Q(1), 1, -Q(1, 2)) == Q(76, 15)
    assert phi(Q(1), 3, Q(3, 2)) == Q(76, 15)
    assert phi_prime(Q(1), 2, Q(1, 2)) == 0
    assert enclosure(Q(1), 2)[0] <= Q(4, 3) <= enclosure(Q(1), 2)[1]

    a_lo = Q(467, 500)
    a_hi = Q(187, 200)
    c1_lo = enclosure(a_lo, 1)
    c2_lo = enclosure(a_lo, 2)
    c1_hi = enclosure(a_hi, 1)
    c2_hi = enclosure(a_hi, 2)
    assert c1_lo[0] > c2_lo[1], 'C1 must exceed C2 at a=467/500'
    assert c1_hi[1] < c2_hi[0], 'C1 must be below C2 at a=187/200'
    print('EXACT RATIONAL ENCLOSURES')
    for a, c1, c2 in ((a_lo, c1_lo, c2_lo), (a_hi, c1_hi, c2_hi)):
        print('a:', a, 'C1:', tuple(map(float, c1)), 'C2:', tuple(map(float, c2)))
    print('PASS: exact rational endpoint inequalities and identities')


if __name__ == '__main__':
    check()
