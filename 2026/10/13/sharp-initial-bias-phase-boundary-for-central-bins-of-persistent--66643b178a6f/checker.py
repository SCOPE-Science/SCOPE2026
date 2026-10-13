"""Exact-rational checks for the sharp biased-start central-bin phase theorem.

Run with Python 3: python checker.py
This finite verification does not replace the theorem's infinite-length proof.
"""
from fractions import Fraction as F
from math import comb


def masses(length, u, alpha):
    """Independent Markov-recursion evaluation (no use of binomial coefficients)."""
    p = 1 / (1 + u)
    q = 1 - p
    plus, minus = [F(0)] * 2, [F(0)] * 2
    plus[1], minus[0] = alpha, 1 - alpha
    for k in range(2, length + 1):
        np, nm = [F(0)] * (k + 1), [F(0)] * (k + 1)
        for j in range(k):
            np[j + 1] += p * plus[j] + q * minus[j]
            nm[j] += p * minus[j] + q * plus[j]
        plus, minus = np, nm
    return [a + b for a, b in zip(plus, minus)]


def c(n, j, u):
    return sum((F(comb(n, h) * comb(n, h - j)) * u**(2*h - j)
                for h in range(j, n + 1)), F(0))


def formula(m, u, alpha):
    n = m - 1
    a, b = c(n, 1, u), c(n, 2, u)
    p = 1 / (1 + u)
    return p**(2*m - 1) * (u / n) * ((2*alpha - 1) * (a + u*b) - u*(a+b))


def check():
    tested = 0
    for u in (F(1, 9), F(1, 4), F(1, 3), F(2, 3), F(4, 5)):
        p = 1 / (1 + u)
        alpha_star = F(3, 2) - p
        for m in range(2, 19):
            n = m - 1
            a, b = c(n, 1, u), c(n, 2, u)
            assert a > b >= 0
            theta = u * (a + b) / (a + u*b)
            assert u <= theta < 2*u/(1+u)
            if m >= 3:
                assert theta > u
            for alpha in (F(1, 2), F(3, 5), F(2, 3), F(7, 10),
                          F(4, 5), F(9, 10), alpha_star, F(1)):
                P = masses(2*m, u, alpha)
                observed = P[m + 1] - P[m]
                predicted = formula(m, u, alpha)
                assert observed == predicted, (m, u, alpha, observed, predicted)
                assert sum(P) == 1
                if alpha >= alpha_star:
                    assert observed > 0
                tested += 1
    u = F(1, 3)
    alpha = F(7, 10)
    assert masses(4, u, alpha)[3] > masses(4, u, alpha)[2]
    assert masses(10, u, alpha)[6] < masses(10, u, alpha)[5]
    assert c(1, 1, u) == u and c(1, 2, u) == 0
    print(f"PASS {tested} exact-rational parameter and chain-length comparisons; reversal example PASS")


if __name__ == '__main__':
    check()
