#!/usr/bin/env python3
from itertools import product

def add(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return c

def sub(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]-=v
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def shift(a,k): return [0]*k+a

def ppower(base,n):
    out=[1]
    for _ in range(n): out=mul(out,base)
    return out

def blade(m):
    A=ppower([1,1,1,1],m)
    one=ppower([1,1],m)
    xm=[0]*m+[1]
    B=add(sub(A,one),xm)
    prev=sub(ppower([1,1],m-1),[0]*(m-1)+[1])
    badone=shift([m*v for v in prev],2)
    C=sub(sub(A,one),badone)
    return A,B,C

def predicted(profile):
    PA=PB=PC=[1]
    for m in profile:
        A,B,C=blade(m)
        PA=mul(PA,A); PB=mul(PB,B); PC=mul(PC,C)
    return add(add(shift(PA,3),shift(PB,2)),mul([1,1],PC))

def graph(profile):
    # vertex 0 is center; each later range is a clique blade.
    N=1+sum(profile)
    adj=[set() for _ in range(N)]
    blades=[]; start=1
    for m in profile:
        B=list(range(start,start+m)); blades.append(B); start+=m
        for v in B:
            adj[0].add(v); adj[v].add(0)
        for i,u in enumerate(B):
            for v in B[i+1:]:
                adj[u].add(v); adj[v].add(u)
    return adj

def is_drdf(labels,adj):
    for v,a in enumerate(labels):
        if a==0:
            if any(labels[u]==3 for u in adj[v]): continue
            if sum(labels[u]==2 for u in adj[v])>=2: continue
            return False
        if a==1 and not any(labels[u]>=2 for u in adj[v]):
            return False
    return True

profiles=[(2,2),(2,3),(3,3),(2,2,2),(2,2,3),(2,3,3)]
labelings=feasible=coefficient_checks=minimum_checks=0
max_order=0
for prof in profiles:
    adj=graph(prof); N=len(adj); max_order=max(max_order,N)
    coeff=[0]*(3*N+1)
    for lab in product(range(4), repeat=N):
        labelings+=1
        if is_drdf(lab,adj):
            feasible+=1; coeff[sum(lab)]+=1
    while len(coeff)>1 and coeff[-1]==0: coeff.pop()
    pred=predicted(prof)
    assert coeff==pred, (prof,coeff,pred)
    coefficient_checks+=len(pred)
    mw=next(i for i,v in enumerate(coeff) if v)
    assert mw==3 and coeff[mw]==1
    minimum_checks+=1
print(f"VERIFY_OK profiles={len(profiles)} labelings={labelings} feasible={feasible} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order={max_order}")
