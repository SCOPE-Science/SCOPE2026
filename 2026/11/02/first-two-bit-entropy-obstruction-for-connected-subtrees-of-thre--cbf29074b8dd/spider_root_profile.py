from functools import lru_cache
from spider_connected_verify import by_intervals
m=12
H=by_intervals(m)
n=3*m+1
cols=[sum(1<<i for i,h in enumerate(H) if h>>v&1) for v in range(n)]
full=(1<<len(H))-1
@lru_cache(None)
def can(S,k):
 if k==0:return bool(S)
 if S.bit_count()<(1<<k):return False
 for C in cols:
  yes=S&C;no=S&~C
  if yes.bit_count()<(1<<(k-1)) or no.bit_count()<(1<<(k-1)):continue
  if can(yes,k-1) and can(no,k-1):return True
 return False
def dim(S):
 d=0
 while can(S,d+1):d+=1
 return d
for j in range(0,13):
 v=0 if j==0 else j
 Y=full&cols[v];N=full&~cols[v]
 print(j,Y.bit_count(),N.bit_count(),dim(Y),dim(N), 'root_depth',1+min(dim(Y),dim(N)),flush=True)
print('states',can.cache_info())
