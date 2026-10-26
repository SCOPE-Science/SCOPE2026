#!/usr/bin/env python3
"""Exact small-field tests of evolution-algebra graph-balance spectra."""
from itertools import permutations, product
from math import gcd
from functools import reduce

def inv_mod(rows,q):
    n=len(rows)
    a=[[v%q for v in row]+[int(i==j) for j in range(n)] for i,row in enumerate(rows)]
    for k in range(n):
        piv=next((i for i in range(k,n) if a[i][k]%q),None)
        if piv is None:return None
        a[k],a[piv]=a[piv],a[k]
        t=pow(a[k][k],-1,q)
        a[k]=[(v*t)%q for v in a[k]]
        for i in range(n):
            if i==k:continue
            t=a[i][k]
            a[i]=[(x-t*y)%q for x,y in zip(a[i],a[k])]
    return [row[n:] for row in a]

def prod(a,b,m,q):
    n=m+1
    v=[0]*n
    for i in range(m):v[(i+1)%m]=(a[i]*b[i])%q
    return tuple(v)

def matmul(M,v,q):return tuple(sum(r[j]*v[j] for j in range(len(v)))%q for r in M)

def support_of_basis(B,m,q):
    n=m+1
    X=[[B[j][i] for j in range(n)] for i in range(n)]
    I=inv_mod(X,q)
    if I is None:return None
    for i in range(n):
        for j in range(i+1,n):
            if any(prod(B[i],B[j],m,q)):return None
    edges=set()
    for i in range(n):
        coeff=matmul(I,prod(B[i],B[i],m,q),q)
        for j,v in enumerate(coeff):
            if v:edges.add((i,j))
    return edges

def balance(n,edges):
    adj=[[] for _ in range(n)]
    for i,j in edges:
        adj[i].append((j,1)); adj[j].append((i,-1))
    h=[None]*n
    for s in range(n):
        if h[s] is None:
            h[s]=0; stack=[s]
            while stack:
                i=stack.pop()
                for j,w in adj[i]:
                    if h[j] is None:h[j]=h[i]+w;stack.append(j)
    return reduce(gcd,(abs(h[i]+1-h[j]) for i,j in edges),0)

def connected(n,edges):
    adj=[set() for _ in range(n)]
    for i,j in edges:adj[i].add(j);adj[j].add(i)
    seen={0};stack=[0]
    while stack:
        for j in adj[stack.pop()]:
            if j not in seen:seen.add(j);stack.append(j)
    return len(seen)==n

def exhaustive(m,q):
    n=m+1
    nonzero=list(product(range(q),repeat=n))[1:]
    observed=set(); connected_obs=set(); num=0
    for B in permutations(nonzero,n):
        edges=support_of_basis(B,m,q)
        if edges is None:continue
        num+=1; b=balance(n,edges); observed.add(b)
        if connected(n,edges):connected_obs.add(b)
    expected={d for d in range(1,m+1) if m%d==0}
    assert observed==expected,(m,q,num,observed,expected)
    assert connected_obs==expected,(m,q,num,connected_obs,expected)
    print(f'exhaustive m={m} q={q}: natural ordered bases={num}; all balances={sorted(observed)}; connected={sorted(connected_obs)}')

def constructed(m,S,q):
    n=m+1
    B=[]
    for i in range(m):
        row=[0]*n;row[i]=1;row[m]=int(i in S)%q
        B.append(tuple(row))
    B.append(tuple([0]*m+[1]))
    edges=support_of_basis(B,m,q)
    assert edges is not None
    b=balance(n,edges)
    pred=gcd(m,*[i-j for i in S for j in S])
    assert b==pred,(m,S,q,b,pred)
    return b

if __name__=='__main__':
    for m,q in [(2,2),(2,3),(3,2)]:exhaustive(m,q)
    for q in (2,3,5,7):
        for m in range(2,13):
            for d in range(1,m+1):
                if m%d==0:
                    S={0} if d==m else {0,d}
                    assert constructed(m,S,q)==d
    print('VERIFY_OK')
