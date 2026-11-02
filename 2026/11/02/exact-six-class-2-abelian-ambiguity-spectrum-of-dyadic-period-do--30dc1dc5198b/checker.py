#!/usr/bin/env python3
"""Reproduce dyadic 2-Abelian class-size spectra of the period-doubling word.

Requires only Python 3 standard library. Checks direct contiguous factors from
explicit substitution iterates, not just the proof's abstract recurrences.
"""
from collections import Counter, defaultdict


def substitute(word):
    return ''.join('01' if c == '0' else '00' for c in word)


def signature(word):
    return (word.count('0'), word.count('1'),
            *(sum(word[i:i+2] == pair for i in range(len(word)-1))
              for pair in ('00','01','10','11')))


def expected_spectrum(k):
    assert k >= 3
    n = 1 << k
    a, b = n // 12, n // 6
    if k & 1:
        return sorted((2*a+1, 2*a+1, 2*a+2, 2*b, 2*b+1, 2*b+1))
    return sorted((2*a, 2*a+1, 2*a+1, 2*b+1, 2*b+1, 2*b+2))


def classes(factors):
    d = defaultdict(set)
    for word in factors:
        d[signature(word)].add(word)
    return sorted(map(len,d.values()))


def dyadic_factor_sets(maxk):
    factors = {'00', '01', '10'}
    yield 1, factors
    for k in range(2, maxk+1):
        new = set()
        for u in factors:
            E = ''.join('0' + str(1-int(c)) for c in u)
            O = ''.join(str(1-int(c)) + '0' for c in u)
            assert E != O
            new.add(E)
            new.add(O)
        factors = new
        yield k, factors


def main():
    # The direct finite prefix is generated separately from factor recurrence.
    prefix = '0'
    for _ in range(15):
        prefix = substitute(prefix)
    for k, factors in dyadic_factor_sets(10):
        n = 1 << k
        direct = {prefix[i:i+n] for i in range(len(prefix)-n+1)}
        assert factors == direct, ('direct-factor mismatch', k, len(factors),len(direct))
        assert len(factors) == 3*(1 << (k-1)), ('factor total',k)
        if k >= 3:
            got = classes(direct)
            want = expected_spectrum(k)
            assert got == want, ('2-Abelian spectrum',k,got,want)
            assert sum(got) == len(factors)
            print(f'k={k}, n={n}, factors={len(factors)}, fibers={got}: OK')
    # Test that 2-Abelian criterion derived from E/O types is exact on all factors.
    for k, factors in dyadic_factor_sets(9):
        if k <= 2:
            continue
        m = 1 << (k-1)
        prev = next(f for j,f in dyadic_factor_sets(k-1) if j == k-1)
        groups = defaultdict(list)
        for word in factors:
            groups[signature(word)].append(word)
        for z in sorted({u.count('0') for u in prev}):
            aa = sum(u[0]=='0' and u[-1]=='0' and u.count('0')==z for u in prev)
            bb = sum(u[0]=='0' and u[-1]=='1' and u.count('0')==z for u in prev)
            cc = sum(u[0]=='1' and u[-1]=='0' and u.count('0')==z for u in prev)
            assert bb == cc
            expected = sorted((aa+bb,aa+bb,2*bb))
            actual = sorted(len(words) for sig, words in groups.items()
                            if sig[1] == z)
            assert expected == actual,(k,z,expected,actual)
    print('ALL_DIRECT_AND_RECURSIVE_CHECKS_PASSED')

if __name__ == '__main__':
    main()
