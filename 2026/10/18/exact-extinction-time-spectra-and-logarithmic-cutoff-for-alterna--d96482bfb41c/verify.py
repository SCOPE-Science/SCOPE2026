#!/usr/bin/env python3
"""Finite exact checks for alternating lower approximations on two-matchings.

Run using Python 3 standard library: python verify.py
"""
from itertools import product
from math import comb


def matching_blocks(cycle_sizes):
    e, f = [], []
    offset = 0
    for n in cycle_sizes:
        assert n >= 1
        for j in range(n):
            e.append((offset + 2*j, offset + 2*j + 1))
            f.append((offset + 2*j + 1, offset + 2*((j+1) % n)))
        offset += 2*n
    return offset, e, f


def lower(mask, blocks):
    out = 0
    for a,b in blocks:
        pair = (1 << a) | (1 << b)
        if mask & pair == pair:
            out |= pair
    return out


def step(mask, e, f, t):
    return lower(mask, e if t % 2 == 1 else f)


def cyclic_count(n, t):
    assert n >= 1 and t >= 1
    ans = 4**n - 1
    for r in range(1, n // (t+1)+1):
        ways = n*comb(n-r*t-1, r-1)//r
        ans += (-1)**r * ways * 3**r * 4**(n-r*(t+1))
    return ans


def check_cycles():
    subsets = 0
    windows = 0
    for n in range(1, 9):
        N, e, f = matching_blocks((n,))
        distribution = [0]*(n+1)
        for S in range(1 << N):
            x = S
            first_zero = False
            block_bit = [int((S & (3 << (2*i))) == (3 << (2*i))) for i in range(n)]
            for t in range(1, n+1):
                x = step(x,e,f,t)
                if t % 2:
                    h = (t-1)//2
                    pairs = e
                    expect = [all(block_bit[(i+j)%n] for j in range(-h,h+1)) for i in range(n)]
                else:
                    h = t//2
                    pairs = f
                    expect = [all(block_bit[(i+j)%n] for j in range(1-h,h+1)) for i in range(n)]
                predicted = 0
                for pair, ok in zip(pairs,expect):
                    if ok:
                        predicted |= (1<<pair[0])|(1<<pair[1])
                assert x == predicted,(n,S,t,x,predicted)
                windows += 1
                if x == 0 and not first_zero:
                    distribution[t] += 1
                    first_zero = True
            subsets += 1
        for t in range(1,n+1):
            direct = sum(distribution[1:t+1])
            assert direct == cyclic_count(n,t),(n,t,direct,cyclic_count(n,t))
        assert sum(distribution) == 4**n-1
    return subsets,windows


def check_multicycles():
    tested = 0
    for sizes in [(1,1),(1,2),(1,3),(2,2),(1,1,3),(2,3),(1,2,3)]:
        N,e,f = matching_blocks(sizes)
        max_t = max(sizes)
        counts = [0]*(max_t+1)
        for S in range(1<<N):
            x = S
            first_zero = False
            for t in range(1,max_t+1):
                x = step(x,e,f,t)
                if x == 0 and not first_zero:
                    counts[t] += 1
                    first_zero = True
            tested += 1
        for t in range(1,max_t+1):
            assert sum(counts[1:t+1]) == __import__('math').prod(cyclic_count(n,t) for n in sizes),(sizes,t)
        assert sum(counts) == __import__('math').prod(4**n-1 for n in sizes)
    return tested


if __name__ == '__main__':
    x,y = check_cycles()
    z = check_multicycles()
    # A second, enumeration-based check for the exact run polynomial.
    # Keep the expensive 4^n enumeration bounded by n <= 7.
    p = 0
    for n in range(1,8):
        for t in range(1,n+1):
            direct = sum(1 for word in product(range(4),repeat=n)
                         if not any(all(word[(i+j)%n] == 3 for j in range(t)) for i in range(n)))
            assert direct == cyclic_count(n,t),(n,t,direct,cyclic_count(n,t))
            p += 1
    print(f'VERIFY_OK connected_subsets={x} step_window_checks={y} disconnected_subsets={z} independent_run_counts={p} n_up_to=8')
