#!/usr/bin/env python3
"""Exact symbolic checks for a diagonal Klein-four invariant biquadric."""
from fractions import Fraction

# Sparse polynomials on a,b,c,u0,u1,v0,v1 with integral coefficients.
N = 7

def mono(i):
    e = [0] * N
    e[i] = 1
    return {tuple(e): 1}

def add(*args):
    out = {}
    for d in args:
        for e, c in d.items():
            out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c}

def mul(a, b):
    out = {}
    for e, c in a.items():
        for f, d in b.items():
            k = tuple(x+y for x, y in zip(e, f))
            out[k] = out.get(k, 0) + c*d
    return {k: v for k, v in out.items() if v}

def neg(a):
    return {k:-v for k,v in a.items()}

def sub(a,b):
    return add(a,neg(b))

def power(a,n):
    ans = {tuple([0]*N): 1}
    for _ in range(n):
        ans=mul(ans,a)
    return ans

def transform(p, indexes, signs):
    out = {}
    for e,c in p.items():
        t=[0]*N
        sign=c
        for i,k in enumerate(e):
            t[indexes[i]] += k
            sign *= signs[i]**k
        k=tuple(t)
        out[k]=out.get(k,0)+sign
    return {k:v for k,v in out.items() if v}

a,b,c,u0,u1,v0,v1 = [mono(i) for i in range(N)]
Q0u=add(power(u0,2),power(u1,2))
Q0v=add(power(v0,2),power(v1,2))
Q1u=sub(power(u0,2),power(u1,2))
Q1v=sub(power(v0,2),power(v1,2))
Q2u=add(mul(u0,u1),mul(u0,u1))
Q2v=add(mul(v0,v1),mul(v0,v1))
F=add(mul(a,mul(Q0u,Q0v)),mul(b,mul(Q1u,Q1v)),mul(c,mul(Q2u,Q2v)))
assert transform(F, list(range(N)), [1,1,1,1,-1,1,-1]) == F
assert transform(F, [0,1,2,4,3,6,5], [1]*N) == F

# The projective matrices R and S anticommute on each factor.
R=((1,0),(0,-1))
S=((0,1),(1,0))
def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def kron(A,B):
    return tuple(tuple(A[i//len(B)][j//len(B[0])]*B[i%len(B)][j%len(B[0])] for j in range(len(A[0])*len(B[0]))) for i in range(len(A)*len(B)))
assert mm(R,S) == tuple(tuple(-z for z in row) for row in mm(S,R))
RR,SS = kron(R,R),kron(S,S)
assert mm(RR,SS)==mm(SS,RR)
I4=tuple(tuple(int(i==j) for j in range(4)) for i in range(4))
assert mm(RR,RR)==mm(SS,SS)==I4

# Verify symbolic discriminant identity for projection to the u-factor.
A=add(mul(add(a,b), power(u0,2)),mul(sub(a,b),power(u1,2)))
B=mul(mul(c,u0),u1)
B=add(B,B,B,B)
C=add(mul(sub(a,b),power(u0,2)),mul(add(a,b),power(u1,2)))
D=sub(power(B,2),mul({tuple([0]*N):4},mul(A,C)))
k=sub(power(b,2),power(a,2))
l=sub(mul({tuple([0]*N):4},power(c,2)),add(power(a,2),power(a,2),power(b,2),power(b,2)))
pred=mul({tuple([0]*N):4},add(mul(k,add(power(u0,4),power(u1,4))),mul(l,mul(power(u0,2),power(u1,2)))))
assert D == pred

# Exact witness (a,b,c)=(1,2,3) gives quartic 3 u^4 + 26 u^2 + 3.
assert 2**2-1**2==3
assert 4*3**2-2*1**2-2*2**2 == 26
assert 26**2 - 4*3**2 == 640
# For u=0 and infinity, the quadratic coefficient pairs are nonzero.
assert (1-2,1+2) != (0,0)
assert (1+2,1-2) != (0,0)
print('VERIFY_OK: invariant forms, tensor lift, anticommutation, symbolic discriminant, smooth witness')
