#!/usr/bin/env python3
"""Finite-field checks for equivariant surface orientation traces."""
from itertools import product

def inverse(a,p):
    return pow(a,-1,p)

def normalize_plane(u,v,p):
    a=[list(u),list(v)]
    row=0
    for c in range(4):
        piv=next((r for r in range(row,2) if a[r][c]%p),None)
        if piv is None: continue
        a[row],a[piv]=a[piv],a[row]
        q=inverse(a[row][c]%p,p)
        a[row]=[(t*q)%p for t in a[row]]
        for r in range(2):
            if r!=row:
                t=a[r][c]
                a[r]=[(s-t*w)%p for s,w in zip(a[r],a[row])]
        row+=1
        if row==2:break
    if row<2:return None
    return tuple(map(tuple,a))

def symplectic(u,v,p):
    return (u[0]*v[2]+u[1]*v[3]-u[2]*v[0]-u[3]*v[1])%p

def planes(p):
    vec=list(product(range(p),repeat=4))
    lines={}
    for v in vec:
        if any(v):
            i=next(i for i,x in enumerate(v) if x)
            w=tuple(x*inverse(v[i],p)%p for x in v)
            lines[w]=1
    L=list(lines)
    P=set()
    for i,u in enumerate(L):
        for v in L[i+1:]:
            if symplectic(u,v,p)==0:
                P.add(normalize_plane(u,v,p))
    return sorted(P)

def transvection(u,p):
    return tuple((x-(u[2] if i==0 else 0))%p for i,x in enumerate(u))

def stable_det(P,g,p):
    a,b=P
    ga=g(a,p);gb=g(b,p)
    C=normalize_plane(ga,gb,p)
    if C!=P:return None
    # Find entries of A,B w.r.t. RREF basis by pivot coordinates.
    piv=[next(i for i,x in enumerate(r) if x) for r in (a,b)]
    x,y=(ga[piv[0]],ga[piv[1]])
    z,w=(gb[piv[0]],gb[piv[1]])
    return (x*w-y*z)%p

def symplectic_involution(u,p):
    return tuple(((-x if i in (0,2) else x)%p) for i,x in enumerate(u))

# For p=3, an orientation-reversing determinant-minus-one matrix
# acts on the four vertices of the tetrahedral surface as a transposition.
def p3_vertex(v):
    a,b=v
    if (a,b)==(0,0): return None
    if a:
        t=inverse(a,3)
    else:
        t=inverse(b,3)
    return ((a*t)%3,(b*t)%3)
V=sorted({p3_vertex(v) for v in product(range(3),repeat=2) if any(v)})
assert len(V)==4
perm=[V.index(p3_vertex((-a%3,b))) for a,b in V]
assert sum(1 for a in range(4) for b in range(a+1,4) if perm[a]>perm[b])%2==1

for p in (3,5,7):
    L=planes(p)
    assert len(L)==(p+1)*(p*p+1),(p,len(L))
    Ds=[stable_det(P,transvection,p) for P in L]
    assert Ds.count(1)==p+1
    assert Ds.count(None)==len(L)-p-1
    assert all(x in (1,None) for x in Ds)
    characters={d:sum(1 if det==1 else -1 if det==p-1 else 0 for det in Ds)*(p-1)//2 for d in ['transvection']}
    assert characters['transvection']==(p*p-1)//2
    total=(p**4-1)//2
    invariant=(total+(p-1)*characters['transvection'])//p
    assert invariant==(p-1)*(p+1)**2//2
    Id=[stable_det(P,symplectic_involution,p) for P in L]
    assert Id.count(p-1)==(p+1)**2
    assert Id.count(None)==len(L)-(p+1)**2
    assert all(x in (p-1,None) for x in Id)
    involution_trace=-(p-1)*(p+1)**2//2
    assert (total+involution_trace)%2==0
    print(f'p={p}: lagrangians={len(L)} surfaces={total} transvection_trace={characters["transvection"]} cyclic_invariants={invariant} symplectic_involution_trace={involution_trace}')
print('VERIFY_OK')
