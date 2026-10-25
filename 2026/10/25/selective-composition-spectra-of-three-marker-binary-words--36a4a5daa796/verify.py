"""Exact finite checks for a selective substring-composition reconstruction theorem.
All counts are computed from literal contiguous substrings; no external modules.
"""
from collections import defaultdict
from itertools import combinations, product


def observed(word, one_counts):
    """Multiplicity vector of zero counts, grouped by selected one counts."""
    selected = set(one_counts)
    count = defaultdict(int)
    for left in range(len(word)):
        zeros = ones = 0
        for right in range(left, len(word)):
            if word[right] == '0':
                zeros += 1
            else:
                ones += 1
            if ones in selected:
                count[(ones, zeros)] += 1
    return tuple(sorted(count.items()))


def canonical(word):
    return min(word, word[::-1])


def gaps(word):
    parts = word.split('1')
    assert len(parts) == 4 and all(set(p) <= {'0'} for p in parts)
    return tuple(map(len, parts))


def representative(a, b, c, d):
    return '0'*a + '1' + '0'*b + '1' + '0'*c + '1' + '0'*d


def expected_ambiguity(g):
    a, b, c, d = g
    return 1 + int(a != d and b != c)


def check():
    checked_words = 0
    for n in range(3, 25):
        by_sparse = defaultdict(set)
        by_plus_one = defaultdict(set)
        first = {}
        for idx in combinations(range(n), 3):
            bitset = set(idx)
            w = ''.join('1' if i in bitset else '0' for i in range(n))
            sparse = observed(w, (0,3))
            enriched = observed(w, (0,1,3))
            by_sparse[sparse].add(canonical(w))
            by_plus_one[enriched].add(canonical(w))
            first.setdefault(sparse,w)
            checked_words += 1
        assert all(len(cls) == 1 for cls in by_plus_one.values()), n
        for signature, classes in by_sparse.items():
            assert len(classes) == expected_ambiguity(gaps(first[signature])), (n, classes)
    # Independently check all three generating-polynomial identities on 1,296
    # small gap quadruples, including every zero-gap boundary case.
    for a,b,c,d in product(range(6),repeat=4):
        w=representative(a,b,c,d)
        from_word={j:defaultdict(int) for j in (0,1,3)}
        for (j,z),multiplicity in observed(w,(0,1,3)):
            from_word[j][z]=multiplicity
        calc_zero=defaultdict(int)
        for g in (a,b,c,d):
            for z in range(1,g+1):
                calc_zero[z]+=g-z+1
        calc_one=defaultdict(int)
        for left,right in ((a,b),(b,c),(c,d)):
            for i in range(left+1):
                for j in range(right+1):
                    calc_one[i+j]+=1
        calc_three=defaultdict(int)
        for i in range(a+1):
            for j in range(d+1):
                calc_three[b+c+i+j]+=1
        for layer,expected in ((0,calc_zero),(1,calc_one),(3,calc_three)):
            assert dict(from_word[layer]) == dict(expected), (a,b,c,d,layer)
    # Explicit ambiguity witness for observing only zero-three strata.
    u = representative(1,1,2,2)
    v = representative(1,2,1,2)
    assert canonical(u) != canonical(v)
    assert observed(u,(0,3)) == observed(v,(0,3))
    assert observed(u,(0,1,3)) != observed(v,(0,1,3))
    # Weight-four full-spectrum indistinguishability, from Acharya et al. (2014).
    x,y='01001101','01101001'
    assert x != y and x != y[::-1]
    assert observed(x,range(5)) == observed(y,range(5))
    print('PASS: n=3..24,',checked_words,'weight-three strings:')
    print('  zero-three strata give exactly the predicted 1 or 2 reversal classes')
    print('  adding single-one strata always yields exactly one reversal class')
    print('PASS: polynomial identities for 1,296 gap quadruples')
    print('PASS: explicit 2-class witness at weight three with zero-three strata')
    print('PASS: weight-four full-spectrum indistinguishable example')


if __name__ == '__main__':
    check()
