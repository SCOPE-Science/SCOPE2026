#!/usr/bin/env python3
"""Exact rational Farkas verification of the theta-graph four-point bound.

Reads theta_dual_certificates.json.gz in the same directory. Only Python's
standard library is needed. No finite sampling and no optimization solver is
used during verification.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from pathlib import Path
import gzip, json

N=6

def unit(i):
    return tuple(F(int(j==i)) for j in range(N))
def const(c):
    return tuple(F(c if i==5 else 0) for i in range(N))
def add(*xs):
    return tuple(sum(x[i] for x in xs) for i in range(N))
def neg(x):return tuple(-v for v in x)
def sub(x,y):return add(x,neg(y))
def scale(t,x):return tuple(F(t)*v for v in x)

X=[unit(i) for i in range(4)]
T=unit(4)
ONE=const(1)
ZERO=const(0)

def d_options(i,j,edges):
    a,b=edges[i],edges[j]
    u,v=X[i],X[j]
    La=T if a==2 else ONE
    Lb=T if b==2 else ONE
    if a==b:
        diff=sub(v,u)  # points are ordered within every path
        if a==2:return (diff,)
        return (diff,sub(add(ONE,T),diff))
    if a!=2 and b!=2:
        return (add(u,v),sub(add(La,Lb),add(u,v)),add(u,sub(Lb,v),T),add(sub(La,u),v,T))
    return (add(u,v),sub(add(La,Lb),add(u,v)))

PAIRS=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))

def sum_options(k,edges):
    (i,j),(a,b)=PAIRS[k]
    return sorted(set(add(u,v) for u in d_options(i,j,edges) for v in d_options(a,b,edges)))

def assignments():
    for edges in combinations_with_replacement(range(3),4):
        mirror=tuple(sorted((1 if e==0 else 0 if e==1 else 2) for e in edges))
        if edges<=mirror:
            yield edges

def intervals():
    return [(F(0),F(1,3),add(scale(F(1,4),ONE),scale(F(1,4),T))),
            (F(1,3),F(1,2),T),
            (F(1,2),F(1),scale(F(1,2),ONE))]

def make_rows(edges,lo,hi,k,cj,ch,options):
    # Each inequality is A(row) . (x0,x1,x2,x3,s,z,w) <= b
    rows=[]
    for i,e in enumerate(edges):
        a=[F(0)]*7; a[i]=-1;rows.append((tuple(a),F(0)))
        a=[F(0)]*7;a[i]=1
        if e==2:a[4]=-1; rhs=F(0)
        else:rhs=F(1)
        rows.append((tuple(a),rhs))
    a=[F(0)]*7;a[4]=-1;rows.append((tuple(a),-lo))
    a=[F(0)]*7;a[4]=1;rows.append((tuple(a),hi))
    for i in range(3):
        if edges[i]==edges[i+1]:
            a=[F(0)]*7;a[i]=1;a[i+1]=-1;rows.append((tuple(a),F(0)))
    for opt in options[k]:
        rows.append((tuple(-v for v in opt[:5])+(F(1),F(0)),opt[5]))
    g=next(g for l,h,g in intervals() if l==lo and h==hi)
    for c in (cj,ch):
        rows.append((tuple(c[i]+2*g[i] for i in range(5))+(F(-1),F(1)),-c[5]-2*g[5]))
    return rows

def instance_iterator():
    for edges in assignments():
        options=tuple(sum_options(k,edges) for k in range(3))
        for lo,hi,g in intervals():
            for k in range(3):
                j,h=(i for i in range(3) if i!=k)
                for cj,ch in product(options[j],options[h]):
                    yield edges,lo,hi,k,cj,ch,options

def verify():
    p=Path(__file__).with_name('theta_dual_certificates.json.gz')
    with gzip.open(p,'rt',encoding='utf-8') as f:
        cert=json.load(f)
    count=0
    for data,sp in zip(instance_iterator(),cert['duals']):
        A=make_rows(*data)
        vec=[F(0)]*7; objective=F(0)
        for idx,num,den in sp:
            lam=F(num,den)
            assert lam>=0
            assert 0<=idx<len(A)
            row,rhs=A[idx]
            for i in range(7):vec[i]+=lam*row[i]
            objective+=lam*rhs
        assert vec==[F(0)]*6+[F(1)],(count,'dual equality')
        assert objective<=0,(count,'dual upper bound',objective)
        count+=1
    assert count==cert['count']==sum(1 for _ in instance_iterator())==len(cert['duals'])
    print('PASS:',count,'exact rational LP dual certificates; complete continuous parameter domain')
    print('No floating-point tolerance used in the certificate check.')

if __name__=='__main__':verify()
