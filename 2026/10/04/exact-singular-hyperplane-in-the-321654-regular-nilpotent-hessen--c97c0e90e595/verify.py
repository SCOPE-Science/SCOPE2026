#!/usr/bin/env python3
"""Exact symbolic verification for the h=(3,4,5,6,6,6), w=321654 Hessenberg-Schubert cell claim.
Requires Python 3 and sympy. Uses exact integer/rational polynomial arithmetic only.
"""
from itertools import combinations
import sympy as sp

n=6
# U lower unitriangular, g=P_w U with w=321654.
u={}
U=sp.eye(n)
for k in range(2,n+1):
    for j in range(1,k):
        u[k,j]=sp.symbols(f"u{k}{j}")
        U[k-1,j-1]=u[k,j]
w=[3,2,1,6,5,4]
P=sp.zeros(n)
for j,wi in enumerate(w, start=1):
    P[wi-1,j-1]=1
G=P*U
N=sp.zeros(n)
for i in range(n-1):
    N[i,i+1]=1
A=sp.simplify(G.inv()*N*G)
h=[3,4,5,6,6,6]
positions=[]; equations=[]
for j in range(1,n+1):
    for i in range(h[j-1]+1,n+1):
        positions.append((i,j))
        equations.append(sp.factor(A[i-1,j-1]))
assert positions==[(4,1),(5,1),(6,1),(5,2),(6,2),(6,3)]
assert len(equations)==6

allvars=[u[k,j] for k in range(2,n+1) for j in range(1,k)]
J=sp.Matrix(equations).jacobian(allvars)
# On the source Schubert cell, only these six u-coordinates survive:
# u21=z23, u31=z13, u32=z12, u54=z56, u64=z46, u65=z45.
free=[u[2,1],u[3,1],u[3,2],u[5,4],u[6,4],u[6,5]]
sub={v:0 for v in allvars if v not in free}
Jc=sp.simplify(J.subs(sub))
assert all(sp.expand(f.subs(sub))==0 for f in equations), "cell is not contained in the patch equations"

# Rename only for the final factor comparison.
z12,z45,z13,z46,z23,z56=sp.symbols("z12 z45 z13 z46 z23 z56")
rename={u[3,2]:z12,u[6,5]:z45,u[3,1]:z13,u[6,4]:z46,u[2,1]:z23,u[5,4]:z56}
Delta=z12-z23-z45+z56

nzcols=[c for c in range(Jc.cols) if any(Jc[r,c]!=0 for r in range(Jc.rows))]
assert nzcols==[3,4,5,6,7,8,11,12]
maxminors=[]
for cols in combinations(nzcols,6):
    d=sp.factor(Jc[:,cols].det())
    if d!=0:
        maxminors.append((cols,d))
assert len(maxminors)==7
# Every nonzero maximal minor is divisible by Delta, after the source-coordinate rename.
for cols,d in maxminors:
    dz=sp.factor(d.subs(rename))
    q,r=sp.div(dz,Delta)
    assert sp.expand(r)==0, (cols,dz)
# And one maximal minor is exactly +/- Delta, so vanishing of all maximal minors is exactly Delta=0.
assert any(sp.factor(d.subs(rename)) in (Delta,-Delta) for _,d in maxminors)

# Uniform rank >=5: a constant 5x5 minor is 1.
rows=(0,1,2,3,4)
cols=(3,4,6,7,8)  # u41,u42,u51,u52,u53
minor5=sp.factor(Jc[list(rows),list(cols)].det())
assert minor5==1

# Explicit non-permutation singular point on the hyperplane: z12=z23=1, others 0.
pt={z12:1,z23:1,z45:0,z56:0,z13:0,z46:0}
Jz=Jc.subs(rename)
assert Delta.subs(pt)==0
assert Jz.subs(pt).rank()==5
# Explicit smooth point: z12=1 and all other cell coordinates zero.
pt2={z12:1,z23:0,z45:0,z56:0,z13:0,z46:0}
assert Delta.subs(pt2)==1
assert Jz.subs(pt2).rank()==6

print("positions", positions)
print("nonzero_maximal_minors", len(maxminors))
print("maximal_minor_factors", sorted({str(sp.factor(d.subs(rename))) for _,d in maxminors}))
print("constant_5x5_minor", minor5)
print("singular_test_rank", Jz.subs(pt).rank())
print("smooth_test_rank", Jz.subs(pt2).rank())
print("VERIFY_OK")
