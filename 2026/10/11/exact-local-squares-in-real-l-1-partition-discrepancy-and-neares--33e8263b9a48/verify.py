"""Exact rational finite-dimensional checks for the local-square partition identity.

The theorem for arbitrary measures is proved analytically, not by this test.
Run with: python3 verify.py
"""
from fractions import Fraction
from itertools import product
from math import prod


def discrepancy(a):
    total = sum(a)
    return Fraction(min((abs(sum(sign * ai for sign, ai in zip(s, a))) for s in product((-1, 1), repeat=len(a))), default=0), total)


def norm_pair(a, b):
    sa, sb = sum(a), sum(map(abs, b))
    upper = sum(abs(x * sb + y * sa) for x, y in zip(a, b))
    lower = sum(abs(x * sb - y * sa) for x, y in zip(a, b))
    return Fraction(max(upper, lower), sa * sb)


def proximity(a, b):
    sa, sb = sum(a), sum(map(abs, b))
    return Fraction(sum(abs(abs(y) * sa - x * sb) for x, y in zip(a, b)), sa * sb)


def check_nearest(a, delta):
    n, total = len(a), sum(a)
    signs = list(product((-1, 1), repeat=n))
    sign = min(signs, key=lambda s: abs(sum(x * t for x, t in zip(a, s))))
    ap = sum(x for x, t in zip(a, sign) if t == 1)
    am = total - ap
    if ap and am:
        h = [Fraction(x, 2 * (ap if t == 1 else am)) for x, t in zip(a, sign)]
    else:
        j = next(i for i, x in enumerate(a) if x)
        k = next(i for i, x in enumerate(a) if not x)
        h = [Fraction(0) for _ in a]
        h[j] = Fraction(1, 2)
        h[k] = Fraction(1, 2)
    assert sum(map(abs, h)) == 1
    assert min(abs(sum(t * abs(v) for t, v in zip(s, h))) for s in signs) == 0
    assert sum(abs(Fraction(x, total) - y) for x, y in zip(a, h)) == delta


def main():
    vectors = pair_tests = squared_witnesses = nearest_witnesses = 0
    for n in range(2, 6):
        aa = [x for x in product(range(4), repeat=n) if sum(x) and (n < 5 or max(x) <= 2)]
        bb = [x for x in product((-1, 0, 1), repeat=n) if any(x)]
        for a in aa:
            d = discrepancy(a)
            minmax = Fraction(100)
            for b in bb:
                m = norm_pair(a, b)
                assert m >= 1 + d
                sign = [1 if x * y >= 0 else -1 for x, y in zip(a, b)]
                sign_mass = abs(sum(s * x for s, x in zip(sign, a)))
                assert Fraction(sign_mass, sum(a)) <= m - 1
                assert proximity(a, b) <= 2 * (m - 1)
                pair_tests += 1
                minmax = min(minmax, m)
            signopt = min(product((-1, 1), repeat=n), key=lambda s: abs(sum(x * t for x, t in zip(a, s))))
            bopt = [x * s for x, s in zip(a, signopt)]
            assert norm_pair(a, bopt) == 1 + d
            squared_witnesses += 1
            check_nearest(a, d)
            nearest_witnesses += 1
            vectors += 1
    print(f'VERIFY_OK profiles={vectors} arbitrary_signed_pairs={pair_tests} '
          f'exact_optimal_sign_witnesses={squared_witnesses} nearest_square_witnesses={nearest_witnesses} '
          'dimensions=2..5 arithmetic=exact')


if __name__ == '__main__':
    main()
