#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations

# Exact rational arithmetic only; basis is (T,X,Z).
def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):
    return [list(r) for r in zip(*A)]

def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))

def inv3(A):
    d=det3(A)
    assert d
    C=[[F(0) for _ in range(3)] for __ in range(3)]
    for i in range(3):
        for j in range(3):
            rows=[r for r in range(3) if r!=i]
            cols=[c for c in range(3) if c!=j]
            minor=A[rows[0]][cols[0]]*A[rows[1]][cols[1]]-A[rows[0]][cols[1]]*A[rows[1]][cols[0]]
            C[i][j]=((-1)**(i+j))*minor
    return [[C[j][i]/d for j in range(3)] for i in range(3)]

def colmat(cols):
    return [[cols[j][i] for j in range(len(cols))] for i in range(len(cols[0]))]

def mvec(A,v):
    return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]

def diag(v):
    return [[v[i] if i==j else F(0) for j in range(len(v))] for i in range(len(v))]

def qpull(A,M):
    return matmul(transpose(M),matmul(A,M))

def proportional(A,B):
    ratio=None
    for i in range(len(A)):
        for j in range(len(A[0])):
            a,b=A[i][j],B[i][j]
            if b:
                r=a/b
                if ratio is None: ratio=r
                elif r!=ratio: return None
            elif a:
                return None
    return ratio

def projectivity(src_pts, dst_pts):
    B=colmat(src_pts[:3]); C=colmat(dst_pts[:3])
    Bi=inv3(B); Ci=inv3(C)
    c=mvec(Bi,src_pts[3]); d=mvec(Ci,dst_pts[3])
    assert all(c) and all(d)
    lam=[d[i]/c[i] for i in range(3)]
    return matmul(C,matmul(diag(lam),Bi))

def p(u): return [F(u),F(u*u),F(1)]

# Symmetric matrices for the source conics.
Q1=[[F(-1),F(0),F(0)],[F(0),F(0),F(1,2)],[F(0),F(1,2),F(0)]]
Q2=[[F(0),F(-5),F(0)],[F(-5),F(1),F(25,2)],[F(0),F(25,2),F(-36)]]
Q3=[[F(-5),F(0),F(4)],[F(0),F(0),F(2)],[F(4),F(2),F(-12)]]

S=(-1,2,3,6)
# Q2 restricted to C1: u^4-10u^3+25u^2-36=(u+1)(u-2)(u-3)(u-6).
def poly_mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out
prod=[F(1)]
for r in S: prod=poly_mul(prod,[F(-r),F(1)])
assert prod==[F(-36),F(0),F(25),F(-10),F(1)]
pts=[p(u) for u in S]

fixed=[]; swapped=[]
for perm in permutations(range(4)):
    dst=[pts[i] for i in perm]
    M=projectivity(pts,dst)
    a11=proportional(qpull(Q1,M),Q1)
    a22=proportional(qpull(Q2,M),Q2)
    a12=proportional(qpull(Q1,M),Q2)
    a21=proportional(qpull(Q2,M),Q1)
    if a11 is not None and a22 is not None: fixed.append((perm,M))
    if a12 is not None and a21 is not None: swapped.append((perm,M))

assert len(fixed)==4, len(fixed)
assert len(swapped)==0, len(swapped)
# Identity plus three involutions: the pair stabilizer is V4.
def matrix_proportional(A,B): return proportional(A,B) is not None
I=[[F(1),F(0),F(0)],[F(0),F(1),F(0)],[F(0),F(0),F(1)]]
nonid=0
for perm,M in fixed:
    if matrix_proportional(M,I):
        continue
    nonid+=1
    assert matrix_proportional(matmul(M,M),I)
assert nonid==3
# Only identity also preserves C3.
triple=[]
for perm,M in fixed:
    if proportional(qpull(Q3,M),Q3) is not None:
        triple.append((perm,M))
assert len(triple)==1
assert matrix_proportional(triple[0][1],I)

# The four lines are distinct.
lines=[(F(-160),F(25),F(256)),(F(0),F(1),F(0)),(F(-10),F(1),F(25)),(F(-90),F(25),F(81))]
def norm_line(v):
    for x in v:
        if x:
            return tuple(y/x for y in v)
assert len({norm_line(v) for v in lines})==4

print('intersection_parameters=',S)
print('pair_stabilizer_order=',len(fixed))
print('pair_swap_coset_size=',len(swapped))
print('triple_stabilizer_order=',len(triple))
print('line_count=',len(lines))
print('VERIFY_OK')
