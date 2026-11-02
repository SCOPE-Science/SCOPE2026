#!/usr/bin/env python3
"""Independent finite checks for the generalized Petersen minimum-set theorem.

Standard-library only; run `python3 VERIFY.py`. Finite checks corroborate but do
not replace the arbitrary-order proof in RESULT.md.
"""
from itertools import combinations, product
from math import gcd


def graph(n):
    assert n >= 5
    adjacency = [set() for _ in range(2*n)]
    for i in range(n):
        for p, q in ((i, (i+1) % n), (n+i, n+(i+2) % n), (i, n+i)):
            adjacency[p].add(q)
            adjacency[q].add(p)
    assert all(len(v) == 3 for v in adjacency)
    return adjacency


def valid(adjacency, vertices):
    selected = set(vertices)
    for i, neighbors in enumerate(adjacency):
        k = len(neighbors & selected)
        if (i in selected and k < 2) or (i not in selected and k < 1):
            return False
    return True


def predicted(n):
    patterns = [(1,)*5, (-1,)*5]
    for signs in product((-1, 1), repeat=5):
        if signs in patterns:
            continue
        if all(signs[j]-signs[(j-1)%5]-signs[(j+1)%5] in (-1,1) for j in range(5)):
            patterns.append(signs)
    assert len(patterns) == 12
    answer = set()
    if n % 5:
        patterns = [(1,)*5,(-1,)*5]
    for pat in patterns:
        if n % 5:
            aa = [pat[0]]*n
        else:
            aa = [pat[i%5] for i in range(n)]
        bb = [aa[i]-aa[(i-1)%n]-aa[(i+1)%n] for i in range(n)]
        assert all(x in (-1,1) for x in bb)
        selected = frozenset([i for i,v in enumerate(aa) if v == 1] +
                             [n+i for i,v in enumerate(bb) if v == 1])
        assert len(selected) == n
        answer.add(selected)
    assert len(answer) == (12 if n%5 == 0 else 2)
    return answer


def verify():
    brute_tests = 0
    for n in range(5,11):
        a = graph(n)
        expected = predicted(n)
        actual = set()
        for subset in combinations(range(2*n), n):
            brute_tests += 1
            if valid(a, subset):
                actual.add(frozenset(subset))
        assert actual == expected, (n, len(actual),len(expected))
        print('BRUTE',n,len(actual))
    for n in range(5,121):
        a=graph(n)
        found=predicted(n)
        assert all(valid(a, d) for d in found)
    # Algebra check, all 32 cyclic words, including the 20 forbidden ones.
    permitted = [s for s in product((-1,1), repeat=5)
                 if all(s[i]-s[(i-1)%5]-s[(i+1)%5] in (-1,1) for i in range(5))]
    assert len(permitted) == 12
    print('VERIFY_OK brute_subsets',brute_tests,'orders=5..10','construction_orders=5..120','period5_words',len(permitted))

if __name__ == '__main__':
    verify()
