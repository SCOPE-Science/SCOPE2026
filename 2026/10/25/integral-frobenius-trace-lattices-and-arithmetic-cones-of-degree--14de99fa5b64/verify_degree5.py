"""Exact degree-five del Pezzo Frobenius Picard, trace-index, and cone verifier.
Requires SymPy 1.12 or newer; no external data files.
"""
import itertools, collections, math
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
Q=s.diag(1,-1,-1,-1,-1)
H=s.Matrix([1,0,0,0,0]); E=[s.eye(5)[:,i] for i in range(1,5)]
C=E[:]+[H-E[i]-E[j] for i,j in itertools.combinations(range(4),2)]
A=[E[0]-E[1],E[1]-E[2],E[2]-E[3],H-E[0]-E[1]-E[2]]
S=[s.eye(5)+a*(a.T*Q) for a in A]
def matstr(M):return [[int(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]
assert all((U.T*Q*U)==Q for U in S)
assert all((U+s.zeros(5))*(U+s.zeros(5))==s.eye(5) for U in S)
for U in S:
 assert {tuple(U*c) for c in C} == {tuple(c) for c in C}

def compsigma(p):
 seen=set();out=[]
 for i in range(5):
  if i not in seen:
   cy=[];k=i
   while k not in seen:seen.add(k);cy.append(k);k=p[k]
   out.append(tuple(cy))
 return tuple(sorted((len(c) for c in out),reverse=True))
base=tuple(range(5)); mats={base:s.eye(5)};stack=[base]
while stack:
 p=stack.pop()
 for k in range(4):
  q=list(p);q[k],q[k+1]=q[k+1],q[k];q=tuple(q)
  if q not in mats:
   mats[q]=S[k]*mats[p];stack.append(q)
assert len(mats)==120
for p,M in mats.items():
 for k in range(4):
  q=list(p);q[k],q[k+1]=q[k+1],q[k];q=tuple(q)
  assert S[k]*M==mats[q], (p,k)
assert all(len(set(tuple(M*c) for c in C))==10 for M in mats.values())

def integer_kernel(A):
 B=s.eye(A.cols)
 for rr in range(A.rows):
  if B.cols==0:break
  v=[int(z) for z in list(A[rr,:]*B)]
  if all(z==0 for z in v):continue
  U=s.eye(B.cols)
  for j in range(1,B.cols):
   aa=sum(v[k]*U[k,0] for k in range(B.cols)); bb=sum(v[k]*U[k,j] for k in range(B.cols))
   if bb==0:continue
   aa,bb=int(aa),int(bb);g=int(s.gcd(aa,bb)); ss,tt,gg=s.gcdex(aa,bb) # gcdex returns (s,t,g)
   assert int(gg)==g
   R=s.eye(B.cols);R[0,0]=ss;R[j,0]=tt;R[0,j]=-bb//g;R[j,j]=aa//g
   U=U*R
  B=B*U[:,1:]
  assert all(x==0 for x in A[:rr+1,:]*B)
 return B

def prim(v):
 v=list(v);d=math.lcm(*[int(s.denom(z)) for z in v]);v=[int(z*d) for z in v];g=math.gcd(*v)
 return tuple(z//g for z in v)

def raylist(U,B):
 # action on 10 C
 perm=[next(j for j,w in enumerate(C) if w==U*v) for v in C]
 visited=set();cycles=[]
 for i in range(10):
  if i in visited:continue
  x=i;cy=[]
  while x not in visited:visited.add(x);cy.append(x);x=perm[x]
  cycles.append(tuple(cy))
 orb=[sum((C[j] for j in cy),s.zeros(5,1)) for cy in cycles]
 # basis coordinates
 coord=[]
 for u in orb:
  xx=B.gauss_jordan_solve(u)[0]
  assert all(z.q==1 for z in xx)
  coord.append(tuple(int(z) for z in xx))
 return cycles,coord

def ext_rays(G,orbs):
 # inequalities D^T G u >=0
 normals=[G*s.Matrix(c) for c in orbs]
 r=G.cols; out=set()
 if r==1:
  sign=1 if all(int(n[0])>=0 for n in normals) else -1
  assert all(sign*int(n[0])>=0 for n in normals)
  return [(sign,)]
 for inds in itertools.combinations(range(len(normals)),r-1):
  mat=s.Matrix.hstack(*[normals[i] for i in inds]).T
  if mat.rank()!=r-1:continue
  ns=mat.nullspace()[0];v=prim(ns)
  prods=[(s.Matrix(v).T*n)[0] for n in normals]
  if all(z>=0 for z in prods):out.add(v)
  elif all(z<=0 for z in prods):out.add(tuple(-z for z in v))
 return sorted(out)

def eff_ext(orbs):
 vv=list(dict.fromkeys(prim(x) for x in orbs))
 # find whether a candidate is in nonnegative cone of others
 def represented(v, others):
  for k in range(1,min(len(others),len(v))+1):
   for ix in itertools.combinations(range(len(others)),k):
    mm=s.Matrix.hstack(*[s.Matrix(others[j]) for j in ix]);b=s.Matrix(v)
    if mm.rank()<k:continue
    if mm.row_join(b).rank()!=k:continue
    ss=mm.gauss_jordan_solve(b)[0]
    if all(z>=0 for z in ss):return True
  return False
 return [v for v in vv if not represented(v,[x for x in vv if x!=v])]


EXPECTED={
 (1,1,1,1,1):(5,10,10,1,1,(1,1,1,1,1)),
 (2,1,1,1):(4,7,7,-2,1,(1,1,1,2)),
 (2,2,1):(3,4,4,4,1,(1,2,2)),
 (3,1,1):(3,4,4,3,3,(1,1,3)),
 (3,2):(2,2,2,-6,1,(1,6)),
 (4,1):(2,2,2,-4,2,(1,4)),
 (5,):(1,1,1,5,1,(5,)),
}

def case_signature(M):
 B=integer_kernel(M-s.eye(5))
 assert B.cols==5-(M-s.eye(5)).rank()
 assert (M-s.eye(5))*B==s.zeros(5,B.cols)
 G=B.T*Q*B
 cycles,cc=raylist(M,B)
 rays=eff_ext(cc);nef=ext_rays(G,cc)
 m=s.Matrix.hstack(*[s.Matrix(v) for v in cc]);r=B.cols
 ix=math.gcd(*[abs(int(m[:,list(j)].det())) for j in itertools.combinations(range(m.cols),r)])
 D=smith_normal_form(G,domain=s.ZZ)
 diagonal=tuple(sorted(abs(int(D[j,j])) for j in range(r)))
 # Independent primal/dual pairing and exact extremality tests.
 for u in rays:
  if r>1:assert any(sum(x*y for x,y in zip(u,v))==0 for v in [tuple(G*s.Matrix(w)) for w in nef])
 for v in nef:
  assert all(int((s.Matrix(v).T*G*s.Matrix(u))[0])>=0 for u in rays)
 assert s.Rational(G.det())!=0
 return (r,len(rays),len(nef),int(G.det()),ix,diagonal),cycles,cc,rays,nef,B,G

classes=collections.defaultdict(list)
for p,M in mats.items():classes[compsigma(p)].append((p,M))
assert set(classes)==set(EXPECTED)
assert sum(len(v) for v in classes.values())==120
for cycle,cs in sorted(classes.items()):
 for p,M in cs:
  sig,*_=case_signature(M)
  assert sig==EXPECTED[cycle],(cycle,p,sig)
 print('type='+str(cycle),'S5_representatives='+str(len(cs)),'rank/eff/nef/disc/index/SNF='+str(EXPECTED[cycle]))
print('VERIFY_OK: all 120 Weyl group elements; seven Frobenius types, primitive Picard lattices, Gram SNF, full trace indices, exact effective and nef cone rays')
