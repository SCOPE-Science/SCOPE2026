"""Independent finite checks for the three-run prefix-normal generating function.
Run with: python3 verify.py (standard library only).
"""
from collections import Counter
from itertools import product
from math import comb


def prefix_normal(word):
    n = len(word)
    pref = 0
    for k in range(1, n + 1):
        pref += word[k - 1] == '1'
        ones = pref
        for start in range(1, n - k + 1):
            ones += (word[start + k - 1] == '1') - (word[start - 1] == '1')
            if ones > pref:
                return False
    return True


def criterion(a, b, c, d, e):
    return a >= c and a >= e and (d >= b or a >= c + e)


def poly_mult(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, pi in enumerate(p):
        for j, qj in enumerate(q):
            out[i + j] += pi * qj
    return out


def inverse_coeffs(den, length):
    assert den[0] == 1
    out = [0] * (length + 1)
    out[0] = 1
    for k in range(1, length + 1):
        out[k] = -sum(den[j] * out[k - j] for j in range(1, min(k, len(den) - 1) + 1))
    return out

# The generating function uses x for zero count and t for one count.
# It factors into x^2 t^3 [1+(1+x)(t+t^2+t^3)] A(x) B(t).
a = inverse_coeffs(poly_mult(poly_mult([1, -1], [1, -1]),
                               poly_mult([1, -1], [1, 1])), 28)
b = inverse_coeffs(poly_mult(poly_mult(poly_mult([1, -1], [1, -1]),
                                         poly_mult([1, -1], poly_mult([1, 1], [1, 1]))),
                               [1, 1, 1]), 28)
numerator = [(2, 3)] + [(i, 3 + k) for k in (1, 2, 3) for i in (2, 3)]

def gf_coefficient(n, ones):
    zeros = n - ones
    return sum(a[zeros - i] * b[ones - j]
               for i, j in numerator
               if zeros >= i and ones >= j)

observed = Counter()
all_run_words = Counter()
for n in range(5, 27):
    for aa in range(1, n - 3):
        for cc in range(1, n - aa - 2):
            for ee in range(1, n - aa - cc - 1):
                for bb in range(1, n - aa - cc - ee):
                    for dd in range(1, n - aa - cc - ee - bb + 1):
                        ff = n - aa - bb - cc - dd - ee
                        if ff < 0:
                            continue
                        ones = aa + cc + ee
                        all_run_words[n] += 1
                        if criterion(aa, bb, cc, dd, ee):
                            observed[n, ones] += 1
                        if n <= 16:
                            word = '1' * aa + '0' * bb + '1' * cc + '0' * dd + '1' * ee + '0' * ff
                            if prefix_normal(word) != criterion(aa, bb, cc, dd, ee):
                                raise AssertionError((n, aa, bb, cc, dd, ee, ff))
    assert all_run_words[n] == comb(n, 5), (n, all_run_words[n])
    for ones in range(3, n - 1):
        assert observed[n, ones] == gf_coefficient(n, ones), (n, ones, observed[n, ones], gf_coefficient(n, ones))

# Separate exhaustive membership check for all five positive run parameters through 6.
for aa, bb, cc, dd, ee in product(range(1, 7), repeat=5):
    word = '1' * aa + '0' * bb + '1' * cc + '0' * dd + '1' * ee
    assert prefix_normal(word) == criterion(aa, bb, cc, dd, ee)

print('VERIFY_OK 7776_run_parameter_tests 5_to_26_length_weight_GF_coefficients direct_prefix_normal_5_to_16 three_run_total_choose_n_5')
for n in (5, 6, 7, 8, 9, 10, 16, 20, 26):
    print(n, sum(observed[n, ones] for ones in range(3, n - 1)), all_run_words[n])
