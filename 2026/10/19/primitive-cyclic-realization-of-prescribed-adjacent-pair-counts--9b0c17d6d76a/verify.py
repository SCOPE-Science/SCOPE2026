from collections import defaultdict
from itertools import product
from math import comb, factorial

def prim(w):
 n=len(w)
 return all(w!=w[:d]*(n//d) for d in range(1,n) if n%d==0)

def profile(w,q):
 m=[0]*(q*q)
 for i,a in enumerate(w):m[a*q+w[(i+1)%len(w)]]+=1
 return tuple(m)

def construct(m,q):
 A=[list(m[i*q:(i+1)*q]) for i in range(q)]; n=sum(m)
 if n==0:raise ValueError('empty')
 v=next(i for i in range(q) if sum(A[i])>0)
 stack=[v]; circuit=[]
 while stack:
  x=stack[-1]
  try:y=next(y for y in range(q) if A[x][y]>0)
  except StopIteration:circuit.append(stack.pop()); continue
  A[x][y]-=1; stack.append(y)
 circuit=circuit[::-1]
 assert len(circuit)==n+1 and circuit[0]==circuit[-1]==v
 E=[]; start=0
 for i in range(1,len(circuit)):
  if circuit[i]==v:
   E.append(tuple(circuit[start:i+1]));start=i
 assert len(E)>0 and sum(len(x)-1 for x in E)==n
 # sort whole excursions lexicographically, which makes every type occur as one run
 E.sort()
 seq=[x for e in E for x in e[:-1]]
 assert len(seq)==n and profile(seq,q)==m
 return tuple(seq)

def exceptional(m,q):
 n=sum(m)
 a=[list(m[i*q:(i+1)*q]) for i in range(q)]
 active=[i for i in range(q) if sum(a[i])>0]
 if not active:return False
 if any(sum(a[i][j]>0 for j in range(q))!=1 for i in active):return False
 v=active[0]; x=v; cycle=[]
 while x not in cycle:
  cycle.append(x); x=next(j for j in range(q) if a[x][j])
 if x!=v or len(cycle)!=len(active):return False
 r=a[cycle[0]][cycle[1%len(cycle)]]
 return r>=2

for q,maxn in [(1,8),(2,11),(3,10),(4,8)]:
 for n in range(1,maxn+1):
  profiles={}; count=0
  for w in product(range(q),repeat=n):
   p=profile(w,q)
   if p not in profiles:profiles[p]=False
   if prim(w):profiles[p]=True
   count+=1
  fails=0; built=0
  for m,primitive_possible in profiles.items():
   witness=construct(m,q)
   exp=exceptional(m,q)
   assert (not prim(witness))==exp,(q,n,m,witness,exp)
   assert (not primitive_possible)==exp,(q,n,m,primitive_possible,exp)
   fails+=exp; built+=1
  expected=sum(comb(q,d)*factorial(d-1) for d in range(1,min(q,n-1)+1) if n%d==0)
  assert fails==expected,(q,n,fails,expected)
  print(f'q={q} n={n} strings={count} profiles={built} exceptional={fails}')
print('PASS')
