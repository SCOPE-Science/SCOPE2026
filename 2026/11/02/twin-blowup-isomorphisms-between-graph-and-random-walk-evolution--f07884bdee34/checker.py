"""Finite exact checks for graph twin-blowup evolution algebra theorem.
This checks finite instances and displayed witnesses; the universal proof is in RESULT.md.
"""
from itertools import combinations, product
from fractions import Fraction
from math import isqrt
import sympy as sp

def connected(adj):
    n=len(adj); reached={0}
    while True:
        nxt=reached|{j for i in reached for j in range(n) if adj[i][j]}
        if nxt==reached: return len(reached)==n
        reached=nxt

def bipartition(adj):
    n=len(adj); side=[-1]*n; side[0]=0; todo=[0]
    for i in todo:
        for j in range(n):
            if adj[i][j]:
                if side[j]==-1: side[j]=1-side[i];todo.append(j)
                elif side[j]==side[i]: return None
    return side

def classify(adj,ns):
    n=len(adj); deg=[sum(adj[i][j]*ns[j] for j in range(n)) for i in range(n)]
    sides=bipartition(adj)
    if sides is None: return len(set(deg))==1,deg,sides
    return all(len({deg[i] for i in range(n) if sides[i]==k})==1 for k in (0,1)),deg,sides

def build(adj,ns):
    classes=[[] for _ in ns]; current=0
    for i,ni in enumerate(ns): classes[i]=list(range(current,current+ni));current+=ni
    d=[sum(adj[i][j]*ns[j] for j in range(len(ns))) for i in range(len(ns))]
    rows=[]
    for i,cls in enumerate(classes):
        z=[sum(j in classes[k] for k in range(len(ns)) if adj[i][k]) for j in range(current)]
        rows.extend([z]*len(cls))
    return rows,classes,d

def verify_witness(adj,ns,k):
    # target normalized squares; source unweighted squares.
    rows,cls,deg=build(adj,ns); N=len(rows)
    for v in range(N):
        left=[k[u]*rows[v][u] for u in range(N)]
        right=[k[v]*k[v]*Fraction(rows[v][u],deg[next(i for i,c in enumerate(cls) if v in c)]) for u in range(N)]
        assert left==right,(adj,ns,v,left,right)
    return True

def qcube(n):
    if n<=0:return None
    x=round(n**(1/3))
    for v in range(max(1,x-2),x+4):
        if v**3==n:return v
    return None

cases=0; positive=0; negative=0; rational_checks=0; singular=0
for r in range(2,5):
    edges=list(combinations(range(r),2))
    for mask in range(1<<len(edges)):
        a=[[0]*r for _ in range(r)]
        for index,(i,j) in enumerate(edges):
            if mask>>index&1:a[i][j]=a[j][i]=1
        if not connected(a) or sp.det(sp.Matrix(a))==0:continue
        for ns in product([1,2],repeat=r):
            cases+=1
            ok,deg,side=classify(a,ns)
            positive+=ok;negative+=not ok
            if max(ns)>1: singular+=1
            if not ok: continue
            if side is None:
                k=[Fraction(deg[0])]*sum(ns)
            else:
                D0=deg[side.index(0)];D1=deg[side.index(1)]
                v=qcube(D0**2*D1)
                if v is None:continue
                y=Fraction(v)
                x=y*y/Fraction(D0)
                kk=[y if s==0 else x for s in side]
                k=[z for z,sz in zip(kk,ns) for _ in range(sz)]
            verify_witness(a,ns,k)
            rational_checks+=1

# Independent determinant-pencil test for K_{2,1,3}; source forms have repeated blocks.
a=[[0,1,1],[1,0,1],[1,1,0]]; ns=[2,1,3]
rows,cls,deg=build(a,ns)
lambdas=sp.symbols('l0:6');
coeff=[sum(lambdas[j]*rows[v][j] for j in range(6)) for v in range(6)]
M=sp.diag(*coeff)
expected=sp.prod(sum(lambdas[j]*rows[cls[i][0]][j] for j in range(6))**ns[i] for i in range(3))
assert sp.expand(M.det()-expected)==0
assert sp.det(sp.Matrix(rows))==0
# K_2 with multiplicities (2,3) has real isomorphism but no rational diagonal witness.
assert qcube(3**2*2) is None
# K_2 with multiplicities (1,8) does have a rational witness.
verify_witness([[0,1],[1,0]],[1,8],[Fraction(4)]+[Fraction(2)]*8)
print('VERIFY_OK', {'base_blowups':cases,'criterion_yes':positive,'criterion_no':negative,'singular_cases':singular,'exact_witnesses':rational_checks,'pencil_test':'pass','rational_cube_boundary':'pass'})
