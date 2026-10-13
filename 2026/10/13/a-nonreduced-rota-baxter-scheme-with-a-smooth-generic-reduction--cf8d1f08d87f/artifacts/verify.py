from itertools import product
import sympy as S
A,B,H,C,D,J,U,V,K,L=S.symbols('a b h c d j u v k lam')
R=S.Matrix([[A,B,H],[C,D,J],[U,V,K]])
basis=[S.eye(3)[:,i] for i in range(3)]
def mul(x,y):return S.Matrix([0,0,x[0]*y[1]-x[1]*y[0]])
def defct(i,j):
 x,y=basis[i],basis[j]
 return (mul(R*x,R*y)-R*(mul(R*x,y)+mul(x,R*y)+L*mul(x,y))).applyfunc(S.expand)
s=A+D+L
f=A*D-B*C-K*s
checks={
 (0,1):[-H*s,-J*s,f],
 (0,2):[-H*J,-J**2,(A-K)*J-C*H],
 (1,2):[H**2,H*J,B*J+(K-D)*H]
}
for (i,j),vec in checks.items():
 assert all(S.expand(x-y)==0 for x,y in zip(defct(i,j),vec))
 assert all(S.expand(x+y)==0 for x,y in zip(defct(j,i),vec))
for i in range(3):assert all(S.expand(x)==0 for x in defct(i,i))
print('SYMBOLIC_DEFECTS_OK')
vars=[A,B,H,C,D,J,U,V,K]
polys=[x for v in checks.values() for x in v]
# fixed nonzero weight set to 1, base R0 with B=diag(0,-1), central k=0
subs={A:0,B:0,H:0,C:0,D:-1,J:0,U:0,V:0,K:0,L:1}
T=S.Matrix(polys).jacobian(vars).subs(subs)
assert T.rank()==2
Tred=S.Matrix([H,J,f]).jacobian(vars).subs(subs)
assert Tred.rank()==3
print('TANGENT_DIMS_OK full=7 reduced=6')
# First-order deformation along R(e3)=eps*e2, unobstructable due to j^2
E=S.symbols('eps')
sub_jet={A:0,B:0,H:0,C:0,D:-L,J:E,U:0,V:0,K:0}
assert all(S.expand(poly.subs(sub_jet)).subs(E**2,0)==0 for poly in polys)
assert S.expand((-J**2).subs(sub_jet))==-E**2
print('DUAL_NUMBER_OBSTRUCTION_OK')

def rawRB(coords,lam,q):
 a,b,h,c,d,j,u,v,k=coords
 vectors=((a,c,u),(b,d,v),(h,j,k))
 def prod(x,y):return (0,0,(x[0]*y[1]-x[1]*y[0])%q)
 def add(*v):return tuple(sum(x[i] for x in v)%q for i in range(3))
 def matvec(v):return tuple(sum(v[t]*vectors[t][i] for t in range(3))%q for i in range(3))
 unit=((1,0,0),(0,1,0),(0,0,1))
 for i in range(3):
  for z in range(3):
   lhs=prod(vectors[i],vectors[z])
   rhs=matvec(add(prod(vectors[i],unit[z]),prod(unit[i],vectors[z]),tuple(lam*t for t in prod(unit[i],unit[z]))))
   if lhs!=rhs:return False
 return True

for q in (2,3):
 for lam in (0,1):
  total=0; mismatch=0
  for coords in product(range(q),repeat=9):
   direct=rawRB(coords,lam,q)
   a,b,h,c,d,j,u,v,k=coords
   pred= h==0 and j==0 and (a*d-b*c-k*(a+d+lam))%q==0
   mismatch+=(direct!=pred)
   total+=direct
  assert mismatch==0
  expected=q**6+(q**4 if lam else 0)
  assert total==expected,(q,lam,total,expected)
  print('FULL_ENUM_OK',q,lam,total)

for q in (3,5,7,11):
 for lam in (0,1,2):
  num=0
  for a,b,c,d,k in product(range(q),repeat=5):
   if (a*d-b*c-k*(a+d+lam))%q==0:num+=1
  assert num*q*q==q**6+(q**4 if lam else 0)
  print('FIBER_COUNT_OK',q,lam,num*q*q)
print('VERIFY_OK')
