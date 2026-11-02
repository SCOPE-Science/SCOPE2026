#!/usr/bin/env python3
"""Exact Fibonacci certificates and finite checks of the Knott--natural bound.

The theorem's proof is by an infinite Fibonacci-state induction; the tests
below check its boundary data and finite instances and do not replace it.
"""
from decimal import Decimal, getcontext
getcontext().prec = 110
PHI = (Decimal(1) + Decimal(5).sqrt()) / 2


def fibonacci(n):
    if n < 0:
        return (-1) ** (-n + 1) * fibonacci(-n)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def lucas(n):
    return fibonacci(n - 1) + fibonacci(n + 1)


def phi_digits(n):
    # Exact integer-coordinate crosscheck of the greedy word in Z[phi].
    aa, bb = 0, n
    out = []
    previous = 1000
    for exponent in range(30, -41, -1):
        ff, gg = fibonacci(exponent), fibonacci(exponent - 1)
        if exponent != previous - 1 and (aa - ff) * PHI + bb - gg >= 0:
            aa -= ff
            bb -= gg
            out.append(exponent)
            previous = exponent
        if aa == 0 and bb == 0:
            break
    assert aa == bb == 0, (n, aa, bb)
    assert all(out[i] - out[i + 1] >= 2 for i in range(len(out) - 1))
    return out


def counts(powers):
    if len(powers) <= 1:
        return 1, 1
    gaps = [powers[i] - powers[i + 1] - 1 for i in range(len(powers) - 1)][::-1]
    s = gaps[0]
    natural = s // 2 + 1 if s % 2 == 0 else (s + 1) // 2
    knott = natural + (s % 2)
    r0k, r1k, r0n, r1n = 1, knott, 1, natural
    for s in gaps[1:]:
        if s % 2:
            c = (s + 3) // 2
            r0k, r1k = r1k, c * r1k - r0k
            r0n, r1n = r1n, c * r1n - r0n
        else:
            c = s // 2 + 1
            r0k, r1k = r1k, c * r1k
            r0n, r1n = r1n, c * r1n
    return r1k, r1n


def update(pair, cost):
    u, v = pair
    if cost % 2:
        a = (cost - 1) // 2
        return (a + 1) * u, a * u
    a = (cost - 2) // 2
    return (a + 1) * u + v, a * u + v


def envelope(span):
    if span % 2 == 0:
        k = span // 2
        return fibonacci(k + 1), fibonacci(k)
    k = span // 2
    return 2 * fibonacci(k), 2 * fibonacci(k - 1)


def run():
    checked = 0
    for span in range(2, 100):
        if span == 3:
            continue
        for cost in range(2, 100):
            x = update(envelope(span), cost)
            y = envelope(span + cost)
            assert x[0] <= y[0] and x[1] <= y[1], (span, cost, x, y)
            checked += 1
    rows = []
    total_ints = 0
    for j in range(1, 9):
        a, b = lucas(2 * j), lucas(2 * j + 1)
        maxi = -1
        mini = 10 ** 30
        argmax = []
        argmin = []
        for n in range(a, b + 1):
            K, H = counts(phi_digits(n))
            d = K - H
            if d > maxi:
                maxi, argmax = d, [n]
            elif d == maxi:
                argmax.append(n)
            if d < mini:
                mini, argmin = d, [n]
            elif d == mini:
                argmin.append(n)
            total_ints += 1
        witness = 2 * fibonacci(2 * j + 1)
        assert mini == 1 and argmin == [a], (j, mini, argmin)
        assert maxi == fibonacci(2 * j + 1) and argmax == [witness], (j, maxi, argmax)
        powers = phi_digits(witness)
        expected = [2*j] + [2*j-2-4*t for t in range(j)] + [-2*j]
        assert powers == expected, (j, powers, expected)
        K, H = counts(powers)
        assert (K, H) == (fibonacci(2*j + 2), fibonacci(2*j)), (j, K, H)
        rows.append((j, a, b, mini, maxi, witness))
    assert counts(phi_digits(3)) == (3, 2)
    assert counts(phi_digits(4)) == (3, 1)
    assert counts(phi_digits(5)) == (5, 5)
    print('CHECK_OK envelope_transition_cases=%d intervals=8 tested_integers=%d' % (checked, total_ints))
    print('j,lower_Lucas,upper_Lucas,min_excess,max_excess,witness')
    for row in rows:
        print(','.join(map(str, row)))


if __name__ == '__main__':
    run()
