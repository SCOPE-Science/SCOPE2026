"""Independent exact-arithmetic finite checks for the Pitman--Yor block-count threshold.

Only Python's standard library is needed. The infinite theorem is proved in
RESULT.md; checking finite cases is not a substitute for that proof.
"""
from fractions import Fraction
from math import comb, factorial


def generalized_stirling(n):
    row = [Fraction(0), Fraction(1)]
    for m in range(1, n):
        following = [Fraction(0)] * (m + 2)
        for k in range(1, m + 2):
            old = row[k] if k < len(row) else Fraction(0)
            earlier = row[k - 1]
            following[k] = (m - Fraction(k, 2)) * old + earlier
        row = following
    return row


def explicit_stirling(n, k):
    return (Fraction(factorial(n - 1), factorial(k - 1))
            * Fraction(4**k, 4**n) * comb(2*n - k - 1, n - k))


def pmf_from_chain(n, theta):
    probs = [Fraction(0), Fraction(1)]
    for m in range(1, n):
        updated = [Fraction(0)] * (m + 2)
        for k in range(1, m + 1):
            updated[k] += probs[k] * (m - Fraction(k, 2)) / (theta + m)
            updated[k + 1] += probs[k] * (theta + Fraction(k, 2)) / (theta + m)
        probs = updated
    return probs


def pmf_from_coefficients(n, theta):
    row = generalized_stirling(n)
    denominator = Fraction(1)
    for j in range(1, n):
        denominator *= theta + j
    top = Fraction(1)
    probs = [Fraction(0)]
    for k in range(1, n + 1):
        if k > 1:
            top *= theta + Fraction(k - 1, 2)
        probs.append(top * row[k] / denominator)
    return probs


def ratio(n, k, theta):
    return Fraction(2 * (n-k), k * (2*n-k-1)) * (k + 2*theta)


def H(n, k, theta):
    return k*(k-1)*(n-1) + 2*theta*(k*k-2*k*n-k+2*n*n)


def main():
    tests = 0
    for n in range(1, 43):
        row = generalized_stirling(n)
        for k in range(1, n+1):
            assert row[k] == explicit_stirling(n, k)
            tests += 1
        choices = [Fraction(-499, 1000), Fraction(-2, 5), Fraction(-1, 4),
                   Fraction(-1, 10), Fraction(0), Fraction(1, 2), Fraction(3)]
        if n >= 3:
            boundary = Fraction(-1, 2*(n-1))
            choices += [boundary-Fraction(1, 100000), boundary,
                        boundary+Fraction(1, 100000)]
        for theta in choices:
            p = pmf_from_chain(n, theta)
            q = pmf_from_coefficients(n, theta)
            assert p == q and sum(p) == 1
            assert all(item > 0 for item in p[1:])
            for k in range(1, n):
                assert p[k+1] / p[k] == ratio(n, k, theta)
                tests += 1
            lc = all(p[k]*p[k] >= p[k-1]*p[k+1]
                     for k in range(2, n))
            assert lc == (n <= 2 or theta >= Fraction(-1, 2*(n-1)))
            tests += 1
            for k in range(2, n):
                denom = k*(k-1)*(2*n-k)*(2*n-k-1)
                assert ratio(n, k-1, theta) - ratio(n, k, theta) == (2*H(n, k, theta) / denom)
                tests += 1
        if n >= 3:
            t = Fraction(-1, 2*(n-1))
            for k in range(2, n):
                assert H(n, k, t) == Fraction(n*(k-2)*(k*n-2*k+n), n-1)
                assert (H(n, k, t) == 0) == (k == 2)
                tests += 2
    print('PASS: {} exact-rational coefficient, PMF, ratio, boundary and sign checks'.format(tests))
    example = pmf_from_chain(4, Fraction(-1, 4))
    assert example[1:] == [Fraction(40,77), Fraction(20,77), Fraction(12,77), Fraction(5,77)]
    assert example[2]**2-example[1]*example[3] == Fraction(-80,5929)
    print('PASS: exact non-log-concave witness at sample size four and strength -1/4')


if __name__ == '__main__':
    main()
