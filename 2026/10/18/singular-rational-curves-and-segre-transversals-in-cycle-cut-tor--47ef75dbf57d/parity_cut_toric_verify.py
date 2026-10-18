#!/usr/bin/env python3
"""Exact finite checks for normal-fan singularities of cycle cut polytopes.
Mathematical proof covers all n >= 4; these small-n tests are corroborative.
No third-party dependencies.
"""
from itertools import combinations
from fractions import Fraction
from math import gcd, comb


def rank(rows):
    if not rows:
        return 0
    aa = [[Fraction(a) for a in r] for r in rows]
    nrows, ncols = len(aa), len(aa[0]); pivot = 0
    for c in range(ncols):
        k = next((k for k in range(pivot,nrows) if aa[k][c]),None)
        if k is None: continue
        aa[pivot],aa[k] = aa[k],aa[pivot]
        a = aa[pivot][c]
        aa[pivot] = [x/a for x in aa[pivot]]
        for k in range(nrows):
            if k!=pivot and aa[k][c]:
                b=aa[k][c]
                aa[k]=[aa[k][j]-b*aa[pivot][j] for j in range(ncols)]
        pivot+=1
        if pivot == nrows: break
    return pivot


def determinant(aa):
    if not aa: return 1
    a = [[Fraction(x) for x in r] for r in aa]
    n=len(a); sign=1; product=Fraction(1)
    for j in range(n):
        k = next((i for i in range(j,n) if a[i][j]), None)
        if k is None: return 0
        if k!=j: a[k],a[j] = a[j],a[k];sign=-sign
        p=a[j][j];product*=p
        for i in range(j+1,n):
            if a[i][j]:
                r=a[i][j]/p
                for t in range(j+1,n):a[i][t]-=r*a[j][t]
                a[i][j]=0
    out=sign*product
    assert out.denominator==1
    return int(out)


def primitive_submodule(ray_columns, n):
    r=len(ray_columns)
    assert rank(ray_columns)==r
    g=0
    for rows in combinations(range(n),r):
        mat=[[ray_columns[col][j] for col in range(r)] for j in rows]
        g=gcd(g,abs(determinant(mat)))
        if g==1: return True
    return g==1


def chart_rays(n):
    # Coordinate form in N=L^*, basis e_0,...,e_{n-2}, h=(1,...,1)/2.
    u=[];v=[]
    for i in range(n):
        e=[0]*n
        if i<n-1:e[i]=1
        else:
            e=[-1]*(n-1)+[2]
        u.append(tuple(-x for x in e))
        v.append(tuple(e[j]-(j==n-1) for j in range(n)))
    return u,v


def check(n):
    vertices=[t for t in range(1<<n) if t.bit_count()%2==0]
    assert vertices[0]==0 and len(vertices)==2**(n-1)
    incident=[]
    for i in range(n):
        # coordinate facet x_i = 0
        incident.append(sum(1<<j for j,t in enumerate(vertices) if not (t>>i)&1))
    for i in range(n):
        # parity facet x_i - sum_{j != i} x_j = 0
        incident.append(sum(1<<j for j,t in enumerate(vertices)
                            if t==0 or t.bit_count()==2 and (t>>i)&1))
    u,v=chart_rays(n)
    rays=u+v
    assert all(mask&1 for mask in incident)
    faces={sum(1<<j for j in range(len(vertices)))}
    # finite intersections of vertex sets of all 2n incident facets
    for facet in incident:
        faces |= {mask&facet for mask in tuple(faces)}
    faces.discard(0)
    by_dim={}
    for mask in faces:
        pts=[tuple((t>>i)&1 for i in range(n)) for j,t in enumerate(vertices) if mask>>j&1]
        d=rank(pts)
        active=[j for j,F in enumerate(incident) if mask&F==mask]
        cone=[rays[j] for j in active]
        assert rank(cone)==n-d, ('cone rank',n,mask,d,active)
        if d>=2:
            assert len(active)==n-d, ('non-simple face >=2',n,mask,active)
            assert primitive_submodule(cone,n), ('non-saturated cone >=2',n,mask,active)
        elif d==1:
            assert len(active)==n, ('edge rays',n,mask,active)
            assert len(pts)==2 and (pts[0]==tuple([0]*n) or pts[1]==tuple([0]*n))
            assert sum(pts[0][i]!=pts[1][i] for i in range(n))==2
        else:
            assert d==0 and len(active)==2*n
        by_dim[d]=by_dim.get(d,0)+1
    assert by_dim[0]==1 and by_dim[1]==comb(n,2)
    expected_faces=(sum(comb(n,m) for m in range(3,n+1)) +
                    n*sum(comb(n-1,m-1) for m in range(3,n+1)) +
                    comb(n,2) + 1)
    assert len(faces)==expected_faces, (n,len(faces),expected_faces)
    # Check primitive circuit in the edge cone (0 to bits 0,1).
    lhs=[v[0][i]+v[1][i] for i in range(n)]
    rhs=[sum(u[j][i] for j in range(2,n)) for i in range(n)]
    assert lhs==rhs
    # Degree-k Segre coordinate dimensions for rank-one 2 x (n-2) matrices.
    m=n-2
    for k in range(1,5):
        semigroup={(a,k-a,*c) for a in range(k+1)
                   for c in product_compositions(k,m)}
        assert len(semigroup)==(k+1)*comb(k+m-1,m-1)
    n_vertices=2**(n-1)
    n_edges=n_vertices*comb(n,2)//2
    print('n=%d vertices=%d edges=%d zero_vertex_faces=%d face_dim_counts=%s ' 
          'edge_local=rank_one_2_by_%d multiplicity=%d OK' %
          (n,n_vertices,n_edges,len(faces),sorted(by_dim.items()),m,m))


def product_compositions(k,m):
    if m==1:
        yield (k,)
    else:
        for a in range(k+1):
            for rest in product_compositions(k-a,m-1):
                yield (a,)+rest


if __name__=='__main__':
    for n in range(4,8):check(n)
    print('VERIFY_OK')
