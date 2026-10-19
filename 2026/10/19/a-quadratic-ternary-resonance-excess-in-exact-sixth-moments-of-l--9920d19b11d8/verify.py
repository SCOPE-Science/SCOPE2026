#!/usr/bin/env python3
"""Exact finite verification of lacunary sixth-moment identities."""
from collections import Counter
from math import cos, pi


def support(q, n):
    return [0] + [s * q**j for j in range(n) for s in (-1, 1)]


def coefficients(q, n, order):
    a = support(q, n)
    hist = Counter({0: 1})
    for _ in range(order):
        nxt = Counter()
        for shift in a:
            for exponent, count in hist.items():
                nxt[exponent + shift] += count
        hist = nxt
    return hist


def expected_energy(q, n):
    if n == 1:
        return 141
    if q == 3:
        return 120*n**3 + 240*n**2 - 280*n - 59
    if q == 4:
        return 120*n**3 + 80*n - 59
    if q == 5:
        return 120*n**3 + 32*n - 11
    return 120*n**3 + 20*n + 1


def expected_fourth(q, n):
    return 12*n*n + (14 if q == 3 else 6)*n + (-7 if q == 3 else 1)


def expected_a5(q, n):
    if q == 3:
        return 15 if n == 1 else 20*n + 5
    return {4: 5, 5: 1}.get(q, 0)


def expected_a3(q):
    return 1 if q == 3 else 0


def root_quadrature(q, n):
    largest = q**(n-1)
    samples = 6*largest + 1
    total = 0.0
    for k in range(samples):
        t = 2*pi*k/samples
        y = 1.0 + 2.0*sum(cos((q**j)*t) for j in range(n))
        total += y**6
    return total/samples


def main():
    exact_cases = 0
    for q in [3,4,5,6,7,8]:
        max_n = 8 if q <= 6 else 5
        for n in range(1, max_n+1):
            m2 = coefficients(q, n, 2)[0]
            assert m2 == 2*n+1, (q,n,'second')
            fourth = coefficients(q, n, 4)[0]
            assert fourth == expected_fourth(q,n), (q,n,'fourth',fourth)
            sixth = coefficients(q, n, 6)[0]
            assert sixth == expected_energy(q,n), (q,n,'sixth',sixth)
            next_m = q**n
            a3 = coefficients(q,n,3)[next_m]
            a5 = coefficients(q,n,5)[next_m]
            assert a3 == expected_a3(q), (q,n,'a3',a3)
            assert a5 == expected_a5(q,n), (q,n,'a5',a5)
            exact_cases += 5
    quad_cases = 0
    for q in [3,4,5,6]:
        for n in range(1,4):
            observed = root_quadrature(q,n)
            target = expected_energy(q,n)
            assert abs(observed-target) < 1e-7*max(1,target), (q,n,'quadrature',observed)
            quad_cases += 1
    print(f'PASS: {exact_cases} exact coefficient and moment checks; {quad_cases} independent root-of-unity quadratures')
    print('Example q=3, n=4:', coefficients(3,4,6)[0]);
    print('Example q=6, n=4:', coefficients(6,4,6)[0]);

if __name__ == '__main__':
    main()
