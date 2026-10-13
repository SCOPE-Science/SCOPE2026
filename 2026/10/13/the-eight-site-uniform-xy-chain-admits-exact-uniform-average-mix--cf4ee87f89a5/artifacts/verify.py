#!/usr/bin/env python3
from fractions import Fraction

W = {
0:[[1,1,14,1],[1,11,1,1],[1,1,4,1],[1,23,1,1]],
1:[[1,1,1,3],[1,1,13,1],[13,1,1,1],[1,1,5,13]],
2:[[17,1,14,1],[1,17,1,1],[1,1,4,1],[1,1,1,1]],
3:[[1,1,1,1],[1,1,1,1],[1,19,1,17],[21,1,1,1]],
}

# Phase coordinates in units of pi/2 on the q=9 Kronecker torus:
# phi_2=a, phi_3=b, phi_4=c, phi_1=a+c and phi_{9-r}=-phi_r (mod 4).
def phase_units(a,b,c):
    return {
        1:(a+c)%4, 2:a%4, 3:b%4, 4:c%4,
        5:(-c)%4, 6:(-b)%4, 7:(-a)%4, 8:(-a-c)%4,
    }

def cos_quarter_turn(k):
    k%=4
    return (1,0,-1,0)[k]

points=[]
weights=[]
for a in range(4):
    for b in range(4):
        for c in range(4):
            weights.append(W[a][b][c])
            ph=phase_units(a,b,c)
            points.append([cos_quarter_turn(ph[r]-ph[s])
                           for r in range(1,9) for s in range(r+1,9)])

assert all(w>0 for w in weights)
assert sum(weights)==256

pairs=[(r,s) for r in range(1,9) for s in range(r+1,9)]
for j,(r,s) in enumerate(pairs):
    numer=sum(weights[i]*points[i][j] for i in range(64))
    target=-32 if (s-r)%2==0 else 0
    assert numer==target, (r,s,numer,target)

# Exact affine rank of the 64 phase-grid coherence vectors.
M=[[Fraction(points[i][j]-points[0][j]) for j in range(28)]
   for i in range(1,64)]
def rank(A):
    A=[row[:] for row in A]
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None:
            continue
        A[r],A[piv]=A[piv],A[r]
        p=A[r][c]
        A[r]=[x/p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]
                A[i]=[A[i][j]-q*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r
assert rank(M)==16

# The 28 pair characters on T^3 reduce to exactly 16 nonzero cosine characters.
v={1:(1,0,1),2:(1,0,0),3:(0,1,0),4:(0,0,1),
   5:(0,0,-1),6:(0,-1,0),7:(-1,0,0),8:(-1,0,-1)}
def canon(x):
    nx=tuple(-z for z in x)
    return min(tuple(x),nx)
chars=set()
for r,s in pairs:
    d=tuple(v[r][k]-v[s][k] for k in range(3))
    assert d!=(0,0,0)
    chars.add(canon(d))
assert len(chars)==16

print("VERIFY_OK")
