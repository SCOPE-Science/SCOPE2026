"""Verify the K_{d,d} girth obstruction algebraically: odd-product system on 4-cycles has no solution."""
import itertools

def check_kdd(d):
    L = [f"a{i}" for i in range(d)]
    R = [f"b{j}" for j in range(d)]
    # variables x[i][j]; equations: x[i][j]+x[i][l]+x[k][j]+x[k][l]=1 for i<k,j<l
    # Gaussian elimination over F2
    import numpy as np
    var = {(i,j):i*d+j for i in range(d) for j in range(d)}
    n = d*d
    rows = []
    for i in range(d):
        for k in range(i+1,d):
            for j in range(d):
                for l in range(j+1,d):
                    r = [0]*n
                    for v in [(i,j),(i,l),(k,j),(k,l)]:
                        r[var[v]] ^= 1
                    rows.append((r,1))
    # use triple (a0,a1,e) x (c,d) subsystem for the short unsatisfiability witness
    # submatrix rows R12,R13,R23 on cols {a0c,a0d,a1c,a1d,ec,ed}: rank check + augmented rank
    # full elimination:
    M = [r+[b] for r,b in rows]
    piv=0
    where=[-1]*n
    for c in range(n):
        f = next((r for r in range(piv,len(M)) if M[r][c]),None)
        if f is None: continue
        M[piv],M[f]=M[f],M[piv]; where[c]=piv
        for r in range(len(M)):
            if r!=piv and M[r][c]:
                M[r]=[(a^b) for a,b in zip(M[r],M[piv])]
        piv+=1
    for r in range(piv,len(M)):
        if M[r][n]==1 and all(v==0 for v in M[r][:n]):
            return False, len(rows), "0=1 derived: system UNSATISFIABLE"
    return True, len(rows), "satisfiable"

for d in [2,3,4]:
    print("K%d,%d:"%(d,d), check_kdd(d))
