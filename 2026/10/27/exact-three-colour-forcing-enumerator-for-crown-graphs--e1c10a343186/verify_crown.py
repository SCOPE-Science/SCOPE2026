from itertools import product
from collections import Counter
from math import comb

def brute(n):
 N=2*n;q=3; nei=[[] for _ in range(N)]
 for i in range(n):
  for j in range(n):
   if i!=j:
    nei[i].append(n+j);nei[n+j].append(i)
 out=Counter();classes=Counter()
 for initial in product(range(4),repeat=N):
  vals=list(initial)
  if any(vals[v]==vals[w]!=3 for v in range(N) for w in nei[v]):continue
  while 3 in vals:
   chosen=None
   for v in range(N):
    if vals[v]!=3: continue
    seen={vals[w] for w in nei[v] if vals[w]!=3}
    if len(seen)==2:
     chosen=(v,3-sum(seen));break
   if chosen is None:break
   vals[chosen[0]]=chosen[1]
  if 3 in vals:continue
  if any(vals[v]==vals[w] for v in range(N) for w in nei[v]):continue
  out[N-initial.count(3)]+=1
  classes[tuple(vals)]+=1
 return out,classes

def formula(n):
 out=Counter({2*n:6})
 # 2 disjoint bicrom-side types, palette choices 3
 for k in range(n+1):
  out[n+k]+=6*(2**n-2-2*n)*comb(n,k)
 for k in range(n):
  out[n+1+k]+=12*n*comb(n-1,k)
 # shared matched-pair type, n>=4
 for k in range(1,2*n-1):
  out[2+k]+=6*n*comb(2*n-2,k)
 return +out

if __name__=='__main__':
 for n in (4,5):
  computed,full=brute(n)
  expected=formula(n)
  assert computed==expected,(n,computed,expected)
  assert len(full)==6*(2**n+n-1),(n,len(full))
  assert computed[3]==12*n*(n-1)
 boundary,_=brute(3)
 assert boundary!=formula(3)
 assert sum(boundary.values())>0
 print('VERIFY_OK exact_cases=2 checked_assignments=1114112 matching_polynomials=True boundary_case_n3=True')
