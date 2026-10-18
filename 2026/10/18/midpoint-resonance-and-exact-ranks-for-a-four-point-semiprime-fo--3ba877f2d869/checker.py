"""Exact Fourier-minor arithmetic for centered four-point apertures.

Only standard Python; no floating point.  A p-th cyclotomic integer
of degree < p is zero precisely when its p cyclic coefficients are equal.
"""
from itertools import combinations, permutations
from math import comb


def cyclotomic_det(rows, cols, p):
    m = len(rows)
    coeff = [0] * p
    for perm in permutations(range(m)):
        sign = -1 if sum(perm[i] > perm[j]
                         for i in range(m) for j in range(i + 1, m)) % 2 else 1
        exponent = 0
        for i, j in enumerate(perm):
            ra, rx = divmod(rows[i], p)
            cb, cy = divmod(cols[j], p)
            sign *= -1 if ra * cb else 1
            exponent += rx * cy
        coeff[exponent % p] += sign
    return any(c != coeff[0] for c in coeff[1:])


def has_proportional_pair(rows, cols, p):
    # A phase (-1)^sign * zeta^exponent has a unique (sign, exponent)
    # representation when p is odd.  Test ratios exactly, never numerically.
    coords = [divmod(i, p) for i in rows]
    freqs = [divmod(i, p) for i in cols]
    for i, j in combinations(range(4), 2):
        e, x = coords[i]
        f, z = coords[j]
        values = [((e - f) * eta % 2, (x - z) * y % p)
                  for eta, y in freqs]
        if len(set(values)) == 1:
            return True
    for i, j in combinations(range(4), 2):
        eta, y = freqs[i]
        theta, z = freqs[j]
        values = [((eta - theta) * e % 2, (y - z) * x % p)
                  for e, x in coords]
        if len(set(values)) == 1:
            return True
    return False


def predicted(cols, p):
    even = [b for b in cols if b < p]
    odd = [b - p for b in cols if b >= p]
    if len(even) in (0, 4):
        return False
    if len(even) != 2:
        return True
    return (sum(even) - sum(odd)) % p != 0


def run():
    for p in (3, 5, 7, 11, 13):
        rows = (0, 1, p - 1, p)
        zero = 0
        nonproportional_singular = 0
        for cols in combinations(range(2 * p), 4):
            exact_nonzero = cyclotomic_det(rows, cols, p)
            assert exact_nonzero == predicted(cols, p), (p, rows, cols)
            zero += not exact_nonzero
            if not exact_nonzero and not has_proportional_pair(rows, cols, p):
                nonproportional_singular += 1
        assert nonproportional_singular == p * (p - 1) ** 2 // 4
        expected = 2 * comb(p, 4) + p * (p - 1) ** 2 // 4 if p >= 4 else p * (p - 1) ** 2 // 4
        assert zero == expected, (p, zero, expected)
        assert zero + (comb(2 * p, 4) - zero) == comb(2 * p, 4)
        print('p', p, 'total', comb(2 * p, 4), 'singular', zero,
              'nonproportional_singular', nonproportional_singular,
              'invertible', comb(2 * p, 4) - zero)
    print('CHECK_PASS')

if __name__ == '__main__':
    run()
