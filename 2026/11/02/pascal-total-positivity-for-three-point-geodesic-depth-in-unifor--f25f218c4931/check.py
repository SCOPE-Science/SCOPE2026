#!/usr/bin/env python3
"""Exact finite checks for a three-point geodesic distribution in uniform labeled trees.

Standard library only; enumeration checks finite cases, not the infinite proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product, combinations
from math import factorial, comb

CHECKS = 0

def check(predicate, context):
    global CHECKS
    CHECKS += 1
    if not predicate:
        raise AssertionError(context)

def falling(k, h):
    if h < 0 or k < h:
        return 0
    z = 1
    for j in range(h):
        z *= k-j
    return z

def tail(n, d, h):
    if h == 0:
        return Fraction(1)
    return Fraction(falling(n-d-1, h), (n-2)*n**(h-1))

def mass(n, d, h):
    return tail(n,d,h)-tail(n,d,h+1)

def edges_from_prufer(code, n):
    deg=[1]*n
    for x in code:
        deg[x]+=1
    edges=[]
    for x in code:
        leaf=next(i for i in range(n) if deg[i]==1)
        edges.append((leaf,x))
        deg[leaf]-=1
        deg[x]-=1
    pair=[i for i in range(n) if deg[i]==1]
    edges.append((pair[0],pair[1]))
    return edges

def find_path(adj, src, dst):
    parents={src:-1}
    queue=[src]
    for x in queue:
        if x==dst:break
        for y in adj[x]:
            if y not in parents:
                parents[y]=x
                queue.append(y)
    out=[]
    x=dst
    while x!=-1:
        out.append(x)
        x=parents[x]
    return out[::-1]

def det(mat):
    # Determinant using exact integer Bareiss elimination.
    n=len(mat)
    if n==0:return 1
    a=[list(row) for row in mat]
    sign=1;prev=1
    for k in range(n-1):
        if a[k][k]==0:
            for q in range(k+1,n):
                if a[q][k]:
                    a[k],a[q]=a[q],a[k]
                    sign=-sign
                    break
            else:return 0
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=pivot*a[i][j]-a[i][k]*a[k][j]
                if num%prev:raise ArithmeticError('nonexact Bareiss division')
                a[i][j]=num//prev
        for i in range(k+1,n):a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

def run():
    # Independent enumeration from Prufer codes. Marked vertices are 0, 1, 2.
    for n in range(3,8):
        counts=defaultdict(int)
        branch=defaultdict(int)
        totals=defaultdict(int)
        for code in product(range(n),repeat=n-2):
            adj=[[] for _ in range(n)]
            for a,b in edges_from_prufer(code,n):
                adj[a].append(b)
                adj[b].append(a)
            path=find_path(adj,0,1)
            d=len(path)-1
            distances=[len(find_path(adj,2,x))-1 for x in path]
            h=min(distances)
            root_index=distances.index(h)
            counts[d,h]+=1
            branch[d,h,root_index]+=1
            totals[d]+=1
        for d in range(1,n):
            check(totals[d]>0,('distance support',n,d))
            for h in range(0,n):
                actual=Fraction(sum(counts[d,t] for t in range(h,n)),totals[d])
                check(actual==tail(n,d,h),('tail',n,d,h,actual,tail(n,d,h)))
            for h in range(1,n-d):
                c=sum(branch[d,h,j] for j in range(d+1))
                for j in range(d+1):
                    check((d+1)*branch[d,h,j]==c,('uniform projection',n,d,h,j))

    # Probability normalization, adjacent monotone likelihood ratio, exact Pascal tails.
    for n in range(3,51):
        for d in range(1,n):
            ps=[mass(n,d,h) for h in range(n)]
            check(all(p>=0 for p in ps),('nonnegative',n,d))
            check(sum(ps)==1,('normalized',n,d))
            k=n-d-1
            for h in range(n-1):
                col_scale=Fraction(1) if h==0 else Fraction(factorial(h),(n-2)*n**(h-1))
                check(tail(n,d,h)==col_scale*comb(k,h) if h<=k else tail(n,d,h)==0,('pascal',n,d,h))
            if d<n-1:
                p=[mass(n,d,h) for h in range(n)]
                q=[mass(n,d+1,h) for h in range(n)]
                for h in range(n-1):
                    check(q[h]*p[h+1]>=q[h+1]*p[h],('reverse MLR',n,d,h))
                    # Ratio criterion includes zeros, with no divisions required.

    # All minors of the normalized Pascal survival kernel through n=8.
    for n in range(3,9):
        rows=list(range(n-1))
        for r in range(1,n):
            for I in combinations(rows,r):
                for J in combinations(rows,r):
                    minor=det([[comb(k,h) if h<=k else 0 for h in J] for k in I])
                    check(minor>=0,('minor sign',n,I,J,minor))
                    check((minor>0)==all(I[t]>=J[t] for t in range(r)),('minor support',n,I,J,minor))
    print(f'PASS: {CHECKS} exact assertions (independent tree enumeration, conditional tails, projections, normalization, MLR, Pascal minors).')

if __name__=='__main__':
    run()
