#!/usr/bin/env python3
from itertools import combinations, permutations, product
from collections import defaultdict, Counter
P=5

def inv(a): return pow(a%P,-1,P)

def rref(rows,n=None):
    A=[[x%P for x in row] for row in rows if any(x%P for x in row)]
    if n is None:
        n=len(A[0]) if A else 0
    m=len(A); rr=0; piv=[]
    for c in range(n):
        k=next((i for i in range(rr,m) if A[i][c]%P),None)
        if k is None: continue
        A[rr],A[k]=A[k],A[rr]
        z=inv(A[rr][c]); A[rr]=[(z*x)%P for x in A[rr]]
        for i in range(m):
            if i!=rr and A[i][c]%P:
                z=A[i][c]%P
                A[i]=[(A[i][j]-z*A[rr][j])%P for j in range(n)]
        piv.append(c); rr+=1
        if rr==m: break
    return tuple(tuple(row) for row in A[:rr]), tuple(piv)

def canon_span(rows,n):
    R,_=rref(rows,n)
    return R

def nullspace(rows,n):
    R,piv=rref(rows,n)
    free=[j for j in range(n) if j not in piv]
    B=[]
    for f in free:
        v=[0]*n; v[f]=1
        for i,c in enumerate(piv): v[c]=(-R[i][f])%P
        B.append(v)
    return canon_span(B,n)

def add(a,b): return tuple((x+y)%P for x,y in zip(a,b))
def scale(c,a): return tuple(c*x%P for x in a)

def full5(v4):
    return tuple(v4)+((-sum(v4))%P,)

def cubic(v4):
    return sum(x**3 for x in full5(v4))%P

def all_two_planes():
    nonzero=[v for v in product(range(P), repeat=4) if any(v)]
    S=set()
    for i,u in enumerate(nonzero):
        for v in nonzero[i+1:]:
            R=canon_span([u,v],4)
            if len(R)==2: S.add(R)
    return S

def is_line_on_X(B):
    u,v=B
    # Exact identity check on F_5[s,t]; degrees in s,t are <=3<5, so values on F_5^2 determine it.
    return all(cubic(add(scale(s,u),scale(t,v)))==0 for s in range(P) for t in range(P))

def contains(B,v):
    return len(canon_span(list(B)+[v],4))==len(B)

def permute_v4(v4,perm):
    w=full5(v4)
    wp=tuple(w[perm[j]] for j in range(5))
    # H=sum x_i=0 is permutation invariant; first four coordinates determine the fifth.
    return wp[:4]

def act_line(B,perm):
    return canon_span([permute_v4(row,perm) for row in B],4)

def line_from_equations(eq5):
    B5=nullspace(eq5,5)
    assert len(B5)==2
    return canon_span([row[:4] for row in B5],4)

planes=all_two_planes()
assert len(planes)==806, len(planes)
lines={B for B in planes if is_line_on_X(B)}
assert len(lines)==21, len(lines)
p=(1,1,1,1)
through={B for B in lines if contains(B,p)}
away=lines-through
assert (len(through),len(away))==(6,15)

# Fifteen diagonal lines: x_i=0 and opposite pair sums zero.
diag=set()
indices=set(range(5))
for i in range(5):
    rem=sorted(indices-{i})
    a=rem[0]
    # three pairings of the four remaining indices
    pairings=[((rem[0],rem[1]),(rem[2],rem[3])),
              ((rem[0],rem[2]),(rem[1],rem[3])),
              ((rem[0],rem[3]),(rem[1],rem[2]))]
    for (j,k),(l,m) in pairings:
        eq=[]
        row=[0]*5; row[i]=1; eq.append(row)
        row=[0]*5; row[j]=1; row[k]=1; eq.append(row)
        row=[0]*5; row[l]=1; row[m]=1; eq.append(row)
        diag.add(line_from_equations(eq))
assert len(diag)==15
assert diag==away

# The twelve smooth Clebsch double-six formulas specialize at phi=(1+sqrt(5))/2=1/2=3 mod 5.
# They collapse pairwise to exactly the six lines through the node.
phi=3
golden=[]
for i,j in combinations(range(4),2):
    comp=[a for a in range(4) if a not in (i,j)]
    for k,l in (comp,comp[::-1]):
        eq=[]
        row=[0]*5; row[i]=1; row[j]=phi; row[k]=1; eq.append(row)
        row=[0]*5; row[i]=phi; row[j]=1; row[l]=1; eq.append(row)
        row=[0]*5; row[i]=(-phi)%P; row[j]=(-phi)%P; row[4]=1; eq.append(row)
        golden.append(line_from_equations(eq))
mult=Counter(golden)
assert len(golden)==12 and len(mult)==6
assert set(mult)==through and set(mult.values())=={2}

# Natural S5 permutation action: two line orbits of sizes 6 and 15.
S5=list(permutations(range(5)))
assert len(S5)==120
for B in lines:
    for g in S5:
        assert act_line(B,g) in lines

def orbit(B): return {act_line(B,g) for g in S5}
def stab(B): return [g for g in S5 if act_line(B,g)==B]
Bt=next(iter(through)); Ba=next(iter(away))
assert len(orbit(Bt))==6 and len(stab(Bt))==20
assert len(orbit(Ba))==15 and len(stab(Ba))==8
assert orbit(Bt)==through and orbit(Ba)==away

# Local A1 check at p. In x4=1, write x0=1+a, x1=1+b, x2=1+c,
# x3=1-(a+b+c) from the hyperplane equation. Quadratic part is
# 3*(a^2+b^2+c^2+(a+b+c)^2). Its symmetric matrix is 3*M below.
M=[[2,1,1],[1,2,1],[1,1,2]]
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))%P
assert det3(M)==4
assert (pow(3,3,P)*det3(M))%P != 0

# Algebraic singular-locus sign check: x_i^2 all equal. Up to common nonzero square root,
# signs eps_i are +/-1; in characteristic 5, sum eps_i=0 only if all signs agree,
# yielding the single projective point p.
sums=[]
for eps in product((1,-1), repeat=5):
    s=sum(eps)%P
    if s==0: sums.append(eps)
assert len(sums)==2 and sums[0]==tuple(-e for e in sums[1])

print('VERIFY_OK planes=806 lines=21 line_orbits=6+15 through_node=6 away=15 golden12_to_6_pairwise stabilizers=20,8 unique_A1_node=true all_lines_F5=true')
