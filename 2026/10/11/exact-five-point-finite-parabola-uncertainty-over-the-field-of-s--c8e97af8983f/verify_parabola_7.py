#!/usr/bin/env python3
"""Exact cyclotomic certificate for five-term parabola Fourier sums over F_7.

Only Python standard-library integer arithmetic is used.  Each element of
Z[zeta_7] is stored as a seven-entry cyclic coefficient vector.  Such a
vector is zero at zeta_7 exactly when all its seven entries are equal.
"""
import itertools
from collections import Counter

P = 7
R = (2, 3, 4, 5, 6)
POINTS = tuple((a, b) for a in range(P) for b in range(P))
E = tuple(tuple((a*x*x + b*x) % P for x in R) for a,b in POINTS)
PERMS = {}
for size in (3, 4, 5):
    perms = []
    for t in itertools.permutations(range(size)):
        inversions = sum(t[i] > t[j] for i in range(size) for j in range(i+1,size))
        perms.append((t, -1 if inversions % 2 else 1))
    PERMS[size] = tuple(perms)

def det_poly(row_ids, col_ids):
    n=len(row_ids)
    result=[0]*7
    sub=[tuple(E[r][c] for c in col_ids) for r in row_ids]
    for perm,sgn in PERMS[n]:
        exponent=sum(sub[i][perm[i]] for i in range(n)) % 7
        result[exponent]+=sgn
    return tuple(result)

def is_zero(a):
    return min(a)==max(a)

def det_mod29(row_ids):
    # Homomorphism Z[zeta_7] -> F_29 with zeta_7 mapped to 16.
    n=len(row_ids); powers=[pow(16,k,29) for k in range(7)]
    mat=[[powers[E[r][c]] for c in range(n)] for r in row_ids]
    d=1
    for j in range(n):
        pivot=next((i for i in range(j,n) if mat[i][j]),None)
        if pivot is None: return 0
        if pivot!=j:
            mat[j],mat[pivot]=mat[pivot],mat[j]
            d=(-d)%29
        v=mat[j][j]
        d=d*v%29
        inv=pow(v,-1,29)
        for i in range(j+1,n):
            w=mat[i][j]*inv%29
            if w:
                for k in range(j+1,n):
                    mat[i][k]=(mat[i][k]-w*mat[j][k])%29
                mat[i][j]=0
    return d

def any_nonzero_minor(rows,cols,n):
    for rr in itertools.combinations(rows,n):
        for cc in itertools.combinations(cols,n):
            if not is_zero(det_poly(rr,cc)):return True
    return False

def kernel_cofactors(four_rows):
    out=[]
    for excluded in range(5):
        cols=tuple(c for c in range(5) if c!=excluded)
        h=det_poly(four_rows,cols)
        out.append(tuple((-1 if excluded%2 else 1)*v for v in h))
    return tuple(out)

def value_zero(row,vec):
    h=[0]*7
    for col,c in enumerate(vec):
        shift=E[row][col]
        for k,ck in enumerate(c):
            h[(k+shift)%7]+=ck
    return is_zero(h)

def run():
    stats=Counter()
    witness=None
    for tail in itertools.combinations(range(1,49),4):
        rows=(0,)+tail
        if det_mod29(rows):
            stats['modular_full_rank']+=1
            continue
        stats['modular_singular']+=1
        if not is_zero(det_poly(rows,tuple(range(5)))):
            stats['modular_false_positive']+=1
            continue
        stats['exact_singular']+=1
        row_four=None
        for rr in itertools.combinations(rows,4):
            if any(not is_zero(h) for h in kernel_cofactors(rr)):
                row_four=rr
                break
        if row_four is not None:
            stats['rank_four']+=1
            vec=kernel_cofactors(row_four)
            if any(is_zero(c) for c in vec):
                stats['rank_four_forces_zero_coefficient']+=1
                continue
            stats['rank_four_full_support']+=1
            roots=tuple(i for i in range(49) if value_zero(i,vec))
            if len(roots)!=5 or any(r not in roots for r in rows):
                raise AssertionError(('unexpected zero set',rows,roots))
            if witness is None:
                witness=(rows,row_four,roots,vec)
            continue
        # Every 4x4 minor vanishes: rank <=3. A three-by-three
        # minor and a dispensable column certify a forced zero.
        cols=tuple(range(5))
        if not any_nonzero_minor(rows,cols,3):
            raise AssertionError(('rank at most two',rows))
        forced=next((j for j in cols if not any_nonzero_minor(rows,tuple(c for c in cols if c!=j),3)),None)
        if forced is None:
            raise AssertionError(('rank-three full-support possibility',rows))
        stats['rank_three_forces_zero_coefficient']+=1
    assert stats['modular_full_rank']+stats['modular_singular']==194580
    assert stats['exact_singular']==5460,stats
    assert stats['rank_four_full_support']==330,stats
    assert stats['rank_three_forces_zero_coefficient']==45,stats
    assert witness is not None
    print('EXACT_CERTIFICATE_PASS')
    print('COUNTS',dict(stats))
    print('WITNESS_ROWS',tuple(POINTS[i] for i in witness[0]))
    print('WITNESS_FOUR_ROWS',tuple(POINTS[i] for i in witness[1]))
    print('WITNESS_COEFFICIENTS',witness[3])
    print('EXACT_FIVE_ZEROS',tuple(POINTS[i] for i in witness[2]))

if __name__ == '__main__':run()
