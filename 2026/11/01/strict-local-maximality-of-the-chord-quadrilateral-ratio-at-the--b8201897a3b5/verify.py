"""Certified interval second-jet check for a local heptagon quadrilateral theorem.
Requires Python 3 and mpmath. All inequalities are checked with outward-rounded
40-digit interval arithmetic; no floating-point tolerance establishes a sign.
"""
from mpmath import iv
iv.dps=45
N=8
Z=lambda: iv.mpf(0)
U=lambda: iv.mpf(1)
class J:
 def __init__(self,v,g=None,h=None):
  self.v=iv.mpf(v);self.g=g if g is not None else [Z() for _ in range(N)]
  self.h=h if h is not None else [[Z() for _ in range(N)] for _ in range(N)]
 @classmethod
 def var(cls,i,v):
  g=[Z() for _ in range(N)];g[i]=U();return cls(v,g)
 def __add__(a,b):
  if not isinstance(b,J):b=J(b)
  return J(a.v+b.v,[a.g[i]+b.g[i] for i in range(N)],[[a.h[i][j]+b.h[i][j] for j in range(N)] for i in range(N)])
 __radd__=__add__
 def __neg__(a):return J(-a.v,[-x for x in a.g],[[-x for x in row] for row in a.h])
 def __sub__(a,b):return a+-b if isinstance(b,J) else a+J(-b)
 def __rsub__(a,b):return -a+b
 def __mul__(a,b):
  if not isinstance(b,J):b=J(b)
  return J(a.v*b.v,[a.g[i]*b.v+a.v*b.g[i] for i in range(N)],[[a.h[i][j]*b.v+a.v*b.h[i][j]+a.g[i]*b.g[j]+a.g[j]*b.g[i] for j in range(N)] for i in range(N)])
 __rmul__=__mul__
 def inv(a):
  q=U()/a.v;q2=q*q;q3=q2*q
  return J(q,[-x*q2 for x in a.g],[[2*a.g[i]*a.g[j]*q3-a.h[i][j]*q2 for j in range(N)] for i in range(N)])
 def __truediv__(a,b):return a*(b.inv() if isinstance(b,J) else J(b).inv())
 def __rtruediv__(a,b):return a.inv()*b

def det(a,b,c,d):return a*d-b*c

def intersection(lines,a,b):
  x,y,z=lines[a];u,v,w=lines[b];d=det(x,y,u,v)
  return ((z*v-w*y)/d,(x*w-u*z)/d)

def candidate(pts,j,area):
  lines=[]
  for k in range(7):
   a,b=pts[k],pts[(k+1)%7];nx=b[1]-a[1];ny=a[0]-b[0];lines.append((nx,ny,nx*a[0]+ny*a[1]))
  e=[(j+2*k)%7 for k in range(4)];v=[intersection(lines,e[i],e[(i+1)%4]) for i in range(4)]
  a=sum((v[i][0]*v[(i+1)%4][1]-v[i][1]*v[(i+1)%4][0] for i in range(4)),J(0))/2
  return a/area

pi=iv.pi
pts=[]
for i in range(7):
 th=2*pi*i/7
 x,y=iv.cos(th),iv.sin(th)
 if i>=3: x=J.var(2*(i-3),x);y=J.var(2*(i-3)+1,y)
 else:x=J(x);y=J(y)
 pts.append((x,y))
area=sum((pts[i][0]*pts[(i+1)%7][1]-pts[i][1]*pts[(i+1)%7][0] for i in range(7)),J(0))/2
f=[candidate(pts,j,area) for j in range(7)]
print('chord competitor interval at regular heptagon:',f[0].v)
assert all(not (q.v.a>f[0].v.b or q.v.b<f[0].v.a) for q in f)
G=[[q.g[i] for i in range(N)] for q in f]
for i in range(N):
 s=sum((G[j][i] for j in range(7)),Z())
 assert s.a<=0<=s.b,('gradient-sum',i,s)
ix=[0,1,3,4,6,7];iy=[2,5]
A=[[G[j][k] for k in ix] for j in range(6)]
R=[[G[j][k] for k in iy] for j in range(6)]
# Eliminate with interval pivots; compute determinant and solve A*X=R.
detA=U()
for k in range(6):
 pivot=A[k][k];assert pivot.a>0 or pivot.b<0,('zero pivot',k,pivot)
 detA*=pivot
 for i in range(k+1,6):
  q=A[i][k]/pivot
  for j in range(k+1,6):A[i][j]-=q*A[k][j]
  for j in range(2):R[i][j]-=q*R[k][j]
  A[i][k]=Z()
X=[[Z(),Z()] for _ in range(6)]
for i in reversed(range(6)):
 for j in range(2):X[i][j]=(R[i][j]-sum((A[i][t]*X[t][j] for t in range(i+1,6)),Z()))/A[i][i]
B=[[Z(),Z()] for _ in range(N)]
for a,k in enumerate(ix):B[k]=[-X[a][0],-X[a][1]]
B[iy[0]]=[U(),Z()];B[iy[1]]=[Z(),U()]
H=[[(sum((f[t].h[i][j] for t in range(7)),Z())/7) for j in range(N)] for i in range(N)]
S=[[sum((B[i][a]*H[i][j]*B[j][b] for i in range(N) for j in range(N)),Z()) for b in range(2)] for a in range(2)]
detS=S[0][0]*S[1][1]-S[0][1]*S[1][0]
print('det pivot:',detA,'\nreduced Hessian:',S,'\nHessian determinant:',detS)
assert detA.a>0 or detA.b<0
assert S[0][0].b<0 and detS.a>0
print('PASS: exact interval certified gradient rank 6 and reduced negative-definite mean Hessian.')

# Exhaustive global base-point certificate: all 14 chord-normal directions.
# Four supporting lines give a bounded quadrilateral only if each angular
# gap between successive outward normals is < pi. Omitted or redundant
# constraints yield a triangular enclosure, separately excluded by the
# regular heptagon's inball radius.
import itertools
c=iv.cos(pi/7)
def bounded_area(ks):
 lines=[]
 for k in ks:
  th=k*pi/7
  x,y=iv.cos(th),iv.sin(th)
  h=U() if k%2==0 else c
  lines.append((x,y,h))
 verts=[]
 for i in range(4):
  x,y,h=lines[i];u,v,w=lines[(i+1)%4];den=x*v-y*u
  verts.append(((h*v-w*y)/den,(x*w-u*h)/den))
 return sum(((verts[i][0]*verts[(i+1)%4][1]-verts[i][1]*verts[(i+1)%4][0]) for i in range(4)),Z())/2
winner={tuple(sorted((k+2*t)%14 for k in (1,3,7,11))) for t in range(7)}
area_min=area.v*f[0].v
ntested=0
for ks in itertools.combinations(range(14),4):
 gaps=[ks[i+1]-ks[i] for i in range(3)]+[ks[0]+14-ks[-1]]
 if max(gaps)>=7:continue
 ntested+=1
 a=bounded_area(ks)
 if ks in winner:
  assert a.a<=area_min.b and area_min.a<=a.b,('winner',ks,a)
 else:
  assert a.a>area_min.b,('competitor',ks,a,area_min)
tri_min=3*iv.sqrt(3)*c*c
assert tri_min.a>area_min.b
print('PASS: all',ntested,'bounded four-direction supporting combinations, with',len(winner),'minimizing configurations; 3-side enclosures excluded by inball bound.')
