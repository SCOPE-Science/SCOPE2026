#!/usr/bin/env python3
"""Independent exact finite checks of cyclic-blowup majority-stable-set formula.
No external dependencies. Finite tests corroborate, but do not replace, proof.
"""
from itertools import product
from math import comb

def poly_add(a,b):
    return [ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b))) ]

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def recurrence(d,m):
    A=[comb(m,j) for j in range(m+1)]
    t=m//2
    B=A[:t+1]
    C=poly_add(A,[-v for v in B])
    p0=[2]; p1=B
    for _ in range(2,d+1):
        p0,p1=p1,poly_add(poly_mul(B,p1),poly_mul(C,p0))
    return p1

def occupancy(d,m):
    ans=[0]*(d*m+1)
    for x in product(range(m+1),repeat=d):
        if all(not x[i] or x[(i+1)%d]<=m//2 for i in range(d)):
            w=1
            for u in x: w*=comb(m,u)
            ans[sum(x)]+=w
    return ans

def leading(d,m):
    degree=d*m//2
    if m%2:
        return degree,(2 if d%2==0 else d*comb(m,(m-1)//2))
    c=comb(m,m//2)
    count=sum((d*comb(d-k,k)//(d-k))*c**(d-2*k) for k in range(d//2+1))
    return degree,count

def direct(d,m):
    n=d*m
    res=[0]*(n+1)
    for mask in range(1<<n):
        x=[((mask>>(i*m))&((1<<m)-1)).bit_count() for i in range(d)]
        if all(x[i]==0 or x[(i+1)%d]<=m//2 for i in range(d)):
            res[mask.bit_count()]+=1
    return res

def two_colour_count(d,m):
    res=0
    for r in product(range(m+1),repeat=d):
        if all( (r[i]==0 or r[(i+1)%d]<=m//2) and (r[i]==m or m-r[(i+1)%d]<=m//2) for i in range(d)):
            w=1
            for v in r: w*=comb(m,v)
            res+=w
    return res

def expected_two(d,m):
    if m%2==0: return comb(m,m//2)**d+(2 if d%2==0 else 0)
    if d%2==0: return 2
    return 0

def test():
    checks=0; direct_checked=0
    for d in range(3,9):
      for m in range(1,5):
        rec=recurrence(d,m); count=occupancy(d,m)
        assert rec==count[:len(rec)] and all(c==0 for c in count[len(rec):]),(d,m,'poly')
        top,ways=leading(d,m)
        assert max(i for i,n in enumerate(count) if n)==top,(d,m,'degree')
        assert count[top]==ways and all(x==0 for x in count[top+1:]),(d,m,'top',count[top],ways)
        c=two_colour_count(d,m)
        assert c==expected_two(d,m),(d,m,'colors',c,expected_two(d,m))
        checks+=3
        if d*m<=14:
            assert direct(d,m)==count,(d,m,'direct')
            direct_checked+=1
    print(f'VERIFY_OK: {checks} recurrence/top/colour checks across 24 parameter pairs; {direct_checked} exhaustive labeled-subset checks; no proof inferred from finite tests')
if __name__=='__main__': test()
