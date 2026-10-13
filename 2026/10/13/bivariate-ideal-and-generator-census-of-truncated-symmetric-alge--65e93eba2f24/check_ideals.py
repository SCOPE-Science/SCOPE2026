#!/usr/bin/env python3
"""Independent finite-field enumeration of the ideal/generator bivariate polynomial.
Public scientific reproducibility code: no external packages or files needed.
"""
from itertools import combinations, product
from collections import Counter
from math import prod, comb

def gauss(n,k,q):
    if not 0 <= k <= n: return 0
    return prod((q**(n-i)-1)//1 for i in range(k)) // prod((q**(k-i)-1)//1 for i in range(k))

def rrefs(n,q):
    for k in range(n+1):
        for piv in combinations(range(n),k):
            cells = [(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
            for values in product(range(q),repeat=len(cells)):
                rows=[[0]*n for _ in piv]
                for i,p in enumerate(piv): rows[i][p]=1
                for (i,j),v in zip(cells,values): rows[i][j]=v
                yield rows,piv

def is_member(vec, rows,piv,q):
    z=list(vec)
    for row,p in zip(rows,piv):
        c=z[p]%q
        if c:
            z=[(a-c*b)%q for a,b in zip(z,row)]
    return not any(z)

def rank(rows,q):
    if not rows: return 0
    m=[list(x) for x in rows]
    n=len(m[0]); r=0
    for j in range(n):
        pivot=next((i for i in range(r,len(m)) if m[i][j]%q),None)
        if pivot is None: continue
        m[r],m[pivot]=m[pivot],m[r]
        inv=pow(m[r][j],-1,q)
        m[r]=[inv*x%q for x in m[r]]
        for i in range(r+1,len(m)):
            c=m[i][j]
            if c: m[i]=[(x-c*y)%q for x,y in zip(m[i],m[r])]
        r+=1
        if r==len(m): break
    return r

def poly(d,q):
    h=d*(d+1)//2
    out=Counter({(d+h+1,1):1})
    for r in range(d+1):
        b=(d-r)*(d-r+1)//2
        for j in range(b+1):
            out[(r+h-b+j,r+j)]+=gauss(d,r,q)*gauss(b,j,q)*q**(r*(b-j))
    return out

def brute(d,q):
    h=d*(d+1)//2; m=d+h
    degree2=list(combinations(range(d),2)) + [(i,i) for i in range(d)]
    index={tuple(sorted(v)):k for k,v in enumerate(degree2)}
    def prod_x(vec,i):
        z=[0]*m
        for j in range(d): z[d+index[tuple(sorted((i,j)))]]=(z[d+index[tuple(sorted((i,j)))]]+vec[j])%q
        return z
    ans=Counter({(m+1,1):1}); visited=0
    for rows,piv in rrefs(m,q):
        visited+=1
        prods=[prod_x(row,i) for row in rows for i in range(d)]
        if all(is_member(w,rows,piv,q) for w in prods):
            ans[(len(rows),len(rows)-rank(prods,q))]+=1
    return ans,visited

def run():
    for d,q in [(1,2),(1,3),(2,2),(2,3)]:
        actual,visited=brute(d,q); predicted=poly(d,q)
        assert actual==predicted,(d,q,actual,predicted)
        print('OK',f'd={d}',f'q={q}',f'visited_subspaces={visited}',f'ideals={sum(actual.values())}',f'coeffs={sorted(actual.items())}')
    print('VERIFY_OK')
if __name__=='__main__':run()
