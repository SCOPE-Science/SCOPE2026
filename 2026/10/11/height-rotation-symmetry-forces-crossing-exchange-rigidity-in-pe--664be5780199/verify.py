#!/usr/bin/env python3
"""Reproducible small-size regression checks of petal-move rigidity."""
from itertools import permutations
from math import gcd, factorial


def canon(word):
    word = tuple(word)
    return word[word.index(0):] + word[:word.index(0)]


def moves(word):
    """All cyclicly normalized height-preserving moves R,S,X (published convention)."""
    N = len(word)
    assert sorted(word) == list(range(N)) and N % 2
    out = {canon((x + 1) % N for x in word),
           canon(N - 1 - x for x in word[::-1])}
    for b in range(N):
        groups = [frozenset((word[(b + 2*j + 1) % N],
                             word[(b + 2*j + 2) % N]))
                  for j in range((N-1)//2)]
        for m in range(N-3):
            for w in range(m+2, N-1):
                g = frozenset((m,w+1))
                h = frozenset((m+1,w))
                if g not in groups or h not in groups:
                    continue
                inside = frozenset(range(m+2, w))
                if not all((not pair & inside or pair <= inside)
                           for pair in groups if pair != g and pair != h):
                    continue
                switched = tuple(x+1 if x in (m,w) else
                                 x-1 if x in (m+1,w+1) else x
                                 for x in word)
                out.add(canon(switched))
    out.discard(word)
    return out


def can_delete(word):
    return any(abs(a-b) == 1 for a,b in
               zip(word, word[1:] + word[:1]))


def independent_x(word):
    """Explicit direct X check, excluding R and S, by exhaustive geometry."""
    N = len(word)
    for b in range(N):
        groups = [frozenset((word[(b+2*j+1) % N],
                             word[(b+2*j+2) % N]))
                  for j in range((N-1)//2)]
        for m in range(N-3):
            for w in range(m+2,N-1):
                g,h = frozenset((m,w+1)), frozenset((m+1,w))
                if g not in groups or h not in groups:
                    continue
                interval = set(range(m+2,w))
                if all((not (set(t)&interval)) or set(t) <= interval
                       for t in groups if t not in (g,h)):
                    return True
    return False


def components7():
    unseen = {(0,)+t for t in permutations(range(1,7))}
    sizes = []
    while unseen:
        seed = next(iter(unseen))
        unseen.remove(seed)
        stack, count = [seed], 0
        while stack:
            w = stack.pop()
            count += 1
            for v in moves(w):
                if v in unseen:
                    unseen.remove(v)
                    stack.append(v)
        sizes.append(count)
    assert sum(sizes) == factorial(6)
    assert len(sizes) == 50


def main():
    for N in (3,5,7,9,11,13):
        units = [s for s in range(1,N) if gcd(s,N)==1]
        trap = 0
        for s in units:
            word = tuple(s*j % N for j in range(N))
            assert word[0] == 0 and len(set(word)) == N
            rotated = canon(((x+1)%N for x in word))
            inverted = canon((N-1-x for x in word[::-1]))
            assert rotated == word and inverted == word
            assert not independent_x(word), (N,s,'crossing exchange')
            assert can_delete(word) == (s in (1,N-1))
            trap += not can_delete(word)
        assert trap == len(units)-2, (N,trap)
        print('N',N,'R_fixed',len(units),'rigid',trap)
    components7()
    print('VERIFY_OK')

if __name__=='__main__':
    main()
