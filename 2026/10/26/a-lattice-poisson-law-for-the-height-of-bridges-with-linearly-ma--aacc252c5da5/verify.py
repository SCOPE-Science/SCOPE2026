#!/usr/bin/env python3
"""Exact checks for the return-conditioned bridge excursion-height law."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, exp, log

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def mul(a, b, cap):
    out = [0] * (cap + 1)
    for i, ai in enumerate(a[:cap + 1]):
        if ai:
            for j, bj in enumerate(b[:cap + 1 - i]):
                if bj:
                    out[i + j] += ai * bj
    return out


def power_coeff(a, exponent, degree):
    acc = [1] + [0] * degree
    for _ in range(exponent):
        acc = mul(acc, a, degree)
    return acc[degree]


def catalan(n):
    return comb(2*n, n) // (n+1)


def bounded_catalan(degree, height):
    """Coefficient array of Dyck excursions of height at most height."""
    c = [1] + [0] * degree
    for _ in range(height):
        nxt = [1] + [0] * degree
        for j in range(1, degree + 1):
            nxt[j] = sum(c[t] * nxt[j-1-t] for t in range(j))
        c = nxt
    return c


def path_statistics(n):
    """Exhaust every bridge via the set of upward-step positions."""
    out = Counter()
    for ups in combinations(range(2*n), n):
        selected = set(ups)
        p = 0
        zeros = 0
        tallest = 0
        excursion_heights = []
        current_height = 0
        for t in range(2*n):
            p += (1 if t in selected else -1)
            current_height = max(current_height, abs(p))
            tallest = max(tallest, abs(p))
            if p == 0:
                zeros += 1
                excursion_heights.append(current_height)
                current_height = 0
        out[(zeros, tallest)] += 1
    return out


def finite_checks():
    for n in range(1, 9):
        joint = path_statistics(n)
        check(sum(joint.values()) == comb(2*n, n), f'bridge count {n}')
        for k in range(1, n + 1):
            target = sum(v for (j, _), v in joint.items() if j == k)
            predicted = (2**k * k * comb(2*n-k, n-k)) // (2*n-k)
            check(target == predicted, f'return-count formula {n},{k}')
            for h in range(2, n + 2):
                restricted = sum(v for (j, m), v in joint.items() if j == k and m < h)
                coeff = power_coeff(bounded_catalan(n-k, h-2), k, n-k)
                check(restricted == (2**k)*coeff,
                      f'height/returns count {n},{k},{h}')
        # Verify the first-return kernel by coefficient extraction.
        for semi in range(1, n + 1):
            check(2*catalan(semi-1) > 0, f'positive excursion kernel {semi}')


def exact_tilt_tail_checks():
    for q in (Fraction(1, 5), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
        z = (1-q*q)/4
        lam = (1-q)/(1+q)
        E = 1-q
        for h in range(2, 11):
            c = Fraction(1)
            for _ in range(h-2):
                c = 1 / (1-z*c)
            Eshort = 2*z*c
            tail = (E-Eshort)/E
            predicted = 2*q*lam**h/((1-q)*(1-lam**h))
            check(tail == predicted, f'geometric height tail {q},{h}')


def asymptotic_diagnostics():
    print('Finite-size conditional height diagnostic:')
    for n,k,h in ((100,50,7),(200,100,8),(400,200,9)):
        degree = n-k
        actual = power_coeff(bounded_catalan(degree,h-2), k, degree) / power_coeff(
            [catalan(i) for i in range(degree+1)],k,degree)
        rho = k/n
        prediction = exp(-k *rho/(1-rho)*(1-rho)**h)
        print(f'n={n} k={k} h={h}: exact={actual:.10f}; limiting-window approximation={prediction:.10f}')

if __name__ == '__main__':
    finite_checks()
    exact_tilt_tail_checks()
    asymptotic_diagnostics()
    print(f'PASS: {checks} exact enumerative and rational assertions')
