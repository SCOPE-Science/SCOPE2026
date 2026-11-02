from collections import Counter
from math import comb

def direct(n):
 pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
 by=Counter(); total=0
 for bits in range(1<<len(pairs)):
  ins=[0]*n; outs=[0]*n
  for z,(i,j) in enumerate(pairs):
   if bits>>z&1: outs[i]|=1<<j; ins[j]|=1<<i
  if any(ins[i] and outs[i] for i in range(n)):continue
  total+=1
  S=[i for i in range(n) if outs[i]]
  T=[j for j in range(n) if ins[j]]
  iso=n-len(S)-len(T)
  inv=sum(j<i for i in S for j in T)
  if not iso:
   counts=[sum(t<i for t in T) for i in S]
   lam=list(reversed(counts))
   assert lam==sorted(lam,reverse=True)
   recovered=[i+r for i,r in enumerate(reversed(lam))]
   assert recovered==S
   assert sum(lam)==inv
  by[(len(S),inv,iso)]+=1
 return total,by

def recurrence(n):
 row=[1] # T(0,0)=1
 # T(n,k) = (2^k-1) T(n-1,k) + T(n-1,k-1); initial at n=1 k=1=1
 for m in range(1,n+1):
  nxt=[0]*(m+1)
  for k in range(1,m+1):
   nxt[k]=(2**k-1)*(row[k] if k<len(row) else 0)+(row[k-1] if k-1<len(row) else 0)
  row=nxt
 return sum(row)
for n in range(1,7):
 tot, b=direct(n)
 rec=recurrence(n)
 print(n,tot,rec,'isolates',sum(c for (_,_,u),c in b.items() if u>0))
 assert tot==rec,(n,tot,rec)
print('VERIFY_OK')
