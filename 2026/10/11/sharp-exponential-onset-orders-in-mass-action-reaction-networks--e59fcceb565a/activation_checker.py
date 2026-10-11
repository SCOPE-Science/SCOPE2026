"""Exact low-order Taylor checks for mass-action activation valuations.

Run with Python 3.9+: python activation_checker.py
All arithmetic uses fractions; these tests support, but do not replace, the proof.
"""
from fractions import Fraction
from random import Random


def activation_orders(initial, reactions):
    n = len(initial)
    inf = None
    h = [0 if value > 0 else inf for value in initial]
    for _ in range(n):
        old = h[:]
        for i in range(n):
            for alpha, beta, _ in reactions:
                if alpha[i] or not beta[i]:
                    continue
                if any(alpha[j] and old[j] is None for j in range(n)):
                    continue
                proposal = 1 + sum(alpha[j] * old[j] for j in range(n) if alpha[j])
                if h[i] is None or proposal < h[i]:
                    h[i] = proposal
        if h == old:
            break
    return h


def convolution(a, b, k):
    out = [Fraction(0) for _ in range(k + 1)]
    for i, ai in enumerate(a[: k + 1]):
        if not ai:
            continue
        for j, bj in enumerate(b[: k + 1 - i]):
            out[i + j] += ai * bj
    return out


def formal_coefficients(initial, reactions, degree):
    n = len(initial)
    c = [[Fraction(v)] + [Fraction(0)] * degree for v in initial]
    for k in range(degree):
        rhs = [Fraction(0)] * n
        for alpha, beta, rate in reactions:
            v = [Fraction(1)] + [Fraction(0)] * k
            for j, a in enumerate(alpha):
                for _ in range(a):
                    v = convolution(v, c[j], k)
            for i in range(n):
                rhs[i] += (beta[i] - alpha[i]) * rate * v[k]
        for i in range(n):
            c[i][k + 1] = rhs[i] / (k + 1)
    return c


def predicted_leading(initial, reactions, orders):
    n = len(initial)
    coefficients = [Fraction(v) if v > 0 else None for v in initial]
    indices = sorted((h, i) for i, h in enumerate(orders) if h is not None and h > 0)
    for h, i in indices:
        total = Fraction(0)
        for alpha, beta, rate in reactions:
            if alpha[i] or beta[i] == 0:
                continue
            if any(alpha[j] and orders[j] is None for j in range(n)):
                continue
            exponent = 1 + sum(alpha[j] * orders[j] for j in range(n) if alpha[j])
            if exponent != h:
                continue
            term = rate * beta[i]
            for j, a in enumerate(alpha):
                if a:
                    term *= coefficients[j] ** a
            total += term
        assert total > 0
        coefficients[i] = total / h
    return coefficients


def run():
    rng = Random(20261004)
    cases = 0
    for _ in range(140):
        n = rng.randrange(2, 5)
        degree = 10
        initial = [Fraction(rng.randrange(3)) for _ in range(n)]
        reactions = []
        for _ in range(rng.randrange(2, 10)):
            alpha = [0] * n
            for __ in range(rng.randrange(3)):
                alpha[rng.randrange(n)] += 1
            beta = [rng.randrange(3) for __ in range(n)]
            rate = Fraction(rng.randrange(1, 4), rng.randrange(1, 4))
            reactions.append((alpha, beta, rate))
        h = activation_orders(initial, reactions)
        coefficients = predicted_leading(initial, reactions, h)
        series = formal_coefficients(initial, reactions, degree)
        for i, order in enumerate(h):
            if order is None or order > degree:
                assert all(z == 0 for z in series[i]), (reactions, i, order)
            elif order == 0:
                assert series[i][0] == initial[i]
            else:
                assert all(z == 0 for z in series[i][:order]), (reactions, i, order)
                assert series[i][order] == coefficients[i], (reactions, i, order)
        cases += 1
    for m in (1, 2, 3):
        for s in (1, 2, 3, 4):
            alpha0 = [0] * s
            beta0 = [0] * s
            beta0[0] = 1
            reactions = [(alpha0, beta0, Fraction(1))]
            for j in range(s - 1):
                alpha = [0] * s
                beta = [0] * s
                alpha[j] = m
                beta[j] = m - 1
                beta[j + 1] = 1
                reactions.append((alpha, beta, Fraction(1)))
            h = activation_orders([Fraction(0)] * s, reactions)
            expected = [(m ** (j + 1) - 1) // (m - 1) if m > 1 else j + 1 for j in range(s)]
            assert h == expected, (m, s, h, expected)
            cases += 1
    print(f"PASS: {cases} exact rational checks; sharp chains for m=1,2,3 and s<=4")


if __name__ == '__main__':
    run()
