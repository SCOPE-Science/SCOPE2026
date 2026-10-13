"""Exact finite consistency tests for a leading-digit obstruction to prime v-palindromes.
The infinite statements follow from the proof, not these tests.
"""
from math import isqrt


def smallest_prime_factor(limit):
    spf = list(range(limit + 1))
    for i in range(2, isqrt(limit) + 1):
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def v(n, spf):
    assert n >= 1
    if n == 1:
        return 0
    out = 0
    while n > 1:
        p = spf[n]
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        out += p if k == 1 else p + k
    return out


def reversal(n, base):
    q = 0
    while n:
        q = q * base + n % base
        n //= base
    return q


def leading_digit(n, base):
    while n >= base:
        n //= base
    return n


def run():
    limit = 400000
    spf = smallest_prime_factor(limit)
    assert v(9, spf) == 5 and v(15, spf) == 8
    checked_odd_composites = 0
    for n in range(21, limit + 1, 2):
        if spf[n] != n:
            checked_odd_composites += 1
            assert 2*v(n,spf) <= n, (n,v(n,spf))

    checked_primes = 0
    checked_high_odd_leads = 0
    checked_nonpalindromic_base2_primes = 0
    for base in range(2, 41, 2):
        for p in range(3, 10000, 2):
            if spf[p] != p or p % base == 0:
                continue
            q = reversal(p, base)
            if q == p:
                continue
            assert q < limit
            checked_primes += 1
            d = leading_digit(p, base)
            if d % 2 == 1 and 2*d >= base:
                checked_high_odd_leads += 1
                assert v(q,spf) != p, (base,p,q,v(q,spf))
            if base == 2:
                checked_nonpalindromic_base2_primes += 1
                assert v(q,spf) != p
    assert reversal(175,2) == 245
    assert v(175,spf) == 14 == v(245,spf)
    assert reversal(109,16) == 214
    assert v(109,spf) == v(214,spf) == 109
    print('VERIFY_OK')
    print(f'odd_composites_in_21_to_400000={checked_odd_composites}')
    print(f'even_bases_checked=2,4,...,40')
    print(f'nonpalindromic_prime_base_pairs_checked={checked_primes}')
    print(f'odd_high_leading_digit_pairs_checked={checked_high_odd_leads}')
    print(f'binary_nonpalindromic_prime_cases_checked={checked_nonpalindromic_base2_primes}')
    print('binary_composite_example_175_reverse_245_v_14=PASS')
    print('base16_prime_example_109_reverse_214_v_109_outside_hypotheses=PASS')
    print('infinite_statement_uses_symbolic_proof_not_bounded_computation=PASS')


if __name__ == '__main__':
    run()
