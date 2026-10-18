"""Reproducible finite corroboration of the first gap in binary 2-deck arch spectra.

This program is independent of the proof's partition count for its principal
exhaustive test: it builds every word and explicitly checks all short binary
subsequences. No external dependencies are needed.
"""
from itertools import product, combinations
from collections import defaultdict


def parameters(word):
    a = 0
    c = 0
    for symbol in word:
        if symbol == 'a':
            a += 1
        else:
            c += a
    return (a, len(word)-a, c)


def is_subsequence(pattern, word):
    iterator = iter(word)
    return all(any(letter == symbol for letter in iterator) for symbol in pattern)


def index_direct(word):
    result = 0
    for k in range(1, len(word)//2 + 1):
        if all(is_subsequence(p, word) for p in product('ab', repeat=k)):
            result = k
        else:
            break
    return result


def index_arch(word):
    arches = 0
    pending = None
    for x in word:
        if pending is None:
            pending = x
        elif x != pending:
            arches += 1
            pending = None
    return arches


def partition_words(A, B, C):
    out = []
    for lam in combinations(range(A+B), A):
        # Auxiliary independent enumeration by a constrained path.
        w = ''.join('a' if j in lam else 'b' for j in range(A+B))
        if parameters(w) == (A,B,C):
            out.append(w)
    return out


def partition_count(A,B,C):
    # Count partitions inside A x B of area C with a simple recurrence.
    # Fix row lengths from largest to smallest.
    def count_rows(rows, maxpart, area):
        if rows == 0:
            return int(area == 0)
        return sum(count_rows(rows - 1, j, area - j)
                   for j in range(min(maxpart, area) + 1))
    return count_rows(A,B,C)


def main():
    group = defaultdict(list)
    word_count = 0
    for n in range(0,9):
        for chars in product('ab', repeat=n):
            w = ''.join(chars)
            word_count += 1
            a = index_direct(w)
            b = index_arch(w)
            assert a == b, (w,a,b)
            group[(n,)+parameters(w)].append((w,a))

    gaps = []
    for key, members in group.items():
        spectrum = {i for _,i in members}
        if spectrum != set(range(min(spectrum),max(spectrum)+1)):
            gaps.append((key,tuple(sorted(spectrum))))
    assert gaps == [((8,4,4,8),(2,4))], gaps
    assert word_count == 511
    exceptional = sorted(group[(8,4,4,8)])
    assert len(exceptional) == partition_count(4,4,8) == 8
    assert len([w for w, i in exceptional if i==2]) == 2
    assert len([w for w, i in exceptional if i==4]) == 6
    assert {w for w,i in exceptional if i==2} == {'aabbbbaa','bbaaaabb'}

    expected_three = {6:'abbabbaa',7:'ababbbaa',9:'aabbbaba',10:'aabbabba'}
    for c,word in expected_three.items():
        assert parameters(word) == (4,4,c)
        assert index_arch(word) == index_direct(word) == 3
        assert any(i==4 for _,i in group[(8,4,4,c)])

    assert sorted(partition_words(4,4,8)) == sorted(w for w,_ in exceptional)
    print('ALL CHECKS PASS')
    print('Lengths 0..8: %d words; %d distinct (length,A,B,C) classes' % (word_count,len(group)))
    print('Noninterval classes through length 8:',gaps)
    print('Exceptional fiber size:',len(exceptional),'(partition count verified independently)')
    for word,idx in exceptional:
        print(word, 'index',idx)
    print('Index-three witnesses at C=6,7,9,10:',expected_three)
    print('Direct all-pattern subsequence test agrees with greedy arches on every word.')

if __name__ == '__main__':
    main()
