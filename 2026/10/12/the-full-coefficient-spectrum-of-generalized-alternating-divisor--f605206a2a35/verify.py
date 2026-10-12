"""Exact finite checks accompanying the prime-sieve divisor-sum coefficient theorem.

Run: python3 verify.py
All assertions concern finite arithmetic; the unrestricted argument is in RESULT.md.
"""
from fractions import Fraction
from math import pi


def primes_up_to(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p :: p] = b'\x00' * ((n - p * p) // p + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def local_factor(p):
    return Fraction((p - 1) ** 2 * (p + 1), p ** 3)


def truncation(primes, target):
    value = Fraction(1)
    selected = []
    for p in primes:
        value_next = value * local_factor(p)
        if value_next >= target:
            value = value_next
            selected.append(p)
        assert value >= target
    return value, selected


def sigma_up_to(N):
    s = [0] * (N + 1)
    for d in range(1, N + 1):
        for n in range(d, N + 1, d):
            s[n] += d
    return s


def signed_sum(sigma, N, primes):
    mask = bytearray(N + 1)
    for p in primes:
        for n in range(p, N + 1, p):
            mask[n] = 1
    return sum((1 - 2 * mask[n]) * sigma[n] for n in range(1, N + 1))


def main():
    P = primes_up_to(5000)
    odd = P[1:]
    assert len(P) == 669
    for t in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
        prod, sel = truncation(odd, t)
        assert prod > t  # all finite odd-prime products have odd denominators at t=1/2
        print('greedy_target', t, 'selected', len(sel),
              'last_selected', sel[-1], 'ratio_to_target', format(float(prod / t), '.12f'))
    for qs in ((), (2,), (3,), (3, 5), (3, 11), (3, 5, 7)):
        prod = Fraction(1)
        for p in qs:
            prod *= local_factor(p)
        assert prod != Fraction(1, 2)
        print('finite_Q', ','.join(map(str, qs)) or 'empty',
              'factor', str(prod), 'coefficient_factor', str(2 * prod - 1))
    # Exact finite experiment vs exact rational coefficient, with no attempted infinity certification.
    N = 30000
    s = sigma_up_to(N)
    for qs in ((), (2,), (3,), (3, 5), (3, 11)):
        prod = Fraction(1)
        for p in qs:
            prod *= local_factor(p)
        mean = signed_sum(s, N, qs) / (N * N)
        predicted = (pi ** 2 / 12) * (2 * float(prod) - 1)
        assert abs(mean - predicted) < 0.005, (qs, mean, predicted)
        print('finite_N', N, 'Q', ','.join(map(str, qs)) or 'empty',
              'measured', format(mean, '.9f'), 'predicted', format(predicted, '.9f'))
    # Prime-support monotonicity is the key estimate used in the tail proof.
    for n in range(1, 400):
        for q in (2, 3, 5, 7, 11):
            if q * n <= N:
                assert s[q * n] <= (q + 1) * s[n]
    print('VERIFY_OK; finite computations are not a proof of the infinite asymptotic.')


if __name__ == '__main__':
    main()
