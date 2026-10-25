#!/usr/bin/env python3
"""Exact finite checks for colored-path independence-complex characters.

Standard-library only. The homological verification uses field arithmetic modulo
101 and 103; the general representation statement is proved separately.
"""
from collections import Counter
from itertools import combinations, product
from math import comb


def choose(a,b):
    return comb(a,b) if a>=0 and 0<=b<=a else 0


def link_contributions(m):
    """Return (degree, number of augmentation factors) multiplicities."""
    out=Counter()
    for mask in range(1<<m):
        if mask&(mask<<1):
            continue
        closed=(mask|(mask<<1)|(mask>>1))&((1<<m)-1)
        blocks=[]
        i=0
        while i<m:
            if (closed>>i)&1:
                i+=1
                continue
            j=i
            while j<m and not ((closed>>j)&1):
                j+=1
            blocks.append(j-i)
            i=j
        if any(b%3==1 for b in blocks):
            continue
        q=mask.bit_count()+sum((b+1)//3 for b in blocks)-1
        out[(q,mask.bit_count())]+=1
    return out


def closed_coefficients(m):
    out=Counter()
    for d in range(m+1):
        for p in range(d+2):
            k=choose(p+1,3*(d+1)-m)*choose(d+1,p)
            if k:out[(d,p)]=k
    return out


def enumerate_faces(m,n):
    """Ordered tuples (position, color), with no adjacent positions."""
    by_degree={-1:[()]}
    for size in range(1,(m+1)//2+1):
        ff=[]
        for pos in combinations(range(m),size):
            if any(pos[i+1]==pos[i]+1 for i in range(size-1)):
                continue
            for colors in product(range(n), repeat=size):
                ff.append(tuple(zip(pos,colors)))
        if ff: by_degree[size-1]=ff
    return by_degree


def image_face(face,flip_positions):
    return tuple((p,1-c if p in flip_positions else c) for p,c in face)


def orbit_eigen_bases(faces, flip_positions, eig):
    """Basis vectors are representatives ± their involutive images."""
    seen=set(); reps=[]; face_to_rep={}
    for face in faces:
        if face in seen:continue
        mate=image_face(face,flip_positions)
        assert mate in faces
        seen.add(face);seen.add(mate)
        if eig==-1 and mate==face:continue
        rep=min(face,mate)
        reps.append(rep)
    return reps, {f:i for i,f in enumerate(reps)}


def sparse_rank(columns,mod):
    pivots={}
    for vec in columns:
        v={r:(x%mod) for r,x in vec.items() if x%mod}
        while v:
            piv=min(v)
            if piv not in pivots:
                scale=pow(v[piv],-1,mod)
                pivots[piv]={r:(x*scale)%mod for r,x in v.items() if x%mod}
                break
            pc=pivots[piv];a=v[piv]
            for r,x in pc.items():
                z=(v.get(r,0)-a*x)%mod
                if z:v[r]=z
                else:v.pop(r,None)
    return len(pivots)


def graded_eigenspace_homology(m,n,flip_positions,mod=101):
    assert n==2  # involution exchanges both colors in selected fibers
    by_degree=enumerate_faces(m,n)
    dims={};ranks={}
    for eig in (1,-1):
        basis={}
        face_idx={}
        for deg,faces in by_degree.items():
            basis[deg],face_idx[deg]=orbit_eigen_bases(faces,flip_positions,eig)
        for deg, reps in basis.items():
            if deg==-1:
                ranks[(eig,deg)]=0
                continue
            cols=[]
            targets=face_idx[deg-1]
            for face in reps:
                mate=image_face(face,flip_positions)
                terms=[(face,1)]
                if mate!=face:terms.append((mate,eig))
                coeffs=Counter()
                for face2, coeff in terms:
                    for j in range(len(face2)):
                        f=face2[:j]+face2[j+1:]
                        if f in targets:
                            coeffs[targets[f]]+=coeff*(-1 if j%2 else 1)
                cols.append(coeffs)
            ranks[(eig,deg)]=sparse_rank(cols,mod)
        for deg, reps in basis.items():
            if deg<0:continue
            dims[(eig,deg)]=(len(reps)-ranks[(eig,deg)]-ranks.get((eig,deg+1),0))
    return {d:(dims.get((1,d),0),dims.get((-1,d),0)) for d in range(m)}


def predicted_characters(m,n,flip_positions):
    out=Counter()
    for mask in range(1<<m):
        if mask&(mask<<1):continue
        closed=(mask|(mask<<1)|(mask>>1))&((1<<m)-1)
        blocks=[];i=0
        while i<m:
            if (closed>>i)&1:i+=1;continue
            j=i
            while j<m and not((closed>>j)&1):j+=1
            blocks.append(j-i);i=j
        if any(b%3==1 for b in blocks):continue
        d=mask.bit_count()+sum((b+1)//3 for b in blocks)-1
        trace=1
        dim=1
        for i in range(m):
            if (mask>>i)&1:
                dim*=n-1
                trace*=-1 if i in flip_positions else n-1
        out[(d,'trace')]+=trace
        out[(d,'dim')]+=dim
    return out


def check():
    # Coefficients are recovered independently by enumerating every link in each base path.
    count=0
    for m in range(4,17):
        a=link_contributions(m)
        b=closed_coefficients(m)
        assert a==b,(m,a,b)
        count+=sum(a.values())
    print('LINK_COEFFICIENTS_OK',13,'path_lengths',count,'contributing_links')
    # Genuine homology calculation in both character eigenspaces on the face chains.
    checked=0
    for m in range(4,8):
        for flips in [set(),{0},{m//2},{0,m-1},set(range(m))]:
            pred=predicted_characters(m,2,flips)
            for mod in (101,103):
                dims=graded_eigenspace_homology(m,2,flips,mod)
                for d in range(m):
                    plus,minus=dims.get(d,(0,0))
                    assert plus+minus==pred[(d,'dim')],(m,flips,mod,d,dims,pred)
                    assert plus-minus==pred[(d,'trace')],(m,flips,mod,d,dims,pred)
                checked+=1
    print('INDEPENDENT_EIGEN_HOMOLOGY_OK',checked,'involution/field_cases')
    # Direct Lefschetz chain traces for uniform permutations for several fiber sizes.
    charchecks=0
    for m in range(4,9):
        for n in (2,3,4):
            bydeg=enumerate_faces(m,n)
            for f in range(n+1):
                if f==n-1:continue  # permutations cannot fix exactly n-1 elements
                # Combinatorial invariant face: each occupied fiber must use a fixed color.
                lef=0
                for deg,faces in bydeg.items():
                    if deg==-1:
                        lef+=-1
                        continue
                    left=sum(1 for face in faces if all(c<f for _,c in face))
                    lef+=(-1)**deg*left
                exp=sum((-1)**d*k*(f-1)**p for (d,p),k in closed_coefficients(m).items())
                # reduced Lefschetz on chains equals reduced Lefschetz on homology
                assert lef==exp,(m,n,f,lef,exp)
                charchecks+=1
    print('SIGNED_EULER_CHARACTERS_OK',charchecks)
    print('LEXICOGRAPHIC_PATH_EQUIVARIANT_HOMOLOGY_VERIFIED')

if __name__=='__main__':check()
