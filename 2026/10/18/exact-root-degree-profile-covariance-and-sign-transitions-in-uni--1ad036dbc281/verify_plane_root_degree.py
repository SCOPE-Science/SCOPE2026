"""Self-contained exact finite checks for the uniform plane-tree root/profile theorem.

Run: python3 verify_plane_root_degree.py
"""
from collections import Counter
from fractions import Fraction
from math import comb


def binom(a, b):
    return comb(a, b) if a >= 0 and 0 <= b <= a else 0


def degree_words(n):
    """Generate all valid plane-tree preorder offspring words of length n."""
    def visit(prefix, slots, edges):
        if len(prefix) == n:
            if slots == 0 and edges == 0:
                yield tuple(prefix)
            return
        for d in range(edges + 1):
            nxt = slots - 1 + d
            if nxt < 0 or (nxt == 0 and len(prefix) != n - 1):
                continue
            if nxt > n - len(prefix) - 1:
                continue
            prefix.append(d)
            yield from visit(prefix, nxt, edges - d)
            prefix.pop()
    yield from visit([], 1, n - 1)


def polynomial(n, k):
    return ((n * n + 3 * n + 2) * k * k
            + (-5 * n * n + n + 6) * k
            + 2 * n * n - 6 * n + 4)


def predicted(n, k):
    en = Fraction(n * binom(2*n-k-3, n-2), binom(2*n-2, n-1))
    er = Fraction(3*(n-1), n+1)
    covariance = en * Fraction(polynomial(n, k), n*(n-1)*(n+1))
    ern = er*en + covariance
    return en, er, covariance, ern


def sign_expectation(n, k):
    if n == 2:
        return 0
    if k == 0:
        return 1
    if k == 1:
        return -1
    if k == 2:
        return 1 if n == 3 else -1
    if k == 3:
        return 1 if n <= 7 else -1
    if k == 4:
        return 1 if n <= 24 else -1
    return 1


def verify():
    assertions = 0
    tree_total = 0
    for n in range(2, 12):
        trees = list(degree_words(n))
        num = len(trees)
        expected_n = Fraction(binom(2*n-2, n-1), n)
        assert num == expected_n
        tree_total += num
        totals = Counter()
        roots = 0
        products = Counter()
        for word in trees:
            root = word[0]
            roots += root
            frequency = Counter(word)
            for k, count in frequency.items():
                totals[k] += count
                products[k] += root * count
        for k in range(n):
            en, er, covariance, ern = predicted(n, k)
            assert Fraction(totals[k], num) == en, (n, k, 'count')
            assert Fraction(roots, num) == er, (n, k, 'root')
            assert Fraction(products[k], num) == ern, (n, k, 'cross')
            empirical = Fraction(products[k], num) - Fraction(roots*totals[k], num*num)
            assert empirical == covariance, (n, k, 'cov')
            observed = (covariance > 0) - (covariance < 0)
            assert observed == sign_expectation(n, k), (n, k, 'sign')
            assertions += 5
    # Check all possible finite-size threshold signs beyond exhaustively enumerable n.
    for n in range(2, 301):
        for k in range(n):
            p = polynomial(n, k)
            observed = (p > 0) - (p < 0)
            assert observed == sign_expectation(n, k), (n, k, 'large-sign')
            assertions += 1
    # Fixed-k limit coefficient is (k^2 - 5k + 2)/2^(k+1)
    # from the exact rational formula, since E[N_k]/n -> 1/2^(k+1).
    for k in range(15):
        expected = Fraction(k*k - 5*k + 2, 2**(k+1))
        n = 100000 + k
        actual = predicted(n, k)[2]
        assert abs(actual - expected) < Fraction(1, 250), (k, actual, expected)
        assertions += 1
    print(f'VERIFY_OK trees={tree_total} assertions={assertions}')


if __name__ == '__main__':
    verify()
