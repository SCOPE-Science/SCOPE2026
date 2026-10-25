#!/usr/bin/env python3
"""Exact integer checks for face-gap balancing in three-level poset polytopes.

No third-party packages. The algebraic theorem is proved separately; the finite
checks exercise its polynomial identities and independent facet-incidence data.
"""
from itertools import product
from math import comb

MOD=1000003

def plus(a,b):
    n=max(len(a),len(b));return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]
def neg(a):return [-u for u in a]
def sub(a,b):return plus(a,neg(b))
def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):z[i+j]+=u*v
    return z

def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def power_linear(c,k):return [comb(k,j)*c**(k-j) for j in range(k+1)]
def gap_factor(a):return plus([1],sub(mul([0,1],power_linear(2,a)),power_linear(1,a+1)))
def face_order_formula(a,b):
    A=power_linear(2,a);B=power_linear(2,b)
    return plus(plus(A,B),mul([0,1],mul(A,B)))
def face_chain_formula(a,b):
    A=power_linear(2,a);B=power_linear(2,b)
    U=power_linear(1,a);V=power_linear(1,b)
    base=plus(sub(plus(A,B),[1]),plus(mul(sub(U,[1]),sub(V,[1])),mul([0,1],mul(sub(A,U),sub(B,V)))))
    return plus([1],mul([1,1],base))

def rank_mod(points):
    if len(points)<=1:return 0
    mat=[[(x-y)%MOD for x,y in zip(row,points[0])] for row in points[1:]]
    ncols=len(points[0]);row=0
    for col in range(ncols):
        piv=next((i for i in range(row,len(mat)) if mat[i][col]),None)
        if piv is None:continue
        mat[row],mat[piv]=mat[piv],mat[row]
        inv=pow(mat[row][col],-1,MOD)
        for i in range(row+1,len(mat)):
            if mat[i][col]:
                f=mat[i][col]*inv%MOD
                for j in range(col,ncols):mat[i][j]=(mat[i][j]-f*mat[row][j])%MOD
        row+=1
        if row==len(mat):break
    return row

def actual_faces(a,b,kind):
    # Coordinates (x_0,...,x_{a-1},z,y_0,...,y_{b-1}).
    n=a+b+1; verts=[]
    if kind=='O':
        for t in product((0,1),repeat=b):verts.append((0,)*a+(0,)+t)
        for t in product((0,1),repeat=a):verts.append(t+(1,)+(1,)*b)
    else:
        for t in product((0,1),repeat=a):verts.append(t+(0,)+(0,)*b)
        for t in product((0,1),repeat=b):
            if any(t):verts.append((0,)*a+(0,)+t)
        verts.append((0,)*a+(1,)+(0,)*b)
    assert len(verts)==2**a+2**b
    facets=[]
    def facet(f):
        mask=sum((1<<k) for k,v in enumerate(verts) if f(v)==0)
        facets.append(mask)
    for i in range(a):facet(lambda v,i=i:v[i])
    for j in range(b):facet(lambda v,j=j:v[a+1+j] if kind=='C' else 1-v[a+1+j])
    if kind=='O':
        for i in range(a):facet(lambda v,i=i:v[a]-v[i])
        for j in range(b):facet(lambda v,j=j:v[a+1+j]-v[a])
    else:
        facet(lambda v:v[a])
        for i in range(a):
            for j in range(b):facet(lambda v,i=i,j=j:1-v[i]-v[a]-v[a+1+j])
    faces={ (1<<len(verts))-1 }
    for f in facets:
        faces.update({u&f for u in list(faces) if u&f})
    ret=[0]*(n+1)
    for mask in faces:
        subverts=[v for j,v in enumerate(verts) if mask>>j&1]
        rank=rank_mod(subverts)
        ret[rank]+=1
    assert ret[n]==1
    return ret

def hpoly(m):
    # Complete homogeneous symmetric function h_m(1,1+t,2+t).
    z=[0]
    for p in range(m+1):
        for q in range(m-p+1):
            z=plus(z,mul(power_linear(1,p),power_linear(2,q)))
    return z

def main():
    checked=0
    for a in range(1,14):
        for b in range(1,14):
            o=face_order_formula(a,b);c=face_chain_formula(a,b)
            d=sub(c,o);g=mul(gap_factor(a),gap_factor(b))
            assert d==g,(a,b,d,g)
            assert d[0]==0 and d[1]==0 and all(x==0 for x in d[a+b+1:])
            if a>=2 and b>=2:
                assert all(x>0 for x in d[2:a+b+1]),(a,b,d)
            else:assert all(x==0 for x in d)
            checked+=1
    balance=0
    for a in range(2,10):
        for b in range(a+2,16):
            d=sub(mul(gap_factor(a+1),gap_factor(b-1)),mul(gap_factor(a),gap_factor(b)))
            # Jacobi-Trudi determinant. b-3 >= a-1.
            schur=sub(mul(hpoly(b-3),hpoly(a-1)),mul(hpoly(b-2),hpoly(a-2)))
            s=mul([0,0,1,2,1],schur)
            assert trim(d[:])==trim(s[:]),(a,b,d,s)
            assert all(v>0 for v in d[2:a+b+1]) and d[0]==d[1]==0 and all(v==0 for v in d[a+b+1:])
            balance+=1
    shapes=0
    for a,b in [(2,2),(2,3),(3,2),(3,3)]:
        for kind in ['O','C']:
            actual=actual_faces(a,b,kind)
            predicted=(face_order_formula if kind=='O' else face_chain_formula)(a,b)
            assert actual==trim(predicted[:]),(a,b,kind,actual,predicted)
            shapes+=1
    print('EXACT_OK gap_pairs=%d balancing_steps=%d independent_facets=%d'%(checked,balance,shapes))
    print('example_a2_b2',face_order_formula(2,2),face_chain_formula(2,2))
    print('example_a2_b3',face_order_formula(2,3),face_chain_formula(2,3))
if __name__=='__main__':main()
