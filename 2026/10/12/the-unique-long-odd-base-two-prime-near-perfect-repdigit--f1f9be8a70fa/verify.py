"""Exact finite certificate for odd-base repdigit near-perfect numbers."""
from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def candidates():
    result = []
    for e in range(1, 10):
        p = e + 1
        if is_prime(p) and is_prime((1 << p) - 1):
            q = (1 << p) - 1
            result.append(("A", e, 0, (1 << e) * q * q))
        if (e + 1) % 2 == 0:
            p = (e + 1) // 2
            if is_prime(p) and is_prime((1 << p) - 1):
                q = (1 << p) - 1
                result.append(("B", e, 0, (1 << e) * q))
        t = e + 1
        for k in range(1, t):
            q = (1 << t) - (1 << k) - 1
            if is_prime(q):
                result.append(("C", e, k, (1 << e) * q))
    result.append(("exception", 3, 0, 40))
    return result


def v2(n):
    assert n > 0
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


if __name__ == '__main__':
    assert 3**19 > 2**17 * 20**3
    assert 3 * 20**3 > 21**3
    C = candidates()
    assert len(C) == 31
    assert len({x[3] for x in C}) == 31
    for family, e, k, N in C:
        assert N % (1 << e) == 0
        qpow = N // (1 << e)
        if family == "A":
            q = isqrt(qpow)
            assert q*q == qpow and is_prime(q)
            sigma_q = 1 + q + q*q
            redundant = q
        else:
            q = qpow
            assert is_prime(q) and q % 2 == 1
            sigma_q = 1 + q
            if family == "B":
                redundant = (1 << ((e + 1) // 2)) * q
            elif family == "C":
                redundant = 1 << k
            else:
                redundant = 10
        assert ((1 << (e+1)) - 1)*sigma_q == 2*N + redundant
        assert 0 < redundant < N and N % redundant == 0
    matches = []
    for g in (3, 5, 7, 9):
        for ell in range(3, 20):
            U = (g**ell - 1) // (g - 1)
            for family, e, k, N in C:
                a, remainder = divmod(N, U)
                if remainder == 0 and 1 <= a < g:
                    matches.append((g, ell, a, N, family, e, k))
                    assert v2(N) == e
                    assert N == a * sum(g**j for j in range(ell))
    assert matches == [(3, 4, 1, 40, 'exception', 3, 0)]
    assert 40 == 2**3 * 5
    sigma_40 = (1 + 2 + 4 + 8) * (1 + 5)
    assert sigma_40 == 2 * 40 + 10
    assert 40 % 10 == 0 and 0 < 10 < 40
    print('VERIFY_OK bases=3,5,7,9 lengths=3..19 exponent_bound=9')
    print('candidate_count=31 candidate_distinct=31')
    print('matched=(g=3,length=4,digit=1,N=40)')
    print('sigma(40)=90 redundant_divisor=10')
