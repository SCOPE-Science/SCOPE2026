#!/usr/bin/env python3
"""Classify minimizers and survivors up to simultaneous permutation; find minor certificates."""
import itertools

def bareiss_rank(mat):
    n=len(mat); m=len(mat[0]) if n else 0
    A=[row[:] for row in mat]
    rank=0; prev=1; row=0
    for col in range(m):
        piv=None
        for i in range(row,n):
            if A[i][col]!=0: piv=i; break
        if piv is None: continue
        A[row],A[piv]=A[piv],A[row]
        for i in range(row+1,n):
            for j in range(col+1,m):
                A[i][j]=(A[i][j]*A[row][col]-A[i][col]*A[row][j])//prev
            A[i][col]=0
        prev=A[row][col]; row+=1; rank+=1
        if row==n: break
    return rank

def bareiss_det_signed(mat):
    n=len(mat)
    if n==0: return 1
    A=[row[:] for row in mat]
    prev=1; sign=1
    for k in range(n-1):
        if A[k][k]==0:
            piv=None
            for i in range(k+1,n):
                if A[i][k]!=0: piv=i; break
            if piv is None: return 0
            A[k],A[piv]=A[piv],A[k]; sign=-sign
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*A[k][k]-A[i][k]*A[k][j])//prev
            A[i][k]=0
        prev=A[k][k]
        if prev==0: return 0
    return sign*A[n-1][n-1]

def row_masks_of(M):
    n=len(M); masks=[]
    for i in range(n):
        m=0
        for j in range(n):
            if M[i][j]: m|=(1<<j)
        masks.append(m)
    return masks

def is_j2free_masks(masks):
    n=len(masks)
    for i in range(n):
        for k in range(i+1,n):
            if bin(masks[i]&masks[k]).count('1')>=2: return False
    return True

def canon(M):
    n=len(M)
    best=None
    for p in itertools.permutations(range(n)):
        T=tuple(tuple(M[p[i]][p[j]] for j in range(n)) for i in range(n))
        if best is None or T<best: best=T
    return best

def mat_from_masks(masks,n):
    return [[1 if (m>>j)&1 else 0 for j in range(n)] for m in masks]

def enumerate_all(n):
    off=[(i,j) for i in range(n) for j in range(n) if i!=j]
    N=len(off)
    surv=[]; minlist=[]
    min_rank=n+1
    # first pass to get min rank already known; recompute ranks
    for mask in range(1<<N):
        M=[[0]*n for _ in range(n)]
        for i in range(n): M[i][i]=1
        for b,(i,j) in enumerate(off):
            if (mask>>b)&1: M[i][j]=1
        masks=row_masks_of(M)
        if not is_j2free_masks(masks): continue
        r=bareiss_rank(M)
        surv.append((mask,M,masks,r))
        if r<min_rank: min_rank=r
    minlist=[t for t in surv if t[3]==min_rank]
    return surv,minlist,min_rank

def analyze(n):
    surv,minlist,mr=enumerate_all(n)
    print(f"n={n} surv={len(surv)} min_rank={mr} nmin={len(minlist)}")
    # orbits of minimizers
    from collections import Counter
    orb={}
    for mask,M,masks,r in minlist:
        c=canon(M)
        orb.setdefault(c,[]).append((mask,M,masks))
    print(f"  minimizer orbits under simultaneous perm: {len(orb)}")
    for c,lst in sorted(orb.items(), key=lambda x:-len(x[1])):
        repM=[list(row) for row in c]
        print(f"   orbit size {len(lst)} rep:")
        for row in repM: print("     "+" ".join(map(str,row)))
        # row weights
        print(f"     row masks {[bin(m).count('1') for m in row_masks_of(repM)]} rank {bareiss_rank(repM)}")
    # orbits of all survivors (for n<=5)
    orb2={}
    for mask,M,masks,r in surv:
        c=canon(M)
        orb2.setdefault(c,[]).append((mask,M,masks,r))
    print(f"  all-survivor orbits: {len(orb2)}")
    # for n=5: find nonsingular 4x4 minor per orbit
    if n==5:
        import itertools as it
        bad=0
        for c,lst in orb2.items():
            mask,M,masks,r=lstm=lst[0]
            found=None
            for rows in it.combinations(range(5),4):
                for cols in it.combinations(range(5),4):
                    sub=[[M[i][j] for j in cols] for i in rows]
                    d=bareiss_det_signed(sub)
                    if d!=0:
                        found=(rows,cols,d); break
                if found: break
            if found is None:
                bad+=1
                print("  NO MINOR for orbit rep",c)
        print(f"  orbits without 4x4 nonsingular minor: {bad} (must be 0 to certify r>=4)")
    return surv,minlist,orb,orb2

if __name__=="__main__":
    for n in [4,5]:
        analyze(n)
