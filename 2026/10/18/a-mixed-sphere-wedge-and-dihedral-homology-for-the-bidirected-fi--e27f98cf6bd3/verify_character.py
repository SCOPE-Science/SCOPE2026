#!/usr/bin/env python3
"""Independent finite-chain and dihedral-character check for a wheel multipath complex."""
from collections import defaultdict, Counter

V = range(5)
links = [(0, j) for j in range(1, 5)] + [(1,2),(2,3),(3,4),(4,1)]
arcs = sorted([(a,b) for a,b in links] + [(b,a) for a,b in links])
assert len(arcs) == 16

def ok(subset):
    # Reconstruct a partial successor function and exclude directed cycles.
    out, incoming = {}, {}
    for a in subset:
        u,v = arcs[a]
        if u in out or v in incoming:
            return False
        out[u] = v
        incoming[v] = u
    for v in V:
        u,seen = v,set()
        while u in out:
            if u in seen:
                return False
            seen.add(u)
            u = out[u]
    return True

faces = {d: [] for d in range(4)}
for f in range(1, 1 << 16):
    members = [j for j in range(16) if f & (1 << j)]
    if len(members) <= 4 and ok(members):
        faces[len(members)-1].append(f)
assert [len(faces[d]) for d in range(4)] == [16,76,120,48]
face_idx = {d: {f:i for i,f in enumerate(layer)} for d,layer in faces.items()}

def boundary_matrix(d,prime):
    rows = [[0]*len(faces[d]) for _ in faces[d-1]]
    for j,mask in enumerate(faces[d]):
        bits = [b for b in range(16) if mask & (1 << b)]
        for k,b in enumerate(bits):
            i = face_idx[d-1][mask ^ (1 << b)]
            rows[i][j] = (1 if k%2==0 else -1) % prime
    return rows

def rref(rows,p):
    mat=[r[:] for r in rows]; nr=len(mat); nc=len(mat[0]); piv=[]; top=0
    for c in range(nc):
        q=next((i for i in range(top,nr) if mat[i][c]%p),None)
        if q is None: continue
        mat[top],mat[q]=mat[q],mat[top]
        v=pow(mat[top][c],-1,p)
        mat[top]=[(z*v)%p for z in mat[top]]
        for i in range(nr):
            if i!=top and mat[i][c]:
                t=mat[i][c]
                mat[i]=[(a-t*b)%p for a,b in zip(mat[i],mat[top])]
        piv.append(c);top+=1
        if top==nr:break
    return mat,piv

ranks=[]
for d in range(1,4):
    _,piv=rref(boundary_matrix(d,2),2)
    ranks.append(len(piv))
assert ranks == [15,61,40]
assert [len(faces[0])-1-ranks[0], len(faces[1])-ranks[0]-ranks[1],
        len(faces[2])-ranks[1]-ranks[2], len(faces[3])-ranks[2]] == [0,0,19,8]

P=101
reduced,pivots=rref(boundary_matrix(3,P),P)
assert len(pivots)==40
free=[j for j in range(len(faces[3])) if j not in pivots]
assert len(free)==8
kernel=[]
for f in free:
    v=[0]*len(faces[3]);v[f]=1
    for i,c in enumerate(pivots):v[c]=(-reduced[i][f])%P
    kernel.append(v)

def signed_image(mask,perm):
    mapping=[arcs.index((perm[u],perm[v])) for u,v in arcs]
    old=[j for j in range(16) if mask & (1 << j)]
    new=[mapping[j] for j in old]
    inversions=sum(x>y for i,x in enumerate(new) for y in new[i+1:])
    im=sum(1<<j for j in new)
    return im, (-1 if inversions%2 else 1)

records=[]
for kind in ('rotation','reflection'):
    for k in range(4):
        p=(0,)+tuple(1+((i+k)%4 if kind=='rotation' else (k-i)%4) for i in range(4))
        total=0
        for d in range(4):
            tr=sum(s for mask in faces[d] for im,s in [signed_image(mask,p)] if im==mask)
            total+=(-1)**d*tr
        total-=1 # reduced Euler trace, subtract augmentation
        toptrace=0
        for basis_idx,v in enumerate(kernel):
            newcoord=0
            target=free[basis_idx]
            for j,a in enumerate(v):
                if a:
                    im,sgn=signed_image(faces[3][j],p)
                    if face_idx[3][im]==target:newcoord+=a*sgn
            toptrace+=newcoord
        toptrace%=P
        if toptrace > P//2:toptrace-=P
        assert abs(toptrace)<=8
        records.append((kind,k,total+toptrace,toptrace))

assert [x[2] for x in records] == [19,-1,3,-1,1,1,1,1]
assert [x[3] for x in records] == [8,0,0,0,0,0,0,0]

# D4 irreducibles: four 1-dimensional characters r -> +/-1, s -> +/-1,
# plus the unique 2-dimensional geometric representation.
for degree in (2,3):
    chi=[x[degree] for x in records]
    mult={}
    for rr in (1,-1):
        for ss in (1,-1):
            numerator = sum(chi[k]*rr**k for k in range(4))
            numerator += sum(chi[k+4]*ss*rr**k for k in range(4))
            assert numerator%8 == 0
            mult[(rr,ss)]=numerator//8
    e=(chi[0]-chi[2])//4
    assert (chi[0]-chi[2])%4 == 0
    if degree==2:
        assert mult=={(1,1):3,(1,-1):2,(-1,1):3,(-1,-1):3} and e==4
    else:
        assert mult=={(1,1):1,(1,-1):1,(-1,1):1,(-1,-1):1} and e==2

print('CHARACTER_OK: ranks mod 2 d1=15,d2=61,d3=40; Betti 0,0,19,8.')
print('D4 character H2=(19,-1,3,-1;1,1,1,1); H3=(8,0,0,0;0,0,0,0).')
print('H3 is rational regular representation; H2 invariants 3, H3 invariants 1.')
