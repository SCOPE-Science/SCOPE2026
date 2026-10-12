from collections import Counter
from math import comb
from itertools import product

def pformula(n):
 d=Counter()
 for k in range(1,n+1):
  for a in range(3):
   for b in range(3):
    t=n-a-b-1-3*(k-1)
    if 0<=t<=k-1:d[k]+=comb(k-1,t)
 if n==1:d[0]=1
 return dict(d)
def cformula(n):
 d=Counter()
 for b in range(n//4+1):
  t=n-4*b
  if t>=0 and t%3==0:
   a=t//3;k=a+b
   assert k>=1
   d[k]+=n*comb(k,b)//k
 return dict(d)
def adjacency(kind,n):
 A=[set() for _ in range(n)]
 E=[(i,i+1) for i in range(n-1)] if kind=='P' else [(i,(i+1)%n) for i in range(n)]
 for u,v in E:
  A[u].add(v);A[v].add(u)
 return A

def direct(A):
 n=len(A);out=Counter()
 for mask in range(1<<n):
  selected=[v for v in range(n) if mask>>v&1]
  dominated=0;good=True
  for v in selected:
   nb=(1<<v)|sum(1<<u for u in A[v])
   if dominated&nb:good=False;break
   dominated|=nb
  if not good:continue
  undominated=((1<<n)-1)^dominated
  if any(undominated>>v&1 and any(undominated>>u&1 for u in A[v]) for v in range(n)):
   continue
  out[len(selected)]+=1
 return dict(out)

def multiply(a,b):
 c=Counter()
 for i,x in a.items():
  for j,y in b.items():c[i+j]+=x*y
 return dict(c)

check_count=0;examined=0
for n in range(1,18):
 for typ in ('P','C'):
  if typ=='C' and n<3:continue
  A=adjacency(typ,n)
  exp=pformula(n) if typ=='P' else cformula(n)
  observed=direct(A)
  assert observed==exp,(typ,n,exp,observed)
  check_count+=1;examined+=2**n
# All unordered disjoint-union component multisets of combined order <=9
comp=[('P',i) for i in range(1,10)]+[('C',i) for i in range(3,10)]
comp.sort(key=lambda x:(x[1],x[0]))
def verify_unions(components,A,expected):
 global check_count,examined
 if components:
  observed=direct(A)
  assert observed==expected,(components,expected,observed)
  check_count+=1;examined+=2**len(A)
 if len(A)>=9:return
 start=comp.index(components[-1]) if components else 0
 for ix in range(start,len(comp)):
  typ,n=comp[ix]
  if len(A)+n>9:break
  sub=adjacency(typ,n);offset=len(A)
  A1=A+[set(offset+u for u in nb) for nb in sub]
  expected1=multiply(expected,pformula(n) if typ=='P' else cformula(n))
  verify_unions(components+[(typ,n)],A1,expected1)
verify_unions([],[],{0:1})
print(f'ALL CHECKS PASSED; graphs_checked={check_count}; vertex_subsets_examined={examined}; connected_paths_and_cycles_n=1..17; all_multicomponent_profiles_total_order<=9')
