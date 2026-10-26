#!/usr/bin/env python3
"""Independently reproduce cyclic-complexity counts for generalized Cantor words.

Runs using Python 3 with only the standard library. The mathematical proof,
not the finite test range, establishes the all-parameter formula.
"""
import csv
from collections import defaultdict
from pathlib import Path


def cantor(q, steps):
    word = '1'
    for _ in range(steps):
        word = ''.join('1' + '0' * (q-2) + '1' if c == '1'
                       else '0' * q for c in word)
    return word


def booth(s):
    """Canonical lexicographically smallest cyclic rotation in linear time."""
    n = len(s)
    t = s+s
    i, j, z = 0, 1, 0
    while i < n and j < n and z < n:
        if t[i+z] == t[j+z]:
            z += 1
            continue
        if t[i+z] > t[j+z]:
            i += z + 1
        else:
            j += z + 1
        if i == j:
            j += 1
        z = 0
    p = min(i,j)
    return t[p:p+n]


def naive_rotation(s):
    return min(s[i:]+s[:i] for i in range(len(s)))


def validate(q,k):
    N=q**k
    A=cantor(q,k)
    assert len(A)==N and A==A[::-1]
    assert A[0]==A[-1]=='1' and A.count('1')==2**k
    expanded=cantor(q,k+2)
    direct={expanded[i:i+N] for i in range(len(expanded)-N+1)}
    # The original infinite word decomposes at level k into zero or A blocks.
    # All three allowed neighboring block pairs 00, 01, 10 occur in cantor(q,2).
    blocks=({A[t:]+'0'*t for t in range(N)} |
            {'0'*(N-t)+A[:t] for t in range(N)})
    assert direct==blocks, (q,k,'block coverage',len(direct),len(blocks))
    necklaces=defaultdict(set)
    for f in direct:
        necklaces[f.count('1')].add(booth(f))
    r=2**k
    assert sorted(necklaces)==list(range(r+1))
    counts=[len(necklaces[m]) for m in range(r+1)]
    assert counts[0]==counts[-1]==1
    for m in range(1,r):
        assert counts[m] == (1 if m & (m-1)==0 else 2), (q,k,m,counts[m])
    distinct=sum(counts)
    assert distinct==2**(k+1)-k
    # Independent direct rotation algorithm, for small enough lengths.
    if N<=64:
        assert {booth(f) for f in direct}=={naive_rotation(f) for f in direct}
    # Verify the exact 2-adic consecutive-one gap formula used in the proof.
    pos=[i for i,letter in enumerate(A) if letter=='1']
    assert all(p%(q-1)==0 for p in pos)
    for j in range(1,len(pos)):
        t=(j&-j).bit_length()-1
        assert pos[j]-pos[j-1]==(q-2)*(q**t)+1
    return (q,k,N,len(direct),distinct,2**(k+1)-k,
            sum(1 for m in range(1,r) if counts[m]==1))


def main():
    results=[]
    for q in range(3,8):
        for k in range(5):
            results.append(validate(q,k))
    for k in (5,6,7):
        results.append(validate(3,k))
    for k in (5,):
        results.append(validate(4,k))
    here=Path(__file__).resolve().parent
    csvpath=here/'counts.csv'
    with csvpath.open('w',newline='',encoding='utf-8') as fp:
        writer=csv.writer(fp,lineterminator='\n')
        writer.writerow(['base_q','level_k','factor_length','distinct_factors',
                         'cyclic_classes_computed','cyclic_classes_formula',
                         'interior_singleton_weight_classes'])
        writer.writerows(results)
    print('VERIFY_OK cases=',len(results),
          'base_range=3..7 level_range=0..4 extra=(3,5..7),(4,5)',
          'block_factor_enumeration=yes independently_generated_full_word=yes',
          'canonical_rotation_algorithms=2_small_cases',
          'gap_formula_verified=yes',
          'full_per_weight_spectrum=yes',sep=' ')
    print('VERIFY_OK classical_q=3 c(1),c(3),...,c(2187)=',
          [r[4] for r in results if r[0]==3],sep='')

if __name__=='__main__':
    main()
