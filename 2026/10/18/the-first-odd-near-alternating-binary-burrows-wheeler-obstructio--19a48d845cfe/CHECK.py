"""Reproduce the exact 49-symbol binary BWT run extremum.

Uses only Python's standard library. Run: python3 CHECK.py
"""
from itertools import combinations
from collections import Counter


def word_from_equalities(length, equal_positions):
    eq = set(equal_positions)
    w = ['1']
    for i in range(length - 1):
        w.append(w[-1] if i in eq else ('0' if w[-1] == '1' else '1'))
    return ''.join(w)


def lf_map(word):
    zeros = word.count('0')
    z = one = 0
    output = []
    for a in word:
        if a == '0':
            output.append(z)
            z += 1
        else:
            output.append(zeros + one)
            one += 1
    return output


def lf_independent(word):
    indices = sorted(range(len(word)), key=lambda i: (word[i], i))
    out = [None] * len(word)
    for rank, source_index in enumerate(indices):
        out[source_index] = rank
    return out


def orbit_length(mapping):
    a = 0
    for step in range(1, len(mapping) + 1):
        a = mapping[a]
        if a == 0:
            return step
    raise AssertionError('Not a permutation cycle at index 0')


def direct_bwt(source):
    n = len(source)
    rotations = [source[i:] + source[:i] for i in range(n)]
    return ''.join(row[-1] for row in sorted(rotations))


def inverse_from_lf(word, mapping):
    p = 0
    backward = []
    for _ in word:
        backward.append(word[p])
        p = mapping[p]
    assert p == 0
    return ''.join(backward[::-1])


def run_count(word):
    return 1 + sum(a != b for a, b in zip(word, word[1:]))


def main():
    witnesses = {}
    onebreak_counts = {}
    for n in range(3, 50, 2):
        valid = []
        for j in range(n - 1):
            w = word_from_equalities(n, (j,))
            pi = lf_map(w)
            assert pi == lf_independent(w)
            if orbit_length(pi) == n:
                assert w[0] == '1' and w[-1] == '0'
                assert run_count(w) == n - 1
                assert direct_bwt(inverse_from_lf(w, pi)) == w
                valid.append(j)
        onebreak_counts[n] = len(valid)
        if n < 49:
            assert valid, ('missing high-run witness', n)
            witnesses[n] = valid[0]
        else:
            assert not valid, ('unexpected 48-run word at n=49', valid)
    print('ONE_BREAK_COUNTS', ' '.join(f'{n}:{onebreak_counts[n]}' for n in sorted(onebreak_counts)))
    print('SMALLEST_ONE_BREAK_WITNESSES', ' '.join(f'{n}:{witnesses[n]}' for n in witnesses))

    n = 49
    orbit_table = [orbit_length(lf_map(word_from_equalities(n, (j,))))
                   for j in range(n - 1)]
    assert all(t < n for t in orbit_table)
    print('LENGTH49_SINGLE_EQUALITY_ORBIT_LENGTHS', ' '.join(map(str, orbit_table)))

    tested = accepted = 0
    min_breaks = Counter()
    exemplar = None
    all_witnesses = set()
    for triple in combinations(range(n-1), 3):
        tested += 1
        w = word_from_equalities(n, triple)
        assert w[0] == '1' and w[-1] == '0' and run_count(w) == 46
        pi = lf_map(w)
        assert pi == lf_independent(w)
        if orbit_length(pi) != n:
            continue
        recovered = inverse_from_lf(w, pi)
        assert direct_bwt(recovered) == w
        assert w not in all_witnesses
        all_witnesses.add(w)
        accepted += 1
        min_breaks[triple[0]] += 1
        if exemplar is None:
            exemplar = (triple, w, recovered)
    assert tested == 17296, tested
    assert accepted == 1128, accepted
    assert exemplar[0] == (0, 1, 8), exemplar
    print('THREE_EQUALITY_CANDIDATES', tested)
    print('LENGTH49_PRIMITIVE_BWT_OUTPUTS_WITH_46_RUNS', accepted)
    print('COUNTS_BY_FIRST_EQUALITY_INDEX', ' '.join(f'{k}:{min_breaks[k]}' for k in sorted(min_breaks)))
    print('EXPLICIT_EQUALITIES', exemplar[0])
    print('EXPLICIT_BWT', exemplar[1])
    print('EXPLICIT_NECKLACE_REPRESENTATIVE', exemplar[2])
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    main()
