"""Independent count of edge colorings via disjoint perfect matchings."""
from collections import Counter
D=(0,1,3,9)
N=13
A=[tuple((i+d)%13 for d in D)for i in range(N)]
assert len(set(tuple(sorted((i+d)%13 for d in D)) for i in range(N)))==N
assert all(len(set(A[i])&set(A[j]))==1 for i in range(N)for j in range(i))
matchings=[]
def gen(i,used,tuple_):
 if i==N:
  matchings.append(tuple_)
  return
 for p in A[i]:
  if not used&(1<<p):gen(i+1,used|1<<p,tuple_+(p,))
gen(0,0,())
print('perfect_matchings',len(matchings))
C=Counter(); total=0
for k,x in enumerate(matchings):
 for y in matchings:
  if any(x[i]==y[i] for i in range(N)):continue
  # complement has degree two. connected components in bipartite leftover graph.
  inv=([0]*N)
  for i in range(N):inv[x[i]]=i
  inv2=([0]*N)
  for i in range(N):inv2[y[i]]=i
  rem=[tuple(p for p in A[i] if p!=x[i] and p!=y[i])for i in range(N)]
  assert all(len(a)==2 for a in rem)
  seen=0;cycs=0
  for start in range(N):
   if seen>>start&1:continue
   cycs+=1
   q=[start];seen|=1<<start
   for l in q:
    for p in rem[l]:
     for z in range(N):
      if z!=l and p in rem[z] and not(seen>>z&1):seen|=1<<z;q.append(z)
  total+=2**cycs
  C[cycs]+=1
print('disjoint_pair_cycles',dict(C),'total_labeled_edge_colorings',total)
assert total==1935360
print('VERIFY_MATCHINGS_OK')
