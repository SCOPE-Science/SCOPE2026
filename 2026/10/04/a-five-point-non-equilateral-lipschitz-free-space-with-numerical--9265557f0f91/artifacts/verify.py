#!/usr/bin/env python3
import json, sys
from fractions import Fraction
from itertools import product
from pathlib import Path

HERE=Path(__file__).resolve().parent
C=json.loads((HERE/"certificate.json").read_text(encoding="utf-8"))

edges=[tuple(e) for e in C["graph"]["edges"]]
d=4
def edgevec(a,b):
    v=[0]*d
    if a: v[a-1]+=1
    if b: v[b-1]-=1
    return v
def dot(a,b): return sum(Fraction(x)*Fraction(y) for x,y in zip(a,b))
def rank(rows):
    A=[[Fraction(x) for x in r] for r in rows if any(x for x in r)]
    if not A: return 0
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r
def kron(f,v): return [int(fi)*int(vj) for fi in f for vj in v]
def mat_eval(f,T,v):
    return sum(Fraction(f[i])*T[i][j]*Fraction(v[j]) for i in range(d) for j in range(d))

# Primal extremes: oriented graph-edge molecules.
E=[]
for a,b in edges:
    v=edgevec(a,b)
    E.extend([v,[-x for x in v]])
assert E==C["extreme_primal"]

# Dual extremes. Hub edges force coordinates into [-1,1].
# Incidence constraints have integral vertices; enumerate integral candidates
# and retain exactly those with rank-4 active edge constraints.
D=[]
for vals in product([-1,0,1], repeat=d):
    acts=[]; ok=True
    for a,b in edges:
        g=edgevec(a,b)
        z=sum(g[i]*vals[i] for i in range(d))
        if abs(z)>1: ok=False; break
        if abs(z)==1:
            acts.append([int((1 if z>0 else -1)*x) for x in g])
    if ok and rank(acts)==d:
        D.append(list(vals))
assert D==C["extreme_dual"]

N=[]
for vi,v in enumerate(E):
    for fi,f in enumerate(D):
        if dot(f,v)==1:
            N.append([vi,fi])
assert N==C["norming_pairs"]

# Numerical-radius inequalities A t <= 1, including both signs.
A=[]
for vi,fi in N:
    a=kron(D[fi],E[vi])
    A.append(a)
    A.append([-x for x in a])

# Verify every exact LP-dual certificate. These imply every operator with
# numerical radius <=1 has every extreme norm evaluation <=2.
seen=set()
for rec in C["upper_bound_duals"]:
    vi,fi=rec["objective"]
    key=(vi,fi); assert key not in seen; seen.add(key)
    c=kron(D[fi],E[vi])
    y={int(k):Fraction(z) for k,z in rec["weights"]}
    assert all(z>=0 for z in y.values())
    assert sum(y.values(),Fraction(0))==Fraction(rec["sum"])
    assert sum(y.values(),Fraction(0))<=2
    for j in range(d*d):
        assert sum(y.get(k,Fraction(0))*A[k][j] for k in range(len(A)))==c[j]
assert len(seen)==len(E)*len(D)

# Exact equality witness.
T=[[Fraction(z) for z in row] for row in C["witness_operator_rows"]]
num=max(abs(mat_eval(D[fi],T,E[vi])) for vi,fi in N)
op=max(abs(mat_eval(f,T,v)) for f in D for v in E)
assert num==1
assert op==2
print("VERIFY_OK")
