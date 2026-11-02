from collections import Counter
import time

def counts(n):
 N=3**n
 p3=[3**i for i in range(n)]
 # Unique labelled perfect matching: paired labels 0-1,2-3,...
 def decode(a):
  z=[]
  for i in range(n):z.append(a%3);a//=3
  return z
 def encode(z):return sum(p3[i]*z[i] for i in range(n))
 def update_full(z):
  return [2 if x==1 else 0 if x==2 else int(any(z[j]==1 for j in range(n) if j!=i and j!=(i^1))) for i,x in enumerate(z)]
 nexts=[0]*N
 for a in range(N):
  z=decode(a);nexts[a]=encode(update_full(z))
 visited=bytearray(N);periods=Counter();sample={}; first_periodic=0; maxT=0
 # exhaustive functional graph classification plus counts of actual periodic vertices
 cycle_states=Counter()
 for a in range(N):
  if visited[a]:continue
  seq=[];local={};current=a
  while not visited[current] and current not in local:
   local[current]=len(seq);seq.append(current);current=nexts[current]
  if current in local:
   start=local[current]; per=len(seq)-start
   periods[per]+=1;cycle_states[per]+=per
   sample.setdefault(per, tuple(decode(s) for s in seq[start:start+min(per,6)]))
  for j in seq:visited[j]=1
 q=(3**(n-1)-2**n-n*2**(n-2)+n+1) if n>=6 else None
 expected=Counter({1:1,3:q}) if n>=6 else Counter({1:1,4:2}) if n==4 else Counter({1:1})
 assert periods==expected,(n,periods,expected)
 # Independent algebraic rotor characterization at EVERY state
 rotor=0
 for a in range(N):
  z=decode(a)
  pure=(all(z.count(c)>0 for c in range(3)) and all(not (z.count(c)==1 and z[z.index(c)^1]==(c-1)%3) for c in range(3)))
  if n>=6 and pure:
   assert nexts[nexts[nexts[a]]]==a,(n,a)
   rotor+=1
 if n>=6: assert rotor==3*q,(n,rotor,3*q)
 return n,N,dict(periods),rotor, sample

if __name__=='__main__':
 start=time.monotonic()
 for n in [2,4,6,8,10,12]:
  n,N,periods,rotor,sample=counts(n)
  print(f'n={n} states={N} primitive_orbits={periods} rotor_states={rotor}',flush=True)
 print(f'VERIFY_OK seconds={time.monotonic()-start:.2f}',flush=True)
