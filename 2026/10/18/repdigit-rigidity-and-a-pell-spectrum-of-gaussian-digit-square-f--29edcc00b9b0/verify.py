#!/usr/bin/env python3
"""Exact signed-digit Gaussian fixed-point checks; standard Python only."""

def gaussian_s(B, a, b):
    assert B >= 2
    aa, bb = abs(a), abs(b)
    sa = -1 if a < 0 else 1
    sb = -1 if b < 0 else 1
    out_a = out_b = 0
    while aa != 0 or bb != 0:
        da = (aa % B) * sa
        db = (bb % B) * sb
        aa //= B
        bb //= B
        out_a += da * da - db * db
        out_b += 2 * da * db
    return out_a, out_b


def pell_pairs(count):
    B, t = 1, 0
    for _ in range(count):
        B, t = 3 * B + 8 * t, B + 3 * t
        assert B * B - 8 * t * t == 1
        yield B, t


def test():
    cases = list(pell_pairs(12))
    assert cases[:4] == [(3, 1), (17, 6), (99, 35), (577, 204)]
    for B, t in cases:
        a = (B + 1) // 2
        assert 0 < a < B and 0 < t < B
        for sign in (1, -1):
            imag = sign * t * (B + 1)
            assert gaussian_s(B, a, imag) == (a, imag)
    expected = set()
    for B, t in cases:
        if B > 120:
            continue
        for sign in (1, -1):
            expected.add((B, (B + 1) // 2, sign * t, 2))
    observed = set()
    scanned = 0
    for B in range(2, 121):
        for m in range(1, 5):
            rep = sum(B ** j for j in range(m))
            for a in range(-B + 1, B):
                for t in range(-B + 1, B):
                    if t == 0:
                        continue
                    scanned += 1
                    imag = t * rep
                    if gaussian_s(B, a, imag) == (a, imag):
                        observed.add((B, a, t, m))
    assert observed == expected, (sorted(observed - expected), sorted(expected - observed))
    print('Cases scanned:', scanned)
    print('All signed repdigit fixed points for bases <=120 and lengths <=4:', sorted(observed))
    print('Pell iterations verified:', len(cases))
    print('VERIFY_OK')


if __name__ == '__main__':
    test()
