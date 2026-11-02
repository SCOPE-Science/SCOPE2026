#!/usr/bin/env python3
"""Exact finite cross-checks for uniform-minimum-spacing subsequence universality.
No third-party dependencies. Run: python3 verify.py
"""
from itertools import product
from math import comb, factorial


def oracle_index(word, q, s):
    """Independent literal oracle testing all target strings by greedy embedding."""
    n = len(word)
    best = 0
    for k in range(1, (n-1)//s+2):
        def embeds(pat):
            pos = -s
            for target in pat:
                for j in range(pos+s, n):
                    if word[j] == target:
                        pos = j
                        break
                else:
                    return False
            return True
        if all(embeds(p) for p in product(range(q), repeat=k)):
            best = k
        else:
            break
    return best


def inclusion_counts(q, nmax):
    # Prefixes avoiding at least one alphabet symbol; shortest all-letter arches.
    I = [sum((-1)**(q-1-j)*comb(q,j)*j**n for j in range(q))
         for n in range(nmax+1)]
    F = [0] + [q*sum((-1)**(q-1-j)*comb(q-1,j)*j**(n-1)
                    for j in range(q)) for n in range(1,nmax+1)]
    return I, F


def predicted(q,s,nmax):
    I,F = inclusion_counts(q,nmax)
    T = [(q**n if n < s-1 else q**(s-1)*I[n-(s-1)])
         for n in range(nmax+1)]
    out = [[0]*(nmax+1) for _ in range(nmax+1)]
    out[0] = I
    for n in range(nmax+1):
        out[1][n] = sum(F[t]*T[n-t] for t in range(n+1))
    for k in range(2,nmax+1):
        for n in range(nmax+1):
            out[k][n] = (q**(s-1)*sum(F[t]*out[k-1][n-s+1-t]
                  for t in range(n-s+2)) if n>=s-1 else 0)
    return out


def run():
    cases = [(2,1,12), (2,2,13), (2,3,12), (2,4,11),
             (3,1,9), (3,2,9), (3,3,8), (4,2,7)]
    total_words = 0
    for q,s,nmax in cases:
        expected = predicted(q,s,nmax)
        for n in range(nmax+1):
            freq = [0]*(nmax+1)
            for w in product(range(q),repeat=n):
                i = oracle_index(w,q,s)
                assert i <= nmax
                freq[i] += 1
                total_words += 1
            assert sum(freq) == q**n
            for k in range(nmax+1):
                assert freq[k] == expected[k][n], (q,s,n,k,freq[k],expected[k][n])
        # Minimum size and all shortest host counts, including k=1.
        for k in range(1,5):
            L = q*k+(s-1)*(k-1)
            if L<=nmax:
                assert expected[k][L] == factorial(q)**k*q**((s-1)*(k-1))
                assert all(expected[k][j]==0 for j in range(L))
        print(f'case_ok q={q} spacing={s} n=0..{nmax}')
    print(f'VERIFY_OK independent_literal_hosts={total_words} alphabets=2..4 spacing=1..4 exact_bivariate_coefficients=TRUE shortest_hosts=TRUE')


if __name__ == '__main__':
    run()
