#!/usr/bin/env python3
"""Finite consistency checks for the dyadic-offset period-doubling lift theorem."""
from collections import Counter

def valuation_2(n):
    assert n > 0
    return (n & -n).bit_length()-1

def pd_word(size):
    word = bytearray(size)
    word[0] = 1
    for j in range(1, size):
        word[j] = 1 if j % 2 == 0 else 1-word[j//2]
    assert all(v == 1-(valuation_2(j+1)%2) for j,v in enumerate(word))
    return word

def run():
    N = 1 << 15
    word = pd_word(N)
    txt = bytes(48 + j for j in word)
    validations = 0
    for r in (1,2,3,4):
        D = 1 << r
        for n in range(r+2, 10):
            B = 1 << (n-1)
            pattern = txt[:(1<<n)-1]
            poses = []
            p = 0
            while True:
                p = txt.find(pattern, p)
                if p < 0: break
                poses.append(p);p += 1
            assert poses[0] == 0 and len(poses)>10
            for s in poses:
                assert s % B == 0 and word[s//B] == 1
            distances = Counter()
            for s,e in zip(poses, poses[1:]):
                L=e-s
                assert L in (B,2*B), (r,n,s,e,L)
                distances[L]+=1
                for j in range(D):
                    v = 0
                    for h in range(L//D):
                        v ^= word[s+j+h*D]
                    assert v == int(j==D-1), (r,n,s,L,j,v)
                validations += 1
            assert all(distances[q]>0 for q in (B,2*B)), (r,n,distances)
            print('r=%d offset=%d n=%d occurrences=%d return_lengths=%s full_translation=e_%d' % (r,D,n,len(poses),str(sorted(distances)),D-1))
    print('PASS %d return intervals independently checked; all exact finite tests passed' % validations)

if __name__ == '__main__': run()
