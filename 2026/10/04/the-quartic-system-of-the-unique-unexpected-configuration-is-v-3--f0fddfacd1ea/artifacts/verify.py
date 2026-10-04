#!/usr/bin/env python3
from itertools import permutations, product, combinations
from fractions import Fraction
from math import gcd
from functools import reduce

PTS=[(-1,0,1),(0,-1,1),(1,0,1),(0,1,1),(0,0,1),(1,-1,0),(1,1,0),(0,1,0),(1,0,0)]
MONS=[(i,j,4-i-j) for i in range(5) for j in range(5-i)]
# basis of I(Z)_4 as sparse coefficient dictionaries
BASIS=[
 {(0,3,1):1,(0,1,3):-1},                 # yz(y^2-z^2)
 {(3,0,1):1,(1,0,3):-1},                 # xz(x^2-z^2)
 {(3,1,0):1,(1,3,0):-1},                 # xy(x^2-y^2)
 {(1,1,2):1},                            # xyz^2
 {(1,2,1):1},                            # xy^2z
 {(2,1,1):1},                            # x^2yz
]

def igcd(vals):
    vals=[abs(v) for v in vals if v]
    return reduce(gcd,vals) if vals else 1

def normproj(v):
    v=list(v); g=igcd(v); v=[a//g for a in v]
    for a in v:
        if a:
            if a<0: v=[-b for b in v]
            break
    return tuple(v)

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def dot(a,b): return sum(x*y for x,y in zip(a,b))

def rank(A):
    A=[[Fraction(x) for x in row] for row in A]
    m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        q=A[r][c]; A[r]=[x/q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]; A[i]=[u-q*v for u,v in zip(A[i],A[r])]
        r+=1
        if r==m: break
    return r

def eval_mon(p,e): return p[0]**e[0]*p[1]**e[1]*p[2]**e[2]

def coeffvec(poly): return [poly.get(e,0) for e in MONS]

def matmul(M,v): return tuple(sum(M[i][j]*v[j] for j in range(3)) for i in range(3))

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def transpose(M): return tuple(tuple(M[j][i] for j in range(3)) for i in range(3))

def negM(M): return tuple(tuple(-a for a in row) for row in M)

def signed_perm_matrices():
    out=[]
    for perm in permutations(range(3)):
        for signs in product((-1,1), repeat=3):
            M=[[0]*3 for _ in range(3)]
            for i,j in enumerate(perm): M[i][j]=signs[i]
            out.append(tuple(tuple(r) for r in M))
    return out

def transform_poly(poly,M):
    # pullback by M^{-1}; for signed permutation M, inverse is transpose.
    N=transpose(M)
    rows=[]
    for i in range(3):
        j=next(j for j,a in enumerate(N[i]) if a)
        rows.append((j,N[i][j]))
    out={}
    for e,c in poly.items():
        ne=[0,0,0]; cc=c
        for i,pow_ in enumerate(e):
            j,s=rows[i]; ne[j]+=pow_; cc*=s**pow_
        ne=tuple(ne); out[ne]=out.get(ne,0)+cc
    return {e:c for e,c in out.items() if c}

def basis_image(poly):
    for j,b in enumerate(BASIS):
        if poly==b: return j,1
        nb={e:-c for e,c in b.items()}
        if poly==nb: return j,-1
    raise AssertionError(('not in signed basis orbit',poly))

def cycle_type(p):
    seen=set(); cyc=[]
    for i in range(len(p)):
        if i in seen: continue
        j=i;n=0
        while j not in seen:
            seen.add(j);n+=1;j=p[j]
        cyc.append(n)
    return tuple(sorted(cyc,reverse=True))

# 1. quartic interpolation space
E=[[eval_mon(p,e) for e in MONS] for p in PTS]
assert rank(E)==9
assert all(all(sum(c*eval_mon(p,e) for e,c in b.items())==0 for p in PTS) for b in BASIS)
assert rank([coeffvec(b) for b in BASIS])==6

# 2. incidence fingerprint: exactly four 3-rich and three 4-rich lines
lines={}
for i,j in combinations(range(9),2):
    L=normproj(cross(PTS[i],PTS[j]))
    S=frozenset(k for k,p in enumerate(PTS) if dot(L,p)==0)
    lines[S]=L
rich=sorted((S,L) for S,L in lines.items() if len(S)>=3)
triple=[S for S,L in rich if len(S)==3]
quad=[S for S,L in rich if len(S)==4]
assert len(triple)==4 and len(quad)==3
# pairwise intersections of the four triple lines are six distinct configuration points
pairs=[]
for a,b in combinations(range(4),2):
    inter=triple[a]&triple[b]
    assert len(inter)==1
    pairs.append(next(iter(inter)))
assert len(set(pairs))==6

# 3. B3 signed-permutation group gives 24 projective symmetries and character data
Pnorm=[normproj(p) for p in PTS]; pindex={p:i for i,p in enumerate(Pnorm)}
proj={}
for M in signed_perm_matrices():
    pp=tuple(pindex[normproj(matmul(M,p))] for p in PTS)
    tp=[]
    for S in triple:
        image=frozenset(pp[i] for i in S)
        tp.append(triple.index(image))
    tp=tuple(tp)
    # trace on the six basis forms
    tr=0
    for i,b in enumerate(BASIS):
        j,s=basis_image(transform_poly(b,M))
        if i==j: tr+=s
    if tp in proj:
        assert proj[tp]==tr  # ±M act identically in degree 4
    else:
        proj[tp]=tr
assert len(proj)==24
cts={}
for p,tr in proj.items():
    ct=cycle_type(p)
    cts.setdefault(ct,[]).append(tr)
expected_counts={(1,1,1,1):1,(2,1,1):6,(2,2):3,(3,1):8,(4,):6}
assert {k:len(v) for k,v in cts.items()}==expected_counts
assert {k:set(v) for k,v in cts.items()}=={
    (1,1,1,1):{6},(2,1,1):{0},(2,2):{-2},(3,1):{0},(4,):{0}}
# S4 character decomposition: standard + standard⊗sign
classes=[(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]
sizes=[1,6,3,8,6]
chi=[6,0,-2,0,0]
irreps={
 'trivial':[1,1,1,1,1],
 'sign':[1,-1,1,1,-1],
 'two_dimensional':[2,0,2,-1,0],
 'standard':[3,1,-1,0,-1],
 'standard_sign_twist':[3,-1,-1,0,1],
}
mult={name:sum(sz*a*b for sz,a,b in zip(sizes,chi,ch))//24 for name,ch in irreps.items()}
assert mult=={'trivial':0,'sign':0,'two_dimensional':0,'standard':1,'standard_sign_twist':1}
# The first and second displayed three-dimensional spans are individually invariant.
split_chars=[]
for inds in (range(3), range(3,6)):
    by_type={}
    for M in signed_perm_matrices():
        pp=tuple(pindex[normproj(matmul(M,p))] for p in PTS)
        tp=[]
        for S in triple:
            image=frozenset(pp[i] for i in S)
            tp.append(triple.index(image))
        tp=tuple(tp)
        tr=0
        for i in inds:
            j,sg=basis_image(transform_poly(BASIS[i],M))
            if i==j: tr+=sg
        by_type.setdefault(cycle_type(tp),set()).add(tr)
    split_chars.append([next(iter(by_type[t])) for t in classes])
assert split_chars==[[3,-1,-1,0,1],[3,1,-1,0,-1]]
print('VERIFY_OK')
print('rank_eval=9 dim_I4=6 rich_lines=4x3+3x4 projective_group=24')
print('character=[6,0,-2,0,0] decomposition=standard+standard_sign_twist invariants=0')
