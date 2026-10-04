#!/usr/bin/env python3
from math import isqrt

P_BOUND=200000
A_MAX=20

def primes_upto(n):
    bs=bytearray(b'\x01')*(n+1)
    if n>=0: bs[0]=0
    if n>=1: bs[1]=0
    for d in range(2,isqrt(n)+1):
        if bs[d]:
            bs[d*d:n+1:d]=b'\x00'*(((n-d*d)//d)+1)
    return [i for i in range(2,n+1) if bs[i]]

PR=primes_upto(P_BOUND)

def factor(n):
    out={}
    x=n
    for r in PR:
        if r*r>x: break
        if x%r==0:
            e=0
            while x%r==0:
                x//=r; e+=1
            out[r]=e
        if x==1: break
    if x>1: out[x]=out.get(x,0)+1
    return out

def addfac(a,b):
    c=dict(a)
    for p,e in b.items(): c[p]=c.get(p,0)+e
    return c

def ceildiv(x,y): return (x+y-1)//y

def super_index_for_2ap(a,p):
    A=a+1
    sf=addfac(factor((1<<A)-1), factor(p+1))
    tf=factor(2*A)
    nf={2:a,p:1}
    k=0
    for r,e in sf.items():
        et=tf.get(r,0)
        en=nf.get(r,0)
        if en==0:
            if e>et: return None
        else:
            k=max(k,ceildiv(max(0,e-et),en))
    return max(1,k)

hits=[]
for a in range(1,A_MAX+1):
    for p in PR:
        if p==2: continue
        k=super_index_for_2ap(a,p)
        if k is not None:
            hits.append((a,p,k))
expected=[]
for a in range(1,A_MAX+1):
    p=(1<<(a+1))-1
    if p<=P_BOUND and p in set(PR) and (a+1) in set(PR):
        expected.append((a,p,1))
assert hits==expected, (hits,expected)
print('VERIFY_OK a_max=%d p_bound=%d hits=%s' % (A_MAX,P_BOUND,hits))
