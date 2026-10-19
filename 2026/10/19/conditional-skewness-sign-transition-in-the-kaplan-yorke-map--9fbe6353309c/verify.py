"""Exact rational consistency check for the Kaplan–Yorke cubic moment law.

The infinite-parameter theorem is proved analytically in RESULT.md. This program
checks Fourier recurrences only at the signed rational sample parameters below.
"""
from fractions import Fraction as Q


def add(*polys):
    out = {}
    for poly in polys:
        for k, v in poly.items():
            out[k] = out.get(k, Q(0)) + v
    return {k: v for k, v in out.items() if v}


def scale(poly, factor):
    return {k: v * factor for k, v in poly.items() if v * factor}


def transfer(poly):
    return {k // 2: v for k, v in poly.items() if k % 2 == 0 and v}


def cosine_times(poly):
    out = {}
    for k, v in poly.items():
        if k == 0:
            out[1] = out.get(1, Q(0)) + v
        else:
            for n in (k - 1, k + 1):
                out[n] = out.get(n, Q(0)) + v / 2
    return {k: v for k, v in out.items() if v}


def verify(alpha):
    c = {1: Q(1)}
    c2 = {0: Q(1, 2), 2: Q(1, 2)}
    c3 = {1: Q(3, 4), 3: Q(1, 4)}
    m1 = c
    assert m1 == add(c, scale(transfer(m1), alpha))
    v = {0: alpha**2 / (2 * (1 - alpha**2)), 1: alpha**2 / 2}
    m2 = add(c2, v)
    assert m2 == add(c2, scale(transfer(m2), alpha**2))
    g = add(c3, scale(cosine_times(v), Q(3)))
    assert g.get(0, Q(0)) == g.get(2, Q(0)) == Q(3) * alpha**2 / 4
    m3 = add(g, {
        0: alpha**3 * g.get(0, Q(0)) / (1 - alpha**3),
        1: alpha**3 * g.get(2, Q(0)),
    })
    assert m3 == add(g, scale(transfer(m3), alpha**3))
    centered = add(m3, scale(cosine_times(m2), Q(-3)), scale(c3, Q(2)))
    expected = add({0: Q(3) * alpha**5 / (4 * (1 - alpha**3))},
                   {1: Q(3) * alpha**5 / 4})
    assert centered == expected
    assert m2[0] == 1 / (2 * (1 - alpha**2))
    assert m3.get(0, Q(0)) == Q(3) * alpha**2 / (4 * (1 - alpha**3))
    if alpha < 0:
        at_zero = sum(expected.values(), Q(0))
        at_half = expected.get(0, Q(0)) - expected.get(1, Q(0))
        assert at_zero < 0 < at_half
    if alpha > 0:
        assert expected[0] - expected[1] > 0


if __name__ == '__main__':
    for alpha in (Q(0), Q(1, 5), Q(-1, 5), Q(3, 5),
                  Q(-3, 5), Q(9, 10), Q(-9, 10)):
        verify(alpha)
    print('VERIFY_OK')
