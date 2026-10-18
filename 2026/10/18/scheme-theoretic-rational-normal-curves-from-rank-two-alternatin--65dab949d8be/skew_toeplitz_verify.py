"""Exact finite-degree checks for the skew-Toeplitz Pfaffian theorem.
Run: python3 skew_toeplitz_verify.py
Requires Python 3 standard library only.
"""
from itertools import combinations
from fractions import Fraction
from math import comb


def plus(p,q,scale=1):
    r=p.copy()
    for mon,val in q.items():
        r[mon]=r.get(mon,0)+scale*val
        if r[mon]==0: del r[mon]
    return r


def mul(p,q):
    r={}
    for (a,b),x in p.items():
        for (c,d),y in q.items():
            k=(a+c,b+d)
            r[k]=r.get(k,0)+x*y
    return {k:v for k,v in r.items() if v}


def parametrization(n):
    d=n-2
    p=[{(0,0):1},{(0,1):1}]
    for m in range(2,d+1):
        p.append(plus(mul({(0,1):1},p[-1]),mul({(2,0):1},p[-2]),-1))
    return [None]+[mul({(d-m,0):1},p[m]) for m in range(d+1)]


def pf_forms(n):
    return [(i,j,k,l) for i,j,k,l in combinations(range(n),4)]


def term(i,j):
    if i==j: return 0,1
    if i<j: return j-i,1
    return i-j,-1


def pf_poly(t,ind):
    i,j,k,l=ind
    def prod(a,b,c,d):
        r,s=term(a,b); u,v=term(c,d)
        return mul(t[r],t[u]) if s*v==1 else {x:-y for x,y in mul(t[r],t[u]).items()}
    return plus(plus(prod(i,j,k,l),prod(i,k,j,l),-1),prod(i,l,j,k))


def linear_rank(rows,cols):
    arr=[[Fraction(z) for z in row] for row in rows]
    r=0
    for c in range(cols):
        p=next((k for k in range(r,len(arr)) if arr[k][c]),None)
        if p is None: continue
        arr[r],arr[p]=arr[p],arr[r]
        q=arr[r][c]
        arr[r]=[v/q for v in arr[r]]
        for k in range(r+1,len(arr)):
            q=arr[k][c]
            if q: arr[k]=[v-q*w for v,w in zip(arr[k],arr[r])]
        r+=1
        if r==len(arr):break
    return r


def check(n):
    t=[{}]+[{(j,0):1} for j in range(1,n)]  # stand-in; not used in degree-two monomials
    params=parametrization(n)
    for inds in pf_forms(n):
        assert pf_poly(params,inds)=={},(n,inds,pf_poly(params,inds))
    # Independent quadratic forms indexed by 2<=i<=j<=n-2.
    pairs=list(combinations(range(1,n),2))+[(j,j) for j in range(1,n)]
    pairs=sorted(pairs)
    cols={m:c for c,m in enumerate(pairs)}
    selected=[]
    for i in range(2,n-1):
        for j in range(i,n-1):
            row=[0]*len(pairs)
            for coeff,p,q in [(1,1,j+1-i),(-1,i,j),(1,i-1,j+1)]:
                key=tuple(sorted((p,q)))
                row[cols[key]]+=coeff
            selected.append(row)
    target=comb(n-2,2)
    assert len(selected)==target
    assert linear_rank(selected,len(pairs))==target
    return len(pf_forms(n)),target

for size in range(4,11):
    all_pf,rank=check(size)
    print('n=%d: %d Pfaffians vanish identically on parameterization; %d independent quadrics: PASS'%(size,all_pf,rank))
print('VERIFY_OK')
