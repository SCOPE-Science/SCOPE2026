#!/usr/bin/env python3
"""Independent finite checks for the Stewart-factor symmetry theorem."""
from itertools import product

PATTERNS = ('01?', '10?', '0?1', '1?0', '?01', '?10')
COMPLEMENT = str.maketrans('01', '10')

def comp(w):
    return w.translate(COMPLEMENT)

def theta(w):
    return comp(w[::-1])

def toeplitz_prefix(patterns, length, exceptional='0'):
    ans = []
    for i in range(length):
        index = i
        val = '?'
        for pattern in patterns:
            val = pattern[index % 3]
            if val != '?':
                break
            index //= 3
        ans.append(exceptional if val == '?' else val)
    return ''.join(ans)

def factor_set(word, n):
    return {word[i:i+n] for i in range(len(word)-n+1)}

def local_length_eight(first):
    assert first in PATTERNS
    pair_set = {''.join(v) for v in product('01', repeat=2)}
    triple_set = {''.join(v) for v in product('01', repeat=3) if len(set(v)) == 2}
    out = set()
    for offset in range(3):
        template = [first[(offset+j)%3] for j in range(8)]
        m = template.count('?')
        for letters in (pair_set if m == 2 else triple_set):
            it = iter(letters)
            out.add(''.join(next(it) if a == '?' else a for a in template))
    return out

def overlap_counts(S, n):
    words = {x[:n] for x in S}
    return (len(words), sum(comp(w) in words for w in words),
            sum(w[::-1] in words for w in words),
            all(theta(w) in words for w in words))

def test_skeleton_reflection():
    check_count = 0
    for depth in range(1, 5):
        for pats in product(PATTERNS, repeat=depth):
            modulus = 3 ** depth
            hole = sum(p.index('?') * 3**j for j, p in enumerate(pats))
            arr = ['?'] * modulus
            for i in range(modulus):
                q = i
                for p in pats:
                    a = p[q % 3]
                    if a != '?':
                        arr[i] = a
                        break
                    q //= 3
            for i, a in enumerate(arr):
                j = (2*hole - i) % modulus
                b = arr[j]
                assert (a == '?' and b == '?') or (a in '01' and b == comp(a))
                check_count += 1
    return check_count

def main():
    all_sets = [local_length_eight(p) for p in PATTERNS]
    assert all(len(s) == 16 for s in all_sets)
    assert len({frozenset(s) for s in all_sets}) == 2
    assert all_sets[0] == all_sets[3] == all_sets[4]
    assert all_sets[1] == all_sets[2] == all_sets[5] == {comp(s) for s in all_sets[0]}
    expected = [2, 4, 6, 6, 6, 6, 2, 0]
    for local in all_sets:
        for n in range(1, 9):
            count, c, rev, symmetric = overlap_counts(local, n)
            assert count == 2*n and c == rev == expected[n-1] and symmetric

    checked_directives = 0
    for p in PATTERNS:
        for tail in product(PATTERNS, repeat=3):
            patterns = (p,) + tail + ('01?',)*5
            direct = toeplitz_prefix(patterns, 2000)
            assert factor_set(direct, 8) == local_length_eight(p)
            checked_directives += 1
    skeleton_pairs = test_skeleton_reflection()

    tests = (
        ('01?',)*12,
        ('?01', '10?', '0?1', '01?', '1?0', '?10')*2,
        ('1?0', '01?', '?10', '0?1', '?01', '10?')*2,
    )
    for patterns in tests:
        direct = toeplitz_prefix(patterns, 25000)
        for n in range(1, 101):
            S = factor_set(direct, n)
            assert len(S) == 2*n
            assert all(theta(w) in S for w in S)
            if n >= 8:
                assert all(comp(w) not in S and w[::-1] not in S for w in S)
    print('STEWART_SYMMETRY_PASS',
          'eight_factor_sets=2',
          'overlap=2,4,6,6,6,6,2,0',
          f'directive_prefixes={checked_directives}',
          f'skeleton_reflection_positions={skeleton_pairs}',
          'long_factor_lengths=1..100')

if __name__ == '__main__':
    main()
