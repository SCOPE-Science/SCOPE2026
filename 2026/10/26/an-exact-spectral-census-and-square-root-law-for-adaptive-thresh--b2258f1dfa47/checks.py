#!/usr/bin/env python3
"""Exact cross-checks for bipartite adaptive-threshold fixed-point counts."""
from fractions import Fraction
from itertools import product
from math import comb, factorial, pi, sqrt


def count_direct(a, b):
    """Brute-force all binary and threshold assignments, tiny graphs only."""
    d = [b] * a + [a] * b
    total = 0
    for x in product((0, 1), repeat=a+b):
        j = sum(x[a:])
        i = sum(x[:a])
        for thresholds in product(*(range(1, z+2) for z in d)):
            ok = True
            for u, (xu, k) in enumerate(zip(x, thresholds)):
                closed_sum = (j if u < a else i) + xu
                if (closed_sum >= k) != bool(xu):
                    ok = False
                    break
            total += ok
    return total


def count_double_sum(a, b):
    return sum(comb(a, i) * comb(b, j) * (j+1)**i * (b+1-j)**(a-i)
               * (i+1)**j * (a+1-i)**(b-j)
               for i in range(a+1) for j in range(b+1))


def count_spectrum(a, b):
    z = Fraction(1)
    term = Fraction(1)
    denom = (a+2)*(b+2)
    for k in range(1, min(a, b)+1):
        term *= Fraction((a-k+1)*(b-k+1), denom)
        z += term
    answer = z * (b+2)**a * (a+2)**b
    assert answer.denominator == 1
    return answer.numerator


def normalized_trace(a, b):
    term = 1.0
    s = term
    for k in range(1, min(a, b)+1):
        term *= (a-k+1)*(b-k+1)/((a+2)*(b+2))
        s += term
    return s


def main():
    print('Tiny exhaustive extended-state checks:')
    for a, b in ((1, 1), (1, 2), (2, 2), (2, 3)):
        values = (count_direct(a, b), count_double_sum(a, b), count_spectrum(a, b))
        assert values[0] == values[1] == values[2], (a, b, values)
        print(f'K_{{{a},{b}}}: {values[0]}')
    print('Additional integer-identity checks:')
    for a in range(1, 8):
        for b in range(1, 8):
            assert count_double_sum(a, b) == count_spectrum(a, b), (a, b)
    print('49 cases passed for 1 <= a,b <= 7.')
    print('Asymptotic diagnostic (not an infinite proof):')
    for n in (20, 80, 320, 1280):
        r = normalized_trace(n, n) / (sqrt(pi)/2 * sqrt(n))
        print(f'n={n}, trace / ((sqrt(pi)/2)*sqrt(n)) = {r:.8f}')

if __name__ == '__main__':
    main()
