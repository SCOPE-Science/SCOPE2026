#!/usr/bin/env python3
from itertools import combinations, product
from collections import Counter
from math import gcd

F={tuple(sorted(x)) for x in [
(1,2,4,5),(1,2,4,8),(1,2,5,7),(1,2,7,8),(1,3,5,7),(1,3,5,11),(1,3,6,7),(1,3,6,10),(1,3,9,10),(1,3,9,11),(1,4,5,11),(1,4,8,11),(1,6,7,12),(1,6,10,12),(1,7,8,11),(1,7,9,11),(1,7,9,12),(1,9,10,12),(2,3,8,9),(2,3,8,12),(2,3,9,11),(2,3,11,12),(2,4,5,10),(2,4,6,8),(2,4,6,12),(2,4,10,12),(2,5,7,10),(2,6,8,9),(2,6,9,11),(2,6,11,12),(2,7,8,10),(2,8,10,12),(3,4,6,7),(3,4,6,10),(3,4,7,9),(3,4,9,10),(3,5,7,9),(3,5,8,9),(3,5,8,12),(3,5,11,12),(4,5,10,11),(4,6,7,12),(4,6,8,10),(4,7,9,12),(4,8,10,11),(4,9,10,12),(5,6,8,9),(5,6,8,12),(5,6,9,11),(5,6,11,12),(5,7,9,11),(5,7,10,11),(6,8,10,12),(7,8,10,11)]}
V=tuple(range(1,13))
def faces(k): return {tuple(sorted(c)) for f in F for c in combinations(f,k)}
E=sorted(faces(2)); T=sorted(faces(3))
assert (len(V),len(E),len(T),len(F))==(12,66,108,54)
assert set(E)==set(combinations(V,2))

# Exact full automorphism enumeration by backtracking. Once three/four source vertices
# are assigned, triangle/facet status must be preserved.
auts=[]
def rec(mapping,used):
    if len(mapping)==12:
        auts.append(tuple(mapping[i] for i in V)); return
    u=next(i for i in V if i not in mapping)
    mapped=list(mapping)
    for v in V:
        if v in used: continue
        ok=True
        for a,b in combinations(mapped,2):
            if (tuple(sorted((u,a,b))) in T)!=(tuple(sorted((v,mapping[a],mapping[b]))) in T):
                ok=False; break
        if not ok: continue
        for abc in combinations(mapped,3):
            if (tuple(sorted((u,)+abc)) in F)!=(tuple(sorted((v,)+tuple(mapping[x] for x in abc))) in F):
                ok=False; break
        if not ok: continue
        mapping[u]=v; used.add(v); rec(mapping,used); used.remove(v); del mapping[u]
rec({},set())
auts=sorted(set(auts))
assert len(auts)==24
assert {p[0] for p in auts}==set(V)  # vertex-transitive

# Integral H1 certificate. Collapse the star tree at vertex 1. The 55 cotree edges
# are coordinates for the integral graph-cycle lattice.
tree={tuple(sorted((1,v))) for v in V if v!=1}
cot=[e for e in E if e not in tree]; ci={e:i for i,e in enumerate(cot)}
assert len(cot)==55

def relcol(t):
    a,b,c=t; z=[0]*55
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        e=tuple(sorted(e))
        if e in ci: z[ci[e]] += s
    return z
Rcols=[relcol(t) for t in T]

# Two integral cocycles. Direct verification below shows they annihilate all facial boundaries.
w1=[-1,0,0,-1,0,0,-1,-1,-1,-1,1,0,0,0,1,0,0,0,0,0,-1,-1,0,-1,-1,0,-1,0,0,1,0,-1,0,0,0,1,0,0,0,0,0,0,-1,0,0,-1,-1,0,-1,0,0,0,1,0,0]
w2=[-1,0,0,0,0,0,-1,0,-1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,-1,0,-1,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,1]
assert len(w1)==len(w2)==55
assert all(sum(w1[i]*c[i] for i in range(55))==0 for c in Rcols)
assert all(sum(w2[i]*c[i] for i in range(55))==0 for c in Rcols)

# A unimodular rank-53 boundary minor proves the quotient is torsion-free of rank 2;
# the two cocycles prove rank <=53, while the minor proves rank >=53.
rows=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53]
cols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,34,35,37,38,39,40,41,43,44,45,46,48,49,50,51,52,55,56,58,79,81]
M=[[Rcols[j][i] for j in cols] for i in rows]
def det_bareiss(A):
    A=[r[:] for r in A]; n=len(A); sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            s=next(i for i in range(k+1,n) if A[i][k])
            A[k],A[s]=A[s],A[k]; sign=-sign
        p=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*p-A[i][k]*A[k][j])//prev
        prev=p
        for i in range(k+1,n): A[i][k]=0
    return sign*A[-1][-1]
assert det_bareiss(M)==1

# Cotree cycles for edges 23 and 26 map under (w1,w2) by a unimodular matrix,
# so they form a basis of H1 ~= Z^2.
basis_edges=[(2,3),(2,6)]
bi=[ci[e] for e in basis_edges]
Q=((w1[bi[0]],w1[bi[1]]),(w2[bi[0]],w2[bi[1]]))
assert Q==((-1,-1),(-1,0))
qdet=Q[0][0]*Q[1][1]-Q[0][1]*Q[1][0]
assert qdet==-1

def eval_path(w,path):
    s=0
    for u,v in zip(path,path[1:]):
        e=tuple(sorted((u,v)))
        c=0 if e in tree else w[ci[e]]
        s += c if u<v else -c
    return s

def qinv_apply(y):
    a,b=Q[0]; c,d=Q[1]; det=a*d-b*c
    n0=d*y[0]-b*y[1]; n1=-c*y[0]+a*y[1]
    assert n0%det==0 and n1%det==0
    return (n0//det,n1//det)

actions=Counter()
for p in auts:
    colsA=[]
    for e in basis_edges:
        a,b=e; path=[a,b,1,a]
        ip=[p[x-1] for x in path]
        y=(eval_path(w1,ip),eval_path(w2,ip))
        colsA.append(qinv_apply(y))
    A=(colsA[0][0],colsA[1][0],colsA[0][1],colsA[1][1])
    actions[A]+=1
assert len(actions)==12 and set(actions.values())=={2}

# Each action preserves q(x,y)=x^2+xy+y^2.
def q(x,y): return x*x+x*y+y*y
def det2(A): return A[0]*A[3]-A[1]*A[2]
def preserves(A):
    a,b,c,d=A
    # Coefficients of q(M(x,y)) must equal those of x^2+xy+y^2.
    return (a*a+a*c+c*c==1 and
            2*a*b+a*d+b*c+2*c*d==1 and
            b*b+b*d+d*d==1)
assert all(abs(det2(A))==1 and preserves(A) for A in actions)

# Exhaust the full integral isometry group: a column of a q-isometry has q=1,
# which forces its coordinates to lie in {-1,0,1}.
isom=set()
for A in product((-1,0,1),repeat=4):
    if abs(det2(A))==1 and preserves(A): isom.add(A)
assert len(isom)==12 and isom==set(actions)

# Mod 2 image is all GL(2,2), so kernels have orders 2 and 4 respectively.
def mod2(A): return tuple(x&1 for x in A)
modacts={mod2(A) for A in actions}
gl22={A for A in product((0,1),repeat=4) if (A[0]*A[3]-A[1]*A[2])%2==1}
assert modacts==gl22 and len(gl22)==6
assert actions[(1,0,0,1)]==2
mod_kernel=sum(n for A,n in actions.items() if mod2(A)==(1,0,0,1))
assert mod_kernel==4

print('VERIFY_OK f=12,66,108,54 aut=24 H1_Z=Z^2 boundary_minor_det=1 '
      'H1_image=O(x^2+xy+y^2,Z):12 action_multiplicity=2 kernel_Z=2 '
      'mod2_image=GL(2,2):6 kernel_F2=4')
