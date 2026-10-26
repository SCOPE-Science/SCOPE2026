#!/usr/bin/env python3
"""Independent finite checks for block-palindrome widths on balanced binary words."""
from collections import Counter
from math import comb
from decimal import Decimal, getcontext


def dyck_words(n):
    def rec(s, opened, closed):
        if opened == n and closed == n:
            yield s
        if opened < n:
            yield from rec(s + '0', opened + 1, closed)
        if closed < opened:
            yield from rec(s + '1', opened, closed + 1)
    yield from rec('', 0, 0)


def is_dyck(s):
    h = 0
    for b in s:
        h += (1 if b == '0' else -1)
        if h < 0:
            return False
    return h == 0


def greedy_width(s):
    count = 0
    while s:
        border_length = None
        for k in range(1, len(s) // 2 + 1):
            if s[:k] == s[-k:]:
                border_length = k
                break
        if border_length is None:
            return count + 1
        b = s[:border_length]
        assert is_dyck(b)
        count += 2
        s = s[border_length:-border_length]
        assert is_dyck(s)
    return count


def coefficients(limit):
    catalan = [comb(2*n, n)//(n+1) for n in range(limit+1)]
    unbordered = [0]*(limit+1)
    for n in range(1, limit+1):
        unbordered[n] = catalan[n] - sum(
            unbordered[k]*catalan[n-2*k] for k in range(1, n//2+1))
        assert unbordered[n] >= 0
    # Coefficients of (1+tU(z))/(1-t^2 U(z^2)).
    poly = [Counter() for _ in range(limit+1)]
    poly[0][0] = 1
    for n in range(1, limit+1):
        poly[n][1] = unbordered[n]
        for k in range(1, n//2+1):
            for t,v in poly[n-2*k].items():
                poly[n][t+2] += unbordered[k]*v
        assert sum(poly[n].values()) == catalan[n]
    return catalan, unbordered, poly


def main():
    nmax = 12
    C,U,P = coefficients(80)
    total = 0
    for n in range(1, nmax+1):
        observed = Counter()
        for w in dyck_words(n):
            observed[greedy_width(w)] += 1
            total += 1
        assert observed == P[n], (n, observed, P[n])
        assert observed.get(1, 0) == U[n]
    expected = [1,1,4,11,36,112,378,1265,4360,15120,53236]
    assert U[1:12] == expected
    getcontext().prec = 45
    alpha = sum(Decimal(U[n])/(Decimal(16)**n) for n in range(1,81))
    # Since 0 <= U_n <= Catalan_n <= 4^n, all omitted terms are
    # bounded by (1/4)^81/(1-1/4).
    tail = (Decimal(1)/4)**81*Decimal(4)/3
    assert abs(alpha-Decimal('0.067593450955121331489218327150')) < Decimal('1e-29')
    print('DYCK_BP_PASS', 'tested_words=', total, 'semilengths=1..12',
          'exact_coefficient_semilengths=0..80', 'alpha_tail_bound=', tail)

if __name__ == '__main__':
    main()
