"""Independent finite verification of minimal time-indexed explanations for p Until q.

Usage: python3 checker.py. Standard library only.
"""
from collections import Counter
from fractions import Fraction
from math import comb


def truth(n, bits):
    return any((bits >> (2*j+1)) & 1 and
               all((bits >> (2*i)) & 1 for i in range(j))
               for j in range(n))


def predicted_sets(n, bits):
    p = lambda i: bool(bits & (1 << (2*i)))
    q = lambda i: bool(bits & (1 << (2*i+1)))
    witnesses = [j for j in range(n) if q(j) and all(p(i) for i in range(j))]
    if witnesses:
        ax = [sum(1 << (2*i) for i in range(j)) | (1 << (2*j+1))
              for j in witnesses]
        last = max(witnesses)
        cx = [sum(1 << (2*j+1) for j in witnesses)]
        for i in range(last):
            cx.append((1 << (2*i)) |
                      sum(1 << (2*j+1) for j in witnesses if j <= i))
        return sorted(ax), sorted(cx)
    z = next((j for j in range(n) if q(j)), n)
    zeros = [i for i in range(z) if not p(i)]
    ax = [(1 << (2*i)) | sum(1 << (2*j+1) for j in range(i+1))
          for i in zeros if i < n-1]
    if z == n:
        ax.append(sum(1 << (2*j+1) for j in range(n)))
    if z < n:
        assert zeros
        cx = [sum(1 << (2*i) for i in zeros)]
        for j in range(zeros[-1]+1):
            cx.append((1 << (2*j+1)) |
                      sum(1 << (2*i) for i in zeros if i < j))
    else:
        cx = [(1 << (2*j+1)) |
              sum(1 << (2*i) for i in zeros if i < j)
              for j in range(n)]
    return sorted(ax), sorted(cx)


def actual_sets(n, bits):
    N = 2*n
    original = truth(n, bits)
    locked_sufficient = []
    unlocked_sufficient = []
    for chosen in range(1 << N):
        holds = all(truth(n, alternate) == original
                    for alternate in range(1 << N)
                    if ((alternate ^ bits) & chosen) == 0)
        flips = any(truth(n, alternate) != original
                    for alternate in range(1 << N)
                    if ((alternate ^ bits) & ~chosen) == 0)
        if holds and not any((x & chosen) == x for x in locked_sufficient):
            locked_sufficient = [x for x in locked_sufficient
                                 if not ((chosen & x) == chosen)] + [chosen]
        if flips and not any((x & chosen) == x for x in unlocked_sufficient):
            unlocked_sufficient = [x for x in unlocked_sufficient
                                   if not ((chosen & x) == chosen)] + [chosen]
    return sorted(locked_sufficient), sorted(unlocked_sufficient)


def verify_profiles():
    for n in range(1, 5):
        for bits in range(1 << (2*n)):
            actual = actual_sets(n, bits)
            predicted = predicted_sets(n, bits)
            assert actual == predicted, (n, bits, actual, predicted)
        print('minimal explanations checked:', n)


def verify_joint_counts():
    for n in range(1, 8):
        observed = {True: Counter(), False: Counter()}
        for bits in range(1 << (2*n)):
            ax, cx = predicted_sets(n, bits)
            observed[truth(n, bits)][(len(ax), len(cx))] += 1
        expected = {True: Counter(), False: Counter()}
        total = 4**n
        for l in range(n):
            alpha = Fraction(1, 2**(l+1)) * (Fraction(2, 3) + Fraction(1, 3*4**(n-l-1)))
            for a in range(1, l+2):
                expected[True][(a, l+1)] += total * alpha * Fraction(comb(l, a-1), 2**l)
        for l in range(n-1):
            beta = Fraction(1, 3*2**(l+1)) * (1-Fraction(1, 4**(n-l-1)))
            for a in range(1, l+2):
                expected[False][(a, l+2)] += total * beta * Fraction(comb(l, a-1), 2**l)
        for a in range(1, n+1):
            expected[False][(a, n)] += total * Fraction(comb(n-1, a-1), 2**(2*n-1))
        assert observed == expected, (n, observed, expected)
        assert sum(observed[True].values()) == Fraction(2, 3)*(1-Fraction(1, 4**n))*total
        assert sum(observed[False].values()) + sum(observed[True].values()) == total
        print('exact joint distribution checked:', n)


if __name__ == '__main__':
    verify_profiles()
    verify_joint_counts()
    print('ALL_CHECKS_OK')
