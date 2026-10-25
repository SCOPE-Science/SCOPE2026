"""Exact symbolic Hessian and independent hull checks for a seven-vertex inscribed four-polytope."""
import sympy as sp
import numpy as np
from scipy.spatial import ConvexHull
from itertools import combinations, product

rt=sp.sqrt(3)
h=sp.Rational(1,2)
E=sp.eye(4)
P=[sp.Matrix([1,0,0,0]),sp.Matrix([-h,rt*h,0,0]),sp.Matrix([-h,-rt*h,0,0]),E[:,2],-E[:,2],E[:,3],-E[:,3]]
B=[]
for i in range(3):
 B.append([sp.Matrix([-P[i][1],P[i][0],0,0]),E[:,2],E[:,3]])
B.extend([[E[:,0],E[:,1],E[:,3]],[E[:,0],E[:,1],E[:,3]],[E[:,0],E[:,1],E[:,2]],[E[:,0],E[:,1],E[:,2]]])
F=[]
for i in range(3):
 for j,k in product([3,4],[5,6]):
  I=(i,(i+1)%3,j,k)
  base=sp.det(sp.Matrix.hstack(*(P[t] for t in I)))
  assert sp.simplify(base**2-sp.Rational(3,4))==0
  F.append((I,sp.sign(base)))
V=sp.simplify(sum(sign*sp.det(sp.Matrix.hstack(*(P[t] for t in I))) for I,sign in F)/24)
assert V==rt/4

def determinant(cols): return sp.det(sp.Matrix.hstack(*cols))
G=sp.zeros(21,1); H=sp.zeros(21)
for I,sgn in F:
 cols=[P[k] for k in I]
 base=sgn*determinant(cols)/24
 for x in I:
  for a in range(3):
   c=cols.copy();c[I.index(x)]=B[x][a]
   G[3*x+a,0]+=sgn*determinant(c)/24
   H[3*x+a,3*x+a]-=base
 for x,y in combinations(I,2):
  for a,b in product(range(3),repeat=2):
   c=cols.copy();c[I.index(x)]=B[x][a];c[I.index(y)]=B[y][b]
   v=sgn*determinant(c)/24
   H[3*x+a,3*y+b]+=v;H[3*y+b,3*x+a]+=v
assert G==sp.zeros(21,1)
assert H==H.T
lam=sp.Symbol('lam')
cp=sp.factor(H.charpoly(lam).as_expr(),extension=rt)
want=lam**6*(lam+rt/8)**6*(lam+rt/6)**2*(lam+rt/4)**3*(lam+7*rt/24)**4
assert sp.simplify(cp-want)==0
print('facets',len(F),'volume',V,'gradient','zero','H charpoly factor verified')
print('eigenvalues',sorted([(str(x),m) for x,m in H.eigenvals().items()]))
assert H.rank()==15
# Check that skew-symmetric rotations span the kernel.
rots=[]
for i,j in combinations(range(4),2):
 Om=sp.zeros(4);Om[i,j]=1;Om[j,i]=-1
 vv=sp.zeros(21,1)
 for k in range(7):
  vv0=Om*P[k]
  for a in range(3):vv[3*k+a,0]=sp.simplify(B[k][a].dot(vv0))
 assert H*vv==sp.zeros(21,1)
 rots.append(vv)
assert sp.Matrix.hstack(*rots).rank()==6
print('rotational kernel exact, rank 6')
# independent volume checks with direct convex hull, no determinant sum.
pn=np.array([np.array(v,dtype=float).reshape(4) for v in P]); bn=np.array([[np.array(z,dtype=float).reshape(4) for z in block] for block in B])
hn=np.array(H.evalf(),dtype=float)
rg=np.random.default_rng(25102026)
for rep in range(5):
 z=rg.normal(size=21);z/=np.linalg.norm(z)
 vv=np.einsum('ij,ijk->ik',z.reshape(7,3),bn)
 pred=.5*z@hn@z
 for t in [1e-2,3e-3,1e-3]:
  new=pn+t*vv;new=new/np.linalg.norm(new,axis=1)[:,None]
  hull=ConvexHull(new)
  assert len(hull.simplices)==12
  diff=hull.volume-float(V)
  assert abs(diff/t**2-pred)<0.018*t+1.e-8,(rep,t,diff,pred)
print('random 4D hull second-order finite difference verified')
