"""Independent finite sanity checks for the Pascal-row p-adic closure theorem.

These tests do not replace the proof for infinitely many indices or primes.
"""
from math import comb


def row_integer(p, n):
    return sum((comb(n, i) % p) * p**i for i in range(n + 1))


def pvaluation(n, p):
    if n == 0:
        return None
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def row_digit(p, n, i):
    ans = 1
    while i:
        a, b = n % p, i % p
        ans = ans * comb(a, b) % p if a >= b else 0
        n //= p
        i //= p
    return ans


def check():
    pair_checks = digit_checks = residue_checks = 0
    for p in (2, 3, 5, 7):
        values = [row_integer(p, n) for n in range(81)]
        for m in range(81):
            for n in range(m):
                observed = pvaluation(values[m] - values[n], p)
                expected = p ** pvaluation(m - n, p)
                assert observed == expected, (p, m, n, observed, expected)
                pair_checks += 1
        for n in range(70):
            for i in range(35):
                assert row_digit(p, n, i) == (values[n] // p**i) % p
                digit_checks += 1
    for p in (2, 3, 5):
        for N in range(1, 15):
            J = 0
            while p**J < N:
                J += 1
            residues = set()
            for n in range(p**J):
                residue = sum(row_digit(p, n, i)*p**i for i in range(N))
                residues.add(residue)
                for j in range(J):
                    assert (residue // p**(p**j)) % p == (n//p**j)%p
            assert len(residues) == p**J, (p, N, len(residues), p**J)
            residue_checks += 1
    return pair_checks, digit_checks, residue_checks


if __name__ == '__main__':
    a,b,c=check()
    print(f'PASS: {a} exact valuation checks; {b} Lucas-digit checks; {c} occupied-residue-count checks.')
    print('Scope: finite sanity checks only; infinite classification follows from Lucas theorem.')
