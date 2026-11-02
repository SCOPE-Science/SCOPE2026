import itertools
import sympy as sp
# GF9 elements a+3*b, a,b in [0,2], i^2=-1=2
p=3

def ab(x):return x%3,x//3
def elem(a,b):return (a%3)+3*(b%3)
def add(x,y):
 a,b=ab(x);c,d=ab(y);return elem(a+c,b+d)
def neg(x):return elem(-ab(x)[0],-ab(x)[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 a,b=ab(x);c,d=ab(y);return elem(a*c-b*d,a*d+b*c)
def powr(x,n):
 o=1
 while n:
  if n&1:o=mul(o,x)
  x=mul(x,x);n//=2
 return o
def div(x,y):return mul(x,powr(y,7))
def S(v):
 o=0
 for t in v:o=add(o,powr(t,4))
 return o
def dot(a,b):
 o=0
 for x,y in zip(a,b):o=add(o,mul(x,y))
 return o
def vecpow(v,n):return tuple(powr(x,n) for x in v)
def normalize(v):
 i=next(i for i,x in enumerate(v) if x)
 return tuple(div(x,v[i]) for x in v)
pts=sorted(set(normalize(v) for v in itertools.product(range(9),repeat=3) if any(v)))
P=sorted(v for v in pts if S(v)==0)
assert len(pts)==91 and len(P)==28
# dictionary for tangent data

def cross(a,b):return (sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0])))
T={}
for q in P:
 line=vecpow(q,3)
 assert dot(line,q)==0
 for v in pts:
  if v!=q and dot(line,v)==0 and S(v)!=0:
   if S(v)==2: v=tuple(mul(4,x) for x in v)
   assert S(v)==1
   break
 else:raise Exception(q)
 for i,j in itertools.combinations(range(3),2):
  det=sub(mul(q[i],v[j]),mul(q[j],v[i]))
  if det:
   def tform(w,i=i,j=j,det=det,q=q):return div(sub(mul(q[i],w[j]),mul(q[j],w[i])),det)
   break
 T[q]=(line,v,tform)
assert all(powr(T[q][2](T[q][1]),2)==1 for q in P)
# list of curves (q,eps) eps 0->+1 1->-1
C=[(q,e) for q in P for e in (0,1)]

# line intersections
D=sp.zeros(56)
for i,(p1,e1) in enumerate(C):
 D[i,i]=-1
 for j in range(i+1,56):
  p2,e2=C[j]
  if p1==p2: m=2
  else:
   Q=cross(T[p1][0],T[p2][0]);assert any(Q)
   # homogeneous representative Q accepted
   w1=powr(T[p1][2](Q),2)
   w2=powr(T[p2][2](Q),2)
   if e1:w1=neg(w1)
   if e2:w2=neg(w2)
   m=int(w1==w2)
  D[i,j]=D[j,i]=m
assert sorted(set(D))==[-1,0,1,2]
# frobenius permutation
index={c:i for i,c in enumerate(C)}
F=[]
for i,(q,e) in enumerate(C):
 qp=normalize(vecpow(q,3))
 v=T[q][1]
 vp=vecpow(v,3)
 n=powr(T[qp][2](vp),2)
 assert n in (1,2),(q,n)
 ep=e if n==1 else 1-e
 F.append(index[(qp,ep)])
assert all(F[F[i]]==i for i in range(56))
assert all(F[i]!=i for i in range(56))
assert all(D[F[i],F[j]]==D[i,j] for i in range(56) for j in range(56))
# disjoint exceptional lines backtracking

def clique(ids):
 if len(ids)==7:return ids
 for j in range(ids[-1]+1 if ids else 0,56):
  if all(D[j,i]==0 for i in ids):
   res=clique(ids+[j])
   if res is not None:return res
 return None
basis=clique([])
assert basis and len(basis)==7
print('P2_F9',len(pts),'HERM_F9',len(P),'FROBENIUS_CURVES_FIXED',sum(i==f for i,f in enumerate(F)))
print('BASIS_7',basis)
assert sum(i<F[i] for i in range(56))==28
print('FROB_CYCLES',sum(i<F[i] for i in range(56)))
# determine coordinate class E from intersection with 7 disjoint curves and H

def cl(j):
 m=[int(D[j,i]) for i in basis]
 assert (1+sum(m))%3==0,(j,m)
 a=(1+sum(m))//3
 return sp.Matrix([a]+[-z for z in m])
E=[cl(j) for j in range(56)]
H=sp.Matrix([3]+[-1]*7)
assert all((3*e[0]+sum(e[1:]))==1 for e in E)
# check arbitrary intersection using intersection form diag(1,-1,...)
J=sp.diag(1,*([-1]*7))
assert all((E[i].T*J*E[j])[0]==D[i,j] for i in range(56) for j in range(56))
# Frobenius 8x8 columns E_basis Frobenius; L from anticanonical invariance
cols=[cl(F[i]) for i in basis]
L=(H+sum(cols,sp.zeros(8,1)))/3
assert all(x.q==1 for x in L)
M=sp.Matrix.hstack(L,*cols)
assert M*M==sp.eye(8)
assert M.T*J*M==J
assert M*H==H
print('FROBENIUS_MATRIX',M.tolist())
print('FROBENIUS_CHARPOLY',sp.factor(M.charpoly().as_expr()))
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
N=smith_normal_form(M-sp.eye(8),domain=ZZ)
print('SMITH_F_MINUS_I',N.diagonal())
print('TRACE',sp.trace(M),'BR_GROUP',tuple(abs(x) for x in N.diagonal() if abs(x)>1))
assert sum(normalize(vecpow(q,3))==q for q in P)==4
print('BITANGENT_FIXED_F3',sum(normalize(vecpow(q,3))==q for q in P))
# 3 point count
cnt3=0
for q in sorted(set(normalize(v) for v in itertools.product(range(3), repeat=3) if any(v))):
 f=S(q)
 cnt3+=(2 if f==1 else 1 if f==0 else 0)
print('SURFACE_F3_POINTS',cnt3)
cnt9=sum(2 if S(v)!=0 else 1 for v in pts)
assert (cnt3,cnt9)==(10,154)
print('SURFACE_F9_POINTS',cnt9)
# Integral root-reflection certificate for the 4A1 arithmetic class.
roots=[sp.Matrix(r) for r in [(2,-1,-1,-1,-1,0,-1,-1),(0,1,-1,0,0,0,0,0),(0,0,0,1,-1,0,0,0),(1,0,0,0,0,-1,-1,-1)]]
assert all((r.T*J*r)[0]==-2 for r in roots)
assert all((r.T*J*H)[0]==0 for r in roots)
assert all((r.T*J*s)[0]==0 for i,r in enumerate(roots) for s in roots[i+1:])
assert all(M*r==-r for r in roots)
RR=sp.eye(8)
for r in roots:RR=(sp.eye(8)+r*r.T*J)*RR
assert RR==M
print('FROBENIUS_ROOT_REFLECTIONS=4_ORTHOGONAL_A1')
assert all(abs(N[i,i])==1 for i in range(4)) and all(N[i,i]==0 for i in range(4,8))
assert (M+sp.eye(8))*(M-sp.eye(8))==sp.zeros(8)
assert sp.trace(M)==0
print('PICARD_H1_C2=0')
print('VERIFY_OK')
