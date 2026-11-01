import sympy as S, itertools,networkx as nx
m=4;V=[(i,s) for i in range(m) for s in (1,-1)]
def valid(J):
 F=set(J)
 if any((i,1) in F and (i,-1) in F for i in range(m)):return False
 if any(((i,1) in F and ((i+1)%m,-1) in F) or ((i,-1) in F and ((i+1)%m,1) in F) for i in range(m)):return False
 return not(len(F)==m and any(all((i,s) in F for i in range(m)) for s in (1,-1)))
E=[e for e in itertools.combinations(range(8),2) if valid(V[z] for z in e)]
T=[t for t in itertools.combinations(range(8),3) if valid(V[z] for z in t)]
G=nx.Graph();G.add_nodes_from(range(8));G.add_edges_from(E)
TE={tuple(sorted(e)) for e in nx.minimum_spanning_tree(G).edges()}
NT=[e for e in E if e not in TE];lookup={e:i for i,e in enumerate(NT)}
fund=[]
for u,v in NT:
 c={tuple(sorted((u,v))):1}
 path=nx.shortest_path(nx.Graph(list(TE)),v,u)
 for a,b in zip(path,path[1:]):
  key=tuple(sorted((a,b))); c[key]=(1 if a<b else -1)
 fund.append(c)
rows=[]
for a,b,c in T:
 f={(a,b):1,(a,c):-1,(b,c):1}
 rows.append([f.get(e,0) for e in NT])
B=S.Matrix(rows)
N=S.Matrix.hstack(*B.nullspace())
print('B size rank',B.shape,B.rank(),'N=',N.T)
assert all(v.q==1 for v in N)
free=[i for i in range(len(NT)) if any(N[i,z] for z in range(N.cols))]
# find identity 3x3 minor of N to extract coefficients, brute
ext=None
for inds in itertools.combinations(range(N.rows),N.cols):
 P=N[list(inds),:]
 if abs(P.det())==1:ext=(inds,P.inv());break
print('cohomology unimodular extraction',ext)
def act(v,kind):
 i,s=v
 return ((i+1)%m,s) if kind=='r' else ((-i-1)%m,-s)
def sign_image(a,b,kind):
 x=V.index(act(V[a],kind));y=V.index(act(V[b],kind));return (tuple(sorted((x,y))),1 if x<y else -1)
def cmat(kind):
 C=S.zeros(len(NT),len(NT))
 for col,f in enumerate(fund):
  for (a,b),sgn in f.items():
   key,eps=sign_image(a,b,kind)
   if key in lookup:C[lookup[key],col]+=sgn*eps
 return C
A={}
for kind in ('r','s'):
 Y=cmat(kind).T*N
 inds,Pinv=ext
 M=Pinv*Y[list(inds),:]
 assert Y==N*M
 A[kind]=M
 print(kind,'cohomology action',M)
r=A['r'];s=A['s'];print('r^2-I=',r**2-S.eye(3),'r^4 I?',r**4==S.eye(3),'s^2?',s**2==S.eye(3),'srs?',s*r*s==r**3)
print('r mod 2',[[int(x)%2 for x in row] for row in r.tolist()]);print('r^2 mod 2',[ [int(x)%2 for x in row] for row in (r**2).tolist()])
print('charpoly',r.charpoly().as_expr())
print('basis N cols', N)
from sympy.matrices.normalforms import smith_normal_form
assert len(V)==8 and len(E)==16 and len(T)==8 and len(NT)==9
D=smith_normal_form(B,domain=S.ZZ)
assert [D[i,i] for i in range(6)] == [1]*6
assert all(D[i,i]==0 for i in range(6,8))
assert N.shape == (9,3) and B*N == S.zeros(8,3)
Q=S.Matrix([[1,-1,0],[-1,0,0],[1,0,-1]])
assert abs(Q.det())==1
assert Q.inv()*A['r']*Q == S.Matrix([[0,0,-1],[1,0,-1],[0,1,-1]])
assert Q.inv()*A['s']*Q == S.Matrix([[1,0,0],[1,0,-1],[1,-1,0]])
idx=S.Matrix([[1,1,0],[0,1,1],[1,0,1]]).det()
assert abs(idx)==2
assert any(int(x)%2 for x in (r**2-S.eye(3)))
print('VERIFY_OK: exact integral cohomology is natural D4 augmentation lattice A3; index 2')
