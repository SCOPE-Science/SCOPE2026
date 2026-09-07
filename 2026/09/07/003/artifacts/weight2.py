#!/usr/bin/env python3
"""Exhaust weight<=2 case: f:[n]->[n], no 2-cycles. Find min rank."""
import itertools, math, random

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

def min_rank_weight2(n, sample=None):
    # iterate over all f if n<=7 else sample
    best=n+1; bestex=None; count=0; nmin=0
    if sample is None:
        # full enumeration n^n
        total=n**n
        print(f"n={n} enumerating {total} functions...")
        for code in range(total):
            f=[]; t=code
            for i in range(n):
                f.append(t % n); t//=n
            # no 2-cycles among off-diagonal: if f[i]!=i and f[f[i]]==i and f[i]... need f[i]!=i, f[k]!=k? Actually 2-cycle requires f[i]=k,f[k]=i with i!=k (both off-diag automatically)
            bad=False
            for i in range(n):
                k=f[i]
                if k!=i and f[k]==i and k>i:  # count each once; but need to skip (both directions same) — just forbid
                    bad=True; break
            if bad: continue
            count+=1
            M=[[0]*n for _ in range(n)]
            for i in range(n):
                M[i][i]=1
                if f[i]!=i: M[i][f[i]]=1
            r=bareiss_rank(M)
            if r<best:
                best=r; bestex=(f[:],[row[:] for row in M]); nmin=1
            elif r==best:
                nmin+=1
        print(f"n={n} weight<=2: valid={count} min_rank={best} nmin={nmin} ceil3n/4={math.ceil(3*n/4)} ceiln/2={math.ceil(n/2)}")
        if bestex: print(f"  example f={bestex[0]}")
        return best
    else:
        best=n+1; bestex=None
        for _ in range(sample):
            f=[random.randrange(n) for _ in range(n)]
            bad=False
            for i in range(n):
                k=f[i]
                if k!=i and f[k]==i and k>i: bad=True; break
            if bad: continue
            M=[[0]*n for _ in range(n)]
            for i in range(n):
                M[i][i]=1
                if f[i]!=i: M[i][f[i]]=1
            r=bareiss_rank(M)
            if r<best: best=r; bestex=f[:]
        print(f"n={n} sampled weight<=2: min_rank={best} ceil3n/4={math.ceil(3*n/4)}")
        return best

if __name__=="__main__":
    for n in [6,7,8]:
        min_rank_weight2(n)
    # larger sampled
    random.seed(1)
    for n in [9,10,12]:
        min_rank_weight2(n, sample=300000)
