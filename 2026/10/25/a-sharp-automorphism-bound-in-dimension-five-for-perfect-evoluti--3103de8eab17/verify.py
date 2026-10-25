from itertools import permutations, combinations
from collections import Counter
N=5
ALL=list(permutations(range(N)))
def mk_mask(edges):
 m=0
 for i,j in edges:m|=1 << (5*i+j)
 return m

# Order-3 root patterns: nontrivial labels a and -a, others zero.
allowed=set()
for k in (1,2):
 for A in combinations(range(N),k):
  for B in combinations([i for i in range(N) if i not in A],k):
   Z=[i for i in range(N) if i not in A and i not in B]
   E=mk_mask([(i,j) for i in A for j in B]+[(i,j) for i in B for j in A]+[(i,j) for i in Z for j in Z])
   allowed.add(E)
# Order 5: a 4-cycle and one fixed vertex
for z in range(N):
 for c in permutations([i for i in range(N) if i!=z]):
  allowed.add(mk_mask([(c[i],c[(i+1)%4]) for i in range(4)]+[(z,z)]))
# Order 7: a 3-cycle and 2 trivial vertices
for T in combinations(range(N),3):
 Z=[i for i in range(N) if i not in T]
 for c in permutations(T):
  allowed.add(mk_mask([(c[i],c[(i+1)%3]) for i in range(3)]+[(i,j) for i in Z for j in Z]))
# Order 31: all vertices one 5-cycle
for c in ALL:
 allowed.add(mk_mask([(c[i],c[(i+1)%5]) for i in range(5)]))
print('distinct allowed edge sets',len(allowed))

candidates=set()
for bound in allowed:
 sub=bound
 while sub:
  candidates.add(sub)
  sub=(sub-1)&bound
print('nonempty candidate masks',len(candidates))
# All candidate supports contain a perfect matching iff at least one of the 120 matching masks subset.
matching_masks=[mk_mask([(i,p[i]) for i in range(N)]) for p in ALL]
candidates={g for g in candidates if any(g&mm==mm for mm in matching_masks)}
print('candidate perfect supports',len(candidates))

# For a graph with a perfect matching, torsion primes are 3,5,7,31 and 3-primary has exponent 3.
# Kernel size modulo p gives exact Sylow p order.
def kernel_dim(edges,p):
 rows=[]
 for i,j in edges:
  a=[0]*N;a[j]=1;a[i]=(a[i]-2)%p
  rows.append(a)
 rank=0
 for col in range(N):
  piv=next((k for k in range(rank,len(rows)) if rows[k][col]%p),None)
  if piv is None:continue
  rows[rank],rows[piv]=rows[piv],rows[rank]
  q=pow(rows[rank][col],-1,p)
  for c in range(col,N):rows[rank][c]=rows[rank][c]*q%p
  for k in range(rank+1,len(rows)):
   q=rows[k][col]
   if q:
    for c in range(col,N):rows[k][c]=(rows[k][c]-q*rows[rank][c])%p
  rank+=1
  if rank==N:break
 return N-rank

# Faster precomputed edge perm map.
permed=[[5*p[i]+p[j] for i in range(N) for j in range(N)] for p in ALL]
def autsize(g,edges):
 size=0
 for tab in permed:
  if all(g&(1<<tab[t]) for t in edges) and all((g&(1<<tab[t])) ==0 for t in range(N*N) if not (g>>t)&1):
   size+=1
 return size

from time import monotonic
start=monotonic()
maxU=0; maxgraphs=[];hist=Counter(); cases=Counter()
for g in candidates:
 edges=[(t//N,t%N) for t in range(N*N) if (g>>t)&1]
 d=1
 for p in (3,5,7,31):
  r=kernel_dim(edges,p)
  d*=p**r
 if d==1:continue
 size=autsize(g,[5*i+j for i,j in edges])
 u=d*size
 if u>maxU:maxU=u;maxgraphs=[g]
 elif u==maxU:maxgraphs.append(g)
 cases[(d,size)]+=1
 hist[u]+=1
print('nontrivial diagonal supports',sum(cases.values()),'max product',maxU,'max graph count',len(maxgraphs),'elapsed',round(monotonic()-start,3))
print('maximizing masks',maxgraphs[:30]);print('most common cases',cases.most_common(20))
assert maxU==155
assert len(maxgraphs)==24
print('VERIFY_OK')
