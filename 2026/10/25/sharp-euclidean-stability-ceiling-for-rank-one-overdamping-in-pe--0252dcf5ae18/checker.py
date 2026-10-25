"""Exact-rational spot checks for a linear implicit-stage perturbation theorem.
Run: python3 checker.py. No third-party packages required.
Finite checks corroborate, but cannot replace, the proof for all dimensions.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt


def matrix(*rows):
    return tuple(tuple(F(x) for x in row) for row in rows)


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(row_a, row_b))
                 for row_a, row_b in zip(a, b))


def scale(a, s):
    return tuple(tuple(F(s) * x for x in row) for row in a)


def mult(a, b):
    bt = tuple(zip(*b))
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) for col in bt)
                 for row in a)


def tr(a):
    return tuple(zip(*a))


def inv(a):
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    assert det
    return matrix((a[1][1] / det, -a[0][1] / det),
                  (-a[1][0] / det, a[0][0] / det))


def sub(a, b):
    return add(a, scale(b, -1))


def psd(a):
    return a[0][0] >= 0 and a[1][1] >= 0 and \
        a[0][0] * a[1][1] >= a[0][1] * a[1][0]


I = matrix((1, 0), (0, 1))


def test_case(a, v, h):
    vv = mult(matrix((v[0],), (v[1],)), matrix((v[0], v[1])))
    b = add(a, vv)
    c = add(I, scale(b, h / 2))
    t = sub(I, scale(mult(a, inv(c)), h))
    k = scale(add(mult(a, vv), mult(vv, a)), F(1, 2))
    direct = sub(I, mult(tr(t), t))
    claim = scale(add(scale(a, 2), scale(k, h)), h)
    assert mult(mult(c, direct), c) == claim
    ainv = inv(a)
    weighted = sub(ainv, mult(mult(tr(t), ainv), t))
    weighted_claim = scale(add(scale(I, 2), scale(vv, h)), h)
    assert mult(mult(c, weighted), c) == weighted_claim
    assert psd(weighted_claim)
    assert psd(direct) == psd(claim)
    av = mult(a, matrix((v[0],), (v[1],)))
    vcol = matrix((v[0], v[1]))
    scalar = mult(vcol, matrix((v[0],), (v[1],)))[0][0]
    alpha = mult(vcol, av)[0][0]
    beta = mult(mult(vcol, ainv), matrix((v[0],), (v[1],)))[0][0]
    delta = sqrt(float(alpha * beta)) - float(scalar)
    if delta > 1e-10 and abs(float(h)*delta-4.0) > 1e-8:
        assert psd(claim) == (float(h)*delta < 4.0)
    elif delta < 1e-10:
        assert psd(claim)


def witness():
    a = matrix((1, 0), (0, 4))
    v = (F(1), F(1))
    b = add(a, matrix((1, 1), (1, 1)))
    for h, want_x, want_y in [
        (F(8), (F(7), F(-13, 2)), (F(-1), F(19, 2))),
        (F(16), (F(13), F(-25, 2)), (F(-3), F(39, 2)))]:
        c = add(I, scale(b, h / 2))
        w = matrix((1,), (F(-1, 2),))
        x = mult(c, w)
        y = sub(x, scale(mult(a, w), h))
        assert (x[0][0], x[1][0]) == want_x
        assert (y[0][0], y[1][0]) == want_y
        diff = sum(z*z for z in want_y) - sum(z*z for z in want_x)
        assert diff == (F(0) if h == 8 else F(64))
        test_case(a, v, h)
    assert F(1557, 1301) > 1


def main():
    count = 0
    for a1, a2, cross, p, q, h in product(
            [1, 2, 3, 5], [1, 2, 4, 7], [F(0), F(1, 2)],
            [-2, -1, 0, 1, 2], [-2, 0, 1], [F(1, 2), F(2), F(8), F(16)]):
        if p == q == 0 or F(a1*a2) <= cross*cross:
            continue
        a = matrix((a1, cross), (cross, a2))
        test_case(a, (F(p), F(q)), h)
        count += 1
    witness()
    print('PASS: {} exact-rational matrix configurations and both sharp witnesses'.format(count))


if __name__ == '__main__':
    main()
