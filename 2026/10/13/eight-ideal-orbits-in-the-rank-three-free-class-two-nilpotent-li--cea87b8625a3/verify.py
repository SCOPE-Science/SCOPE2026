#!/usr/bin/env python3
"""Independent exhaustive finite-field ideal census for a rank-three free class-two Lie algebra.

Coordinates x1,x2,x3,z12,z13,z23, with [xi,xj]=zij. No dependencies.
"""
from itertools import combinations, product
from collections import Counter, deque


def rref_subspaces(q,n=6):
    # Canonical RREF matrix: pivot rows have 1, earlier pivots in other rows 0;
    # free entries occur strictly after that row's pivot and outside pivot columns.
    for k in range(n+1):
        for piv in combinations(range(n),k):
            free=[(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
            for vals in product(range(q),repeat=len(free)):
                mat=[[0]*n for _ in range(k)]
                for i,j in enumerate(piv):mat[i][j]=1
                for (i,j),a in zip(free,vals):mat[i][j]=a
                yield tuple(tuple(r) for r in mat)


def rank(rows,q):
    a=[list(r) for r in rows if any(r)]
    if not a:return 0
    n=len(a[0]); k=0
    for c in range(n):
        pivot=next((i for i in range(k,len(a)) if a[i][c]),None)
        if pivot is None:continue
        a[k],a[pivot]=a[pivot],a[k]
        inv=pow(a[k][c],-1,q)
        a[k]=[(x*inv)%q for x in a[k]]
        for i in range(k+1,len(a)):
            if a[i][c]:
                alpha=a[i][c]
                a[i]=[(x-alpha*y)%q for x,y in zip(a[i],a[k])]
        k+=1
        if k==len(a):break
    return k


def bracket_with_x(r,i,q):
    a,b,c=r[:3]
    if i==0:z=(b,c,0)
    elif i==1:z=(-a,0,c)
    else:z=(0,-a,-b)
    return (0,0,0)+tuple(t%q for t in z)


def reduced(rows,q):
    mat=[list(r) for r in rows if any(r)]
    if not mat:return tuple()
    k=0
    for j in range(6):
        idx=next((i for i in range(k,len(mat)) if mat[i][j]%q),None)
        if idx is None:continue
        mat[k],mat[idx]=mat[idx],mat[k]
        inv=pow(mat[k][j]%q,-1,q)
        mat[k]=[(a*inv)%q for a in mat[k]]
        for i in range(len(mat)):
            if i!=k and mat[i][j]:
                t=mat[i][j]
                mat[i]=[(a-t*b)%q for a,b in zip(mat[i],mat[k])]
        k+=1
        if k==len(mat):break
    return tuple(tuple(row) for row in mat[:k])


def matmul(g,v,q):
    return tuple(sum(g[i][j]*v[j] for j in range(3))%q for i in range(3))


def wedge(a,b,q):
    return ((a[0]*b[1]-a[1]*b[0])%q,(a[0]*b[2]-a[2]*b[0])%q,(a[1]*b[2]-a[2]*b[1])%q)


def generators(q):
    I=((1,0,0),(0,1,0),(0,0,1))
    gs=[]
    for i in range(3):
        for j in range(3):
            if i==j:continue
            g=[list(row) for row in I];g[i][j]=1;gs.append((tuple(tuple(row) for row in g),None))
    if q>2:
        g=[list(row) for row in I];g[0][0]=2;gs.append((tuple(tuple(row) for row in g),None))
    for i in range(3):
        for j in range(3):gs.append((I,(i,j)))
    return gs


def action(basis,gen,q):
    g,shear=gen
    cols=[matmul(g,tuple(1 if t==i else 0 for t in range(3)),q) for i in range(3)]
    Z=(wedge(cols[0],cols[1],q),wedge(cols[0],cols[2],q),wedge(cols[1],cols[2],q))
    out=[]
    for r in basis:
        v=matmul(g,r[:3],q)
        z=[sum(r[3+k]*Z[k][j] for k in range(3))%q for j in range(3)]
        if shear is not None:z[shear[1]]=(z[shear[1]]+r[shear[0]])%q
        out.append(tuple(v)+tuple(z))
    return reduced(out,q)


def verify_orbits(ideals,q):
    todo=set(ideals);gs=generators(q);sizes=[]
    while todo:
        rep=next(iter(todo)); todo.remove(rep)
        orbit={rep};pending=deque([rep])
        while pending:
            basis=pending.popleft()
            for g in gs:
                image=action(basis,g,q)
                if image not in orbit:
                    assert image in ideals,(q,'image outside ideal set',image)
                    orbit.add(image);todo.remove(image);pending.append(image)
        sizes.append(len(orbit))
    G=q*q+q+1
    assert sorted(sizes)==sorted([1,1,1,G,G,G,G,q*G]),(q,sizes)
    print(f'q={q}: explicit automorphism-generator BFS gives orbit sizes {sorted(sizes)}')


def run(q):
    assert q in (2,3,5,7,11)
    G=q*q+q+1
    expected=Counter({
        (0,0,0):1,(0,1,1):G,(0,2,2):G,(0,3,3):1,
        (1,2,3):q*G,(1,3,4):G,(2,3,5):G,(3,3,6):1
    })
    actual=Counter(); spaces=0; ideals=set()
    for basis in rref_subspaces(q):
        spaces+=1
        k=len(basis)
        rr=rank(basis,q)
        if any(rank(basis+(bracket_with_x(row,j,q),),q)!=rr
               for row in basis for j in range(3)):
            continue
        u=rank([r[:3] for r in basis],q)
        w=k-u
        actual[(u,w,k)]+=1
        ideals.add(basis)
    assert actual==expected,(q,actual,expected)
    dims=[sum(n for (_,_,d),n in actual.items() if d==j) for j in range(7)]
    assert dims==[1,G,G,1+q*G,G,G,1],(q,dims)
    assert sum(actual.values())==q**3+5*q*q+5*q+7
    print(f'q={q}: all {spaces} subspaces searched; ideals={sum(actual.values())}; dimension_profile={dims}; orbit_strata=8')
    verify_orbits(ideals,q)

if __name__=='__main__':
    for qq in (2,3):run(qq)
    print('VERIFY_OK')
