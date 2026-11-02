"""Exact finite certificates for two central six-plane arrangements.

Only Python's standard library is needed. All arithmetic is integral.
The face-generation argument is given in the accompanying mathematical proof.
"""
from collections import Counter
from itertools import combinations

A = ((1,2,1),(2,-3,1),(3,1,1),(-3,-3,1),(-1,0,1),(-1,2,1))
B = ((2,0,1),(1,-3,1),(-2,-2,1),(-3,-2,1),(1,-1,1),(2,-3,1))


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def sign(x):
    return (x > 0)-(x < 0)


def covector(normals, v):
    return tuple(sign(dot(n,v)) for n in normals)


def generates_face_lattice(normals):
    """Exact face enumeration via rays, planar wedges and chamber perturbations."""
    n=len(normals)
    assert n==6
    assert all(dot(normals[i],cross(normals[j],normals[k]))
               for i,j,k in combinations(range(n),3))
    ray_vectors={}
    for i,j in combinations(range(n),2):
        v=cross(normals[i],normals[j])
        for w in (v,tuple(-x for x in v)):
            s=covector(normals,w)
            assert s.count(0)==2
            ray_vectors[s]=w
    planar=set()
    for u,v in combinations(ray_vectors.values(),2):
        w=tuple(a+b for a,b in zip(u,v))
        if w==(0,0,0):
            continue
        s=covector(normals,w)
        if s.count(0)==1:
            planar.add(s)
    chambers=set()
    for s in planar:
        i=s.index(0)
        for t in (-1,1):
            chambers.add(s[:i]+(t,)+s[i+1:])
    faces=set(ray_vectors)|planar|chambers|{(0,)*n}
    assert (len(faces),len(ray_vectors),len(planar),len(chambers))==(123,30,60,32)
    return sorted(faces),set(ray_vectors),planar,chambers


def below(a,b):
    return all(u==0 or u==v for u,v in zip(a,b))


def commutes(a,b):
    # Compare products signwise: first nonzero sign wins.
    return all(u==0 or v==0 or u==v for u,v in zip(a,b))


def all_maximal_cliques(faces, masks):
    n=len(faces)
    edges=[{j for j in range(n) if i!=j and masks[i]>>j&1} for i in range(n)]
    found=[]
    def bron_kerbosch(R,P,X):
        if not P and not X:
            found.append(frozenset(R));return
        pivot=max(P|X,key=lambda i:len(P&edges[i])) if P|X else None
        for v in list(P-(edges[pivot] if pivot is not None else set())):
            bron_kerbosch(R|{v},P&edges[v],X&edges[v]);P.remove(v);X.add(v)
    bron_kerbosch(set(),set(range(n)),set())
    return set(found)


def census(normals):
    faces,rays,planar,chambers=generates_face_lattice(normals)
    counts=Counter(sum(below(r,c) for r in rays) for c in chambers)
    assert sum(counts.values())==32 and sum(m*v for m,v in counts.items())==120
    incidence={frozenset(i for i,f in enumerate(faces) if below(f,c)) for c in chambers}
    assert {len(S) for S in incidence}=={2*m+2 for m in counts}
    n=len(faces)
    masks=[]
    for a in faces:
        masks.append(sum(1<<j for j,b in enumerate(faces) if commutes(a,b)))
    c2=sum(a.bit_count() for a in masks)
    c3=sum((masks[i]&masks[j]).bit_count() for i in range(n)
           for j in range(n) if masks[i]>>j&1)
    def formula(k):
        return 1+30*(2**k-1)+60*(1-4**k)-32+sum(v*(2*m+2)**k for m,v in counts.items())
    assert c2==formula(2) and c3==formula(3)
    assert formula(0)==1 and formula(1)==123
    assert all_maximal_cliques(faces,masks)==incidence
    return dict(sorted(counts.items())),c2,c3,[formula(k) for k in range(5)]


if __name__=='__main__':
    a=census(A)
    b=census(B)
    assert a[0]=={3:12,4:16,5:4},a
    assert b[0]=={3:12,4:18,6:2},b
    assert a[1:3]==(2103,25455) and b[1:3]==(2119,26031)
    assert a[3]==[1,123,2103,25455,277215],a
    assert b[3]==[1,123,2119,26031,291103],b
    print('ARRANGEMENT_A',a)
    print('ARRANGEMENT_B',b)
    print('VERIFY_OK')
