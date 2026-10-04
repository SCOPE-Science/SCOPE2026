#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction
from math import comb
P=1000003

def trans_map(v): return [x^v for x in range(16)]
def swap_map(i,j):
    out=[]
    for x in range(16):
        y=x; bi=(x>>i)&1; bj=(x>>j)&1
        if bi!=bj: y ^= (1<<i)|(1<<j)
        out.append(y)
    return out
def transvection_map(i,j):
    out=[]
    for x in range(16):
        y=x
        if (x>>j)&1: y ^= 1<<i
        out.append(y)
    return out
GENS=[trans_map(1<<i) for i in range(4)]
GENS += [swap_map(i,i+1) for i in range(3)]
GENS += [transvection_map(0,1),transvection_map(1,2),transvection_map(2,3),transvection_map(3,0)]

def act(mask,mp):
    out=0
    for x in range(16):
        if (mask>>x)&1: out |= 1<<mp[x]
    return out

def orbit(seed):
    seen={seed}; queue=[seed]
    for m in queue:
        for g in GENS:
            y=act(m,g)
            if y not in seen:
                seen.add(y); queue.append(y)
    return seen

def mask(S):
    return sum(1<<x for x in S)

S_plane=[0,1,2,3,4]
S_simplex=[0,1,2,4,8]
O1=orbit(mask(S_plane)); O2=orbit(mask(S_simplex))
assert len(O1)==1680 and len(O2)==2688 and O1.isdisjoint(O2)
assert len(O1|O2)==comb(16,5)==4368

W=[[1 if ((k & x).bit_count()&1)==0 else -1 for x in range(16)] for k in range(16)]

def rank_mod(rows):
    A=[[v%P for v in row] for row in rows]
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        iv=pow(A[r][c],P-2,P)
        for i in range(r+1,m):
            if A[i][c]:
                f=A[i][c]*iv%P
                for j in range(c,n):
                    A[i][j]=(A[i][j]-f*A[r][j])%P
        r+=1
        if r==n: break
    return r

def rref_q(rows):
    A=[[Fraction(v) for v in row] for row in rows]
    m=len(A); n=len(A[0]); r=0; pivs=[]
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        pv=A[r][c]
        A[r]=[z/pv for z in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        pivs.append(c); r+=1
        if r==m: break
    return A,pivs

def in_row_span(v,R,pivs):
    x=[Fraction(z) for z in v]
    for rr,c in enumerate(pivs):
        if x[c]:
            f=x[c]
            x=[x[j]-f*R[rr][j] for j in range(len(x))]
    return all(z==0 for z in x)

def census(S):
    rows=[[W[k][x] for x in S] for k in range(16)]
    out={"rank_deficient":0,"rank_distribution":{},"forced_time_zero":0,"forced_extra_fourier_zero":0,"admissible":0}
    for T in combinations(range(16),7):
        M=[rows[k] for k in T]
        if rank_mod(M)>=5:
            continue
        R,pivs=rref_q(M); rq=len(pivs)
        assert rq<5
        out["rank_deficient"]+=1
        out["rank_distribution"][rq]=out["rank_distribution"].get(rq,0)+1
        if any(in_row_span([1 if j==u else 0 for j in range(5)],R,pivs) for u in range(5)):
            out["forced_time_zero"]+=1
            continue
        st=set(T)
        if any(k not in st and in_row_span(rows[k],R,pivs) for k in range(16)):
            out["forced_extra_fourier_zero"]+=1
            continue
        out["admissible"]+=1
    return out

A=census(S_plane)
B=census(S_simplex)
assert A=={"rank_deficient":3248,"rank_distribution":{4:3200,3:48},"forced_time_zero":3184,"forced_extra_fourier_zero":64,"admissible":0},A
assert B=={"rank_deficient":160,"rank_distribution":{4:160},"forced_time_zero":160,"forced_extra_fourier_zero":0,"admissible":0},B
print('support_orbits',[(S_plane,1680),(S_simplex,2688)])
print('plane_plus_point',A)
print('affine_simplex',B)
print('seven_frequency_sets_per_rep',comb(16,7))
print('VERIFY_OK')
