"""Exact, independent checks for the two-right-neighbor reverse-rank covariance law.
Run with Python 3.10+; only the standard library is required.
Finite checks complement, but do not replace, the algebraic proof.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial

count = 0

def check(statement, label):
    global count
    count += 1
    if not statement:
        raise AssertionError(label)


def score(p):
    n = len(p)
    return (sum(min(p[i], p[i + delta])
                for delta in (1, 2) for i in range(n - delta))
            + p[-2] + 2 * p[-1])


def reverse(p):
    q = [0] * len(p)
    for i, val in enumerate(p):
        q[val - 1] = i + 1
    return q


def mean(n):
    return F((n + 1) * (4 * n + 3), 6)


def variance(n):
    return F((n + 1) * (4 * n * n + 14 * n + 35), 180)


def covariance(n):
    return F(4*n**4 + n**3 + 11*n*n - 127*n + 147, 18*n*(n-1))


def correlation(n):
    return F(10*(4*n**4 + n**3 + 11*n*n - 127*n + 147),
             n*(n-1)*(n+1)*(4*n*n + 14*n + 35))


def pair_projection(n, a):
    # a is symmetric edge-weight dict keyed by sorted zero-indexed (i,j)
    edges = [(i, j) for i in range(n) for j in range(i+1, n)]
    avg = sum(a[e] for e in edges) / F(len(edges))
    cent = {e: a[e] - avg for e in edges}
    s = [sum(cent[(min(i, j), max(i, j))]
             for j in range(n) if i != j) for i in range(n)]
    one = {e: (s[e[0]] + s[e[1]]) / (n-2) for e in edges}
    two = {e: cent[e] - one[e] for e in edges}
    return cent, one, two, s


def dot(a, b):
    return sum((a[k] * b[k] for k in a), F(0))


def exhaustive(n):
    total = factorial(n)
    a_sum = 0
    a_sq = 0
    ab_sum = 0
    for p in permutations(range(1, n+1)):
        a = score(p)
        b = score(reverse(p))
        a_sum += a
        a_sq += a*a
        ab_sum += a*b
    m = F(a_sum, total)
    v = F(a_sq, total) - m*m
    c = F(ab_sum, total) - m*m
    check(m == mean(n), (n, 'mean', m, mean(n)))
    check(v == variance(n), (n, 'variance', v, variance(n)))
    check(c == covariance(n), (n, 'covariance', c, covariance(n)))
    check(c / v == correlation(n), (n, 'correlation'))


def projection_check(n):
    edges = [(i, j) for i in range(n) for j in range(i+1, n)]
    a = {(i, j): F(int(1 <= j-i <= 2)) for i, j in edges}
    b = {(i, j): F(i+1) for i, j in edges}
    ac, a1, a2, sa = pair_projection(n, a)
    bc, b1, b2, sb = pair_projection(n, b)
    norm_a1 = F(2*(5*n-18), n*(n-2))
    norm_a2 = F(2*n**3-17*n*n+43*n-26, (n-2)*(n-1))
    norm_b1 = F(n*(n-1)*(n+1)*(4*n-7), 180)
    norm_b2 = F(n*(n-3)*(n-1)*(n+1), 180)
    check(dot(a1, a1) == norm_a1, (n,'A-one norm'))
    check(dot(a2, a2) == norm_a2, (n,'A-two norm'))
    check(dot(b1, b1) == norm_b1, (n,'B-one norm'))
    check(dot(b2, b2) == norm_b2, (n,'B-two norm'))
    check(dot(a1, b1) == F(n-3, 2), (n,'mixed one'))
    check(dot(a2, b2) == F((n-3)*(2*n-7), 6), (n,'mixed two'))
    check(dot(ac, bc) == dot(a1,b1)+dot(a2,b2), (n,'orthogonality'))
    for i in range(n):
        expected_sb = F((i+1)*n) - F((i+1)*(i+2),2) - F((n-1)*(n+1),3)
        check(sb[i] == expected_sb, (n,'score B', i))
    for i in range(n):
        check(sum(a1[e] for e in edges if i in e) == sa[i], (n, 'score A1', i))
        check(sum(a2[e] for e in edges if i in e) == 0, (n, 'score A2', i))
        check(sum(b1[e] for e in edges if i in e) == sb[i], (n, 'score B1', i))
        check(sum(b2[e] for e in edges if i in e) == 0, (n, 'score B2', i))
    xvar = norm_a1 * norm_b1 / (n-1) + norm_a2 * norm_b2 / F(n*(n-3),2)
    lvar = F((n+1)*(5*n-9), 12)
    x_l_cov = -F((n+1)*(5*n-18),24)
    check(xvar + lvar + 2*x_l_cov == variance(n), (n,'variance decomposition'))
    reverse_cov_x = F(n-3,2)**2 / (n-1) + F((n-3)*(2*n-7),6)**2 / F(n*(n-3),2)
    reverse_cov_l = F((3*n-5)**2, 4*(n-1))
    check(reverse_cov_x + reverse_cov_l == covariance(n), (n,'reverse covariance decomposition'))


def monotonicity_checks():
    # At n=5 correlation is the unique maximum over integer n >= 4.
    check(correlation(5) > correlation(4), 'first increase')
    for n in range(5, 501):
        check(correlation(n+1) < correlation(n), (n,'strict decrease'))
        check(correlation(n) > 0, (n,'positive'))
    for n in range(4, 501):
        check(correlation(n) < 1, (n,'strictly less than one'))
    # Exact finite values and limit coefficient.
    check(correlation(4) == F(301,310), 'n=4 rho')
    check(correlation(5) == F(201,205), 'n=5 rho')


if __name__ == '__main__':
    for n in range(4, 9):
        exhaustive(n)
    for n in range(4, 41):
        projection_check(n)
    monotonicity_checks()
    print(f'PASS: {count} exact assertions, independent exhaustive permutations for n=4..8')
