#!/usr/bin/env python3
"""Finite 2-truncated color multiplicity certificate for 4-state threshold-2 GHM on K_{a,b}."""
from itertools import product
from collections import Counter
import csv, sys

def advance(A, B):
    trigger_A = sum(x == 1 for x in B) >= 2
    trigger_B = sum(x == 1 for x in A) >= 2
    def one(side, trigger):
        return tuple((x + 1) % 4 if x else (1 if trigger else 0) for x in side)
    return one(A,trigger_A), one(B,trigger_B)

def kind(A,B):
    def ct(T):return tuple(T.count(c) for c in range(4))
    ca, cb = ct(A),ct(B)
    if all(x==0 for x in A+B):return 'zero'
    if (ca[0]>=2 and ca[2]>=2 and ca[1]==ca[3]==0 and
        cb[1]>=2 and cb[3]>=2 and cb[0]==cb[2]==0):return 'alternate'
    if (cb[0]>=2 and cb[2]>=2 and cb[1]==cb[3]==0 and
        ca[1]>=2 and ca[3]>=2 and ca[0]==ca[2]==0):return 'alternate'
    if min(ca)>=2 and min(cb)>=2:return 'full'
    return 'other'

if __name__=='__main__':
    hist=Counter(); periodic_types=Counter();max_examples=[]; signatures=[]
    for mult in product(range(3), repeat=8):
        A=tuple(c for c in range(4) for _ in range(mult[c]));B=tuple(c for c in range(4) for _ in range(mult[c+4]))
        trajectory=[(A,B)]
        for t in range(11): trajectory.append(advance(*trajectory[-1]))
        H=next(i for i in range(8) if trajectory[i]==trajectory[i+4])
        assert trajectory[7]==trajectory[11], ('global-identity',mult)
        hist[H]+=1
        if H==7:max_examples.append((mult,A,B))
        p=1 if kind(*trajectory[H])=='zero' else 4
        signatures.append((mult,H,p))
        if trajectory[0]==trajectory[4]:
            k=kind(A,B)
            assert k!='other',('other-periodic',mult)
            assert (trajectory[0]==trajectory[1]) == (k=='zero')
            assert (trajectory[0]==trajectory[2]) == (k=='zero')
            periodic_types[k]+=1
        else:assert kind(A,B)=='other',('false-periodic',mult)
    print('cap-patterns',3**8,'first-entry',sorted(hist.items()))
    print('periodic-types',sorted(periodic_types.items()))
    print('sharp-example', max_examples[0]); print('sharp-count',len(max_examples))
    assert max(hist)==7 and len(max_examples)==2
    def feasible(caps,n):
        m=sum(caps)
        return n>=m if 2 in caps else n==m
    def exact_max(a,b):
        return max(h for cap,h,p in signatures if feasible(cap[:4],a) and feasible(cap[4:],b))
    for a in range(2,9):
        for b in range(2,9):
            lo,hi=sorted((a,b))
            expected = (4 if a==b==2 else (5 if lo==2 or (a==b==3) else
                        (7 if lo>=7 and hi>=8 else 6)))
            assert exact_max(a,b)==expected,(a,b,exact_max(a,b),expected)
    print('entrance-phase-diagram PASS: sizes >=8 reduce to the 8 class')
    if len(sys.argv)>1:
        with open(sys.argv[1],'w',encoding='utf-8',newline='') as f:
            w=csv.writer(f)
            w.writerow(['cap_A_0123','cap_B_0123','first_entry','eventual_period'])
            for cap,h,p in signatures:
                w.writerow([''.join(map(str,cap[:4])),''.join(map(str,cap[4:])),h,p])
        print('certificate table written:',len(signatures),'data rows')
    print('CERTIFICATE PASS: F^11=F^7, sharp entrance diagram, and only zero, alternating and full periodic families')
