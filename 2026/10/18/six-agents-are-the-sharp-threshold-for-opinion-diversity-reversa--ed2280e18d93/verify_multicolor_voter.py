"""Exact verification of the sharp six-vertex two-vs-three-opinion voter edge reversal.
All calculations use Python standard-library fractions, with complete finite graph enumeration.
"""
from itertools import combinations, permutations
from fractions import Fraction as F
from functools import lru_cache
from time import monotonic

def canonical(p):
 d={};a=[]
 for z in p:
  if z not in d:d[z]=len(d)
  a.append(d[z])
 return tuple(a)
@lru_cache(None)
def partstates(n,q):
 a=[]
 def rec(st,k):
  if len(st)==n:
   if k>1:a.append(tuple(st))
   return
  for z in range(min(k+1,q)):
   st.append(z);rec(st,max(k,z+1));st.pop()
 rec([0],1)
 return a

def solve_frac(A,b):
 n=len(b)
 for j in range(n):
  pi=next((i for i in range(j,n) if A[i].get(j,F(0))),None)
  if pi is None:raise RuntimeError('Singular')
  if pi!=j:A[j],A[pi]=A[pi],A[j];b[j],b[pi]=b[pi],b[j]
  pivot=A[j][j]
  # eliminate below; no need normalize rows until backsolve
  for i in range(j+1,n):
   aij=A[i].pop(j,None)
   if aij is None:continue
   fac=aij/pivot
   for k,val in A[j].items():
    if k<=j:continue
    res=A[i].get(k,F(0))-fac*val
    if res:A[i][k]=res
    else:A[i].pop(k,None)
   b[i]-=fac*b[j]
 x=[F(0)]*n
 for i in range(n-1,-1,-1):
  x[i]=(b[i]-sum(val*x[j] for j,val in A[i].items() if j>i))/A[i][i]
 return x

@lru_cache(maxsize=None)
def avg(n,E,q):
 nbr=[[] for _ in range(n)]
 for a,b in E:nbr[a].append(b);nbr[b].append(a)
 states=partstates(n,q);index={s:i for i,s in enumerate(states)};N=len(states)
 rows=[{i:F(1)} for i in range(N)];rhs=[F(1)]*N
 for i,s in enumerate(states):
  for v in range(n):
   for w in nbr[v]:
    t=list(s);t[v]=t[w];t=canonical(t)
    j=index.get(t)
    if j is None:continue
    f=F(1,n*len(nbr[v]));val=rows[i].get(j,F(0))-f
    if val:rows[i][j]=val
    else:rows[i].pop(j,None)
 x=solve_frac(rows,rhs)
 z=F(0)
 for s,t in zip(states,x):
  k=max(s)+1;ways=1
  for j in range(k):ways*=q-j
  z+=F(ways,q**n)*t
 return z


def enumerate_connected_unlabeled(n):
 pairs=list(combinations(range(n),2));emap={e:i for i,e in enumerate(pairs)};N=len(pairs)
 perms=list(permutations(range(n)))
 # represent each relabelled graph as bit mask, canonical pick minimal
 seen=set();ret=[]
 for mask in range(1<<N):
  E=tuple(e for i,e in enumerate(pairs) if (mask>>i)&1)
  nbr=[set() for _ in range(n)]
  for u,v in E:nbr[u].add(v);nbr[v].add(u)
  comp={0};todo=[0]
  for v in todo:
   for w in nbr[v]:
    if w not in comp:comp.add(w);todo.append(w)
  if len(comp)!=n:continue
  if mask in seen:continue
  ret.append(E)
  for perm in perms:
   m=0
   for u,v in E:
    a,b=sorted((perm[u],perm[v]));m|=1<<emap[a,b]
   seen.add(m)
 return ret

def verify():
 assert len(enumerate_connected_unlabeled(3))==2
 assert len(enumerate_connected_unlabeled(4))==6
 assert len(enumerate_connected_unlabeled(5))==21
 C={};tests=0;zero=0;positive=0;negative=0
 for n in range(2,6):
  for E in enumerate_connected_unlabeled(n):
   for u,v in combinations(range(n),2):
    if (u,v) in E:continue
    H=tuple(sorted(E+((u,v),)))
    d2=avg(n,E,2)-avg(n,H,2)
    d3=avg(n,E,3)-avg(n,H,3)
    assert d2*d3>=0, (n,E,(u,v),d2,d3)
    tests+=1
    if d2==0 or d3==0:
     assert d2==d3==0
     zero+=1
    elif d2>0:positive+=1
    else:negative+=1
    C[n]=C.get(n,0)+1
 E=((0,2),(0,3),(0,4),(0,5),(1,2),(1,3));H=tuple(sorted(E+((1,4),)))
 d2=avg(6,H,2)-avg(6,E,2)
 d3=avg(6,H,3)-avg(6,E,3)
 assert d2>0 and d3<0
 print('VERIFIED',{'n_to_5_graph_edits':C,'tests':tests,'zero':zero,'positive_old_minus_new':positive,'negative_old_minus_new':negative})
 print('WITNESS 2',repr(d2));print('WITNESS 3',repr(d3))

if __name__=='__main__':
 verify()
