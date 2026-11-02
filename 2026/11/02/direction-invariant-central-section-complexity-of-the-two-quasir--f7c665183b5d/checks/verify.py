"""Exact Q(phi) checks for central sections of the two quasiregular solids.
Run: python3 checker.py. No nonstandard dependencies.
"""
from itertools import combinations, product

Z=(0,0)
ONE=(1,0)
PHI=(0,1)

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y): return (x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def vadd(x,y): return tuple(add(a,b) for a,b in zip(x,y))
def vsub(x,y): return tuple(sub(a,b) for a,b in zip(x,y))
def dot(x,y):
 s=Z
 for a,b in zip(x,y): s=add(s,mul(a,b))
 return s

def cross(x,y):
 return (sub(mul(x[1],y[2]),mul(x[2],y[1])),
         sub(mul(x[2],y[0]),mul(x[0],y[2])),
         sub(mul(x[0],y[1]),mul(x[1],y[0])))

def sign(z):
 # 2(a+b*phi)=(2a+b)+b*sqrt(5).
 a,b=z; p=2*a+b
 if b==0: return (p>0)-(p<0)
 if p==0: return (b>0)-(b<0)
 if p*b>0: return (b>0)-(b<0)
 g=p*p-5*b*b
 assert g!=0
 return ((p>0)-(p<0)) if g>0 else ((b>0)-(b<0))

def construct(name):
 if name=='icosidodecahedron':
  V=[]
  for c in range(3):
   for s,t in product((-1,1),repeat=2):
    v=[Z,Z,Z];v[(c+1)%3]=(s,0);v[(c+2)%3]=(0,t)
    V.append(tuple(v))
  dist= (4,0)
  assert len(V)==12
 else:
  V=[]
  for i in range(3):
   for s in (-1,1):
    v=[Z,Z,Z];v[i]=(s,0);V.append(tuple(v))
  dist=(2,0)
  assert len(V)==6
 E=[(i,j) for i,j in combinations(range(len(V)),2) if dot(vsub(V[i],V[j]),vsub(V[i],V[j]))==dist]
 assert len(E)==({'icosidodecahedron':30,'cuboctahedron':12}[name])
 idx={e:i for i,e in enumerate(E)}
 tris=[(i,j,k) for i,j,k in combinations(range(len(V)),3)
       if all(tuple(sorted(z)) in idx for z in combinations((i,j,k),2))]
 assert len(tris)==({'icosidodecahedron':20,'cuboctahedron':8}[name])
 R=[vadd(V[i],V[j]) for i,j in E] # actual vertices are R/2
 T=[tuple(idx[e] for e in combinations(tri,2)) for tri in tris]
 B=[tuple(idx[e] for e in E if i in e) for i in range(len(V))]
 RE=set()
 for tri in T:
  for e in combinations(tri,2): RE.add(tuple(sorted(e)))
 assert len(RE)==({'icosidodecahedron':60,'cuboctahedron':24}[name])
 assert all(sum(i in edge for edge in RE)==4 for i in range(len(R)))
 # Each original edge has precisely two opposite triangular third vertices.
 for i,j in E:
  common=[k for k in range(len(V)) if (min(i,k),max(i,k)) in idx and (min(j,k),max(j,k)) in idx]
  assert len(common)==2
  u,v=V[i],V[j]
  wsum=vadd(V[common[0]],V[common[1]])
  assert cross(vadd(u,v),wsum)==(Z,Z,Z)
  # Four distinct neighbors of the rectified vertex.
  a,b,c,d=[vadd(u,V[common[0]]),vadd(v,V[common[0]]),
             vadd(u,V[common[1]]),vadd(v,V[common[1]])]
  assert cross(vadd(a,d),vadd(u,v))==(Z,Z,Z)
  assert cross(vadd(b,c),vadd(u,v))==(Z,Z,Z)
  assert len({idx[tuple(sorted((i,k))) ] for k in common} | {idx[tuple(sorted((j,k))) ] for k in common})==4

 def test_normal(n):
  n=tuple((int(x),0) for x in n)
  s=[sign(dot(n,r)) for r in R]
  if 0 in s: return None
  NT=sum(min(s[i] for i in f)<0<max(s[i] for i in f) for f in T)
  NB=sum(min(s[i] for i in f)<0<max(s[i] for i in f) for f in B)
  NE=sum(s[i]!=s[j] for i,j in RE)
  assert NT+NB==NE
  return NT,NB,NE

 expected={'icosidodecahedron':(6,6,12),'cuboctahedron':(4,4,8)}[name]
 base=test_normal((1,2,4))
 assert base==expected,(name,base)
 tested=0
 for n in product(range(-5,6),repeat=3):
  if n==(0,0,0): continue
  out=test_normal(n)
  if out is None: continue
  assert out==expected,(name,n,out)
  tested+=1
 print(name, 'original_vertices=',len(V),'original_edges=',len(E),'original_triangles=',len(tris),
       'rectified_edges=',len(RE),'symbolic_edge_balance_checks=',len(E),
       'generic_rational_directions=',tested,'triangle_face_hits=',base[0],
       'other_face_hits=',base[1],'section_sides=',base[2])
 return expected

if __name__=='__main__':
 assert construct('cuboctahedron')==(4,4,8)
 assert construct('icosidodecahedron')==(6,6,12)
 print('EXACT CHECKS PASSED')
