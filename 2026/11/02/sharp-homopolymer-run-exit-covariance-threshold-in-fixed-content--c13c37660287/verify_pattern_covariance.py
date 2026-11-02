"""Exact checks for the fixed-content 000/001 pattern-count covariance theorem.

Requires only Python's standard library. The universal proof is given separately;
these finite checks are independent corroboration, not an infinite certificate.
"""

from fractions import Fraction
from itertools import combinations


def falling(x, k):
    if x < k:
        return 0
    out = 1
    for j in range(k):
        out *= x - j
    return out


def probability(a, b, word):
    n = a + b
    k = len(word)
    if k > n:
        return Fraction(0)
    return Fraction(falling(a, word.count('0')) * falling(b, word.count('1')),
                    falling(n, k))


def theorem_covariance(a, b):
    n = a + b
    if a < 3 or b == 0 or n < 4:
        return Fraction(0)
    numerator = -a*b*b*(a-1)*(a-2)*((4*n-6)*a - (n+6)*(n-1))
    denominator = n*n*(n-3)*(n-2)*(n-1)*(n-1)
    return Fraction(numerator, denominator)


def placement_covariance(a, b):
    n = a + b
    if n < 3:
        return Fraction(0)
    L = n-2
    ex = L*probability(a, b, '000')
    ey = L*probability(a, b, '001')
    cross = Fraction(0)
    for i in range(L):
        for j in range(L):
            assignments = {}
            valid = True
            for pos, bit in list(zip(range(i, i+3), '000')) + list(zip(range(j, j+3), '001')):
                if pos in assignments and assignments[pos] != bit:
                    valid = False
                    break
                assignments[pos] = bit
            if valid:
                w = ''.join(assignments[pos] for pos in sorted(assignments))
                cross += probability(a, b, w)
    return cross - ex*ey


def brute_moments(a, b):
    n = a+b
    count = xsum = ysum = xysum = 0
    for zeros in combinations(range(n), a):
        zero_set = set(zeros)
        word = ''.join('0' if i in zero_set else '1' for i in range(n))
        x = sum(word[j:j+3] == '000' for j in range(n-2))
        y = sum(word[j:j+3] == '001' for j in range(n-2))
        count += 1
        xsum += x
        ysum += y
        xysum += x*y
    return Fraction(xsum,count),Fraction(ysum,count),Fraction(xysum,count)


def run():
    checks = 0
    for n in range(4,18):
        for a in range(1,n):
            b=n-a
            ex,ey,exy=brute_moments(a,b)
            assert ex == (n-2)*probability(a,b,'000')
            assert ey == (n-2)*probability(a,b,'001')
            assert exy-ex*ey == theorem_covariance(a,b)
            assert exy-ex*ey == placement_covariance(a,b)
            checks += 4
    for n in range(4,21):
        for a in range(1,n):
            b=n-a
            assert placement_covariance(a,b) == theorem_covariance(a,b)
            checks += 1
    # Integer sign and arithmetic exception checks.
    zero_pairs=[]
    for n in range(4,401):
        for a in range(3,n):
            sign_expr=(n+6)*(n-1)-(4*n-6)*a
            numerator=theorem_covariance(a,n-a).numerator
            assert (numerator > 0)-(numerator < 0) == (sign_expr > 0)-(sign_expr < 0)
            if numerator == 0:
                zero_pairs.append((n,a))
            checks += 1
    assert zero_pairs == [(4,3),(9,4)]
    checks += 1
    print('EXACT_CHECKS_PASSED',checks)
    print('NONDEGENERATE_ZERO_PAIRS',zero_pairs)
    print('ALL_DONE')

if __name__ == '__main__':
    run()
