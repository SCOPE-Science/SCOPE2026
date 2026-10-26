#!/usr/bin/env python3
"""Reproduce finite cyclic-trigram profile checks from first principles."""
from itertools import combinations


def spectrum(bits):
    n = len(bits)
    out = [0] * 8
    for i in range(n):
        k = 4 * bits[i] + 2 * bits[(i + 1) % n] + bits[(i + 2) % n]
        out[k] += 1
    return tuple(out)


def f(t, s):
    return int(s == t) + max(0, min(t, s - t))


def predicted_composition(p, q):
    if p == 0 or q == 0:
        return 1
    return sum(f(t, p) * f(t, q) for t in range(1, min(p, q) + 1))


def parameter_spectra(p, q):
    if p == 0:
        return {(0, 0, 0, 0, 0, 0, 0, q)}
    if q == 0:
        return {(p, 0, 0, 0, 0, 0, 0, 0)}
    ans = set()
    for t in range(1, min(p, q) + 1):
        for x in range(t + 1):
            a = p - t - x
            if a < 0 or (x == 0 and a != 0):
                continue
            for y in range(t + 1):
                h = q - t - y
                if h < 0 or (y == 0 and h != 0):
                    continue
                ans.add((a, x, t - y, y, x, t - x, y, h))
    return ans


def brute_composition(p, q):
    n = p + q
    ans = set()
    for ones in combinations(range(n), q):
        b = [0] * n
        for j in ones:
            b[j] = 1
        ans.add(spectrum(b))
    return ans


def composition_total(n):
    return sum(predicted_composition(p, n - p) for p in range(n + 1))


def rational_coefficients(N):
    # F(z) = num(z)/den(z). Integer recurrences; no symbolic package.
    num_inner = {0: 2, 1: -3, 2: 1, 3: -1,
                 5: 5, 6: -5, 7: 6, 8: -7, 9: 3}
    num = {j + 1: v for j, v in num_inner.items()}
    polys = [[1, -1]] * 5 + [[1, 1], [1, 0, 1], [1, 1, 1]]
    den = [1]
    for poly in polys:
        c = [0] * (len(den) + len(poly) - 1)
        for i, x in enumerate(den):
            for j, y in enumerate(poly):
                c[i + j] += x * y
        den = c
    assert den[0] == 1
    a = [0] * (N + 1)
    for n in range(N + 1):
        a[n] = num.get(n, 0) - sum(den[j] * a[n-j]
                                     for j in range(1, min(n, len(den)-1)+1))
    return a


def main():
    # Direct independent enumeration of all strings with each composition.
    for n in range(1, 19):
        for p in range(n + 1):
            q = n - p
            direct = brute_composition(p, q)
            formula = predicted_composition(p, q)
            structural = parameter_spectra(p, q)
            assert len(direct) == formula == len(structural), (n, p, q)
            assert direct == structural, (n, p, q)

    # The graph parameter formula is independent of brute-force words.
    coeffs = rational_coefficients(120)
    assert coeffs[0] == 0
    assert coeffs[1:17] == [2,3,4,6,8,13,18,27,38,53,72,98,128,167,214,271]
    for n in range(1, 121):
        assert coeffs[n] == composition_total(n), n
    print('VERIFY_OK: 18 word lengths, all fixed compositions; 120 rational coefficients')


if __name__ == '__main__':
    main()
