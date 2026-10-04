#!/usr/bin/env python3
from itertools import product, combinations
from math import comb


def det_bareiss(a):
    a=[row[:] for row in a]
    n=len(a)
    if n==0:
        return 1
    sign=1
    prev=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:
                return 0
            a[k],a[j]=a[j],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                a[i][j]=(a[i][j]*pivot-a[i][k]*a[k][j])//prev
        prev=pivot
        for i in range(k+1,n):
            a[i][k]=0
    return sign*a[n-1][n-1]


def root_vectors(m, signs):
    # Coordinates in the A_{m-1} basis e_0-e_{m-1},...,e_{m-2}-e_{m-1}.
    out=[]
    for i,s in enumerate(signs):
        t=i; h=(i+1)%m
        v=[0]*m
        v[h]+=s; v[t]-=s
        out.append(v[:m-1])
    return out


def det_columns(cols):
    n=len(cols)
    mat=[[cols[j][i] for j in range(n)] for i in range(n)]
    return det_bareiss(mat)


def poly_add(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return c


def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c


def h_from_faces(nverts, forbidden, dim):
    # Complex consists of all subsets not containing the forbidden vertex set.
    h=[0]
    for mask in range(1<<nverts):
        if all(mask & (1<<i) for i in forbidden):
            continue
        sz=mask.bit_count()
        term=[0]*sz+[1]
        # t^sz (1-t)^(dim+1-sz)
        for _ in range(dim+1-sz):
            term=poly_mul(term,[1,-1])
        h=poly_add(h,term)
    while len(h)>1 and h[-1]==0: h.pop()
    return h


def check(m, signs):
    vs=root_vectors(m, signs)
    p=sum(s==1 for s in signs); q=m-p
    a=min(p,q); b=max(p,q)
    # primitive cycle relation sum s_i v_i=0
    rel=[sum(signs[j]*vs[j][i] for j in range(m)) for i in range(m-1)]
    assert rel==[0]*(m-1)
    # every cycle-minus-one set is a signed tree incidence basis of A_{m-1}
    for omit in range(m):
        cols=[vs[j] for j in range(m) if j!=omit]
        assert abs(det_columns(cols))==1
    if p!=q:
        base=vs[-1]
        diffs=[[vs[j][i]-base[i] for i in range(m-1)] for j in range(m-1)]
        assert abs(det_columns(diffs))==abs(p-q)
        r=b-a
        heights=[0]+[a+k for k in range(1,r)]
        expected=[0]+list(range(a+1,b))
        assert heights==expected
    else:
        # Semi-balanced Q_C circuit triangulation: boundary simplex on either side.
        P=[i for i,s in enumerate(signs) if s==1]
        h=h_from_faces(m,P,m-2)
        assert h==[1]*a
    # Extended circuit triangulation: choose the majority side; ties choose +.
    majority=1 if p>=q else -1
    P=[i+1 for i,s in enumerate(signs) if s==majority]  # vertex 0 is origin
    h=h_from_faces(m+1,P,m-1)
    assert h==[1]*b


def main():
    cases=0
    for m in range(3,9):
        for signs in product((1,-1), repeat=m):
            check(m,signs); cases+=1
    print(f"VERIFY_OK oriented-cycle-root-polytopes cases={cases} max_m=8")

if __name__=='__main__':
    main()
