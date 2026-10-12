#!/usr/bin/env python3
"""Independent finite-instance checks for the finite-field burst-covering theorem."""
from itertools import permutations

def fmul(a,b,m,poly):
    n=1<<m; ans=0
    while b:
        if b&1: ans^=a
        b>>=1
        a<<=1
        if a&n:a^=poly
    return ans

def primitive_order(m,poly):
    q=1<<m
    a=1; seen=[]
    for _ in range(q-1):
        if a in seen: break
        seen.append(a)
        a=fmul(a,2,m,poly)
    assert a==1 and len(seen)==q-1, (m,poly,len(seen),a)
    return seen

def syndromes_from_windows(seq,b,cyclic=False):
    q=len(seq); s={0}
    for i in range(q if cyclic else q-b+1):
        w=[seq[(i+j)%q] for j in range(b)]
        for mask in range(1<<b):
            parity=mask.bit_count()&1
            x=0
            for j in range(b):
                if mask>>j&1: x^=w[j]
            s.add((parity<<(q.bit_length()-1)) | x)
    return s

def main():
    specs={2:0b111,3:0b1011,4:0b10011,5:0b100101,
           6:0b1000011,7:0b10000011,8:0b100011101}
    for m,poly in specs.items():
        q=1<<m
        seq=[0]+primitive_order(m,poly)
        assert len(seq)==q and len(set(seq))==q
        full=set(range(2*q))
        for cyclic in [False,True]:
            assert syndromes_from_windows(seq,3,cyclic)==full,(m,cyclic)
            assert syndromes_from_windows(seq,2,cyclic)!=full,(m,cyclic)
        labels_1={seq[i]^seq[i+1] for i in range(q-1)}
        labels_2={seq[i]^seq[i+2] for i in range(q-2)}
        assert labels_1|labels_2==set(range(1,q))
        assert len(labels_1)==q-2
        print(f'm={m} n={q}: q-2 adjacent differences; all q-1 covered within span 3, both boundary conventions')
    for m in (2,3):
        q=1<<m
        count=0
        for tail in permutations(range(1,q)):
            seq=(0,)+tail
            # These tests are equivalent to testing all orderings because translation
            # by the initial symbol preserves every pair difference.
            for cyclic in (False,True):
                labels={seq[i]^seq[i+1] for i in range(q-1)}
                if cyclic: labels.add(seq[-1]^seq[0])
                assert len(labels)!=q-1, (seq,cyclic)
            count+=1
        print(f'm={m}: all {count} translation-normalized orderings fail burst radius 2')
    print('VERIFY_OK')
if __name__=='__main__': main()
