from collections import defaultdict
from itertools import combinations_with_replacement
import random
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def full_snf(bands):
 S=sorted(set(x for lo,hi in bands for x in range(lo,hi+1))); P=defaultdict(list)
 for i in range(len(S)):
  for j in range(i,len(S)):P[S[i]+S[j]].append((i,j))
 mat=[]
 for ps in P.values():
  for i,j in ps[1:]:
   x,y=ps[0];z=[0]*len(S)
   for idx,sgn in [(i,1),(j,1),(x,-1),(y,-1)]:z[idx]+=sgn
   mat.append(z)
 A=sp.Matrix(mat) if mat else sp.zeros(0,len(S))
 D=smith_normal_form(A,domain=ZZ)
 dd=[abs(int(D[i,i])) for i in range(min(D.rows,D.cols)) if D[i,i]]
 return len(S)-len(dd),[d for d in dd if d>1]

def compressed_snf(bands):
 r=len(bands); typ=[]
 for i in range(r):
  for j in range(i,r):
   l=bands[i][0]+bands[j][0]; h=bands[i][1]+bands[j][1]
   typ.append((i,j,l,h))
 row=[]
 for i,x in enumerate(typ):
  for y in typ[i+1:]:
   if max(x[2],y[2])<=min(x[3],y[3]):
    v=[0]*r
    for idx,sgn in [(x[0],1),(x[1],1),(y[0],-1),(y[1],-1)]: v[idx]+=sgn
    row.append(v)
 A=sp.Matrix(row) if row else sp.zeros(0,r)
 D=smith_normal_form(A,domain=ZZ)
 dd=[abs(int(D[i,i])) for i in range(min(D.rows,D.cols)) if D[i,i]]
 return 1+r-len(dd),[d for d in dd if d>1]

rgen=random.Random(1729)
found=[]
for r in [2,3,4,5]:
 for k in range(70):
  current=0; bands=[]
  for i in range(r):
   start=current+rgen.randrange(0,6)
   end=start+rgen.randrange(2,5)
   bands.append((start,end)); current=end+1
  x=full_snf(bands); y=compressed_snf(bands)
  assert x==y,(bands,x,y)
  if x[1] and len(found)<10:found.append((bands,x))
 print('PASS number_of_bands=',r,'parameter_tests=70')
print('TORSION_examples:',found)
