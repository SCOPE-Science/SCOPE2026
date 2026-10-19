#!/usr/bin/env python3
"""Finite exhaustive certificate and independent spot checks for cyclic Thue--Morse square formulas.
No external dependencies. Run: python verify.py
"""
from collections import Counter
from itertools import product
from fractions import Fraction


def morph(word, times):
    for _ in range(times):
        word = ''.join('01' if c == '0' else '10' for c in word)
    return word


def bits_word(m):
    return ''.join(str(i.bit_count() & 1) for i in range(1 << m))


def square_positions(word):
    n = len(word)
    ww = word * 2
    return {(i, h) for h in range(1, n // 2 + 1) for i in range(n)
            if ww[i:i+h] == ww[i+h:i+2*h]}


def spectrum(m):
    result = Counter()
    for k in range(m-1):
        h = 1 << k
        result[h] = ((1 << (m-k)) + 2 * (-1)**(m-k)) // 3
    for k in range(m-2):
        h = 3 << k
        result[h] = ((1 << (m-k)) - 16 * (-1)**(m-k)) // 12
    return +result  # suppress zero counts


def crossing(squares, n, cut):
    return sum(0 < (cut-i) % n < 2*h for i,h in squares)


def check_local_group_certificate():
    # The complete set of length-three Thue--Morse factors is the six nonconstant triples.
    triples = [''.join(x) for x in product('01', repeat=3) if ''.join(x) not in ('000','111')]
    assert set(triples) == set(bits_word(3)[i:i+3] for i in range(6))
    case_count = 0
    for tri in triples:
        w = morph(tri, 4)
        for r in range(16):
            cut = 16+r
            g = sum(w[i:i+h] == w[i+h:i+2*h]
                    for h in (1,2,3,6) for i in range(cut-2*h+1,cut))
            start = sum(w[cut:cut+h] == w[cut+h:cut+2*h] for h in (1,2,3,6))
            assert g == 3 if r == 0 else g <= 2, (tri,r,g)
            assert g+start <= 3, (tri,r,g,start)
            case_count += 1
    # Boundary words when the lower block contains fewer than five dyadic levels.
    for q in (2,3,4):
        n=1<<q; sq={(i,h) for i,h in square_positions(bits_word(q)) if h in (1,2,3,6)}
        v=[crossing(sq,n,j) for j in range(n)]
        counts=Counter(i for i,h in sq)
        assert max(v[j]+counts[j] for j in range(n)) == (1 if q == 2 else 3)
        assert [j for j in range(n) if v[j] == max(v)] == [0,n//2]
    return case_count


def check_all_levels():
    # Fully independent direct cyclic-factor scan at every start and possible period.
    tested=0; examined=0; total_cuts=0
    for m in range(2,11):
        w=bits_word(m); n=len(w)
        assert w == morph('0',m)
        squares=square_positions(w)
        hist=Counter(h for i,h in squares)
        assert hist==spectrum(m), (m,hist,spectrum(m))
        s=(5*n-6-2*(-1)**m)//6
        weighted=(n*(21*m-14)-40*(-1)**m)//36
        assert len(squares)==s
        assert sum(h for i,h in squares)==weighted
        minimum_cross=(3*m//2-2 if m%2==0 else 3*(m-1)//2)
        crosses=[crossing(squares,n,c) for c in range(n)]
        assert max(crosses)==minimum_cross
        assert [c for c,x in enumerate(crosses) if x==max(crosses)] == [0,n//2]
        mean=Fraction(sum(s-crosses[c] for c in range(n)),n)
        assert mean==Fraction(s*(n+1)-2*weighted,n)
        tested+=1;examined+=len(squares);total_cuts+=n
    return tested,examined,total_cuts


def check_long_levels():
    # Larger levels checked only at the four base half-lengths and their scaled images.
    n_tests=0
    for m in range(11,16):
        w=bits_word(m); n=len(w); ww=w*2
        for k in range(m-1):
            h=1<<k
            starts=sum(ww[i:i+h]==ww[i+h:i+2*h] for i in range(n))
            assert starts == spectrum(m)[h], (m,h,starts)
            n_tests+=1
        for k in range(m-2):
            h=3<<k
            starts=sum(ww[i:i+h]==ww[i+h:i+2*h] for i in range(n))
            assert starts == spectrum(m)[h], (m,h,starts)
            n_tests+=1
    return n_tests

if __name__ == '__main__':
    local=check_local_group_certificate()
    levels,squares,cuts=check_all_levels()
    # Deliberately excludes very large direct full scans: the infinite proof is symbolic.
    large=check_long_levels()
    print(f'VERIFY_OK local_6x16_cases={local} full_spectrum_levels={levels} '
          f'cyclic_square_occurrences={squares} cut_profiles={cuts} larger_period_checks={large}')
