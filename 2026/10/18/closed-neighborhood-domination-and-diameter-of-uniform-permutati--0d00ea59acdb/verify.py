"""Standalone exact checks for closed-neighborhood domination in permutation trees.

Uses only Python standard library; finite checks corroborate rather than prove
asymptotic theorems.  Run as: python verify.py
"""
from fractions import Fraction as Q
from itertools import product
from math import comb


def perm_from_word(word):
    p = [2, 1]
    for bit in word:
        m = len(p)
        if bit:
            p = p[:-1] + [m + 1, p[-1]]
        else:
            p = [m + 1 if x == m else x for x in p] + [m]
    return p


def brute_gamma_and_diameter(p):
    n = len(p)
    neighborhoods = [1 << i for i in range(n)]
    graph = [set() for _ in range(n)]
    edges = 0
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] > p[j]:
                a, b = p[i] - 1, p[j] - 1
                neighborhoods[a] |= 1 << b
                neighborhoods[b] |= 1 << a
                graph[a].add(b)
                graph[b].add(a)
                edges += 1
    assert edges == n - 1
    target = (1 << n) - 1
    gamma = n
    for mask in range(1, 1 << n):
        if mask.bit_count() >= gamma:
            continue
        union = 0
        for i in range(n):
            if mask & (1 << i):
                union |= neighborhoods[i]
        if union == target:
            gamma = mask.bit_count()
    diameter = 0
    for root in range(n):
        seen = {root}
        frontier = {root}
        distance = 0
        while frontier:
            next_frontier = set().union(*(graph[v] for v in frontier)) - seen
            if next_frontier:
                distance += 1
            seen.update(next_frontier)
            frontier = next_frontier
        assert len(seen) == n
        diameter = max(diameter, distance)
    return gamma, diameter


def formula(word):
    lengths = []
    count = 0
    last = None
    for b in word:
        if b != last and count:
            lengths.append(count)
            count = 0
        count += 1
        last = b
    lengths.append(count)
    m = len(lengths)
    forced = sorted(set([0, m - 1] + [i for i in range(1, m - 1)
                                           if lengths[i] >= 2]))
    gamma = len(forced) + sum((b - a - 1) // 3 for a, b in zip(forced, forced[1:]))
    return gamma, m + 1


def independent_cycle_moments():
    # K = 3W+B; W and B independent; J = 2+G.
    # K,G geometric with mass 2^(-k-1).  W geometric with P(W=w)=7/8^(w+1).
    EW, VW = Q(1, 7), Q(8, 49)
    EB, VB = Q(4, 7), Q(26, 49)
    EG, VG = Q(1), Q(2)
    EM = 3*EW + EB + 2 + EG
    ER = 1 + EW
    EC = 3*EW + EB + 1
    assert (EM, ER, EC) == (4, Q(8,7), 2)
    alpha, beta = ER/EM, EC/EM
    assert (alpha, beta) == (Q(2,7), Q(1,2))
    vgamma = (VW+4*VB+4*VG)/(49*EM)
    vdiam = (9*VW+VB+VG)/(4*EM)
    cross = (3*VW-2*VB+2*VG)/(14*EM)
    assert (vgamma, cross, vdiam) == (Q(18,343),Q(3,49),Q(1,4))
    assert vgamma*vdiam-cross*cross == Q(45,4802)


def main():
    independent_cycle_moments()
    tally = 0
    for n in range(3, 12):
        for word in product((0, 1), repeat=n-2):
            assert brute_gamma_and_diameter(perm_from_word(word)) == formula(word), (n, word)
            tally += 1
    print(f"PASS: {tally} exact permutation-tree/domain checks for n=3..11;")
    print("PASS: exact rational renewal-reward mean/covariance checks.")


if __name__ == '__main__':
    main()
