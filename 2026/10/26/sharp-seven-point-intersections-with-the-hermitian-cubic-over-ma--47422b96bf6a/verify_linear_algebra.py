#!/usr/bin/env python3
"""Independent exact linear-algebra classification of cubics through seven Hermitian points."""
from itertools import product,combinations

def plus(a,b):return a^b

def mult(a,b):
    # Polynomial multiplication modulo t^2+t+1 over F2.
    z=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1:z^=1<<(i+j)
    if z&4:z^=7
    return z

def power(a,n):
    out=1
    for _ in range(n):out=mult(out,a)
    return out

def inv(a):
    if not a:raise ZeroDivisionError()
    return power(a,2)

P=[(1,y,z) for y,z in product(range(4),repeat=2)]
P += [(0,1,z) for z in range(4)] + [(0,0,1)]
exps=[(3-i-j,i,j) for i in range(4) for j in range(4-i)]
# This exponent order is intentionally different from the exhaustive verifier.
def eval_monomials(x):
    return tuple(mult(mult(power(x[0],a),power(x[1],b)),power(x[2],c)) for a,b,c in exps)
EV=[eval_monomials(p) for p in P]
def f_eval(coeff,j):
    v=0
    for a,b in zip(coeff,EV[j]):v ^= mult(a,b)
    return v

def h(p):
    x,y,z=p
    return power(x,3)^mult(power(y,2),z)^mult(y,power(z,2))
H=[i for i,p in enumerate(P) if h(p)==0]
assert len(H)==9

def rref(rows):
    matrix=[list(row) for row in rows]
    pivots=[];rank=0
    for col in range(10):
        pivot=next((i for i in range(rank,len(matrix)) if matrix[i][col]),None)
        if pivot is None:continue
        matrix[rank],matrix[pivot]=matrix[pivot],matrix[rank]
        z=inv(matrix[rank][col])
        matrix[rank]=[mult(z,v) for v in matrix[rank]]
        for i in range(len(matrix)):
            if i!=rank and matrix[i][col]:
                v=matrix[i][col]
                matrix[i]=[a^mult(v,b) for a,b in zip(matrix[i],matrix[rank])]
        pivots.append(col)
        rank+=1
        if rank==len(matrix):break
    return matrix[:rank],pivots

def null_basis(rows):
    reduced,pivots=rref(rows)
    free=[i for i in range(10) if i not in pivots]
    ans=[]
    for f in free:
        v=[0]*10;v[f]=1
        for row,pivot in zip(reduced,pivots):v[pivot]=row[f]
        ans.append(tuple(v))
    return ans

def combine(basis,c):
    v=[0]*10
    for b,s in zip(basis,c):
        for i in range(10):v[i] ^= mult(s,b[i])
    return tuple(v)

def normalize(c):
    leading=next((a for a in c if a),None)
    return tuple(mult(inv(leading),a) for a in c) if leading is not None else None

lines=[]
for l in P:
    indexes=[]
    for j,p in enumerate(P):
        if not (mult(l[0],p[0])^mult(l[1],p[1])^mult(l[2],p[2])):indexes.append(j)
    assert len(indexes)==5
    lines.append(indexes)

assert len(null_basis([EV[i] for i in H]))==2
assert all(len(null_basis([EV[i] for i in subset]))==2 for subset in combinations(H,8))
# Every cubic zero on any eight rational Hermitian points is zero on the ninth.

def tangent_count(coeff):
    count=0
    for i in H:
        if f_eval(coeff,i):continue
        x,y,z=P[i]
        grad=[]
        for axis in range(3):
            derivative=0
            for a,(u,v,w) in zip(coeff,exps):
                ex=[u,v,w]
                if ex[axis]&1:
                    ex[axis]-=1
                    derivative ^= mult(a,mult(mult(power(x,ex[0]),power(y,ex[1])),power(z,ex[2])))
            grad.append(derivative)
        dh=(power(x,2),power(z,2),power(y,2))
        cross=(mult(grad[1],dh[2])^mult(grad[2],dh[1]),
               mult(grad[2],dh[0])^mult(grad[0],dh[2]),
               mult(grad[0],dh[1])^mult(grad[1],dh[0]))
        if cross==(0,0,0):count+=1
    return count

hist={7:0,8:0};contacts={(7,1):0,(8,2):0};pairs=0
for omitted in combinations(H,2):
    pts=[i for i in H if i not in omitted]
    basis=null_basis([EV[i] for i in pts])
    assert len(basis)==3
    forms={normalize(combine(basis,cs)) for cs in product(range(4),repeat=3)}
    forms.discard(None)
    exactly_seven=[c for c in forms if all(f_eval(c,i)==0 for i in pts)
                   and all(f_eval(c,i)!=0 for i in omitted)]
    assert len(exactly_seven)==16
    smooth=[]
    for c in exactly_seven:
        if any(all(f_eval(c,i)==0 for i in line) for line in lines):continue
        n=sum(f_eval(c,i)==0 for i in range(21))
        assert n in (7,8)
        smooth.append(n)
        hist[n]+=1
        tc=tangent_count(c)
        assert (n,tc) in contacts
        contacts[(n,tc)]+=1
    assert len(smooth)==5 and smooth.count(7)==2 and smooth.count(8)==3
    pairs+=1
assert pairs==36 and hist=={7:72,8:108}
print("MATRIX_RANK 8; PAIRS 36; EXACT_SEVEN_PER_PAIR 16")
print("NO_RATIONAL_LINE_FACTOR 5 PER_PAIR; RATIONAL_POINT_SPLIT 2/3")
assert contacts=={(7,1):72,(8,2):108}
print("COUNTS",hist,"CONTACTS",contacts)
print("VERIFY_LINEAR_ALGEBRA_OK")
