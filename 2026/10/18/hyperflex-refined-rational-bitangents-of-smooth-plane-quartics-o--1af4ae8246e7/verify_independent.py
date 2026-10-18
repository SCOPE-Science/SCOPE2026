"""Independent exact checks of the F3 quartic orbit/bitangent census.
No dependency on the generated coefficient-action or restriction matrices.
"""
from itertools import product
from collections import deque
import csv, pathlib, time
import sympy as sp
x,y,z,u,v=sp.symbols('x y z u v')
M=[(i,j,4-i-j) for i in range(4,-1,-1) for j in range(4-i,-1,-1)]
DATA=pathlib.Path(__file__).parent
ROWS=list(csv.DictReader(open(DATA/'orbits.csv')))

def normalized(p):
 f=next(w for w in p if w%3)
 return tuple(w*pow(f%3,-1,3)%3 for w in p)
P=sorted({normalized((a,b,c)) for a,b,c in product(range(3),repeat=3) if a or b or c})
assert len(P)==13
lines=P
basis=[]
for l in lines:
 K=[p for p in P if sum(l[i]*p[i] for i in range(3))%3==0]
 assert len(K)==4
 # intentionally use final two basis points; independent of first-two choice
 A,B=K[-1],K[-2]
 if B==A:raise AssertionError
 basis.append((A,B))

# Compute all quadratic squares by sympy expansion, classifying squarefree quadratic factors.
def qc(a,b,c):
 q=sp.Poly(a*u*u+b*u*v+c*v*v,u,v,modulus=3)
 return tuple(int((q*q).coeff_monomial(u**(4-j)*v**j))%3 for j in range(5))
pro=set(); hyp=set()
for a,b,c in product(range(3),repeat=3):
 if a==b==c==0:continue
 t=normalized((a,b,c));sq=qc(*t)
 if (t[1]*t[1]-t[0]*t[2])%3:pro.add(sq)
 else:hyp.add(sq)
assert len(pro)==9 and len(hyp)==4

# construct restriction transformation independently using substitution and sympy expansions
R=[]
for A,B in basis:
 rr=[]
 for i,j,k in M:
  f=sp.Poly(sp.expand((A[0]*u+B[0]*v)**i*(A[1]*u+B[1]*v)**j*(A[2]*u+B[2]*v)**k),u,v,modulus=3)
  rr.append(tuple(int(f.coeff_monomial(u**(4-t)*v**t))%3 for t in range(5)))
 R.append(rr)

def check_bitangents(code):
 coeff=[]
 for _ in range(15):coeff.append(code%3);code//=3
 assert code==0
 outp=outh=0; proper_lines=[];hyper_lines=[]
 for t,row in enumerate(R):
  d=[sum(coeff[i]*row[i][j] for i in range(15))%3 for j in range(5)]
  if not any(d):continue
  d=normalized(d)
  if d in pro:outp+=1;proper_lines.append(lines[t])
  elif d in hyp:outh+=1;hyper_lines.append(lines[t])
 return outp,outh,proper_lines,hyper_lines

def check_group_order():
 # generators as matrices acting on column vectors
 g=[((1,1,0),(0,1,0),(0,0,1)),((0,1,0),(1,0,0),(0,0,1)),((1,0,0),(0,0,1),(0,1,0)),((2,0,0),(0,1,0),(0,0,1))]
 def permutation(g):
  return tuple(P.index(normalized(tuple(sum(row[j]*p[j] for j in range(3))%3 for row in g))) for p in P)
 gens=[permutation(gi) for gi in g]
 identity=tuple(range(len(P)));group={identity};Q=deque([identity])
 while Q:
  perm=Q.popleft()
  for gen in gens:
   p=tuple(perm[gen[i]] for i in range(len(P)))
   if p not in group:group.add(p);Q.append(p)
 assert len(group)==5616,len(group)
 print('PGL3(F3) order checked independently:',len(group))

if __name__=='__main__':
 start=time.time();check_group_order()
 for i,row in enumerate(ROWS):
  pr,hy,_,_=check_bitangents(int(row['code']))
  if int(row['smooth'])==1:
   assert pr==int(row['bitangent_proper']) and hy==int(row['hyperflex']),(i,row,pr,hy)
 print('Bitangent spectra independently verified for all',sum(int(x['smooth']) for x in ROWS),'smooth orbits; secs',round(time.time()-start,2))
 for row in ROWS:
  if row['smooth']=='1' and row['bitangent_proper']=='9':
   pr,hy,l,h=check_bitangents(int(row['code']))
   print('MAX',row['code'],'orbit',row['size'],'rational_points',row['rational_points'],'proper_lines',l,'hyper',h)
