#!/usr/bin/env python3
"""Finite checks for exact cyclic covers of all four-letter tandem squares."""
from itertools import product
from math import comb
from functools import lru_cache


def motifs(q):
    return [tuple((a, b, a, b)) for a in range(q) for b in range(q)]


def overlap(a, b):
    return max((k for k in (1, 2, 3) if a[-k:] == b[:k]), default=0)


def target_order(q):
    order = []
    for a in range(q):
        order.append((a, a, a, a))
        for b in range(a+1, q):
            order.extend(((a, b, a, b), (b, a, b, a)))
    return order


def construct(q):
    order = target_order(q)
    word = list(order[0])
    for a, b in zip(order, order[1:]):
        word.extend(b[overlap(a, b):])
    return tuple(word)


def cyclic_windows(w, k):
    n = len(w)
    return {tuple(w[(i+j) % n] for j in range(k)) for i in range(n)}


def held_karp(q):
    """Independent exhaustive dynamic program for all Hamiltonian motif tours."""
    M = motifs(q)
    n = len(M)
    C = [[4-overlap(M[i], M[j]) for j in range(n)] for i in range(n)]

    @lru_cache(maxsize=None)
    def dp(mask, last):
        if mask == (1<<n)-1:
            return C[last][0]
        return min(C[last][j] + dp(mask | (1<<j), j)
                   for j in range(1,n) if not mask & (1<<j))
    return dp(1,0)


def transition_counts(order):
    costs = [4-overlap(a,b) for a,b in zip(order,order[1:]+order[:1])]
    return {i: costs.count(i) for i in (1,2,3,4)}


def test():
    for q in range(2,51):
        order = target_order(q)
        W = construct(q)
        assert len(order) == q*q
        assert len(set(order)) == q*q
        assert len(W) == 2*q*(q+1), (q,len(W))
        assert set(motifs(q)) <= cyclic_windows(W,4)
        hist = transition_counts(order)
        assert hist[1] == comb(q,2), (q,hist)
        assert hist[2] == 0
        assert hist[4] == q
        assert hist[3] == q*q - comb(q,2) - q
        print(f'construct q={q}: length={len(W)}, overlap histogram={hist}' if q<=5 or q==50 else '', end='\n' if q<=5 or q==50 else '')
    for q in (2,3,4):
        v=held_karp(q)
        assert v==2*q*(q+1),(q,v)
        print(f'independent exact Held-Karp q={q}: {v}')
    # Exhaust all binary circular words below the claimed optimum.
    for L in range(4,12):
        for W in product((0,1), repeat=L):
            assert not set(motifs(2)).issubset(cyclic_windows(W,4)),(L,W)
    print('all short binary cyclic strings excluded; construction and exact DP passed')

if __name__=='__main__':test()
