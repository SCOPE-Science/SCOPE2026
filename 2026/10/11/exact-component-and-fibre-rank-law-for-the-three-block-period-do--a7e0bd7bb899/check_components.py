#!/usr/bin/env python3
"""Finite sanity checks for return words and subgroup indices; not an infinite proof."""
from math import gcd

def substitute(word):
    return ''.join('10' if c == '1' else '11' for c in word)

def subgroup(k, v, w):
    return {((a*v[0]+b*w[0]) % k, (a*v[1]+b*w[1]) % k)
            for a in range(k) for b in range(k)}

tau = ['1']
for _ in range(17):
    tau.append(substitute(tau[-1]))
word = tau[-1]
for n in range(2, 10):
    length = 2**n-1
    prefix = word[:length]
    pos = [i for i in range(len(word)-length+1) if word.startswith(prefix,i)]
    pairs = {(pos[j+1]-pos[j], word[pos[j]:pos[j+1]])
             for j in range(len(pos)-1)}
    assert pairs == {(2**(n-1),tau[n-1]),(2**n,tau[n])}, (n,pairs)
    sm = (2**n + (-1)**(n-1))//3
    sn = (2**(n+1) + (-1)**n)//3
    v = (2**(n-1), 2**(n-1)-sm)
    w = (2**n, 2**n-sn)
    det = v[0]*w[1] - v[1]*w[0]
    assert abs(det) == 2**(n-1)
    for k in range(2, 18):
        h = subgroup(k,v,w)
        assert k*k//len(h) == gcd(k,2**(n-1)), (n,k,len(h))
print('Finite return lengths and Smith-index tests passed for n=2..9, k=2..17.')
