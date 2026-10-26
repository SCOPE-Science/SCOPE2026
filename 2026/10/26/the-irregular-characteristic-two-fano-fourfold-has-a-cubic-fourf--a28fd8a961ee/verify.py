#!/usr/bin/env python3
"""Finite-field point-count consistency checks for the cubic Y."""
from collections import Counter

def mul(a,b,mod,degree):
    z=0
    while b:
        if b&1: z^=a
        b >>=1
        a <<=1
        if a&(1<<degree): a^=mod
    return z

def count(qdeg,mod):
    q=1<<qdeg
    freq=Counter()
    for x in range(q):
        for y in range(q):
            x2=mul(x,x,mod,qdeg)
            y2=mul(y,y,mod,qdeg)
            v=mul(x2,y,mod,qdeg)^mul(x,y2,mod,qdeg)
            freq[v]+=1
    conv={0:1}
    for _ in range(3):
        conv2=Counter()
        for a,na in conv.items():
            for b,nb in freq.items(): conv2[a^b]+=na*nb
        conv=conv2
    ans=(conv[0]-1)//(q-1)
    base=sum(q**i for i in range(5))
    predicted=base+(8 if qdeg%2 else 22)*q*q
    assert (conv[0]-1)%(q-1)==0
    assert ans==predicted,(qdeg,ans,predicted)
    print(f'q=2^{qdeg}={q}; pair value counts={sorted(freq.items())}; #Y={ans}; expected={predicted}')
for degree,mod in [(1,0b11),(2,0b111),(3,0b1011),(4,0b10011)]: count(degree,mod)
print('CUBIC_ZETA_CHECKS_OK')
