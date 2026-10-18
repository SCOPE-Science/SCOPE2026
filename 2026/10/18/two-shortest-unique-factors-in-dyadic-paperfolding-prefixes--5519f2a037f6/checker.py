"""Finite certificates for regular paperfolding shortest unique factors.
Run: python checker.py. Uses Python 3 standard library only.
"""
from collections import defaultdict, Counter
from itertools import product


def bit(n):
    assert n >= 1
    return '1' if (n // (n & -n)) % 4 == 3 else '0'


def nine_templates():
    # The only variable letters in an interval of nine consecutive indices
    # are the indices divisible by eight. All other letters depend solely
    # on the parity of the block index.
    by_residue = defaultdict(set)
    for r in range(1, 9):
        for parity in range(2):
            t = 100 + parity
            start = 8 * t + r
            word = [bit(j) for j in range(start, start + 9)]
            unknowns = [j for j in range(9) if (start+j) % 8 == 0]
            for choices in product('01', repeat=len(unknowns)):
                copy = word.copy()
                for j, v in zip(unknowns, choices):
                    copy[j] = v
                by_residue[r].add(''.join(copy))
    sizes = [len(by_residue[r]) for r in range(1, 9)]
    assert sizes == [4, 4, 4, 4, 4, 4, 4, 8]
    for r in range(1, 9):
        for s in range(r+1, 9):
            assert by_residue[r].isdisjoint(by_residue[s]), (r, s)
    assert len(set().union(*by_residue.values())) == 36
    print('nine-symbol residue certificate: 36 distinct templates; groups 4,4,4,4,4,4,4,8; all disjoint')


def endpoint_classes():
    prefix = ''.join(bit(i) for i in range(1, 17))
    assert prefix == '0010011000110110'
    groups = defaultdict(list)
    for t in range(1, 16):
        groups[(t % 2, prefix[t-1], prefix[t])].append(t)
    singleton = sorted(T[0] for T in groups.values() if len(T) == 1)
    assert singleton == [11, 12]
    assert sorted(map(len, groups.values())) == [1,1,2,2,2,2,2,3]
    print('endpoint classes:', sorted(groups.items()))


def check_prefix(k):
    q = 2**(k-4)
    word = ''.join(bit(i) for i in range(1, 2**k+1))
    counts_short = Counter(word[i:i+q] for i in range(len(word)-q+1))
    assert min(counts_short.values()) >= 2
    long_factors = [word[i:i+q+1] for i in range(len(word)-q)]
    counts_long = Counter(long_factors)
    starts = [i + 1 for i, w in enumerate(long_factors) if counts_long[w] == 1]
    assert starts == [11*q, 12*q], (k,starts)
    print('n=%d, length=%d, min_unique_length=%d, unique_one_based_starts=%s' % (k, 2**k, q+1, starts))

if __name__ == '__main__':
    nine_templates()
    endpoint_classes()
    for n in range(6, 13):
        check_prefix(n)
    print('All finite checks passed. Infinite statement follows from paper proof, not the finite prefix tests.')
