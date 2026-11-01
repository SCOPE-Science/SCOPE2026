#!/usr/bin/env python3
"""Exact finite rational-homology and character verifier for PG(2,3) cap complex.
Uses Python standard library only; no external inputs or research services.
"""
from itertools import product, combinations
from collections import defaultdict

P=3

def norm(v):
    j=next(a for a in v if a)
    return tuple((a*(1 if j==1 else 2))%3 for a in v)

points=sorted({norm(v) for v in product(range(3),repeat=3) if any(v)})
assert len(points)==13
index={p:i for i,p in enumerate(points)}

def det(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]))%3

bad={frozenset(t) for t in combinations(range(13),3) if det(*(points[i] for i in t))==0}
assert len(bad)==52
faces={k:[t for t in combinations(range(13),k+1) if not any(b.issubset(t) for b in bad)] for k in range(5)}
assert tuple(len(faces[k]) for k in range(5))==(13,78,234,234,0)

# The 1-skeleton is complete. A missing triangle is collinear, and any
# point off its line cones its boundary with three allowed triangles.
# Thus H1=0 and boundary_2 has rank 78-13+1=66 over Q.
face2_index={f:i for i,f in enumerate(faces[2])}
cols=[]
for tet in faces[3]:
    col={face2_index[tet[:j]+tet[j+1:]]:(-1)**j for j in range(4)}
    assert len(col)==4
    cols.append(col)

def rank_mod(q):
    piv={}
    for col in cols:
        v={k:a%q for k,a in col.items()}
        while v:
            r=min(v)
            if r not in piv:
                inv=pow(v[r],-1,q)
                piv[r]={i:(a*inv)%q for i,a in v.items()}
                break
            p=piv[r]
            a=v[r]
            for j,b in p.items():
                z=(v.get(j,0)-a*b)%q
                if z:v[j]=z
                else:v.pop(j,None)
    return len(piv)

rank_101=rank_mod(101)
rank_1009=rank_mod(1009)
assert (rank_101,rank_1009)==(168,168)
# Image(boundary_3) is contained in ker(boundary_2), dim_Q ker=234-66=168.
# A rank-168 minor mod 101 therefore forces rank_Q=168, and H2(Q)=0.
# Since no 4-faces, H3(Q) has dimension 234-168=66.

# Full PGL_3(F_3), represented by unique scalar-normalized 3x3 matrices.
def perm_matrix(A):
    image=[]
    for v in points:
        u=tuple(sum(A[3*r+c]*v[c] for c in range(3))%3 for r in range(3))
        image.append(index[norm(u)])
    return tuple(image)

def sign_of_image(seq):
    return -1 if sum(a>b for i,a in enumerate(seq) for b in seq[i+1:])%2 else 1

def red_lefschetz(perm):
    z=-1
    for d,Flist in faces.items():
        if d==4:continue
        alt=1 if d%2==0 else -1
        for F in Flist:
            im=tuple(perm[i] for i in F)
            if set(im)==set(F):z+=alt*sign_of_image(im)
    return z

def cycle_type(perm):
    seen=set();typ=[]
    for a in range(13):
        if a in seen:continue
        b=a;c=0
        while b not in seen:
            seen.add(b);c+=1;b=perm[b]
        typ.append(c)
    return tuple(sorted(typ))

seen=set(); classes=defaultdict(lambda:[0,set(),set()]); bad_chars=[]
for A in product(range(3),repeat=9):
    if next((x for x in A if x!=0),0)!=1:continue
    if det((A[0],A[3],A[6]),(A[1],A[4],A[7]),(A[2],A[5],A[8]))==0:continue
    perm=perm_matrix(A)
    assert perm not in seen
    seen.add(perm)
    top_trace=-red_lefschetz(perm)
    fixed=sum(perm[i]==i for i in range(13))
    fixed2=sum(perm[perm[i]]==i for i in range(13))
    wedge_trace=((fixed-1)**2-(fixed2-1))//2
    cls=cycle_type(perm)
    classes[cls][0]+=1
    classes[cls][1].add(top_trace)
    classes[cls][2].add(wedge_trace)
    if top_trace!=wedge_trace:bad_chars.append((cls,top_trace,wedge_trace))
assert len(seen)==(27-1)*(27-3)*(27-9)//2==5616
assert not bad_chars
assert len(classes)==8
assert sum(c[0] for c in classes.values())==5616
assert sum(c[0]*next(iter(c[1])) for c in classes.values())==0
print('PG23_POINTS 13')
print('COLLINEAR_TRIPLES 52')
print('FACE_COUNTS_0_TO_4 13,78,234,234,0')
print('BOUNDARY_2_RANK_Q 66 (complete graph and off-line cone)')
print('BOUNDARY_3_RANK_MOD_101',rank_101)
print('BOUNDARY_3_RANK_MOD_1009',rank_1009)
print('RATIONAL_REDUCED_BETTI_0_TO_3 0,0,0,66')
print('PROJECTIVE_LINEAR_GROUP_ORDER',len(seen))
for cls in sorted(classes):
    n,actual,pred=classes[cls]
    assert len(actual)==len(pred)==1
    print('CLASS',','.join(map(str,cls)),'SIZE',n,'H3_TRACE',next(iter(actual)),'EXTERIOR_TRACE',next(iter(pred)))
print('FULL_CHARACTER_EQUALITY_OK')
print('GLOBAL_INVARIANTS 0')
print('VERIFY_OK')
