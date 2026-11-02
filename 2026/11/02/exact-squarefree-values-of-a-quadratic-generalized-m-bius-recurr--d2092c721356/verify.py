"""Exact integer checks for the quadratic generalized Mobius recurrence.

The finite checks accompany, but do not replace, the unrestricted proof.
"""
from math import comb, isqrt


def arithmetic_spf(bound):
    spf = list(range(bound + 1))
    for p in range(2, isqrt(bound) + 1):
        if spf[p] == p:
            for n in range(p * p, bound + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def factor_info(n, spf):
    primes, squarefree = [], True
    while n > 1:
        p = spf[n]
        primes.append(p)
        n //= p
        if n % p == 0:
            squarefree = False
            while n % p == 0:
                n //= p
    return primes, squarefree


def moments(kmax):
    m = [1]
    for j in range(1, kmax + 1):
        m.append(-2 * sum((-1) ** r * comb(j, r) * m[j-r]
                          for r in range(1, j + 1)))
    return m


def squarefree_formula(primes, moment):
    k = len(primes)
    total = 0
    for mask in range((1 << k) - 1):
        product = 1
        count = 0
        for i, p in enumerate(primes):
            if mask & (1 << i):
                count += 1
                product *= p - 1
        total += moment[count] * product
    return (-1) ** k * total


def verify(nmax=10000, direct_max=900):
    # Recurrence obtained by finite differences; no floating arithmetic.
    a = [0] * (nmax + 1)
    a[1] = 1
    for n in range(2, nmax + 1):
        value = -1
        for d in range(2, isqrt(n) + 1):
            if n % d:
                continue
            e = n // d
            value -= a[d] * (2*e-1)
            if d != e:
                value -= a[e] * (2*d-1)
        a[n] = value

    # Independent computation using the original floor recurrence.
    direct = [0] * (direct_max + 1)
    direct[1] = 1
    for n in range(2, direct_max + 1):
        direct[n] = 1-n-sum(direct[d] * (n//d)**2 for d in range(2, n))
        assert a[n] == direct[n], ("floor/divisor", n, a[n], direct[n])

    spf = arithmetic_spf(nmax)
    max_distinct = 1
    for n in range(2, nmax + 1):
        p, sqfree = factor_info(n, spf)
        max_distinct = max(max_distinct, len(p))
    m = moments(max_distinct)
    assert m[:5] == [1, 2, 6, 26, 150]

    sfree = non_sfree = primes_checked = 0
    for n in range(2, nmax+1):
        p, sf = factor_info(n, spf)
        expected_parity = 1 if sf else 0
        assert a[n] % 2 == expected_parity, ("parity", n)
        assert (a[n] == -1) == (len(p) == 1 and sf), ("prime iff -1", n)
        if sf:
            sfree += 1
            exact = squarefree_formula(p, m)
            assert a[n] == exact, ("closed formula", n, a[n], exact)
            if len(p) == 1:
                primes_checked += 1
            else:
                assert abs(a[n]) > 1
        else:
            non_sfree += 1

    assert a[4] == 2 and a[6] == 7 and a[8] == 0
    assert a[9] == 4 and a[12] == -14 and a[30] == -99
    print("VERIFY_OK", f"n_max={nmax}", f"original_recurrence={direct_max}",
          f"squarefree_exact={sfree}", f"nonsquarefree_parity={non_sfree}",
          f"primes={primes_checked}", f"moment_values={m}",
          "arithmetic=exact")


if __name__ == '__main__':
    verify()
