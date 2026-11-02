#!/usr/bin/env python3
"""Standalone exact-arithmetic checks of a ternary binomial value-set theorem.

Standard-library only. Finite tests supplement, not replace, the proof.
"""
from fractions import Fraction
from math import comb


def coeffs(a):
    p = [1]
    for j in range(6):
        q = [0] * (len(p) + 1)
        for i, v in enumerate(p):
            q[i] += (a - j) * v
            q[i + 1] += 9 * v
        p = q
    return [Fraction(v, 720) for v in p]


def residue(x, modulus):
    x = Fraction(x)
    assert x.denominator % 3 != 0, (x, modulus)
    return (x.numerator * pow(x.denominator, -1, modulus)) % modulus


def check_branch_coefficients():
    for a in range(9):
        c = coeffs(a)
        assert c[0] == comb(a, 6)
        if a <= 5:
            assert residue(c[1] / 3, 3) == (1 if a <= 2 else 2)
            assert all(residue(c[j] / 3, 3) == 0 for j in range(2, 7))
        else:
            assert all(residue(c[j] / 9, 3) == (2 if j in (1, 2) else 0)
                       for j in range(1, 7))
    return 9


def critical_t(a, digits):
    c = coeffs(a)
    h = [c[j] / 9 for j in range(7)]
    t = 1
    assert residue(sum(j * h[j] * t**(j - 1) for j in range(1, 7)), 3) == 0
    for r in range(1, digits):
        modulus = 3 ** (r + 1)
        choices = []
        for d in range(3):
            candidate = t + d * (3 ** r)
            deriv = sum(j * h[j] * candidate ** (j - 1) for j in range(1, 7))
            if residue(deriv, modulus) == 0:
                choices.append(candidate)
        assert len(choices) == 1, (a, r, choices)
        t = choices[0]
    return t


def direct_images(k):
    modulus = 3 ** k
    period = 3 ** (k + 2)  # v_3(6!) = 2
    return {comb(n, 6) % modulus for n in range(period)}


def predicted_images(k):
    modulus = 3 ** k
    if k == 1:
        return {0, 1}
    baseline = set(range(0, modulus, 3))
    sq_mod = 3 ** (k - 2)
    sq = {i * i % sq_mod for i in range(sq_mod)}
    c6 = comb(6 + 9 * critical_t(6, k), 6) % modulus
    c7 = residue(Fraction(-5, 1024), modulus)
    return baseline | {(c6 + 18 * y) % modulus for y in sq} | \
           {(c7 + 18 * y) % modulus for y in sq}


def predicted_count(k):
    if k == 1:
        return 2
    correction = 5 if k % 2 == 0 else 7
    return (5 * 3 ** (k - 1) + correction) // 4


def main():
    checked = check_branch_coefficients()
    lengths = []
    for k in range(1, 10):
        direct = direct_images(k)
        predicted = predicted_images(k)
        target = predicted_count(k)
        assert direct == predicted, (k, len(direct), len(predicted), sorted(direct ^ predicted)[:15])
        assert len(direct) == target, (k, len(direct), target)
        lengths.append(len(direct))
        print(f'LEVEL_OK k={k} values={len(direct)} period={3**(k+2)}')
    print('VERIFY_OK coeff_branches=', checked, 'levels=1..9',
          'image_counts=', lengths, 'asymptotic_density=5/12')


if __name__ == '__main__':
    main()
