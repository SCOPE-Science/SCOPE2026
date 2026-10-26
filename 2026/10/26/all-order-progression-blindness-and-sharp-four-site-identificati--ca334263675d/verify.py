"""Exact arithmetic checks for progression correlations of paperfolding words.

No external modules are needed.  The cylinder algorithm computes every fixed
finite correlation as a polynomial in fold-direction signs.  See RESULT.md
for the proof that its finite dyadic partition is exhaustive.
"""
from fractions import Fraction
from itertools import combinations


def cylinder_polynomial(offsets):
    offsets = tuple(sorted(offsets))
    assert offsets and len(set(offsets)) == len(offsets)
    span = offsets[-1] - offsets[0]
    K = max(3, span.bit_length() + 2)
    mod = 1 << K
    num = {}
    for r in range(mod):
        # At most one observation lies in the unresolved high-valuation class.
        # Its conditional mean is zero, independently of every fold sign.
        if any((r + d) % (mod // 2) == 0 for d in offsets):
            continue
        monomial = 0
        sign = 1
        for d in offsets:
            z = (r + d) % mod
            val = (z & -z).bit_length() - 1
            assert val <= K - 2
            monomial ^= 1 << val  # epsilon_val squared is 1
            if ((z >> val) % 4) == 3:
                sign = -sign
        num[monomial] = num.get(monomial, 0) + sign
    return {key: Fraction(value, mod) for key, value in num.items() if value}


def predicted(m, h):
    if m % 2 or h % 2:
        return {}
    a = (h & -h).bit_length() - 1
    out = Fraction(1) - Fraction(2, 1 << a) + Fraction((-1) ** (m // 2), 1 << a)
    return {} if out == 0 else {0: out}


def fold_sign(n, eps):
    assert n >= 1
    b = (n & -n).bit_length() - 1
    u = n >> b
    return eps[b] * (1 if u % 4 == 1 else -1)


def direct_mean(offsets, eps, N):
    v = 0
    for n in range(1, N + 1):
        product = 1
        for d in offsets:
            product *= fold_sign(n + d, eps)
        v += product
    return Fraction(v, N)


def main():
    ap = 0
    for m in range(1, 15):
        for h in range(1, 33):
            got = cylinder_polynomial(tuple(j * h for j in range(m)))
            expect = predicted(m, h)
            assert got == expect, (m, h, got, expect)
            ap += 1

    short = 0
    for diameter in range(3, 8):
        for a, b in combinations(range(1, diameter), 2):
            got = cylinder_polynomial((0, a, b, diameter))
            assert not any(mask for mask in got), (a, b, diameter, got)
            short += 1
    assert short == 35

    witness = cylinder_polynomial((0, 1, 2, 8))
    assert witness == {3: Fraction(1, 8)}, witness

    for k in range(1, 8):
        off = (0, 1 << k, 2 << k, 8 << k)
        got = cylinder_polynomial(off)
        expect = {0: 1 - Fraction(3, 1 << k), 3 << k: Fraction(1, 1 << (k + 3))}
        expect = {mask: value for mask, value in expect.items() if value}
        assert got == expect, (k, got, expect)

    # Independent contiguous prefix computation with different fold instructions.
    N = 1 << 16
    patterns = [
        [1] * 24,
        [1 if k != 2 else -1 for k in range(24)],
        [1 if k % 2 == 0 else -1 for k in range(24)],
    ]
    sample = ((2, 1), (2, 2), (4, 2), (6, 4), (8, 6), (7, 11))
    for eps in patterns:
        for m, h in sample:
            estimate = direct_mean(tuple(j * h for j in range(m)), eps, N)
            target = predicted(m, h).get(0, Fraction(0))
            assert abs(estimate - target) < Fraction(1, 1000), (m, h, estimate, target)
        for off in ((0, 1, 2, 8), (0, 2, 4, 16), (0, 4, 8, 32)):
            k = (off[1]).bit_length() - 1
            target = (Fraction(eps[0] * eps[1], 8) if k == 0 else
                      1 - Fraction(3, 1 << k) + Fraction(eps[k] * eps[k + 1], 1 << (k + 3)))
            estimate = direct_mean(off, eps, N)
            assert abs(estimate - target) < Fraction(1, 1000), (off, estimate, target)
    print('VERIFY_OK:', ap, 'exact symbolic progression identities;', short,
          'short-diameter four-point shapes;',
          'first distinguishing witness and 7 scaled witnesses;',
          '27 independently averaged dyadic-prefix comparisons')


if __name__ == '__main__':
    main()
