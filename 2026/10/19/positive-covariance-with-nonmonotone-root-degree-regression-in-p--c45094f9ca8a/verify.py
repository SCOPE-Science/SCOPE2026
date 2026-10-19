"""Exact independent checks for a preferential-attachment tree mixed-moment theorem.

Run with Python 3.9 or later: python verify.py
No dependencies beyond the standard library.
"""
from fractions import Fraction
from math import comb, pi, sqrt


def p(n):
    return Fraction(comb(2 * (n - 2), n - 2), 4 ** (n - 2))


def mean_d(n):
    return (2 * n - 3) * p(n)


def mean_l(n):
    return Fraction(2 * (n - 1), 3) + Fraction(4, 3) * p(n)


def expected_l_given_d1(n):
    return Fraction(2 * n, 3)


def expected_l_given_d2(n):
    return Fraction(2 * n, 3) - Fraction(2 * n - 6, 2 * n - 5)


def exact_cov(n):
    return sum((Fraction(k - 3, 3 * (k - 1)) * p(k)
                + Fraction(2 * k - 3, 3 * (k - 1) ** 2) * p(k) ** 2)
               for k in range(3, n))


def enumerate_full_histories(n):
    """Enumerate each possible list of chosen parents, tracking all degrees."""
    states = [(Fraction(1), (1, 1))]
    for k in range(2, n):
        nxt = []
        for weight, degrees in states:
            assert sum(degrees) == 2 * (k - 1)
            for idx, degree in enumerate(degrees):
                changed = list(degrees)
                changed[idx] += 1
                changed.append(1)
                nxt.append((weight * degree / (2 * (k - 1)), tuple(changed)))
        states = nxt
    assert sum(w for w, _ in states) == 1
    joint = {}
    for weight, degrees in states:
        d, l = degrees[0], degrees.count(1)
        joint[d, l] = joint.get((d, l), Fraction(0)) + weight
    return joint


def expectation(joint, f):
    return sum(w * f(d, l) for (d, l), w in joint.items())


def tests():
    checks = 0
    def check(expr, detail):
        nonlocal checks
        checks += 1
        if not expr:
            raise AssertionError(detail)

    for n in range(2, 10):
        j = enumerate_full_histories(n)
        m_d = expectation(j, lambda d, l: d)
        m_l = expectation(j, lambda d, l: l)
        cov = expectation(j, lambda d, l: d * l) - m_d * m_l
        check(m_d == mean_d(n), (n, 'root degree mean'))
        check(m_l == mean_l(n), (n, 'leaf mean'))
        check(cov == exact_cov(n), (n, 'mixed covariance'))
        check(expectation(j, lambda d, l: d * d) == 2 * (n - 1) - mean_d(n), (n, 'second root moment'))
        check(expectation(j, lambda d, l: int(d == 1)) == p(n), (n, 'root degree 1 mass'))
        if n >= 3:
            check(expectation(j, lambda d, l: int(d == 2)) == p(n), (n, 'root degree 2 mass'))
            check(expectation(j, lambda d, l: l * int(d == 1)) == p(n) * expected_l_given_d1(n), (n, 'conditional d1 mean'))
            check(expectation(j, lambda d, l: l * int(d == 2)) == p(n) * expected_l_given_d2(n), (n, 'conditional d2 mean'))
            check(expectation(j, lambda d, l: l * int(d == n - 1)) == (n - 1) * expectation(j, lambda d, l: int(d == n - 1)), (n, 'star endpoint'))
        if n >= 4:
            check(cov > 0, (n, 'positive covariance'))
            check(expected_l_given_d1(n) > expected_l_given_d2(n), (n, 'strict regression drop'))

    # Check algebraic variance recurrence independently of history enumeration.
    pprev = Fraction(1)
    d = Fraction(1)
    m = Fraction(2)
    covariance = Fraction(0)
    leaf_variance = Fraction(0)
    for n in range(2, 80):
        check(pprev == p(n), (n, 'survival probability recurrence'))
        check(d == mean_d(n), (n, 'root first moment recurrence'))
        check(m == mean_l(n), (n, 'leaf first moment recurrence'))
        check(covariance == exact_cov(n), (n, 'exact covariance recurrence'))
        q = 2 * (n - 1)
        g = (m / q) * (1 - m / q)
        leaf_variance = (1 - Fraction(2, q)) * leaf_variance + g
        covariance += d * m / q ** 2 - pprev / q
        m = (1 - Fraction(1, q)) * m + 1
        d = (1 + Fraction(1, q)) * d
        pprev = (1 - Fraction(1, q)) * pprev
    check(exact_cov(4) == Fraction(1, 16), 'first nontrivial covariance')
    check(exact_cov(3) == 0, 'small n zero covariance')

    # Asymptotic corroboration, not an infinite proof.
    x = 1.0
    d = 1.0
    m = 2.0
    cv = 0.0
    vl = 0.0
    for n in range(2, 100001):
        q = 2 * (n - 1)
        z = m / q
        vl = (1 - 2 / q) * vl + z * (1 - z)
        cv += d * m / q ** 2 - x / q
        m = (1 - 1 / q) * m + 1
        d = (1 + 1 / q) * d
        x = (1 - 1 / q) * x
    n = 100001
    cconst = 2 / (3 * sqrt(pi))
    check(abs(cv / sqrt(n) - cconst) / cconst < .01, 'root degree-leaf square-root covariance rate')
    check(abs(vl / n - 1 / 9) < .0003, 'linear leaf variance rate')
    vd = 2 * (n - 1) - d - d * d
    limit = sqrt(2 / (pi - 2))
    check(abs(sqrt(n) * cv / sqrt(vd * vl) - limit) / limit < .02, 'correlation rate')
    print(f'PASS: {checks} deterministic tests; exact history enumeration through n=9.')

if __name__ == '__main__':
    tests()
