#!/usr/bin/env python3
"""Independent finite-case and algebraic checks for the stated geometric probability law.
Uses Python standard library only. Finite enumeration is corroboration, not the asymptotic proof.
"""
import itertools
from fractions import Fraction
from math import comb


def rank_affine(vertices, n):
    if not vertices:
        return -1
    anchor = vertices[0]
    rows = [[Fraction(((v >> i) & 1) - ((anchor >> i) & 1)) for i in range(n)]
            for v in vertices[1:]]
    rank = 0
    for c in range(n):
        pivot = next((j for j in range(rank, len(rows)) if rows[j][c]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        lead = rows[rank][c]
        rows[rank] = [z / lead for z in rows[rank]]
        for j in range(rank + 1, len(rows)):
            if rows[j][c]:
                v = rows[j][c]
                rows[j] = [rows[j][k] - v * rows[rank][k] for k in range(n)]
        rank += 1
        if rank == n:
            break
    return rank


def projections(vertices, n, I):
    I = list(I)
    return {sum(((v >> i) & 1) << k for k, i in enumerate(I)) for v in vertices}


def product_split(vertices, n, I):
    if not vertices:
        return False
    J = tuple(i for i in range(n) if i not in I)
    return len(projections(vertices, n, I)) * len(projections(vertices, n, J)) == len(vertices)


def singleton_event(vertices, n, i):
    V = set(vertices)
    return all((v ^ (1 << i)) in V for v in V)


def exact_small(n, p):
    q = 1 - p
    N = 1 << n
    prob_full = prob_decomp = prob_prism = Fraction(0)
    counts = {'full': 0, 'decomp_full': 0, 'prism_full': 0,
              'no_singleton_split_full': 0}
    spl = [tuple(I) for k in range(1, n // 2 + 1)
           for I in itertools.combinations(range(n), k)]
    for mask in range(1 << N):
        vertices = [v for v in range(N) if (mask >> v) & 1]
        if rank_affine(vertices, n) != n:
            continue
        v_count = len(vertices)
        prob = p ** v_count * q ** (N - v_count)
        decomposition = any(product_split(vertices, n, I) for I in spl)
        prism = any(singleton_event(vertices, n, i) for i in range(n))
        prob_full += prob
        counts['full'] += 1
        if decomposition:
            counts['decomp_full'] += 1
            prob_decomp += prob
        if prism:
            counts['prism_full'] += 1
            prob_prism += prob
        if decomposition and not prism:
            counts['no_singleton_split_full'] += 1
    b = p*p + q*q
    c = p**4+q**4
    lower_bonf = n*b**(N//2)-comb(n, 2)*c**(N//4)
    assert lower_bonf <= n*b**(N//2)
    assert prob_decomp >= prob_prism
    assert prob_prism <= n*b**(N//2)
    assert prob_decomp <= 1
    return counts, {'full': prob_full, 'decomp_full': prob_decomp,
                    'prism_full': prob_prism, 'n_b_N2': n*b**(N//2),
                    'bonferroni': lower_bonf}


def verify_gap(p):
    q=1-p
    b=p*p+q*q
    c=p**4+q**4
    assert c < b*b
    if p >= q:
        rho4=p**4+q**4
    else:
        rho4=q*q*b
    assert rho4 < b*b
    for k in range(2,8):
        M=1<<k
        bound = rho4 ** (M//4)
        for a in range(2,M+1):
            f=q**M+p**a*q**(M-a)
            assert f <= bound, (p,k,a, f, bound)


if __name__ == '__main__':
    for p in [Fraction(1,10),Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(9,10)]:
        verify_gap(p)
        print('analytic finite-parameter rate tests:',str(p),'PASS')
    for n in (3, 4):
        for p in (Fraction(1,2), Fraction(1,3)):
            counts,probs=exact_small(n,p)
            print('exhaustive', n, str(p), counts,
                  'probability_decomp_given_full=',float(probs['decomp_full']/probs['full']),
                  'probability_prism_given_full=',float(probs['prism_full']/probs['full']))
    print('ALL TESTS PASSED')
