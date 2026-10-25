from itertools import combinations
from collections import Counter
from math import comb

def H(p):
 return sum((-1)**(p-i)*comb(p,i)*2**(2**i-1) for i in range(p+1))

def check(n):
 W=range(1,1<<n);w=list(W);N=len(w); counts=Counter(); allmask=(1<<n)-1
 for familymask in range(1<<N):
  P=0; Q=0;A=set()
  for i,S in enumerate(w):
   if familymask & (1<<i): P|=S;A.add(S)
   else: Q|=S
  box=tuple(S for S in w if all((S&T)==0 or T in A for T in w))
  dia=tuple(S for S in w if any((S&T)!=0 and T in A for T in w))
  expbox=tuple(S for S in w if not S & Q)
  expdia=tuple(S for S in w if S & P)
  assert (box,dia)==(expbox,expdia), ('operation',n,familymask)
  assert P==allmask or Q==allmask,('support',n,familymask)
  counts[(P,Q)] +=1
 expected={}
 for s in range(1<<n):
  if s!=allmask:expected[(s,allmask)]=H(s.bit_count());expected[(allmask,s)]=H(s.bit_count())
 expected[(allmask,allmask)]=2**N-2*sum(comb(n,p)*H(p) for p in range(n))
 assert counts=={k:v for k,v in expected.items() if v}, ('fibers',n,counts,expected)
 print('n',n,'valuations',2**N,'fiber_count',len(counts),'central',counts.get((allmask,allmask),0),'exception',2**N-counts.get((allmask,allmask),0),'max_proper',H(n-1))

for n in (1,2,3,4): check(n)

print("ALL_CHECKS_OK")
