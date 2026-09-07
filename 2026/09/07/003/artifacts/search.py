#!/usr/bin/env python3
"""Heuristic search for low-rank J2-free diag-ones matrices, n=6..12.
Greedy + local search using exact Bareiss rank. Also verifies upper-bound construction.
"""
import random

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

def masks_to_mat(masks,n):
    return [[1 if (m>>j)&1 else 0 for j in range(n)] for m in masks]

def is_j2free(masks):
    n=len(masks)
    for i in range(n):
        for k in range(i+1,n):
            if bin(masks[i]&masks[k]).count('1')>=2: return False
    return True

def construct_upper(n):
    # 4-cycle tiling block diagonal
    masks=[]
    for i in range(n):
        q=i//4; r=i%4; rem=n-4*q
        if 4*q+4<=n:
            # full block of 4
            succ={0:1,1:2,2:3,3:0}[r]
            m=(1<<i)|(1<<(4*q+succ))
        else:
            m=(1<<i)
        masks.append(m)
    return masks

def check_upper(n):
    masks=construct_upper(n)
    M=masks_to_mat(masks,n)
    assert is_j2free(masks), f"construction not J2-free n={n}"
    r=bareiss_rank(M)
    import math
    target=math.ceil(3*n/4)
    print(f"n={n} construction rank={r} target<={target} {'OK' if r<=target else 'FAIL'} masks={[bin(m) for m in masks]}")
    return r

def random_j2free(n, p=0.15, tries=20000):
    best=None; bestm=None
    for _ in range(tries):
        masks=[(1<<i) for i in range(n)]
        # random order of off-diagonal edges, add if keeps J2-free
        edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
        random.shuffle(edges)
        for (i,j) in edges:
            if random.random()<p:
                if not (masks[i]>>j)&1:
                    new=masks[i]|(1<<j)
                    # check against all k != i
                    ok=True
                    for k in range(n):
                        if k==i: continue
                        if bin(new&masks[k]).count('1')>=2:
                            ok=False; break
                    if ok: masks[i]=new
        M=masks_to_mat(masks,n)
        r=bareiss_rank(M)
        if best is None or r<best:
            best=r; bestm=masks[:]
            if best<= (n//2):
                break
    return best,bestm

def local_search(n, init, iters=4000):
    masks=init[:]
    M=masks_to_mat(masks,n)
    best=bareiss_rank(M)
    cur=masks[:]; currank=best
    for it in range(iters):
        i=random.randrange(n); j=random.randrange(n)
        if i==j: continue
        newm=cur[:]
        if (newm[i]>>j)&1:
            newm[i]=newm[i]^(1<<j)
        else:
            cand=newm[i]|(1<<j)
            ok=True
            for k in range(n):
                if k==i: continue
                if bin(cand&newm[k]).count('1')>=2:
                    ok=False; break
            if not ok: continue
            newm[i]=cand
        M2=masks_to_mat(newm,n)
        r2=bareiss_rank(M2)
        if r2<=currank or random.random()<0.05:
            cur=newm; currank=r2
            if r2<best:
                best=r2; bestm=newm[:]
    return best

if __name__=="__main__":
    import math
    print("=== upper bound construction ===")
    for n in range(2,13):
        check_upper(n)
    print("=== random+local search for low rank ===")
    random.seed(0)
    for n in [6,7,8,9,10,12]:
        b,m=random_j2free(n, p=0.2, tries=3000)
        print(f"n={n} random best={b} ceil3n/4={math.ceil(3*n/4)} ceiln/2={math.ceil(n/2)}")
        # local improve from construction
        lb=local_search(n, construct_upper(n), iters=2000)
        print(f"  local-from-construction best={lb}")
        if m is not None:
            lb2=local_search(n, m, iters=2000)
            print(f"  local-from-random best={lb2}")
