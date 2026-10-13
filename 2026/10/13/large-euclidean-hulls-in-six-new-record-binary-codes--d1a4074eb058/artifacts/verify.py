#!/usr/bin/env python3
from pathlib import Path
from functools import reduce
from collections import Counter
import json

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/'artifacts'/'certificate.json').read_text(encoding='utf-8'))

def pmul(a,b):
    r=0
    while b:
        if b&1:r^=a
        b>>=1;a<<=1
    return r

def pdiv(a,b):
    q=0;db=b.bit_length()-1
    while a and a.bit_length()-1>=db:
        s=a.bit_length()-1-db
        q^=1<<s;a^=b<<s
    return q,a

def poly(exps):
    z=0
    for e in exps:z^=1<<e
    return z

def build(m,hfactors,fs,tails):
    h=1
    for f in hfactors:h=pmul(h,poly(f))
    k=h.bit_length()-1
    g,rem=pdiv((1<<m)|1,h)
    assert rem==0
    mask=(1<<m)-1
    base=[]
    for f in fs:
        p=pmul(g,poly(f))
        while p.bit_length()-1>=m:
            d=p.bit_length()-1
            p^=1<<d;p^=1<<(d-m)
        base.append(p)
    rows=[]
    for j in range(k):
        z=0;off=0
        for p in base:
            q=((p<<j)&mask)^(p>>(m-j) if j else 0)
            z|=q<<off;off+=m
        for t in tails:
            bit=1 if t=='all' else int(t[j%5])
            if bit:z|=1<<off
            off+=1
        rows.append(z)
    return rows,off

def rank_bits(rows,n):
    A=[x for x in rows if x]
    rr=0
    for c in range(n):
        p=next((i for i in range(rr,len(A)) if (A[i]>>c)&1),None)
        if p is None:continue
        A[rr],A[p]=A[p],A[rr]
        for i in range(len(A)):
            if i!=rr and ((A[i]>>c)&1):A[i]^=A[rr]
        rr+=1
    return rr

def nullspace(rows,n):
    A=[x for x in rows if x]
    rr=0;piv=[]
    for c in range(n):
        p=next((i for i in range(rr,len(A)) if (A[i]>>c)&1),None)
        if p is None:continue
        A[rr],A[p]=A[p],A[rr]
        for i in range(len(A)):
            if i!=rr and ((A[i]>>c)&1):A[i]^=A[rr]
        piv.append(c);rr+=1
    free=[c for c in range(n) if c not in piv]
    B=[]
    for f in free:
        x=1<<f
        for i,c in enumerate(piv):
            if (A[i]&x).bit_count()&1:x|=1<<c
        B.append(x)
    return B

def enumerate_min(rows):
    if not rows:return None,None
    cur=0;prev=0;mn=10**9;cnt=0
    for t in range(1,1<<len(rows)):
        gray=t^(t>>1);diff=gray^prev;j=(diff&-diff).bit_length()-1
        cur^=rows[j];prev=gray
        w=cur.bit_count()
        if w<mn:mn=w;cnt=1
        elif w==mn:cnt+=1
    return mn,cnt

codes=[
('172',85,[[1,0],[4,3,2,1,0],[8,6,5,4,3,1,0],[8,7,5,1,0]],[[0],[13,11,9,6,4,3,2,1,0]],['all','all']),
('173',85,[[4,3,2,1,0],[8,5,4,3,2,1,0],[8,7,6,5,4,3,0]],[[0],[15,11,6,3,2,0]],['01001','10100','01010']),
('176',85,[[1,0],[4,3,2,1,0],[8,6,5,4,3,1,0],[8,7,5,1,0]],[[0],[13,11,9,6,4,3,2,1,0]],['01111','11111','11111','10010','11011','00101']),
('181',85,[[1,0],[4,3,2,1,0],[8,5,4,3,2,1,0],[8,7,3,1,0]],[[0],[13,10,7,6,4,3,0]],['11000','10100','11100','01010','01110','10001','11101','00011','10011','00111','01111']),
('184',85,[[1,0],[4,3,2,1,0],[8,6,5,4,2,1,0],[8,7,5,4,3,2,0]],[[0],[13,9,8,7,6,5,3,1,0]],['11001','01001','00101','11101','11110','00111','11100','01010','10010','10001','11111','01110','10011','00110']),
('189',63,[[1,0],[3,2,0],[6,5,0],[6,5,3,2,0],[6,5,4,2,0]],[[0],[14,13,12,9,7,5,3,2,0],[16,14,13,10,7,1,0]],[]),
]

for spec,data in zip(codes,CERT['codes']):
    name,m,hf,fs,tails=spec
    rows,n=build(m,hf,fs,tails)
    assert [n,len(rows)]==data['parameters'][:2]
    assert rank_bits(rows,n)==len(rows)
    pd,pa=enumerate_min(rows)
    assert (pd,pa)==(data['parameters'][2],data['published_Ad'])
    gram=[]
    for i in range(len(rows)):
        z=0
        for j in range(len(rows)):
            if (rows[i]&rows[j]).bit_count()&1:z|=1<<j
        gram.append(z)
    gr=rank_bits(gram,len(rows))
    assert len(rows)-gr==data['hull_dimension']
    ker=nullspace(gram,len(rows))
    assert len(ker)==data['hull_dimension']
    hrows=[]
    for coeff in ker:
        z=0
        for i in range(len(rows)):
            if (coeff>>i)&1:z^=rows[i]
        hrows.append(z)
    assert rank_bits(hrows,n)==data['hull_dimension']
    hd,ha=enumerate_min(hrows)
    assert (hd,ha)==(data['hull_minimum_distance'],data['hull_Amin'])

assert CERT['gram_ranks']==[4,18,1,2,0,1]
print('VERIFY_OK')
