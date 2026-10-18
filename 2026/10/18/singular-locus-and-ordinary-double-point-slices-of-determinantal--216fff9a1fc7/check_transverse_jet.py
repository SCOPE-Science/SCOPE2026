#!/usr/bin/env python3
"""Exact modular linear-algebra checks for rank-one determinantal first jets.

The checks supplement the characteristic-zero proof and use prime 101 only
for rank calculations; they are not a substitute for the general proof.
"""
from itertools import combinations

P = 101

def rank_mod(matrix, p=P):
    if not matrix:
        return 0
    rows = [list(map(lambda a: a % p, row)) for row in matrix]
    n = len(rows[0]); r = 0
    for c in range(n):
        pivot = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        inv = pow(rows[r][c], -1, p)
        rows[r] = [(z * inv) % p for z in rows[r]]
        for i in range(r + 1, len(rows)):
            z = rows[i][c]
            if z:
                rows[i] = [(x - z*y) % p for x,y in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r

def determin2(A, i, j, k, l):
    return A[i][k]*A[j][l]-A[i][l]*A[j][k]

def e_linear_rows(Y):
    m = len(Y); n = len(Y[0]); out=[]
    for i,j in combinations(range(m),2):
        for k,l in combinations(range(n),2):
            row = [0]*(m*n)
            row[j*n+l] += Y[i][k]
            row[i*n+k] += Y[j][l]
            row[j*n+k] -= Y[i][l]
            row[i*n+l] -= Y[j][k]
            out.append(row)
    return out

def psi_linear_rows(Y):
    m = len(Y); n = len(Y[0]); out=[]
    for rs in combinations(range(m),3):
        for cs in combinations(range(n),3):
            row=[0]*(m*n)
            for a in range(3):
                for b in range(3):
                    rr=[u for ix,u in enumerate(rs) if ix!=a]
                    cc=[v for ix,v in enumerate(cs) if ix!=b]
                    cofactor = ((-1)**(a+b))*determin2(Y,*rr,*cc)
                    row[rs[a]*n+cs[b]] += cofactor
            out.append(row)
    return out

def run():
    total=0
    for m in range(3,7):
        for n in range(m,7):
            for r in (1,2):
                Y = [[int(i==j and i<r) for j in range(n)] for i in range(m)]
                e_rank=rank_mod(e_linear_rows(Y))
                psi_rank=rank_mod(psi_linear_rows(Y))
                if r == 2:
                    assert e_rank == m*n-3, (m,n,r,e_rank)
                    assert psi_rank == (m-2)*(n-2), (m,n,r,psi_rank)
                    tangent_dim=2*m*n-e_rank-psi_rank
                    assert tangent_dim == 2*(m+n-1)+1
                else:
                    assert e_rank == (m-1)*(n-1), (m,n,r,e_rank)
                    assert psi_rank == 0
                    tangent_dim=2*m*n-e_rank
                    assert tangent_dim>2*(m+n-1)
                total+=1
            print(f"m={m}, n={n}: rank-two transverse tangent excess 1; rank-one fiber singular")
    print(f"PASS: {total} exact finite-field rank checks at p={P}; general proof is separate")

if __name__ == '__main__': run()
