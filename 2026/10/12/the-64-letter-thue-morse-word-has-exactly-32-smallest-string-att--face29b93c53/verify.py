#!/usr/bin/env python3
import itertools,json
from pathlib import Path

def tm(n):
    s='0'
    for _ in range(n):
        s=s+''.join('1' if c=='0' else '0' for c in s)
    return s

def covers_a(s):
    n=len(s);d={}
    for L in range(1,n+1):
        for i in range(n-L+1):
            f=s[i:i+L]
            d[f]=d.get(f,0)|(((1<<L)-1)<<i)
    return d

def covers_b(s):
    n=len(s);fs=set()
    for i in range(n):
        for j in range(i+1,n+1):fs.add(s[i:j])
    d={}
    for f in fs:
        L=len(f);m=0;st=0
        while True:
            i=s.find(f,st)
            if i<0:break
            m|=((1<<L)-1)<<i;st=i+1
        d[f]=m
    return d

def minimal_masks(d):
    ms=sorted(set(d.values()),key=lambda x:(x.bit_count(),x));out=[]
    for m in ms:
        if not any((x&m)==x for x in out):out.append(m)
    return out

def brute(ms,k,n):
    out=[]
    for C in itertools.combinations(range(n),k):
        z=sum(1<<p for p in C)
        if all(z&m for m in ms):out.append(C)
    return out

def recursive(ms,k,n):
    ms=tuple(sorted(set(ms),key=lambda x:(x.bit_count(),x)));out=set()
    def rec(chosen,unhit):
        new=[m for m in unhit if not any((m>>p)&1 for p in chosen)]
        if not new:
            if len(chosen)==k:out.add(tuple(sorted(chosen)))
            return
        if len(chosen)==k:return
        m=min(new,key=int.bit_count)
        for p in range(n):
            if (m>>p)&1 and p not in chosen:rec(chosen+(p,),new)
    rec(tuple(),ms)
    return sorted(out)

root=Path(__file__).resolve().parent
C=json.loads((root/'certificate.json').read_text(encoding='utf-8'))
s=tm(6);assert s==C['word'] and len(s)==64
D1=covers_a(s);D2=covers_b(s);assert D1==D2
M=minimal_masks(D1);assert len(M)==C['inclusion_minimal_cover_masks']
A3=brute(M,3,64);assert A3==[]
A4=brute(M,4,64);assert len(A4)==32
B4=recursive(D1.values(),4,64);assert B4==A4
formula=[]
for e in itertools.product((0,1),repeat=4):
    formula.append(tuple(sorted((15+e[0],23+e[1],31+e[2],47+e[3]))))
    formula.append(tuple(sorted((15+e[0],31+e[1],39+e[2],47+e[3]))))
formula=sorted(set(formula));assert formula==A4
assert [[p+1 for p in x] for x in A4]==C['all_attractors_1_based']
# Reflection p -> 65-p on 1-based positions exchanges the two formula families.
S=set(A4)
for x in A4:
    y=tuple(sorted(63-p for p in x))
    assert y in S
print('VERIFY_OK t6_length=64 factors=%d min_size=4 size3_count=0 size4_count=32 families=16+16 cover_engines=2 enumeration_engines=2 reflection_closed=1' % len(D1))
