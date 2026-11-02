from itertools import product

def vals(a,b,S):
 return (sum(a[i] for i in S),sum(b[i] for i in range(len(a)) if i not in S))
def ef1(a,b,S):
 T=set(range(len(a)))-set(S)
 return (sum(a[i] for i in S)>=sum(a[i] for i in T)-(max([a[i] for i in T],default=0)) and sum(b[i] for i in T)>=sum(b[i] for i in S)-max([b[i] for i in S],default=0))
def po(a,b,S):
 v=vals(a,b,S)
 for mask in range(1<<len(a)):
  t={i for i in range(len(a)) if mask>>i&1}; w=vals(a,b,t)
  if w[0]>=v[0] and w[1]>=v[1] and w!=v: return False
 return True
def connected(n,S):
 T=set(range(n))-set(S)
 return all(not x or max(x)-min(x)+1==len(x) for x in (S,T))
count=0
for n in (1,2,3):
 for z in product(range(1,5),repeat=2*n):
  a=z[:n];b=z[n:]
  if not any(ef1(a,b,S) and po(a,b,S) and connected(n,S) for m in range(1<<n) for S in [{i for i in range(n) if m>>i&1}]):raise AssertionError(('positive',n,z))
  count+=1
a=(1,1,1,1);b=(1,2,2,1)
assert not any(ef1(a,b,S) and po(a,b,S) and connected(4,S) for m in range(1<<4) for S in [{i for i in range(4) if m>>i&1}])
print('VERIFY_OK positive_profiles='+str(count)+' four_item_witness=(1,1,1,1);(1,2,2,1)')
