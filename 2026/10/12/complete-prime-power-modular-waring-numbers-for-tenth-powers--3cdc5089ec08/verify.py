#!/usr/bin/env python3
"""Exact finite verification of modular tenth-power Waring number exceptional primes.
Run: python3 verify.py. Standard library only; no network access.
Infinite-prime coverage is supplied by the mathematical argument in RESULT.md,
not by this finite regression.
"""
import csv
import io
from pathlib import Path

LIMIT = 6000
EXCEPTION_GAMMA_P = {
    11: 10, 31: 5, 41: 4, 61: 4,
    71: 3, 101: 3, 131: 3, 151: 3, 181: 3,
    191: 3, 211: 3, 241: 3, 251: 3, 271: 3, 281: 3,
    311: 3, 331: 3, 401: 3, 421: 3, 431: 3, 461: 3,
    491: 3, 641: 3, 911: 3,
}
EXCEPTION_GAMMA_P2 = {
    11: 11, 31: 5, 41: 4, 61: 4, 71: 4, 131: 4,
    311: 4, 431: 4, 491: 4, 911: 4,
    101: 3, 181: 3, 241: 3, 281: 3,
    401: 3, 421: 3, 461: 3, 641: 3,
}

def primes_below(n):
    a = bytearray(b'\x01') * n
    a[:2] = b'\x00\x00'
    for i in range(2, int(n**0.5) + 1):
        if a[i]:
            a[i * i:n:i] = b'\x00' * len(a[i * i:n:i])
    return [i for i in range(n) if a[i]]

def shift(mask, delta, n, full):
    if delta == 0: return mask
    return ((mask << delta) | (mask >> (n - delta))) & full

def gamma_mod(n, exponent=10):
    """Exact minimal positive t for all residues as sums of <=t powers."""
    vals = {pow(x, exponent, n) for x in range(n)}
    full = (1 << n) - 1
    cur = 1
    for t in range(1, n + 1):
        nxt = 0
        for v in vals: nxt |= shift(cur, v, n, full)
        cur = nxt
        if cur == full:return t
    raise AssertionError(f'no cover modulo {n}')

def gamma_and_nontrivial_zero_mod_p(p):
    """Exact modular prime basis size and minimum nontrivial zero length."""
    H = sorted({pow(x, 10, p) for x in range(1, p)})
    full = (1 << p) - 1
    covered = 1  # empty sum 0
    exact_positive = 0  # all summands nonzero mod p
    gamma = min_zero = None
    for t in range(1, 15):
        updated = covered
        for h in H:updated |= shift(covered, h, p, full)
        covered = updated
        if t == 1:
            exact_positive = sum(1 << h for h in H)
        else:
            updated = 0
            for h in H:updated |= shift(exact_positive, h, p, full)
            exact_positive = updated
        if gamma is None and covered == full: gamma = t
        if min_zero is None and exact_positive & 1:min_zero=t
        if gamma is not None and min_zero is not None:return gamma, max(gamma,min_zero), min_zero
    raise AssertionError(f'insufficient steps for p={p}')

def certificate():
    lines = ['prime,gamma_at_prime,gamma_at_higher_powers,minimal_nontrivial_zero_length']
    cnt = 0
    for p in primes_below(LIMIT):
        if p in (2,5):continue
        g,star,z = gamma_and_nontrivial_zero_mod_p(p)
        g_expected=EXCEPTION_GAMMA_P.get(p,2)
        star_expected=EXCEPTION_GAMMA_P2.get(p,2 if p % 4 == 1 else 3)
        assert (g,star)==(g_expected,star_expected), (p,g,star,g_expected,star_expected)
        if p in EXCEPTION_GAMMA_P or p in EXCEPTION_GAMMA_P2:
            lines.append(f'{p},{g},{star},{z}')
        cnt += 1
    assert cnt==781 and len(lines)==25,(cnt,len(lines))
    assert set(EXCEPTION_GAMMA_P2) | set(EXCEPTION_GAMMA_P) == set(int(row.split(',')[0]) for row in lines[1:])
    return '\n'.join(lines) + '\n',cnt

if __name__ == '__main__':
    data,cnt=certificate()
    path=Path(__file__).with_name('prime_exceptions.csv')
    assert path.read_text(encoding='utf8') == data, 'exception table differs from exact recomputation'
    for a,expected in [(1,1),(2,3),(3,7),(4,8),(5,8),(6,8),(7,8),(8,8),(9,8),(10,8)]:
        assert gamma_mod(2**a)==expected, ('2',a)
    for a,expected in [(1,2),(2,12),(3,12),(4,12),(5,12)]:
        assert gamma_mod(5**a)==expected, ('5',a)
    for p in (3,7,11,13,17,19,23,31,41,61,71):
        expected=EXCEPTION_GAMMA_P2.get(p,2 if p%4==1 else 3)
        assert gamma_mod(p*p)==expected,('p2',p,expected)
    # For all p >= 6000, Fermat degree 10 genus 36 has more than
    # 30 non-affine/non-unit points to spare in the Hasse--Weil estimate:
    # sqrt(p) > 77 => p-29-72 sqrt(p) > 5p/77-29 > 0.
    assert 77*77 < LIMIT and 5*LIMIT > 29*77
    print('VERIFY_OK')
    print(f'exhaustive_odd_primes_below_6000_excluding_5={cnt}')
    print(f'exceptional_prime_rows={len(data.splitlines())-1}')
    print('power_of_two_exponents=1..10')
    print('power_of_five_exponents=1..5')
    print('direct_odd_prime_square_checks=11')
    print('genus_36_hasse_weil_6000_cutoff_inequality=PASS')
    print('all_modular_checks_exact_integer_bitsets=PASS')
