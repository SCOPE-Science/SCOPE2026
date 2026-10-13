#!/usr/bin/env python3
from fractions import Fraction
from math import factorial
from itertools import product

N = 12

def add(a,b):
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(N+1)]

def scale(a,c):
    return [x*c for x in a]

def mul(a,b):
    out=[Fraction(0) for _ in range(N+1)]
    for i,x in enumerate(a[:N+1]):
        if not x: continue
        for j,y in enumerate(b[:N+1-i]):
            if y: out[i+j]+=x*y
    return out

def shift(a,k=1):
    return [Fraction(0)]*k + a[:N+1-k]

def exp_series(a):
    # a[0]=0; recurrence for f=exp(a): n f_n = sum_{k=1}^n k a_k f_{n-k}
    assert a[0] == 0
    f=[Fraction(0) for _ in range(N+1)]
    f[0]=1
    for n in range(1,N+1):
        f[n]=sum(Fraction(k)*a[k]*f[n-k] for k in range(1,n+1))/n
    return f

one=[Fraction(0) for _ in range(N+1)]; one[0]=1
# Formal fixed-point iteration is coefficient-stable because the RHS is multiplied by x.
L=[Fraction(0) for _ in range(N+1)]
for _ in range(N+2):
    eL=exp_series(L)
    H=shift(add(add(eL, scale(one,-1)), scale(L,-1)))
    P=add(L,H)
    L=shift(add(one,P))
eL=exp_series(L)
H=shift(add(add(eL, scale(one,-1)), scale(L,-1)))
P=add(L,H)
P2=mul(P,P); L2=mul(L,L); LH=mul(L,H)
low_root=shift(add(add(one,P), scale(P2,Fraction(1,2))))
high_inside=add(add(add(eL,scale(one,-1)),scale(L,-1)),scale(L2,Fraction(-1,2)))
high_root=shift(high_inside)
Tbullet=add(low_root,high_root)
U=add(add(Tbullet,scale(L2,Fraction(-1,2))),scale(LH,-1))
F=exp_series(U)

def labeled(a):
    out=[]
    for n,c in enumerate(a):
        v=c*factorial(n)
        assert v.denominator==1
        out.append(v.numerator)
    return out

Ulab=labeled(U)
Flab=labeled(F)
EXPECTED_U=[0,1,1,3,16,125,1206,13867,188504,2972097,53238250,1067540771,23711808132]
EXPECTED_F=[1,1,2,7,38,291,2842,33391,459748,7288273,130922666,2629437009,58418631196]
assert Ulab==EXPECTED_U, (Ulab,EXPECTED_U)
assert Flab==EXPECTED_F, (Flab,EXPECTED_F)

# Independent brute-force check for labeled trees via Prüfer codes.
def tree_from_prufer(seq):
    n=len(seq)+2
    deg=[1]*n
    for x in seq: deg[x]+=1
    edges=[]
    for x in seq:
        leaf=next(i for i,d in enumerate(deg) if d==1)
        edges.append((leaf,x)); deg[leaf]-=1; deg[x]-=1
    leaves=[i for i,d in enumerate(deg) if d==1]
    edges.append(tuple(leaves))
    return edges

def admissible(n,edges):
    deg=[0]*n
    for u,v in edges: deg[u]+=1; deg[v]+=1
    return all(not (deg[u]>2 and deg[v]>2) for u,v in edges)

brute_t=[0,1]
for n in range(2,8):
    c=0
    for seq in product(range(n), repeat=n-2):
        e=tree_from_prufer(seq)
        c += admissible(n,e)
    brute_t.append(c)
assert brute_t==EXPECTED_U[0:8]

# Independent brute-force check for labeled forests by scanning all simple graphs through n=6.
def is_forest_admissible(n,mask):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    parent=list(range(n)); rank=[0]*n; deg=[0]*n; edges=[]
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a==b: return False
        if rank[a]<rank[b]: a,b=b,a
        parent[b]=a
        if rank[a]==rank[b]: rank[a]+=1
        return True
    for k,(u,v) in enumerate(pairs):
        if (mask>>k)&1:
            if not union(u,v): return False
            deg[u]+=1; deg[v]+=1; edges.append((u,v))
    return all(not (deg[u]>2 and deg[v]>2) for u,v in edges)

brute_f=[]
for n in range(0,7):
    m=n*(n-1)//2
    brute_f.append(sum(is_forest_admissible(n,mask) for mask in range(1<<m)))
assert brute_f==EXPECTED_F[:7]

print('connected:', Ulab[1:13])
print('forests:', Flab[:13])
print('brute_trees_n<=7:', brute_t[1:])
print('brute_forests_n<=6:', brute_f)
print('VERIFY_OK')
