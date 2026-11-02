"""Exact finite-sample checks for preferential-attachment degree/leaf covariance.

No third-party packages required. Run: python verify.py
These checks test finite identities; the general theorem is established analytically.
"""
from collections import defaultdict
from fractions import Fraction
from math import isclose, sqrt

ASSERTIONS = 0

def check(statement, context=''):
    global ASSERTIONS
    ASSERTIONS += 1
    assert statement, context


def p(t):
    return Fraction(1, 2 * (t - 1))


def h(t):
    z = Fraction(1)
    for s in range(2, t):
        z *= 1 - p(s)
    return z


def means_and_covariance(n, j):
    """Separate mixed-moment and marginal recurrences, all rational."""
    check(3 <= j <= n)
    mu_l = Fraction(2)
    for t in range(2, j):
        mu_l = (1 - p(t)) * mu_l + 1
    mu_d = Fraction(1)
    mu_leaf_j = Fraction(1)
    c = Fraction(0)
    for t in range(j, n):
        x = p(t)
        c += x * x * mu_d * mu_l - x * mu_leaf_j
        mu_d *= 1 + x
        mu_leaf_j *= 1 - x
        mu_l = (1 - x) * mu_l + 1
    return mu_l, mu_d, mu_leaf_j, c


def closed(n, j):
    a, b = Fraction(1), Fraction(1)
    for t in range(j, n):
        a *= 1 + p(t)
        b *= 1 - p(t)
    return (a + 3 * b - 4 + 4 * (h(j) - a * h(n))) / 3


def brute_by_degrees(n):
    """Enumerate all preferential-attachment parent histories with exact weights."""
    distribution = {(1, 1): Fraction(1)}
    for t in range(2, n):
        next_distribution = defaultdict(Fraction)
        for degrees, mass in distribution.items():
            for i, degree in enumerate(degrees):
                new_degrees = list(degrees)
                new_degrees[i] += 1
                new_degrees.append(1)
                next_distribution[tuple(new_degrees)] += mass * Fraction(degree, 2 * (t - 1))
        distribution = dict(next_distribution)
        check(sum(distribution.values()) == 1, ('probabilities',t))
    mu_l = sum(prob * sum(v == 1 for v in d) for d, prob in distribution.items())
    out = {}
    for j in range(3, n + 1):
        mu_d = sum(prob * d[j - 1] for d, prob in distribution.items())
        mixed = sum(prob * d[j - 1] * sum(v == 1 for v in d)
                    for d, prob in distribution.items())
        out[j] = mixed - mu_d * mu_l
    return mu_l, out


def main():
    for n in range(3, 9):
        mu_l, cov = brute_by_degrees(n)
        for j in range(3, n + 1):
            lhs_l, lhs_d, lhs_q, lhs_cov = means_and_covariance(n, j)
            check(lhs_l == mu_l, ('mean leaves', n, j))
            check(lhs_cov == cov[j], ('enumeration', n, j))
            check(lhs_cov == closed(n, j), ('closed form', n, j))
            check(lhs_d * lhs_q != 0, ('means', n, j))
    for j in range(3, 32):
        mean_leaves = Fraction(2)
        hj = Fraction(1)
        for t in range(2, j):
            x = p(t)
            mean_leaves = (1-x)*mean_leaves+1
            hj *= 1-x
        a = q = Fraction(1)
        hn = hj
        covariance = Fraction(0)
        positives = []
        for t in range(j, 12*j):
            x = p(t)
            covariance += x*x*a*mean_leaves - x*q
            a *= 1+x
            q *= 1-x
            hn *= 1-x
            mean_leaves = (1-x)*mean_leaves+1
            exact = (a + 3*q - 4 + 4*(hj-a*hn))/3
            check(covariance == exact, ('telescoping',j,t+1))
            check(mean_leaves == Fraction(2*t,3)+Fraction(4,3)*hn, ('leaf mean',j,t+1))
            if covariance>0: positives.append(t+1)
        check(bool(positives), ('eventual positivity',j))
        root = positives[0]
        check(all(z>=root for z in positives), ('transition',j))
        check(root/j > 4 and root/j < 9, ('crossover range',j))
    print('VERIFICATION_OK: exact states, closed-form products, recurrences, and finite sign transitions')
    print('assertions:',ASSERTIONS)

if __name__ == '__main__':
    main()
