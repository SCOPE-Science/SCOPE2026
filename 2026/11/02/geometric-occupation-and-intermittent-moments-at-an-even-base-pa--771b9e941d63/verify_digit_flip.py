"""Exact finite-prefix checks for a flip-resonant proportional-delay recurrence.

This script verifies finite identities. Infinite statements use the analytic proof.
"""
from collections import Counter
from fractions import Fraction


def odd_tail(n, base):
    t = 0
    while n % base % 2 == 1:
        t += 1
        n //= base
    return t


def inspect(base, init, G, K):
    N = base ** K
    x = [init]
    for n in range(N - 1):
        x.append(-x[n] + G(x[n // base]))
    f = lambda y: -init + G(y)
    orbit = [init]
    for _ in range(K):
        orbit.append(f(orbit[-1]))
    assert all(x[n] == orbit[odd_tail(n, base)] for n in range(N))
    assert all(x[base * k] == init for k in range(N // base))
    cnt = Counter(odd_tail(n, base) for n in range(N))
    assert all(cnt[r] == N // (2 ** (r + 1)) for r in range(K))
    assert cnt[K] == N // (2 ** K)
    return x, orbit


for m in (2, 4, 6):
    x, orbit = inspect(m, Fraction(1), lambda t: 2*t*t-t+3, 4)
    print(f'EXACT_NONLINEAR_BLOCK_AND_DIGIT_COUNTS_PASS_base_{m}')

for d in (Fraction(-3), Fraction(-1), Fraction(0), Fraction(4, 5),
          Fraction(1), Fraction(3, 2), Fraction(2), Fraction(3)):
    m, K, c = 4, 6, Fraction(2)
    x, orbit = inspect(m, c, lambda t, d=d: d*t, K)
    for r, y in enumerate(orbit):
        expect = c*(1-r) if d == 1 else c*((d-2)*d**r+1)/(d-1)
        assert y == expect
    # Exact 2nd moment from the digit histogram, including its terminal atom.
    lhs = sum(z*z for z in x)/len(x)
    rhs = sum(orbit[r]**2/Fraction(2**(r+1)) for r in range(K)) + orbit[K]**2/Fraction(2**K)
    assert lhs == rhs
    print(f'EXACT_AFFINE_ORBIT_AND_MOMENT_PASS_delta_{d}')
print('ALL_EXACT_FINITE_CHECKS_PASS')
