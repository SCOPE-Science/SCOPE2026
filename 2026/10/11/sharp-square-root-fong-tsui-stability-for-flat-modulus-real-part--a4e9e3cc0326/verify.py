#!/usr/bin/env python3
"""Finite sanity checks for a sharp operator modulus inequality.

These computations are not a proof of the infinite-dimensional theorem.
No third-party packages required.
"""
from math import sqrt


def two_by_two_defect(a, r, b, s):
    # A=diag(a,0), B=[[r,b],[b,s]]; use exact 2x2 positive square-root identity.
    m11 = a * a + r * r + b * b
    m22 = b * b + s * s
    m12_re = b * (r + s)
    m12_im = a * b
    det = m11 * m22 - m12_re**2 - m12_im**2
    assert det >= -1e-9
    root_det = sqrt(max(det, 0.0))
    denom = sqrt(m11 + m22 + 2 * root_det)
    assert denom > 0
    z11 = (m11 + root_det) / denom - a
    z22 = (m22 + root_det) / denom
    z12sq = (m12_re * m12_re + m12_im * m12_im) / (denom * denom)
    top_eig = (z11 + z22 + sqrt((z11 - z22) ** 2 + 4 * z12sq)) / 2
    eps = max(0.0, top_eig)
    rad = sqrt((r - s) ** 2 + 4 * b * b)
    normB = max(abs((r + s + rad) / 2), abs((r + s - rad) / 2))
    return eps, normB


def main():
    for a, eps, b in [(3.0, 2.0, 4.0), (5.0, 8.0, 12.0), (1.0, 0.0, 0.0)]:
        assert abs((a + eps) ** 2 - a * a - b * b) < 1e-12
        assert abs(b * b - eps * (2 * a + eps)) < 1e-12
    # Cases include genuine noncommutation since b != 0 and a>0.
    choices = (-0.75, -0.25, 0.0, 0.25, 0.75)
    n = 0
    for a in (1.0, 2.0, 3.0):
        for r in choices:
            for s in choices:
                for b in choices:
                    eps, normB = two_by_two_defect(a, r, b, s)
                    assert normB**2 <= eps * (2 * a + eps) + 1e-9, (a, r, b, s, eps, normB)
                    n += 1
    assert n == 375
    print('FLAT_MODULUS_FONG_TSUI_TWO_BY_TWO_AND_EQUALITY_OK: 375 matrix cases, 3 exact witnesses')


if __name__ == '__main__':
    main()
