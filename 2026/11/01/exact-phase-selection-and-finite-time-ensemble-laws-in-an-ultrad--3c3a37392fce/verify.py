"""Exact-rational finite checks for the max-plus phase-selection identities.

Usage: python verify.py
The analytical argument in RESULT.md proves the universal statements.
"""
from fractions import Fraction as Q


def f(x, I, B):
    return max(2*x, I) - max(2*x, B)


def check(I, B=Q(1)):
    L, H, q = max(Q(0), 2*B-I), I-B, I/Q(3)
    M = min(I/Q(2), H)
    a = (B/Q(2)-L)/(H-L)
    b = (H-M)/(H-L)
    w = Q(1, 3) + Q(2, 3)*b
    assert B > 0 and I > Q(3,2)*B
    assert L < q < H
    assert f(L, I, B) == H and f(H, I, B) == L
    assert f(q, I, B) == q
    assert a + b == Q(1,2) and a >= 0 and b >= 0
    assert M-B/Q(2) == (H-L)/2
    want = (Q(1,3) if I <= 2*B else (2*I-3*B)/(3*(I-B)))
    assert w == want
    cont, high, low = Q(1), Q(0), Q(0)
    for n in range(21):
        assert cont == Q(1,2)**n
        assert high + low + cont == 1
        if n % 2 == 0:
            assert high == (1-cont)*w
            assert low == (1-cont)*(1-w)
        cont, high, low = cont/Q(2), a*cont+low, b*cont+high

    # Exact finite tests of the mirror pairing. Tests are only supplementary.
    delta = min(q-L, H-q)
    for k in range(1, 98):
        t = delta*Q(k, 97)
        pair = [q-t, q+t]
        bits = []
        for x in pair:
            y = x
            phase = None
            for n in range(80):
                if y == H:
                    phase = 1 if n % 2 == 0 else 0
                    break
                if y == L:
                    phase = 0 if n % 2 == 0 else 1
                    break
                y = f(y, I, B)
            assert phase is not None, (I, k, x)
            bits.append(phase)
        assert bits[0] + bits[1] == 1, (I, k, bits)


if __name__ == '__main__':
    ratios = [Q(8,5), Q(39,20), Q(2), Q(11,5), Q(3), Q(10)]
    for ratio in ratios:
        check(ratio, Q(1))
        check(5*ratio, Q(5))
    print('PASS: 12 parameter instances, 252 transfer time-step checks, 1164 mirror pair tests')
