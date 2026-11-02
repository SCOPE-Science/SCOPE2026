#!/usr/bin/env python3
"""Reproduce the zero-run-constrained cyclic covering counts and instances."""
from collections import Counter
from itertools import product
from random import Random


def windows(s, k):
    ext = s + s[:k-1]
    return Counter(ext[i:i+k] for i in range(len(s)))


def admissible(r):
    return {''.join(x) for x in product('01', repeat=r+1) if '0'*r not in ''.join(x)}


def canon(s):
    return min(s[j:]+s[:j] for j in range(len(s)))


def target_deck(r):
    return Counter({s: 1 for s in admissible(r)}) + Counter({'1'+'0'*(r-1)+'1': 1})


def exhaustive(r):
    length = 2**(r+1)-2
    target = target_deck(r)
    representatives = set()
    for tpl in product('01', repeat=length):
        s = ''.join(tpl)
        if '0'*r in s+s[:r-1]:
            continue
        deck = windows(s, r+1)
        if set(deck) != set(target):
            continue
        assert deck == target
        representatives.add(canon(s))
    assert len(representatives) == 2**(2**r-r-2)
    return length, len(representatives)


def bareiss_det(a):
    a = [row[:] for row in a]
    n = len(a)
    old = 1
    sign = 1
    for k in range(n-1):
        if a[k][k] == 0:
            row = next((j for j in range(k+1,n) if a[j][k]), None)
            assert row is not None
            a[k],a[row] = a[row],a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k+1,n):
            v = a[i][k]
            for j in range(k+1,n):
                a[i][j] = (pivot*a[i][j]-v*a[k][j])//old
            a[i][k] = 0
        old = pivot
    return sign*a[-1][-1]


def tree_count(r):
    states = list(range(1, 2**r))
    n = len(states)
    idx = {v:j for j,v in enumerate(states)}
    L = [[0]*n for _ in states]
    for v in states:
        a = idx[v]
        L[a][a] += 2
        for bit in (0,1):
            dest = ((v<<1) | bit) & (2**r-1)
            if dest == 0:
                dest = 1
            L[a][idx[dest]] -= 1
    return bareiss_det([row[1:] for row in L[1:]])


def eulerian_example(r, rng):
    # Construct Euler circuit of the degree-two completed graph.
    n = 2**r
    a = {state: [] for state in range(1, n)}
    for state in a:
        for bit in (0,1):
            dest = ((state<<1) | bit) & (n-1)
            if dest == 0:
                dest = 1
                bit = 1
            a[state].append((dest,str(bit)))
        rng.shuffle(a[state])
    stack = [(1,'')]
    digits = []
    while stack:
        state, digit = stack[-1]
        if a[state]:
            dest, bit = a[state].pop()
            stack.append((dest,bit))
        else:
            stack.pop()
            if digit: digits.append(digit)
    s = ''.join(reversed(digits))
    assert len(s) == n*2-2
    assert windows(s,r+1)==target_deck(r)
    return s


def main():
    for r in (2,3):
        print('EXHAUSTIVE',r,exhaustive(r))
    for r in range(2,7):
        got = tree_count(r)
        want = 2**(2**r-r-1)
        assert got == want, (r,got,want)
        print('MATRIX_TREE',r,got)
    rng=Random(20261028)
    for r in range(2,11):
        for trial in range(25):
            eulerian_example(r,rng)
    print('VERIFY_OK cyclic_exhaustive_r=2,3 matrix_tree_r=2..6 constructed_r=2..10 instances=225')

if __name__ == '__main__':main()
