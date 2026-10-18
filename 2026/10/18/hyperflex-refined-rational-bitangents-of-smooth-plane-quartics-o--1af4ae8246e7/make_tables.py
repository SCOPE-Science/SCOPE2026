from itertools import product
from math import comb
import json
from pathlib import Path
P=3
M4=[(i,j,4-i-j) for i in range(4,-1,-1) for j in range(4-i,-1,-1)]
M7=[(i,j,7-i-j) for i in range(7,-1,-1) for j in range(7-i,-1,-1)]
M3=[(i,j,3-i-j) for i in range(3,-1,-1) for j in range(3-i,-1,-1)]
assert len(M4)==15 and len(M7)==36 and len(M3)==10
# homogeneous polys as dict tuple exponent -> coeff
unit={(0,0,0):1}
def add(A,B):
 r=A.copy()
 for k,v in B.items():
  x=(r.get(k,0)+v)%3
  if x:r[k]=x
  elif k in r:del r[k]
 return r
def mul(A,B):
 r={}
 for a,av in A.items():
  for b,bv in B.items():
   k=tuple(x+y for x,y in zip(a,b));r[k]=(r.get(k,0)+av*bv)%3
 return {k:v for k,v in r.items() if v}
def powp(A,n):
 r=unit
 for _ in range(n):r=mul(r,A)
 return r
# 4 gens enough for PGL3(F3)
# each generator lists the image of original x y z under substitution
G=[[[1,1,0],[0,1,0],[0,0,1]],[[0,1,0],[1,0,0],[0,0,1]],[[1,0,0],[0,0,1],[0,1,0]],[[2,0,0],[0,1,0],[0,0,1]]]
def transform(g):
 L=[{tuple(1 if k==j else 0 for k in range(3)):v for j,v in enumerate(coeffs) if v} for coeffs in g]
 rows=[]
 for ex in M4:
  p=unit
  for i,n in enumerate(ex):p=mul(p,powp(L[i],n))
  rows.append([p.get(v,0) for v in M4])
 return rows
Gmat=[transform(g) for g in G]
# finite rational point list
points=[]
for a,b,c in product(range(3),repeat=3):
 if a==b==c==0:continue
 v=(a,b,c);f=next(z for z in v if z!=0);v=tuple(z*pow(f,-1,3)%3 for z in v)
 if v not in points:points.append(v)
assert len(points)==13
lines=points.copy()
def dot(a,b):return sum(x*y for x,y in zip(a,b))%3
# binary polys as coefficient vectors indexed (4-k,k), for u,s

def binmul(A,B):
 r=[0]*(len(A)+len(B)-1)
 for i,a in enumerate(A):
  for j,b in enumerate(B):r[i+j]=(r[i+j]+a*b)%3
 return r
bsqproper=[];bsqrepeat=[]
for aa,bb,cc in product(range(3),repeat=3):
 if not any([aa,bb,cc]):continue
 f=next(v for v in (aa,bb,cc) if v);aa,bb,cc=[v*pow(f,-1,3)%3 for v in (aa,bb,cc)]
 q=[aa,bb,cc];s=binmul(q,q)
 normalized=tuple(s)
 if (bb*bb-aa*cc)%3==0:
  if normalized not in bsqrepeat:bsqrepeat.append(normalized)
 else:
  if normalized not in bsqproper:bsqproper.append(normalized)
assert len(bsqproper)==9 and len(bsqrepeat)==4,(bsqproper,bsqrepeat)

restr=[]
for l in lines:
 ker=[v for v in points if dot(v,l)==0]
 assert len(ker)==4
 v,w=ker[0],ker[1]
 # independent; homogeneous point ker[0],ker[1]
 # (x,y,z) = u*v+s*w; coefficient vector for each M4
 R=[]
 for e in M4:
  a=[1];
  for coord,power in enumerate(e):
   lin=[v[coord],w[coord]]
   for _ in range(power):a=binmul(a,lin)
  assert len(a)==5
  R.append(a)
 restr.append(R)

# gradient map produce monomial products needed for rank
m4_index={m:i for i,m in enumerate(M4)}
m7_index={m:i for i,m in enumerate(M7)}
m3_index={m:i for i,m in enumerate(M3)}
# columns labelled (partial coordinate, exponent of multiplier degree4) with row S7
# precompute that for each coefficient a_m contributes to columns gradient via exponent*monomial
ranks=[]
for deriv in range(3):
 for j,mul4 in enumerate(M4):
  items=[]
  for i,exp in enumerate(M4):
   if exp[deriv]==0:continue
   new=tuple(exp[k]+mul4[k]-(k==deriv) for k in range(3))
   items.append((i,m7_index[new],exp[deriv]%3))
  ranks.append(items)
assert len(ranks)==45

def cpp_arr(name,a):
 def rec(x):return '{'+','.join(rec(z) if isinstance(z,list) else str(z) for z in x)+'}' if isinstance(x,list) else str(x)
 return 'static constexpr auto '+name+' = '+rec(a)+';\n'
# output plain flattened C array dimension if auto initializer C++ deduces nested braces? -> std::initializer_list wrong. use int dimensions
with open(Path(__file__).parent / 'tables.hpp','w') as f:
 f.write('constexpr int NGEN=4;\nconstexpr int GM[4][15][15] = '+str(Gmat).replace('[','{').replace(']','}')+';\n')
 f.write('constexpr int RESTR[13][15][5] = '+str(restr).replace('[','{').replace(']','}')+';\n')
 f.write('constexpr int PROPER[9][5] = '+str(bsqproper).replace('[','{').replace(']','}').replace('(','{').replace(')','}')+';\n')
 f.write('constexpr int HYPER[4][5] = '+str(bsqrepeat).replace('[','{').replace(']','}').replace('(','{').replace(')','}')+';\n')
 # exact map derivative multiplications generate rank dense matrix on fly easily from col lists
 f.write('constexpr int RANK_I[45][15] = '+str([[it[0] for it in col]+[-1]*(15-len(col)) for col in ranks]).replace('[','{').replace(']','}')+';\n')
 f.write('constexpr int RANK_R[45][15] = '+str([[it[1] for it in col]+[-1]*(15-len(col)) for col in ranks]).replace('[','{').replace(']','}')+';\n')
 f.write('constexpr int RANK_V[45][15] = '+str([[it[2] for it in col]+[0]*(15-len(col)) for col in ranks]).replace('[','{').replace(']','}')+';\n')
 f.write('constexpr int RANK_NUM[45] = '+str([len(col) for col in ranks]).replace('[','{').replace(']','}')+';\n')
 f.write('constexpr int POINTS[13][3] = '+str(points).replace('[','{').replace(']','}').replace('(','{').replace(')','}')+';\n')
 f.write('constexpr int LINES[13][3] = '+str(lines).replace('[','{').replace(']','}').replace('(','{').replace(')','}')+';\n')
 f.write('constexpr int MONOMS[15][3] = '+str(M4).replace('[','{').replace(']','}').replace('(','{').replace(')','}')+';\n')
print('monomials',M4)
print('proper',bsqproper,'hyper',bsqrepeat)
print('wrote hpp')
