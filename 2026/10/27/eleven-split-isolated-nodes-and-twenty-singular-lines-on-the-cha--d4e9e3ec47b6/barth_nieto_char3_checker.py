"""Standalone finite-field sanity checks for the characteristic-three Barth--Nieto model.
Geometric completeness is established separately by the symbolic argument in RESULT.md.
"""
from itertools import product,combinations
from collections import Counter
P=3

def esym(v,k):
    a=[1]+[0]*k
    for x in v:
        for i in range(k,0,-1):
            a[i]=(a[i]+x*a[i-1])%P
    return a[k]

def grad(v):
    return [esym(v[:i]+v[i+1:],4) for i in range(6)]

def det(a):
    a=[row[:] for row in a]; n=len(a); d=1
    for j in range(n):
        r=next((i for i in range(j,n) if a[i][j]%P),None)
        if r is None: return 0
        if r!=j:
            a[r],a[j]=a[j],a[r]; d=-d
        t=a[j][j]%P;d=d*t%P;ti=pow(t,-1,P)
        for i in range(j+1,n):
            z=a[i][j]*ti%P
            for h in range(j,n):a[i][h]=(a[i][h]-z*a[j][h])%P
    return d%P

def affine_hessian_det(v):
    H=[[0 if i==j else esym([v[t] for t in range(6) if t not in (i,j)],3) for j in range(6)] for i in range(6)]
    B=[[(H[i][j]-H[i][4]-H[4][j]+H[4][4])%P for j in range(4)] for i in range(4)]
    return det(B)

points=[]
for y in product(range(P),repeat=5):
    if y==(0,)*5:continue
    first=next(a for a in y if a)
    if first!=1:continue
    v=(*y,-sum(y)%P)
    if esym(v,5)==0:
        g=grad(v)
        points.append((v,len(set(g))==1))
assert len(points)==91, len(points)
sing=[v for v,s in points if s]
assert len(sing)==46,len(sing)
assert Counter(sum(x==0 for x in v) for v in sing)=={3:20,4:15,0:11}
sign=[v for v in sing if all(x for x in v)]
assert len(sign)==11
assert all(affine_hessian_det(v)!=0 for v in sign)
E=(1,1,1,1,1,1)
assert affine_hessian_det(E)!=0
assert affine_hessian_det((2,2,2,1,1,1))!=0
assert 15==len([v for v in sing if v.count(0)==4])
assert 20==len([v for v in sing if v.count(0)==3])
print('CHECK_OK points_F3=91 singular_F3=46 line_intersections=15 line_interior_F3=20 isolated_nodes=11')
print('CHECK_OK ordinary_node_Hessian_determinants E=%d signed=%d'%(affine_hessian_det(E),affine_hessian_det((2,2,2,1,1,1))))
