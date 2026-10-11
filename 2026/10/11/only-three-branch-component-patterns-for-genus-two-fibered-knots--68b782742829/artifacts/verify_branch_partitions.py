#!/usr/bin/env python3
from itertools import permutations
from collections import Counter, defaultdict

N=6

# Quotient V = E/<1>, where E is the even-weight subspace of F_2^6.
# Represent a class by four coordinates q_i=x_i+x_4, i=0..3,
# after using coordinates x_0,...,x_4 on E with x_5=sum_{0..4} x_i.

def cycle_type(p):
    seen=[False]*N
    out=[]
    for i in range(N):
        if not seen[i]:
            j=i; k=0
            while not seen[j]:
                seen[j]=True; k+=1; j=p[j]
            out.append(k)
    return tuple(sorted(out, reverse=True))

def mat_for_perm(p):
    # basis b_i=e_i+e_5 for E, i=0..4. columns are E-coordinates.
    A5=[[0]*5 for _ in range(5)]
    for k in range(5):
        y=[0]*6
        y[p[k]] ^= 1
        y[p[5]] ^= 1
        # E-coordinate c_i=y_i for i=0..4
        for i in range(5):
            A5[i][k]=y[i]
    A4=[[0]*4 for _ in range(4)]
    for k in range(4):
        y=[A5[i][k] for i in range(5)]
        for i in range(4):
            A4[i][k]=y[i]^y[4]
    return A4

def rank2(M):
    A=[row[:] for row in M]
    m=len(A); n=len(A[0]) if m else 0
    r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        for i in range(m):
            if i!=r and A[i][c]:
                A[i]=[a^b for a,b in zip(A[i],A[r])]
        r+=1
    return r

def fixed_dim(A):
    B=[[A[i][j] ^ (1 if i==j else 0) for j in range(4)] for i in range(4)]
    return 4-rank2(B)

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: c[i+j]^=1
    return c

def det_poly_tI_minus_A(A):
    # Leibniz over F2; sign irrelevant. coefficients low-to-high in t.
    out=[0]
    for perm in permutations(range(4)):
        term=[1]
        for i,j in enumerate(perm):
            factor=[A[i][j]]
            if i==j:
                if len(factor)<2: factor += [1]
                else: factor[1]^=1
            term=poly_mul(term,factor)
        if len(out)<len(term): out += [0]*(len(term)-len(out))
        for k,v in enumerate(term): out[k]^=v
    while len(out)>1 and out[-1]==0: out.pop()
    return tuple(reversed(out)) # high-to-low

counts=Counter()
char_by_type=defaultdict(set)
for p in permutations(range(N)):
    A=mat_for_perm(p)
    fd=fixed_dim(A)
    if fd==0:
        tp=cycle_type(p)
        counts[tp]+=1
        char_by_type[tp].add(det_poly_tI_minus_A(A))

expected={(6,):120,(5,1):144,(3,3):40}
assert dict(counts)==expected, (counts, expected)
assert char_by_type[(5,1)]=={(1,1,1,1,1)}
assert char_by_type[(6,)]=={(1,0,1,0,1)}
assert char_by_type[(3,3)]=={(1,0,1,0,1)}
assert sum(counts.values())==304
print('VERIFY_OK allowed_types=(6),(5,1),(3,3) counts=120,144,40 total=304')
print('CHAR_OK (5,1)=t^4+t^3+t^2+t+1; (6),(3,3)=t^4+t^2+1')
