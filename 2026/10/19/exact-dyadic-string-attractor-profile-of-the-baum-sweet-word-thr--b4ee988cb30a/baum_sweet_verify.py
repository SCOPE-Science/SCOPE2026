#!/usr/bin/env python3
"""Replays finite exact Baum--Sweet prefix attractor certificates using only Python stdlib."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'baum_sweet_certificate.json').read_text(encoding='utf-8'))

def digit_term(n):
    if n==0:return '1'
    return '1' if all(len(run)%2==0 for run in bin(n)[2:].split('1')) else '0'

def morphic_word(n):
    table={'00':'0000','01':'1001','10':'0100','11':'1101'}
    result='11'
    while len(result)<n:
        result=''.join(table[result[j:j+2]] for j in range(0,len(result),2))
    assert len(result)==n
    return result

def verify(case):
    n=case['length']
    assert n>0 and (n&(n-1))==0
    w=morphic_word(n)
    assert w==''.join(digit_term(k) for k in range(n))
    S=case['attractor_positions_zero_based']
    v=case['optimum']
    assert S==sorted(set(S)) and len(S)==v and all(0<=x<n for x in S)

    # Exact upper bound: every distinct nonempty factor has an occurrence
    # intersecting a specified attractor position.
    total_factors=0
    for ell in range(1,n+1):
        all_factors={w[j:j+ell] for j in range(n-ell+1)}
        covered={w[j:j+ell] for j in range(n-ell+1)
                 if any(j<=s<j+ell for s in S)}
        assert all_factors==covered, ('upper_bound',n,ell,all_factors-covered)
        total_factors += len(all_factors)

    # Exact lower bound: for each specified factor f, U(f) is the union of
    # positions covered by its occurrences.  Weight y_f = two/2.
    # The explicitly checked packing condition is sum_{f:p in U(f)} y_f<=1
    # for every p; it proves gamma>=ceil(sum_f y_f).
    loads=[0]*n
    total=0
    for start,ell,two in case['lower_dual_half_units_start_length_weight']:
        assert 0<=start<n and 1<=ell<=n-start and two>=1
        f=w[start:start+ell]
        total += two
        marked=[False]*n
        for j in range(n-ell+1):
            if w[j:j+ell]==f:
                for p in range(j,j+ell):marked[p]=True
        assert any(marked)
        for p in range(n):
            if marked[p]:loads[p]+=two
    assert max(loads)<=2, ('packing',n,max(loads))
    assert (total+1)//2 == v, ('lower_bound',n,total,v)
    print(f'length={n} optimum={v} substrings={total_factors} upper=OK lower={total}/2 ceiling={v} max_load={max(loads)}/2')

assert DATA['schema_version']==1
assert [x['length'] for x in DATA['cases']]==[2,4,8,16,32,64,128,256,512]
for case in DATA['cases']: verify(case)
print('ALL NINE EXACT VALUES CERTIFIED')
