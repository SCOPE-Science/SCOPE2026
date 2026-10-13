#!/usr/bin/env python3
"""Exact integer-arithmetic verification of a nine-column four-request batch code."""
import json
import itertools
from collections import Counter
from pathlib import Path

def verify():
    data = json.loads(Path(__file__).with_name('certificates.json').read_text(encoding='utf-8'))
    cols = data['columns']
    assert len(cols) == 9 and all(len(c) == 4 for c in cols)
    assert cols[:4] == [[1 if r == j else 0 for r in range(4)] for j in range(4)]
    assert cols[4:] == [[1,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,1],[1,1,1,1]]
    assert len(data['all_equal']) == 9 and len(data['two_pairs']) == 36
    def mask_and_identity(rep,target):
        assert rep, 'Empty recovery set is forbidden'
        used = set()
        sums = [0]*4
        for j,a in rep:
            assert type(j) is int and type(a) is int and 1<=j<=9 and a in (-1,1)
            assert j not in used
            used.add(j)
            for r in range(4):sums[r] += a * cols[j-1][r]
        assert sums == cols[target-1], (target,rep,sums)
        return used
    def check_bundle(reps,targets):
        assert len(reps)==len(targets)==4
        used=set()
        for rep,target in zip(reps,targets):
            mask=mask_and_identity(rep,target)
            assert not (used & mask)
            used |= mask
    for i in range(1,10):
        check_bundle(data['all_equal'][str(i)],[i]*4)
    for i,j in itertools.combinations(range(1,10),2):
        check_bundle(data['two_pairs'][f'{i},{j}'],[i,i,j,j])
    # Independently exercise every one of the C(12,4)=495 requested multisets.
    for req in itertools.combinations_with_replacement(range(1,10),4):
        counts=Counter(req)
        multiplicities=sorted(counts.values(),reverse=True)
        if multiplicities==[4]:
            reps=data['all_equal'][str(req[0])]
            targets=list(req)
        elif multiplicities==[2,2]:
            i,j=sorted(counts)
            reps=data['two_pairs'][f'{i},{j}']
            targets=[i,i,j,j]
        elif multiplicities in ([3,1],[2,1,1]):
            i=next(x for x,n in counts.items() if n>1)
            unique=[x for x,n in counts.items() if n==1]
            avoid=set(unique)
            pool=[]
            for rep in data['all_equal'][str(i)]:
                if not any(j in avoid for j,a in rep):pool.append(rep)
            assert len(pool)>=counts[i]
            reps=pool[:counts[i]]+[[[x,1]] for x in unique]
            targets=[i]*counts[i]+unique
        else:
            assert multiplicities==[1,1,1,1]
            reps=[[[x,1]] for x in req]
            targets=list(req)
        check_bundle(reps,targets)
    print('VERIFY_OK: 9 column targets, 36 two-pair targets, all 495 request multisets, exact integer identities')

if __name__=='__main__': verify()
