#!/usr/bin/env python3
"""Exact finite subset-sum classification for factorial divisor sets.

Run with Python 3.9 or newer. The recurrence is entirely integer-based.
"""
from math import factorial, isqrt
from hashlib import sha256
from pathlib import Path
import re

EXPECTED_H = [1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 7, 8]
EXPECTED_MAX_LAYER = [1, 2, 2, 5, 9, 14, 343, 306, 1, 7150, 272934, 175]
EXPECTED_FIRST = [1, 1, 4, 17, 97, 659, 3733, 33473,
                  362783, 2979161, 29749079, 475785157]

def trial_divisors(N):
    return sorted({z for i in range(1, isqrt(N) + 1) if N % i == 0
                   for z in (i, N // i)})

def factor_divisors(N):
    """Second divisor generator, using prime powers rather than divisor pairs."""
    factors = []
    k = N
    p = 2
    while p * p <= k:
        if k % p == 0:
            e = 0
            while k % p == 0:
                k //= p
                e += 1
            factors.append((p, e))
        p += 1
    if k > 1:
        factors.append((k, 1))
    result = [1]
    for p, e in factors:
        previous = result[:]
        power = 1
        for _ in range(e):
            power *= p
            result.extend(v * power for v in previous)
    return sorted(result)

def exact_layers(N, divisors, max_terms):
    # Bit j of layers[t] is one iff j is a sum of exactly t distinct
    # divisors processed so far. Descending updates disallow reusing d.
    mask = (1 << (N + 1)) - 1
    layers = [1] + [0] * max_terms
    for d in divisors:
        for t in range(max_terms, 0, -1):
            layers[t] |= (layers[t-1] << d) & mask
    return layers, mask

def canonical_hard(N, layers, mask):
    covered = 1  # empty representation contributes zero only
    for k in range(1, len(layers)):
        previous = covered
        covered |= layers[k]
        if covered == mask:
            hard = mask & ~previous
            first = (hard & -hard).bit_length() - 1
            return (k, hard.bit_count(), first, hard)
    raise AssertionError('provided term cutoff too small')

def hard_list(bitset):
    # Scan a packed little-endian byte buffer once, rather than repeatedly
    # copying a 60 MB integer for each isolated high-position bit.
    data = bitset.to_bytes((bitset.bit_length() + 7) // 8, 'little')
    answer = []
    for match in re.finditer(rb'[\x01-\xff]', data):
        offset = 8 * match.start()
        value = data[match.start()]
        for k in range(8):
            if value & (1 << k):
                answer.append(offset + k)
    return answer

def main():
    table = []
    record = None
    for n in range(1, 13):
        N = factorial(n)
        ds = trial_divisors(N)
        assert ds == factor_divisors(N)
        assert all(N % d == 0 for d in ds)
        assert ds[0] == 1 and ds[-1] == N
        assert len(ds) == len(set(ds))
        layers, mask = exact_layers(N, ds, 8)
        h, count, first, misses = canonical_hard(N, layers, mask)
        assert (h, count, first) == (
            EXPECTED_H[n-1], EXPECTED_MAX_LAYER[n-1], EXPECTED_FIRST[n-1]
        ), (n, h, count, first)
        table.append((n, N, len(ds), h, count, first))
        if n == 12:
            record = (N, misses, ds, mask)

    N, misses, ds, mask = record
    hard = hard_list(misses)
    assert len(hard) == 175
    assert min(hard) == 475785157
    assert max(hard) == 479001547
    assert all(v % 2 == 1 and v % 3 and v % 5 for v in hard)
    assert sum(1 for v in hard if __import__('math').gcd(v,N)==7)==8

    # Permuted-order dynamic programming checks order independence without
    # incurring huge early bitsets from starting with the largest divisor.
    permuted = list(reversed(ds[:120])) + ds[120:]
    reverse_layers, reverse_mask = exact_layers(N, permuted, 8)
    reverse_h, reverse_count, reverse_first, reverse_misses = canonical_hard(
        N, reverse_layers, reverse_mask
    )
    assert (reverse_h, reverse_count, reverse_first) == (8,175,475785157)
    assert reverse_misses == misses
    assert reverse_mask == mask

    # Direct finite checks at low n, independent of the bitset transition.
    for n in range(1, 6):
        M = factorial(n)
        d = trial_divisors(M)
        exact = [set() for _ in range(len(d)+1)]
        exact[0] = {0}
        for divisor in d:
            for t in range(len(d),0,-1):
                exact[t].update(v+divisor for v in exact[t-1] if v+divisor<=M)
        best = next(k for k in range(1,len(d)+1)
                    if len(set().union(*exact[:k+1])) == M+1)
        assert best == EXPECTED_H[n-1]

    # The least eight-term witness has an explicit representation.
    witness_terms = [239500800,159667200,68428800,7983360,201600,3360,36,1]
    assert len(set(witness_terms)) == 8
    assert all(N % d == 0 for d in witness_terms)
    assert sum(witness_terms) == hard[0]

    content = ''.join(str(v)+'\n' for v in hard)
    digest = sha256(content.encode('ascii')).hexdigest()
    out = Path(__file__).with_name('eight_term_layer.txt')
    if out.exists():
        assert out.read_text('ascii') == content
    else:
        out.write_text(content,'ascii')
    for n, num, t, h, count, first in table:
        print('n=%02d N=%d divisors=%d h=%d hard_count=%d first_hard=%d'%(
            n,num,t,h,count,first))
    print('EIGHT_TERM_LAYER_SHA256='+digest)
    print('VERIFY_OK first_h_eight_n=12 hard_count=175 first_hard=475785157 '
          'last_hard=479001547 permuted_order=yes independent_small_cases=yes')

if __name__=='__main__':
    main()
