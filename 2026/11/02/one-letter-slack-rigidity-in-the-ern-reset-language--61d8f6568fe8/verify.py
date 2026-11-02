#!/usr/bin/env python3
"""Exact subset-automaton checks for near-minimum reset words in the Cerny family."""
from collections import defaultdict


def transitions(n):
    size=1 << n
    a=[0]*size
    b=[0]*size
    for s in range(size):
        a[s]=((s << 1) & (size-1)) | (s >> (n-1))
        b[s]=(s & ~(1 << (n-1))) | (s >> (n-1))
    return a,b


def words(n):
    core=('a'*(n-1)+'b')
    shortest='b'+core*(n-2)
    candidates={'a'+shortest}
    for j in range(1,n-1):
        for t in range(n-1):
            if t != j:
                w='b'+core*(j-1)+'a'*t+'b'+'a'*(n-1-t)+'b'+core*(n-2-j)
                candidates.add(w)
    return shortest,candidates


def first_reset(n,w,a,b):
    s=(1<<n)-1
    for i,ch in enumerate(w):
        s=(a if ch=='a' else b)[s]
        if s.bit_count()==1:
            return i+1
    return None


def count_new_reset(n,length,a,b):
    d={(1<<n)-1:1}
    answers={}
    for k in range(1,length+1):
        nxt=defaultdict(int)
        hits=0
        for s,cnt in d.items():
            for trans in a,b:
                t=trans[s]
                if t.bit_count()==1:
                    hits+=cnt
                else:
                    nxt[t]+=cnt
        d=nxt
        answers[k]=hits
    return answers


def test():
    for n in range(2,12):
        a,b=transitions(n)
        L=(n-1)**2
        shortest,candidates=words(n)
        assert len(shortest)==L
        assert len(candidates)==(n-2)**2+1, (n,len(candidates))
        assert first_reset(n,shortest,a,b)==L
        for w in candidates:
            assert len(w)==L+1 and first_reset(n,w,a,b)==L+1,(n,w)
        answers=count_new_reset(n,L+1,a,b)
        assert sum(answers[k] for k in range(1,L))==0, n
        assert answers[L]==1, (n,answers[L])
        assert answers[L+1]==len(candidates), (n,answers[L+1])
        print(f'n={n}: shortest=1, first-at-next={answers[L+1]}, all-at-next={answers[L+1]+2}')
    print('VERIFY_OK')

if __name__ == '__main__':
    test()
