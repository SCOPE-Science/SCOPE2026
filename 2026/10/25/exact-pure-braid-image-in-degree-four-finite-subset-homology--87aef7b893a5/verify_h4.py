#!/usr/bin/env python3
"""Exact finite check of the degree-four pure-braid image formula.

For H_4(exp_4 Gamma_n), the only potentially nonzero corrections from a
pure generator are on cycles a_i*a_j*b_k with i,j,k distinct.  The script
builds the two-dimensional cycle space for each triple, applies each
standard pure-generator translation, and computes the exact rank of the
resulting operator family using rational Gaussian elimination.
The symbolic proof in RESULT.md establishes the formula for every n.
"""
from itertools import combinations
from fractions import Fraction


def exterior_product(mask1, mask2):
    if mask1 & mask2:
        return 0, 0
    inversions = 0
    for i in range(mask1.bit_length()):
        if (mask1 >> i) & 1:
            inversions += (mask2 & ((1 << i) - 1)).bit_count()
    sign = -1 if inversions % 2 else 1
    return mask1 | mask2, sign


def wedge3_cycle_basis(i, j, k):
    # x1=a_i a_j b_k, x2=a_i a_k b_j, x3=a_j a_k b_i.
    # Their boundaries are proportional to (1,-1,1), so these two
    # independent cycles span the kernel: x1+x2 and x1-x3.
    return [((i, j, k, 1), (i, k, j, 1)), ((i, j, k, 1), (j, k, i, -1))]


def term_correction(term, pair, n):
    # term=(i,j,k,coefficient) represents coefficient*a_i*a_j*b_k,
    # with i<j. For A_pq, b_p -> b_p -2 a_p a_q and
    # b_q -> b_q +2 a_p a_q.
    i,j,k,coef=term
    p,q=pair
    if k not in pair:
        return {}
    c=-2 if k==p else 2
    mask=(1<<i)|(1<<j)
    pairmask=(1<<p)|(1<<q)
    outmask,sgn=exterior_product(mask,pairmask)
    if not sgn:
        return {}
    return {outmask:coef*c*sgn}


def add_vectors(a,b):
    r=dict(a)
    for key,val in b.items():
        r[key]=r.get(key,0)+val
        if r[key]==0: del r[key]
    return r


def operator_column(n, pair, triples, foursets):
    # Flatten outputs for each (triple, one of its two cycle basis vectors,
    # four-set output). The remaining degree-four cycles are killed by all
    # translations, so these rows capture the complete operator.
    col=[]
    four_index={sum(1<<i for i in S):idx for idx,S in enumerate(foursets)}
    for i,j,k in triples:
        for cyc in wedge3_cycle_basis(i,j,k):
            out={}
            for term in cyc:
                out=add_vectors(out,term_correction(term,pair,n))
            for mask in four_index:
                col.append(out.get(mask,0))
    return col


def rank_q(matrix):
    if not matrix: return 0
    A=[[Fraction(x) for x in row] for row in matrix]
    m,n=len(A),len(A[0])
    r=0
    for c in range(n):
        pivot=next((i for i in range(r,m) if A[i][c]),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        p=A[r][c]
        A[r]=[x/p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]
                A[i]=[x-q*y for x,y in zip(A[i],A[r])]
        r+=1
        if r==m: break
    return r


def check(n):
    pairs=list(combinations(range(n),2))
    triples=list(combinations(range(n),3))
    foursets=list(combinations(range(n),4))
    cols=[operator_column(n,p,triples,foursets) for p in pairs]
    if not cols:
        return 0
    # Columns are the flattened operator matrices. Compute rank by rows.
    matrix=[list(row) for row in zip(*cols)] if cols[0] else []
    r=rank_q(matrix)
    expected=0 if n<=3 else len(pairs)-1
    if r!=expected:
        raise SystemExit(f"n={n}: rank {r}, expected {expected}")
    if n>=4:
        # The all-ones relation is in the kernel, and rank N-1 means it is
        # the entire rational kernel. Verify the sum column-by-column is zero.
        if any(sum(col[j] for col in cols)!=0 for j in range(len(cols[0]))):
            raise SystemExit(f"n={n}: all-ones relation failed")
    return r


def main():
    for n in range(2,9):
        r=check(n)
        print(f"n={n}: dim(image span)={r}")
    print("VERIFY_OK_DEGREE_FOUR_PURE_BRAID_IMAGE")

if __name__=='__main__': main()
