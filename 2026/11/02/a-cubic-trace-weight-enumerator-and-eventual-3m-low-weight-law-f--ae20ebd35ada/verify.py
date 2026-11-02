#!/usr/bin/env python3
"""Exact, dependency-free consistency checks for wheel graph-state SLD."""
from collections import Counter
from math import comb

# Polynomials in t, stored as coefficient vectors.
def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def add(a,b):
    return trim([ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return trim(r)

def scale(a,k):return trim([k*x for x in a])

def sub(a,b):return add(a,scale(b,-1))

def pow3trace(m,a,c):
    # p(lambda)=lambda^3-a*lambda^2+c; S0=3, S1=a, S2=a^2.
    p=[ [3],a,mul(a,a)]
    for j in range(3,m+1): p.append(sub(mul(a,p[j-1]),mul(c,p[j-3])))
    return p[m]

def transfer_enumerator(m):
    t=[0,1]; one=[1]
    sa=pow3trace(m,add(one,t),sub(t,[0,0,0,1]))
    sb=pow3trace(m,sub(one,t),sub([0,0,0,1],t))
    sc=pow3trace(m,scale(t,2),sub([0,0,0,1],t))
    num=add(add(mul(add(one,t),sa),mul(sub(one,t),sb)),scale(mul(t,sc),2))
    assert all(v%2==0 for v in num)
    return trim([v//2 for v in num])

def direct_enumerator(m):
    # Independent direct symplectic support count, hub at position 0.
    result=[0]*(m+2)
    adj=[sum(1<<(i+1) for i in range(m))]
    for i in range(m):
        adj.append((1<<0)|(1<<((i-1)%m+1))|(1<<((i+1)%m+1)))
    for mask in range(1<<(m+1)):
        zmask=0
        for j,a in enumerate(adj):
            if (mask>>j)&1:zmask ^= a
        support=(mask|zmask).bit_count()
        result[support]+=1
    return trim(result)

# Two independent exact methods, all 14, 12, ... vertex powers of 2.
for m in range(3,15):
    trans=transfer_enumerator(m)
    direct=direct_enumerator(m)
    assert trans==direct,(m,trans,direct)
    assert sum(trans)==(1<<(m+1))
    assert trans[0]==1 and trans[1]==0

# The analytically derived coefficient identities from the rational series.
A2={3:6,4:2}
A3={4:8,6:3}
A4extra={4:1,5:30,6:11,7:21,8:2,9:3}
for m in range(3,111):
    a=transfer_enumerator(m)
    assert a[2]==A2.get(m,0),(m,'A2',a[2])
    assert a[3]==A3.get(m,0),(m,'A3',a[3])
    assert a[4]==3*m+A4extra.get(m,0),(m,'A4',a[4])
    assert sum(a)==1<<(m+1)

# Distinct exact examples; the six-vertex wheel is 3-uniform.
assert transfer_enumerator(5)[1:4]==[0,0,0]
assert transfer_enumerator(6)[3]==3
assert transfer_enumerator(10)[4]==30
print('VERIFY_OK: independent exhaustive graph support through 15 vertices; exact cubic recurrences through rim length 110; low sectors and normalization checked')
