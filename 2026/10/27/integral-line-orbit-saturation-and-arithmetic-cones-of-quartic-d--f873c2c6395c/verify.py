import itertools, math, json, collections, time
from sympy import Matrix, ZZ, eye, gcdex
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from functools import lru_cache
st=time.monotonic()
n=6
Q=Matrix.diag(1,-1,-1,-1,-1,-1)
H=Matrix([1,0,0,0,0,0]); E=[Matrix([int(i==j) for i in range(6)]) for j in range(1,6)]
lines=E+[H-E[i]-E[j] for i in range(5) for j in range(i+1,5)]+[2*H-sum(E,Matrix.zeros(6,1))]
assert len(lines)==16 and len(set(tuple(v) for v in lines))==16
K=3*H-sum(E,Matrix.zeros(6,1))
assert all((v.T*Q*v)[0]==-1 and (K.T*Q*v)[0]==1 for v in lines)
# matrix tuple, multiplication
I=tuple(int(i==j) for i in range(6) for j in range(6))
def mul(A,B):return tuple(sum(A[6*i+k]*B[6*k+j] for k in range(6)) for i in range(6) for j in range(6))
def apply(A,v): return tuple(sum(A[6*i+k]*v[k] for k in range(6)) for i in range(6))
gens=[]
for i in range(1,5):
 P=list(I)
 for r in range(6):P[6*r+i],P[6*r+i+1]=P[6*r+i+1],P[6*r+i]
 gens.append(tuple(P))
alpha=(1,-1,-1,-1,0,0)
# A = I + alpha*(Q*alpha)^T
P=list(I)
for r in range(6):
 for c in range(6):P[6*r+c]+=alpha[r]*alpha[c]*(1 if c==0 else -1)
gens.append(tuple(P))
assert all(mul(g,g)==I for g in gens)
vecs=[tuple(v) for v in lines];idx={v:i for i,v in enumerate(vecs)}
for g in gens:assert all(apply(g,v) in idx for v in vecs)
# enumerate W(D5)
group={I}; todo=[I]
for A in todo:
 for s in gens:
  B=mul(A,s)
  if B not in group:group.add(B);todo.append(B)
assert len(group)==1920, len(group)
print('GROUP',len(group),'seconds',round(time.monotonic()-st,2), flush=True)
# classes
remaining=set(group);clss=[]
while remaining:
 seed=next(iter(remaining)); cc={seed};q=[seed]
 for A in q:
  for s in gens:
   B=mul(mul(s,A),s)
   if B not in cc:cc.add(B);q.append(B)
 remaining-=cc
 clss.append((seed,len(cc)))
print('CLASSES',len(clss),'sizes',sorted(x[1] for x in clss),'seconds',round(time.monotonic()-st,2), flush=True)

# Integer kernel of A with unimodular column operations
def kernel_Z(A):
 mat=[list(map(int,row)) for row in A.tolist()]
 m=len(mat);ncols=len(mat[0]); U=[[int(i==j) for j in range(ncols)] for i in range(ncols)]
 def colcomb(p,j,a,b,c,d):
  for rows in [mat,U]:
   for row in rows:
    x,y=row[p],row[j]
    row[p]=a*x+b*y
    row[j]=c*x+d*y
 pivot=0
 for i in range(m):
  nz=next((j for j in range(pivot,ncols) if mat[i][j]!=0),None)
  if nz is None:continue
  if nz!=pivot:colcomb(pivot,nz,0,1,1,0)
  for j in range(pivot+1,ncols):
   if not mat[i][j]:continue
   a,b=mat[i][pivot],mat[i][j]
   u,v,g=map(int,gcdex(a,b))
   if g<0:u,v,g=-u,-v,-g
   colcomb(pivot,j,u,v,-b//g,a//g)
  assert all(mat[i][j]==0 for j in range(pivot+1,ncols))
  pivot+=1
 return Matrix(U)[:,pivot:],Matrix(mat)

def order(A):
 T=I
 for i in range(1,100):
  T=mul(T,A)
  if T==I:return i
 raise Exception

def cycles(A):
 perm=[idx[apply(A,v)] for v in vecs]; seen=set();out=[]
 for i in range(16):
  if i in seen:continue
  cyc=[];j=i
  while j not in seen:
   seen.add(j);cyc.append(j);j=perm[j]
  out.append(cyc)
 assert sum(len(c) for c in out)==16
 return sorted(out,key=lambda x:(len(x),x))

rows=[]
for ci,(A,cs) in enumerate(clss):
 M=Matrix(6,6,A); invbasis,rr=kernel_Z(M-eye(6));r=invbasis.cols
 assert (M-eye(6))*invbasis==Matrix.zeros(6,r)
 assert all(x==int(x) for x in invbasis)
 # check primitive via gcd minors for L
 assert hermite_normal_form(invbasis.T).rows==r
 orbits=cycles(A)
 traces=[sum((Matrix(vecs[j]) for j in cyc),Matrix.zeros(6,1)) for cyc in orbits]
 coords=[]
 for t in traces:
  sol=invbasis.gauss_jordan_solve(t)[0]
  assert all(int(x)==x for x in sol),('non-integral',ci,sol)
  coords.append(sol)
 TT=Matrix.hstack(*coords)
 HM=hermite_normal_form(TT)
 assert HM.shape==(r,r),(ci,r,HM.shape)
 index=abs(int(HM.det()))
 gram=invbasis.T*Q*invbasis
 snf=smith_normal_form(gram,domain=ZZ)
 diag=tuple(abs(int(snf[i,i])) for i in range(r))
 roots=[tuple(map(int,c)) for c in coords]
 rows.append({'class_idx':ci,'size':cs,'order':order(A),'pic_rank':r,'orbit_lengths':sorted(len(c) for c in orbits), 'orbits':orbits,'trace_index':index,'disc':int(gram.det()),'disc_snf':diag,'charpoly':str(M.charpoly().as_expr()), 'matrix':list(A), 'invariant_basis':[[int(x) for x in y] for y in invbasis.tolist()],'trace_coords':roots})
# Cone computations: nef rays are intersections of rank-1 independent supporting hyperplanes
from functools import reduce
from math import gcd

def primitive(v):
 a=[int(x) for x in v]; gg=reduce(gcd,a,0);return tuple(x//gg for x in a)

def cone_dual_rays(ineq):
 r=len(ineq[0]); out=set()
 if r==1:
  vv=1 if any(row[0]>0 for row in ineq) else -1
  return {(vv,)}
 for comb in itertools.combinations(ineq,r-1):
  B=Matrix(comb)
  if B.rank()!=r-1:continue
  v=B.nullspace()[0]
  l=math.lcm(*(x.q for x in v))
  w=primitive([l*x for x in v])
  test=[sum(x*y for x,y in zip(row,w)) for row in ineq]
  if min(test)>=0:out.add(w)
  elif max(test)<=0:out.add(tuple(-x for x in w))
 return out

for row in rows:
 r=row['pic_rank'];G=Matrix(row['invariant_basis']).T*Q*Matrix(row['invariant_basis'])
 coords=[Matrix(x) for x in row['trace_coords']]
 inequalities=set(tuple(G*c) for c in coords)
 nef=cone_dual_rays(sorted(inequalities))
 row['nef_ray_count']=len(nef)
 row['nef_rays']=[list(v) for v in sorted(nef)]
 # An effective ray is dual to a facet of the nef cone. A vector is effective-extremal
 # exactly when its zero face in nef cone has full dimension r-1.
 nmat=Matrix.hstack(*(Matrix(v) for v in nef))
 effective=[]
 for c in coords:
  vals=[int((c.T*G*Matrix(v))[0]) for v in nef]
  zeros=[Matrix(v) for v,val in zip(nef,vals) if val==0]
  if r==1 or (zeros and Matrix.hstack(*zeros).rank()==r-1):effective.append(tuple(c))
 row['effective_ray_count']=len(set(primitive(v) for v in effective))
 # finite generated cones are pointed: invariant hyperplane class positive on each line trace
 assert row['nef_ray_count']>0
 row['trace_quotient_snf']=tuple(abs(int(smith_normal_form(hermite_normal_form(Matrix.hstack(*coords)),domain=ZZ)[i,i])) for i in range(r))
print('CALC_DONE',round(time.monotonic()-st,2),flush=True)
for row in sorted(rows,key=lambda x:(x['pic_rank'],x['order'],x['orbit_lengths'],x['trace_index'])):
 print(row['class_idx'], 'size',row['size'],'ord',row['order'],'rho',row['pic_rank'],'orbits',row['orbit_lengths'],'index',row['trace_index'],'disc',row['disc'],'snf',row['disc_snf'],'tracequot',row['trace_quotient_snf'],'cones',row['effective_ray_count'],row['nef_ray_count'])

EXPECTED={'(20, 4, 1, (4, 4, 4, 4))': [1, 4, [4], [1], 1, 1], '(240, 8, 1, (8, 8))': [2, 4, [4], [2], 1, 1], '(160, 12, 1, (4, 12))': [1, 4, [4], [1], 1, 1], '(5, 2, 2, (2, 2, 2, 2, 2, 2, 2, 2))': [1, -4, [2, 2], [1, 1], 2, 2], '(60, 4, 2, (4, 4, 4, 4))': [4, -4, [2, 2], [2, 2], 2, 2], '(120, 4, 2, (4, 4, 4, 4))': [2, -8, [2, 4], [1, 2], 2, 2], '(384, 5, 2, (1, 5, 5, 5))': [1, -5, [1, 5], [1, 1], 2, 2], '(80, 6, 2, (2, 2, 6, 6))': [1, -12, [2, 6], [1, 1], 2, 2], '(160, 6, 2, (2, 2, 6, 6))': [1, -4, [2, 2], [1, 1], 2, 2], '(60, 2, 3, (2, 2, 2, 2, 2, 2, 2, 2))': [1, 8, [2, 2, 2], [1, 1, 1], 4, 4], '(60, 4, 3, (4, 4, 4, 4))': [16, 4, [1, 1, 4], [1, 4, 4], 4, 4], '(240, 4, 3, (1, 1, 2, 4, 4, 4))': [2, 4, [1, 1, 4], [1, 1, 2], 4, 4], '(160, 6, 3, (1, 1, 2, 3, 3, 6))': [1, 6, [1, 1, 6], [1, 1, 1], 5, 5], '(10, 2, 4, (2, 2, 2, 2, 2, 2, 2, 2))': [4, -4, [1, 1, 2, 2], [1, 1, 2, 2], 8, 6], '(60, 2, 4, (1, 1, 1, 1, 2, 2, 2, 2, 2, 2))': [1, -4, [1, 1, 2, 2], [1, 1, 1, 1], 8, 10], '(80, 3, 4, (1, 1, 1, 1, 3, 3, 3, 3))': [1, -3, [1, 1, 1, 3], [1, 1, 1, 1], 8, 8], '(20, 2, 5, (1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2))': [1, 2, [1, 1, 1, 1, 2], [1, 1, 1, 1, 1], 12, 16], '(1, 1, 6, (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))': [1, -1, [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], 16, 26]}

ACTUAL={str((r["size"],r["order"],r["pic_rank"],tuple(r["orbit_lengths"]))):[r["trace_index"],r["disc"],list(r["disc_snf"]),list(r["trace_quotient_snf"]),r["effective_ray_count"],r["nef_ray_count"]] for r in rows}
assert len(ACTUAL)==18 and ACTUAL==EXPECTED
assert sum(r["size"] for r in rows)==1920
from collections import Counter
assert Counter(r["trace_index"] for r in rows)=={1:12,2:3,4:2,16:1}
print("VERIFY_OK: 1920 Weyl elements; 18 classes; exact Picard, trace Smith and 18 effective/nef cone ray profiles")
