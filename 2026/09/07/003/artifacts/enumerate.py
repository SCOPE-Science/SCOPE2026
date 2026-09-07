#!/usr/bin/env python3
"""Exhaustive enumeration of F_n for n<=5 with exact Bareiss rank.
Reproducible: stdlib only. Run: python3 enumerate.py
"""
import time

def bareiss_rank(mat):
    n = len(mat); m = len(mat[0]) if n else 0
    A = [row[:] for row in mat]
    rank = 0; prev = 1; row = 0
    for col in range(m):
        piv = None
        for i in range(row, n):
            if A[i][col] != 0:
                piv = i; break
        if piv is None:
            continue
        A[row], A[piv] = A[piv], A[row]
        for i in range(row+1, n):
            for j in range(col+1, m):
                A[i][j] = (A[i][j]*A[row][col] - A[i][col]*A[row][j]) // prev
            A[i][col] = 0
        prev = A[row][col]
        row += 1; rank += 1
        if row == n:
            break
    return rank

def row_masks_of(M):
    n = len(M); masks = []
    for i in range(n):
        m = 0
        for j in range(n):
            if M[i][j]:
                m |= (1 << j)
        masks.append(m)
    return masks

def is_j2free_masks(masks):
    n = len(masks)
    for i in range(n):
        for k in range(i+1, n):
            if bin(masks[i] & masks[k]).count('1') >= 2:
                return False
    return True

def gen_matrices(n):
    off = [(i, j) for i in range(n) for j in range(n) if i != j]
    N = len(off)
    for mask in range(1 << N):
        M = [[0]*n for _ in range(n)]
        for i in range(n):
            M[i][i] = 1
        for b, (i, j) in enumerate(off):
            if (mask >> b) & 1:
                M[i][j] = 1
        yield mask, M

def enumerate_n(n, collect_min=False, verbose=True):
    total = 0; survivors = 0
    rank_dist = {}; min_rank = n+1; nmin = 0
    min_masks = []
    for mask, M in gen_matrices(n):
        total += 1
        masks = row_masks_of(M)
        if not is_j2free_masks(masks):
            continue
        survivors += 1
        r = bareiss_rank(M)
        rank_dist[r] = rank_dist.get(r, 0)+1
        if r < min_rank:
            min_rank = r; nmin = 1
            min_masks = [(mask, [row[:] for row in M])]
        elif r == min_rank:
            nmin += 1
            if collect_min:
                min_masks.append((mask, [row[:] for row in M]))
    if verbose:
        print(f"n={n}: total={total} survivors={survivors} min_rank={min_rank} rank_dist={dict(sorted(rank_dist.items()))} n_min={nmin}", flush=True)
    return survivors, min_rank, rank_dist, min_masks, nmin

if __name__ == "__main__":
    for n in [2, 3, 4]:
        enumerate_n(n, collect_min=(n == 4))
    t0 = time.time()
    s, mr, rd, mm, nm = enumerate_n(5, collect_min=False)
    print(f"n=5 time {time.time()-t0:.1f}s")
