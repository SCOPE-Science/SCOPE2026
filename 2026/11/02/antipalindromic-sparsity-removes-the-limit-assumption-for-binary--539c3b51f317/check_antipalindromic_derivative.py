#!/usr/bin/env python3
"""Finite consistency checks for the binary-difference palindromic reduction.
The infinite asymptotic proof invokes Shallit's theorem; these finite tests do
not establish convergence and are not presented as asymptotic certificates.
"""
from itertools import product


def factors(word, n):
    return {tuple(word[i:i+n]) for i in range(len(word)-n+1)}


def derivative(word):
    return tuple(x ^ y for x,y in zip(word, word[1:]))


def antipal(word):
    return all(word[i] != word[-i-1] for i in range(len(word)))


def pal(word):
    return word == word[::-1]


def transformations(word):
    return {word, word[::-1], tuple(1-x for x in word), tuple(1-x for x in word[::-1])}


def check_all_short_words():
    tests = 0
    for L in range(2,12):
        for word in product((0,1),repeat=L):
            diff = derivative(word)
            for n in range(2,L+1):
                source = factors(word,n)
                differences = factors(diff,n-1)
                E = {w for w in source if antipal(w)}
                P = {w for w in differences if pal(w)}
                assert all(pal(derivative(w)) for w in E)
                assert len(E) <= 2*len(P)
                assert len(differences) <= len(source)
                tests += 1
    return tests


def check_group_identity():
    tests = 0
    for L in range(1,10):
        for word in product((0,1),repeat=L):
            for n in range(1,L+1):
                lang = set().union(*(transformations(f) for f in factors(word,n)))
                orbits = {min(transformations(f)) for f in lang}
                ordinary = sum(pal(w) for w in lang)
                anti = sum(antipal(w) for w in lang)
                assert 4*len(orbits) == len(lang)+ordinary+anti
                tests += 1
    return tests


def check_examples():
    # Prefix experiments merely test algebra on familiar morphic sequences.
    thue = [0]
    for _ in range(11):
        thue = [y for x in thue for y in (x,1-x)]
    fib = [0]
    for _ in range(15):
        fib = [y for x in fib for y in ((0,1) if x==0 else (0,))]
    tests = 0
    for name,word in [('Thue-Morse',thue),('Fibonacci',fib)]:
        for n in range(2,26):
            F = factors(word,n)
            D = factors(derivative(word),n-1)
            E = {w for w in F if antipal(w)}
            P = {w for w in D if pal(w)}
            assert len(E) <= 2*len(P)
            assert len(D) <= len(F)
            tests += 1
        print(f'{name}: prefix_length={len(word)} tested_lengths=2..25')
    return tests


def main():
    a = check_all_short_words()
    b = check_group_identity()
    c = check_examples()
    print(f'finite_derivative_inequality_cases={a}')
    print(f'finite_Burnside_identity_cases={b}')
    print(f'morphic_prefix_cases={c}')
    print('PASS: all finite identities; asymptotics follow from the cited theorem, not finite tests.')

if __name__ == '__main__':
    main()
