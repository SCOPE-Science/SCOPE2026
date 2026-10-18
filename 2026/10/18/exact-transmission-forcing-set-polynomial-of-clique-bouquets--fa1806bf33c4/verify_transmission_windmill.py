#!/usr/bin/env python3
"""Direct exhaustive checks for the transmission forcing-set polynomial on clique bouquets.

For a graph with a common vertex adjoining k disjoint cliques K_m, compare
all 2**(km+1) initial sets with the exact proposed count by set cardinality.
The simulator uses simultaneous rounds and exact rational arithmetic.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


def neighbors(k, m):
    n = 1 + k * m
    out = [set() for _ in range(n)]
    for i in range(k):
        block = list(range(1 + i*m, 1 + (i+1)*m))
        for u in block:
            out[0].add(u)
            out[u].add(0)
            for v in block:
                if v != u:
                    out[u].add(v)
    return [tuple(sorted(x)) for x in out]


def succeeds(adj, seeds_mask, alpha, beta):
    n = len(adj)
    filled = seeds_mask
    weights = [Fraction((seeds_mask >> i) & 1) for i in range(n)]
    if filled == (1 << n)-1:
        return True
    for _ in range(n):
        next_weights = weights[:]
        for v in range(n):
            if not (filled >> v) & 1:
                continue
            white = [u for u in adj[v] if not ((filled >> u) & 1)]
            if len(white) == 1:
                next_weights[white[0]] += alpha * weights[v]
        new_mask = 0
        for u in range(n):
            if not (filled >> u) & 1 and next_weights[u] >= beta:
                new_mask |= 1 << u
        if new_mask == 0:
            return False
        weights = next_weights
        filled |= new_mask
        if filled == (1 << n)-1:
            return True
    raise AssertionError("Unbounded filling process")


def predicted_counts(k, m, alpha, beta):
    n = 1 + k*m
    L, U, H = (m-1)*alpha, m*alpha, k*m*alpha
    T = min(m*(k-1)*alpha, (m-1)*alpha + m*(k-1)*alpha*alpha)
    out = Counter()
    if beta <= L:
        # Expand z^(n-k-1) * ((1+z)*(z+m)^k-m^k), coefficient by coefficient.
        for j in range(k+1):
            a = comb(k,j) * m**(k-j)
            out[n-k-1+j] += a
            out[n-k+j] += a
        out[n-k-1] -= m**k
    else:
        out[n] += 1
        if beta <= U:
            out[n-1] += k*m
        if beta <= H:
            out[n-1] += 1
        if beta <= T:
            out[n-2] += k*m
    return +out


def actual_counts(k, m, alpha, beta):
    adj = neighbors(k,m)
    n = len(adj)
    return +Counter(mask.bit_count() for mask in range(1<<n)
                    if succeeds(adj,mask,alpha,beta))


def main():
    graph_cases = [(2,2), (3,2), (4,2), (2,3), (3,3), (2,4), (3,4)]
    total = 0
    for k,m in graph_cases:
        alpha_choices = [Fraction(1,17),Fraction(1,7),Fraction(1,3),Fraction(3,4),Fraction(1)]
        for alpha in alpha_choices:
            L = (m-1)*alpha
            U = m*alpha
            H = k*m*alpha
            T = min(m*(k-1)*alpha,L+m*(k-1)*alpha*alpha)
            test_betas = {Fraction(1,1),Fraction(1,2),Fraction(1,7),Fraction(1,17)}
            for boundary in (L,T,U,H):
                for beta in (boundary-Fraction(1,10000),boundary,boundary+Fraction(1,10000)):
                    if 0<beta<=1:
                        test_betas.add(beta)
            for beta in sorted(test_betas):
                if not 0<beta<=1:
                    continue
                got = actual_counts(k,m,alpha,beta)
                exp = predicted_counts(k,m,alpha,beta)
                assert got == exp, (k,m,alpha,beta,exp,got)
                total+=1
        print(f"PASS k={k}, m={m}")
    print(f"PASS {total} parameter/graph pairs; each checks all labelled seed subsets by cardinality")
    k,m,alpha = 4,2,Fraction(1,20)
    cases = [Fraction(1,25),Fraction(3,50),Fraction(2,25),Fraction(1,5),Fraction(7,10)]
    print('Sharp phase example, k=4,m=2,alpha=1/20:')
    for beta in cases:
        counts = actual_counts(k,m,alpha,beta)
        print(f' beta={beta}, minimum={min(counts)}, number_of_minimum_sets={counts[min(counts)]}')


if __name__ == '__main__':
    main()
