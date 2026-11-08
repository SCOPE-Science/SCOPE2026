#!/usr/bin/env python3
"""Finite checks for the hypercube-edge lower bound for cactus NFAs.

These checks test finite examples and graph arithmetic; they are not a
substitute for the structural proof for arbitrary alphabet size.
"""
from collections import defaultdict, deque
from itertools import product
from math import ceil
import random


def cube_edges(k):
    n = 1 << k
    out = set()
    for g in range(n):
        for i in range(k):
            h = g ^ (1 << i)
            out.add((min(g,h),max(g,h)))
    return out


def cactus_edges(cycle_lengths, bridge_count=0):
    # Glue each cycle at the original vertex; add optional bridges.
    n=1
    edges=set()
    for ell in cycle_lengths:
        assert ell >= 4 and ell % 2 == 0
        v=[0]+list(range(n,n+ell-1))
        n += ell-1
        for i in range(ell):
            a,b=v[i],v[(i+1)%ell]
            edges.add((min(a,b),max(a,b)))
    for j in range(bridge_count):
        edges.add((0,n)); n+=1
    return n,edges


def check():
    cubes=0
    for k in range(1,13):
        edges=cube_edges(k)
        n=1<<k
        assert len(edges)==k*(1<<(k-1))
        assert all(((g^h).bit_count()==1) for g,h in edges)
        assert all((g.bit_count()-h.bit_count())%2 for g,h in edges)
        if k>=3:
            bound=1+3*k*(1<<(k-3))
            assert bound==1+ceil(3*len(edges)/4)
            assert bound>n
        cubes+=1
    cacti=0
    rng=random.Random(26061008)
    for _ in range(3500):
        cycles=[rng.choice([4,6,8,10,12]) for _ in range(rng.randrange(0,12))]
        bridges=rng.randrange(0,13)
        n,edges=cactus_edges(cycles,bridges)
        assert len(edges)==n-1+len(cycles)
        assert 3*len(edges)<=4*(n-1)
        cacti+=1
    # Cross-check the target language membership against its parity DFA.
    word_tests=0
    for k in range(1,5):
        for L in range(0,9):
            for letters in product(range(k),repeat=L):
                state=0
                for i in letters: state^=1<<i
                direct=all(letters.count(i)%2==0 for i in range(k))
                assert (state==0)==direct
                word_tests+=1
    print(f'VERIFY_OK cube_dimensions={cubes} cactus_graphs={cacti} words={word_tests}')

if __name__=='__main__':
    check()
