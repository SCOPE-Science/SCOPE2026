#!/usr/bin/env python3
"""Checks oriented reduced Lefschetz traces of page-permutation/reflection symmetries."""
import itertools,collections,math
from pentabook_verify import masks

def action_map(n,perm,flip):
    p=[0]*(4*n+1);p[0]=0
    for i in range(n):
        for j in range(4):
            p[1+4*i+j]=1+4*perm[i]+((3-j) if flip else j)
    return p

def character(n,faces,p):
    total=0
    for f in faces:
        image=0; bit=f
        while bit:
            b=bit&-bit;bit-=b;image |=1<<p[b.bit_length()-1]
        if image!=f:continue
        orbs=0;done=0;bit=f
        while bit:
            b=bit&-bit; bit-=b
            if done&b:continue
            orbs+=1;j=b.bit_length()-1
            while not(done & (1<<j)):
                done|=1<<j;j=p[j]
        total += (-1)**orbs
    return (-1)**(n+1)*total

def sign(p):
    x=0
    for i in range(len(p)):
      for j in range(i+1,len(p)):x+=(p[i]>p[j])
    return (-1)**x

def ctype(p):
    unseen=set(range(len(p)));sizes=[]
    while unseen:
      a=next(iter(unseen)); cur=a;L=0
      while cur in unseen:
        unseen.remove(cur);cur=p[cur];L+=1
      sizes.append(L)
    return tuple(sorted(sizes))

def verify(n):
    f=masks(n); data={}
    for p in itertools.permutations(range(n)):
        for flip in (0,1):
            val=character(n,f,action_map(n,p,flip));key=(ctype(p),flip)
            if key in data: assert val==data[key],(n,key,val,data[key])
            data[key]=val
            expected=sign(p)*sum(i==p[i] for i in range(n)) * ((-1)**(n*flip))
            assert val==expected,(n,p,flip,val,expected)
    return data

if __name__=='__main__':
    for n in range(1,6):
        dat=verify(n);print('CHAR_OK',n, sorted(dat.items()),flush=True)
