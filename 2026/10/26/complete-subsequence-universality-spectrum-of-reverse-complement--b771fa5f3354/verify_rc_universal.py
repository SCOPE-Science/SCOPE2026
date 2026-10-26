#!/usr/bin/env python3
"""Independent finite checks for a reverse-complement subsequence-universality census."""
from collections import Counter, defaultdict
from itertools import product
from math import comb, factorial


def index_and_rest(word, q):
    complete = 0
    seen = set()
    for symbol in word:
        seen.add(symbol)
        if len(seen) == q:
            complete += 1
            seen.clear()
    return complete, frozenset(seen)


def contains_subsequence(target, source):
    pos = 0
    for letter in source:
        if pos < len(target) and letter == target[pos]:
            pos += 1
    return pos == len(target)


def stirling(max_n, max_k):
    S = [[0] * (max_k + 1) for _ in range(max_n + 1)]
    S[0][0] = 1
    for n in range(1, max_n + 1):
        for k in range(1, min(n, max_k) + 1):
            S[n][k] = k*S[n-1][k] + S[n-1][k-1]
    return S


def formula_coefficients(q, M):
    # Build arch and residue ordinary generating functions independently
    # using surjection counts (Stirling numbers of the second kind).
    p = q // 2
    S = stirling(M, q)
    A = [0] * (M + 1)
    B = [0] * (M + 1)
    H = [0] * (M + 1)
    for m in range(M + 1):
        if m >= q:
            A[m] = factorial(q) * S[m-1][q-1]
        for s in range(0, min(q - 1, m) + 1):
            n_fixed_alphabet = factorial(s) * S[m][s]
            B[m] += comb(q, s) * n_fixed_alphabet
            if s >= p:
                H[m] += comb(p, s-p) * (2 ** (q-s)) * n_fixed_alphabet
    arch_powers = [[0] * (M+1) for _ in range(M//q+1)]
    arch_powers[0][0] = 1
    for k in range(1, len(arch_powers)):
        for m in range(M+1):
            arch_powers[k][m] = sum(arch_powers[k-1][m-j]*A[j] for j in range(q, m+1))
    counts = [Counter() for _ in range(M+1)]
    for k, P in enumerate(arch_powers):
        for m in range(M+1):
            complete = sum(P[a] * H[m-a] for a in range(m+1))
            other = sum(P[a] * (B[m-a]-H[m-a]) for a in range(m+1))
            counts[m][2*k] += other
            counts[m][2*k+1] += complete
    return counts


def automaton_coefficients(q, M):
    # Direct finite-state walk count on half-word letters, no Stirling formulas.
    dp = {(0,0): 1}
    result = []
    full = (1<<q)-1
    for m in range(M+1):
        C=Counter()
        for (k,mask), ways in dp.items():
            mirrored=0
            for j in range(q):
                if mask & (1<<j):
                    mirrored |= 1<<(j^1)
            C[2*k + int((mask | mirrored)==full)] += ways
        result.append(C)
        nxt=defaultdict(int)
        for (k, mask), ways in dp.items():
            for letter in range(q):
                newmask = mask | (1<<letter)
                if newmask == full:
                    nxt[(k+1,0)] += ways
                else:
                    nxt[(k,newmask)] += ways
        dp=nxt
    return result


def brute_check(q, M):
    checked=0
    for m in range(M+1):
        for half in product(range(q), repeat=m):
            whole = half + tuple((a ^ 1) for a in half[::-1])
            idx, _ = index_and_rest(whole,q)
            k, residue=index_and_rest(half,q)
            expected=2*k + int(len(residue | frozenset(a^1 for a in residue))==q)
            assert idx == expected, (q, half, idx, expected)
            # Completely separate definition-level check of universal subsequences.
            for L in range(0,min(2*m//q, 3)+1):
                is_universal = all(contains_subsequence(t,whole) for t in product(range(q),repeat=L))
                assert is_universal == (idx>=L), (q,half,L)
            checked += 1
    return checked


def main():
    words=0
    tests=[]
    for q, m_max, brute_max in [(2,60,11),(4,30,7),(6,22,5),(8,17,3)]:
        algebra=formula_coefficients(q,m_max)
        automaton=automaton_coefficients(q,m_max)
        for m in range(m_max+1):
            aa=Counter({i:n for i,n in algebra[m].items() if n})
            bb=Counter({i:n for i,n in automaton[m].items() if n})
            assert aa==bb, (q,m,aa,bb)
            assert sum(aa.values())==q**m,(q,m)
        words+=brute_check(q, brute_max)
        for h in range(1, min(2*m_max//q,9)+1):
            m=q*h//2
            predicted=(factorial(q)**(h//2)) * (1 if h%2==0 else (2**(q//2))*factorial(q//2))
            assert algebra[m][h]==predicted,(q,h,algebra[m][h],predicted)
            assert all(algebra[j][h]==0 for j in range(m)),(q,h)
        tests.append(f'q={q}:coeff_half_lengths=0..{m_max}')
    print('REVERSE_COMPLEMENT_UNIVERSALITY_PASS', 'brute_half_words='+str(words), ';'.join(tests))


if __name__ == '__main__':
    main()
