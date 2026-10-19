"""Self-contained exact checker for weak directed-path endomorphism centralizers.
Run: python check.py. No third-party dependencies. Exhaustive finite tests
are independent checks, not a replacement for the uniform proof.
"""
from collections import Counter
from itertools import product
from math import comb


def path_maps(n):
    for start in range(n):
        for steps in product((0, 1), repeat=n-1):
            if start + sum(steps) >= n:
                continue
            values = [start]
            for step in steps:
                values.append(values[-1] + step)
            yield tuple(values)


def compose(f, g):
    return tuple(f[g[i]] for i in range(len(g)))


def clamp(n, a, b):
    return tuple(min(max(i, a), b) for i in range(n))


def expected_polynomial(l, h, r):
    coefficients = Counter()
    for i in range(h):
        for j in range(i, h):
            middle = comb(h - 1, j - i)
            left_options = range(l + 1) if i == 0 else (0,)
            right_options = range(r + 1) if j == h - 1 else (0,)
            for alpha in left_options:
                for beta in right_options:
                    weight = middle * comb(l, alpha) * comb(r, beta)
                    coefficients[1 + j - i + alpha + beta] += weight
    return coefficients


def convolution(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out


def rational_coefficients(N, u, z):
    # x*u*z*(1-x-x*u*z)^2 divided by the five factors
    numerator = convolution([0, u*z], convolution([1, -(1+u*z)], [1, -(1+u*z)]))
    denominator = [1]
    for factor in ([1, -1], [1, -1], [1, -u*z],
                   [1, -(1+z)], [1, -(1+z)],
                   [1, -u*(1+z)], [1, -u*(1+z)]):
        denominator = convolution(denominator, factor)
    result = [0] * (N+1)
    for n in range(N+1):
        result[n] = (numerator[n] if n < len(numerator) else 0) - sum(
            denominator[j]*result[n-j] for j in range(1, min(n, len(denominator)-1)+1))
    return result


def main():
    all_direct = {}
    for n in range(1, 10):
        maps = tuple(path_maps(n))
        assert len(maps) == ((n+1)*2**(n-2) if n >= 2 else 1)
        rank_profile = Counter()
        for a in range(n):
            for b in range(a, n):
                e = clamp(n, a, b)
                actual = Counter()
                for g in maps:
                    if compose(e, g) == compose(g, e):
                        rank = g[-1] - g[0] + 1
                        actual[rank] += 1
                        rank_profile[(b-a+1, rank)] += 1
                expected = expected_polynomial(a, b-a+1, n-b-1)
                assert actual == expected, (n, a, b, actual, expected)
        direct_count = sum(rank_profile.values())
        formula = (4*n-12)*2**n + (n*n+9*n+24)//2
        assert direct_count == formula, (n, direct_count, formula)
        all_direct[n] = rank_profile
        print('n=', n, 'total=', direct_count, 'rank_cells=', len(rank_profile))

    for u, z in ((1,1), (2,3), (3,2), (2,2)):
        coeff = rational_coefficients(9, u, z)
        for n in range(1, 10):
            actual = sum(count*u**h*z**k for (h, k), count in all_direct[n].items())
            assert actual == coeff[n], (n, u, z, actual, coeff[n])
    print('ALL_EXACT_CHECKS_PASSED')


if __name__ == '__main__':
    main()
