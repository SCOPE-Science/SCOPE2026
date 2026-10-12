"""Definition-based finite checks for the unary-inclusion defect distribution.

Run with Python 3: python verify.py
No third-party modules are needed.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb, factorial


def brute_joint_histogram(n):
    """Count 0/1 binary teams by (number of defects, number of pairs)."""
    counts = defaultdict(int)
    row_masks = [sum(1 << (i * n + j) for j in range(n)) for i in range(n)]
    col_masks = [sum(1 << (i * n + j) for i in range(n)) for j in range(n)]
    for mask in range(1 << (n * n)):
        w = sum((mask & row_masks[i] != 0) and (mask & col_masks[i] == 0)
                for i in range(n))
        counts[(w, mask.bit_count())] += 1
    return counts


def theoretical_probability(n, p, j):
    """Coefficient of z**j in the exact defect-count generating polynomial."""
    q = 1 - p
    return sum(Fraction((-1)**(k-j) * comb(n, k) * comb(k, j))
               * q**(n*k) * (1-q**(n-k))**k
               for k in range(j, n+1))


def brute_probability(histogram, n, p, j):
    return sum(Fraction(count) * p**edges * (1-p)**(n*n-edges)
               for (w, edges), count in histogram.items() if w == j)


def falling(n, k):
    return factorial(n) // factorial(n-k)


def theoretical_factorial_moment(n, p, k):
    q = 1-p
    return falling(n,k) * q**(n*k) * (1-q**(n-k))**k


def check():
    total = 0
    checked_probabilities = 0
    cases = 0
    for n in range(1, 5):
        hist = brute_joint_histogram(n)
        total += 1 << (n*n)
        assert sum(hist.values()) == (1 << (n*n))
        for p in [Fraction(0), Fraction(1, 3), Fraction(1, 2),
                  Fraction(2, 3), Fraction(1)]:
            probs = [brute_probability(hist, n, p, j) for j in range(n+1)]
            assert sum(probs) == 1
            for j in range(n+1):
                assert probs[j] == theoretical_probability(n, p, j), (n, p, j)
                checked_probabilities += 1
            for k in range(n+1):
                brute_moment = sum(falling(j,k)*probs[j] for j in range(k,n+1))
                assert brute_moment == theoretical_factorial_moment(n,p,k)
            cases += 1
        if n >= 2:
            q = Fraction(2, 3)
            one = q**n * (1-q**(n-1))
            two = q**(2*n) * (1-q**(n-2))**2
            assert two <= one**2
        print('n=', n, 'teams=', 1 << (n*n), 'unweighted_defect_histogram=',
              [sum(c for (w, e), c in hist.items() if w == j) for j in range(n+1)])
    print('VERIFY_OK', 'teams',total, 'rational_parameter_cases',cases,
          'exact_probability_coefficients', checked_probabilities)


if __name__ == '__main__':
    check()
