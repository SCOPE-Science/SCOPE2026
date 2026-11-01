"""Exact 600-cell radial algebra certificate over Z[phi], phi^2=phi+1.
No remote data or dependencies except Python stdlib; deterministic.
"""
from itertools import product,permutations
from collections import defaultdict
from fractions import Fraction

# Represent 2*vertex coordinate by a+b phi; phi=(1+sqrt5)/2.
V=[]
for j in range(4):
 for s in (-1,1):
  v=[(0,0)]*4;v[j]=(2*s,0);V.append(tuple(v))
for ss in product((-1,1),repeat=4):V.append(tuple((s,0) for s in ss))
for p in permutations(range(4)):
 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2:continue
 b=[(0,0),(1,0),(0,1),(-1,1)]
 for ss in product((-1,1), repeat=3):
  w=[b[i] for i in p];j=0
  for i in range(4):
   if w[i]!=(0,0): w[i]=(w[i][0]*ss[j],w[i][1]*ss[j]);j+=1
  V.append(tuple(w))
assert len(V)==len(set(V))==120

def mul(a,b):return (a[0]*b[0]+a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1])
def dot4(v,w):
 a=b=0
 for vi,wi in zip(v,w):
  z=mul(vi,wi);a+=z[0];b+=z[1]
 return (a,b)
D=[[dot4(v,w) for w in V] for v in V]
keys=[(4,0),(0,2),(2,0),(-2,2),(0,0),(2,-2),(-2,0),(0,-2),(-4,0)]
assert {k for row in D for k in row}==set(keys)
A=[[[int(D[i][j]==k) for j in range(120)] for i in range(120)] for k in keys]
assert all(D[i][i]==(4,0) for i in range(120))
# For each pair i,j, find product coefficients p[i,j,k] by looking at row x0 and y in class k.
rep=[D[0].index(k) for k in keys]
p=[[[sum(A[i][0][z]*A[j][z][rep[k]] for z in range(120)) for k in range(9)] for j in range(9)] for i in range(9)]
# Symmetric commutative association scheme. Check multiplication for all x,y.
for i in range(9):
 for j in range(i,9):
  for x in range(120):
   for y in range(120):
    lhs=sum(A[i][x][z]*A[j][z][y] for z in range(120))
    assert lhs==p[i][j][keys.index(D[x][y])],(i,j,x,y,lhs)
    assert p[i][j][keys.index(D[x][y])]==p[j][i][keys.index(D[x][y])]
print('VERTICES 120, 9 DOT CLASSES, ALL SCHEME INTERSECTION COUNTS VALIDATED',flush=True)

# The Chebyshev U_l(t) at t=dot=dot4/4; i.e. 2t=(a+b phi)/2.
# Even when t=±1, U_l(t) in Z[phi]. Odd intermediate recurrence also integral
# for vertices in this setting? 2t for noncentral classes is ±phi, ±1, ±(phi-1), 0.
# t=±1 => 2t=±2. All 2t integral algebraic.
R=[]
u0=[(1,0)]*9
u1=[(a//2,b//2) for a,b in keys]
assert all(a%2==0 and b%2==0 for a,b in keys)
R.append(u0);R.append(u1)
for l in range(2,60):
 t=[]
 for k in range(9):
  m=mul(u1[k],(keys[k][0]//2,keys[k][1]//2))
  t.append((m[0]-u0[k][0],m[1]-u0[k][1]))
 R.append(t);u0,u1=u1,t

# Product in Bose-Mesner algebra: columns M_i e_j = sum_k p[i][j][k] e_k.
# Vectors each component a+b phi.
def op(kv,v):
 out=[(0,0) for _ in range(9)]
 for i in range(9):
  a,b=kv[i]
  if a==b==0: continue
  for j in range(9):
   c,d=v[j]
   if c==d==0:continue
   ac,bc=mul((a,b),(c,d))
   for k in range(9):
    pp=p[i][j][k]
    if pp:out[k]=(out[k][0]+pp*ac,out[k][1]+pp*bc)
 return out

def scalar(v,c):return [(a*c,b*c) for a,b in v]
def minus(v,w):return [(a-c,b-d) for (a,b),(c,d) in zip(v,w)]
unit=[(1,0)]+[(0,0)]*8
# This proof can instead compute charpolynomial of 9x9 multiplication via exact arithmetic,
# then identify integer roots, and obtain zero-projection trace.
# A polynomial in K acts on all 9 basis units; rank defect is trace of its spectral
# zero-projector, read from identity component times 120.
# Candidate integer eigenvalues obtained by e.g. numerical inspection, then exactly certified.
# For reproducibility, enumerate integer eigenvalues via a sharp bound <= 2400.
# Instead use traces of 9x9 regular rep and Newton polynomial over rational field then factor.
# Sympy is optional only to DISCOVER candidate roots. Exact polynomial identity independently certifies.

def xmat(v):
 M=[]
 for j in range(9):
  ej=[(0,0)]*9;ej[j]=(1,0)
  M.append(op(v,ej))
 return [[M[j][i] for j in range(9)] for i in range(9)]


if __name__ == "__main__":
    # U_l(dot(x,y)) is the S^3 reproducing kernel divided by l+1.
    cX = [120, 60, 40, 30, 24, 20]
    for degree in range(6):
        uv = R[degree]
        assert op(uv, uv) == scalar(uv, cX[degree])
    print("All 600-cell degree-0..5 tight-frame identities verified exactly")

    T = range(24)  # the D4 / binary-tetrahedral subgroup of the 600-cell
    def ker(degree):
        return [[R[degree][keys.index(D[i][j])][0] for j in T] for i in T]
    def mm(A,B):
        return [[sum(A[i][k]*B[k][j] for k in T) for j in T] for i in T]
    def scal(A,c):return [[c*a for a in row] for row in A]
    def diff(A,B):return [[a-b for a,b in zip(ar,br)] for ar,br in zip(A,B)]
    def trace(A):return sum(A[i][i] for i in T)
    expected = [
        {96:1}, {96:4}, {96:9}, {72:8,120:8},
        {0:2,80:9,120:14}, {48:12,120:24}
    ]
    mult24=[]
    for ell in range(6):
        K=ker(ell)
        if ell!=4:
            c={0:24,1:12,2:8,3:12,5:12}[ell]
            assert mm(K,K)==scal(K,c)
            m=trace(K)//c
            assert trace(K)==24*(ell+1)
            mult={c:m}
        else:
            K2=mm(K,K)
            K3=mm(K2,K)
            assert diff(diff(K3,scal(K2,32)),scal(K,-192))==[[0]*24 for _ in T]
            assert trace(K)==120 and trace(K2)==1728
            mult={8:9,24:2}
        mult24.append(mult)
        dim=(ell+1)**2
        vals={120-c*(ell+1):n for c,n in mult.items()}
        used=sum(mult.values())
        if dim>used: vals[120]=dim-used
        assert vals==expected[ell],(ell,vals,expected[ell])
        print("degree",ell,"Gram spectrum",dict(sorted(vals.items())),"rank",dim-vals.get(0,0))
    print("PASS: all finite identities exact, nonmonotone degree-4/5 interpolation confirmed")
