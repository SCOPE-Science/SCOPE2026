#!/usr/bin/env python3
"""Exact integer calculation for transposition-fixed antichain complexes."""
import itertools, math, time
from sympy import SparseMatrix,ZZ
from sympy.matrices.normalforms import smith_normal_form

def complex_faces(n):
    orbits=[('D',i,i) for i in range(1,n+1)]+[('P',i,j) for i in range(1,n+1) for j in range(i+1,n+1)]
    def valid(a,b):
        if a[0]=='D' and b[0]=='D': return False
        if a[0]=='D':return b[1]<a[1]<b[2]
        if b[0]=='D':return a[1]<b[1]<a[2]
        return (a[1]<b[1] and b[2]<a[2]) or (b[1]<a[1] and a[2]<b[2])
    faces=[]
    for k in range(1,n//2+2):
        F=[tuple(combo) for combo in itertools.combinations(orbits,k) if all(valid(a,b) for a,b in itertools.combinations(combo,2))]
        if not F:break
        faces.append(F)
        assert len(F)==math.comb(n,2*k-1)+ (math.comb(n,2*k) if 2*k<=n else 0)
    assert sum(map(len,faces))==2**n-1
    return faces

def boundary(faces,k):
    # k index 0=0-faces, k=1=1-faces, etc; ∂_k:C_k->C_{k-1}
    rows={f:i for i,f in enumerate(faces[k-1])}
    D={}
    for j,f in enumerate(faces[k]):
        for p in range(k+1):
            g=f[:p]+f[p+1:]; D[(rows[g],j)]=(-1)**p
    return SparseMatrix(len(faces[k-1]),len(faces[k]),D)

def rank_mod2(D):
    bas={}
    for c in range(D.cols):
        s=0
        for (r,col),value in D.todok().items():
            if col==c and int(value)%2:s^=1<<r
        while s:
            p=s.bit_length()-1
            if p not in bas:bas[p]=s;break
            s^=bas[p]
    return len(bas)

def invariants(D):
    t=time.monotonic()
    S=smith_normal_form(D,domain=ZZ)
    v=[abs(int(S[i,i])) for i in range(min(S.rows,S.cols)) if S[i,i]]
    print(' SNF',D.shape,'rank',len(v),'counts', {x:v.count(x) for x in set(v)},'seconds',round(time.monotonic()-t,2),flush=True)
    return v

if __name__=='__main__':
    for n in range(3,9):
        f=complex_faces(n)
        B=[None]+[boundary(f,k) for k in range(1,len(f))]
        ranks=[0]+[rank_mod2(x) for x in B[1:]]+[0]
        betti=[len(f[k])-ranks[k]-ranks[k+1] for k in range(len(f))]
        betti[0]-=1
        print('n',n,'f',list(map(len,f)),'ranks',ranks,'reduced_betti_F2',betti,flush=True)
        for k in range(1,len(B)):
            v=invariants(B[k]);assert len(v)==ranks[k] and set(v)=={1}
        if n==8:
            assert list(map(len,f))==[36,126,84,9]
            assert ranks==[0,31,67,9,0]
            assert betti==[4,28,8,0]
    print('PASS complete',flush=True)
