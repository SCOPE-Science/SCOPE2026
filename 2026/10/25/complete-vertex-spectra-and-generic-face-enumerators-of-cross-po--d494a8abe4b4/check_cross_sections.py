"""Exact combinatorial and optional geometric checks for cross-polytope hyperplane sections.
Run: python check_cross_sections.py
"""
from itertools import combinations, product
from math import comb

def vertices(n):
    return [(i,s) for i in range(n) for s in (-1,1)]

def signs(a,b):
    return {(i,s): (1 if s*a[i]>b else (-1 if s*a[i]<b else 0))
            for i in range(len(a)) for s in (-1,1)}

def section_vertices(n,a,b):
    sig=signs(a,b)
    vs=vertices(n)
    return sum(sig[v]==0 for v in vs) + sum(sig[u]*sig[v]<0
        for u,v in combinations(vs,2) if u[0]!=v[0])

def poly_coefficient(n,r,j):
    # f_{j-2}, via the generating polynomial.
    c= (2**j)*comb(n,j)
    c-=sum(comb(r,k)*comb(n-r,j-k)*2**(j-k)
           for k in range(max(0,j-(n-r)),min(r,j)+1))
    c-=comb(r,j) if j<=r else 0
    return c

def enumerate_faces(n,a,b):
    sig=signs(a,b)
    out=[]
    for j in range(2,n+1):
        count=0
        for idx in combinations(range(n),j):
            for ss in product((-1,1),repeat=j):
                vals=[sig[(i,s)] for i,s in zip(idx,ss)]
                if min(vals)<0<max(vals):count+=1
        out.append(count)
    return out

cnt=0
for n in range(2,10):
    for r in range(n+1):
        for s in range(n-r+1):
            if r+s==0:continue
            a=[2]*r+[1]*s+[0]*(n-r-s)
            exp=s+r*(2*n-r-s-1)
            got=section_vertices(n,a,1)
            assert got==exp,(n,r,s,exp,got)
            cnt+=1
            if s==0 and r>=1 and n<=7:
                computed=enumerate_faces(n,a,1)
                predicted=[poly_coefficient(n,r,j) for j in range(2,n+1)]
                assert computed==predicted,(n,r,computed,predicted)
    for r in range(1,n+1):
        a=[1]*r+[0]*(n-r)
        exp=r*(r-1)+2*(n-r)
        assert section_vertices(n,a,0)==exp,(n,r)
        cnt+=1
    values={s+r*(2*n-r-s-1) for r in range(n+1)
        for s in range(n-r+1) if r+s>=1}
    values|={r*(r-1)+2*(n-r) for r in range(1,n+1)}
    assert max(values)==n*(n-1)
    if n>=4:
        assert not any(n<k<2*n-2 for k in values)
    if n>=2:
        assert {r*(2*n-r-1) for r in range(1,n+1)}=={r*(2*n-r-1) for r in range(1,n)}
        assert sum(k not in {r*(2*n-r-1) for r in range(1,n+1)} for k in range(2*n-2,n*(n-1)+1))==(n-2)**2
print('EXACT_SECTION_COMBINATORICS_OK',cnt,'parameter cases')

# Independently obtain geometric vertices from edge-plane intersections and
# check all are extremal in ambient coordinates projected to the hyperplane.
import numpy as np
from scipy.spatial import ConvexHull
from scipy.linalg import null_space
num=0
for n in range(3,7):
    for r in range(n+1):
        for s in range(n-r+1):
            if r+s==0 or (r==0 and s==1): continue
            a=np.asarray([2]*r+[1]*s+[0]*(n-r-s),dtype=float)
            b=1.
            vv=[]
            for i in range(n):
                for ss in (-1,1):
                    x=np.zeros(n);x[i]=ss
                    vv.append(x)
            pts=[]
            for p in vv:
                if abs(a@p-b)<1e-10:pts.append(p)
            for ii,jj in combinations(range(len(vv)),2):
                if ii//2==jj//2: continue
                p,q=vv[ii],vv[jj]
                fp=a@p-b;fq=a@q-b
                if fp*fq<0:
                    t=fp/(fp-fq)
                    pts.append(p+t*(q-p))
            if not pts:continue
            p0=pts[0];B=null_space(a.reshape(1,-1));X=(np.array(pts)-p0)@B
            if r==0: # supporting simplex of s vertices, possibly low-dimensional
                continue
            hull=ConvexHull(X,qhull_options='QJ')
            assert len(hull.vertices)==len(pts),(n,r,s,len(pts),len(hull.vertices))
            num+=1
    for r in range(1,n+1):
        a=np.array([1]*r+[0]*(n-r),dtype=float);b=0
        vv=[]
        for i in range(n):
            for ss in (-1,1):
                x=np.zeros(n);x[i]=ss;vv.append(x)
        pts=[]
        for p in vv:
            if abs(a@p)<1e-10:pts.append(p)
        for ii,jj in combinations(range(len(vv)),2):
            if ii//2==jj//2:continue
            p,q=vv[ii],vv[jj];fp=a@p;fq=a@q
            if fp*fq<0:
                t=fp/(fp-fq);pts.append(p+t*(q-p))
        B=null_space(a.reshape(1,-1)); X=(np.array(pts)-pts[0])@B
        hull=ConvexHull(X,qhull_options='QJ')
        assert len(hull.vertices)==len(pts),(n,r,len(pts),len(hull.vertices))
        num+=1
print('GEOMETRIC_SECTION_CHECK_OK',num,'nontrivial polytope sections')
