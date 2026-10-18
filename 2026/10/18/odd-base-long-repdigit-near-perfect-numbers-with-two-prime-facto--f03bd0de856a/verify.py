"""Finite, independent checks for the odd-base repdigit theorem.

Uses only the Python standard library; the published infinite classification
and the mathematical proof, not finite enumeration, establish the theorem.
"""
from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            return n == p
    return True


def repdigit_length(n, base):
    if n <= 0:
        return 0
    first = n % base
    if first == 0:
        return 0
    count = 0
    while n:
        d = n % base
        if d != first:
            return 0
        n //= base
        count += 1
    return count


def nearperfect_two_prime_family():
    numbers = {40}
    mersennes = [(p, 2**p - 1) for p in range(2, 18)
                 if is_prime(p) and is_prime(2**p - 1)]
    for p, q in mersennes:
        numbers.add(2**(p-1) * q*q)
        numbers.add(2**(2*p-1) * q)
    for t in range(2, 18):
        for k in range(1, t):
            q = 2**t - 2**k - 1
            if is_prime(q):
                numbers.add(2**(t-1) * q)
    return numbers


def brute_divisors(n):
    out = []
    for d in range(1, isqrt(n)+1):
        if n % d == 0:
            out.append(d)
            if d*d != n:
                out.append(n//d)
    return out


def verify():
    candidates = nearperfect_two_prime_family()
    comparisons = 0
    witnesses = []
    for n in sorted(candidates):
        for b in range(3, 152, 2):
            comparisons += 1
            if repdigit_length(n, b) >= 3:
                witnesses.append((n, b, repdigit_length(n, b)))
    assert witnesses == [(40, 3, 4)], witnesses

    # Independent direct divisor-sum and support-count census in a small range.
    direct_nearperfect = []
    for n in range(2, 10001):
        ds = brute_divisors(n)
        total = sum(ds)
        if total-2*n not in ds or total-2*n == n:
            continue
        distinct = 0
        temp = n
        for p in range(2,isqrt(temp)+1):
            if temp % p == 0:
                distinct += 1
                while temp%p==0:
                    temp//=p
        if temp>1:
            distinct += 1
        if distinct == 2:
            direct_nearperfect.append(n)
    assert set(direct_nearperfect) == {n for n in candidates if n <= 10000}, (
        sorted(set(direct_nearperfect)^set(n for n in candidates if n<=10000)))
    repdigits = []
    for n in direct_nearperfect:
        for b in range(3, 152, 2):
            if repdigit_length(n,b) >=3:
                repdigits.append((n,b,repdigit_length(n,b)))
    assert repdigits == [(40,3,4)], repdigits
    assert sum(brute_divisors(40)) == 2*40+10
    print('VERIFY_OK')
    print('classified candidates',len(candidates),'base comparisons',comparisons)
    print('direct two-prime near-perfect numbers <=10000',len(direct_nearperfect))
    print('only qualifying (number, base, length):',witnesses)

if __name__ == '__main__':
    verify()
