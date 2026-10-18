"""Exact finite tests of the weighted graph-BV extreme-point and path-facet formulas."""
from fractions import Fraction as F
from itertools import product

def rank(rows):
    if not rows: return 0
    a=[list(map(F,row)) for row in rows]
    m=len(a); n=len(a[0]);r=0
    for c in range(n):
        q=next((i for i in range(r,m) if a[i][c]),None)
        if q is None: continue
        a[r],a[q]=a[q],a[r]
        pivot=a[r][c]
        a[r]=[z/pivot for z in a[r]]
        for i in range(r+1,m):
            k=a[i][c]
            if k: a[i]=[a[i][j]-k*a[r][j] for j in range(n)]
        r+=1
        if r==m:break
    return r

def vertex(signs, edges):
    denominator = F(1)+sum(w*abs(signs[i]-signs[j]) for i,j,w in edges)
    return tuple(F(s)/denominator for s in signs)

def norm(x,edges):
    return max(map(abs,x))+sum(w*abs(x[i]-x[j]) for i,j,w in edges)

def signs(n): return list(product((-1,1),repeat=n))

def certify(n,edges):
    s_all=signs(n);vv=[vertex(s,edges) for s in s_all]
    for s,x in zip(s_all,vv):
        assert norm(x,edges)==1
        # Explicit norm-one exposing functional for s.
        def phi(y):
            return sum(F(s[i])*y[i] for i in range(n))/n + sum(w*F((s[i]-s[j])//2)*(y[i]-y[j]) for i,j,w in edges if s[i]!=s[j])
        assert phi(x)==1
        assert all(phi(y)<1 for t,y in zip(s_all,vv) if t!=s)
    return len(vv)

def facets_path(n,weights):
    edges=[(i,i+1,w) for i,w in enumerate(weights)]
    vv=[vertex(s,edges) for s in signs(n)]
    count=0; total=0
    for j in range(n):
        for s in (-1,1):
            for eps in product((-1,1),repeat=n-1):
                a=[F(0)]*n;a[j]+=s
                for i,w in enumerate(weights):
                    a[i]-=w*eps[i];a[i+1]+=w*eps[i]
                active=[x for x in vv if sum(a[i]*x[i] for i in range(n))==1]
                assert all(sum(a[i]*x[i] for i in range(n))<=1 for x in vv)
                compatible=(j==0 or eps[j-1]==s) and (j==n-1 or eps[j]==-s)
                # A facet has n affinely independent tight vertices.
                active_rank=rank([[F(1)]+list(x) for x in active])
                assert (active_rank==n)==compatible, (n,weights,j,s,eps,active_rank,compatible)
                count+=compatible;total+=1
    assert count==(n+2)*2**(n-2)
    return total,count

if __name__=='__main__':
    checks=0
    for n in range(2,7):
        for wcase in (tuple(F(1) for i in range(n-1)),tuple(F(i+1, i+2) for i in range(n-1))):
            edges=[(i,i+1,wcase[i]) for i in range(n-1)]
            assert certify(n,edges)==2**n
            checks+=2**n
            if n<=5:
                total,count=facets_path(n,wcase);checks+=total
    for n in range(3,7):
        edges=[(i,j,F(1+i+j,2+i+j)) for i in range(n) for j in range(i+1,n) if (i+j)%2]
        certify(n,edges);checks+=2**n
    print('PASS exact exposed-vertex and path-facet tests:',checks)
