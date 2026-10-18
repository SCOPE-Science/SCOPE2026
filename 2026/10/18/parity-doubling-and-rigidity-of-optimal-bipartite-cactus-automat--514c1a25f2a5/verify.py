#!/usr/bin/env python3
"""Finite independent tests of explicit modular-language cycle construction."""
from collections import deque

def verify(m, r, letters):
    h = m if m % 2 == 0 else 2*m
    vertices = list(range(h))
    final = {j for j in vertices if j % m == r}
    trans = {(j,a): (j+1)%h for j in vertices for a in letters}
    undirected = {frozenset((j,(j+1)%h)) for j in vertices}
    assert len(undirected) == (1 if h==2 else h)
    assert all((j % 2) != ((j+1)%h % 2) for j in vertices)
    # These are precisely the single edge K2 or a simple even cycle, hence cacti.
    for length in range(4*h+1):
        for chosen in (letters[0],letters[-1]):
            state=0
            for i in range(length):
                state = trans[(state, letters[(i+ord(chosen[0]))%len(letters)])]
            assert (state in final) == (length % m == r)
    assert len(final) == h//m
    return h, len(final)

if __name__ == '__main__':
    count=0
    for m in range(2,26):
        for r in range(m):
            for alphabet in [('a',),('a','b')]:
                verify(m,r,alphabet)
                count+=1
    print('OK: canonical construction, coloring, cactus structure and modular acceptance')
    print('Parameter/alphabet configurations:',count)
    print('Moduli: 2..25; lengths: 0..4*lcm(m,2)')
